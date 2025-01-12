from ..src import model
import mibian


def convert_pct_to_dec(val: float) -> float:
    return val / 100

# Validate my implementation of Black-Scholes model against mibian's implementation
def test_bs_1() -> None:
    S = 100
    K = 100
    T = 365
    r = 5 
    sigma = 20 

    bs = mibian.BS([S, K, r, T], volatility=sigma)

    my_call_price = bs.callPrice
    my_put_price = bs.putPrice

    T = 1
    r = convert_pct_to_dec(r)
    sigma = convert_pct_to_dec(sigma)

    third_prty_call_price = model.black_scholes(S, K, T, r, sigma, 'call')
    third_prty_put_price = model.black_scholes(S, K, T, r, sigma, 'put')

    assert my_call_price == third_prty_call_price
    assert my_put_price == third_prty_put_price


def test_bs_2() -> None:
    S = 150
    K = 90  
    T = 365 * 2  
    r = 8  
    sigma = 25 

    bs = mibian.BS([S, K, r, T], volatility=sigma)

    my_call_price = bs.callPrice
    my_put_price = bs.putPrice

    T = 2
    r = convert_pct_to_dec(r)
    sigma = convert_pct_to_dec(sigma)

    third_prty_call_price = model.black_scholes(S, K, T, r, sigma, 'call')
    third_prty_put_price = model.black_scholes(S, K, T, r, sigma, 'put')

    assert my_call_price == third_prty_call_price
    assert my_put_price == third_prty_put_price


def test_edge_cases() -> None:
    # low stock price
    S = 1
    K = 100
    T = 365
    r = 5
    sigma = 20

    bs = mibian.BS([S, K, r, T], volatility=sigma)
    my_call_price = bs.callPrice
    my_put_price = bs.putPrice

    T = 1
    r = convert_pct_to_dec(r)
    sigma = convert_pct_to_dec(sigma)

    third_prty_call_price = model.black_scholes(S, K, T, r, sigma, 'call')
    third_prty_put_price = model.black_scholes(S, K, T, r, sigma, 'put')

    assert my_call_price == third_prty_call_price
    assert my_put_price == third_prty_put_price

    # high stock price
    S = 1000
    K = 100
    T = 365
    r = 5
    sigma = 20

    bs = mibian.BS([S, K, r, T], volatility=sigma)
    my_call_price = bs.callPrice
    my_put_price = bs.putPrice

    T = 1
    r = convert_pct_to_dec(r)
    sigma = convert_pct_to_dec(sigma)

    third_prty_call_price = model.black_scholes(S, K, T, r, sigma, 'call')
    third_prty_put_price = model.black_scholes(S, K, T, r, sigma, 'put')

    assert my_call_price == third_prty_call_price
    assert my_put_price == third_prty_put_price
