from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'Pedro Casas'

LOGGER = getLogger(__name__)




class AnalyzeChordsSkill(MycroftSkill):
    def __init__(self):
        super(AnalyzeChordsSkill, self).__init__(name="AnalyzeChordsSkill")
        
    def initialize(self):
        pass
    def handle_analyze_chords_intent(self, message):
        pass
    def stop(self):
        pass
def create_skill():
    return AnalyzeChordsSkill()
