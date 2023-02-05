from flask import Flask, render_template, Response
# from flask_caching import Cache
from face_verification import Video, gen, face_authenticated
from speech_to_text import speech_to_text
from text_to_speech import text_to_speech
from text_similarity_check import most_sim_query

app=Flask(__name__)
cache = Cache(app)



"""Home Page"""
@app.route('/')
def index():
    return render_template('index.html')




"""Sign In/Sign up"""
@app.route('/login_registration')
def login_registration():
    return render_template('login_registration.html')


"""Face Authentication"""
@app.route('/authentication')
def authentication():
    return render_template('face_authentication.html')


@app.route('/video')
def video():
    return Response(gen(Video()), mimetype='multipart/x-mixed-replace; boundary=frame')


"""User Access"""
@app.route('/verified')
def verification():
    authenticated = face_authenticated()
    return render_template('conversation.html', verification = authenticated)




"""Conversation"""
@app.route('/conversation', methods=["GET","POST"])
# @cache.cached(timeout=20)
def conversation():
    urser_text_path = "static/texts/audio.txt"
    text = speech_to_text()
    similar_q = most_sim_query(text)
    text_to_speech(similar_q)
    return render_template('conversation.html', verification = True)

"""Test Url"""
# @app.route('/ui')
# def ui():
#     return render_template('login.html')


app.run(debug=True, threaded = True)