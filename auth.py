# Jean Ludovic 
import streamlit as st
import snowflake.connector
# Jean Ludovic 
def connect_to_snowflake():
    st.sidebar.header("Snowflake Connection")
    
    # Inputs pour la connexion
    user = st.sidebar.text_input(label="Username",value="JEANLUDO",help="You can modify the username if it is not yours")
    password = st.sidebar.text_input("Password", type="password")
    account = st.sidebar.text_input("Account",value="hzjumte-kl23756",help="you can change the account id if it is not you")
   
    if st.sidebar.button("Connect"):
        try:
            # Connexion à Snowflake
            conn = snowflake.connector.connect(
                user=user,
                password=password,
                account=account,
            )
            # Si la connexion est réussie, on sauvegarde dans la session
            st.session_state['connection'] = conn
            st.session_state['user'] = user
            st.sidebar.success(f"Connected to Snowflake as {user}")
            
            # Relancer l'application automatiquement après la connexion
            st.rerun()  # Si disponible dans ta version

        except Exception as e:
            st.sidebar.error(f"Error: {e}")

def disconnect():
    # Réinitialiser la session à la déconnexion
    st.session_state['connection'] = None
    st.session_state['user'] = None
    st.session_state['selected_option'] = None
    # Forcer le rechargement automatique de la page pour revenir au login
    st.rerun()  # Recharger l'application
# Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic # Jean Ludovic 