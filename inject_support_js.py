import os
import glob

html_files = glob.glob(os.path.join("export_zip", "*.html"))

support_script = '<script src="js/support.js"></script>'

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if support.js is already included
    if support_script not in content and 'src="js/support.js"' not in content:
        # Inject just before closing head tag, or before the closing body tag
        if '</head>' in content:
            content = content.replace('</head>', f'{support_script}\n</head>')

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

print(f"Ensured support.js is in {len(html_files)} files.")
