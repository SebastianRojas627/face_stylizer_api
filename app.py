from fastapi import (
    FastAPI,
    UploadFile,
    File,
    HTTPException,
    status,
    Depends
)
import sys
import csv
from datetime import datetime
from PIL import Image
from fastapi.responses import Response, StreamingResponse
import numpy as np
from stylizer import ColorSketch, ColorInk, OilPainting
import uvicorn
import io

app = FastAPI(title="Stylizer API")

sketch_stylizer = ColorSketch()
ink_stylizer = ColorInk()
oil_stylizer = OilPainting()

report_data = []

def get_sketch_stylizer():
    return sketch_stylizer

def get_ink_stylizer():
    return ink_stylizer

def get_oil_stylizer():
    return oil_stylizer

def style_image(file, model):
    img_stream = io.BytesIO(file.file.read())
    if file.content_type.split("/")[0] != "image":
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, 
            detail='Invalid content type'
        )
    pil_img = Image.open(img_stream)
    img_array = np.array(pil_img)
    return model.stylize_image(img_array)

def rebuild_styled_image(img):
    img_pil = Image.fromarray(img)
    img_stream = io.BytesIO()
    img_pil.save(img_stream, format='PNG')
    img_stream.seek(0)
    return img_stream

def create_report_data_entry(time, file_name, file_size, processing_time, model, message):
    report_data.append({
        'Time and Date of Query': time,
        'File Name': file_name,
        'Size (bytes)': file_size,
        'Processing Time (s)': processing_time,
        'Model': model,
        'Message': message
    })
    
@app.get("/status")
def get_status():
    return {"message": "Server is running",
            "service": "Face filter application",
            "models": "Service uses the Face Stylizer models offered from mediapipe, the 3 applied models are Color Ink Model, Color Sketch Model and Oil Painting Model"
            }
    
@app.get("/reports", responses={
    200: {"content": {"text/csv": {}}}
})
def download_report() -> Response:
    csv_stream = io.StringIO()
    writer = csv.DictWriter(
        csv_stream, 
        fieldnames=["Time and Date of Query", "File Name", "Size (bytes)", "Processing Time (s)", "Model", "Message"],
        quoting=csv.QUOTE_ALL
        )
    writer.writeheader()
    for row in report_data:
        writer.writerow(row)
    
    text = csv_stream.getvalue()
    return Response(content=text, media_type="text/csv")
    
@app.post("/predict_ink")
def predict_ink_image(
    file: UploadFile = File(...),
    model: ColorInk = Depends(get_ink_stylizer)
) -> StreamingResponse:
    start_time = datetime.now()
    
    file_name = file.filename
    file_size = sys.getsizeof(file)

    result = style_image(file, model)
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
        headers=pred_info
    )

@app.post("/predict_sketch")
def predict_sketch_image(
    file: UploadFile = File(...),
    model: ColorSketch = Depends(get_sketch_stylizer)
) -> Response:
    
    start_time = datetime.now()

    file_name = file.filename
    file_size = sys.getsizeof(file)

    result = style_image(file, model)
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

    pred_info = {
        'file_name': file_name,
        'processing_time': str(processing_time),
        'model': "Color Sketch",
        'img_size': str(file_size)
    }

    return StreamingResponse(
        content=final_img_bytes,
        media_type="image/jpeg",
        headers=pred_info
    )

@app.post("/predict_oil")
def predict_oil_image(
    file: UploadFile = File(...),
    model: OilPainting = Depends(get_oil_stylizer)
) -> Response:
    
    start_time = datetime.now()

    file_name = file.filename
    file_size = sys.getsizeof(file)

    result = style_image(file, model)
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
        headers=pred_info
    )

if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)