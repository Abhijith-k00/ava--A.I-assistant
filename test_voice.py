import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 210)  # Good speaking speed

# Set voice to Microsoft Zira (female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Replace index if different

engine.say("Hello, I am AVA. Your smart assistant.")
engine.runAndWait()
