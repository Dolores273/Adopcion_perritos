# 🐾 Centro de Adopción de Perritos
> Sistema de gestión de adopciones desarrollado con Python y Flask.

Este proyecto es una plataforma web diseñada para conectar a perritos en busca de un hogar con posibles adoptantes. Permite gestionar el catálogo de mascotas, procesar solicitudes y mantener un historial organizado de adopciones.

---

## 🚀 Funcionalidades Principales

* **🐶 Catálogo Dinámico:** Visualización detallada de todos los perritos disponibles.
* **📝 Formulario de Solicitud:** Proceso simplificado para que los usuarios envíen sus datos de interés.
* **📂 Gestión de Datos:** Registro centralizado de mascotas y estados de adopción.
* **📱 Diseño Responsivo:** Interfaz optimizada para navegar desde móviles, tablets o PCs.

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología |
| :--- | :--- |
| **Lenguaje** | Python 3.x |
| **Framework Web** | Flask |
| **Base de Datos** | SQLAlchemy (SQLite) |
| **Frontend** | HTML5, CSS3 & Jinja2 |

---

## 📦 Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

### 1. Preparación del Entorno
Clona el repositorio y accede a la carpeta del proyecto:
```bash
git clone https://github.com/Dolores273/Adopcion_perritos.git
cd Centro_Adopcion
```

### 2. Configuración del Entorno Virtual
Es recomendable usar un entorno aislado para evitar conflictos de dependencias:
```bash
# Crear el entorno
python3 -m venv venv

# Activar el entorno (Linux/macOS)
source venv/bin/activate

# Activar el entorno (Windows)
venv\Scripts\activate
```

### 3. Instalación de Dependencias
Instala todas las librerías necesarias listadas en el archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Ejecución de la Aplicación
Inicia el servidor de desarrollo:
```bash
python3 routes.py
```
> Una vez ejecutado, abre tu navegador en: `http://127.0.0.1:5000`

---

## 📂 Estructura del Proyecto
```text
Centro_Adopcion/
├── static/          # Archivos CSS, imágenes y JS
├── templates/       # Plantillas HTML (Jinja2)
├── models.py        # Definición de la base de datos
├── routes.py        # Lógica de rutas y servidor Flask
├── requirements.txt # Dependencias del proyecto
└── database.db      # Base de datos SQLite (se genera al iniciar)
```

---

## 📄 Licencia
Este proyecto tiene fines estrictamente **educativos**. Puedes utilizarlo como base para aprender Flask o mejorar tus habilidades de desarrollo web.

---
**Nota:** Si encuentras algún error o tienes sugerencias, ¡siéntete libre de abrir un *Pull Request*! 🐕✨
<img width="1846" height="1070" alt="Captura desde 2026-04-09 07-58-42" src="https://github.com/user-attachments/assets/ca66834b-5198-4944-b9dd-4443d6d7f09f" />
<img width="1846" height="1070" alt="Captura desde 2026-04-09 07-58-56" src="https://github.com/user-attachments/assets/510155d5-58a3-4cb0-b6fe-5a56136ff02c" />
<img width="1846" height="1070" alt="Captura desde 2026-04-09 07-59-10" src="https://github.com/user-attachments/assets/27473b2f-db71-47b4-ada9-3db5ea08e4d4" />
