# Global
import requests

# Local
from .helper import check_correct

class EconomyConnection:
    def __init__(self, url: str, port: int):
        self.url = url
        self.port = port
    
    def get_balance(self, account, currency_id):
        if not check_correct(account):
            raise ValueError(f"Invalid account: {account}")

        payload = {
            "account": account,
            "currency_id": currency_id
        }

        response = requests.post(f"{self.url}:{self.port}/public/balance", json=payload, timeout=15)

        if response.ok:
            return response.json()
        else:
            raise Exception(f"Error: {response.json().get('error')}")
    
    def transaction(self, account, currency_id, recipient, amount):
        if amount < 1:
            raise ValueError(f"Invalid amount: {amount}")

        if recipient < 0:
            raise ValueError(f"Invalid recipient: {recipient}")

        if not check_correct(account):
            raise ValueError(f"Invalid account: {account}")

        payload = {
            "account": account,
            "currency_id": currency_id,
            "recipient": recipient,
            "amount": amount
        }

        response = requests.post(f"{self.url}:{self.port}/public/transaction", json=payload, timeout=15)

        if response.ok:
            return response.json()
        else:
            raise Exception(f"Error: {response.json().get('error')}")