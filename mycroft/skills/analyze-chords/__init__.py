from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from __future__ import print_function
import vamp
import matplotlib
import librosa
import matplotlib.pyplot as plt
from sys import byteorder
from array import array
from struct import pack
import pyaudio
import wave
import recorder

__author__ = 'Pedro Casas'

LOGGER = getLogger(__name__)




class AnalyzeChordsSkill(MycroftSkill):
    def __init__(self):
        super(AnalyzeChordsSkill, self).__init__(name="AnalyzeChordsSkill")
        
    def initialize(self):
        self.load_data_files(dirname(__file__))

        analyze_chords_intent = IntentBuilder("AnalyzeChordsIntent").\
        require("AnalyzeChordsKeyword").build()
        self.register_intent(analyze_chords_intent, self.handle_analyze_chords_intent)

    def handle_analyze_chords_intent(self, message):
        
        #Here is where the actual Chord analysis will take place

        # First We have to Record the audio

        output_chords = "./chords.wav"
        
        self.speak_dialog("Ok, listening")

        recorder.record_to_file(output_chords)

        # Then run the Chordata algorithm

        audio, sr = librosa.load(output_chords, sr=44100, mono=True)

        data = vamp.collect(audio, sr, "nnls-chroma:chordino")


        # Then Verbalize the information
        
    def stop(self):
        pass
def create_skill():
    return AnalyzeChordsSkill()
