
# Proyecto de Farmacia con Tkinter y MySQL

Este es un proyecto de aplicación de escritorio para la gestión de los remedios de una farmacia, desarrollado en **Python** utilizando **Tkinter** para la interfaz gráfica y **MySQL** para gestionar la base de datos.



---

## **Estado del proyecto**  
El proyecto está casi terminado, pero aún faltan algunos ajustes y funcionalidades por implementar.

---

## Requisitos

- **Python 3.8 o superior**: [Descargar Python](https://www.python.org/downloads/)
- **XAMPP** para ejecutar el servidor MySQL: [Descargar XAMPP](https://www.apachefriends.org/es/index.html)
- Librerías necesarias para ejecutar el proyecto:

  ```bash
  pip install mysql-connector-python
  pip install tk
  ```



---


## Instalación y Configuración

### 1. Instalar Python
- Descarga e instala Python desde [aquí](https://www.python.org/downloads/).
- Asegúrate de marcar la opción "Add Python to PATH" durante la instalación.
- Para verificar que Python se instaló correctamente, abre una terminal o línea de comandos y ejecuta:

  ```bash
  python --version
  ```

  Esto debería mostrar la versión de Python que instalaste.

### 2. Instalar XAMPP
- Descarga e instala [XAMPP](https://www.apachefriends.org/es/index.html).
- Abre el panel de control de XAMPP y enciende los servicios de **Apache** y **MySQL**.

### 3. Configurar la Base de Datos
- Abre **phpMyAdmin** desde XAMPP en `http://localhost/phpmyadmin`.
- Crea una nueva base de datos llamada `farmacia`.
- Importa el archivo `farmacia.sql` que se encuentra en este repositorio:
  - Haz clic en la pestaña **Importar**.
  - Selecciona el archivo `farmacia.sql`.
  - Haz clic en **Continuar** para importar la estructura y los datos de la base de datos.

---

## Ejecución del Proyecto

1. Asegúrate de que los servicios de **Apache** y **MySQL** estén activos en XAMPP.
2. Ejecuta el archivo principal del proyecto con el siguiente comando:

   ```bash
   python schmer.farmacia_20_10_23.py
   ```

   Esto abrirá la interfaz gráfica de la aplicación, donde podrás interactuar con la base de datos.

---

## Archivos en este Repositorio

- **`schmer.farmacia_20_10_23.py`**: El archivo principal de Python para ejecutar la aplicación.
- **`farmacia.sql`**: El archivo SQL para crear y poblar la base de datos.
- **`imagenes`**: Las imágenes utilizadas en la interfaz gráfica.

---

## Autor

- **Emanuel Schmer**
- Contacto: [emanuelschmer@hotmail.com](mailto:emanuelschmer@hotmail.com)

---

¡Gracias por usar este proyecto! 😊
