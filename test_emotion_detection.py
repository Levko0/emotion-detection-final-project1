import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    
    def test_joy_case(self):
        result = emotion_detector("I am so happy and excited for the results")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger_case(self):
        result = emotion_detector("This situation makes me incredibly furious")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_case(self):
        result = emotion_detector("The smell of this food is absolutely revolting")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness_case(self):
        result = emotion_detector("I feel very lonely and heartbroken today")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_case(self):
        result = emotion_detector("I am terrified of what might happen next")
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_invalid_input(self):
        result = emotion_detector("")
        self.assertIsNone(result['dominant_emotion'])

if __name__ == '__main__':
    unittest.main()
