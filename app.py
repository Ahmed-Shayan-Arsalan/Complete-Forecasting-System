import streamlit as st

# Title
st.title("Sector Forecasting System")

# Sidebar
st.sidebar.title("Select Sector")
selected_sector = st.sidebar.selectbox("Choose Sector", ["Finance", "Energy", "Environmental"])

# Display PNG files based on selected sector
if selected_sector == "Finance":
    st.sidebar.title("Finance Sector Models")
    selected_model = st.sidebar.selectbox("Select Model", ["ARIMA", "ETS", "Hybrid ANN", "LSTM", "Prophet", "SARIMA", "SVR"])
    
    if selected_model == "ARIMA":
        st.image("s&p/acf,pacf - arima.png", caption="ACF and PACF Plots")
    elif selected_model == "ETS":
        st.image("s&p/ets-forecast.png", caption="ETS Forecast")
    elif selected_model == "Hybrid ANN":
        st.image("s&p/hybrib-ann-forecast.png", caption="Hybrid ANN Forecast")
    elif selected_model == "LSTM":
        st.image("s&p/lstm-forecast.png", caption="LSTM Forecast")
    elif selected_model == "Prophet":
        st.image("s&p/prophet - forecast.png", caption="Prophet Forecast")
    elif selected_model == "SARIMA":
        st.image("s&p/sarima acf.pacf.png", caption="SARIMA ACF and PACF Plot")
    elif selected_model == "SVR":
        st.image("s&p/svr - results.png", caption="SVR Results")
    
    # Training and Validation Loss (ANN)
    st.header("Training and Validation Loss (ANN)")
    st.image("s&p/training and validation loss -ann.png", caption="Training and Validation Loss (ANN)")

elif selected_sector == "Energy":
    st.sidebar.title("Energy Sector Models")
    selected_model = st.sidebar.selectbox("Select Model", ["ARIMA", "ETS", "Hybrid ANN", "LSTM", "Prophet", "SARIMA", "SVR"])

    if selected_model == "ARIMA":
        st.image("energy/arima-acf-pacf.png", caption="ACF and PACF Plots")
    elif selected_model == "ETS":
        st.image("energy/ets-forecast.png", caption="ETS Forecast")
    elif selected_model == "Hybrid ANN":
        st.image("energy/hybrid-froecast.png", caption="Hybrid ANN Forecast")
    elif selected_model == "LSTM":
        st.image("energy/lstm-forecast.png", caption="LSTM Forecast")
    elif selected_model == "Prophet":
        st.image("energy/prophet-forecast.png", caption="Prophet Forecast")
    elif selected_model == "SARIMA":
        st.image("energy/sarima-acf-pacf.png", caption="SARIMA acf and pacf Forecast")
    elif selected_model == "SVR":
        st.image("energy/energy-svr-forecast.png", caption="SVR Forecast")

    # Training and Validation Loss (ANN)
    st.header("Training and Validation Loss (ANN)")
    st.image("energy/energy-ann-validation-loss.png", caption="Training and Validation Loss (ANN)")

elif selected_sector == "Environmental":
    st.sidebar.title("Environmental Sector Models")
    selected_model = st.sidebar.selectbox("Select Model", ["ARIMA", "ETS", "Hybrid ANN", "LSTM", "Prophet", "SARIMA", "SVR"])

    if selected_model == "ARIMA":
        st.image("env/env-arima-acf-pacf.png", caption="ARIMA ACF and PACF Plots")
    elif selected_model == "ETS":
        st.image("env/env-ets-forecast.png", caption="ETS Forecast")
    elif selected_model == "Hybrid ANN":
        st.image("env/env-hybrid-forecast.png", caption="Hybrid ANN Forecast")
    elif selected_model == "LSTM":
        st.image("env/env-lstm-forecast.png", caption="LSTM Forecast")
    elif selected_model == "Prophet":
        st.image("env/env-prophet-forecast.png", caption="Prophet Forecast")
    elif selected_model == "SARIMA":
        st.image("env/env-sarima-acf-pacf.png", caption="SARIMA ACF and PACF Plot")
    elif selected_model == "SVR":
        st.image("env/env-svr-forecast.png", caption="SVR Results")

    # Training and Validation Loss (ANN)
    st.header("Training and Validation Loss (ANN)")
    st.image("env/env-ann-validation-loss.png", caption="Training and Validation Loss (ANN)")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Developed by Your Name")
