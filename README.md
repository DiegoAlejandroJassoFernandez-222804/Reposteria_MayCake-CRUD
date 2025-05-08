
# 🧁 Repostería May Cake - Sistema CRUD en Django

Este proyecto es una aplicación web básica de gestión para una pastelería. Permite a los usuarios registrarse, ver productos, agregar al carrito y realizar pedidos. Los administradores pueden gestionar productos, usuarios y pedidos desde una vista de administración.

---

## 🔧 Herramientas previas 🔧

- Python 3.12
- Git
- Acceso a terminal/PowerShell
- Visual Studio Code

---

## ESTRUCTURA DEL PROYECTO

```
└── 📁Reposteria_MayCake-CRUD
    └── 📁maycake_project
        └── __init__.py
        └── asgi.py
        └── settings.py
        └── urls.py
        └── wsgi.py
    └── 📁media
        └── 📁productos
            └── Pastel.webp
    └── 📁pedidos
        └── __init__.py
        └── 📁__pycache__
            └── __init__.py
            └── admin.py
            └── apps.py
            └── models.py
            └── urls.py
            └── views.py
        └── admin.py
        └── apps.py
        └── 📁migrations
            └── __init__.py
            └── 📁__pycache__
                └── __init__.py
        └── models.py
        └── 📁templates
            └── 📁pedidos
                └── create.html
                └── detail.html
                └── index.html
                └── update.html
        └── tests.py
        └── urls.py
        └── views.py
    └── 📁productos
        └── __init__.py
        └── 📁__pycache__
            └── __init__.py
            └── admin.py
            └── apps.py
            └── models.py
            └── urls.py
            └── views.py
        └── admin.py
        └── apps.py
        └── 📁migrations
            └── __init__.py
            └── 📁__pycache__
                └── __init__.py
                └── 0001_initial.py
            └── 0001_initial.py
        └── models.py
        └── 📁static
            └── 📁productos
                └── estilos.css
        └── 📁templates
            └── 📁productos
                └── catalogo.html
                └── create.html
                └── detail.html
                └── index.html
                └── lista.html
                └── update.html
        └── tests.py
        └── urls.py
        └── views.py
    └── 📁templates
        └── base.html
    └── 📁usuarios
        └── __init__.py
        └── 📁__pycache__
            └── __init__.py
            └── admin.py
            └── apps.py
            └── models.py
            └── urls.py
            └── views.py
        └── admin.py
        └── apps.py
        └── 📁migrations
            └── __init__.py
            └── 📁__pycache__
                └── __init__.py
        └── models.py
        └── 📁templates
            └── 📁usuarios
                └── create.html
                └── detail.html
                └── index.html
                └── update.html
        └── tests.py
        └── urls.py
        └── views.py
    └── db.sqlite3
    └── Documento de Requisitos.pdf
    └── manage.py
    └── README.md
    └── requirements.txt
```

---

## Pasos realizados para creación de entorno.

### 1. Crear carpeta del proyecto

```bash
mkdir Reposteria_MayCake-CRUD
cd Reposteria_MayCake-CRUD
```

### 2. Crear entorno virtual

```bash
python -m venv env
```

> En Windows:
```bash
env\Scripts\activate
```

> Si falla por políticas de windows, ejecutar en PowerShell:
```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
env\Scripts\activate
```

### 3. Instalar Django

```bash
pip install django
```


## ✅ Estado actual del proyecto ☝️🤓

- [x] Proyecto Django inicializado
- [x] Entorno virtual funcional
- [x] Apps creadas (`productos`, `usuarios`, `pedidos`)
- [x] `.gitignore` configurado
- [x] Proyecto versionado en GitHub
- [x] Estructura preparada para modelos
- [x] Panel de Administrador e ingreso de productos
- [x] Vista de página de catálogo

---

## 🔜 Próximos pasos 👀

1. Crear modelos en cada app
2. Migraciones y base de datos
3. Formularios y vistas CRUD
4. Templates con navegación
5. Autenticación de usuarios
6. Lógica del carrito y pedidos

---
