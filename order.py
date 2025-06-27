import os
from dotenv import load_dotenv
from alpha_trader.client import Client

load_dotenv()

client = Client(
    base_url="https://stable.alpha-trader.com",
    username=os.getenv("USERNAME"),
    password=os.getenv("PASSWORD"),
    partner_id=os.getenv("PARTNER_ID")
)
client.login()
 print(client.token)

