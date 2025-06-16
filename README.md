# EconomyConnection API Client

A lightweight Python client for interacting with the Economy Service API.
Enables secure queries of account balances and performing transactions with built-in input validation and error handling.

---

## Features

* Retrieve the balance for a given account and currency.
* Perform validated transactions between accounts.
* Validates account ID format before making requests.
* Gracefully handles API errors by raising descriptive exceptions.

---

## Installation

Make sure Python is installed on your system, then run:

```bash
pip install git+https://github.com/Ghosteined/vaihtaa_api
```

---

## Usage

### Connect to the API Server

Create an `EconomyConnection` instance specifying the server URL and port.

```python
from vaihtaa_api import EconomyConnection

eco = EconomyConnection(url="http://localhost", port=5000)
```

### Query Account Balance

Retrieve the balance for a specific account string (e.g., `"account-xyz-abc"`) and currency ID (e.g., `1`):

```python
balance = eco.get_balance("account-xyz-abc", 1)
print(f"User has {balance.balance} units of currency {balance.currency_id}.")
```

### Perform a Transaction

Send funds from an account to a recipient by specifying the sender’s account string, currency ID, recipient ID, and amount:

```python
eco.transaction("account-xyz-abc", 1, 42, 50)
```

---

## Notes

* Account strings are validated internally; ensure your account IDs match the required format.
* API errors (e.g., invalid requests or network issues) will raise exceptions — handle them as needed.
