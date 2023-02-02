import os
from datetime import date, timedelta
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


proxy_client = TwilioHttpClient()


account_sid = "AC95ee413e05099b325b8f7374cf7b33cc"
auth_token = "ecb71d7f0799cbf6a49897947df4895c"

STOCK = "APRN"
COMPANY_NAME = "Blue Apron"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

STOCK_API_KEY = "9117AUDPI9X3UQ8K"

stock_params = {
    "function":'TIME_SERIES_DAILY',
    "outputsize":"compact",
    "symbol":STOCK,
    "apikey":STOCK_API_KEY,
}


# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
stock_url = 'https://www.alphavantage.co/query?'
response = requests.get(stock_url,params=stock_params)
data = response.json()

today = date.today()
dayno = today.weekday()
if dayno == 6:
    yesterday = today - timedelta(days=2)
    day_bfr_yest = today - timedelta(days=3)
elif dayno == 5:
    yesterday = today - timedelta(days=1)
    day_bfr_yest = today - timedelta(days=2)
elif dayno == 0:
    yesterday = today - timedelta(days=3)
    day_bfr_yest = today - timedelta(days=4)
elif dayno == 1:
    yesterday = today - timedelta(days=1)
    day_bfr_yest = today - timedelta(days=4)
else:
    yesterday = today - timedelta(days=1)
    day_bfr_yest = today - timedelta(days=2)

print(yesterday)
print(day_bfr_yest)

yest_close = 0
bfr_yest_close = 0

for stock_data in data["Time Series (Daily)"]:
    if stock_data == str(yesterday):
        yest_close = float(data["Time Series (Daily)"][stock_data]['4. close'])
        print(yest_close)
    elif stock_data == str(day_bfr_yest):
        bfr_yest_close = float(data["Time Series (Daily)"][stock_data]['4. close'])
        print(bfr_yest_close)

#stock price change calculation - ((new price - old price)/old price) * 100
percentage_change = ((yest_close-bfr_yest_close)/bfr_yest_close)*100

client = Client(account_sid, auth_token, http_client=proxy_client)
MESSAGE = ""
if abs(percentage_change) > 5:
    arrowupordown = ""
    if percentage_change > 0:
        arrowupordown = "🔺"
    elif percentage_change < 0:
        arrowupordown = "🔻"
    MESSAGE = f"\n{STOCK}: {arrowupordown}{round(abs(percentage_change),2)}%\n\n"

    NEWS_API_KEY = "a55640f3765b44d59d702e1ec9461678"
    news_url = "https://newsapi.org/v2/everything?"

    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "sortBy": "publishedAt",
        "searchIn": "title",
        "pageSize": 3,
    }

    news_response = requests.get(news_url, params=news_params)
    news = news_response.json()

    for article in news['articles']:
        MESSAGE += "Headline:" + article['title'] + '\n'
        MESSAGE += "Brief:" + article['description'] + '\n\n'

else:
    MESSAGE = "minimal change"

print(MESSAGE)

message = client.messages \
        .create(
        body=MESSAGE,
        from_='+18149148065',
        to='+15177558608'
    )
print(message.status)

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.











## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


