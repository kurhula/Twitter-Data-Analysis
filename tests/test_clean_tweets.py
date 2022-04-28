import unittest
import pandas as pd
import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from extract_dataframe import read_json
from fix_clean_tweets_dataframe import Clean_Tweets
# from fix_clean_tweets_dataframe.Clean_Tweets import

_, tweet_list = read_json("data/covid19.json")

columns = ['created_at', 'source', 'original_text','clean_text', 'sentiment','polarity','subjectivity', 'lang', 'favorite_count', 'retweet_count',
    'original_author', 'screen_count', 'followers_count','friends_count','possibly_sensitive', 'hashtags', 'user_mentions', 'place', 'place_coord_boundaries']


class TestCleanTweet(unittest.TestCase):
    """
		A class for unit-testing function in the fix_clean_tweets_dataframe.py file

		Args:
        -----
			unittest.TestCase this allows the new class to inherit
			from the unittest module
	"""

    def setUp(self) -> pd.DataFrame:
        # df_ =
        # print(df_)
        self.df = Clean_Tweets(tweet_list[:5])
        # tweet_df = self.df.get_tweet_df()

    def test_drop_unwanted_rows():
        # expected
        expected_shape = (100, 10)
        # given
        df = self.df.drop_unwanted_rows(df=self.df.df)
        returned_shape = df.shape
        # assert
        assertEqual(expected_shape, returned_shape)




if __name__ == '__main__':
	unittest.main()
