import streamlit as st
import controller as ctrl

def init_title() -> None:
    st.title("Black-Scholes Options Pricer")

def init_sidebar() -> None:
    st.sidebar.title("Black-Scholes Model")
    stock_price: float = st.sidebar.number_input(label="Current Stock Price", min_value=0.0)
    strike_price: float = st.sidebar.number_input(label="Strike Price", min_value=0.0)
    years_to_exp: int = st.sidebar.number_input(label="Years to Maturity", min_value=0.0)
    sigma: float = st.sidebar.number_input(label="Volatility (σ)", min_value=0.0)
    risk_free_rate: float = st.sidebar.number_input(label="Risk Free Rate")
    
    st.session_state['S'] = stock_price
    st.session_state['K'] = strike_price
    st.session_state['T'] = years_to_exp
    st.session_state['sigma'] = sigma
    st.session_state['r'] = risk_free_rate

def dollar_format(price: float) -> str:
    return f"${price:.2f}"

def get_call_price() -> str:
    call_price: float = ctrl.get_call_price()
    
    if call_price is not None:
        return dollar_format(call_price)
    else:
        return ""

def get_put_price() -> str:
    put_price: float = ctrl.get_put_price()

    if put_price is not None:
        return dollar_format(put_price)
    else:
        return ""

def price_display() -> None:
    col1, col2 = st.columns(2)

    call_price: str = get_call_price()
    put_price: str = get_put_price()

    with col1:
        with st.container():
            st.markdown(f"""
                <div style="
                    background-color: #00C805;
                    padding: 0px;
                    border-radius: 10px;
                    text-align: center;
                ">
                    <h3>CALL Value</h3>
                    <h2>{call_price}</h2>
                </div>
            """, unsafe_allow_html=True)

    with col2:
        with st.container():
            st.markdown(f"""
                <div style="
                    background-color: #FF3B30;
                    padding: 0px;
                    border-radius: 10px;
                    text-align: center;
                ">
                    <h3>PUT Value</h3>
                    <h2>{put_price}</h2>
                </div>
            """, unsafe_allow_html=True)
    
    
if __name__ == '__main__':
    init_title()
    init_sidebar()
    price_display() 
