import streamlit as st # streamlit is a library for building web applications
# unit_converter function takes a value, unit_from, unit_to as input and returns the converted value
def unit_converter(value, unit_from, unit_to):

    conversions = {
        "meter_kilometer": 0.001, # 1 meter = 0.001 kilometer
        "kilometer_meter": 1000, # 1 kilometer = 1000 meter
        "gram_kilogram" : 0.001, # 1 gram = 0.001 kilogram
        "kilogram_gram": 1000 , # 1 kilogram = 1000 gram       
    }

    key = f"{unit_from}_{unit_to}" # generate a key based on the input and output units

    if key in conversions: # check if the key is in the conversions dictionary
        conversion = conversions[key] 
        return value * conversion 
    else:# if the key is not in the conversions dictionary return an error message
       return "Invalid units"
           


st.title("Unit Converter") # set the title of the web application

value = st.number_input("Enter your value",min_value=0,step=1) # create a number input field for the user to enter the value to be converted

unit_from = st.selectbox("convert_from:",["meter","kilometer","gram","kilogram"]) # create a dropdown menu for the user to select the unit to be converted from

unit_to = st.selectbox("convert_to:",["meter","kilometer","gram","kilogram"]) # create a dropdown menu for the user to select the unit to be converted to

if st.button("convert"): # create a button for the user to convert the value
    result = unit_converter(value,unit_from,unit_to) # call the unit converter function and store the result in the result variable
    st.write(f"converted_value: {result}") # display the result to the user