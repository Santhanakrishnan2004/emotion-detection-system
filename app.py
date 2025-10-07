from fastai.vision.all import *
import gradio as gr
from fastai.vision.all import load_learner


# Load model
learn = load_learner('export.pkl')

# Prediction function
def predict(img):
    pred, pred_idx, probs = learn.predict(img)
    return {pred: float(probs[pred_idx])}

# Gradio interface
iface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type='pil'),
    outputs=gr.Label(num_top_classes=2),
    title="🚢 Emotion Detector ",
    description="Upload an  image, and the model will predict the emption of the person"
)

# Launch
iface.launch()
