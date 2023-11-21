import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np

MODEL_PATH_COLOR_SKETCH = r'C:\Users\osina\Documents\Universidad\Topicos Selectos en IA\app_deploy\parcial1\models\face_stylizer_color_sketch.task'
MODEL_PATH_COLOR_INK = r'C:\Users\osina\Documents\Universidad\Topicos Selectos en IA\app_deploy\parcial1\models\face_stylizer_color_ink.task'
MODEL_PATH_OIL_PAINTING = r'C:\Users\osina\Documents\Universidad\Topicos Selectos en IA\app_deploy\parcial1\models\face_stylizer_oil_painting.task'

class ColorSketch:
    def __init__(self, model_selection=MODEL_PATH_COLOR_SKETCH):
      print("Starting the color sketch model")
      base_options = python.BaseOptions(model_asset_path=model_selection)
      options = vision.FaceStylizerOptions(base_options=base_options)
      self.stylizer = vision.FaceStylizer.create_from_options(options)

    def stylize_image(self, image_array: np.ndarray):
      mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_array)
      stylized_image = self.stylizer.stylize(mp_image)
      #rgb_stylized_image = cv2.cvtColor(stylized_image.numpy_view(), cv2.COLOR_BGR2RGB)
      if stylized_image is None:
        print("Stylized image is None. Cannot proceed.")
        return None
      else:
        return stylized_image.numpy_view()

class ColorInk:
    def __init__(self, model_selection=MODEL_PATH_COLOR_INK):
      print("Starting the color sketch model")
      base_options = python.BaseOptions(model_asset_path=model_selection)
      options = vision.FaceStylizerOptions(base_options=base_options)
      self.stylizer = vision.FaceStylizer.create_from_options(options)

    def stylize_image(self, image_array):
      mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_array)
      stylized_image = self.stylizer.stylize(mp_image)
      #rgb_stylized_image = cv2.cvtColor(stylized_image.numpy_view(), cv2.COLOR_BGR2RGB)
      if stylized_image is None:
        print("Stylized image is None. Cannot proceed.")
        return None
      else:
        return stylized_image.numpy_view()

class OilPainting:
    def __init__(self, model_selection=MODEL_PATH_OIL_PAINTING):
      print("Starting the color sketch model")
      base_options = python.BaseOptions(model_asset_path=model_selection)
      options = vision.FaceStylizerOptions(base_options=base_options)
      self.stylizer = vision.FaceStylizer.create_from_options(options)

    def stylize_image(self, image_array):
      mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_array)
      stylized_image = self.stylizer.stylize(mp_image)
      #rgb_stylized_image = cv2.cvtColor(stylized_image.numpy_view(), cv2.COLOR_BGR2RGB)
      if stylized_image is None:
        print("Stylized image is None. Cannot proceed.")
        return None
      else:
        return stylized_image.numpy_view()
