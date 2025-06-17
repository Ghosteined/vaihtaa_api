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

Make sure [Python](https://www.python.org/downloads/) and [Git](https://git-scm.com/downloads) are installed on your system, then run:

```bash
pip install git+https://github.com/Ghosteined/vaihtaa_api
```

---

## Usage

### Connect to the API Server

Create an `EconomyConnection` instance specifying the server URL and port.

```python
from vaihtaa_api import EconomyConnection

# Create a local connection on port 5000
eco = EconomyConnection(url="http://localhost", port=5000)
```

### Query Account Balance

Retrieve the balance for a specific account string (e.g., `"account-xyz-abc"`) and currency ID (e.g., `1`):

```python
# Get user's balance
try:
    balance = eco.get_balance(account="account-xyz-abc", currency_id=1)
    print(f"User has {balance.get('balance')} units of currency.")
except Exception:
    print(f"User was not found.")
```

### Perform a Transaction

Send funds from an account to a recipient by specifying the sender’s account string, currency ID, recipient ID, and amount:

```python
# Perform a transaction
try:
    transaction = eco.transaction(account="account-xyz-abc", currency_id=1, recipient=42, amount=50)
    print(f"Transaction done successfully: {transaction.get('response')}.")
except Exception:
    print(f"Transaction failed.")
```

---

## Notes

* Account strings are validated internally; ensure your account IDs match the required format.
* API errors (e.g., invalid requests or network issues) will raise exceptions — handle them as needed.
