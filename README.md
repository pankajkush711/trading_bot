# Binance Trading Bot (Testnet)

A simplified Python trading bot that places MARKET and LIMIT orders on Binance Testnet using a clean, structured architecture with proper logging and error handling.

---

## 📌 Project Overview

This application allows users to place BUY or SELL orders via CLI on Binance Testnet.

The project demonstrates:

- Structured project architecture
- Separation of concerns (API layer, business logic, CLI)
- Input validation
- Proper exception handling
- Logging of requests, responses, and errors
- Secure API key handling using environment variables

---

## 🏗 Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance API wrapper
│   ├── orders.py          # Order execution logic
│   ├── validators.py      # Input validation
│   └── logging_config.py  # Logging configuration
│
├── logs/                  # Log files generated here
├── cli.py                 # CLI entry point
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone or Download Project

```bash
git clone <your-repository-link>
cd trading_bot
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Create `.env` File

Create a file named `.env` in the project root directory:

```
API_KEY=your_api_key_here
API_SECRET=your_secret_key_here
```

⚠️ Do NOT commit this file to GitHub.

---

## 🚀 How to Run

### ✅ Place MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

### ✅ Place LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 67000
```

(Ensure the LIMIT price is near the current market price.)

---

## 🖥 Sample Output

```
===== ORDER SUMMARY =====
Symbol: BTCUSDT
Side: SELL
Type: LIMIT
Quantity: 0.001
Price: 67000.0

===== ORDER RESPONSE =====
Order ID: 5341521
Status: NEW
Executed Qty: 0.00000000

✅ Order Successful!
```

---

## 📝 Logging

All API requests, responses, and errors are logged in:

```
logs/trading_bot.log
```

Logs include:
- Timestamp
- Order request parameters
- API response details
- Error messages (if any)

---

## 🛡 Error Handling

The application handles:

- Invalid side input
- Invalid order type
- Missing price for LIMIT orders
- Negative quantity values
- Binance API errors
- Network failures

---

## 📦 Requirements

- Python 3.x
- python-binance
- python-dotenv

---

## ⚠️ Note

Due to regional restrictions on Binance Futures Testnet access, Binance Spot Testnet was used instead.

The project architecture remains fully compatible with Binance Futures endpoints and can easily be extended to support Futures trading by switching the client implementation.

---

## 🧠 Design Approach

The project follows a layered architecture:

- **CLI Layer** → Handles user input
- **Service Layer** → Business logic and validation
- **Client Layer** → API communication
- **Logging Layer** → Centralized logging

This design ensures:

- Maintainability
- Scalability
- Clean separation of concerns
- Reusability of components

---

## 📧 Submission Includes

- Source code
- requirements.txt
- README.md
- Log file (with MARKET and LIMIT order examples)

---