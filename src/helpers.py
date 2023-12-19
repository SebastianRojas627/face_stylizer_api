from PIL import Image
import numpy as np
import io
from google.cloud import vision
from llm import generate_text_character

def style_image(img_stream, model):
    pil_img = Image.open(img_stream)
    img_array = np.array(pil_img)
    return model.stylize_image(img_array)

def rebuild_styled_image(img):
    img_pil = Image.fromarray(img)
    img_stream = io.BytesIO()
    img_pil.save(img_stream, format='PNG')
    img_stream.seek(0)
    return img_stream

def analyze_faces_sentiment(image_path):
    client = vision.ImageAnnotatorClient()

    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.face_detection(image=image)

    sentiment_analysis = []
    for face in response.face_annotations:
        sentiment = {
            'joy': str(round(face.joy_likelihood, 2)),
            'sorrow': str(round(face.sorrow_likelihood, 2)),
            'anger': str(round(face.anger_likelihood, 2)),
            'surprise': str(round(face.surprise_likelihood, 2)),
        }
        sentiment_analysis.append(sentiment)

    return sentiment

def generate_text(sentiment, world: str):
    felicidad = sentiment.get('joy')
    tristeza = sentiment.get('sorrow')
    enojo = sentiment.get('anger')
    sorpresa = sentiment.get('surprise')

    response = generate_text_character(world, felicidad, tristeza, sorpresa, enojo)
    
    return response
    