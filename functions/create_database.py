import streamlit as st
from view import get_warehouses
# Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic 
def create_database():
    conn = st.session_state['connection']
    st.header("Create Database")

    # Get existing warehouses using the imported function
    try:
        warehouses = get_warehouses(conn)
        
        if not warehouses:
            st.error("No warehouses found. Please create a warehouse first.")
            return

        warehouse_name = st.selectbox("Select Warehouse", warehouses)
        database_name = st.text_input("Database Name")

        if st.button("Create Database"):
            if not database_name:
                st.error("Please enter a database name.")
                return
            
            try:
                cursor = conn.cursor()
                cursor.execute(f"USE WAREHOUSE {warehouse_name}")
                cursor.execute(f"CREATE DATABASE {database_name}")
                st.success(f"Database {database_name} created successfully!")
            except Exception as e:
                st.error(f"Error: {e}")
            finally:
                cursor.close()
    except Exception as e:
        st.error(f"Error: {e}")
# Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic 