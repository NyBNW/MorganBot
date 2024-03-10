# Import libraries
import streamlit as st
from PIL import Image  
import requests
import random

# Bot details
BOT_NAME = 'Morgan'

# To-do list
todo_list = []

def add_to_list(item):
  todo_list.append(item)
  return f"Added {item} to your to-do list."

def view_list():
  return f"Your to-do list: {todo_list}"
  
# Image generation   
def generate_image():
  # code
  
# Web search  
def search(query):
  pass
  
# Response function  
def respond(prompt):

  if "add" in prompt:
    # code
    
  if "view list" in prompt:  
    # code  

  if "image" in prompt:
    # code  

  if "search" in prompt:
    # code

  return "I'm afraid I don't have enough context. How can I help?"

# UI
st.title(f'Talk to {BOT_NAME}') 

conversation = st.empty()
user_input = ''

while user_input != 'quit':

  user_input = st.text_input('You: ')

  conversation.write(f'You: {user_input}')

  response = respond(user_input)   

  conversation.write(f'{BOT_NAME}: {response}')
