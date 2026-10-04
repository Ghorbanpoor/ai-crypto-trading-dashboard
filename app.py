import streamlit as st
import pandas as pd
import numpy as np
import random
import time
from datetime import datetime

# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Crypto Trader",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #0b1020;
}

[data-testid="stSidebar"] {
    background-color: #111827;
}

.block-container {
    padding-top: 1.5rem;
}

h1, h2, h3 {
    color: white;
}

.metric-card {
    background: #151c2f;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #26304a;
}

.price {
    font-size: 30px;
    font-weight: bold;
    color: white;
}

.green {
    color: #00d084;
}

.red {
    color: #ff4d67;
}

.signal-buy {
    background: #063b2a;
    border: 1px solid #00d084;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
}

.signal-sell {
    background: #421522;
    border: 1px solid #ff4d67;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
}

.signal-hold {
    background: #3d3211;
    border: 1px solid #f5c542;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
}

.trade-box {
    background: #151c2f;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #26304a;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# SESSION STATE
# ============================================================

if "balance" not in st.session_state:
    st.session_state.balance = 1000.0

if "profit" not in st.session_state:
    st.session_state.profit = 0.0

if "trades" not in st.session_state:
    st.session_state.trades = []

if "prices" not in st.session_state:
    st.session_state.prices = {
        "BTC/USDT": 68000.0,
        "ETH/USDT": 2450.0,
        "SOL/USDT": 155.0,
        "BNB/USDT": 610.0
    }

# ============================================================
# FUNCTIONS
# ============================================================

def update_prices():

    for symbol in st.session_state.prices:

        old_price = st.session_state.prices[symbol]

        change = np.random.normal(0, 0.002)

        new_price = old_price * (1 + change)

        st.session_state.prices[symbol] = new_price


def generate_signal(symbol):

    r = random.random()

    if r > 0.66:
        return "BUY", random.randint(70, 95)

    elif r < 0.33:
        return "SELL", random.randint(70, 95)

    return "HOLD", random.randint(55, 75)


def execute_trade(symbol, direction, amount):

    price = st.session_state.prices[symbol]

    if amount <= 0:
        return

    if amount > st.session_state.balance:
        st.error("Insufficient demo balance.")
        return

    # Simulated outcome
    market_move = np.random.normal(0, 0.01)

    if direction == "BUY":
        result = amount * market_move

    else:
        result = amount * (-market_move)

    st.session_state.balance += result
    st.session_state.profit += result

    trade = {
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Asset": symbol,
        "Direction": direction,
        "Amount": round(amount, 2),
        "Entry Price": round(price, 4),
        "Result": round(result, 2)
    }

    st.session_state.trades.insert(0, trade)


# ============================================================
# UPDATE MARKET
# ============================================================

update_prices()

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("# 🤖 AI Trader")

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "⚡ 60 Second Trade",
            "📊 Market",
            "📜 Trade History",
            "💼 Portfolio"
        ]
    )

    st.markdown("---")

    st.caption("Demo Trading Platform")
    st.caption("No real funds are used.")

# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    st.title("AI Crypto Trading Dashboard")

    st.write(
        "AI-assisted cryptocurrency trading simulation."
    )

    # --------------------------------------------------------
    # ACCOUNT METRICS
    # --------------------------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Demo Balance",
            f"${st.session_state.balance:,.2f}"
        )

    with c2:
        st.metric(
            "Total P/L",
            f"${st.session_state.profit:,.2f}"
        )

    with c3:
        st.metric(
            "Trades",
            len(st.session_state.trades)
        )

    with c4:
        if st.session_state.balance > 1000:
            roi = (
                (st.session_state.balance - 1000)
                / 1000
                * 100
            )
        else:
            roi = (
                (st.session_state.balance - 1000)
                / 1000
                * 100
            )

        st.metric(
            "ROI",
            f"{roi:.2f}%"
        )

    st.markdown("---")

    # --------------------------------------------------------
    # MARKET
    # --------------------------------------------------------

    st.subheader("Live Market Simulation")

    cols = st.columns(4)

    for i, (symbol, price) in enumerate(
        st.session_state.prices.items()
    ):

        with cols[i]:

            st.markdown(
                f"""
                <div class="metric-card">

                <b>{symbol}</b>

                <div class="price">
                ${price:,.2f}
                </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("---")

    # --------------------------------------------------------
    # AI SIGNALS
    # --------------------------------------------------------

    st.subheader("🤖 AI Market Signals")

    cols = st.columns(4)

    for i, symbol in enumerate(
        st.session_state.prices.keys()
    ):

        signal, confidence = generate_signal(symbol)

        with cols[i]:

            if signal == "BUY":
                css = "signal-buy"

            elif signal == "SELL":
                css = "signal-sell"

            else:
                css = "signal-hold"

            st.markdown(
                f"""
                <div class="{css}">

                <h3>{signal}</h3>

                <p>{symbol}</p>

                <b>Confidence: {confidence}%</b>

                </div>
                """,
                unsafe_allow_html=True
            )

# ============================================================
# 60 SECOND TRADING
# ============================================================

elif page == "⚡ 60 Second Trade":

    st.title("⚡ 60 Second Trading")

    st.warning(
        "Demo mode only. No real money is involved."
    )

    symbol = st.selectbox(
        "Select Asset",
        list(st.session_state.prices.keys())
    )

    price = st.session_state.prices[symbol]

    st.markdown(
        f"""
        <div class="trade-box">

        <h2>{symbol}</h2>

        <div class="price">
        ${price:,.4f}
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 🤖 AI Signal")

    signal, confidence = generate_signal(symbol)

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "AI Signal",
            signal
        )

    with c2:

        st.metric(
            "Confidence",
            f"{confidence}%"
        )

    st.markdown("---")

    amount = st.number_input(
        "Trade Amount (USDT)",
        min_value=1.0,
        max_value=float(st.session_state.balance),
        value=10.0,
        step=1.0
    )

    st.markdown(
        "### Choose Direction"
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🟢 BUY",
            use_container_width=True
        ):

            execute_trade(
                symbol,
                "BUY",
                amount
            )

            st.success(
                "BUY trade executed in demo mode."
            )

    with col2:

        if st.button(
            "🔴 SELL",
            use_container_width=True
        ):

            execute_trade(
                symbol,
                "SELL",
                amount
            )

            st.success(
                "SELL trade executed in demo mode."
            )

    st.markdown("---")

    st.subheader("⏱️ Trade Duration")

    st.info(
        "60-second settlement is simulated. "
        "The current version does not connect to a real exchange."
    )

# ============================================================
# MARKET
# ============================================================

elif page == "📊 Market":

    st.title("📊 Crypto Market")

    rows = []

    for symbol, price in st.session_state.prices.items():

        change = np.random.uniform(
            -3,
            3
        )

        rows.append(
            {
                "Asset": symbol,
                "Price": round(price, 4),
                "24h Change": f"{change:.2f}%"
            }
        )

    df = pd.DataFrame(rows)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    symbol = st.selectbox(
        "Chart Asset",
        list(st.session_state.prices.keys())
    )

    base = st.session_state.prices[symbol]

    history = []

    current = base

    for i in range(100):

        current *= (
            1 + np.random.normal(
                0,
                0.003
            )
        )

        history.append(current)

    chart_df = pd.DataFrame(
        {
            "Price": history
        }
    )

    st.line_chart(chart_df)

# ============================================================
# TRADE HISTORY
# ============================================================

elif page == "📜 Trade History":

    st.title("📜 Trading History")

    if len(st.session_state.trades) == 0:

        st.info(
            "No trades have been executed yet."
        )

    else:

        df = pd.DataFrame(
            st.session_state.trades
        )

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

# ============================================================
# PORTFOLIO
# ============================================================

elif page == "💼 Portfolio":

    st.title("💼 Portfolio")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Cash",
            f"${st.session_state.balance:,.2f}"
        )

    with c2:
        st.metric(
            "Profit/Loss",
            f"${st.session_state.profit:,.2f}"
        )

    with c3:

        roi = (
            st.session_state.profit
            / 1000
            * 100
        )

        st.metric(
            "ROI",
            f"{roi:.2f}%"
        )

    st.markdown("---")

    if st.session_state.trades:

        df = pd.DataFrame(
            st.session_state.trades
        )

        total_trades = len(df)

        winning = len(
            df[df["Result"] > 0]
        )

        losing = len(
            df[df["Result"] < 0]
        )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Total Trades",
            total_trades
        )

        c2.metric(
            "Winning",
            winning
        )

        c3.metric(
            "Losing",
            losing
        )

    else:

        st.info(
            "Portfolio statistics will appear "
            "after your first demo trade."
        )

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "AI Crypto Trader — Educational Demo Platform"
)