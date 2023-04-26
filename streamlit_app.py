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
my_fruit_list = my_fruit_list.set_index('Fruit');
# Lets puta a pick list here so tey can pick the fruis they want to include
#streamlit.multiselect("Pick some fruits", list(my_fruit_list.index)) -- 1st version
#We want to filter the table data based on the fruits a customer will choose, so we'll pre-populate the list to set an example for the customer. 
#streamlit.multiselect("Pick some fruits", list(my_fruit_list.index),['Avocado','Strawberries']) ---2nd version
#streamlit.dataframe(my_fruit_list)

"""
We'll ask our app to put the list of selected fruits into a variable called fruits_selected. 
Then, we'll ask our app to use the fruits in our fruits_selected list to pull rows from the full data set (and assign that data to a variable called fruits_to_show).
Finally, we'll ask the app to use the data in fruits_to_show in the dataframe it displays on the page.  --- 3rd version
"""
fruits_selected = streamlit.multiselect("Pick some fruits", list(my_fruit_list.index),['Avocado','Strawberries']) 
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
#New section to show fruitvice api response
streamlit.header('Fruityvice Fruit Advice')
fruit_choice = streamlit.text_input('What fruit would you like information about?' ,'Kiwi')
streamlit.write('The user entered',fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
streamlit.text(fruityvice_response.json())# Just writes the data to screen as a test.
#Take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it in the screen as table
streamlit.dataframe(fruityvice_normalized)
import snowflake.connector





