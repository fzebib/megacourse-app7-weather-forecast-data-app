import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, 
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky") )

st.subheader(f"{option} for the next {days} days in {place}")

if place:
#data = get_data(place, days, option)
    try: 
        filtered_data = get_data(place, days)
        if filtered_data == '':
            st.write("Try again with a valid place name")
        # d, t = get_data(days)
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            # sky_conditions = [condition.lower() for condition in sky_conditions]
            # for condition in sky_conditions:
            #     st.image(f"images/{condition}.png", width=115)
            images = { "Clear": "images/clear.png", "Clouds": "images/clouds.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}
            image_condition = [images[condition] for condition in sky_conditions]
            st.image(image_condition, width=115)
    except KeyError:
        st.write("Invalid location name. Please try again.")

