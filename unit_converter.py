import streamlit as st

# 🌙 Dark Mode Toggle Button
dark_mode = st.checkbox("🌙 Enable Dark Mode")

# 🎨 Dark & Light Theme CSS
if dark_mode:
    theme_css = """
        <style>
            body { background-color: #121212; color: white; }
            .stApp { background-color: #121212; }
            .stButton>button {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 8px;
            }
        </style>
    """
else:
    theme_css = """
        <style>
            body { background-color: white; color: black; }
            .stApp { background-color: white; }
            .stButton>button {
                background-color: #008CBA;
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 8px;
            }
        </style>
    """

st.markdown(theme_css, unsafe_allow_html=True)


st.title("🔥Unit Converter")
# Category Selection
st.write("Select a conversion category and enter a value to convert.")
category = st.selectbox("Select a Category" , ["📏Length", "⚖️Weight", "⏳Time", "🌡️Temperature"])
st.write(f"Your Selected : {category}")

 # Function for conversions
def convert(value, conversion_type):
    if conversion_type == "Kilometers to Meters":
        return value * 1000
    elif conversion_type == "Meters to Kilometers":
        return value / 1000
    elif conversion_type == "Meters to Centimeters":
        return value * 100
    elif conversion_type == "Centimeters to Meters": 
        return value / 100
    elif conversion_type == "Miles to Kilometers":
        return value * 1.60934  
    elif conversion_type == "Kilometers to Miles":
        return value / 1.60934
    elif conversion_type == "Inches to Centimeters":
        return value * 2.54  
    elif conversion_type == "Centimeters to Inches":
        return value / 2.54
    elif conversion_type == "Kilograms to Grams":
        return value * 1000
    elif conversion_type == "Grams to Kilograms":
        return value / 1000
    elif conversion_type == "Hours to Minutes":
          return value * 60
    elif conversion_type == "Minutes to Seconds":
        return value * 60
    elif  conversion_type == "Seconds to Minutes":
        return value / 60
    elif  conversion_type == "Minutes to Hours":
        return value / 60
    elif conversion_type == "Celsius to Fahrenheit":
        return (value * 9/5) + 32
    elif conversion_type == "Fahrenheit to Celsius":
        return (value - 32) * 5/9
    return None
# Formatting Function
def format_result(value):
    if abs(value) >= 1:
        return f"{value:.2f}"
    else:
        return f"{value:.5f}"

    # Conversion options based on category
if category == "📏Length":
     conversion = st.selectbox("Convert:",["Kilometers to Meters", "Meters to Kilometers", "Meters to Centimeters", "Centimeters to Meters","Miles to Kilometers","Kilometers to Miles","Inches to Centimeters","Centimeters to Inches"])
elif category == "⚖️Weight":
      conversion = st.selectbox("Convert:", ["Kilograms to Grams", "Grams to Kilograms"])
elif category == "⏳Time":
      conversion = st.selectbox("Convert:", ["Hours to Minutes", "Minutes to Seconds"])
elif category == "🌡️Temperature":
      conversion = st.selectbox("Convert:", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
     
# User Input
if conversion:
    value = st.number_input(f"Enter value in {conversion.split(' to ')[0]}:", min_value=0.0, format="%.5f")
if st.button("convert"):
    result = convert(value, conversion)
    
    if result is not None:
        formatted_value = format_result(value)
        formatted_result = format_result(result)
        st.success(f"{formatted_value} {conversion.split(' to ')[0]} = {formatted_result} {conversion.split(' to ')[1]}")
    else:
       st.error("Invalid conversion type.")
    st.balloons()
   













