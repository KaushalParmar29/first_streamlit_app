import streamlit

streamlit.title('My parents new healthy dinner')

streamlit.header('Breakfast Favorties')

streamlit.text('🥣Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach and Rocekt Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range egg')
streamlit.text('🥑 Avocada Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
