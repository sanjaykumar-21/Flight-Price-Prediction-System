import streamlit as st
import pandas as pd
import pickle


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Flight Price Prediction",
    page_icon="✈️",
    layout="wide"
)


# ==========================================
# TITLE
# ==========================================

st.title("✈️ Flight Price Prediction")
st.write("Predict the price of your flight using the details below.")


# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv("flight_price_Dataset.csv")


# ==========================================
# LOAD MODEL
# ==========================================

try:

    with open("model_flight.pkl", "rb") as file:
        model = pickle.load(file)

except Exception as e:

    st.error("❌ Model could not be loaded.")
    st.exception(e)
    st.stop()


# ==========================================
# INPUT SECTION
# ==========================================

st.header("✈️ Enter Flight Details")

col1, col2 = st.columns(2)


# ==========================================
# SOURCE CITY
# ==========================================

with col1:

    source_city = st.selectbox(
        "Source City",
        sorted(df["source_city"].unique())
    )


# ==========================================
# DESTINATION CITY
# ==========================================

with col2:

    destination_city = st.selectbox(
        "Destination City",
        sorted(df["destination_city"].unique())
    )


# ==========================================
# SAME CITY VALIDATION
# ==========================================

if source_city == destination_city:

    st.warning(
        "⚠️ Source City and Destination City cannot be the same."
    )

    st.info(
        "Please select a different destination city."
    )


# ==========================================
# FIND FLIGHTS FOR SELECTED ROUTE
# ==========================================

route_df = df[
    (df["source_city"] == source_city) &
    (df["destination_city"] == destination_city)
]


# ==========================================
# FLIGHT DETAILS
# ==========================================

col1, col2 = st.columns(2)


with col1:

    airline = st.selectbox(
        "Airline",
        sorted(df["airline"].unique())
    )


    # --------------------------------------
    # Flight numbers based on route
    # --------------------------------------

    available_flights = sorted(
        route_df["flight"].unique()
    )


    if len(available_flights) > 0:

        flight = st.selectbox(
            "Flight Number",
            available_flights
        )

    else:

        flight = None

        st.warning(
            "⚠️ No flights available for this route."
        )


    departure_time = st.selectbox(
        "Departure Time",
        sorted(df["departure_time"].unique())
    )


    stops = st.selectbox(
        "Stops",
        sorted(df["stops"].unique())
    )


with col2:

    arrival_time = st.selectbox(
        "Arrival Time",
        sorted(df["arrival_time"].unique())
    )


    flight_class = st.selectbox(
        "Class",
        sorted(df["class"].unique())
    )


    duration = st.number_input(
        "Duration (Hours)",
        min_value=float(df["duration"].min()),
        max_value=float(df["duration"].max()),
        value=float(df["duration"].median()),
        step=0.1
    )


    days_left = st.number_input(
        "Days Left",
        min_value=int(df["days_left"].min()),
        max_value=int(df["days_left"].max()),
        value=int(df["days_left"].median()),
        step=1
    )


# ==========================================
# PREDICTION
# ==========================================

st.write("")


if st.button("🔮 Predict Flight Price", type="primary"):

    # --------------------------------------
    # Check same city
    # --------------------------------------

    if source_city == destination_city:

        st.error(
            "❌ Prediction cannot be made because "
            "Source City and Destination City are the same."
        )


    # --------------------------------------
    # Check flight availability
    # --------------------------------------

    elif flight is None:

        st.error(
            "❌ No flight is available for the selected route."
        )


    # --------------------------------------
    # Make prediction
    # --------------------------------------

    else:

        input_data = pd.DataFrame({

            "airline": [airline],

            "flight": [flight],

            "source_city": [source_city],

            "departure_time": [departure_time],

            "stops": [stops],

            "arrival_time": [arrival_time],

            "destination_city": [destination_city],

            "class": [flight_class],

            "duration": [duration],

            "days_left": [days_left]
        })


        try:

            prediction = model.predict(input_data)

            predicted_price = prediction[0]


            # ----------------------------------
            # Display Prediction
            # ----------------------------------

            st.success("✅ Prediction Successful!")


            st.metric(
                label="💰 Predicted Flight Price",
                value=f"₹ {predicted_price:,.2f}"
            )


            # ----------------------------------
            # Display Flight Details
            # ----------------------------------

            st.subheader("✈️ Flight Details")

            st.dataframe(
                input_data,
                use_container_width=True
            )


        except Exception as e:

            st.error("❌ Prediction failed.")

            st.exception(e)