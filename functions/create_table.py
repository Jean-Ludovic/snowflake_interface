import streamlit as st
# Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic 
def create_table():
    conn = st.session_state['connection']
    st.header("Create Table")

    # Get existing databases
    cursor = conn.cursor()
    cursor.execute("SHOW DATABASES")
    databases = [row[1] for row in cursor.fetchall()]

    # Get schemas for the selected database
    selected_database = st.selectbox("Select Database", databases)
    if selected_database:
        cursor.execute(f"SHOW SCHEMAS IN DATABASE {selected_database}")
        schemas = [row[1] for row in cursor.fetchall()]

        schema_name = st.selectbox("Select Schema", schemas)
        table_name = st.text_input("Table Name")
        columns = st.text_area("Columns (e.g., id INT, name STRING)")

        if st.button("Create Table"):
            try:
                cursor.execute(f"USE DATABASE {selected_database}")
                cursor.execute(f"USE SCHEMA {schema_name}")
                cursor.execute(f"CREATE TABLE {table_name} ({columns})")
                st.success(f"Table {table_name} created successfully!")
            except Exception as e:
                st.error(f"Error: {e}")
            finally:
                cursor.close()
# Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic 