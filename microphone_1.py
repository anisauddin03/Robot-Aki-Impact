import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Microphone as source
# Listening the speech and store in audio_text variable
with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")

    # Recognize speech using Google Web Speech API
    try:
        # Using google speech recognition
        print("Text: " + r.recognize_google(audio_text))
    except:
        print("Sorry, I did not get that")
