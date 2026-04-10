
try:
    import importlib
    pyttsx3 = importlib.import_module('pyttsx3')
    engine = pyttsx3.init()
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    engine = None
except Exception:
    TTS_AVAILABLE = False
    engine = None

try:
    sr = importlib.import_module('speech_recognition')
    try:
        importlib.import_module('pyaudio')
        PA_AVAILABLE = True
    except ImportError:
        PA_AVAILABLE = False
    SR_AVAILABLE = True
except ImportError:
    sr = None
    SR_AVAILABLE = False
    PA_AVAILABLE = False
except Exception:
    sr = None
    SR_AVAILABLE = False
    PA_AVAILABLE = False

import webbrowser
import datetime

def speak(text):
    print("Assistant:", text)
    if TTS_AVAILABLE and engine:
        engine.say(text)
        engine.runAndWait()

def listen():
    if not SR_AVAILABLE or sr is None:
        print("Speech recognition tidak tersedia.")
        return None

    if not PA_AVAILABLE:
        print("PyAudio tidak tersedia. Silakan install PyAudio.")
        return None

    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Mendengarkan...")
            audio = r.listen(source)
    except Exception as e:
        print("Gagal membuka mikrofon:", e)
        return None

    try:
        command = r.recognize_google(audio, language='id-ID')
        print("Kamu:", command)
        return command.lower()
    except Exception:
        return ""

# mulai
speak("Halo, saya siap membantu")

if not SR_AVAILABLE or sr is None:
    speak("Speech recognition tidak tersedia. Silakan install paket SpeechRecognition.")
else:
    while True:
        command = listen()
        if command is None:
            speak("Mikrofon tidak tersedia. Program keluar.")
            break

        if "youtube" in command:
            speak("Membuka YouTube")
            webbrowser.open("https://youtube.com")

        elif "google" in command:
            speak("Membuka Google")
            webbrowser.open("https://google.com")

        elif "jam" in command:
            waktu = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sekarang jam {waktu}")

        elif "halo" in command:
            speak("Halo juga!")

        elif "keluar" in command:
            speak("Sampai jumpa")
            break 