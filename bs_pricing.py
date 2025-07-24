import math
from scipy.stats import norm

def calculate_d1(S, K, T, r, sigma):
    """
    Calculate d1 in the Black-Scholes formula
    """
    numerator = math.log(S / K) + (r + 0.5 * sigma ** 2) * T
    denominator = sigma * math.sqrt(T)
    return numerator / denominator

def calculate_d2(d1, sigma, T):
    """
    Calculate d2 from d1
    """
    return d1 - sigma * math.sqrt(T)

def black_scholes_call(S, K, T, r, sigma):
    """
    Price of a European call option
    """
    d1 = calculate_d1(S, K, T, r, sigma)
    d2 = calculate_d2(d1, sigma, T)
    return S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)

def black_scholes_put(S, K, T, r, sigma):
    """
    Price of a European put option
    """
    d1 = calculate_d1(S, K, T, r, sigma)
    d2 = calculate_d2(d1, sigma, T)
    return K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)