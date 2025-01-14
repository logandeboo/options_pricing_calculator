from ..src.black_scholes import BlackScholes
import mibian


def convert_pct_to_dec(val: float) -> float:
    return val / 100


def test_bs_1() -> None:
    S = 100
    K = 100
    T = 365
    r = 5 
    sigma = 20 

    bs = mibian.BS([S, K, r, T], volatility=sigma)
    mibian_call = bs.callPrice
    mibian_put = bs.putPrice

    # Create BlackScholes instance with converted values
    my_bs = BlackScholes(S, K, T/365, convert_pct_to_dec(r), convert_pct_to_dec(sigma))
    my_call = my_bs.price('call')
    my_put = my_bs.price('put')

    assert mibian_call == my_call
    assert mibian_put == my_put


def test_bs_2() -> None:
    S = 150
    K = 90  
    T = 365 * 2  
    r = 8  
    sigma = 25 

    bs = mibian.BS([S, K, r, T], volatility=sigma)
    mibian_call = bs.callPrice
    mibian_put = bs.putPrice

    my_bs = BlackScholes(S, K, T/365, convert_pct_to_dec(r), convert_pct_to_dec(sigma))
    my_call = my_bs.price('call')
    my_put = my_bs.price('put')

    assert mibian_call == my_call
    assert mibian_put == my_put


def test_bs_3() -> None:
    # low stock price
    S = 1
    K = 100
    T = 365
    r = 5
    sigma = 20

    bs = mibian.BS([S, K, r, T], volatility=sigma)
    mibian_call = bs.callPrice
    mibian_put = bs.putPrice

    my_bs = BlackScholes(S, K, T/365, convert_pct_to_dec(r), convert_pct_to_dec(sigma))
    my_call = my_bs.price('call')
    my_put = my_bs.price('put')

    assert mibian_call == my_call
    assert mibian_put == my_put

    # high stock price
    S = 1000
    K = 100
    T = 365
    r = 5
    sigma = 20

    bs = mibian.BS([S, K, r, T], volatility=sigma)
    mibian_call = bs.callPrice
    mibian_put = bs.putPrice

    my_bs = BlackScholes(S, K, T/365, convert_pct_to_dec(r), convert_pct_to_dec(sigma))
    my_call = my_bs.price('call')
    my_put = my_bs.price('put')

    assert mibian_call == my_call
    assert mibian_put == my_put


def test_calc_delta() -> None:
    S = 100
    K = 100
    T = 365
    r = 5
    sigma = 20

    bs = mibian.BS([S, K, r, T], volatility=sigma)
    mibian_call_delta = bs.callDelta
    mibian_put_delta = bs.putDelta

    my_bs = BlackScholes(S, K, T/365, convert_pct_to_dec(r), convert_pct_to_dec(sigma))
    my_call_delta = my_bs.delta('call')
    my_put_delta = my_bs.delta('put')

    assert my_call_delta == mibian_call_delta
    assert my_put_delta == mibian_put_delta


def test_calc_gamma() -> None:
    S = 101
    K = 90
    T = 365
    r = 5
    sigma = 20

    bs = mibian.BS([S, K, r, T], volatility=sigma)
    mibian_gamma = bs.gamma

    my_bs = BlackScholes(S, K, T/365, convert_pct_to_dec(r), convert_pct_to_dec(sigma))
    my_gamma = my_bs.gamma()

    assert my_gamma == mibian_gamma


def test_calc_theta() -> None:
    S = 150
    K = 100
    T = 365
    r = 5
    sigma = 2

    bs = mibian.BS([S, K, r, T], volatility=sigma)
    mibian_call_theta = bs.callTheta
    mibian_put_theta = bs.putTheta

    my_bs = BlackScholes(S, K, T/365, convert_pct_to_dec(r), convert_pct_to_dec(sigma))
    my_call_theta = my_bs.theta('call')
    my_put_theta = my_bs.theta('put')

    assert my_call_theta == mibian_call_theta
    assert my_put_theta == mibian_put_theta


def test_calc_vega() -> None:
    S = 120
    K = 110
    T = 180
    r = 3
    sigma = 15

    bs = mibian.BS([S, K, r, T], volatility=sigma)
    mibian_vega = bs.vega

    my_bs = BlackScholes(S, K, T/365, convert_pct_to_dec(r), convert_pct_to_dec(sigma))
    my_vega = my_bs.vega()

    assert my_vega == mibian_vega


def test_calc_rho() -> None:
    S = 130
    K = 120
    T = 200
    r = 4
    sigma = 18

    bs = mibian.BS([S, K, r, T], volatility=sigma)
    mibian_call_rho = bs.callRho
    mibian_put_rho = bs.putRho

    my_bs = BlackScholes(S, K, T/365, convert_pct_to_dec(r), convert_pct_to_dec(sigma))
    my_call_rho = my_bs.rho('call')
    my_put_rho = my_bs.rho('put')

    assert my_call_rho == mibian_call_rho
    assert my_put_rho == mibian_put_rho