from distutils.command.config import LANG_EXT
from attr import dataclass
from flask import Flask, render_template, request
#import sqlalchemy
import speech_recognition as sr
from PIL import Image
import os
import transformers
from transformers import pipeline
import argparse
import multiprocessing
from playsound import playsound


from sound_text_correct import sound_text_Eng
from summarization import *
from clip_fft_helper import main

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        mytxt = sound_text_Eng()
        global text
        text = sum_text(mytxt)
        text = text.strip()
        #print(text)

        return render_template('create.html', value="Start creating!")
    return render_template('create.html')

@app.route("/image")
def image():
    print("DREAM RECEIVED")
    music_name= "static/yoga_wait.mp3"
    print(text)
    p1 = multiprocessing.Process(target= main, args=(text, [300, 300], 100, 10))
    p2 = multiprocessing.Process(target= playsound, args=(music_name,))

    p1.start()
    p2.start()

    p1.join()
    if p1.is_alive() == False:
        p2.terminate()
    return render_template("create.html", value="You can now see your result!")
    
@app.route("/final")
def final():
    print(text)
    x = text.strip().lower().split( )
    name = x[0] + "_" + x[1] + "_" + x[2]
    for files in os.listdir('static'):
        files = files.split('.')[0]
        if files.startswith(name):
            pic_name = files + '.jpg'
            print('picname'+ pic_name)
            if pic_name != None:
                return render_template("create.html", image= pic_name)
                



if __name__== "__main__":
    app.run(debug=False)