import os

import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings.production")
django.setup()

HTML_PATH = settings.TEMPLATE_DIR / "index.html"
DJANGO_LOAD_STATIC = "{% load static %}"
HREF = 'href="./static/'
SRC = 'src="./static/'


def fix_html():
    with open(HTML_PATH, "r+") as f:
        data = f.read()
        data = data[:15] + DJANGO_LOAD_STATIC + data[15:]
        fixed_data = add_django_static_to_files(data)
        f.seek(0)
        f.write(fixed_data)
        f.truncate()


def add_django_static_to_files(data):
    for i in range(len(data)):
        if data[i : i + len(HREF)] == HREF:
            data, i = fix_static(data, i, 6, HREF)

        elif data[i : i + len(SRC)] == SRC:
            data, i = fix_static(data, i, 5, SRC)
    return data


def fix_static(data, i, length, val):
    data = data[: i + length] + "{% static '" + data[i + len(val) :]
    i += len(val)
    while True:
        if data[i] == '"':
            data = data[:i] + "' %}" + data[i:]
            break
        else:
            i += 1
    return data, i


if __name__ == "__main__":
    fix_html()
    print("Html Fixed")
