# Global
import requests

# Local
from .helper import check_correct, get_id

class EconomyAPIError(Exception):
    def __init__(self, status_code, message):
        super().__init__(f"Error {status_code}: {message}")
        self.status_code = status_code
        self.message = message

class EconomyConnection:
    def __init__(self, url: str, port: int):
        if not url and not port:
            self.url = "http://utopia.wisp.uno:11132/"
        
        self.url = f"{url}:{port}" if port else url

    def get_id_from_account(self, account: str, currency_id: int):
        if not check_correct(account):
            return None

        user_id = get_id(account)
        try:
            self.get_balance(account=account, currency_id=currency_id, return_code=False)
            return user_id
        except Exception:
            return None

    def get_balance(self, account: str, currency_id: int, return_code: bool=False):
        if not check_correct(account):
            raise EconomyAPIError(401, f"Invalid account: {account}")

        payload = {
            "account": account,
            "currency_id": currency_id
        }

        response = requests.post(f"{self.url}/public/balance", json=payload, timeout=15)

        try:
            response.raise_for_status()
            data = response.json()
        except requests.HTTPError:
            try:
                data = response.json()
            except ValueError:
                data = {"error": "Invalid JSON response"}
            raise EconomyAPIError(response.status_code, data.get("error", "Unknown error"))

        if response.ok:
            return (response.status_code, data) if return_code else data
        else:
            raise EconomyAPIError(response.status_code, data.get("error", "Unknown error"))
    
    def get_economy_stats(self, account: str, currency_id: int, return_code: bool=False):
        if not check_correct(account):
            raise EconomyAPIError(401, f"Invalid account: {account}")

        payload = {
            "account": account,
            "currency_id": currency_id
        }

        response = requests.post(f"{self.url}/public/infos", json=payload, timeout=15)

        try:
            response.raise_for_status()
            data = response.json()
        except requests.HTTPError:
            try:
                data = response.json()
            except ValueError:
                data = {"error": "Invalid JSON response"}
            raise EconomyAPIError(response.status_code, data.get("error", "Unknown error"))

        if response.ok:
            return (response.status_code, data) if return_code else data
        else:
            raise EconomyAPIError(response.status_code, data.get("error", "Unknown error"))

    def transaction(self, account: str, currency_id: int, recipient: int, amount: int, return_code=False):
        if amount < 1:
            raise EconomyAPIError(402, f"Invalid amount: {amount}")

        if recipient < 0:
            raise EconomyAPIError(402, f"Invalid recipient: {recipient}")

        if not check_correct(account):
            raise EconomyAPIError(401, f"Invalid account: {account}")

        payload = {
            "account": account,
            "currency_id": currency_id,
            "recipient": recipient,
            "amount": amount
        }

        response = requests.post(f"{self.url}/public/transaction", json=payload, timeout=15)

        try:
            data = response.json()
        except ValueError:
            data = {"error": "Invalid JSON response"}

        if response.ok:
            return (response.status_code, data) if return_code else data
        else:
            raise EconomyAPIError(response.status_code, data.get("error", "Unknown error"))
