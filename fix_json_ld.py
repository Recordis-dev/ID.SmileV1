import re

with open("export_zip/js/scripts.js", "r", encoding="utf-8") as f:
    js_content = f.read()

# Extract JSON-LD (everything before the first 'class ' or similar code)
match = re.search(r'^\s*(\{.*?\})\s*\n+class', js_content, re.DOTALL | re.MULTILINE)
if match:
    json_ld = match.group(1)

    # Save the extracted JSON-LD to a file to be injected later
    with open("export_zip/json_ld.json", "w", encoding="utf-8") as f:
        f.write(json_ld)

    # Remove the JSON-LD from the JS file
    cleaned_js = js_content.replace(json_ld, "").strip()

    with open("export_zip/js/scripts.js", "w", encoding="utf-8") as f:
        f.write(cleaned_js)

    print("JSON-LD extracted and removed from scripts.js")
else:
    print("Could not find JSON-LD in scripts.js")
