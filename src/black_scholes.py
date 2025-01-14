import math
from scipy.stats import norm

class BlackScholes:
    def __init__(self, S: float, K: float, T: float, r: float, sigma: float):
        """
        Initialize Black-Scholes model with option parameters.
        
        Parameters:
        S : float : Current stock price
        K : float : Option strike price
        T : float : Time to maturity in years
        r : float : Risk-free interest rate
        sigma : float : Volatility of the underlying asset
        """
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        
        # Pre-calculate common values
        self.d1 = self._calc_d1()
        self.d2 = self._calc_d2()

    def _calc_d1(self) -> float:
        return (math.log(self.S / self.K) + (self.r + (self.sigma ** 2) / 2) * self.T) / (self.sigma * math.sqrt(self.T))

    def _calc_d2(self) -> float:
        return self.d1 - self.sigma * math.sqrt(self.T)

    def price(self, option_type: str) -> float:
        """Calculate Black-Scholes option price."""
        if option_type == 'call':
            return self.S * norm.cdf(self.d1) - self.K * math.exp(-self.r * self.T) * norm.cdf(self.d2)
        elif option_type == 'put':
            return self.K * math.exp(-self.r * self.T) * norm.cdf(-self.d2) - self.S * norm.cdf(-self.d1)

    def delta(self, option_type: str) -> float:
        """Calculate option delta."""
        if option_type == 'call':
            return norm.cdf(self.d1)
        elif option_type == 'put':
            return norm.cdf(self.d1) - 1

    def gamma(self) -> float:
        """Calculate option gamma."""
        return norm.pdf(self.d1) / (self.S * self.sigma * math.sqrt(self.T))

    def theta(self, option_type: str) -> float:
        """Calculate option theta."""
        if option_type == 'call':
            return (-(self.S * norm.pdf(self.d1) * self.sigma) / (2 * math.sqrt(self.T)) - 
                    self.r * self.K * math.exp(-self.r * self.T) * norm.cdf(self.d2)) / 365
        elif option_type == 'put':
            return (-(self.S * norm.pdf(self.d1) * self.sigma) / (2 * math.sqrt(self.T)) + 
                    self.r * self.K * math.exp(-self.r * self.T) * norm.cdf(-self.d2)) / 365

    def vega(self) -> float:
        """Calculate option vega."""
        return self.S * norm.pdf(self.d1) * math.sqrt(self.T) / 100

    def rho(self, option_type: str) -> float:
        """Calculate option rho."""
        if option_type == 'call':
            return self.K * self.T * math.exp(-self.r * self.T) * norm.cdf(self.d2) / 100
        elif option_type == 'put':
            return -self.K * self.T * math.exp(-self.r * self.T) * norm.cdf(-self.d2) / 100