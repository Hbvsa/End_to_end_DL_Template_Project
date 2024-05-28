import gradio as gr
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, model_path):
        self.model = load_model(model_path)

    def predict(self, img_path):
        test_image = image.load_img(img_path, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(self.model.predict(test_image), axis=1)

        if result[0] == 1:
            prediction = 'Healthy'
        else:
            prediction = 'Coccidiosis'

        return prediction

def predict_image(img):
    img_path = 'temp_image.jpg'
    img.save(img_path)
    pipeline = PredictionPipeline(os.path.join("artifacts", "training", "model.h5"))
    prediction = pipeline.predict(img_path)
    return prediction

# Gradio Interface
interface = gr.Interface(
    fn=predict_image,
    inputs=gr.Image(type='pil'),
    outputs=gr.Textbox(label="Prediction"),
    title="Chicken Disease Classifier",
    description="Upload an image of a chicken to classify if it's Healthy or has Coccidiosis."
)

if __name__ == "__main__":
    interface.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 8080)))
