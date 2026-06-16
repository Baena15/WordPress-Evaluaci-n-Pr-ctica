#!/usr/bin/env python3
"""Generate Elementor JSON files for UrbanFit Gym inner pages."""
import json
import textwrap


def elementor_json(html: str) -> str:
    return elementor_container_json([{
        "id": "880cdac",
        "elType": "widget",
        "widgetType": "html",
        "settings": {"html": html}
    }])


def elementor_container_json(widgets: list) -> str:
    payload = [{
        "id": "702517e",
        "elType": "container",
        "settings": {"classes": {"$$type": "classes", "value": ["e-588726d"]}},
        "elements": widgets
    }]
    return json.dumps(payload, ensure_ascii=False)


COMMON_HEAD = '''
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Oswald:wght@500;600;700&display=swap" rel="stylesheet">
<style>
.uf-page { font-family: 'Inter', system-ui, sans-serif; color: #18181b; }
.uf-page h1, .uf-page h2, .uf-page h3 { font-family: 'Oswald', sans-serif; font-weight: 700; text-transform: uppercase; letter-spacing: -0.02em; margin: 0 0 16px; }
.uf-page p { margin: 0; line-height: 1.7; }
.uf-page a { text-decoration: none; color: inherit; }
</style>
'''


def hero(title: str, subtitle: str, image: str, height: str = "55vh") -> str:
    return f'''
<div style="position: relative; background: linear-gradient(rgba(15,15,17,0.80), rgba(15,15,17,0.65)), url('/assets/images/{image}') center/cover no-repeat; color: #fff; min-height: {height}; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 100px 24px; box-sizing: border-box;">
  <div style="max-width: 900px;">
    <p style="font-size: 0.9em; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; color: #ff6b35; margin-bottom: 16px;">UrbanFit Gym</p>
    <h1 style="font-size: clamp(40px, 7vw, 72px); line-height: 1.05; margin-bottom: 20px; color: #fff;">{title}</h1>
    <p style="font-size: 1.15em; color: rgba(255,255,255,0.85); max-width: 640px; margin: 0 auto; font-weight: 400;">{subtitle}</p>
  </div>
</div>
'''


def section_title(label: str, title: str) -> str:
    return f'''
<div style="text-align: center; margin-bottom: 50px;">
  <p style="font-size: 0.85em; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; color: #ff6b35; margin-bottom: 10px;">{label}</p>
  <h2 style="font-size: clamp(32px, 5vw, 48px); color: #18181b;">{title}</h2>
</div>
'''


def cta_section() -> str:
    return '''
<div style="background: #ff6b35; color: #fff; text-align: center; padding: 80px 24px;">
  <div style="max-width: 800px; margin: 0 auto;">
    <h2 style="font-size: clamp(32px, 5vw, 48px); margin-bottom: 16px; color: #fff;">¿Listo para empezar?</h2>
    <p style="font-size: 1.15em; margin-bottom: 32px; color: rgba(255,255,255,0.95);">Únete hoy a UrbanFit Gym y da el primer paso hacia una vida más saludable.</p>
    <a href="/contacto/" style="display: inline-block; background: #18181b; color: #fff; padding: 18px 40px; border-radius: 4px; font-weight: 700; font-size: 1rem; letter-spacing: 0.05em; text-transform: uppercase;">Contacta con nosotros</a>
  </div>
</div>
'''


SVG_DUMBBELL = '''<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ff6b35" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M6.5 6.5l11 11"/><path d="M21 21l-1-1"/><path d="M3 3l1 1"/><path d="M18 22l4-4"/><path d="M2 6l4-4"/><path d="M3 10l4-4"/><path d="M14 21l4-4"/></svg>'''
SVG_BIKE = '''<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ff6b35" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="5.5" cy="17.5" r="3.5"/><circle cx="18.5" cy="17.5" r="3.5"/><path d="M15 6a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm-3 11.5V14l-3-3 4-3 2 3h2"/><path d="M8 14.5v.5"/></svg>'''
SVG_USER = '''<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ff6b35" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>'''
SVG_CHART = '''<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ff6b35" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/></svg>'''
SVG_APPLE = '''<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ff6b35" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20.94c1.5 0 2.75 1.06 4 1.06 3 0 6-8 6-12.22A4.91 4.91 0 0 0 17 5c-2.22 0-4 1.44-5 2-1-.56-2.78-2-5-2a4.9 4.9 0 0 0-5 4.78C2 14 5 22 8 22c1.25 0 2.5-1.06 4-1.06Z"/><path d="M10 2c1 .5 2 2 2 5"/></svg>'''
SVG_HEART = '''<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ff6b35" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/></svg>'''
SVG_LOCATION = '''<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#ff6b35" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>'''
SVG_PHONE = '''<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#ff6b35" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'''
SVG_MAIL = '''<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#ff6b35" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>'''
SVG_CLOCK = '''<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#ff6b35" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>'''
SVG_CHECK = '''<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#ff6b35" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>'''


def nosotros_page() -> str:
    return f'''
{COMMON_HEAD}
<div class="uf-page">
{hero("Conócenos", "Más que un gimnasio: una comunidad que entrena, mejora y crece junta.", "team-training.jpg", "60vh")}

<div style="max-width: 1200px; margin: 0 auto; padding: 90px 24px;">
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 60px; align-items: center;">
    <div>
      <p style="font-size: 0.85em; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; color: #ff6b35; margin-bottom: 10px;">Nuestra historia</p>
      <h2 style="font-size: clamp(28px, 4vw, 40px); margin-bottom: 20px;">De una idea a una comunidad</h2>
      <p style="color: #4b5563; margin-bottom: 20px;">UrbanFit Gym nació en 2018 con una misión clara: crear un espacio donde cualquier persona pudiera entrenar, mejorar y sentirse parte de algo más grande. Desde entonces, hemos acompañado a cientos de socios en su camino hacia un estilo de vida más saludable.</p>
      <p style="color: #4b5563;">Creemos que el deporte transforma vidas. Por eso combinamos instalaciones de primera, entrenadores certificados y un ambiente inclusivo donde todos pueden crecer.</p>
    </div>
    <div style="border-radius: 12px; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.12);">
      <img src="/assets/images/hero-gym.jpg" alt="Interior de UrbanFit Gym" style="width: 100%; height: auto; display: block;">
    </div>
  </div>
</div>

<div style="background: #f3f4f6; padding: 90px 24px;">
  <div style="max-width: 1200px; margin: 0 auto;">
    {section_title("Filosofía", "Misión, visión y valores")}
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px;">
      <div style="background: #fff; padding: 40px 30px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
        <h3 style="font-size: 1.4rem; color: #ff6b35; margin-bottom: 12px;">Misión</h3>
        <p style="color: #4b5563;">Ofrecer un entorno profesional, motivador y accesible para que cada persona alcance sus objetivos de salud y bienestar, independientemente de su nivel de partida.</p>
      </div>
      <div style="background: #fff; padding: 40px 30px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
        <h3 style="font-size: 1.4rem; color: #ff6b35; margin-bottom: 12px;">Visión</h3>
        <p style="color: #4b5563;">Ser el gimnasio de referencia en nuestra ciudad, reconocido por la calidad de nuestros servicios, la cercanía con nuestros socios y los resultados que logramos juntos.</p>
      </div>
      <div style="background: #fff; padding: 40px 30px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
        <h3 style="font-size: 1.4rem; color: #ff6b35; margin-bottom: 12px;">Valores</h3>
        <p style="color: #4b5563;">Compromiso, profesionalidad, comunidad e innovación. Cuatro pilares que guían cada decisión y cada entrenamiento en UrbanFit Gym.</p>
      </div>
    </div>
  </div>
</div>

<div style="max-width: 1200px; margin: 0 auto; padding: 90px 24px;">
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 24px; text-align: center;">
    <div style="padding: 30px;">
      <p style="font-size: 3rem; font-family: 'Oswald', sans-serif; font-weight: 700; color: #ff6b35; line-height: 1;">8+</p>
      <p style="font-size: 0.85em; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: #6b7280; margin-top: 8px;">Años de experiencia</p>
    </div>
    <div style="padding: 30px;">
      <p style="font-size: 3rem; font-family: 'Oswald', sans-serif; font-weight: 700; color: #ff6b35; line-height: 1;">1.200+</p>
      <p style="font-size: 0.85em; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: #6b7280; margin-top: 8px;">Socios activos</p>
    </div>
    <div style="padding: 30px;">
      <p style="font-size: 3rem; font-family: 'Oswald', sans-serif; font-weight: 700; color: #ff6b35; line-height: 1;">15</p>
      <p style="font-size: 0.85em; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: #6b7280; margin-top: 8px;">Entrenadores</p>
    </div>
    <div style="padding: 30px;">
      <p style="font-size: 3rem; font-family: 'Oswald', sans-serif; font-weight: 700; color: #ff6b35; line-height: 1;">800m²</p>
      <p style="font-size: 0.85em; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: #6b7280; margin-top: 8px;">De instalaciones</p>
    </div>
  </div>
</div>

{cta_section()}
</div>
'''


def servicios_page() -> str:
    cards = [
        (SVG_DUMBBELL, "Sala de musculación", "Máquinas de última generación, mancuernas, barras y zona de peso libre. Todo lo que necesitas para ganar fuerza y tono muscular."),
        (SVG_BIKE, "Clases dirigidas", "Spinning, body pump, yoga, pilates y HIIT. Horarios de mañana y tarde para adaptarnos a tu rutina."),
        (SVG_USER, "Entrenamiento personal", "Evaluación inicial, planificación periódica y seguimiento cercano con entrenadores certificados."),
        (SVG_CHART, "Valoración física", "Mediciones, test de condición física y análisis de composición corporal para diseñar tu plan ideal."),
        (SVG_APPLE, "Asesoramiento nutricional", "Complementa tu entrenamiento con pautas nutricionales personalizadas de la mano de nuestros expertos."),
        (SVG_HEART, "Zona de bienestar", "Relájate después de entrenar en nuestra zona de estiramientos, recuperación activa y saunas."),
    ]
    cards_html = "\n".join(f'''
      <div style="background: #fff; padding: 40px 30px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); transition: transform .2s;">
        <div style="margin-bottom: 20px;">{icon}</div>
        <h3 style="font-size: 1.3rem; margin-bottom: 12px;">{title}</h3>
        <p style="color: #4b5563;">{desc}</p>
      </div>
''' for icon, title, desc in cards)

    features = [
        "Más de 45 clases semanales",
        "Entrenadores certificados",
        "Instalaciones renovadas en 2024",
        "Horario flexible de 06:00 a 23:00",
    ]
    features_html = "\n".join(f'''
        <li style="display: flex; align-items: flex-start; gap: 12px; margin-bottom: 16px; color: #374151;">
          <span style="flex-shrink: 0;">{SVG_CHECK}</span>
          <span style="font-weight: 500;">{f}</span>
        </li>
''' for f in features)

    return f'''
{COMMON_HEAD}
<div class="uf-page">
{hero("Servicios", "Todo lo que necesitas para entrenar, mejorar y cuidar de ti.", "gym-equipment.jpg", "60vh")}

<div style="max-width: 1200px; margin: 0 auto; padding: 90px 24px;">
  {section_title("Qué ofrecemos", "Entrenamiento sin límites")}
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
    {cards_html}
  </div>
</div>

<div style="background: #f3f4f6; padding: 90px 24px;">
  <div style="max-width: 1200px; margin: 0 auto;">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 60px; align-items: center;">
      <div style="border-radius: 12px; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.12);">
        <img src="/assets/images/group-class.jpg" alt="Clases dirigidas en UrbanFit Gym" style="width: 100%; height: auto; display: block;">
      </div>
      <div>
        <p style="font-size: 0.85em; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; color: #ff6b35; margin-bottom: 10px;">Por qué elegirnos</p>
        <h2 style="font-size: clamp(28px, 4vw, 40px); margin-bottom: 24px;">Entrena a tu ritmo, con el mejor equipo</h2>
        <ul style="list-style: none; padding: 0; margin: 0;">
          {features_html}
        </ul>
      </div>
    </div>
  </div>
</div>

<div style="max-width: 1100px; margin: 0 auto; padding: 90px 24px; text-align: center;">
  <p style="font-size: 0.85em; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; color: #ff6b35; margin-bottom: 10px;">Planes</p>
  <h2 style="font-size: clamp(32px, 5vw, 48px); margin-bottom: 40px;">Empieza hoy</h2>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 30px;">
    <div style="background: #fff; border: 1px solid #e5e7eb; border-radius: 12px; padding: 40px 30px;">
      <h3 style="font-size: 1.2rem; color: #6b7280;">Básico</h3>
      <p style="font-size: 2.5rem; font-family: 'Oswald', sans-serif; font-weight: 700; color: #18181b; margin: 16px 0;">29€<span style="font-size: 1rem; font-family: 'Inter', sans-serif; font-weight: 400; color: #6b7280;">/mes</span></p>
      <p style="color: #4b5563; margin-bottom: 24px;">Acceso a sala de musculación y zona cardio en horario completo.</p>
      <a href="/contacto/" style="display: inline-block; border: 2px solid #18181b; color: #18181b; padding: 14px 28px; border-radius: 4px; font-weight: 700; text-transform: uppercase; font-size: 0.9rem;">Elegir plan</a>
    </div>
    <div style="background: #18181b; color: #fff; border-radius: 12px; padding: 50px 30px; transform: scale(1.03); box-shadow: 0 20px 40px rgba(0,0,0,0.2);">
      <h3 style="font-size: 1.2rem; color: #ff6b35;">Premium</h3>
      <p style="font-size: 2.5rem; font-family: 'Oswald', sans-serif; font-weight: 700; margin: 16px 0;">49€<span style="font-size: 1rem; font-family: 'Inter', sans-serif; font-weight: 400; color: #9ca3af;">/mes</span></p>
      <p style="color: #d1d5db; margin-bottom: 24px;">Todo lo del plan Básico + clases dirigidas ilimitadas y valoración física.</p>
      <a href="/contacto/" style="display: inline-block; background: #ff6b35; color: #fff; padding: 14px 28px; border-radius: 4px; font-weight: 700; text-transform: uppercase; font-size: 0.9rem;">Elegir plan</a>
    </div>
    <div style="background: #fff; border: 1px solid #e5e7eb; border-radius: 12px; padding: 40px 30px;">
      <h3 style="font-size: 1.2rem; color: #6b7280;">Elite</h3>
      <p style="font-size: 2.5rem; font-family: 'Oswald', sans-serif; font-weight: 700; color: #18181b; margin: 16px 0;">79€<span style="font-size: 1rem; font-family: 'Inter', sans-serif; font-weight: 400; color: #6b7280;">/mes</span></p>
      <p style="color: #4b5563; margin-bottom: 24px;">Incluye 4 sesiones de entrenamiento personal y asesoramiento nutricional.</p>
      <a href="/contacto/" style="display: inline-block; border: 2px solid #18181b; color: #18181b; padding: 14px 28px; border-radius: 4px; font-weight: 700; text-transform: uppercase; font-size: 0.9rem;">Elegir plan</a>
    </div>
  </div>
</div>

{cta_section()}
</div>
'''


def blog_page() -> str:
    top = f'''
{COMMON_HEAD}
<div class="uf-page">
{hero("Blog", "Consejos, rutinas y noticias para llevar tu entrenamiento al siguiente nivel.", "personal-trainer.jpg", "60vh")}

<div style="max-width: 1200px; margin: 0 auto; padding: 90px 24px 40px;">
  {section_title("Contenido", "Últimas publicaciones")}
</div>
<div style="max-width: 1200px; margin: 0 auto; padding: 0 24px 90px;">
'''
    bottom = '''
</div>

<div style="background: #f3f4f6; padding: 90px 24px;">
  <div style="max-width: 1100px; margin: 0 auto;">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 24px; text-align: center;">
      <div style="background: #fff; padding: 32px 24px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
        <h3 style="font-size: 1.1rem; color: #ff6b35; margin-bottom: 10px;">Entrenamiento</h3>
        <p style="color: #4b5563; font-size: 0.95rem;">Rutinas, técnica y progresión de cargas para todos los niveles.</p>
      </div>
      <div style="background: #fff; padding: 32px 24px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
        <h3 style="font-size: 1.1rem; color: #ff6b35; margin-bottom: 10px;">Nutrición</h3>
        <p style="color: #4b5563; font-size: 0.95rem;">Consejos alimenticios para acompañar tu esfuerzo en el gimnasio.</p>
      </div>
      <div style="background: #fff; padding: 32px 24px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
        <h3 style="font-size: 1.1rem; color: #ff6b35; margin-bottom: 10px;">Bienestar</h3>
        <p style="color: #4b5563; font-size: 0.95rem;">Hábitos saludables, descanso y motivación para el día a día.</p>
      </div>
    </div>
  </div>
</div>

<div style="background: #18181b; color: #fff; padding: 80px 24px; text-align: center;">
  <div style="max-width: 700px; margin: 0 auto;">
    <h2 style="font-size: clamp(28px, 4vw, 40px); margin-bottom: 16px; color: #fff;">¿No quieres perderte nada?</h2>
    <p style="color: #d1d5db; margin-bottom: 28px;">Suscríbete para recibir nuestras mejores rutinas y consejos de nutrición.</p>
    <a href="/contacto/" style="display: inline-block; background: #ff6b35; color: #fff; padding: 16px 36px; border-radius: 4px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em;">Suscribirme</a>
  </div>
</div>
</div>
'''
    return elementor_container_json([
        {"id": "880cdac", "elType": "widget", "widgetType": "html", "settings": {"html": top}},
        {"id": "a1b2c3d", "elType": "widget", "widgetType": "shortcode", "settings": {"shortcode": "[urbanfit_recent_posts]"}},
        {"id": "d4e5f6g", "elType": "widget", "widgetType": "html", "settings": {"html": bottom}}
    ])


def home_page() -> str:
    return f'''
{COMMON_HEAD}
<style>
@keyframes uf-bounce {{ 0%,100%{{transform:translateY(0)}} 50%{{transform:translateY(10px)}} }}
@keyframes uf-fade {{ from{{opacity:0; transform:translateY(20px)}} to{{opacity:1; transform:translateY(0)}} }}
.uf-hero {{ animation: uf-fade 1s ease-out; }}
.uf-scroll {{ animation: uf-bounce 2s infinite; }}
</style>
<div class="uf-page">

<!-- Hero Pro -->
<div style="position: relative; background: linear-gradient(135deg, rgba(15,15,17,0.92) 0%, rgba(15,15,17,0.70) 50%, rgba(255,107,53,0.25) 100%), url('/assets/images/hero-gym.jpg') center/cover no-repeat; color: #fff; min-height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 140px 24px 100px; box-sizing: border-box;">
  <div class="uf-hero" style="max-width: 980px; position: relative; z-index: 2;">
    <div style="display: inline-flex; align-items: center; gap: 10px; background: rgba(255,107,53,0.15); border: 1px solid rgba(255,107,53,0.35); color: #ff6b35; padding: 10px 20px; border-radius: 50px; font-size: 0.8rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 24px; backdrop-filter: blur(4px);">
      <span style="font-size: 1.1em;">★</span> Más de 1.200 socios confían en nosotros
    </div>
    <h1 style="font-size: clamp(44px, 9vw, 96px); line-height: 0.98; margin-bottom: 24px; color: #fff; text-shadow: 0 4px 30px rgba(0,0,0,0.4);">Transforma tu cuerpo.<br><span style="color: #ff6b35;">Supera tus límites.</span></h1>
    <p style="font-size: clamp(1.1rem, 2vw, 1.4rem); color: rgba(255,255,255,0.9); max-width: 700px; margin: 0 auto 36px; font-weight: 400;">Entrena con equipamiento profesional, entrenadores certificados y una comunidad que te impulsa a dar lo mejor de ti. Tu cambio empieza hoy.</p>

    <div style="display: flex; flex-wrap: wrap; gap: 16px; justify-content: center; margin-bottom: 36px;">
      <a href="/contacto/" style="display: inline-block; background: #ff6b35; color: #fff; padding: 20px 42px; text-decoration: none; border-radius: 4px; font-weight: 700; font-size: 1rem; letter-spacing: 0.05em; text-transform: uppercase; box-shadow: 0 10px 30px rgba(255,107,53,0.35); transition: transform .2s;">Empezar ahora</a>
      <a href="/servicios/" style="display: inline-block; background: transparent; color: #fff; padding: 20px 42px; text-decoration: none; border-radius: 4px; font-weight: 700; font-size: 1rem; letter-spacing: 0.05em; text-transform: uppercase; border: 2px solid rgba(255,255,255,0.5); transition: all .2s;">Ver servicios</a>
    </div>

    <form action="/contacto/" method="get" style="max-width: 520px; margin: 0 auto 40px; display: flex; flex-wrap: wrap; gap: 10px; background: rgba(255,255,255,0.1); padding: 8px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.15); backdrop-filter: blur(6px);">
      <input type="email" name="email" placeholder="Tu email" required style="flex: 1; min-width: 220px; padding: 16px 18px; border: none; border-radius: 4px; background: rgba(0,0,0,0.35); color: #fff; font-size: 1rem; outline: none;">
      <button type="submit" style="padding: 16px 28px; border: none; border-radius: 4px; background: #fff; color: #18181b; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; cursor: pointer;">Quiero info</button>
    </form>
  </div>

  <div style="position: absolute; bottom: 30px; left: 50%; transform: translateX(-50%); z-index: 2;" class="uf-scroll">
    <a href="#inicio-contenido" style="color: rgba(255,255,255,0.7); display: flex; flex-direction: column; align-items: center; gap: 6px; font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase;">
      <span>Descubre más</span>
      <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M19 12l-7 7-7-7"/></svg>
    </a>
  </div>

  <div style="position: absolute; bottom: 0; left: 0; right: 0; background: rgba(15,15,17,0.85); border-top: 1px solid rgba(255,255,255,0.08); padding: 30px 24px; z-index: 2;">
    <div style="max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 24px; text-align: center;">
      <div>
        <p style="font-size: 1.6rem; font-family: 'Oswald', sans-serif; font-weight: 700; color: #ff6b35;">8+</p>
        <p style="font-size: 0.75rem; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: rgba(255,255,255,0.7);">Años de experiencia</p>
      </div>
      <div>
        <p style="font-size: 1.6rem; font-family: 'Oswald', sans-serif; font-weight: 700; color: #ff6b35;">1.200+</p>
        <p style="font-size: 0.75rem; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: rgba(255,255,255,0.7);">Socios activos</p>
      </div>
      <div>
        <p style="font-size: 1.6rem; font-family: 'Oswald', sans-serif; font-weight: 700; color: #ff6b35;">45+</p>
        <p style="font-size: 0.75rem; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: rgba(255,255,255,0.7);">Clases semanales</p>
      </div>
      <div>
        <p style="font-size: 1.6rem; font-family: 'Oswald', sans-serif; font-weight: 700; color: #ff6b35;">15</p>
        <p style="font-size: 0.75rem; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: rgba(255,255,255,0.7);">Entrenadores</p>
      </div>
    </div>
  </div>
</div>

<div id="inicio-contenido">

<div style="max-width: 1200px; margin: 0 auto; padding: 90px 24px;">
  {section_title("Nuestros servicios", "Todo para tu entrenamiento")}
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px;">
    <div style="background: #fff; padding: 40px 30px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); text-align: center;">
      <div style="margin-bottom: 18px;">{SVG_DUMBBELL}</div>
      <h3 style="font-size: 1.25rem; margin-bottom: 10px;">Sala de musculación</h3>
      <p style="color: #4b5563;">Máquinas y pesos libres de última generación para entrenar todos los grupos musculares con seguridad.</p>
    </div>
    <div style="background: #fff; padding: 40px 30px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); text-align: center;">
      <div style="margin-bottom: 18px;">{SVG_BIKE}</div>
      <h3 style="font-size: 1.25rem; margin-bottom: 10px;">Clases dirigidas</h3>
      <p style="color: #4b5563;">Spinning, HIIT, yoga, body pump y más disciplinas con monitores especializados y energía de sobra.</p>
    </div>
    <div style="background: #fff; padding: 40px 30px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); text-align: center;">
      <div style="margin-bottom: 18px;">{SVG_USER}</div>
      <h3 style="font-size: 1.25rem; margin-bottom: 10px;">Entrenamiento personal</h3>
      <p style="color: #4b5563;">Planes a medida, seguimiento de progreso y asesoramiento nutricional para alcanzar tus objetivos.</p>
    </div>
  </div>
</div>

<div style="background: #f3f4f6; padding: 90px 24px;">
  <div style="max-width: 1200px; margin: 0 auto;">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 60px; align-items: center;">
      <div style="border-radius: 12px; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.12);">
        <img src="/assets/images/gym-floor.jpg" alt="Instalaciones UrbanFit Gym" style="width: 100%; height: auto; display: block;">
      </div>
      <div>
        <p style="font-size: 0.85em; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; color: #ff6b35; margin-bottom: 10px;">Instalaciones</p>
        <h2 style="font-size: clamp(28px, 4vw, 40px); margin-bottom: 20px;">Espacios diseñados para rendir</h2>
        <p style="color: #4b5563; margin-bottom: 20px;">Más de 800 m² distribuidos en zona de cardio, musculación, sala polivalente para clases y zona de entrenamiento funcional. Ventilación, iluminación y equipamiento pensados para que cada sesión sea cómoda y efectiva.</p>
        <ul style="list-style: none; padding: 0; margin: 0;">
          <li style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px; color: #374151; font-weight: 500;">{SVG_CHECK} Zona de cardio con vistas</li>
          <li style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px; color: #374151; font-weight: 500;">{SVG_CHECK} Vestuarios con duchas privadas</li>
          <li style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px; color: #374151; font-weight: 500;">{SVG_CHECK} Sala de clases con aforo limitado</li>
          <li style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px; color: #374151; font-weight: 500;">{SVG_CHECK} Parking gratuito para socios</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<div style="max-width: 1200px; margin: 0 auto; padding: 90px 24px;">
  {section_title("Testimonios", "Lo que dicen nuestros socios")}
  <div style="background: #fff; border-radius: 16px; box-shadow: 0 10px 40px rgba(0,0,0,0.08); padding: 50px 40px; max-width: 800px; margin: 0 auto; text-align: center; position: relative;">
    <div style="font-size: 4rem; color: rgba(255,107,53,0.2); line-height: 1; position: absolute; top: 20px; left: 30px;">“</div>
    <p style="font-size: 1.25rem; font-style: italic; color: #374151; line-height: 1.8; margin-bottom: 24px;">Llevo seis meses entrenando en UrbanFit y los resultados son increíbles. El ambiente es inmejorable, los entrenadores se implican de verdad y las instalaciones están siempre impecables.</p>
    <p style="font-weight: 700; color: #18181b;">— María G.</p>
  </div>
</div>

{cta_section()}

</div>
</div>
'''


def contacto_page() -> str:
    return f'''
{COMMON_HEAD}
<div class="uf-page">
{hero("Contacto", "Estamos aquí para ayudarte. Escríbenos, llámanos o pásate por el gimnasio.", "dumbbells.jpg", "55vh")}

<div style="max-width: 1200px; margin: 0 auto; padding: 90px 24px;">
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 50px; align-items: start;">
    <div>
      {section_title("Información", "Habla con nosotros")}
      <div style="display: flex; flex-direction: column; gap: 28px; margin-top: 40px;">
        <div style="display: flex; gap: 18px; align-items: flex-start;">
          <div style="background: rgba(255,107,53,0.1); padding: 12px; border-radius: 10px;">{SVG_LOCATION}</div>
          <div>
            <h3 style="font-size: 1.1rem; margin-bottom: 6px;">Dirección</h3>
            <p style="color: #4b5563;">Calle Fitness, 123<br>30001 Ciudad deportiva</p>
          </div>
        </div>
        <div style="display: flex; gap: 18px; align-items: flex-start;">
          <div style="background: rgba(255,107,53,0.1); padding: 12px; border-radius: 10px;">{SVG_PHONE}</div>
          <div>
            <h3 style="font-size: 1.1rem; margin-bottom: 6px;">Teléfono</h3>
            <p style="color: #4b5563;"><a href="tel:+34900123456" style="color: #ff6b35; font-weight: 600;">+34 900 123 456</a></p>
          </div>
        </div>
        <div style="display: flex; gap: 18px; align-items: flex-start;">
          <div style="background: rgba(255,107,53,0.1); padding: 12px; border-radius: 10px;">{SVG_MAIL}</div>
          <div>
            <h3 style="font-size: 1.1rem; margin-bottom: 6px;">Email</h3>
            <p style="color: #4b5563;"><a href="mailto:info@urbanfitgym.local" style="color: #ff6b35; font-weight: 600;">info@urbanfitgym.local</a></p>
          </div>
        </div>
        <div style="display: flex; gap: 18px; align-items: flex-start;">
          <div style="background: rgba(255,107,53,0.1); padding: 12px; border-radius: 10px;">{SVG_CLOCK}</div>
          <div>
            <h3 style="font-size: 1.1rem; margin-bottom: 6px;">Horario</h3>
            <p style="color: #4b5563;">Lunes a Viernes: 06:00 - 23:00<br>Sábados y Domingos: 08:00 - 14:00</p>
          </div>
        </div>
      </div>
    </div>

    <div style="background: #fff; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); padding: 40px;">
      <h2 style="font-size: 1.6rem; margin-bottom: 24px;">Envíanos un mensaje</h2>
      [contact-form-7 id="24" title="Formulario de contacto"]
    </div>
  </div>
</div>

<div style="max-width: 1200px; margin: 0 auto 90px; padding: 0 24px;">
  <div style="border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.08);">
    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3151.835434509374!2d144.9537353153167!3d-37.81732767975171!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6ad65d4c2b349649%3A0xb6899234e561db11!2sEnvato!5e0!3m2!1ses!2ses!4v1620000000000!5m2!1ses!2ses" width="100%" height="420" style="border:0; display: block;" allowfullscreen="" loading="lazy"></iframe>
  </div>
</div>

{cta_section()}
</div>
'''


def main():
    pages = {
        "elementor-home.json": home_page(),
        "elementor-nosotros.json": nosotros_page(),
        "elementor-servicios.json": servicios_page(),
        "elementor-blog.json": blog_page(),
        "elementor-contacto.json": contacto_page(),
    }
    for filename, content in pages.items():
        with open(filename, "w", encoding="utf-8") as f:
            # blog_page already returns the full Elementor JSON
            if isinstance(content, str) and content.strip().startswith("["):
                f.write(content)
            else:
                f.write(elementor_json(content))
        print(f"Generated {filename}")


if __name__ == "__main__":
    main()
