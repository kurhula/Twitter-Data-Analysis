import pandas as pd

class Clean_Tweets:
    """
    The PEP8 Standard AMAZING!!!
    """
    def __init__(self, df:pd.DataFrame):
        self.df = df
        print('Automation in Action...!!!')

    def drop_unwanted_columns(self, column_names)->pd.DataFrame:
        """
        remove rows that has column names. This error originated from
        the data collection stage.
        """
        print(self.df.columns)
        self.df.drop(columns=column_names, inplace=True)
        print(self.df.columns)
        return self.df

    # def drop_duplicate(self, df:pd.DataFrame)->pd.DataFrame:
    #     """
    #     drop duplicate rows
    #     """
    #
    #     ---
    #
    #     return df
    # def convert_to_datetime(self, df:pd.DataFrame)->pd.DataFrame:
    #     """
    #     convert column to datetime
    #     """
    #     ----
    #
    #     ----
    #
    #     df = df[df['created_at'] >= '2020-12-31' ]
    #
    #     return df
    #
    # def convert_to_numbers(self, df:pd.DataFrame)->pd.DataFrame:
    #     """
    #     convert columns like polarity, subjectivity, retweet_count
    #     favorite_count etc to numbers
    #     """
    #     df['polarity'] = pd.----
    #
    #     ----
    #     ----
    #
    #     return df
    #
    # def remove_non_english_tweets(self, df:pd.DataFrame)->pd.DataFrame:
    #     """
    #     remove non english tweets from lang
    #     """
    #
    #     df = ----
    #
    #     return df
