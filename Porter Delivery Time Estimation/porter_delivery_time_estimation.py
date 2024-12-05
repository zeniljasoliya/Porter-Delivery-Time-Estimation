

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
def load_data():
    return pd.read_csv("dataset.csv")

df = load_data()

# Sidebar
st.sidebar.title("Filters")
selected_columns = st.sidebar.multiselect("Select Columns", df.columns)
filtered_df = df[selected_columns]

st.title("Porter Delivery Time Estimation")

# Display filtered data
st.subheader("Filtered Data")
st.write(filtered_df)

# Display statistics for numerical columns
if not filtered_df.empty:
    st.subheader("Statistics for Numerical Columns")
    st.write(filtered_df.describe())



# Data visualization
st.title("Data Visualization")

# Bar chart
st.subheader("Bar Chart")
bar_column = st.selectbox("Select column for bar chart", df.columns)
barplot_data = df[bar_column].value_counts()
st.bar_chart(barplot_data)

# Box plot
st.subheader("Box Plot")
box_column = st.selectbox("Select column for box plot", df.columns)
box_data = df[box_column]
plt.figure(figsize=(6, 4))
sns.boxplot(data=box_data)
st.pyplot(plt)

# Pie chart
st.subheader("Pie Chart")
pie_column = st.selectbox("Select column for pie chart", df.columns)
pie_data = df[pie_column].value_counts()
plt.figure(figsize=(6, 4))
plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')
st.pyplot(plt)




