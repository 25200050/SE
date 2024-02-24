# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 02:58:51 2024

@author: isisa
"""
import random

# Base de datos de respuestas
respuestas_precargadas = [
    "Hola",
    "¿Cómo estás?",
    "¿Qué te gustaría ver?"
    
]

# Base de datos de preguntas
preguntas_nuevas = [
    "¿Cuál es tu genero de peliculas y series favorito?",
    "¿Cuál es tu pelicula favorita?",
    "¿Cuál es tu serie favorita?",
    "¿Quién es tu actor favorito?",
    "¿Te gustan las peliculas nacionales?",
    "¿Te gustan las peliculas internacionales?",
    
]

def chat():
    nombre = input("Hola, ¿cuál es tu nombre? ")
    print("Hola", nombre, "soy tu asistente dentro de esta app de peliculas y series ")
    print("Necesito saber mas de ti y tus gustos para saber que peliculas y series recomendarte, ¿contestarias las siguientes preguntas?")

    while True:
        respuesta = input()
        
        if respuesta.lower() in [r.lower() for r in respuestas_precargadas]:
            print(random.choice(respuestas_precargadas))
        else:
            # Si la respuesta no coincide, hacer una pregunta para agregar nuevo conocimiento
            print(random.choice(preguntas_nuevas))
            nueva_respuesta = input("Por favor ingresa una respuesta para agregar a la base de datos: ")
            respuestas_precargadas.append(nueva_respuesta)
            print("Gracias por tu respuesta. Ahora sé más sobre ti.")


chat()


