'''
For Hosting Web App
Flask Server for Application
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/')
def render_index_page():
    '''
    Function for route
    To render Index Template
    '''
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detect():
    '''
    Function for route
    To render Emotion Detector Functionality Template
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze == '':
        return 'Invalid text! Please try again!'
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    del response['dominant_emotion']
    if dominant_emotion is None:
        return 'Invalid text! Please try again!'
    return f"For the given statement, the system response is {response}. \
    The dominant emotion is {dominant_emotion}."

if __name__ == '__main__':
    app.run(host='localhost', port = 5000)
