"""tflite_inference.py
Run inference with a TFLite model on a single image.
"""
import numpy as np
from PIL import Image
import tensorflow as tf

IMG_SIZE = 128

interpreter = tf.lite.Interpreter(model_path="model/recycle_model.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

img = Image.open("test_images/example.jpg").resize((IMG_SIZE, IMG_SIZE))
input_data = np.expand_dims(np.array(img)/255.0, axis=0).astype('float32')

interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()
output = interpreter.get_tensor(output_details[0]['index'])
print("Raw output:", output)
print("Predicted class index:", int(output.argmax()))
