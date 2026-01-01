"""
Flask server for the Emotion Detection application.

This module provides a web interface and API endpoint
to analyze emotions from user-provided text.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    """
    Render the home page of the Emotion Detection application.

    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """
    Analyze the given text and return formatted emotion results.

    The text to analyze is passed as a query parameter named
    'textToAnalyze'. If the text is invalid or empty, an
    error message is returned.

    Returns:
        str: Formatted emotion analysis result or error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
