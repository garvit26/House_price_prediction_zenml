import streamlit as st
import requests
import json

st.set_page_config(page_title="House Price Predictor", layout="centered")

st.title("House Price Prediction")
st.write("Enter house details below to get an estimated market price.")

# Create the layout with columns
col1, col2 = st.columns(2)

with col1:
    overall_qual = st.slider("Overall Quality (1-10)", 1, 10, 5)
    gr_liv_area = st.number_input("Living Area (sq ft)", min_value=500, max_value=5000, value=1500)
    year_built = st.number_input("Year Built", 1800, 2024, 2000)

with col2:
    garage_cars = st.selectbox("Garage Cars", [0, 1, 2, 3, 4], index=2)
    full_bath = st.selectbox("Full Bathrooms", [1, 2, 3, 4], index=2)
    tot_rooms = st.slider("Total Rooms Above Grade", 2, 15, 6)

# The Prediction Button
if st.button("Calculate Predicted Price"):
    # We must provide EVERY field the model schema requires
    data = {
        "dataframe_records": [
            {
                "Order": 1,
                "PID": 5286,
                "MS SubClass": 20,
                "Lot Frontage": 80.0,
                "Lot Area": 9600,
                "Overall Qual": overall_qual,  # User Input
                "Overall Cond": 7,
                "Year Built": year_built,      # User Input
                "Year Remod/Add": year_built,
                "Mas Vnr Area": 0.0,
                "BsmtFin SF 1": 700.0,
                "BsmtFin SF 2": 0.0,
                "Bsmt Unf SF": 150.0,
                "Total Bsmt SF": 850.0,
                "1st Flr SF": 856,
                "2nd Flr SF": 0,
                "Low Qual Fin SF": 0,
                "Gr Liv Area": float(gr_liv_area), # User Input
                "Bsmt Full Bath": 1.0,
                "Bsmt Half Bath": 0.0,
                "Full Bath": full_bath,        # User Input
                "Half Bath": 0,
                "Bedroom AbvGr": 3,
                "Kitchen AbvGr": 1,
                "TotRms AbvGrd": tot_rooms,     # User Input
                "Fireplaces": 1,
                "Garage Yr Blt": float(year_built),
                "Garage Cars": float(garage_cars), # User Input
                "Garage Area": 500.0,
                "Wood Deck SF": 0,
                "Open Porch SF": 0,
                "Enclosed Porch": 0,
                "3Ssn Porch": 0,
                "Screen Porch": 0,
                "Pool Area": 0,
                "Misc Val": 0,
                "Mo Sold": 5,
                "Yr Sold": 2010
            }
        ]
    }

    try:
        response = requests.post("http://127.0.0.1:8000/invocations", json=data)
        
        if response.status_code == 200:
            prediction = response.json()["predictions"][0]
            st.success(f"### Estimated Price: ${prediction:,.2f}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
            
    except Exception as e:
        st.error(f"Could not connect to model server. Is it running on Port 8000? Error: {e}")