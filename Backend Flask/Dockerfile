# Utiliza la imagen oficial de Python versión 3.11.5 como base
FROM python:3.11.5

# Crea un directorio llamado /app dentro del contenedor
RUN mkdir /app

# Establece /app como el directorio de trabajo actual
WORKDIR /app

# Copia el archivo requirements.txt desde el directorio local al directorio /app en el contenedor
COPY ./requirements.txt /app

# Instala las dependencias especificadas en requirements.txt usando pip
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos los archivos del directorio local al directorio /app en el contenedor
COPY . /app

# Establece variables de entorno para la aplicación Flask
ENV FLASK_APP entrypoint.py
ENV FLASK_RUN_HOST 0.0.0.0

# Expone el puerto 5000 para que la aplicación Flask pueda ser accedida desde fuera del contenedor
EXPOSE 5000

# Comando que se ejecutará al iniciar el contenedor
CMD ["sh", "-c", "flask db init; flask db migrate; flask db upgrade; flask run"]