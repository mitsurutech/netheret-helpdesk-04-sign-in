# Servicio de asistencia de Netheret, paso 04: inicio de sesión

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

Un ejemplo para enseñar. En dieciséis pasos construimos una aplicación web de servicio de asistencia para Netheret, una empresa inventada que da soporte informático a pequeñas empresas. Este paso permite iniciar y cerrar sesión, y da a cada rol su propio panel.

## Qué añade este paso

- `helpdesk/auth.py`: las páginas para iniciar y cerrar sesión, escritas a mano sin
  ninguna biblioteca extra:
  - la contraseña escrita se comprueba contra el hash guardado;
  - el id del usuario se guarda en la `session` de Flask, una cookie firmada con la
    clave secreta;
  - `load_signed_in_user` se ejecuta antes de cada petición y define `g.user`;
  - `@login_required` y `@role_required(...)` protegen las páginas.
- `SECRET_KEY` en `helpdesk/__init__.py`, leída de una variable de entorno.
- Un panel en `/dashboard` que dice algo distinto para cada rol.
- El menú cambia cuando has iniciado sesión, con un botón Sign out.

## Ejecútalo

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py
flask --app helpdesk run --debug
```

Inicia sesión con cualquier cuenta de demostración, por ejemplo `manager@netheret.example`,
`tier1@netheret.example`, `tier2@netheret.example`, `tier3@netheret.example`
o `customer@brightwell.example`. La contraseña de demostración de todas es
`password123` (solo para los datos de ejemplo).

En un servidor real, primero pondrías una clave secreta larga y aleatoria, por ejemplo
`export SECRET_KEY=...` en macOS y Linux. Sin ella, la aplicación crea una clave aleatoria
nueva cada vez que arranca, así que se cierra tu sesión cuando se reinicia.

## En qué fijarse

- Por qué el error al iniciar sesión nunca dice qué parte estaba mal.
- `session.clear()` antes de guardar el id del usuario: una sesión nueva cada vez.
- Cerrar sesión es un formulario que hace POST, no un enlace.
- Cómo `role_required` es una función que crea un decorador.

## Aprende este paso

Este es el paso 4 de 16 de **Task 2. Developing the solution**, una serie gratuita de lecciones de T Level Digital Software Development, en inglés, que construye el servicio de asistencia de Netheret en sprints ágiles con Python y Flask. Lee la lección de este paso:
[Iniciar sesión, roles y sesiones](https://mitsurutech.co.uk/resources/t-level/dsd-t2-04-sign-in).

- Paso anterior: [paso 03, la base de datos con Flask-SQLAlchemy](https://github.com/mitsurutech/netheret-helpdesk-03-database)
- Paso siguiente: [paso 05, crear una solicitud de soporte](https://github.com/mitsurutech/netheret-helpdesk-05-raise-request)
- [Todas las lecciones gratuitas de T Level Digital](https://mitsurutech.co.uk/resources/t-level)
- [Enseña estas lecciones a tu clase en MitsuruTech](https://mitsurutech.co.uk/es/learning), [mira los precios](https://mitsurutech.co.uk/es/pricing) o
  [empieza un año gratis para tu centro](https://mitsurutech.co.uk/es/signup)

## Acerca de

Escrito por [Mitsuru Technologies](https://mitsurutech.co.uk/es) (MitsuruTech) como ejemplo para enseñar T Level Digital
Software Development. El encargo de Netheret IT Support Solutions procede del material de evaluación de muestra de Pearson; este código
y sus notas son nuestros, y no los publica, respalda ni aprueba Pearson ni el Department for Education.
"T Level" es una marca registrada del Department for Education.
