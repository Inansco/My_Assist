from voice.speech import Voice

voice = Voice()

voice.speak("Hello. I am Inansco.")

text = voice.listen()

print("You said:", text)