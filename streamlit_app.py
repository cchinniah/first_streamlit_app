import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError

streamlit.title('Mels Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text (' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard -Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build your Own Fruit Smoothie 🥝🍇' )
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit');
# Lets puta a pick list here so they can pick the fruis they want to include
#streamlit.multiselect("Pick some fruits", list(my_fruit_list.index)) -- 1st version
#We want to filter the table data based on the fruits a customer will choose, so we'll pre-populate the list to set an example for the customer. 
#streamlit.multiselect("Pick some fruits", list(my_fruit_list.index),['Avocado','Strawberries']) ---2nd version
#streamlit.dataframe(my_fruit_list)


#We'll ask our app to put the list of selected fruits into a variable called fruits_selected. 
#Then, we'll ask our app to use the fruits in our fruits_selected list to pull rows from the full data set (and assign that data to a variable called fruits_to_show).
#Finally, we'll ask the app to use the data in fruits_to_show in the dataframe it displays on the page.  --- 3rd version

fruits_selected = streamlit.multiselect("Pick some fruits", list(my_fruit_list.index),['Avocado','Strawberries']) 
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#New section to show fruitvice api response
streamlit.header('Fruityvice Fruit Advice')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select the fruit to get information")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    #Take the json version of the response and normalize it
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    #output it in the screen as table
    streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()
  
#dont run anything passed this point.

streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#streamlit.text("Hello from snowflake:")
#my_cur.execute("select current_user(),current_account(),current_region()")
my_cur.execute("select * from fruit_load_list")
#my_data_row = my_cur.fetchone()
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

#add a second fruit
adding_my_fruit = streamlit.text_input('What fruit would you like to add?' ,'Jackfruit')
streamlit.write('Thanks for adding ' + adding_my_fruit)
my_cur.execute("Insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from Streamlit')")




