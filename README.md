# Black-Scholes Option Pricing & Visualization Tool

An interactive Streamlit app that calculates and visualizes **European option prices** using the **Black-Scholes model**, complete with dynamic payoff charts, volatility/time sensitivity graphs, **Greeks**, and **heatmaps**.

---

## Implementation Details

This app is built with clarity and education in mind. Below is a breakdown of what’s implemented and what each part contributes to the overall Black-Scholes pricing tool.

---

### Real-Time Pricing with Sliders

The sidebar of the app provides intuitive sliders for core Black-Scholes parameters:

| Parameter | Meaning |
|----------|---------|
| `S` | Spot price — current price of the underlying asset |
| `K` | Strike price — the price agreed in the option contract |
| `T` | Time to expiration (in years) |
| `r` | Risk-free interest rate |
| `σ` | Volatility — the expected fluctuation of the asset’s price |

These values dynamically update the call and put prices every time they are changed, providing real-time output using:

```python
black_scholes_call(S, K, T, r, sigma)
black_scholes_put(S, K, T, r, sigma)
````

---

### Visualizing Option Behavior

The app includes three core visualizations:

1. **Payoff Diagram**
   Shows how profit or loss changes depending on where the stock ends up at expiration.

2. **Sensitivity to Volatility**
   Demonstrates how increasing or decreasing volatility affects the value of call and put options.

3. **Sensitivity to Time to Expiration**
   Illustrates how time decay impacts option value, especially as expiration nears.

Each chart is generated using `matplotlib` and rendered in Streamlit with `st.pyplot()`.

---

### Heatmaps of Option Prices

To intuitively show how **spot price** and **volatility** affect call and put prices, the app generates two heatmaps:

* **Call Option Heatmap**
* **Put Option Heatmap**

Each heatmap shows price levels across a grid of:

* X-axis: Spot Prices
* Y-axis: Volatility (σ)

🔍 You can also view a table-style heatmap using Seaborn, where **each cell is annotated with the exact option price**, ideal for study or report use.

```python
sns.heatmap(call_df, annot=True, fmt=".2f", cmap="viridis")
```

---

### Greek Calculations

Greeks quantify how sensitive an option’s value is to different variables:

| Greek            | Description                         | Formula                                                                         |
| ---------------- | ----------------------------------- | ------------------------------------------------------------------------------- |
| **Delta (Call)** | Sensitivity to stock price          | $\Delta = N(d_1)$                                                               |
| **Delta (Put)**  | Sensitivity to stock price          | $\Delta = N(d_1) - 1$                                                           |
| **Gamma**        | Sensitivity of Delta to stock price | $\Gamma = \frac{N'(d_1)}{S \cdot \sigma \cdot \sqrt{T}}$                        |
| **Vega**         | Sensitivity to volatility           | $\text{Vega} = S \cdot N'(d_1) \cdot \sqrt{T}$                                  |
| **Theta (Call)** | Time decay                          | $\Theta = \frac{-S \cdot N'(d_1) \cdot \sigma}{2\sqrt{T}} - rK e^{-rT} N(d_2)$  |
| **Theta (Put)**  | Time decay                          | $\Theta = \frac{-S \cdot N'(d_1) \cdot \sigma}{2\sqrt{T}} + rK e^{-rT} N(-d_2)$ |

These are computed in `bs_pricing.py` using NumPy and SciPy for normal distribution evaluations.

---

### Educational Use Case

This app is designed as a **learning sandbox** for:

* Finance students trying to understand option pricing
* Interview prep for quant/dev roles
* Visual intuition for how Black-Scholes works
* Exploring how the Greeks behave near-the-money or close to expiration

---

## Getting Started

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

<img width="1389" height="822" alt="App Screenshot" src="https://github.com/user-attachments/assets/21be6a6a-21bd-4b97-9785-65ccdc6f8a57" />

---

## Formulae

**Call Option Price:**

$$
C = S \cdot N(d_1) - K \cdot e^{-rT} \cdot N(d_2)
$$

**Put Option Price:**

$$
P = K \cdot e^{-rT} \cdot N(-d_2) - S \cdot N(-d_1)
$$

---

## Project Structure

```
black-scholes-gui/
├── app.py             # Streamlit GUI logic
├── bs_pricing.py      # Pricing logic for d1, d2, call/put, and Greeks
├── requirements.txt   # Python dependencies
├── README.md          # This file
```

---

## License

MIT License. Built by [Rahul Rengan Ramakrishnan](https://github.com/rahulr-1006).
