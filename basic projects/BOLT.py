import datetime
import pyttsx3
import speech_recognition as sr

# Initialize text-to-speech engine
engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    print("Bolt:", text)  # Print the sentence
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I assist you today?")

def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time

def get_voice_input():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        print("Listening...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        user_input = recognizer.recognize_google(audio)
        print("You:", user_input)
        return user_input.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""

def main():
    wishMe()  # Greet the user
    while True:
        user_input = get_voice_input()

        if "time" in user_input:
            current_time = get_time()
            speak(f"The current time is {current_time}")

        elif "exit" in user_input or "quit" in user_input:
            speak("Goodbye!")
            break

        else:
            speak("I'm sorry, I didn't understand that. Can you please repeat?")

if __name__ == "__main__":
    main()
