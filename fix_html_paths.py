import os
import glob

# Directory containing the HTML files
html_dir = "export_zip"

# Find all HTML files in the directory
html_files = glob.glob(os.path.join(html_dir, "*.html"))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace relative paths pointing from 'html/'
    # E.g. "../css/styles.css" becomes "css/styles.css"
    # E.g. "../js/scripts.js" becomes "js/scripts.js"
    # E.g. "../js/support.js" becomes "js/support.js"

    content = content.replace('href="../css/', 'href="css/')
    content = content.replace('src="../js/', 'src="js/')

    # Assuming internal html links might be relative e.g., href="blog.html" or href="../html/blog.html"
    content = content.replace('href="../html/', 'href="')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Updated paths in {len(html_files)} HTML files.")
