# ai-crypto-trading-dashboard
AI-powered cryptocurrency trading dashboard built with Python and Streamlit. Includes market simulation, AI trading signals, 60-second demo trades, portfolio tracking, and trade history.

## Features

* 📊 Cryptocurrency market dashboard
* 🤖 AI-inspired BUY / SELL / HOLD signals
* ⚡ 60-second demo trading
* 💰 Virtual USDT balance
* 📈 Profit and Loss tracking
* 💼 Portfolio management
* 📜 Trading history
* 📉 Simulated cryptocurrency price charts
* 📱 Responsive Streamlit interface
* 🧪 Fully simulated trading environment
* 🚫 No real money or real orders are used

## Supported Assets

The current demo includes:

* BTC/USDT
* ETH/USDT
* SOL/USDT
* BNB/USDT

## Project Structure

```text
ai-crypto-trading-dashboard/
│
├── app.py
├── requirements.txt
└── README.md
```

## Requirements

* Python 3.9+
* Streamlit
* Pandas
* NumPy

## Installation

Clone the repository:

```bash
git clone https://github.com/Ghorbanpoor/ai-crypto-trading-dashboard.git
cd ai-crypto-trading-dashboard
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Run the Application

Start Streamlit with:

```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

If Streamlit is not recognized, use:

```bash
python -m streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

## GitHub Codespaces

This project can be run directly in **GitHub Codespaces**.

After opening the repository in Codespaces:

```bash
pip install -r requirements.txt
```

Then:

```bash
python -m streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

Open port **8501** in the Codespaces Ports panel to access the dashboard.

## How It Works

The application generates simulated cryptocurrency prices and provides AI-inspired market signals.

Each signal can be:

```text
BUY
SELL
HOLD
```

A confidence percentage is also generated for each signal.

Users can select an asset, enter a virtual trade amount, and execute a simulated BUY or SELL trade.

The application then updates the virtual balance and records the trade in the trading history.

## Demo Trading

The default virtual balance is:

```text
$1,000 USDT
```

All transactions are simulated.

No real cryptocurrency is purchased or sold.

## Important Disclaimer

This project is an **educational and experimental demo**.

The market prices, AI signals, trade results, and portfolio performance are simulated and should not be considered financial advice or predictions of real cryptocurrency markets.

Do not use the current version for real-money trading.

## Future Development

Possible future improvements include:

* Real-time cryptocurrency price APIs
* Binance or Bitpin API integration
* Technical indicators such as RSI, MACD, and moving averages
* Machine-learning price prediction
* Advanced AI trading signals
* User authentication
* SQLite/PostgreSQL database
* Real-time charts
* Backtesting engine
* Risk management
* Stop-loss and take-profit
* Trading bot automation
* API-based exchange execution
* Admin dashboard

## Technology Stack

* **Python**
* **Streamlit**
* **Pandas**
* **NumPy**
* **GitHub Codespaces**

## License

This project is intended for educational and research purposes.
