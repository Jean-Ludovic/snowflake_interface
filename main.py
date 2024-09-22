import streamlit as st
from auth import connect_to_snowflake, disconnect
from view import display_view
from functions.create_database import create_database
from functions.create_schema import create_schema
from functions.create_table import create_table
from functions.create_warehouse import create_warehouse

#  les variables de session pour la connexion
if 'connection' not in st.session_state:
    st.session_state['connection'] = None
if 'user' not in st.session_state:
    st.session_state['user'] = None
if 'selected_option' not in st.session_state:
    st.session_state['selected_option'] = None


def main():
    # Si l'utilisateur n'est pas connecté, afficher le formulaire de connexion
    if st.session_state['connection'] is None:
        connect_to_snowflake()

    # Si l'utilisateur est connecté, afficher les options "View" et "Create"
    else:
        st.sidebar.text(f"Logged in as: {st.session_state['user']}")
        if st.sidebar.button("Disconnect"):
            disconnect()

        st.title("SNOWFLAKE DASHBOARD")

        if st.session_state['selected_option'] is None:
            st.write("Please choose an action:")
            col1, col2 = st.columns(2)

            with col1:
                if st.button("View"):
                    st.session_state['selected_option'] = "View"
            with col2:
                if st.button("Create"):
                    st.session_state['selected_option'] = "Create"

        # Si "View" est sélectionné, afficher les options de visualisation
        elif st.session_state['selected_option'] == "View":
            st.header("VIEW")
            display_view()

        # Si "Create" est sélectionné, afficher les options de création
        elif st.session_state['selected_option'] == "Create":
            st.subheader("CREATE")
            create_option = st.selectbox("Select resource to create:", ["Warehouse", "Database", "Schema", "Table"])

            if create_option == "Warehouse":
                create_warehouse()
            elif create_option == "Database":
                create_database()
            elif create_option == "Schema":
                create_schema()
            elif create_option == "Table":
                create_table()

        # Ajouter un bouton "Retour" pour revenir à l'écran des options
        if st.button("Back to Menu"):
            st.session_state['selected_option'] = None

if __name__ == "__main__":
    main()
# Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic 