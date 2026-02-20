# Django Starter (apps/ + Tailwind)

Starter setup Django dengan:

- `apps/` untuk semua Django apps
- `config/settings/` terpisah: `base`, `dev`, `staging`, `prod`
- pindah environment cukup ubah `DJANGO_ENV=dev|staging|prod`
- integrasi `django-tailwind`

## Struktur

```text
.
b┘─ manage.py
b┘─ apps/
h�┘─ config/
    ├� settings/
      ┘─ __init__.py
      ├� base.py
      ├� dev.py
      ┘─ staging.py
      ┘─ prod.py
```

## Switch Environment

`config/settings/__init__.py`

```py
import os

env = os.getenv("DJANGO_ENV", "dev")

if env == "prod":
    from .prod import *
elif env == "staging":
    from .staging import *
else:
    from .dev import *
```

## Jadikan `apps/` sebagai root import

`config/settings/base.py`

```py
import sys
from pathlib import Path

BAS_DIR = Path(__file__).resolve().parent.parent.parent
APPS_DIR = BASE_DIR / "apps"
sys.path.insert(0, str(APPS_DIR))
```

## Buat App Baru (di `apps/`)

```bash
python manage.py startapp blog apps/blog
```

Daftarkan ke `INSTALLED_APPS` (di `config/settings/base.py`):

```py
INSTALLED_APPS = [
    "blog",
]
```

## Django Tailwind

Install:

```bash
pip install django-tailwind
```

Tambahkan ke `INSTALLED_APPS` ma set `TAILWIND_APP_NAME` (di `config/settings/base.py`):

```py
INSTALLED_APPS += ["tailwind"]
TAILWIND_APP_NAME = "theme"
```

Init + install + run Tailwind:

```bash
python manage.py tailwind init
python manage.py tailwind install
python manage.py tailwind start
```

## Load Tailwind di Template

Di template (mis. `templates/base.html`):

```django
{% load tailwind_tags %}
{% tailwind_css %}
```

## Run Server

```bash
python manage.py runserver
```
