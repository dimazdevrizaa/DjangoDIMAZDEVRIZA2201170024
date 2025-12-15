from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import MahasiswaForm
from .models import Mahasiswa
import json

@login_required(login_url='/admin/login/')
@never_cache
def input_mahasiswa(request):
    pesan = None
    if request.method == 'POST':
        form = MahasiswaForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                form.save()
            return redirect('input_mahasiswa')  # Redirect after POST
    else:
        form = MahasiswaForm()

    mahasiswa = Mahasiswa.objects.all().order_by('id')
    
    # Search and Filter
    search_query = request.GET.get('q', '')
    jurusan_filter = request.GET.get('jurusan', '')

    if search_query:
        from django.db.models import Q
        mahasiswa = mahasiswa.filter(Q(nama__icontains=search_query) | Q(npm__icontains=search_query))
    
    if jurusan_filter:
        mahasiswa = mahasiswa.filter(jurusan=jurusan_filter)

    return render(request, 'mahasiswa/input.html', {
        'form': form,
        'mahasiswa': mahasiswa,
        'pesan': pesan,
        'search_query': search_query,
        'jurusan_filter': jurusan_filter,
    })

@login_required(login_url='/admin/login/')
@require_POST
@never_cache
def mahasiswa_delete(request, pk):
    try:
        with transaction.atomic():
            m = Mahasiswa.objects.get(pk=pk)
            m.delete()
        return JsonResponse({'success': True})
    except Mahasiswa.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Data tidak ditemukan'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

@login_required(login_url='/admin/login/')
@require_POST
@never_cache
def mahasiswa_update(request, pk):
    try:
        data = json.loads(request.body)
        mahasiswa = get_object_or_404(Mahasiswa, pk=pk)
        
        # Update fields
        mahasiswa.nama = data.get('nama', mahasiswa.nama)
        mahasiswa.npm = data.get('npm', mahasiswa.npm)
        mahasiswa.email = data.get('email', mahasiswa.email)
        mahasiswa.no_hp = data.get('no_hp', mahasiswa.no_hp)
        mahasiswa.jurusan = data.get('jurusan', mahasiswa.jurusan)
        mahasiswa.alamat = data.get('alamat', mahasiswa.alamat)
        
        # Validate and save
        mahasiswa.full_clean()
        mahasiswa.save()
        
        return JsonResponse({
            'success': True,
            'message': 'Data berhasil diupdate'
        })
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid JSON format'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)
