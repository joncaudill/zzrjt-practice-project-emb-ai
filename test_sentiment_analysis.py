from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        #test positive sentiment
        #arrange
        test_text = "I love working with Python"
        #act
        result = sentiment_analyzer(test_text)
        #assert
        self.assertEqual(result['label'], 'SENT_POSITIVE')

        #test negative sentiment
        #arrange
        test_text = "I hate working with Python"
        #act
        result = sentiment_analyzer(test_text)
        #assert
        self.assertEqual(result['label'], 'SENT_NEGATIVE')

        #test neutral sentiment
        #arrange
        test_text = "I am neutral about working with Python"
        #act
        result = sentiment_analyzer(test_text)
        #assert
        self.assertEqual(result['label'], 'SENT_NEUTRAL')

unittest.main()