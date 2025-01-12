import model
import streamlit as st
import mibian

def get_call_price() -> float:
    
    S: float = st.session_state['S']
    K: float = st.session_state['K']
    T: float = st.session_state['T']
    r: float = st.session_state['r']
    sigma: float = st.session_state['sigma']
    option_type: str = 'call'

    if S == 0 or K == 0 or T == 0 or sigma == 0:
        return 0

    call_price: float = model.black_scholes(S, K, T, r, sigma, option_type)
    return call_price

def get_put_price() -> float:
    
    S: float = st.session_state['S']
    K: float = st.session_state['K']
    T: float = st.session_state['T']
    r: float = st.session_state['r']
    sigma: float = st.session_state['sigma']
    option_type: str = 'put'

    if S == 0 or K == 0 or T == 0 or sigma == 0:
        return 0

    put_price: float = model.black_scholes(S, K, T, r, sigma, option_type)
    return put_price


