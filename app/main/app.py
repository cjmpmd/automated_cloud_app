import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
import os
import plotly.graph_objs as go
from io import BytesIO
from PIL import Image


# Define a list of genders
genders = ["men","total","women"]

# # Function to generate SQL statement based on selected province
# def generate_sql_statement(province):
#     return f"SELECT * FROM public.population WHERE geography = '{province}'"

# # Function to execute SQL statement
# def execute_sql_statement(sql_statement):
    
#     # Retrieve database connection details from environment variables
#     username = os.environ.get('DB_USERNAME')
#     password = os.environ.get('DB_PASSWORD')
#     host = os.environ.get('DB_HOST')
#     port = os.environ.get('DB_PORT')
#     db = os.environ.get('DB')
        
#     # Create an engine to connect to your PostgreSQL database
#     engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{db}')
        
#     # Connect to the engine
#     conn = engine.connect()

#     # Execute SQL statement and fetch the result into a Pandas DataFrame
#     df = pd.read_sql_query(sql_statement, conn)
    
#     # Close connection
#     conn.close()

#     # Fetch and return the result
    # return df


# Main Streamlit app
def main():
    st.title("Age Data by gender")
    
    # Province selection dropdown
    gender = st.selectbox("Select a Gender:", genders)
    
    # Generate SQL statement based on selected province
    # sql_statement = generate_sql_statement(province)
    
    # # Execute SQL statement and get the result as a DataFrame
    # df = execute_sql_statement(sql_statement)
    df = pd.read_csv('../initialization/population_ages.csv')
    df.sort_values('order',inplace=True)
    df = df[df.gender==gender].copy()
    
    # Plot the data using Plotly
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df['age_range'], y=df['population'], name='Population'))
    fig.update_layout(title='Population Distribution by Age Range', xaxis_title='Age Range', yaxis_title='Population', height=300)
    
    # Display the Plotly line plot
    st.plotly_chart(fig)

    # Display image
    st.subheader("Gender:")
    image = Image.open(f'../app_images/{gender}.jpeg')
    st.image(image,width=300)

if __name__ == "__main__":
    main()