from speech import SpeechManager

_speech_manager = None

PITCH_MIN = 0
PITCH_MAX = 200
RATE_MIN = 0
RATE_MAX = 200

def get_speech_manager():
    global _speech_manager

    if not _speech_manager:
        _speech_manager = SpeechManager()
        if not _speech_manager.enabled():
            _speech_manager = None

    return _speech_manager
