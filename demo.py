import streamlit as st

st.image(
    "https://datascientest.com/wp-content/uploads/2020/10/logo-text-right.png.webp"
)

st.header("Développer et déployer une application de Machine learning en **Streamlit**")


st.info("Webinar du 04/05/2021")

st.markdown("---")

st.markdown(
    """
    **Objectifs 🎯** 

    * Se familiariser avec Streamlit
    * Découvrir les différents types de widgets
    * Créér une démo d'application de Machine Learning
    * Déployer cette application 🚀

"""
)

first_name = st.sidebar.text_input("Prénom")
last_name = st.sidebar.text_input("Nom")
job = st.sidebar.selectbox(
    "Profession",
    options=("Data Scientist", "Data Engineer", "Développeur", "Autre"),
)

experience = st.sidebar.slider(
    "Années d'expériences", min_value=0, max_value=10, value=2, step=1
)

interests = st.sidebar.multiselect(
    "Intérêts",
    options=["technologie", "IA", "développement", "python", "statistiques", "R"],
    default=["python", "IA"],
)
