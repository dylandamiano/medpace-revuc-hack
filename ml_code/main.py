import streamlit as st
import ml_trained

# Define a callback function to process the form data
def process_form_data(age, wc, sod, bp, sc):
    # Perform some processing with the input data
    # For example, you can calculate some metrics or make predictions
    result = ml_trained.predict(age, wc, sod, bp, sc)
    return result

# Create a form
with st.form("ckd_form"):
    # age
    age = st.number_input("Age", min_value=0, max_value=200, value=0, step=1)

    # wc
    wc = st.number_input("White Blood Cell Count", min_value=0, max_value=10000, value=0, step=1)

    # sod
    sod = st.number_input("Sodium", min_value=0, max_value=10000, value=0, step=1)

    # bp
    bp = st.number_input("Blood Pressure", min_value=0, max_value=10000, value=0, step=1)

    sc = st.number_input("Serum Ccreatinine", min_value=0, max_value=10000, value=0, step=1)

    # create a button to submit the form
    submit = st.form_submit_button("Submit")

# if the form is submitted, process the data and display the results
if submit:
    result = process_form_data(age, wc, sod, bp, sc)
    st.write(result)
else:
    st.write("Form not submitted")