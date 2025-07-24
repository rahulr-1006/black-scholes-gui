````markdown
# 📈 Black-Scholes Option Pricing Tool

An interactive Python web app that calculates and visualizes European option prices using the Black-Scholes model. Built with **Streamlit**, this tool lets users adjust inputs in real time and view live option pricing, payoff charts, and sensitivity plots.

---

## 🧮 Features

- 📊 **Live pricing** for European call and put options
- 🎛️ Adjustable sliders for \( S, K, T, r, \sigma \)
- 💰 Real-time output of call and put prices
- 📉 Payoff diagram at expiration
- 📈 Sensitivity to **volatility** and **time to expiration**
- 🧠 Educational tool for understanding option behavior

---

## 🚀 Getting Started

### 1. Install dependencies:
```bash
pip install -r requirements.txt
````

### 2. Run the app:

```bash
streamlit run app.py
```

---

## 📸 Screenshot

![Screenshot](screenshot.png)

---

## 📘 Formulae

Call option price:

$$
C = S \cdot N(d_1) - K \cdot e^{-rT} \cdot N(d_2)
$$

Put option price:

$$
P = K \cdot e^{-rT} \cdot N(-d_2) - S \cdot N(-d_1)
$$

---

## 📂 Project Structure

```
black-scholes-gui/
├── app.py             # Streamlit GUI
├── bs_pricing.py      # Pricing logic (d1, d2, call, put)
├── requirements.txt   # Required Python packages
├── README.md          # This file
```

---

## 📎 License

MIT License. Built by [Rahul Rengan Ramakrishnan](https://github.com/rahulr-1006).

````

---

Once you paste this in and commit it:

```bash
git add README.md
git commit -m "Add README with features, usage, and formulas"
git push origin main
````

Let me know when it's up — we’ll finalize your resume bullet with the live link.
