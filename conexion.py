
from unittest import result
import mysql.connector
import streamlit as st
import os
#import openai


usuario  = st.text_input(label="Usuario...")
clave = st.text_input(label="Clave...")
button = st.button("Conectarse...")


if button:
  

        #conexion = mysql.connector.connect(user='gpt3',password='makc2510', host= '34.176.80.44',database='mygpt3', port='3306')
        conexion = mysql.connector.connect(user='futurodc_gpt3',password='frampton2510', host= '51.222.240.18',database='futurodc_gpt3', port='3306')
        #conexion = mysql.connector.connect(user='root',password='makc2510', host= '127.0.0.1',database='gpt3', port='3306')

        if conexion.is_connected():
            cursor=conexion.cursor()
            query=f'SELECT correo, clave FROM futurodc_gpt3.usuarios WHERE correo = "{usuario}"'
            cursor.execute(query)
            result=cursor.fetchone()
        if result and result[0] == usuario and result[1] == clave:
                st.write("usuario ok")
                os.system("streamlit run consulta.py")
        else:
                st.write("claves no validas")
    
        if conexion.is_connected():
           cursor.close()
           conexion.close()
        print("La conexion ha finalizado...")


