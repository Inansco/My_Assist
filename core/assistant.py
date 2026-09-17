from core.brain import Brain
from voice.speech import Voice

class Assistant:

    def __init__(self):
        self.brain = Brain()
        self.voice = Voice()

    def process(self, message):

        print("Assistant.process() called")

        reply = self.brain.think(message)

        print("Reply:", reply)

        self.voice.speak(reply)

        return reply