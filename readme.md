Sebastian Rojas Osinaga
56814
Topicos Selectos en IA

# Modelo 

Esta API aplica los modelos de estilizacion de rostros disponibles en [mediapipe](https://developers.google.com/mediapipe/solutions/vision/face_stylizer). Los modelos mencionados son el modelo de **Color Sketch**, que simula el rostro del usuario recreandolo como un personaje de libro de comic. El siguiente modelo es **Color Ink**, que recrea el rostro del usuario como un dibujo de boligrafos de tinta. Y finalmente el ultimo modelo implementado es **Oil Painting**, que simula la apariencia del rostro del usuario como si este se encontrara en una pintura de aceite.

# Stylizer API
Este es un API que ofrece servicios de estilización de imágenes utilizando tres modelos diferentes: Color Ink, Color Sketch y Oil Painting.

## Métodos Fundamentales
### GET /status
Este endpoint devuelve el estado del servidor y detalles sobre el servicio ofrecido.

Funcionalidad:
Retorna un mensaje indicando que el servidor está en funcionamiento.
Proporciona información sobre el servicio de aplicación de filtros faciales, detallando los modelos utilizados.
### GET /reports
Este endpoint descarga un informe en formato CSV con datos de consultas anteriores.

Funcionalidad:
Genera un informe en formato CSV con detalles sobre consultas previas, incluyendo fecha y hora, nombre del archivo, tamaño, tiempo de procesamiento, modelo utilizado y mensaje asociado.
### POST /predict_ink
Este endpoint aplica el modelo Color Ink a una imagen proporcionada.

Funcionalidad:
Estiliza la imagen de acuerdo al modelo Color Ink.
Genera un informe de procesamiento y devuelve la imagen estilizada en formato JPEG.
### POST /predict_sketch
Este endpoint aplica el modelo Color Sketch a una imagen proporcionada.

Funcionalidad:
Estiliza la imagen de acuerdo al modelo Color Sketch.
Genera un informe de procesamiento y devuelve la imagen estilizada en formato JPEG.
### POST /predict_oil
Este endpoint aplica el modelo Oil Painting a una imagen proporcionada.

Funcionalidad:
Estiliza la imagen de acuerdo al modelo Oil Painting.
Genera un informe de procesamiento y devuelve la imagen estilizada en formato JPEG.

# Cómo Ejecutar el Proyecto
Para ejecutar este proyecto localmente, sigue los siguientes pasos:

## 1. Clonar el Repositorio
Primero, clona el repositorio desde GitHub:

```bash
git clone <URL_del_repositorio>
```
Reemplaza <URL_del_repositorio> con la URL del repositorio donde se encuentra el código.


## 2. Ingresar al Directorio del Proyecto
Accede al directorio recién clonado:

```bash
cd nombre_del_directorio
```
Reemplaza nombre_del_directorio con el nombre del directorio clonado.

## 3. Instalar Dependencias
Asegúrate de tener todas las dependencias instaladas ejecutando:

```bash
pip install -r requirements.txt
```
Esto instalará todas las dependencias necesarias para ejecutar el proyecto.

## 4. Iniciar el Servidor
Ejecuta el siguiente comando para iniciar el servidor utilizando Uvicorn:

```bash
uvicorn app:app --reload
```
Esto iniciará el servidor de la aplicación FastAPI. El argumento --reload permite que el servidor se reinicie automáticamente cuando se realicen cambios en el código.

## 5. Esperar a que el Servicio se Levante
Una vez que ejecutes el comando, espera a que el servicio se levante completamente. Verás un mensaje indicando que el servidor está en funcionamiento.

## 6. Interactuar con el API
Ahora que el servidor está en funcionamiento, puedes interactuar con los diferentes endpoints del API para estilizar imágenes utilizando los modelos disponibles.
