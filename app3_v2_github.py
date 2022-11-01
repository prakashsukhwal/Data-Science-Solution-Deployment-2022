# Author: Prakash Sukhwal
# Aug 2021

import streamlit as st
# other libs
import numpy as np
import pandas as pd
import pickle
# import pyautogui # for reset button: pip install pyautogui

# load the model.pkl
# path = r'D:\work\courses\SI-Solution Implementation\SI\code\streamlit\app3\model.pkl'
# https://docs.streamlit.io/library/api-reference/performance/st.cache
@st.cache
with open('model.pkl', "rb") as f:
	model = pickle.load(f)

# Streamlit provides a caching mechanism that allows your app to stay performant 
# even when loading data from the web, manipulating large datasets, 
# or performing expensive computations. This is done with the @st.cache decorator.
@st.cache()
def prediction(int_rate, emp_length, annual_inc, delinq_2yrs, fico_range_high,revol_bal, open_acc):
	# Making predictions
	prediction = model.predict([[int_rate, emp_length, annual_inc, delinq_2yrs,fico_range_high,revol_bal, open_acc]])
	if prediction == 0:
		pred = 'Rejected'
	else:
		pred = 'Approved'
	return pred


# putting the app related codes in main()
def main():
	# -- Set page config
	apptitle = 'DSSI'
	st.set_page_config(page_title=apptitle, page_icon='random', 
		layout= 'wide', initial_sidebar_state="expanded")
	# random icons in the browser tab

	# give a title to your app
	st.title('Solution Implementation')

	#front end elements of the web page 
	# pick colors from: https://www.w3schools.com/tags/ref_colornames.asp
	html_temp = """ <div style ="background-color:AntiqueWhite;padding:15px"> 
       <h1 style ="color:black;text-align:center;">A loan application assessment app</h1> 
       </div> <br/>"""

    #display the front end aspect
	st.markdown(html_temp, unsafe_allow_html = True)

	# let us make infrastructure to provide inputs
	# we will add the inputs to side bar

	st.sidebar.info('Provide input using the panel')
	st.info('Click Assess button below')

	int_rate = st.sidebar.slider('int_rate', 5, 25, 10)
	st.write('input int_rate', int_rate)

	emp_length = st.sidebar.slider('emp_length', 0, 40, 5)
	st.write('input emp_length', emp_length)

	annual_inc = st.sidebar.slider('annual_inc in 1000s', 40, 100, 60)
	st.write('input annual_inc', annual_inc*1000)

	delinq_2yrs = st.sidebar.slider('delinq_2yrs', 0, 20, 0)
	st.write('input delinq_2yrs', delinq_2yrs)

	fico_range_high = st.sidebar.slider('fico_range_high', 630, 900, 700)
	st.write('input fico_range_high', fico_range_high)

	revol_bal = st.sidebar.slider('revol_bal', 1, 1000, 2)
	st.write('input revol_bal', revol_bal*1000)

	open_acc = st.sidebar.slider('open_acc', 1, 50, 2)
	st.write('input open_acc', open_acc)

	result =""
	# assessment button
	if st.button("Predict"):
		assessment = prediction(int_rate, emp_length, annual_inc*1000, delinq_2yrs, fico_range_high,revol_bal*1000, open_acc)
		st.success('**System assessment says:** {}'.format(assessment))

	# if st.button("Reset"):
	# 	pyautogui.hotkey("ctrl","F5")

	# st.balloons()
	st.success("App is working!!") # other tags include st.error, st.warning, st.help etc.

if __name__ == '__main__':
	main()
