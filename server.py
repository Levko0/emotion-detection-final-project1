"""
This module contains a Flask application for emotion detection using Watson NLP API.
It provides a web interface and an API endpoint for analyzing emotions in text.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the main page with the interface for emotion detection.
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def detect_emotion():
    """
    Detect emotions in a given text using the emotion_detector function.
    """
    # Змінюємо request.json на request.args для отримання даних з URL (GET запит)
    text_to_analyze = request.args.get('textToAnalyze')

    # Виклик функції детекції
    emotion_response = emotion_detector(text_to_analyze)

    # Перевірка на порожній або некоректний ввід
    if emotion_response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Формування рядка відповіді (саме так, як очікує JavaScript у проекті)
    response_message = (
        f"For the given statement, the system response is 'anger': "
        f"{emotion_response['anger']}, 'disgust': {emotion_response['disgust']}, "
        f"'fear': {emotion_response['fear']}, 'joy': {emotion_response['joy']} "
        f"and 'sadness': {emotion_response['sadness']}. The dominant emotion is "
        f"{emotion_response['dominant_emotion']}."
    )

    return response_message

if __name__ == '__main__':
    # Включаємо debug=True для зручності розробки
    app.run(host='127.0.0.1', port=5000, debug=True)
