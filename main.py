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
  from PIL import Image, ImageDraw

# Create a blank image 
img = Image.new('RGB', (200, 200), color=(255, 255, 255)) 

# Get a drawing context
draw = ImageDraw.Draw(img)

# Draw a rectangle 
draw.rectangle((50, 50, 150, 150), fill=(0,0,255)) 

# Draw some text 
draw.text((50,50), "Hello World", fill=(0,0,0))

# Save the image 
img.save('image.png')

print("Image generated!")
  
# Response function  
def respond(prompt):
  if "add" in prompt:
    if "hat"
      print("Here is your hat")
    from PIL import Image, ImageDraw

# Create a blank image 
img = Image.new('RGB', (200, 200), color=(255, 255, 255)) 

# Get a drawing context
draw = ImageDraw.Draw(img)

# Draw a rectangle 
draw.rectangle((50, 50, 150, 150), fill=(0,0,255)) 

# Draw some text 
draw.text((50,50), "Hello World", fill=(0,0,0))

# Save the image 
img.save('image.png')

print("Image generated!")
    
  if "view list" in prompt:  
    view_list ()

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
