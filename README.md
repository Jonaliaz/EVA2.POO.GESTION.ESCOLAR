# SISTEMA DE GESTIÓN ESCOLAR

   
> Una solución integral y modular para administrar el ecosistema 
académico de una institución educativa de forma ordenada, rápida y segura.

---

## INTEGRANTES

Equipo de desarrollo del proyecto:

* **Jonathan Aliaz**
* **Leonardo Barriga**
* **Martín**

---

## DESCRIPCIÓN GENERAL

El **Sistema de Gestión Escolar** es una aplicación de consola desarrollada en **Python** bajo el paradigma de **Programación Orientada a Objetos (POO)** y estructurada mediante una **arquitectura en capas** (*Presentación, Negocio, Datos y Auxiliares*). 

Utiliza **Peewee ORM** para la persistencia de datos en una base de datos relacional **MySQL / MariaDB** y **PrettyTable** para ofrecer una visualización limpia y tabulada en terminal.

---

## DEPENDENCIAS

Para su correcto funcionamiento, el proyecto requiere **Python 3.10+** (compatible con Python 3.13) y un servidor de base de datos **MySQL / MariaDB** (por ejemplo, mediante **XAMPP**, **WAMP** o **MySQL Server**).

Las librerías externas utilizadas (especificadas en `requirements.txt`) son:

| Librería | Versión | Propósito en el Proyecto |
| :--- | :---: | :--- |
| **`peewee`** | `3.17.0` | ORM (Object-Relational Mapping) para mapear modelos de Python a tablas MySQL. |
| **`python-decouple`** | `3.8` | Carga segura de variables de entorno desde el archivo `.env`. |
| **`PyMySQL`** | `1.1.0` | Driver de conexión entre Python/Peewee y el motor MySQL/MariaDB. |
| **`prettytable`** | `3.9.0` | Renderizado estético de tablas de datos en la consola. |

---

## PROCEDIMIENTO DE INSTALACIÓN

Para preparar el entorno de desarrollo local, clona o descarga el repositorio y accede a la carpeta del proyecto:

git clone https://github.com/Jonaliaz/EVA2.POO.GESTION.ESCOLAR.git
cd EVA2.POO.GESTION.ESCOLAR

Luego, instala las dependencias necesarias:

pip install -r requirements.txt

Finalmente, crea un archivo llamado .env en la raíz del proyecto y configura las credenciales de conexión a MySQL con la siguiente estructura:

db=poo_eva2
host=localhost
port=3306
user=SU_USUARIO_AQUI
password=SU_CONTRASEÑA_AQUI

Reemplaza SU_USUARIO_AQUI y SU_CONTRASEÑA_AQUI por tus credenciales locales de MySQL. Una vez completados estos pasos, el entorno estará configurado.

---

## PROCEDIMIENTO DE CREACIÓN DE BASE DE DATOS

El proyecto incluye los scripts SQL necesarios dentro del directorio `datos/sql/`:
* `datos/sql/poo_eva2.sql`: Script principal con la estructura de tablas, claves foráneas y datos de prueba precargados (cursos, secciones, alumnos, profesores, apoderados, notas y asistencias).
* `datos/sql/2026.09.08_14.25_DDL_Escuela.sql`: Script DDL con la definición de tablas (incluyendo la tabla `usuario`).

### Pasos para importar en phpMyAdmin / MySQL:
1. Inicia los servicios de Apache y MySQL en tu panel de control (ej. XAMPP).
2. Ingresa a phpMyAdmin o a tu cliente SQL preferido.
3. Crea una nueva base de datos llamada poo_eva2
4. Selecciona la base de datos `poo_eva2`, dirígete a la pestaña sql y pega las sintaxis de creacion de tablas de el archivo datos/sql/2026.09.08_14.25_DDL_Escuela.sql 
5. Luego de crear las tablas inserta los datos iniciales de prueba en la pestaña SQL de /datos/sql/insert_tabla_cursos.sql
---

## USUARIO INICIAL

* **Credenciales de Base de Datos (Local):** Por defecto, en entornos locales como XAMPP se utiliza el usuario de base de datos `root` sin contraseña (configurable en el archivo `.env`).
* **Registros Iniciales Precargados:** Al importar "insert_tabla_cursos.sql", la base de datos cuenta con registros iniciales de prueba listos para consultar (profesores, apoderados, cursos de 1° a 3° año, secciones, alumnos y usuarios). Además, puedes registrar nuevos usuarios del sistema directamente desde la opción **`[5] - Gestión de Usuarios`** del menú principal.

---

## NSTRUCCIONES DE EJECUCIÓN

Una vez instaladas las dependencias, configurada la base de datos y creado tu archivo `.env`, inicia la aplicación ejecutando el archivo principal `main.py` desde la raíz del proyecto:

```bash
python main.py
```

Al ejecutarse, verás en consola el menú interactivo del sistema:

```text
Sistema de Gestión Escolar v1.0.0
===================================

[1] - Gestión de Alumnos
[2] - Gestión de Profesores
[3] - Gestión de Cursos y Secciones
[4] - Gestión Académica (Apoderados, Asignaturas, Contenidos, Evaluaciones, Notas, Asistencia, Clases, Registro)
[5] - Gestión de Usuarios
[0] - Salir
Ingrese su opción:
```

Ingresa el número correspondiente a la categoría que deseas administrar y presiona **ENTER**. Para regresar al menú anterior o salir del sistema de forma segura, ingresa la opción **`0`**.
