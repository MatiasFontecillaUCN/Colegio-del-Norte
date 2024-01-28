# Backend [Colegio del Norte] #

El Backend del proyecto Colegio del Norte esto desarrollado en Flask, un framework de Python para el desarrollo de aplicaciones web, utilizando una base de datos MySQL.

### Requisitos Previos ###

* Haber instalado Python
* Haber instalado MySQL
* Haber instalado Pip

### Paso 1: Descargar o clonar el repositorio ###
Puede descargar el repositorio como un archivo ZIP o clonarlo usando Git en su terminal:

```+
$ git clone https://vale9@bitbucket.org/equipo-bola8/backend.git
```

### Paso 2: Instalacion ###
Entrar a la carpeta del proyecto:
```+
cd backend
```

Instalar y crear el entorno virtual:

```+
<!-- Quizas hay que cambiarlo, quitarle el 3 a python -->
python3 -m pip install virtualenv
python3 -m virtualenv venv
```

Configurar la ejecucion de scripts:

```+
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Antes de ejecutar comandos se debe entrar al entorno virual.

```
.\venv\Scripts\activate
```

#### Instalar Dependencias: ####

```+
pip install -r requirements.txt
```

### Paso 3: Migrar base de datos, se debe contar con una base de datos creada ###
Crear un .env creado a partir de .env.example, una vez creado debe modificar los datos segun los de la base de datos creada previamente.

```+
cp .env.example .env
```

Inicializar la base de datos:

```+
flask db init
```

Migrar la base de datos:

```+
flask db migrate
```

Actualizar la base de datos:

```+
flask db upgrade
```

### Paso 4: Iniciar Servidor de desarrollo ###
Ejecutar aplicacion:

```
flask run
```



### Importante ##
Para correr el servidor o ejecutar comandos relacionados a la aplicacion es necesario estar en el entorno virtual

### Correr los seeds ###
```
flask seed run
```
