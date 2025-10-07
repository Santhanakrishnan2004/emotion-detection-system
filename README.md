
## 🚢 Emotion Detector

### 😃 About the Project

This app uses a **FastAI deep learning model** to detect human emotions from images.
Upload a face image, and the model will predict the **emotion** (such as happy, sad, angry, etc.) with confidence scores.

Built with ❤️ using:

* **FastAI** for model training
* **PyTorch** for deep learning backend
* **Gradio** for an interactive UI
* **Hugging Face Spaces** for deployment

---

### 🧠 Model Details

* Trained using **FastAI’s vision learner**.
* Exported as `export.pkl`.
* Hosted on the Hugging Face Model Hub:
  👉 [`VSakhi/emotion-detection`](https://huggingface.co/VSakhi/emotion-detection)

---

### ⚙️ Tech Stack

| Component | Library             |
| --------- | ------------------- |
| Model     | FastAI              |
| Inference | PyTorch             |
| Interface | Gradio              |
| Hosting   | Hugging Face Spaces |

---

### 🧩 Requirements

```
fastai==2.7.14
gradio==4.44.0
huggingface_hub==0.24.6
torch
torchvision
```

---

### 💻 How It Works

1. The app downloads the trained model from Hugging Face Hub.
2. The model is loaded with a patch that converts `WindowsPath` to `PosixPath` (for Linux compatibility).
3. When a user uploads an image, the app runs inference and returns the predicted emotion with probability.

---

### 🚀 Running Locally

If you want to run this on your local machine:

```bash
git clone https://huggingface.co/spaces/VSakhi/emotion-detection-app
cd emotion-detection-app
pip install -r requirements.txt
python app.py
```

Then open the local Gradio link in your browser!

---

### 💬 Creator

👩‍💻 **(Santhana Krishnan Vasudevan)**
🎓 Data Scientist | AI Enthusiast | FastAI Learner

Connect with me on [GitHub](https://github.com/Santhanakrishnan2004)


