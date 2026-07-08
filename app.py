import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Analysis Dashboard", layout="wide")

st.title("📊 Data Analysis Dashboard")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("Dataset Uploaded Successfully!")

    # -----------------------------------
    # Dataset Preview
    # -----------------------------------

    st.header("Dataset Preview")

    option = st.radio(
        "Choose Preview",
        ("Entire Dataset", "Top 5 Rows", "Bottom 5 Rows")
    )

    if option == "Entire Dataset":
        st.dataframe(df)

    elif option == "Top 5 Rows":
        st.dataframe(df.head())

    elif option == "Bottom 5 Rows":
        st.dataframe(df.tail())

    # -----------------------------------
    # Shape
    # -----------------------------------

    st.header("Dataset Shape")

    rows, cols = df.shape

    col1, col2 = st.columns(2)

    col1.metric("Rows", rows)
    col2.metric("Columns", cols)

    # -----------------------------------
    # Column Names
    # -----------------------------------

    st.header("Column Names")

    st.write(df.columns.tolist())

    # -----------------------------------
    # Describe
    # -----------------------------------

    st.header("Dataset Summary (Describe)")

    st.dataframe(df.describe())

    # -----------------------------------
    # Missing Values
    # -----------------------------------

    st.header("Missing Values")

    st.dataframe(df.isnull().sum())

    # -----------------------------------
    # Duplicate Values
    # -----------------------------------

    st.header("Duplicate Values")

    st.write("Duplicate Rows :", df.duplicated().sum())

    # -----------------------------------
    # Describe
    # -----------------------------------

    st.header("Statistical Summary")

    st.dataframe(df.describe(include="all"))

    # -----------------------------------
    # Dataset Information
    # -----------------------------------

    st.header("Dataset Information")

    info_df = pd.DataFrame({
        "Column": df.columns,
        "Describe": df.describe(),
        "Missing Values": df.isnull().sum().values,
        "Unique Values": df.nunique().values
    })

    st.dataframe(info_df)

    # -----------------------------------
    # Graph Section
    # -----------------------------------

    st.header("Visualization")

    numeric_columns = df.select_dtypes(include=np.number).columns.tolist()

    if len(numeric_columns) > 0:

        graph = st.selectbox(
            "Select Graph",
            ["Line Chart", "Bar Chart", "Histogram", "Box Plot"]
        )

        column = st.selectbox(
            "Select Numeric Column",
            numeric_columns
        )

        fig, ax = plt.subplots(figsize=(8,5))

        if graph == "Line Chart":
            ax.plot(df[column])

        elif graph == "Bar Chart":
            ax.bar(df.index, df[column])

        elif graph == "Histogram":
            ax.hist(df[column], bins=10)

        elif graph == "Box Plot":
            ax.boxplot(df[column])

        ax.set_title(f"{graph} - {column}")

        st.pyplot(fig)

    else:
        st.warning("No Numeric Columns Available!")

    