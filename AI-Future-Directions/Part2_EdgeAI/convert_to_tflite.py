"""convert_to_tflite.py
Converts a Keras .h5 model to TensorFlow Lite (.tflite)
"""
import tensorflow as tf

model = tf.keras.models.load_model("model/recycle_model.h5")
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

with open("model/recycle_model.tflite", "wb") as f:
    f.write(tflite_model)

print("Converted to model/recycle_model.tflite")
