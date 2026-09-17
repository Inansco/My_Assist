import os
import asyncio
import tempfile

import edge_tts
from playsound3 import playsound

import sounddevice as sd
import soundfile as sf
import speech_recognition as sr


class Voice:

    def __init__(self):

        self.recognizer = sr.Recognizer()

        # Microsoft Neural Voice
        self.voice = "en-US-GuyNeural"

    async def _tts(self, text, filename):

        communicate = edge_tts.Communicate(
            text=text,
            voice=self.voice,
        )

        await communicate.save(filename)

    def speak(self, text):

        if not text:
            return

        print(f"Inansco: {text}")

        filename = None

        try:

            with tempfile.NamedTemporaryFile(
                suffix=".mp3",
                delete=False,
            ) as f:

                filename = f.name

            asyncio.run(
                self._tts(text, filename)
            )

            playsound(filename)

        except Exception as e:

            print("Speech Error:", e)

        finally:

            if filename and os.path.exists(filename):

                os.remove(filename)

    def listen(self, seconds=5):

        print("Listening...")

        samplerate = 16000

        recording = sd.rec(
            int(seconds * samplerate),
            samplerate=samplerate,
            channels=1,
            dtype="int16",
        )

        sd.wait()

        filename = None

        try:

            with tempfile.NamedTemporaryFile(
                suffix=".wav",
                delete=False,
            ) as f:

                filename = f.name

            sf.write(filename, recording, samplerate)

            with sr.AudioFile(filename) as source:

                audio = self.recognizer.record(source)

            text = self.recognizer.recognize_google(audio)

            return text

        except sr.UnknownValueError:

            return ""

        except sr.RequestError:

            return ""

        except Exception as e:

            print("Recognition Error:", e)

            return ""

        finally:

            if filename and os.path.exists(filename):

                os.remove(filename)