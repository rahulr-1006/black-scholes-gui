import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from bs_pricing import (
    black_scholes_call, black_scholes_put,
    delta_call, delta_put, gamma, vega, theta_call, theta_put
)

st.set_page_config(page_title="Black-Scholes Option Calculator", layout="centered")
st.title("Black-Scholes Option Pricing Tool")

# --- Inputs ---
st.sidebar.header("Option Parameters")
S = st.sidebar.slider("Spot Price (S)", min_value=50.0, max_value=150.0, value=100.0, step=0.5)
K = st.sidebar.slider("Strike Price (K)", min_value=50.0, max_value=150.0, value=100.0, step=0.5)
T = st.sidebar.slider("Time to Expiration (T, in years)", min_value=0.01, max_value=5.0, value=1.0, step=0.01)
r = st.sidebar.slider("Risk-Free Rate (r)", min_value=0.0, max_value=0.10, value=0.05, step=0.001)
sigma = st.sidebar.slider("Volatility (σ)", min_value=0.05, max_value=1.0, value=0.2, step=0.01)

# --- Prices ---
call_price = black_scholes_call(S, K, T, r, sigma)
put_price = black_scholes_put(S, K, T, r, sigma)

st.subheader("Option Prices")
st.write(f"**Call Option Price:** ${call_price:.2f}")
st.write(f"**Put Option Price:** ${put_price:.2f}")
st.caption("Based on Black-Scholes formula for European options.")

# --- Greeks ---
st.subheader("Option Greeks")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Call Option")
    st.write(f"**Delta:** {delta_call(S, K, T, r, sigma):.4f}")
    st.write(f"**Gamma:** {gamma(S, K, T, r, sigma):.4f}")
    st.write(f"**Vega:** {vega(S, K, T, r, sigma):.4f}")
    st.write(f"**Theta:** {theta_call(S, K, T, r, sigma):.4f}")

with col2:
    st.markdown("#### Put Option")
    st.write(f"**Delta:** {delta_put(S, K, T, r, sigma):.4f}")
    st.write(f"**Gamma:** {gamma(S, K, T, r, sigma):.4f}")
    st.write(f"**Vega:** {vega(S, K, T, r, sigma):.4f}")
    st.write(f"**Theta:** {theta_put(S, K, T, r, sigma):.4f}")

st.caption("Greeks measure sensitivities: Δ=price, Γ=curvature, ν=volatility, Θ=time decay")

# --- Payoff Plot ---
st.subheader("Option Payoff at Expiration")

option_type = st.radio("Select Option Type", ["Call", "Put"], horizontal=True)
S_range = np.linspace(0.5 * K, 1.5 * K, 100)

if option_type == "Call":
    payoff = np.maximum(S_range - K, 0) - call_price
else:
    payoff = np.maximum(K - S_range, 0) - put_price

fig, ax = plt.subplots()
ax.plot(S_range, payoff, label=f"{option_type} Payoff")
ax.axhline(0, color='gray', linestyle='--')
ax.set_xlabel("Stock Price at Expiration")
ax.set_ylabel("Profit / Loss")
ax.set_title(f"{option_type} Option Payoff")
ax.legend()
st.pyplot(fig)

# --- Volatility Sensitivity ---
st.subheader("Option Value vs. Volatility")

vol_range = np.linspace(0.01, 1.0, 100)
call_vals = [black_scholes_call(S, K, T, r, vol) for vol in vol_range]
put_vals = [black_scholes_put(S, K, T, r, vol) for vol in vol_range]

fig2, ax2 = plt.subplots()
ax2.plot(vol_range, call_vals, label='Call Price')
ax2.plot(vol_range, put_vals, label='Put Price')
ax2.set_xlabel("Volatility (σ)")
ax2.set_ylabel("Option Price")
ax2.set_title("Price Sensitivity to Volatility")
ax2.legend()
st.pyplot(fig2)

# --- Time Sensitivity ---
st.subheader("Option Value vs. Time to Expiration")

T_range = np.linspace(0.01, 2.0, 100)
call_T = [black_scholes_call(S, K, T_i, r, sigma) for T_i in T_range]
put_T = [black_scholes_put(S, K, T_i, r, sigma) for T_i in T_range]

fig3, ax3 = plt.subplots()
ax3.plot(T_range, call_T, label="Call Price")
ax3.plot(T_range, put_T, label="Put Price")
ax3.set_xlabel("Time to Expiration (T)")
ax3.set_ylabel("Option Price")
ax3.set_title("Option Price vs. Time to Expiration")
ax3.legend()
st.pyplot(fig3)
