import duckdb
import pandas as pd
import streamlit as st
import io

csv = '''
beverage,price
orange juice, 2.5
expresso, 2
tea, 3
'''

beverages = pd.read_csv(io.StringIO(csv))

csv2 = '''
food_item,food_price
cookie, 2.5
chocolatine, 2
muffin, 3
'''

food_items = pd.read_csv(io.StringIO(csv2))

answer = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

solution = duckdb.sql(answer).df()


st.header("Enter your code")
query = st.text_area(label="Entrez votre code SQL", key="user_input")

if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    st.write("table: beverage")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected")
    st.dataframe(solution)

with tab3:
    st.write(answer)