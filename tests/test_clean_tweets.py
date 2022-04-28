import unittest
import pandas as pd
import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from fix_clean_tweets_dataframe import Clean_Tweets

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
        filename = "data/cleaned_fintech_data.csv"
        self.df = pd.read_csv(filename)
        # print(df_)
        self.clean_tweets_obj = Clean_Tweets(self.df)
        # tweet_df = self.df.get_tweet_df()

    def test_drop_unwanted_columns(self):
        # Arrange
        column_names = ['friends_count']
        columns = self.df.columns
        for c in column_names:
            self.assertIn(c, columns)

        # Act
        df = self.clean_tweets_obj.drop_unwanted_columns(column_names)

        # Assert
        columns = df.columns
        for c in column_names:
            self.assertNotIn(c, columns)

    def test_drop_unwanted_rows(self):
        




if __name__ == '__main__':
	unittest.main()
