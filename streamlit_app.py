import streamlit
import pandas

streamlit.title('Mels Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text (' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard -Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build your Own Fruit Smoothie 🥝🍇' )
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Lets puta a pick list here so tey can pick the fruis they want to include
streamlit.multiselect("Pick some fruits", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)


