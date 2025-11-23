"""train_model.py
Minimal script to train a small image classifier using TensorFlow.
Replace 'recycle_dataset/' with your dataset folder structured by class subfolders.
"""
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

IMG_SIZE = 128
BATCH = 32
EPOCHS = 8

datagen = ImageDataGenerator(rescale=1/255, validation_split=0.2)

train_data = datagen.flow_from_directory(
    "recycle_dataset",
    target_size=(IMG_SIZE, IMG_SIZE),
    class_mode="categorical",
    subset="training",
    batch_size=BATCH
)

val_data = datagen.flow_from_directory(
    "recycle_dataset",
    target_size=(IMG_SIZE, IMG_SIZE),
    class_mode="categorical",
    subset="validation",
    batch_size=BATCH
)

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(IMG_SIZE,IMG_SIZE,3)),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(train_data.num_classes, activation='softmax')
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

model.fit(train_data, validation_data=val_data, epochs=EPOCHS)
model.save("model/recycle_model.h5")
print("Model saved to model/recycle_model.h5")
