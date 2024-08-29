import joblib
import streamlit as st
import pandas as pd
import sklearn

# Load the trained model
model = joblib.load('laptop_price_model')

# Create the Streamlit app
st.title('Laptop Price Predictor')

# Input features
ram = st.slider('RAM (GB)', 4, 64, 8)
weight = st.number_input('Weight (kg)', 0.5, 5.0, 1.37, 0.01)
touchscreen = st.checkbox('Touchscreen')
ips = st.checkbox('IPS Panel')
ppi = st.slider('PPI', 100, 400, 226, 1)
company = st.selectbox('Company', ('Acer', 'Apple', 'MSI', 'Razer'))
typename = st.selectbox('TypeName', ('Gaming', 'Notebook', 'Ultrabook', 'Workstation'))
opsys = st.selectbox('OpSys', ('Chrome OS', 'Linux', 'Mac OS X', 'No OS', 'Windows 10', 'Windows 7'))
hd = st.selectbox('HD', ('0', '4K Ultra HD', 'Full HD', 'Quad HD+'))
cpu = st.selectbox('Cpu brand', ('AMD Processor', 'Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'Nvidia', 'Other Intel Processor'))
gpu = st.selectbox('Gpu brand', ('AMD', 'Intel', 'Nvidia'))

# Create a dictionary with the input features
input_data = {
    'Ram': ram,
    'Weight': weight,
    'TouchScreen': int(touchscreen),
    'IPS Panel': int(ips),
    'PPI': ppi,
    'Company_Acer': 1 if company == 'Acer' else 0,
    'Company_Apple': 1 if company == 'Apple' else 0,
    'Company_MSI': 1 if company == 'MSI' else 0,
    'Company_Razer': 1 if company == 'Razer' else 0,
    'TypeName_Gaming': 1 if typename == 'Gaming' else 0,
    'TypeName_Notebook': 1 if typename == 'Notebook' else 0,
    'TypeName_Ultrabook': 1 if typename == 'Ultrabook' else 0,
    'TypeName_Workstation': 1 if typename == 'Workstation' else 0,
    'OpSys_Chrome OS': 1 if opsys == 'Chrome OS' else 0,
    'OpSys_Linux': 1 if opsys == 'Linux' else 0,
    'OpSys_Mac OS X': 1 if opsys == 'Mac OS X' else 0,
    'OpSys_No OS': 1 if opsys == 'No OS' else 0,
    'OpSys_Windows 10': 1 if opsys == 'Windows 10' else 0,
    'OpSys_Windows 7': 1 if opsys == 'Windows 7' else 0,
    'HD_0': 1 if hd == '0' else 0,
    'HD_4K Ultra HD': 1 if hd == '4K Ultra HD' else 0,
    'HD_Full HD': 1 if hd == 'Full HD' else 0,
    'HD_Quad HD+': 1 if hd == 'Quad HD+' else 0,
    'Cpu brand_AMD Processor': 1 if cpu == 'AMD Processor' else 0,
    'Cpu brand_Intel Core i3': 1 if cpu == 'Intel Core i3' else 0,
    'Cpu brand_Intel Core i5': 1 if cpu == 'Intel Core i5' else 0,
    'Cpu brand_Intel Core i7': 1 if cpu == 'Intel Core i7' else 0,
    'Cpu brand_Nvidia': 1 if cpu == 'Nvidia' else 0, 
    'Cpu brand_Other Intel Processor': 1 if cpu == 'Other Intel Processor' else 0,
    'Gpu brand_AMD': 1 if gpu == 'AMD' else 0,
    'Gpu brand_Intel': 1 if gpu == 'Intel' else 0,
    'Gpu brand_Nvidia': 1 if gpu == 'Nvidia' else 0
}

# Remove unnecessary features
input_data.pop('Company_Apple', None)
input_data.pop('Cpu brand_Nvidia', None)
input_data.pop('OpSys_Mac OS X', None)


# Create a DataFrame from the input data
input_df = pd.DataFrame([input_data])

# Make predictions
if st.button('Predict Price'):
    prediction = model.predict(input_df)
    st.success(f'The predicted price is: ₹{prediction[0]:.2f}')