
import os

path = 'd:/FrameworkDjango/project1/mahasiswa/templates/mahasiswa/input.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the targets to replace (carefully matching the split lines)
target1 = """<option value="Teknologi Informasi" {% if jurusan_filter=='Teknologi Informasi'
                                            %}selected{% endif %}>Teknologi Informasi</option>"""
val1 = """<option value="Teknologi Informasi" {% if jurusan_filter == 'Teknologi Informasi' %}selected{% endif %}>Teknologi Informasi</option>"""

target2 = """<option value="Sains Data" {% if jurusan_filter=='Sains Data' %}selected{% endif
                                            %}>Sains Data</option>"""
val2 = """<option value="Sains Data" {% if jurusan_filter == 'Sains Data' %}selected{% endif %}>Sains Data</option>"""

# Replace
new_content = content.replace(target1, val1)
new_content = new_content.replace(target2, val2)

# Verify if replacement happened
if content == new_content:
    print("No changes made. Targets not found?")
    # Try a looser replacement if exact match failed due to spacing
    lines = content.splitlines()
    fixed_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if 'Teknologi Informasi' in line and '{% if' in line and 'selected' not in line:
            # We found the start of the split tag
            next_line = lines[i+1]
            if '%}selected{% endif %}' in next_line:
                print("Found split tag (TI), fixing...")
                fixed_lines.append('<option value="Teknologi Informasi" {% if jurusan_filter == "Teknologi Informasi" %}selected{% endif %}>Teknologi Informasi</option>')
                i += 2
                continue
        if 'Sains Data' in line and '{% if' in line and 'selected' in line and 'endif' not in line:
             next_line = lines[i+1]
             if '%}>Sains Data</option>' in next_line:
                 print("Found split tag (SD), fixing...")
                 fixed_lines.append('<option value="Sains Data" {% if jurusan_filter == "Sains Data" %}selected{% endif %}>Sains Data</option>')
                 i += 2
                 continue
        
        fixed_lines.append(line)
        i += 1
    new_content = '\n'.join(fixed_lines)

if content != new_content:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully fixed input.html")
else:
    print("Content matched, no changes needed or targets still not found.")
