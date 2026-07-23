# Emotion Detection Web Application Using IBM Watson NLP and Flask

## Project Description
This application provides text-based emotion detection built using the **IBM Watson NLP API** and **Flask**. The service evaluates text input and extracts emotional metrics for **anger**, **disgust**, **fear**, **joy**, and **sadness**, identifying the **dominant emotion**.

## Project Architecture & Package Structure
```text
emotion_detector/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── static/
│   ├── mywebscript.js
│   └── style.css
├── templates/
│   └── index.html
├── server.py
├── test_emotion_detection.py
└── README.md
```

## Setup & Running Instructions
1. Install dependencies:
   ```bash
   pip install flask requests pylint
   ```
2. Run Unit Tests:
   ```bash
   python -m unittest test_emotion_detection.py
   ```
3. Run Static Code Analysis:
   ```bash
   python -m pylint server.py EmotionDetection/emotion_detection.py
   ```
4. Start Flask Server:
   ```bash
   python server.py
   ```
5. Access Application:
   Open browser at `http://localhost:5000`
