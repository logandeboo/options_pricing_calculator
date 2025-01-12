import math
from scipy.stats import norm

def black_scholes(S: float, K: float, T: float, r: float, sigma: float, option_type: str) -> float:
    """
    Calculate Black-Scholes option price.
    
    Parameters:
    S : float : Current stock price
    K : float : Option strike price
    T : float : Time to maturity in years
    r : float : Risk-free interest rate
    sigma : float : Volatility of the underlying asset
    option_type : str : 'call' for call option, 'put' for put option
    
    Returns:
    float : Option price
    """

    # Calculate d1 and d2
    d1 = (math.log(S / K) + (r + (sigma ** 2) / 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == 'call':
        return S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)

    elif option_type == 'put':
        return K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)