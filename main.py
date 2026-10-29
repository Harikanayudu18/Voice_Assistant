
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import subprocess
import platform
import sys
from urllib.parse import quote_plus


print("Voice assistant script started!")

# Initialize speech recognition
recognizer = sr.Recognizer()

# Initialize text-to-speech
try:
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)
except Exception as error:
    print("Text-to-speech initialization failed:", error)
    sys.exit(1)


def speak(text):
    """Speak a message and print it to the terminal."""
    print("Assistant:", text)
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as error:
        print("Speech output error:", error)


def listen():
    """Listen through the microphone and recognize speech."""
    try:
        with sr.Microphone() as source:
            print("\nListening... Please speak.")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        print("Recognizing your speech...")
        command = recognizer.recognize_google(audio)
        command = command.lower().strip()

        print("You said:", command)
        return command

    except sr.WaitTimeoutError:
        print("No speech detected. Try again.")

    except sr.UnknownValueError:
        speak("Sorry, I could not understand that.")

    except sr.RequestError as error:
        print("Speech recognition service error:", error)
        speak("Please check your internet connection.")

    except OSError as error:
        print("Microphone error:", error)
        speak("Please check your microphone permissions.")

    except Exception as error:
        print("Unexpected listening error:", error)

    return ""


def open_application(app_name):
    """Open supported desktop applications."""
    system = platform.system()

    try:
        if system == "Windows":
            apps = {
                "notepad": ["notepad.exe"],
                "calculator": ["calc.exe"]
            }

            if app_name in apps:
                subprocess.Popen(apps[app_name])
                return True

        elif system == "Darwin":
            apps = {
                "notepad": "TextEdit",
                "calculator": "Calculator"
            }

            if app_name in apps:
                subprocess.Popen(["open", "-a", apps[app_name]])
                return True

        elif system == "Linux":
            apps = {
                "notepad": ["gedit"],
                "calculator": ["gnome-calculator"]
            }

            if app_name in apps:
                subprocess.Popen(apps[app_name])
                return True

    except OSError as error:
        print("Could not open application:", error)

    return False


def process_command(command):
    """Process recognized voice commands."""

    if not command:
        return True

    # Exit assistant
    if any(word in command for word in [
        "exit", "quit", "stop assistant", "goodbye"
    ]):
        speak("Goodbye! Have a nice day.")
        return False

    # Greeting
    elif any(word in command for word in [
        "hello", "hi assistant", "hey assistant"
    ]):
        speak("Hello! How can I help you?")

    # Current time
    elif "time" in command:
        now = datetime.datetime.now()
        speak("The time is " + now.strftime("%I:%M %p"))

    # Current date
    elif "date" in command or "today" in command:
        today = datetime.datetime.now()
        speak("Today's date is " + today.strftime("%d %B %Y"))

    # Open YouTube
    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    # Open Google
    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    # Open GitHub
    elif "open github" in command:
        speak("Opening GitHub.")
        webbrowser.open("https://github.com")

    # Google search
    elif command.startswith("search for "):
        query = command.removeprefix("search for ").strip()

        if query:
            speak("Searching Google for " + query)
            url = "https://www.google.com/search?q=" + quote_plus(query)
            webbrowser.open(url)
        else:
            speak("Please tell me what to search for.")

    # Open Notepad
    elif "open notepad" in command:
        if open_application("notepad"):
            speak("Opening Notepad.")
        else:
            speak("I could not open Notepad.")

    # Open Calculator
    elif "open calculator" in command:
        if open_application("calculator"):
            speak("Opening Calculator.")
        else:
            speak("I could not open Calculator.")

    # Help
    elif "help" in command or "what can you do" in command:
        speak(
            "You can ask me to open YouTube, Google, GitHub, "
            "Notepad, or Calculator. You can ask for the time "
            "or date, search Google, or say goodbye."
        )

    # Unknown command
    else:
        speak("Sorry, I do not know that command yet.")

    return True


def main():
    print("Starting main function...")

    speak("Welcome! Your voice assistant is ready.")
    speak("Say help to hear the available commands.")

    while True:
        command = listen()

        if not process_command(command):
            break


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\nAssistant stopped by user.")

    except Exception as error:
        print("Application error:", error)

    finally:
        print("Voice assistant has stopped.")
