import os
import glob
import re

# We will apply all AI SEO and structural improvements directly to the files IN their original directories.
# This ensures that the Storefront (index.html) and paths remain exactly as they were designed originally.

slp_dir = "ui_kits/idsmile_remix/"

# 1. POPULATE SLPS WITH MEDICAL CONTENT
content_library = {
    'servicio-ortodoncia.html': {
        'title': 'Ortodoncia Especializada',
        'subtitle': 'Alineación perfecta y mordida saludable',
        'body': '''
        <div style="font-family:'Inter',sans-serif;color:#121417">
            <h2 style="font-family:'Bricolage Grotesque',sans-serif;font-size:32px;letter-spacing:-0.03em;margin-bottom:16px">No es solo estética, es función.</h2>
            <p style="font-size:17px;line-height:1.65;color:#3C4248;margin-bottom:24px">La ortodoncia moderna va más allá de enderezar los dientes. Un tratamiento especializado corrige la mordida, previene el desgaste prematuro de las piezas dentales y alivia tensiones articulares. En ID Smile utilizamos tanto sistemas de brackets convencionales y estéticos como la última tecnología en alineadores invisibles.</p>
            
            <h3 style="font-size:24px;margin:32px 0 16px">Nuestras opciones de tratamiento</h3>
            <ul style="font-size:16px;line-height:1.6;color:#5A6169;margin-bottom:32px;padding-left:20px">
                <li style="margin-bottom:12px;position:relative;"><strong>Brackets Metálicos:</strong> La opción más probada, resistente y rápida para casos complejos.</li>
                <li style="margin-bottom:12px;position:relative;"><strong>Brackets Estéticos (Zafiro/Cerámica):</strong> Altamente discretos, se mimetizan con el color de tu diente.</li>
                <li style="margin-bottom:12px;position:relative;"><strong>Alineadores Transparentes:</strong> Férulas removibles que corrigen tu sonrisa sin que nadie lo note. Ideales para pacientes adultos con casos leves a moderados.</li>
            </ul>

            <div style="background:#FAFBFC;border:1px solid #DCDFE3;box-shadow:inset 0 2px 4px rgba(0,0,0,0.02);border-radius:12px;padding:24px;margin-bottom:40px">
                <h3 style="font-family:'Bricolage Grotesque',sans-serif;font-size:22px;margin:0 0 16px;color:#2E9AA0">Preguntas Frecuentes</h3>
                <strong style="display:block;margin-bottom:8px;color:#121417;font-size:17px">¿Cuánto tiempo dura el tratamiento?</strong>
                <p style="font-size:15px;color:#5A6169;margin:0 0 16px">Depende de la complejidad de la mordida. Casos sencillos con alineadores pueden tomar 6 meses, mientras que correcciones severas toman entre 18 y 24 meses.</p>
                <strong style="display:block;margin-bottom:8px;color:#121417;font-size:17px">¿Duele ponerse brackets?</strong>
                <p style="font-size:15px;color:#5A6169;margin:0">La colocación no duele. Sentirás presión los primeros 3 a 5 días después de cada ajuste mensual mientras los dientes se adaptan al movimiento.</p>
            </div>
        </div>
        '''
    },
    'servicio-implantes.html': {
        'title': 'Implantes y Prótesis Dentales',
        'subtitle': 'Recupera la fuerza y naturalidad de tu sonrisa',
        'body': '''
        <div style="font-family:'Inter',sans-serif;color:#121417">
            <h2 style="font-family:'Bricolage Grotesque',sans-serif;font-size:32px;letter-spacing:-0.03em;margin-bottom:16px">La solución definitiva a la pérdida dental.</h2>
            <p style="font-size:17px;line-height:1.65;color:#3C4248;margin-bottom:24px">Un implante dental es la forma más avanzada y segura de reemplazar un diente perdido. Consiste en una pequeña raíz de titanio biocompatible que se integra al hueso, sobre la cual colocamos una corona de porcelana hecha a la medida. El resultado es un diente que se ve, se siente y funciona exactamente igual que uno natural.</p>
            
            <h3 style="font-size:24px;margin:32px 0 16px">¿Por qué elegir implantes?</h3>
            <ul style="font-size:16px;line-height:1.6;color:#5A6169;margin-bottom:32px;padding-left:20px">
                <li style="margin-bottom:12px;position:relative;"><strong>Detienen la pérdida ósea:</strong> Al estimular el hueso, evitan que tu rostro envejezca prematuramente.</li>
                <li style="margin-bottom:12px;position:relative;"><strong>Protegen a los dientes vecinos:</strong> A diferencia de los puentes tradicionales, no es necesario desgastar los dientes sanos adyacentes.</li>
                <li style="margin-bottom:12px;position:relative;"><strong>Durabilidad extrema:</strong> Con una higiene adecuada, un implante puede durar toda la vida.</li>
            </ul>

            <div style="background:#FAFBFC;border:1px solid #DCDFE3;box-shadow:inset 0 2px 4px rgba(0,0,0,0.02);border-radius:12px;padding:24px;margin-bottom:40px">
                <h3 style="font-family:'Bricolage Grotesque',sans-serif;font-size:22px;margin:0 0 16px;color:#2E9AA0">Preguntas Frecuentes</h3>
                <strong style="display:block;margin-bottom:8px;color:#121417;font-size:17px">¿Soy candidato para un implante?</strong>
                <p style="font-size:15px;color:#5A6169;margin:0 0 16px">La mayoría de los adultos con encías sanas y suficiente hueso son candidatos. Si te falta hueso, podemos realizar un injerto óseo previo.</p>
                <strong style="display:block;margin-bottom:8px;color:#121417;font-size:17px">¿El procedimiento es doloroso?</strong>
                <p style="font-size:15px;color:#5A6169;margin:0">Se realiza bajo anestesia local, por lo que no sentirás dolor durante la cirugía. El postoperatorio es sorprendentemente leve y se maneja con analgésicos comunes.</p>
            </div>
        </div>
        '''
    },
    'servicio-odontopediatria.html': {
        'title': 'Odontopediatría',
        'subtitle': 'Experiencias dentales positivas desde la infancia',
        'body': '''
        <div style="font-family:'Inter',sans-serif;color:#121417">
            <h2 style="font-family:'Bricolage Grotesque',sans-serif;font-size:32px;letter-spacing:-0.03em;margin-bottom:16px">Cuidando el futuro de su sonrisa.</h2>
            <p style="font-size:17px;line-height:1.65;color:#3C4248;margin-bottom:24px">La odontopediatría no solo trata los dientes de leche; se trata de guiar el crecimiento facial, educar sobre higiene y, sobre todo, crear un ambiente de confianza para que los niños crezcan sin miedo al dentista. En ID Smile tenemos la paciencia y el entrenamiento para manejar la ansiedad infantil.</p>
            
            <h3 style="font-size:24px;margin:32px 0 16px">Nuestros servicios para niños</h3>
            <ul style="font-size:16px;line-height:1.6;color:#5A6169;margin-bottom:32px;padding-left:20px">
                <li style="margin-bottom:12px;position:relative;"><strong>Odontología Preventiva:</strong> Limpiezas, aplicación de flúor y selladores de fosetas y fisuras para bloquear caries antes de que empiecen.</li>
                <li style="margin-bottom:12px;position:relative;"><strong>Restauración Pediátrica:</strong> Resinas estéticas y coronas de acero cromo para dientes de leche muy dañados.</li>
                <li style="margin-bottom:12px;position:relative;"><strong>Ortopedia Maxilar:</strong> Uso de aparatos removibles o fijos (antes de los 11 años) para corregir el crecimiento del hueso y evitar cirugías severas en la adultez.</li>
            </ul>

            <div style="background:#FAFBFC;border:1px solid #DCDFE3;box-shadow:inset 0 2px 4px rgba(0,0,0,0.02);border-radius:12px;padding:24px;margin-bottom:40px">
                <h3 style="font-family:'Bricolage Grotesque',sans-serif;font-size:22px;margin:0 0 16px;color:#2E9AA0">Preguntas Frecuentes</h3>
                <strong style="display:block;margin-bottom:8px;color:#121417;font-size:17px">¿Cuándo debe ser la primera cita de mi hijo?</strong>
                <p style="font-size:15px;color:#5A6169;margin:0 0 16px">La Academia Americana de Odontopediatría recomienda la primera visita cuando aparece el primer diente, o a más tardar al cumplir su primer año.</p>
                <strong style="display:block;margin-bottom:8px;color:#121417;font-size:17px">¿Por qué arreglar un diente de leche si se va a caer?</strong>
                <p style="font-size:15px;color:#5A6169;margin:0">Los dientes de leche guían la erupción de los permanentes, permiten masticar bien y hablar correctamente. Una caries infantil profunda puede infectar el germen del diente permanente que viene debajo.</p>
            </div>
        </div>
        '''
    },
    'servicio-endodoncia.html': {
        'title': 'Endodoncia',
        'subtitle': 'Salva tu diente natural del dolor y la infección',
        'body': '''
        <div style="font-family:'Inter',sans-serif;color:#121417">
            <h2 style="font-family:'Bricolage Grotesque',sans-serif;font-size:32px;letter-spacing:-0.03em;margin-bottom:16px">Eliminamos el dolor, conservamos tu diente.</h2>
            <p style="font-size:17px;line-height:1.65;color:#3C4248;margin-bottom:24px">Cuando una caries es muy profunda o un diente sufre un fuerte golpe, el nervio en su interior se inflama o infecta, causando dolor agudo. La endodoncia (tratamiento de conductos) retira este tejido dañado, desinfecta la raíz y la sella, permitiéndote conservar tu diente original en lugar de extraerlo.</p>
            
            <h3 style="font-size:24px;margin:32px 0 16px">Señales de que necesitas una endodoncia</h3>
            <ul style="font-size:16px;line-height:1.6;color:#5A6169;margin-bottom:32px;padding-left:20px">
                <li style="margin-bottom:12px;position:relative;"><strong>Dolor espontáneo y punzante:</strong> Especialmente intenso por la noche o al acostarte.</li>
                <li style="margin-bottom:12px;position:relative;"><strong>Sensibilidad extrema al frío o calor:</strong> Que persiste durante minutos después de retirar el estímulo.</li>
                <li style="margin-bottom:12px;position:relative;"><strong>Inflamación en la encía:</strong> Presencia de una "bolita" (fístula) cerca de la raíz del diente.</li>
            </ul>

            <div style="background:#FAFBFC;border:1px solid #DCDFE3;box-shadow:inset 0 2px 4px rgba(0,0,0,0.02);border-radius:12px;padding:24px;margin-bottom:40px">
                <h3 style="font-family:'Bricolage Grotesque',sans-serif;font-size:22px;margin:0 0 16px;color:#2E9AA0">Preguntas Frecuentes</h3>
                <strong style="display:block;margin-bottom:8px;color:#121417;font-size:17px">¿El tratamiento de conductos es doloroso?</strong>
                <p style="font-size:15px;color:#5A6169;margin:0 0 16px">Con las técnicas de anestesia modernas, la endodoncia es similar a hacerse un empaste de rutina. De hecho, el procedimiento alivia inmediatamente el dolor causado por la infección.</p>
                <strong style="display:block;margin-bottom:8px;color:#121417;font-size:17px">¿Qué pasa después de la endodoncia?</strong>
                <p style="font-size:15px;color:#5A6169;margin:0">El diente queda "hueco" y más frágil. Es indispensable colocar una incrustación o una corona de porcelana semanas después para protegerlo de fracturas.</p>
            </div>
        </div>
        '''
    },
    'servicio-integral.html': {
        'title': 'Odontología Integral',
        'subtitle': 'Salud, prevención y resinas estéticas',
        'body': '''
        <div style="font-family:'Inter',sans-serif;color:#121417">
            <h2 style="font-family:'Bricolage Grotesque',sans-serif;font-size:32px;letter-spacing:-0.03em;margin-bottom:16px">La base de una sonrisa duradera.</h2>
            <p style="font-size:17px;line-height:1.65;color:#3C4248;margin-bottom:24px">La odontología integral es el primer frente de defensa. Nos enfocamos en el diagnóstico general, la eliminación de caries en etapas tempranas mediante resinas del color exacto de tu diente, limpiezas profundas con ultrasonido y el mantenimiento general de toda la cavidad oral.</p>
            
            <h3 style="font-size:24px;margin:32px 0 16px">¿Qué incluye el cuidado integral?</h3>
            <ul style="font-size:16px;line-height:1.6;color:#5A6169;margin-bottom:32px;padding-left:20px">
                <li style="margin-bottom:12px;position:relative;"><strong>Profilaxis (Limpieza Ultrasónica):</strong> Remoción de sarro y placa bacteriana, finalizando con un pulido para eliminar manchas de café y tabaco.</li>
                <li style="margin-bottom:12px;position:relative;"><strong>Resinas Estéticas:</strong> Eliminación de amalgamas grises o caries nuevas, reemplazándolas por un material compuesto que imita la translucidez natural del diente.</li>
                <li style="margin-bottom:12px;position:relative;"><strong>Valoración Diagnóstica:</strong> Revisión intraoral con cámara y radiografías para detectar problemas antes de que causen dolor.</li>
            </ul>

            <div style="background:#FAFBFC;border:1px solid #DCDFE3;box-shadow:inset 0 2px 4px rgba(0,0,0,0.02);border-radius:12px;padding:24px;margin-bottom:40px">
                <h3 style="font-family:'Bricolage Grotesque',sans-serif;font-size:22px;margin:0 0 16px;color:#2E9AA0">Preguntas Frecuentes</h3>
                <strong style="display:block;margin-bottom:8px;color:#121417;font-size:17px">¿Cada cuándo debo hacerme una limpieza?</strong>
                <p style="font-size:15px;color:#5A6169;margin:0 0 16px">La norma general es cada 6 meses. Sin embargo, pacientes con brackets o antecedentes de enfermedad en las encías deben hacerla cada 3 o 4 meses.</p>
            </div>
        </div>
        '''
    },
    'servicio-periodoncia.html': {
        'title': 'Periodoncia',
        'subtitle': 'Tratamiento de encías y soporte dental',
        'body': '''
        <div style="font-family:'Inter',sans-serif;color:#121417">
            <h2 style="font-family:'Bricolage Grotesque',sans-serif;font-size:32px;letter-spacing:-0.03em;margin-bottom:16px">Protegiendo los cimientos de tu sonrisa.</h2>
            <p style="font-size:17px;line-height:1.65;color:#3C4248;margin-bottom:24px">La periodoncia trata las enfermedades que afectan a las encías y al hueso que sostiene a los dientes. El sangrado de encías (gingivitis) no es normal y, si no se trata, avanza hacia la periodontitis, la causa número uno de pérdida de dientes en adultos.</p>
            
            <h3 style="font-size:24px;margin:32px 0 16px">Señales de alerta periodontal</h3>
            <ul style="font-size:16px;line-height:1.6;color:#5A6169;margin-bottom:32px;padding-left:20px">
                <li style="margin-bottom:12px;position:relative;"><strong>Sangrado persistente:</strong> Al cepillarte o usar hilo dental.</li>
                <li style="margin-bottom:12px;position:relative;"><strong>Movilidad dental:</strong> Sientes que tus dientes están "flojos".</li>
                <li style="margin-bottom:12px;position:relative;"><strong>Retracción gingival:</strong> Tus dientes parecen más largos porque la encía se ha encogido.</li>
            </ul>

            <div style="background:#FAFBFC;border:1px solid #DCDFE3;box-shadow:inset 0 2px 4px rgba(0,0,0,0.02);border-radius:12px;padding:24px;margin-bottom:40px">
                <h3 style="font-family:'Bricolage Grotesque',sans-serif;font-size:22px;margin:0 0 16px;color:#2E9AA0">Preguntas Frecuentes</h3>
                <strong style="display:block;margin-bottom:8px;color:#121417;font-size:17px">¿La periodontitis tiene cura?</strong>
                <p style="font-size:15px;color:#5A6169;margin:0 0 16px">El daño al hueso causado por la periodontitis es irreversible, pero el progreso de la enfermedad puede detenerse por completo mediante raspados, alisados radiculares y un estricto control de higiene, conservando los dientes restantes.</p>
            </div>
        </div>
        '''
    },
    'servicio-cirugia.html': {
        'title': 'Cirugía Bucal',
        'subtitle': 'Extracción de terceros molares y procedimientos menores',
        'body': '''
        <div style="font-family:'Inter',sans-serif;color:#121417">
            <h2 style="font-family:'Bricolage Grotesque',sans-serif;font-size:32px;letter-spacing:-0.03em;margin-bottom:16px">Procedimientos quirúrgicos seguros y controlados.</h2>
            <p style="font-size:17px;line-height:1.65;color:#3C4248;margin-bottom:24px">Realizamos extracciones complejas, cirugía de muelas del juicio (terceros molares) impactadas o retenidas, y regularizaciones de hueso. Nuestro enfoque en ID Smile es realizar estas intervenciones de la manera menos traumática posible para asegurar una recuperación rápida y sin dolor.</p>
            
            <h3 style="font-size:24px;margin:32px 0 16px">Muelas del Juicio</h3>
            <ul style="font-size:16px;line-height:1.6;color:#5A6169;margin-bottom:32px;padding-left:20px">
                <li style="margin-bottom:12px;position:relative;"><strong>¿Por qué extraerlas?:</strong> A menudo no tienen suficiente espacio para salir, empujan a los otros dientes (arruinando tratamientos de ortodoncia previos) o se quedan atoradas bajo la encía causando quistes o infecciones recurrentes.</li>
                <li style="margin-bottom:12px;position:relative;"><strong>Recuperación:</strong> Gracias a técnicas quirúrgicas modernas, la mayoría de los pacientes regresan a sus actividades normales en 48 a 72 horas.</li>
            </ul>

            <div style="background:#FAFBFC;border:1px solid #DCDFE3;box-shadow:inset 0 2px 4px rgba(0,0,0,0.02);border-radius:12px;padding:24px;margin-bottom:40px">
                <h3 style="font-family:'Bricolage Grotesque',sans-serif;font-size:22px;margin:0 0 16px;color:#2E9AA0">Preguntas Frecuentes</h3>
                <strong style="display:block;margin-bottom:8px;color:#121417;font-size:17px">¿Tienen que quitarme las 4 muelas a la vez?</strong>
                <p style="font-size:15px;color:#5A6169;margin:0 0 16px">Es la recomendación más habitual para pasar por el proceso de inflamación y recuperación una sola vez, pero podemos adaptarnos a extraerlas por lados (derecho e izquierdo) si el paciente lo prefiere.</p>
            </div>
        </div>
        '''
    }
}

# 2. CTAs, META and SCHEMAS
metadata_map = {
    'servicio-ortodoncia.html': {
        'title': 'Ortodoncia en Cuernavaca | Brackets y Alineadores | ID Smile',
        'desc': 'Tratamiento de ortodoncia especializada en el Hospital San Diego. Corrección de mordida con brackets estéticos y alineadores invisibles.',
        'cta': 'Agenda tu valoración de Ortodoncia',
        'schema': 'Ortodoncia'
    },
    'servicio-implantes.html': {
        'title': 'Implantes Dentales en Cuernavaca | Prótesis Fijas | ID Smile',
        'desc': 'Recupera la función y estética de tu sonrisa con implantes dentales de titanio y coronas de porcelana en Cuernavaca.',
        'cta': 'Recupera tu diente con Implantes',
        'schema': 'Colocación de Implantes Dentales'
    },
    'servicio-odontopediatria.html': {
        'title': 'Odontopediatra en Cuernavaca | Dentista para Niños | ID Smile',
        'desc': 'Atención dental especializada para niños. Prevención de caries, aplicación de flúor y ortopedia maxilar infantil en un ambiente seguro.',
        'cta': 'Agenda la revisión de tu pequeño',
        'schema': 'Odontología Pediátrica'
    },
    'servicio-endodoncia.html': {
        'title': 'Endodoncia en Cuernavaca | Tratamiento de Conductos | ID Smile',
        'desc': 'Salva tu diente natural y elimina el dolor con nuestro tratamiento de endodoncia seguro y sin dolor en el Hospital San Diego.',
        'cta': 'Salva tu diente hoy mismo',
        'schema': 'Tratamiento de Conductos (Endodoncia)'
    },
    'servicio-integral.html': {
        'title': 'Dentista General en Cuernavaca | Limpiezas y Resinas | ID Smile',
        'desc': 'Odontología preventiva e integral. Limpiezas ultrasónicas, eliminación de caries y resinas estéticas del color de tu diente.',
        'cta': 'Agenda tu limpieza profunda',
        'schema': 'Odontología General y Limpieza'
    },
    'servicio-periodoncia.html': {
        'title': 'Tratamiento de Encías en Cuernavaca | Periodoncia | ID Smile',
        'desc': 'Especialistas en periodoncia para detener el sangrado de encías, tratar la gingivitis y salvar los dientes con movilidad.',
        'cta': 'Detén el sangrado de encías',
        'schema': 'Tratamiento Periodontal'
    },
    'servicio-cirugia.html': {
        'title': 'Extracción de Muelas del Juicio en Cuernavaca | Cirugía Bucal',
        'desc': 'Cirugía maxilofacial segura. Extracción sin dolor de terceros molares (muelas del juicio) impactadas o retenidas.',
        'cta': 'Extracción de muelas sin dolor',
        'schema': 'Extracción de Terceros Molares'
    }
}

# 3. TOPIC CLUSTERS AND BREADCRUMBS
clusters = {
    'servicio-ortodoncia.html': ('Ortodoncia y Alineación', [('Odontopediatría', 'servicio-odontopediatria.html'), ('Odontología Integral', 'servicio-integral.html')]),
    'servicio-odontopediatria.html': ('Ortodoncia y Alineación', [('Ortodoncia', 'servicio-ortodoncia.html'), ('Prevención', 'servicio-integral.html')]),
    'servicio-implantes.html': ('Restauración y Rehabilitación', [('Endodoncia', 'servicio-endodoncia.html'), ('Periodoncia', 'servicio-periodoncia.html')]),
    'servicio-endodoncia.html': ('Restauración y Rehabilitación', [('Implantes y Prótesis', 'servicio-implantes.html'), ('Odontología Integral', 'servicio-integral.html')]),
    'servicio-integral.html': ('Salud Bucal y Cirugía', [('Periodoncia', 'servicio-periodoncia.html'), ('Endodoncia', 'servicio-endodoncia.html')]),
    'servicio-periodoncia.html': ('Salud Bucal y Cirugía', [('Implantes y Prótesis', 'servicio-implantes.html'), ('Odontología Integral', 'servicio-integral.html')]),
    'servicio-cirugia.html': ('Salud Bucal y Cirugía', [('Implantes y Prótesis', 'servicio-implantes.html'), ('Ortodoncia', 'servicio-ortodoncia.html')])
}

# MEGA MENU FOR SLPS AND LANDING
mega_menu_nav_slp = """
<nav aria-label="Navegación principal" style="display:flex;align-items:center;gap:18px;flex-wrap:wrap;list-style:none;margin:0;padding:0">
  <li style="position:relative" class="nav-dropdown">
    <a href="IDSmileApertureRemix.dc.html#servicios" style="font-size:14px;color:#A8AEB6;padding:8px 12px;border-radius:99px;text-decoration:none" aria-haspopup="true" aria-expanded="false">Tratamientos ▼</a>
    <ul class="dropdown-content" aria-label="Lista de tratamientos" style="display:none;position:absolute;top:100%;left:0;background:rgba(20, 22, 26, 0.95);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,0.1);border-radius:12px;padding:12px;min-width:260px;z-index:100;box-shadow:0 10px 25px rgba(0,0,0,0.5)">
      <li style="margin-bottom:8px"><span style="color:#2E9AA0;font-size:11px;text-transform:uppercase;letter-spacing:1px;padding:0 12px">Ortodoncia y Alineación</span></li>
      <li><a href="servicio-ortodoncia.html" style="display:block;padding:8px 12px;color:#fff;text-decoration:none;font-size:14px;border-radius:6px;transition:background 0.2s">Ortodoncia Especializada</a></li>
      <li><a href="servicio-odontopediatria.html" style="display:block;padding:8px 12px;color:#fff;text-decoration:none;font-size:14px;border-radius:6px;transition:background 0.2s">Odontopediatría</a></li>
      <li style="margin:12px 0 8px"><span style="color:#2E9AA0;font-size:11px;text-transform:uppercase;letter-spacing:1px;padding:0 12px">Restauración y Prótesis</span></li>
      <li><a href="servicio-implantes.html" style="display:block;padding:8px 12px;color:#fff;text-decoration:none;font-size:14px;border-radius:6px;transition:background 0.2s">Implantes Dentales</a></li>
      <li><a href="servicio-endodoncia.html" style="display:block;padding:8px 12px;color:#fff;text-decoration:none;font-size:14px;border-radius:6px;transition:background 0.2s">Endodoncia (Salva tu diente)</a></li>
      <li style="margin:12px 0 8px"><span style="color:#2E9AA0;font-size:11px;text-transform:uppercase;letter-spacing:1px;padding:0 12px">Salud Bucal y Cirugía</span></li>
      <li><a href="servicio-integral.html" style="display:block;padding:8px 12px;color:#fff;text-decoration:none;font-size:14px;border-radius:6px;transition:background 0.2s">Odontología Integral</a></li>
      <li><a href="servicio-periodoncia.html" style="display:block;padding:8px 12px;color:#fff;text-decoration:none;font-size:14px;border-radius:6px;transition:background 0.2s">Periodoncia (Encías)</a></li>
      <li><a href="servicio-cirugia.html" style="display:block;padding:8px 12px;color:#fff;text-decoration:none;font-size:14px;border-radius:6px;transition:background 0.2s">Cirugía Bucal (Muelas del juicio)</a></li>
    </ul>
  </li>
  <li><a href="IDSmileApertureRemix.dc.html#doctores" style="font-size:14px;color:#A8AEB6;padding:8px 12px;border-radius:99px;text-decoration:none">Especialistas</a></li>
  <li><a href="blog.html" style="font-size:14px;color:#A8AEB6;padding:8px 12px;border-radius:99px;text-decoration:none">Blog & Recursos</a></li>
  <li><a href="https://wa.me/5217773773106" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;gap:8px;background:#2E9AA0;color:#fff;font-weight:700;font-size:14px;padding:11px 18px;border-radius:99px;text-decoration:none">Agendar Valoración</a></li>
</nav>
"""

css_injection = """
<style>
  .nav-dropdown:hover .dropdown-content { display: block !important; }
  .dropdown-content a:hover { background: rgba(46,154,160,0.15); }
  .breadcrumb a { color: #2E9AA0; text-decoration: none; font-family:'Inter',sans-serif;font-weight:400; }
  .breadcrumb a:hover { text-decoration: underline; }
</style>
</head>
"""

def generate_related_section(related):
    links_html = "".join([f'<a href="{url}" style="display:inline-block;padding:12px 24px;border:1px solid #DCDFE3;border-radius:8px;color:#121417;text-decoration:none;font-family:\'Inter\',sans-serif;font-weight:600;font-size:15px;background:#fff;transition:border-color 0.2s, background-color 0.2s, transform 0.2s" onmouseover="this.style.borderColor=\'#2E9AA0\'; this.style.backgroundColor=\'#FAFBFC\'; this.style.transform=\'translateY(-2px)\'" onmouseout="this.style.borderColor=\'#DCDFE3\'; this.style.backgroundColor=\'transparent\'; this.style.transform=\'translateY(0)\'">{name} →</a>' for name, url in related])
    
    return f"""
    <!-- Related Services Cross-linking (AI SEO) -->
    <section style="padding:80px 24px;background:#F2F4F6;border-top:1px solid #E7EAEE">
        <div style="max-width:800px;margin:0 auto;text-align:center">
            <h3 style="font-family:'Bricolage Grotesque',sans-serif;font-size:24px;margin:0 0 24px">Explora otros servicios relacionados</h3>
            <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap">
                {links_html}
            </div>
        </div>
    </section>
    """

for filename, content_data in content_library.items():
    filepath = os.path.join(slp_dir, filename)
    if not os.path.exists(filepath): continue

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. CLEAN ARTIFACTS
    html = html.replace('<x-dc>', '').replace('</x-dc>', '')
    html = html.replace('<helmet>', '').replace('</helmet>', '')
    html = re.sub(r'<script src="\./support\.js"></script>\s*', '', html)

    # 2. FIX HEAD (Standardize)
    # The previous injection put the actual head metadata inside the body. We need to grab it and put it in real head.
    head_match = re.search(r'(<meta name="description".*?</style>)', html, re.DOTALL)
    if head_match:
        real_head = head_match.group(1)
        html = html.replace(real_head, '') # remove from body
        # Clean double heads
        html = re.sub(r'</head>\s*</head>', '</head>', html)
        html = html.replace('</head>', f'{real_head}\n</head>')

    # 3. METADATA & SCHEMA (Anti-Duplicate)
    meta = metadata_map[filename]
    html = re.sub(r'<title>.*?</title>', '', html, flags=re.DOTALL)
    html = re.sub(r'<meta name="description".*?>', '', html, flags=re.DOTALL)
    html = re.sub(r'<meta property="og:title".*?>', '', html, flags=re.DOTALL)
    html = re.sub(r'<meta property="og:description".*?>', '', html, flags=re.DOTALL)
    html = re.sub(r'<script type="application/ld\+json">.*?</script>', '', html, flags=re.DOTALL) # remove old
    
    new_meta = f"""
<title>{meta['title']}</title>
<meta name="description" content="{meta['desc']}">
<meta property="og:title" content="{meta['title']}">
<meta property="og:description" content="{meta['desc']}">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "MedicalWebPage",
  "name": "{meta['schema']} en ID Smile",
  "about": {{
    "@type": "MedicalProcedure",
    "name": "{meta['schema']}",
    "procedureType": "SurgicalProcedure",
    "bodyLocation": "Boca",
    "provider": {{
      "@type": "MedicalClinic",
      "name": "ID Smile Cuernavaca",
      "address": "Hospital San Diego, Cuernavaca"
    }}
  }}
}}
</script>
"""
    html = html.replace('<head>', '<head>\n' + new_meta)

    # 4. MEGA MENU
    if "</head>" in html and "nav-dropdown:hover" not in html:
        html = html.replace("</head>", css_injection)
    html = re.sub(r'<nav.*?</nav>', mega_menu_nav_slp, html, count=1, flags=re.DOTALL)

    # 5. CONTENT INJECTION (SLP BODY) + BREADCRUMBS + CTAs + RETURN BUTTON
    pillar, related = clusters[filename]
    
    breadcrumb_html = f"""
    <!-- SEO Breadcrumbs -->
    <nav aria-label="Breadcrumb" class="breadcrumb" style="max-width:1140px;margin:0 auto;padding:16px 16px;font-size:13px;color:#7C838C">
      <ol style="list-style:none;padding:0;margin:0;display:flex;gap:8px">
        <li><a href="IDSmileApertureRemix.dc.html">Inicio</a></li>
        <li><span aria-hidden="true">/</span></li>
        <li><a href="IDSmileApertureRemix.dc.html#servicios">Tratamientos</a></li>
        <li><span aria-hidden="true">/</span></li>
        <li>{pillar}</li>
        <li><span aria-hidden="true">/</span></li>
        <li aria-current="page" style="color:#121417;font-weight:500">{filename.replace('servicio-', '').replace('.html', '').capitalize()}</li>
      </ol>
    </nav>
    """

    specific_cta = f"""
    <!-- Specific CTA -->
    <div style="margin: 48px 0; text-align: center;">
        <a href="{{{{ waUrl }}}}" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;gap:12px;background:#2E9AA0;color:#fff;font-family:'Inter',sans-serif;font-weight:700;font-size:18px;padding:18px 32px;border-radius:99px;box-shadow:0 8px 24px rgba(46,154,160,.28);text-decoration:none;transition:transform .2s,box-shadow .2s" onmouseover="this.style.transform='translateY(-2px)';this.style.boxShadow='0 14px 32px rgba(46,154,160,.36)'" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='0 8px 24px rgba(46,154,160,.28)'">
            <svg viewBox="0 0 24 24" style="width:24px;height:24px;fill:#fff"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.25-1.38a9.9 9.9 0 0 0 4.79 1.22h.01c5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2zm5.8 14.14c-.24.68-1.42 1.31-1.96 1.36-.5.05-.98.24-3.3-.69-2.77-1.09-4.53-3.92-4.67-4.1-.14-.18-1.12-1.49-1.12-2.84 0-1.35.71-2.02.96-2.29a1 1 0 0 1 .73-.34h.52c.17 0 .4-.06.62.47.24.58.81 2 .88 2.14.07.14.12.31.02.5-.44.87-.91.83-.67 1.24.9 1.54 1.79 2.08 3.15 2.76.23.12.37.1.5-.06.14-.16.58-.68.73-.91.15-.23.3-.19.51-.12.21.08 1.33.63 1.56.74.23.12.38.17.44.27.06.1.06.58-.18 1.26z"/></svg>
            {meta['cta']}
        </a>
    </div>
    """

    return_button = """
    <div style="max-width:800px;margin:24px auto;padding:0 24px;text-align:center">
        <a href="IDSmileApertureRemix.dc.html#servicios" style="display:inline-flex;align-items:center;gap:8px;color:#7C838C;text-decoration:none;font-family:'Inter',sans-serif;font-size:15px;padding:12px 24px;border:1px solid #DCDFE3;border-radius:99px;transition:background 0.2s,color 0.2s" onmouseover="this.style.background='#F2F4F6';this.style.color='#121417'" onmouseout="this.style.background='transparent';this.style.color='#7C838C'">
            ← Ver todos los tratamientos
        </a>
    </div>
    """

    new_content_body = f"""
    <main style="max-width:800px;margin:40px auto;padding:32px 24px;background:#ffffff;border-radius:12px;box-shadow:0 4px 20px rgba(0,0,0,0.03);border:1px solid #E7EAEE">
        <h1 style="font-family:'Bricolage Grotesque',sans-serif;font-size:clamp(32px, 5vw, 48px);font-weight:700;line-height:1.1;letter-spacing:-0.03em;margin:0 0 8px;color:#121417">{content_data['title']}</h1>
        <p style="font-family:'IBM Plex Mono',monospace;font-size:13px;color:#2E9AA0;text-transform:uppercase;letter-spacing:1px;margin:0 0 40px">{content_data['subtitle']}</p>
        
        {content_data['body'].replace('<div style="background:#FAFBFC;border:1px solid #DCDFE3', specific_cta + '<div style="background:#FAFBFC;border:1px solid #DCDFE3')}
        {return_button}
    </main>
    """
    
    related_html = generate_related_section(related)

    # Inject
    start_marker = "</header>"
    end_marker = "<footer"
    
    if start_marker in html and end_marker in html:
        before = html.split(start_marker)[0] + start_marker
        after = "<footer" + html.split(end_marker)[1]
        
        html = before + "\n" + breadcrumb_html + "\n" + new_content_body + "\n" + related_html + "\n" + after

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)


# 6. FIX LANDING PAGE (IDSmileApertureRemix.dc.html) MEGA MENU and ANCHORS
landing_path = os.path.join(slp_dir, 'IDSmileApertureRemix.dc.html')
if os.path.exists(landing_path):
    with open(landing_path, 'r', encoding='utf-8') as f:
        landing_html = f.read()

    # Clean artifacts
    landing_html = landing_html.replace('<x-dc>', '').replace('</x-dc>', '')
    landing_html = landing_html.replace('<helmet>', '').replace('</helmet>', '')
    landing_html = re.sub(r'<script src="\./support\.js"></script>\s*', '', landing_html)

    if "</head>" in landing_html and "nav-dropdown:hover" not in landing_html:
        landing_html = landing_html.replace("</head>", css_injection)
    
    landing_html = re.sub(r'<nav.*?</nav>', mega_menu_nav_slp, landing_html, count=1, flags=re.DOTALL)

    with open(landing_path, 'w', encoding='utf-8') as f:
        f.write(landing_html)

# 7. GENERATE SITEMAP AND ROBOTS IN ROOT
sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://recordis-dev.github.io/ID.SmileV1/ui_kits/idsmile_remix/IDSmileApertureRemix.dc.html</loc>
    <lastmod>2026-08-25</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://recordis-dev.github.io/ID.SmileV1/ui_kits/idsmile_remix/servicio-ortodoncia.html</loc>
    <lastmod>2026-08-25</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://recordis-dev.github.io/ID.SmileV1/ui_kits/idsmile_remix/servicio-implantes.html</loc>
    <lastmod>2026-08-25</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://recordis-dev.github.io/ID.SmileV1/ui_kits/idsmile_remix/servicio-odontopediatria.html</loc>
    <lastmod>2026-08-25</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://recordis-dev.github.io/ID.SmileV1/ui_kits/idsmile_remix/servicio-endodoncia.html</loc>
    <lastmod>2026-08-25</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://recordis-dev.github.io/ID.SmileV1/ui_kits/idsmile_remix/servicio-integral.html</loc>
    <lastmod>2026-08-25</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://recordis-dev.github.io/ID.SmileV1/ui_kits/idsmile_remix/servicio-periodoncia.html</loc>
    <lastmod>2026-08-25</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://recordis-dev.github.io/ID.SmileV1/ui_kits/idsmile_remix/servicio-cirugia.html</loc>
    <lastmod>2026-08-25</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://recordis-dev.github.io/ID.SmileV1/ui_kits/idsmile_remix/blog.html</loc>
    <lastmod>2026-08-25</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.6</priority>
  </url>
</urlset>
"""
with open('sitemap.xml', 'w') as f: f.write(sitemap_xml)

robots_txt = """User-agent: *
Allow: /

# Specifically allow AI crawlers
User-agent: GPTBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: Google-Extended
Allow: /

Sitemap: https://recordis-dev.github.io/ID.SmileV1/sitemap.xml
"""
with open('robots.txt', 'w') as f: f.write(robots_txt)

print("In-Situ Self-Healing Loop applied across all files.")
