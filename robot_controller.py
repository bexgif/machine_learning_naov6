import time
from src.config_loader import load_config

cfg = load_config()

USE_MOCK = cfg.get("use_mock", True)

if USE_MOCK:
    class NAOEmotionResponder:
        def __init__(self, *args, **kwargs):
            print("Initialising NAO...")

        def act_on_sentiment(self, sentiment, text):
            print(f"NAO would react to '{sentiment}' with: {text}")

else:
    from naoqi import ALProxy

    class NAOEmotionResponder:
        def __init__(self, ip=cfg["nao_ip"], port=cfg["nao_port"]):
            self.tts = ALProxy("ALTextToSpeech", ip, port)
            self.leds = ALProxy("ALLeds", ip, port)
            self.motion = ALProxy("ALMotion", ip, port)
            self.posture = ALProxy("ALRobotPosture", ip, port)
            print(f"[REAL] Connected to NAO at {ip}:{port}")

        def act_on_sentiment(self, sentiment, text):
            if sentiment == "positive":
                self.leds.fadeRGB("FaceLeds", 0x00FF00, 1.0)  # Green
                self.tts.setParameter("pitchShift", 1.2)
                self.tts.say("Lovely weather ahead! " + text)
                self.posture.goToPosture("StandInit", 1.0)
                self.motion.angleInterpolationWithSpeed("HeadYaw", 0.5, 0.2)

            elif sentiment == "neutral":
                self.leds.fadeRGB("FaceLeds", 0xFFFFFF, 1.0)  # White
                self.tts.setParameter("pitchShift", 1.0)
                self.tts.say("Just your regular day. " + text)
                self.motion.rest()

            elif sentiment == "negative":
                self.leds.fadeRGB("FaceLeds", 0xFF0000, 1.0)  # Red
                self.tts.setParameter("pitchShift", 0.8)
                self.tts.say("Oh no! Bad weather incoming. " + text)
                self.motion.angleInterpolationWithSpeed("HeadPitch", 0.3, 0.2)
