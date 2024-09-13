from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/')
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detect():
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze == '':
        return 'Invalid text! Please try again!'
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    del response['dominant_emotion']
    if dominant_emotion == None:
        return 'Invalid text! Please try again!'
    return f"For the given statement, the system response is {response}. \
    The dominant emotion is {dominant_emotion}."

if __name__ == '__main__':
    app.run(host='localhost', port = 5000)