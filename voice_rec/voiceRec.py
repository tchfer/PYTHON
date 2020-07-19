# import library

import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)

r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable

with sr.Microphone() as source:
    print("Fale algo:")
    audio_text = r.listen(source)
    print("Tempo esgotado. Obrigado!")
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

    try:
        # using google speech recognition
            #print("Text: " + r.recognize_google(audio_text))
        # Adding Brazilian Portuguese language option
            print("Texto: " + r.recognize_google(audio_text, language="pt-BR"))
    except:
        print("Desculpa, não entendi.")
