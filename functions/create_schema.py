import streamlit as st
# Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic 
def create_schema():
    conn = st.session_state['connection']
    st.header("Create Schema")

    # Get existing databases
    cursor = conn.cursor()
    cursor.execute("SHOW DATABASES")
    databases = [row[1] for row in cursor.fetchall()]
    cursor.close()

    database_name = st.selectbox("Select Database", databases)
    schema_name = st.text_input("Schema Name")

    if st.button("Create Schema"):
        try:
            cursor = conn.cursor()
            cursor.execute(f"USE DATABASE {database_name}")
            cursor.execute(f"CREATE SCHEMA {schema_name}")
            st.success(f"Schema {schema_name} created successfully!")
        except Exception as e:
            st.error(f"Error: {e}")
        finally:
            cursor.close()
# Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic 