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
    # d1 = (math.log(S / K) + (r + (sigma ** 2) / 2) * T) / (sigma * math.sqrt(T))
    d1: float = calc_d1(S, K, T, r, sigma)
    d2: float = calc_d2(d1, T, sigma)

    if option_type == 'call':
        return S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)

    elif option_type == 'put':
        return K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

def calc_d1(S: float, K: float, T: float, r: float, sigma: float) -> float:
    return (math.log(S / K) + (r + (sigma ** 2) / 2) * T) / (sigma * math.sqrt(T))

def calc_d2(d1: float, T: float, sigma: float) -> float:
    return d1 - sigma * math.sqrt(T)

def calc_delta(S: float, K: float, T: float, r: float, sigma: float, option_type: str) -> float:
    # Measures the rate of change of the options's price with response to the underlying asset's price
    # If the price of the underlying asset increases by $1, the price of the option will change by delta dollars.
    if option_type == 'call':
        d1: float = calc_d1(S, K, T, r, sigma)
        return norm.cdf(d1)
    
    elif option_type == 'put':
        d1: float = calc_d1(S, K, T, r, sigma)
        return norm.cdf(d1) - 1

def calc_gamma(S: float, K: float, T: float, r: float, sigma: float) -> float:
    # Measures the rate of change of the delta with respect to the underlying asset's price
    # If the price of the underlying asset increases by $1, the option’s delta will change by gamma dollars.

    d1: float = calc_d1(S, K, T, r, sigma)
    return norm.pdf(d1) / (S * sigma * math.sqrt(T))

def calc_theta(S: float, K: float, T: float, r: float, sigma: float, option_type: str) -> float:
    # Measures the rate of change of the option's price with respect to time
    # If the option's time to maturity decreases by one day, the optin's price will change by theta dollars.
  
    d1: float = calc_d1(S, K, T, r, sigma)
    d2: float = calc_d2(d1, T, sigma)

    if option_type == 'call':
        return -(S * norm.pdf(d1) * sigma) / (2 * math.sqrt(T)) - r * K * math.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        return -(S * norm.pdf(d1) * sigma) / (2 * math.sqrt(T)) + r * K * math.exp(-r * T) * norm.cdf(-d2)

def calc_vega(S: float, K: float, T: float, r: float, sigma: float) -> float:
    # Measures the rate of change of the option's price with respect to the volatility of the underlying asset
    # If the volatility of the underlying asset increases by 1%, the option's price will change by vega dollars.

    d1: float = calc_d1(S, K, T, r, sigma)
    return S * norm.pdf(d1) * math.sqrt(T) / 100

def calc_rho(S: float, K: float, T: float, r: float, sigma: float, option_type: str) -> float:
    # Measures the rate of change of the option's price with respect to the risk-free interest rate.
    # If the risk-free interest rate increases by 1%, the option's price will change by rho dollars.
    
    d1: float = calc_d1(S, K, T, r, sigma)
    d2: float = calc_d2(d1, T, sigma)

    if option_type == 'call':
        return K * T * math.exp(-r * T) * norm.cdf(d2) / 100
    
    if option_type == 'put':
        return - K * T * math.exp(-r * T) * norm.cdf(-d2) / 100
        