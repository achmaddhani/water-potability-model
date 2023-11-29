'''
Achmad Dhani

Objective : Creating a page for classification prediction
'''
import streamlit as st
import pandas as pd
import joblib
from PIL import Image

def run():
    '''
    This function is for running the page for predictions
    '''
    st.title('Is Your Water Drinkable ?')
    model = joblib.load("best_model.pkl") # loading the model
    
    ph = st.number_input(label='Input ph:',min_value=0,max_value=14)
    hard= st.slider('Hardness', min_value=40, max_value=320)
    solid= st.slider('Total dissolved solids', min_value=320, max_value=60000)
    chlo= st.slider('Chloramines Level', min_value=0.0, max_value=13.0, step=0.1)
    sulf= st.slider('Sulfate', min_value=130, max_value=480)
    cond= st.slider('Conductivity', min_value=180, max_value=750)
    organ= st.slider('Total Organic Carbon', min_value=2.0, max_value=28.0, step=0.1)
    thm= st.slider('Trihalomethanes (THM)', min_value=0, max_value=120)
    turb= st.slider('Turbidity', min_value=0.0, max_value=7.0, step=0.1)

    # data for predictions
    data_pred={
        'ph': ph,
        'hardness':hard,
        'solids': solid,
        'chloramines':chlo,
        'sulfate': sulf,
        'conductivity': cond,
        'organic_carbon':organ,
        'trihalomethanes': thm,
        'turbidity': turb
    }

    # data for display
    data_show = {
    'Parameters': ['ph', 'hardness', 'solids', 'chloramines', 'sulfate', 'conductivity', 'organic_carbon', 'trihalomethanes', 'turbidity'],
    'Value': [ph, hard, solid, chlo, sulf, cond, organ, thm, turb]
    }

    st.write('The following table is the result of the data you have input : ')

    # display table
    display = pd.DataFrame(data_show)
    st.table(display)

    # df predictions
    df= pd.DataFrame([data_pred])

    # button
    if st.button(label='Predict'):
    
        y_pred_inf = model.predict(df)

        # printing result
        if y_pred_inf == 1:
            st.write('The water is DRINKABLE')
            
        else:
            st.write('The water is NOT DRINKABLE')

