import unittest
import pandas as pd
import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from fix_clean_tweets_dataframe import Clean_Tweets

class TestCleanTweet(unittest.TestCase):

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
        pass




if __name__ == '__main__':
	unittest.main()
