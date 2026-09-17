from core.assistant import Assistant

assistant = Assistant()

assistant.voice.speak("Hello. I am Inansco.")

while True:

    text = assistant.voice.listen()

    if not text:
        continue

    print("You:", text)

    reply = assistant.process(text)

    print("Inansco:", reply)