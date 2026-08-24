import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The semantic navigation block (same as above)
nav_html = """
<nav aria-label="Navegación principal" style="display:flex;align-items:center;gap:18px;flex-wrap:wrap;list-style:none;margin:0;padding:0">
  <li style="position:relative" class="nav-dropdown">
    <a href="#servicios" style="font-size:14px;color:#A8AEB6;padding:8px 12px;border-radius:99px;text-decoration:none" aria-haspopup="true" aria-expanded="false">Tratamientos ▼</a>
    <ul class="dropdown-content" aria-label="Lista de tratamientos" style="display:none;position:absolute;top:100%;left:0;background:#14161A;border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:12px;min-width:220px;z-index:100;box-shadow:0 10px 25px rgba(0,0,0,0.5)">
      <li style="margin-bottom:8px"><span style="color:#2E9AA0;font-size:11px;text-transform:uppercase;letter-spacing:1px;padding:0 12px">Ortodoncia</span></li>
      <li><a href="ui_kits/idsmile_remix/servicio-ortodoncia.html" style="display:block;padding:8px 12px;color:#fff;text-decoration:none;font-size:14px;border-radius:4px">Ortodoncia Especializada</a></li>
      <li><a href="ui_kits/idsmile_remix/servicio-odontopediatria.html" style="display:block;padding:8px 12px;color:#fff;text-decoration:none;font-size:14px;border-radius:4px">Odontopediatría</a></li>
      <li style="margin:12px 0 8px"><span style="color:#2E9AA0;font-size:11px;text-transform:uppercase;letter-spacing:1px;padding:0 12px">Restauración</span></li>
      <li><a href="ui_kits/idsmile_remix/servicio-implantes.html" style="display:block;padding:8px 12px;color:#fff;text-decoration:none;font-size:14px;border-radius:4px">Implantes y Prótesis</a></li>
      <li><a href="ui_kits/idsmile_remix/servicio-endodoncia.html" style="display:block;padding:8px 12px;color:#fff;text-decoration:none;font-size:14px;border-radius:4px">Endodoncia</a></li>
      <li style="margin:12px 0 8px"><span style="color:#2E9AA0;font-size:11px;text-transform:uppercase;letter-spacing:1px;padding:0 12px">Salud Bucal</span></li>
      <li><a href="ui_kits/idsmile_remix/servicio-integral.html" style="display:block;padding:8px 12px;color:#fff;text-decoration:none;font-size:14px;border-radius:4px">Odontología Integral</a></li>
      <li><a href="ui_kits/idsmile_remix/servicio-periodoncia.html" style="display:block;padding:8px 12px;color:#fff;text-decoration:none;font-size:14px;border-radius:4px">Periodoncia</a></li>
      <li><a href="ui_kits/idsmile_remix/servicio-cirugia.html" style="display:block;padding:8px 12px;color:#fff;text-decoration:none;font-size:14px;border-radius:4px">Cirugía Bucal</a></li>
    </ul>
  </li>
  <li><a href="#doctores" style="font-size:14px;color:#A8AEB6;padding:8px 12px;border-radius:99px;text-decoration:none">Especialistas</a></li>
  <li><a href="ui_kits/idsmile_remix/blog.html" style="font-size:14px;color:#A8AEB6;padding:8px 12px;border-radius:99px;text-decoration:none">Blog</a></li>
  <li><a href="https://wa.me/5217773773106" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;gap:8px;background:#2E9AA0;color:#fff;font-weight:700;font-size:14px;padding:11px 18px;border-radius:99px;text-decoration:none">Agendar Cita</a></li>
</nav>
"""

css_injection = """
<style>
  .nav-dropdown:hover .dropdown-content { display: block !important; }
  .dropdown-content a:hover { background: rgba(46,154,160,0.15); }
</style>
</head>
"""

if "</head>" in content and "nav-dropdown:hover" not in content:
    content = content.replace("</head>", css_injection)

content = re.sub(r'<nav.*?</nav>', nav_html, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
