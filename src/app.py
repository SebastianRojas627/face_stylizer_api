from fastapi import (
    FastAPI,
    UploadFile,
    File,
    HTTPException,
    status,
    Depends
)
import sys
from typing import List
import tempfile
from pydantic import BaseModel
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain.chat_models import ChatOpenAI
import csv
from datetime import datetime
from PIL import Image
from fastapi.responses import Response, StreamingResponse
import numpy as np
from stylizer import ColorSketch, ColorInk, OilPainting
from helpers import style_image, rebuild_styled_image, analyze_faces_sentiment, generate_text, generate_text1
from reports import Reports
from config import get_settings
from llm import LLMService
import uvicorn
from starlette.middleware.cors import CORSMiddleware
import io
import os

SETTINGS = get_settings()
sketch_stylizer = ColorSketch()
ink_stylizer = ColorInk()
oil_stylizer = OilPainting()
reports = Reports()
llm = LLMService()

app = FastAPI(
    title=SETTINGS.service_name,
    version=SETTINGS.k_revision
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SETTINGS.google_vision_api       
def get_sketch_stylizer():
    return sketch_stylizer

def get_ink_stylizer():
    return ink_stylizer

def get_oil_stylizer():
    return oil_stylizer

def get_reports():
    return reports

def get_llm():
    return llm

def create_report_data_entry(time, file_name, file_size, processing_time, model, message):
    entry = {
        'Time and Date of Query': time,
        'File Name': file_name,
        'Size (bytes)': file_size,
        'Processing Time (s)': processing_time,
        'Model': model,
        'Message': message
    }
    reports.add_prediction(entry)

@app.get("/status")
def get_status():
    return {"message": "Server is running",
            "service": "Face filter application",
            "models": "Service uses the Face Stylizer models offered from mediapipe, the 3 applied models are Color Ink Model, Color Sketch Model and Oil Painting Model"
            }
    
@app.get("/reports", responses={
    200: {"content": {"text/csv": {}}}
})
def get_reports(reports: Reports = Depends(get_reports)):
    report = reports.generate_report()
    return Response(content=report, media_type="text/csv") 
    
@app.post("/predict_ink")
async def predict_ink_image(
    file: UploadFile = File(...),
    model: ColorInk = Depends(get_ink_stylizer),
) -> StreamingResponse:
    start_time = datetime.now()
    
    with open(file.filename, "wb") as image_file:
        content = await file.read()
        copy = io.BytesIO(content)
        image_file.write(content)

    facial = analyze_faces_sentiment(file.filename)
    character = generate_text1(facial, "Un mundo colorido lleno de detalle y riesgos tan vividos como sus colores")

    file_name = file.filename
    file_size = sys.getsizeof(copy)

    result = style_image(copy, model)
    end_time = datetime.now()
    processing_time = (end_time - start_time).total_seconds()

    if result is None:
        create_report_data_entry(start_time, file_name, file_size, processing_time, model="Ink Stylizer", message="No face detected")
        return StreamingResponse(content={"message": "No face detected"}, media_type="application/json")

    create_report_data_entry(start_time, file_name, file_size, processing_time, model="Ink Stylizer", message="Successful")
    final_img = rebuild_styled_image(result)

    final_img_bytes = io.BytesIO()
    final_img_bytes.write(final_img.read())
    final_img_bytes.seek(0)

    pred_info = {
        'file_name': file_name,
        'processing_time': str(processing_time),
        'model': "Ink Stylizer",
        'img_size': str(file_size)
    }

    return StreamingResponse(
        content=final_img_bytes,
        media_type="image/jpeg",
        headers=character
    )

@app.post("/predict_sketch")
async def predict_sketch_image(
    file: UploadFile = File(...),
    model: ColorSketch = Depends(get_sketch_stylizer),
) -> Response:
    
    start_time = datetime.now()

    with open(file.filename, "wb") as image_file:
        content = await file.read()
        copy = io.BytesIO(content)
        image_file.write(content)

    facial = analyze_faces_sentiment(file.filename)
    character = generate_text(facial, "Un mundo de superheroes, cada individuo con habilidades especiales, cada individuo en una pelea por supervivencia")

    file_name = file.filename
    file_size = sys.getsizeof(copy)

    result = style_image(copy, model)
    end_time = datetime.now()
    processing_time = (end_time - start_time).total_seconds()

    if result is None:
        create_report_data_entry(start_time, file_name, file_size, processing_time, model="Color Sketch", message="No face detected")
        return {"message": "No face detected"}

    create_report_data_entry(start_time, file_name, file_size, processing_time, model="Color Sketch", message="Succesful")
    final_img = rebuild_styled_image(result)

    final_img_bytes = io.BytesIO()
    final_img_bytes.write(final_img.read())
    final_img_bytes.seek(0)

    pred_info = [{
        'file_name': file_name,
        'processing_time': str(processing_time),
        'model': "Color Sketch",
        'img_size': str(file_size)
    }]
    

    return StreamingResponse(
        content=final_img_bytes,
        media_type="image/jpeg",
        headers=character
    )

@app.post("/predict_oil")
async def predict_oil_image(
    file: UploadFile = File(...),
    model: OilPainting = Depends(get_oil_stylizer),
) -> Response:
    
    start_time = datetime.now()
    with open(file.filename, "wb") as image_file:
        content = await file.read()
        copy = io.BytesIO(content)
        image_file.write(content)

    facial = analyze_faces_sentiment(file.filename)
    character = generate_text(facial, "Un mundo de tragedia y angustia, distorciones visuales y peligros de otra realidad")

    file_name = file.filename
    file_size = sys.getsizeof(copy)

    result = style_image(copy, model)
    end_time = datetime.now()
    processing_time = (end_time - start_time).total_seconds()

    if result is None:
        create_report_data_entry(start_time, file_name, file_size, processing_time, model="Oil Painting", message="No face detected")
        return {"message": "No face detected"}

    create_report_data_entry(start_time, file_name, file_size, processing_time, model="Oil Painting", message="Succesful")
    final_img = rebuild_styled_image(result)

    final_img_bytes = io.BytesIO()
    final_img_bytes.write(final_img.read())
    final_img_bytes.seek(0)

    pred_info = {
        'file_name': file_name,
        'processing_time': str(processing_time),
        'model': "Oil Painting",
        'img_size': str(file_size)
    }


    return StreamingResponse(
        content=final_img_bytes,
        media_type="image/jpeg",
        headers=character
    )

if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)