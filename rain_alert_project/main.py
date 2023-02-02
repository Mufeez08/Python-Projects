import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https':os.environ['https_proxy']}

api_key = "a470976429cc7e3a9b9d6f57f9d431d8"
account_sid = "AC95ee413e05099b325b8f7374cf7b33cc"
auth_token = "ecb71d7f0799cbf6a49897947df4895c"



params = {
    "lat":42.746880,
    "lon":-84.483700,
    "appid":api_key,
    "cnt":4,
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast?",params=params)
response.raise_for_status()
data = response.json()


umbrella_count = 0
for x in data["list"]:
    for weathercond in x['weather']:
        if weathercond['id'] < 700:
            umbrella_count += 1

if umbrella_count > 0:
    client = Client(account_sid, auth_token,http_client=proxy_client)
    message = client.messages \
        .create(
        body="Take an umbrella☔ with you.",
        from_='+18149148065',
        to='+15177558608'
    )
    print(message.status)

