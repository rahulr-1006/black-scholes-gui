# 📈 Black-Scholes Option Pricing Tool

An interactive Python web app that calculates and visualizes European option prices using the Black-Scholes model. Built with **Streamlit**, this tool lets users adjust inputs in real time and view live option pricing, payoff charts, sensitivity plots, and the Greeks. This is an extremely basic options model, solely for tutorial purposes. Improvements with better graphs and more customizability coming soon!

---

## 🧮 Features

- 📊 **Live pricing** for European call and put options
- 🎛️ Adjustable sliders for \( S, K, T, r, \sigma \)
- 💰 Real-time output of call and put prices
- 📉 Payoff diagram at expiration
- 📈 Sensitivity plots for **volatility** and **time to expiration**
- ⚙️ Computes core **Greeks** (Delta, Gamma, Vega, Theta)
- 🧠 Educational tool for understanding option behavior

---

## 🚀 Getting Started

### 1. Install dependencies:
```bash
pip install -r requirements.txt
```

### 2. Run the app:
```bash
streamlit run app.py
```

---

## 📸 Screenshot

![Screenshot](screenshot.png)

---

## 📘 Formulae

**Call Option Price:**
$$
C = S \cdot N(d_1) - K \cdot e^{-rT} \cdot N(d_2)
$$

**Put Option Price:**
$$
P = K \cdot e^{-rT} \cdot N(-d_2) - S \cdot N(-d_1)
$$

**Greeks:**

- **Delta (Call):** \( \Delta = N(d_1) \)
- **Delta (Put):** \( \Delta = N(d_1) - 1 \)
- **Gamma:** \( \Gamma = \frac{N'(d_1)}{S \cdot \sigma \sqrt{T}} \)
- **Vega:** \( \nu = S \cdot N'(d_1) \cdot \sqrt{T} \)
- **Theta (Call):** 
  $$
  \Theta = \frac{-S \cdot N'(d_1) \cdot \sigma}{2 \sqrt{T}} - rK e^{-rT} N(d_2)
  $$
- **Theta (Put):** 
  $$
  \Theta = \frac{-S \cdot N'(d_1) \cdot \sigma}{2 \sqrt{T}} + rK e^{-rT} N(-d_2)
  $$

---

## 📂 Project Structure

```
black-scholes-gui/
├── app.py             # Streamlit GUI
├── bs_pricing.py      # Pricing logic (d1, d2, call, put, Greeks)
├── requirements.txt   # Required Python packages
├── README.md          # This file
```

---

## 📎 License

MIT License. Built by [Rahul Rengan Ramakrishnan](https://github.com/rahulr-1006).
