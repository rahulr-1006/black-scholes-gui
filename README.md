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

<img width="1389" height="822" alt="image" src="https://github.com/user-attachments/assets/21be6a6a-21bd-4b97-9785-65ccdc6f8a57" />


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

- **Delta (Call):** Delta = N(d₁)
- **Delta (Put):** Delta = N(d₁) − 1
- **Gamma:** Gamma = N′(d₁) / [S × σ × √T]
- **Vega:** Vega = S × N′(d₁) × √T
- **Theta (Call):** 
  Theta = [−S × N′(d₁) × σ / (2√T)] − rK × e^(−rT) × N(d₂)
- **Theta (Put):** 
  Theta = [−S × N′(d₁) × σ / (2√T)] + rK × e^(−rT) × N(−d₂)


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
