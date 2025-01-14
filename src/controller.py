import streamlit as st
import pandas as pd
from black_scholes import BlackScholesModel


def get_bs_model() -> BlackScholesModel:
    S: float = st.session_state['S']
    K: float = st.session_state['K']
    T: float = st.session_state['T']
    r: float = st.session_state['r']
    sigma: float = st.session_state['sigma']

    if S == 0 or K == 0 or T == 0 or sigma == 0:
        return

    bs_model = BlackScholesModel(S, K, T, r, sigma)
    st.session_state['bs_model'] = bs_model
    return bs_model

def get_call_price() -> float:
    if 'bs_model' in st.session_state.keys():        
        bs_model = st.session_state['bs_model']
        return bs_model.price('call')

def get_put_price() -> float:
    if 'bs_model' in st.session_state.keys(): 
        bs_model = st.session_state['bs_model']
        return bs_model.price('put')

def get_greeks() -> pd.DataFrame:
    if 'bs_model' in st.session_state.keys(): 
        bs_model = st.session_state['bs_model']
        
        greeks_dict = {
            'Delta (call)': bs_model.delta('call'),
            'Delta (put)': bs_model.delta('put'),
            'Gamma': bs_model.gamma(),
            'Theta (call)': bs_model.theta('call'),
            'Theta (put)': bs_model.theta('put'),
            'Vega': bs_model.vega()
        }
        return pd.DataFrame(greeks_dict, index=[0])




# def get_pnl_plot() -> float:
#     if 'bs_model' not in st.session_state.keys():
#         return 0
    
#     bs_model = st.session_state['bs_model']
#     return bs_model.pri


     


