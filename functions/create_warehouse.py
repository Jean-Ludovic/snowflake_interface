import streamlit as st
# Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic 
def create_warehouse():
    warehouse_name = st.text_input("Enter Warehouse Name")
    warehouse_size = st.selectbox("Select Warehouse Size", ["X-Small", "Small", "Medium", "Large"])

    if st.button("Create Warehouse"):
        query = f"CREATE WAREHOUSE {warehouse_name} WAREHOUSE_SIZE = '{warehouse_size}'"
        conn = st.session_state['connection']
        try:
            conn.cursor().execute(query)
            st.success(f"Warehouse {warehouse_name} created successfully.")
        except Exception as e:
            st.error(f"Error: {e}")
# Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic 