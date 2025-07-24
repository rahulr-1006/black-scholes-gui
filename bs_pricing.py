import math
from scipy.stats import norm

def d1(S, K, T, r, sigma):
    return (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))

def d2(S, K, T, r, sigma):
    return d1(S, K, T, r, sigma) - sigma * math.sqrt(T)

def black_scholes_call(S, K, T, r, sigma):
    d_1 = d1(S, K, T, r, sigma)
    d_2 = d2(S, K, T, r, sigma)
    return S * norm.cdf(d_1) - K * math.exp(-r * T) * norm.cdf(d_2)

def black_scholes_put(S, K, T, r, sigma):
    d_1 = d1(S, K, T, r, sigma)
    d_2 = d2(S, K, T, r, sigma)
    return K * math.exp(-r * T) * norm.cdf(-d_2) - S * norm.cdf(-d_1)

# Greeks
def delta_call(S, K, T, r, sigma):
    return norm.cdf(d1(S, K, T, r, sigma))

def delta_put(S, K, T, r, sigma):
    return norm.cdf(d1(S, K, T, r, sigma)) - 1

def gamma(S, K, T, r, sigma):
    d_1 = d1(S, K, T, r, sigma)
    return norm.pdf(d_1) / (S * sigma * math.sqrt(T))

def vega(S, K, T, r, sigma):
    d_1 = d1(S, K, T, r, sigma)
    return S * norm.pdf(d_1) * math.sqrt(T)

def theta_call(S, K, T, r, sigma):
    d_1 = d1(S, K, T, r, sigma)
    d_2 = d2(S, K, T, r, sigma)
    first = -(S * norm.pdf(d_1) * sigma) / (2 * math.sqrt(T))
    second = r * K * math.exp(-r * T) * norm.cdf(d_2)
    return first - second

def theta_put(S, K, T, r, sigma):
    d_1 = d1(S, K, T, r, sigma)
    d_2 = d2(S, K, T, r, sigma)
    first = -(S * norm.pdf(d_1) * sigma) / (2 * math.sqrt(T))
    second = r * K * math.exp(-r * T) * norm.cdf(-d_2)
    return first + second
