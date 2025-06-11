from alpha_trader.client import Client

client = Client(username="MY_USERNAME", password="MY_PASSWORD", partner_id="MY_PARTNER_ID")
client.login()
miner = client.get_miner()
miner.transfer_coins()
