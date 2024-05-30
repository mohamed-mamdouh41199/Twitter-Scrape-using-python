from ntscraper import Nitter
import re
import datetime
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from time import time
import time

twitter_accounts = [
    "Mr_Derivatives",
    "warrior_0719",
    "ChartingProdigy",
    "allstarcharts",
    "yuriymatso",
    "TriggerTrades",
    "AdamMancini4",
    "CordovaTrades",
    "Barchart",
    "RoyLMattox"
]
interval = 15

def monthToNum(shortMonth):
    return {
            'Jan': 1,
            'Feb': 2,
            'Mar': 3,
            'Apr': 4,
            'May': 5,
            'Jun': 6,
            'Jul': 7,
            'Aug': 8,
            'Sep': 9, 
            'Oct': 10,
            'Nov': 11,
            'Dec': 12
    }[shortMonth]

def scrape_tweets(user_name):
    text_list = []
    tweets = scraper.get_tweets(user_name , mode= "user" , number=100)
    today = date.today()
    time_now = datetime.now()
    limit_time = time_now - timedelta(hours=1)
    # print("Limit time:-",limit_time.hour)
    for i, tweet in enumerate(tweets['tweets']):
        split_date = tweet['date'].split()

        # tweet times 
        tweet_hour = split_date[4].split(":")[0]
        tweet_day = split_date[1].replace(",","")
        tweet_month = split_date[0]
        tweet_year = split_date[2]
        tweet_hour_type = split_date[5]
        # print("#"*90)
        if int(tweet_day) is int(time_now.day) and monthToNum(tweet_month) is int(time_now.month) and int(tweet_year) == int(time_now.year):
            text_list.append(tweet['text'])
    
    text_list_string = ",".join(text_list)
    return text_list_string

while True:
    scraper = Nitter()
    my_searach = []
    for user_name in twitter_accounts:
        tweets = scrape_tweets(user_name)
        # ticker = r"[$A-Z]{3,5}"
        ticker = "NVDA"
        my_searach = my_searach + re.findall(ticker, tweets)
        print("--"*60)
    print(f"'${ticker}' was mentioned '{len(my_searach)}' times in last day.")
        # print(len(my_searach))
        # print(my_searach)
    time.sleep(interval * 60)
    print("=========Refrech after 15 minute=======")