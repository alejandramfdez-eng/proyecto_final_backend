# 🎬 Movie Management System - Proyecto Final

¡Bienvenido/a a CineApp! Este proyecto Full Stack permite buscar películas en OMDb y consultar sus detalles. El backend expone una API REST para gestionar comentarios y calificaciones, que se guardan localmente en SQLite; el frontend consume la API de forma asíncrona.


## 🚀 Características Principales

*   **API REST Robusta:** Backend rápido y eficiente encargado de las operaciones lógicas y consultas a base de datos.
*   **Búsqueda de películas:** Consulta películas y sus detalles mediante la API de OMDb.
*   **Comentarios y calificaciones:** Crea, consulta, edita y elimina comentarios y calificaciones almacenados en SQLite.
*   **Interfaz dinámica:** Consume la API desde el navegador sin recargar la página.


## 🛠️ Tecnologías Utilizadas

### Backend
*   **Python 3.14+** (Lenguaje principal)
*   **FastAPI** (Framework web asíncrono de alto rendimiento para la API)
*   **Uvicorn** (Servidor ASGI para ejecutar la aplicación)
*   **SQLite** (Motor de base de datos relacional ligero y embebido)
*   **Pydantic** (Validación de datos y modelado)

### Frontend
*   **HTML5** (Estructura semántica)
*   **JavaScript (ES6+)** (Lógica de consumo asíncrono mediante Fetch API)
*   **Bootstrap 5 y CSS** (Estilos y componentes de la interfaz)


## 📂 Estructura del Proyecto

El proyecto está dividido en dos grandes módulos independientes:

```text
├── Proyecto_final_backend/       # Servidor y Base de datos
│   ├── main.py                   # Punto de entrada de la aplicación FastAPI
│   ├── controller.py             # Lógica de negocio y ruteo de endpoints
│   ├── consultas.py              # Capa de datos (Queries SQL detalladas)
│   ├── conexion.py               # Gestión del ciclo de vida de la conexión a la DB
│   ├── create_tables.sql         # Script SQL para la inicialización del esquema
│   ├── bd_movies.db              # Base de datos SQLite local
│   └── requirements.txt          # Dependencias del backend
│
└── Proyecto_final_frontend/      # Interfaz de Usuario (Cliente)
    ├── index.html                # Vista principal de la aplicación
    └── js/
        └── app.js                # Lógica en JS para peticiones fetch al backend
```


## 🔧 Instalación y Configuración

### Prerrequisitos
*   Python 3.14 o superior instalado.
*   Un navegador web moderno.

### Configuración del Backend

1. Desde el directorio que contiene las carpetas `Proyecto_final_backend` y `Proyecto_final_frontend`, entra al backend:
   ```bash
   cd Proyecto_final_backend
   ```

2. Crea un entorno virtual:
   ```bash
   # macOS/Linux
   python3 -m venv entorno
   # Windows
   py -m venv entorno
   ```

3. Activa el entorno virtual:
   *   **En Windows:** `entorno\Scripts\activate`
   *   **En macOS/Linux:** `source entorno/bin/activate`

4. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

5. (Opcional) Para crear las tablas en una base de datos nueva, ejecuta el script SQL. Si `bd_movies.db` ya existe, elimínala primero; esto borrará los comentarios y las calificaciones guardados:
   ```bash
   sqlite3 bd_movies.db < create_tables.sql
   ```

6. Inicia el servidor de desarrollo:
   ```bash
   fastapi dev main.py
   # o alternativamente: uvicorn main:app --reload
   ```
   *El backend estará disponible en `http://127.0.0.1:8000` y la documentación interactiva de Swagger en `http://127.0.0.1:8000/docs`.*

### Configuración del Frontend

1. Dirígete a la carpeta del frontend:
   ```bash
   cd ../Proyecto_final_frontend
   ```
2. Abre el archivo `index.html` en tu navegador o levanta un servidor local rápido (como *Live Server* en VS Code).


## 📌 Endpoints de la API (Resumen)

A continuación se listan las rutas disponibles en la documentación de Swagger. `{id_movies}` corresponde al identificador IMDb de la película; `{qualification_id}` y `{comment_id}` identifican una calificación o comentario.

*   `GET /movies/search?title={title}&year={year}` - Busca películas en OMDb. `year` es opcional.
*   `GET /movies/{id_movies}/details` - Obtiene los detalles de una película desde OMDb.
*   `GET /movies/{id_movies}/qualifications` - Lista las calificaciones de una película.
*   `POST /movies/{id_movies}/qualifications` - Añade una calificación.
*   `PUT /movies/{id_movies}/qualifications/{qualification_id}` - Actualiza una calificación.
*   `DELETE /movies/{id_movies}/qualifications/{qualification_id}` - Elimina una calificación.
*   `GET /movies/{id_movies}/comments` - Lista los comentarios de una película.
*   `POST /movies/{id_movies}/comments` - Añade un comentario.
*   `PUT /movies/{id_movies}/comments/{comment_id}` - Actualiza un comentario.
*   `DELETE /movies/{id_movies}/comments/{comment_id}` - Elimina un comentario.


## 👥 Autor
*   **Alejandra Moscoso Fernandez** 