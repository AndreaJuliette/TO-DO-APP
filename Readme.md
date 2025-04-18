
# 📝 To-Do App en Python

Una aplicación básica de tareas pendientes (To-Do) desarrollada en Python usando `tkinter`, `customtkinter` y `sqlite3` para la interfaz gráfica y el almacenamiento local.

## 📌 Características

- Añadir tareas con un solo clic
- Marcar tareas como completadas
- Editar tareas directamente desde la interfaz
- Eliminar tareas fácilmente
- Guardado persistente usando SQLite

## 🛠️ Tecnologías utilizadas

- Python 3
- [tkinter](https://docs.python.org/3/library/tkinter.html) – Librería estándar para interfaces gráficas en Python
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter) – Estilo moderno para tkinter
- sqlite3 – Base de datos local ligera

## 🧠 Estructura del proyecto

```bash
📁 todo-app/
├── main.py           # Archivo principal que lanza la aplicación
├── todo.db           # Base de datos SQLite (generada automáticamente)
└── README.md         # Documentación del proyecto
```

## 🚀 Cómo usar

1. Clona este repositorio:

```bash
git clone https://github.com/tu-usuario/todo-app.git
cd todo-app
```

2. Instala los requisitos (solo `customtkinter`, ya que `tkinter` y `sqlite3` vienen con Python):

```bash
pip install customtkinter
```

3. Ejecuta la aplicación:

```bash
python main.py
```

## 📷 Captura de pantalla

![image](https://github.com/user-attachments/assets/cf5e1136-adaf-4e53-bbe7-44618c41b40f)


## 🗃️ Base de datos

La base de datos `todo.db` se crea automáticamente y contiene una tabla llamada `TODO` con los siguientes campos:

- `idTodo`: ID único de la tarea (autoincremental)
- `texto`: Contenido de la tarea
- `checkTODO`: Booleano que indica si la tarea está marcada como completada

## 🧹 Mejoras futuras

- Filtro de tareas completadas/pendientes
- Guardado automático al editar texto
- Soporte para múltiples listas de tareas
- Exportación de tareas

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

---

¡Gracias por revisar este proyecto! Si te gusta, no dudes en darle una ⭐ en GitHub.
