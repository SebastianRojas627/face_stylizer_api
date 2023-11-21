Sebastian Rojas Osinaga
56814
Topicos Selectos en IA

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
