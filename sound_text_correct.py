import speech_recognition as sr 
#r = sr.Recognizer() 
#language=["pt-BR", "pt-PT", "en-US"]
def sound_text_Eng(): 
    r = sr.Recognizer()   
    try:
        with sr.Microphone() as source:                                                                       
            r.adjust_for_ambient_noise(source, duration=0.2)                                                                                  
            audio = r.listen(source)
            MyText=""
            with open("transcript12345.wav", "wb") as f:
                f.write(audio.get_wav_data())
                MyText= r.recognize_google(audio, language="en-US")
                MyText=MyText.lower()
                # if str is bytes: 
                #     result = u"{}".format(MyText).encode("utf-8")

                # else: 
                #     result = "{}".format(MyText)
                # with open("transcript12345.txt", "w") as f:
                #     f.write(MyText)
                #     f.truncate()
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    return MyText

#print(sound_text_Eng())           

# def sound_text_Port():
#     try:
#         MyText= r.recognize_google(audio, language="pt")
#         MyText=MyText.lower()
#         if str is bytes: 
#             result = u"{}".format(MyText).encode("utf-8")
#         else: 
#             result = "{}".format(MyText)
#         with open("dream.txt", "w") as f:
#             f.write(MyText)
#             f.truncate()                           
#     except sr.UnknownValueError:
#         print("Could not understand audio")
#     except sr.RequestError as e:
#         print("Could not request results; {0}".format(e))

#     return MyText


#def respond(MyText):
#    print("Your dream was: "+MyText+"Is that correct? Please answer yes or no.")
#    sound_text()
#    if "yes" in MyText:
#        print("We are making your dream painting now. Please wait.")
#    else:
#        print("Please repeate your dream.")
#        sound_text()
#        respond(MyText)

# print(sound_text("Portuguese-PT"))
#MyText=record_audio()

#print(sound_text_Eng())

#COLOCAR O OUTPUT COMO DREAM