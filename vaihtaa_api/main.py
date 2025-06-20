# Global
import requests

# Local
from .helper import check_correct

class EconomyAPIError(Exception):
    def __init__(self, status_code, message):
        super().__init__(f"Error {status_code}: {message}")
        self.status_code = status_code
        self.message = message

class EconomyConnection:
    def __init__(self, url: str, port: int):
        self.url = url
        self.port = port

    def get_balance(self, account, currency_id, return_code=False):
        if not check_correct(account):
            raise ValueError(f"Invalid account: {account}")

        payload = {
            "account": account,
            "currency_id": currency_id
        }

        response = requests.post(f"{self.url}:{self.port}/public/balance", json=payload, timeout=15)

        try:
            data = response.json()
        except ValueError:
            data = {"error": "Invalid JSON response"}

        if response.ok:
            return (response.status_code, data) if return_code else data
        else:
            raise EconomyAPIError(response.status_code, data.get("error", "Unknown error"))

    def transaction(self, account, currency_id, recipient, amount, return_code=False):
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

        try:
            data = response.json()
        except ValueError:
            data = {"error": "Invalid JSON response"}

        if response.ok:
            return (response.status_code, data) if return_code else data
        else:
            raise EconomyAPIError(response.status_code, data.get("error", "Unknown error"))