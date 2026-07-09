import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------
# PAGE CONFIGURATION
# ----------------------------------
st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

# ----------------------------------
# TITLE
# ----------------------------------
st.title("📊 Student Performance Dashboard")
st.markdown("Analyze your dataset using Streamlit, Pandas, NumPy and Matplotlib")
st.markdown("---")

# ----------------------------------
# FILE UPLOADER
# ----------------------------------
uploaded_file = st.file_uploader(
    "📂 Upload CSV File",
    type=["csv"]
)

# ----------------------------------
# DASHBOARD
# ----------------------------------
if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("✅ Dataset Uploaded Successfully")

    # ----------------------------------
    # OVERVIEW
    # ----------------------------------
    st.header("📌 Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    with col3:
        st.metric(
            "Missing Values",
            df.isnull().sum().sum()
        )

    with col4:
        st.metric(
            "Duplicate Rows",
            df.duplicated().sum()
        )

    st.markdown("---")

    # ----------------------------------
    # PREVIEW
    # ----------------------------------
    st.header("👀 Dataset Preview")

    tab1, tab2 = st.tabs(
        ["Top 5 Rows", "Bottom 5 Rows"]
    )

    with tab1:
        st.dataframe(df.head())

    with tab2:
        st.dataframe(df.tail())

    st.markdown("---")

    # ----------------------------------
    # COMPLETE DATASET
    # ----------------------------------
    st.header("📄 Complete Dataset")

    show_data = st.checkbox(
        "Show Complete Dataset"
    )

    if show_data:
        st.dataframe(
            df,
            use_container_width=True
        )

    st.markdown("---")

    # ----------------------------------
    # DATA TYPES
    # ----------------------------------
    st.header("📋 Data Types")

    datatype_df = pd.DataFrame({
        "Column Name": df.columns,
        "Data Type": df.dtypes.values
    })

    st.dataframe(
        datatype_df,
        use_container_width=True
    )

    st.markdown("---")

    # ----------------------------------
    # MISSING VALUES
    # ----------------------------------
    st.header("❓ Missing Values")

    missing_df = pd.DataFrame({
        "Column Name": df.columns,
        "Missing Values":
        df.isnull().sum().values
    })

    st.dataframe(
        missing_df,
        use_container_width=True
    )

    st.markdown("---")

    # ----------------------------------
    # UNIQUE VALUES
    # ----------------------------------
    st.header("🔢 Unique Values")

    unique_df = pd.DataFrame({
        "Column Name": df.columns,
        "Unique Values":
        df.nunique().values
    })

    st.dataframe(
        unique_df,
        use_container_width=True
    )

    st.markdown("---")

    # ----------------------------------
    # STATISTICAL SUMMARY
    # ----------------------------------
    st.header("📈 Statistical Summary")

    st.dataframe(
        df.describe(),
        use_container_width=True
    )

    st.markdown("---")

    # ----------------------------------
    # CORRELATION MATRIX
    # ----------------------------------
    st.header("📉 Correlation Matrix")

    numeric_df = df.select_dtypes(
        include=np.number
    )

    if not numeric_df.empty:

        corr = numeric_df.corr()

        fig, ax = plt.subplots(
            figsize=(10, 6)
        )

        cax = ax.imshow(
            corr,
            aspect="auto"
        )

        plt.colorbar(cax)

        ax.set_xticks(
            range(len(corr.columns))
        )

        ax.set_yticks(
            range(len(corr.columns))
        )

        ax.set_xticklabels(
            corr.columns,
            rotation=90
        )

        ax.set_yticklabels(
            corr.columns
        )

        st.pyplot(fig)

    st.markdown("---")

    # ----------------------------------
    # VISUALIZATION
    # ----------------------------------
    st.header("📊 Data Visualization")

    numeric_columns = df.select_dtypes(
        include=np.number
    ).columns.tolist()

    chart_type = st.selectbox(
        "Select Chart Type",
        [
            "Histogram",
            "Line Chart",
            "Bar Chart",
            "Box Plot",
            "Area Chart",
            "Scatter Plot",
            "Pie Chart"
        ]
    )

    if chart_type == "Scatter Plot":

        col1, col2 = st.columns(2)

        with col1:
            x_col = st.selectbox(
                "Select X Axis",
                numeric_columns
            )

        with col2:
            y_col = st.selectbox(
                "Select Y Axis",
                numeric_columns
            )

    else:

        selected_column = st.selectbox(
            "Select Column",
            numeric_columns
        )

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    # Histogram
    if chart_type == "Histogram":

        ax.hist(
            df[selected_column],
            bins=15
        )

        ax.set_title(
            f"Histogram - {selected_column}"
        )

    # Line Chart
    elif chart_type == "Line Chart":

        ax.plot(
            df[selected_column]
        )

        ax.set_title(
            f"Line Chart - {selected_column}"
        )

    # Bar Chart
    elif chart_type == "Bar Chart":

        ax.bar(
            range(len(df[selected_column])),
            df[selected_column]
        )

        ax.set_title(
            f"Bar Chart - {selected_column}"
        )

    # Box Plot
    elif chart_type == "Box Plot":

        ax.boxplot(
            df[selected_column]
        )

        ax.set_title(
            f"Box Plot - {selected_column}"
        )

    # Area Chart
    elif chart_type == "Area Chart":

        ax.fill_between(
            range(len(df[selected_column])),
            df[selected_column]
        )

        ax.set_title(
            f"Area Chart - {selected_column}"
        )

    # Scatter Plot
    elif chart_type == "Scatter Plot":

        ax.scatter(
            df[x_col],
            df[y_col]
        )

        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)

        ax.set_title(
            f"{x_col} vs {y_col}"
        )

    # Pie Chart
    elif chart_type == "Pie Chart":

        pie_data = (
            df[selected_column]
            .value_counts()
            .head(5)
        )

        ax.pie(
            pie_data,
            labels=pie_data.index,
            autopct="%1.1f%%"
        )

        ax.set_title(
            f"Pie Chart - {selected_column}"
        )

    st.pyplot(fig)

    st.markdown("---")

 