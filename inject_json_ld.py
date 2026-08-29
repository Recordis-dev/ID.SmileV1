import os
import glob

# Load JSON-LD
try:
    with open("export_zip/json_ld.json", "r", encoding="utf-8") as f:
        json_ld_content = f.read()
except FileNotFoundError:
    print("No json_ld.json found, skipping.")
    exit(0)

# Create the script tag
script_tag = f'\n<script type="application/ld+json">\n{json_ld_content}\n</script>\n'

html_files = glob.glob(os.path.join("export_zip", "*.html"))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Inject just before closing head tag
    if '</head>' in content:
        content = content.replace('</head>', f'{script_tag}</head>')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Injected JSON-LD into {len(html_files)} files.")
