import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Multi-Converter", page_icon="📐")

# Title with an icon
st.title("📐 Multi-Converter")

# Sidebar for selecting converter type
with st.sidebar:
    st.header("⚙️ Settings")
    converter_type = st.radio(
        "Select the converter type:",
        ("Meter Converter", "Temperature Converter"),
        index=0,
    )

# Meter Converter
if converter_type == "Meter Converter":
    st.subheader("📏 Meter Converter")
    meters = st.number_input("Enter length in meters:", min_value=0.0, value=1.0, step=0.1)

    # Conversion options for meters
    meter_option = st.radio(
        "Select the unit to convert to:",
        ("Centimeters", "Kilometers", "Millimeters"),
        index=0,
    )

    # Meter conversion logic
    if meter_option == "Centimeters":
        result = meters * 100
        st.success(f"✅ {meters} meters = {result} centimeters")
    elif meter_option == "Kilometers":
        result = meters / 1000
        st.success(f"✅ {meters} meters = {result} kilometers")
    elif meter_option == "Millimeters":
        result = meters * 1000
        st.success(f"✅ {meters} meters = {result} millimeters")

# Temperature Converter
elif converter_type == "Temperature Converter":
    st.subheader("🌡️ Temperature Converter")
    temperature = st.number_input("Enter temperature:", value=0.0, step=0.1)

    # Conversion options for temperature
    temp_option = st.radio(
        "Select the conversion type:",
        ("Celsius to Fahrenheit", "Fahrenheit to Celsius"),
        index=0,
    )

    # Temperature conversion logic
    if temp_option == "Celsius to Fahrenheit":
        result = (temperature * 9/5) + 32
        st.success(f"✅ {temperature}°C = {result}°F")
    elif temp_option == "Fahrenheit to Celsius":
        result = (temperature - 32) * 5/9
        st.success(f"✅ {temperature}°F = {result}°C")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")