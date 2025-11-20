from wish.wish import speak
import speech_recognition as sr

def voiceinp():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8   # Slightly increased for natural pauses
        r.adjust_for_ambient_noise(source, duration=0.5)  # Reduces background noise
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User Said: {query}")

    except sr.UnknownValueError:
        query = ""
        speak("Sorry, I could not understand. Could you please say that again?")

    except sr.RequestError:
        query = ""
        speak("Network error. Please check your internet connection.")

    except Exception:
        query = ""
        speak("Something went wrong while recognizing your voice.")

    return query
