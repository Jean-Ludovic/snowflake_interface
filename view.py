##VIEW.PY
# Jean Ludovic 
import streamlit as st
import pandas as pd

def get_warehouses(conn):
    query = "SHOW WAREHOUSES"
    df = pd.read_sql(query, conn)
    return df['name'].tolist()
# Jean Ludovic 
def get_databases(conn):
    query = "SHOW DATABASES"
    df = pd.read_sql(query, conn)
    return df['name'].tolist()
# Jean Ludovic 
def get_schemas(conn, database):
    query = f"SHOW SCHEMAS IN DATABASE {database}"
    df = pd.read_sql(query, conn)
    return df['name'].tolist()

def get_tables(conn, database, schema):
    query = f"SHOW TABLES IN {database}.{schema}"
    df = pd.read_sql(query, conn)
    return df['name'].tolist()

def view_table_data(conn, database, schema, table):
    query = f"SELECT * FROM {database}.{schema}.{table} LIMIT 100"
    df = pd.read_sql(query, conn)
    st.dataframe(df)

def display_view():
    conn = st.session_state['connection']

    # Choisir  Warehouse
    warehouses = get_warehouses(conn)
    warehouse = st.selectbox("Select Warehouse", warehouses)
# Jean Ludovic 
    if warehouse:
        # Choisir  Database
        databases = get_databases(conn)
        database = st.selectbox("Select Database", databases)

        if database:
            # Choisir  Schema
            schemas = get_schemas(conn, database)
            schema = st.selectbox("Select Schema", schemas)

            if schema:
                # Choisir  Table
                tables = get_tables(conn, database, schema)
                table = st.selectbox("Select Table", tables)

                if table:
                    # Afficher les données de la table 
                    st.write(f"Displaying data for table: {table}")
                    view_table_data(conn, database, schema, table)
                    
                    
                    
# Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic 