
import mysql.connector
import streamlit as st
import os
#import openai


usuario  = st.text_input(label="Usuario...")
clave = st.text_input(label="Clave...")
button = st.button("Conectarse...")


if button:
  
        #conexion = mysql.connector.connect(user='gpt3',password='makc2510', host= '34.176.80.44',database='mygpt3')
        conexion = mysql.connector.connect(user='futurodc_gpt3',password='frampton2510', host= '51.222.240.18',database='futurodc_gpt3', port='3306')
        #conexion = mysql.connector.connect(user='root',password='makc2510', host= '127.0.0.1',database='gpt3', port='3306')
                
        
        if conexion.is_connected():
            cursor=conexion.cursor()
            cursor.execute("Select database();")
            registro=cursor.fetchone()
            #print("Conectado a la BD:", registro)
            cursor.execute("SELECT * FROM usuarios")
            resultados=cursor.fetchall()
        for fila in resultados:
            print(fila[0],fila[1])
        if usuario == fila[0] and clave == fila[1]:
                st.write("usuario ok")
                os.system("streamlit run consulta.py")
        else:
                st.write("claves no validas")

    
        if conexion.is_connected():
         conexion.close()
        print("La conexion ha finalizado...")


