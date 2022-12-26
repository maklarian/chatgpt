import streamlit as st
import openai
import mysql.connector

conexion = mysql.connector.connect(user='futurodc_gpt3',password='frampton2510', host= '51.222.240.18',database='futurodc_gpt3', port='3306')

if conexion.is_connected():
            cursor=conexion.cursor()
            cursor.execute("Select database();")
            registro=cursor.fetchone()
            cursor.execute("SELECT * FROM futurodc_gpt3.mk")
            resultados=cursor.fetchall()
            for fila in resultados:
                llave = fila[1]
             
openai.api_key = llave

conversation = ""
user_name = "Miki"
bot_name = "AI"


st.header("Servicio de Consulta")

review  = st.text_area("Escribe tu pregunta...")
button = st.button("Generar respuesta")
#response = st.text_area(" ")
start_sequence = "\nAI:"
restart_sequence = "\nHuman: "
                                  
def generate_reply(review):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"You: hola\n\nAI: ¡Hola! ¿Cómo puedo ayudarte?.\n\nReview:{review}\n\nreplay:",
    #prompt="Este es un bot de respuesta de revisión de restaurantes.",
    #prompt=f"You: hola\n\nBot: ¡Hola! ¿Cómo puedo ayudarte?",
    temperature=0.7,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=[" Human:", " AI:"]
    )
    #st.write(response)
    return response.choices[0].text
    #print(response)


if button and review:
        with st.spinner("Generando respuesta..."):
            
            
            
            reply = generate_reply(review)
            
            #st.write(reply)
                         
            st.markdown(reply, unsafe_allow_html=False)    
            
            #conversation += f"\n{user_name}: {review}\n{bot_name}: {reply}"
            #st.write(conversation)
       
        
            
