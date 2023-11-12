'''
Phase 1 Milestone 2

Nama : Achmad Dhani

Batch : HCK-009

Objective : Creating EDA page specifically to explain insights from EDA
'''

import streamlit as st
import pandas as pd
from PIL import Image

def run():
    '''
    Function for EDA page
    '''
    st.title('Exploration Data Analysis Section')

    df= pd.read_csv('water_potability.csv') # reading CSV

#============================= Display Data ===============================

    col1, col2 = st.columns(2)
    
    with col1.expander("View the top 10 entries of the original dataset"):
        st.table(df.head(10))
    
    with col2.expander("View the bottom 10 entries of the original dataset"):
        st.table(df.tail(10))


#============================= Correlation =====================================
    st.subheader('Correlation Matrix Between The Chemicals')
    col3, col4 = st.columns(2)

    # 1st image
    col3.write('Pearsons Correlation Matrix')
    image1 = Image.open('pearsons.png')
    col3.image(image1, caption='Figure 1 Pearsons Correlation Matrix of All Chemicals')

    # 2nd image
    col4.write('Spearman Correlation Matrix')
    image2 = Image.open('spearman.png')
    col4.image(image2, caption='Figure 2 Spearman Correlation Matrix of All Chemicals')

    # explaination
    with st.expander('Explanation'):
        st.caption(
            '''
            Based on both visualization, most of the variables do not have any relationship except for a few.
            
            Based on both visualization, most of the variables do not have any relationship except for a few.

            - `Hardness` has a very positive low value with `ph` in spearman but close to 0 in pearsons. This suggests there might be a very weak positive non
            linear relationship.
            - `Sulfate` with `Solids` and with `Sulfate` has a very low negative value both in spearman and pearsons. This suggests there might be a very weak
            negative linear relationship.
            '''
            )
        
#================================ ph ==========================================
    
    st.subheader('ph Values Distribution')
    image3 = Image.open('ph.png')
    st.image(image3, caption='Figure 3 ph values distribution histogram',  width=600)

    # explaination
    with st.expander('Explanation'):
        st.caption(
            '''
            - The water sample taken mostly has ph between `5-9`
            - The visualization also suggest a lot of data are in the range for drinkable water but doesn't mean that the water is drinkable.
            - This could mean most water samples that's taken could come contaminated water bodies.
            '''
            )

#================================ Missing Values ===============================
    st.subheader('Missing Values Visualizations')

    # missing plot
    st.write('Missing Values Bar Plot')
    image4 = Image.open('missing_values.png')
    st.image(image4, caption='Figure 4 Bar plot of missing values of each column')

    # displaying explaination
    with st.expander('Explanation'):
        st.caption(
            '''
            **From Data Loading**
            
            - There are otal missing values in the dataset: 1434
            
            - Columns with missing values: 
            
            `['ph', 'Sulfate', 'Trihalomethanes']`
            
            Number of missing values per column:
            >ph                 `491`
            >
            >Sulfate            `781`
            >
            >Trihalomethanes    `162`
            >
            >dtype: int64
            
            Missing data percentage (%):
            >ph                 `15`
            >
            >Sulfate            `24`
            >
            >Trihalomethanes     `5`
            '''
            )
        
    # missing matrix
    st.write('Missing Values Correlation Matrix')
    image5 = Image.open('missing_corr.png')
    st.image(image5, caption='Figure 5 Correlation matrix of the missing values')
    
        
    # display explaination
    with st.expander('Explanation'):
        st.caption(
            '''
            - Based on the visualization above, the missing values have no correlation and can be cosidered the missingness is `completly random`
            - The missing values being random could be due to the person that took the water sample did not have the equipment to measure the chemical level.
            '''
            )

#================================== PCA =============================
    
    st.subheader('Feature Importance')
    image6 = Image.open('PCA.png')
    st.image(image6, caption='Figure 6 Linechart of explained variance ratio with number of components')

    # displaying explaination
    with st.expander('Explanation'):
        st.caption(
            '''
            - Based on the visualization of PCA, there is a linear relationship between number of components and the EVR cummulative
            - This suggest, each feature is important and retains unique information of the dataset
            '''
            )