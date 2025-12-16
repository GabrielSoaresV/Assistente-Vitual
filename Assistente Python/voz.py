import speech_recognition as sr

def ouvir():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Ouvindo...")
        r.adjust_for_ambient_noise(source, duration=0.8)
        audio = r.listen(source)

    try:
        texto = r.recognize_google(audio, language="pt-BR")
        print("🗣️ Você disse:", texto)
        return texto.lower()
    except:
        print("❌ Não entendi")
        return ""
