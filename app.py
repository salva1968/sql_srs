import duckdb
import pandas as pd
import streamlit as st

st.write("""
# SQL SRS
Spaced Repetition system SQL practice
""")

option = st.selectbox(
    "What would you like to review",
    ("Join", "GroupBy", "Windows Functions"),
    index=None,
    placeholder="Select a theme...",
)

st.write("You selected:", option)

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    sql_query = st.text_area(label="Entrez votre code SQL")
    if sql_query.strip():
        try:
            result = duckdb.query(sql_query).df()
            st.write(f"Vous avez entré la requête suivante : `{sql_query}`")
            st.dataframe(result)
        except Exception as e:
            st.error(f"Erreur lors de l'exécution de la requête : {e}")
    else:
        st.info("Veuillez entrer une requête SQL.")

with tab2:
    st.header("A dog")

with tab3:
    st.header("A cat")