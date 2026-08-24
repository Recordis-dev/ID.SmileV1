import os
import glob

# SLP to Cluster Mapping
clusters = {
    'servicio-ortodoncia.html': ('Ortodoncia y Alineación', [('Odontopediatría', 'servicio-odontopediatria.html'), ('Odontología Integral', 'servicio-integral.html')]),
    'servicio-odontopediatria.html': ('Ortodoncia y Alineación', [('Ortodoncia', 'servicio-ortodoncia.html'), ('Prevención', 'servicio-integral.html')]),
    'servicio-implantes.html': ('Restauración y Rehabilitación', [('Endodoncia', 'servicio-endodoncia.html'), ('Periodoncia', 'servicio-periodoncia.html')]),
    'servicio-endodoncia.html': ('Restauración y Rehabilitación', [('Implantes y Prótesis', 'servicio-implantes.html'), ('Odontología Integral', 'servicio-integral.html')]),
    'servicio-integral.html': ('Salud Bucal y Cirugía', [('Periodoncia', 'servicio-periodoncia.html'), ('Endodoncia', 'servicio-endodoncia.html')]),
    'servicio-periodoncia.html': ('Salud Bucal y Cirugía', [('Implantes y Prótesis', 'servicio-implantes.html'), ('Odontología Integral', 'servicio-integral.html')]),
    'servicio-cirugia.html': ('Salud Bucal y Cirugía', [('Implantes y Prótesis', 'servicio-implantes.html'), ('Ortodoncia', 'servicio-ortodoncia.html')]),
    'blog.html': ('Recursos', [('Tratamientos', 'index.html#servicios')])
}

# The semantic navigation block
nav_html = """
<nav aria-label="Navegación principal" style="display:flex;align-items:center;gap:18px;flex-wrap:wrap;list-style:none;margin:0;padding:0">
  <li style="position:relative" class="nav-dropdown">
    <a href="index.html#servicios" style="font-size:14px;color:#A8AEB6;padding:8px 12px;border-radius:99px;text-decoration:none" aria-haspopup="true" aria-expanded="false">Tratamientos ▼</a>
    <ul class="dropdown-content" aria-label="Lista de tratamientos" style="display:none;position:absolute;top:100%;left:0;background:#14161A;border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:12px;min-width:220px;z-index:100;box-shadow:0 10px 25px rgba(0,0,0,0.5)">
      <li style="margin-bottom:8px"><span style="color:#2E9AA0;font-size:11px;text-transform:uppercase;letter-spacing:1px;padding:0 12px">Ortodoncia</span></li>
      <li><a href="servicio-ortodoncia.html" style="display:block;padding:8px 12px;color:#fff;text-decoration:none;font-size:14px;border-radius:4px">Ortodoncia Especializada</a></li>
      <li><a href="servicio-odontopediatria.html" style="display:block;padding:8px 12px;color:#fff;text-decoration:none;font-size:14px;border-radius:4px">Odontopediatría</a></li>
      <li style="margin:12px 0 8px"><span style="color:#2E9AA0;font-size:11px;text-transform:uppercase;letter-spacing:1px;padding:0 12px">Restauración</span></li>
      <li><a href="servicio-implantes.html" style="display:block;padding:8px 12px;color:#fff;text-decoration:none;font-size:14px;border-radius:4px">Implantes y Prótesis</a></li>
      <li><a href="servicio-endodoncia.html" style="display:block;padding:8px 12px;color:#fff;text-decoration:none;font-size:14px;border-radius:4px">Endodoncia</a></li>
      <li style="margin:12px 0 8px"><span style="color:#2E9AA0;font-size:11px;text-transform:uppercase;letter-spacing:1px;padding:0 12px">Salud Bucal</span></li>
      <li><a href="servicio-integral.html" style="display:block;padding:8px 12px;color:#fff;text-decoration:none;font-size:14px;border-radius:4px">Odontología Integral</a></li>
      <li><a href="servicio-periodoncia.html" style="display:block;padding:8px 12px;color:#fff;text-decoration:none;font-size:14px;border-radius:4px">Periodoncia</a></li>
      <li><a href="servicio-cirugia.html" style="display:block;padding:8px 12px;color:#fff;text-decoration:none;font-size:14px;border-radius:4px">Cirugía Bucal</a></li>
    </ul>
  </li>
  <li><a href="index.html#doctores" style="font-size:14px;color:#A8AEB6;padding:8px 12px;border-radius:99px;text-decoration:none">Especialistas</a></li>
  <li><a href="blog.html" style="font-size:14px;color:#A8AEB6;padding:8px 12px;border-radius:99px;text-decoration:none">Blog</a></li>
  <li><a href="https://wa.me/5217773773106" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;gap:8px;background:#2E9AA0;color:#fff;font-weight:700;font-size:14px;padding:11px 18px;border-radius:99px;text-decoration:none">Agendar Cita</a></li>
</nav>
"""

css_injection = """
<style>
  .nav-dropdown:hover .dropdown-content { display: block !important; }
  .dropdown-content a:hover { background: rgba(46,154,160,0.15); }
  .breadcrumb a { color: #2E9AA0; text-decoration: none; }
  .breadcrumb a:hover { text-decoration: underline; }
</style>
</head>
"""

def generate_related_section(related):
    links_html = "".join([f'<a href="{url}" style="display:inline-block;padding:12px 24px;border:1px solid #DCDFE3;border-radius:8px;color:#121417;text-decoration:none;font-weight:500;transition:border-color 0.2s" onmouseover="this.style.borderColor=\'#2E9AA0\'" onmouseout="this.style.borderColor=\'#DCDFE3\'">{name} →</a>' for name, url in related])
    
    return f"""
    <!-- Related Services Cross-linking (AI SEO) -->
    <section style="padding:60px 24px;background:#FAFBFC;border-top:1px solid #E7EAEE">
        <div style="max-width:800px;margin:0 auto;text-align:center">
            <h3 style="font-family:'Bricolage Grotesque',sans-serif;font-size:24px;margin:0 0 24px">Explora otros servicios relacionados</h3>
            <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap">
                {links_html}
            </div>
        </div>
    </section>
    """

def process_file(filepath):
    filename = os.path.basename(filepath)
    if filename not in clusters:
        return

    pillar, related = clusters[filename]
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Inject CSS before </head>
    if "</head>" in content and "nav-dropdown:hover" not in content:
        content = content.replace("</head>", css_injection)

    # Replace old Nav with new semantic Mega Menu Nav
    if "<nav " in content:
        import re
        content = re.sub(r'<nav.*?</nav>', nav_html, content, flags=re.DOTALL)
    
    # Inject Breadcrumbs right after the header ends and before the main content starts
    # We look for </header>
    breadcrumb_html = f"""
    <!-- SEO Breadcrumbs -->
    <nav aria-label="Breadcrumb" class="breadcrumb" style="max-width:1140px;margin:0 auto;padding:16px 24px;font-size:13px;color:#7C838C">
      <ol style="list-style:none;padding:0;margin:0;display:flex;gap:8px">
        <li><a href="index.html">Inicio</a></li>
        <li><span aria-hidden="true">/</span></li>
        <li><a href="index.html#servicios">Tratamientos</a></li>
        <li><span aria-hidden="true">/</span></li>
        <li>{pillar}</li>
        <li><span aria-hidden="true">/</span></li>
        <li aria-current="page" style="color:#121417;font-weight:500">{filename.replace('servicio-', '').replace('.html', '').capitalize()}</li>
      </ol>
    </nav>
    """
    
    if "</header>" in content and "aria-label=\"Breadcrumb\"" not in content:
        content = content.replace("</header>", f"</header>\n{breadcrumb_html}")

    # Inject Related Services before the Footer
    related_html = generate_related_section(related)
    if "<footer" in content and "Explora otros servicios relacionados" not in content:
        content = content.replace("<footer", f"{related_html}\n<footer")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for root, _, files in os.walk('ui_kits/idsmile_remix'):
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))

# Also apply MegaMenu to index.html
with open('ui_kits/idsmile_remix/IDSmileApertureRemix.dc.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()
    if "</head>" in idx_content and "nav-dropdown:hover" not in idx_content:
        idx_content = idx_content.replace("</head>", css_injection)
    import re
    idx_content = re.sub(r'<nav.*?</nav>', nav_html, idx_content, flags=re.DOTALL)
with open('ui_kits/idsmile_remix/IDSmileApertureRemix.dc.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)

print("SLPs and Index cross-linked with Semantic Mega Menu and Breadcrumbs successfully.")
