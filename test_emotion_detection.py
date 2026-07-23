"""
Unit tests for EmotionDetection package.
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """
    Test suite for emotion detection function.
    """

    def test_emotion_detector_joy(self):
        """Test joy statement."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_emotion_detector_anger(self):
        """Test anger statement."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_emotion_detector_disgust(self):
        """Test disgust statement."""
        result = emotion_detector("I feel disgusted just thinking about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_emotion_detector_fear(self):
        """Test fear statement."""
        result = emotion_detector("I am so scared that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_emotion_detector_sadness(self):
        """Test sadness statement."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')


if __name__ == '__main__':
    unittest.main()
