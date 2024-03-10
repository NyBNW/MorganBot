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
    if "hat"in prompt:
      print("Here is your hat")
    from PIL import Image, ImageDraw

from PIL import Image, ImageDraw

# Dictionary to store images 
images = {}

def generate_image():

  img = Image.new('RGB', (200,200))
  draw = ImageDraw.Draw(img)

  # Draw shape  
  draw.rectangle((50,50,100,100), fill='blue')

  # Prompt for tag
  tag = input("Enter tag: ")  

  # Save image with tag
  images[tag] = img

def show_images():

  for tag, img in images.items():

    # Render tag 
    print(f"Image - {tag}")

    # Save image
    img.save(f"images/{tag}.png")

while True:

  print("1. Generate Image")
  print("2. View Images")
  print("3. Exit")

  choice = input("> ")

  if choice == "1":
    generate_image()
  
  elif choice == "2":  
    show_images()

  elif choice == "3":
    break
    
  if "view list" in prompt:  
    view_list ()

  if "image" in prompt:
    # code  

  if "search" in prompt:
    import requests
from bs4 import BeautifulSoup

while True:

  prompt = input("Enter search query or press enter to exit: ")
  
  if prompt:

    # Query Google
    url = f"https://www.google.com/search?q={prompt}"
    resp = requests.get(url)

    # Extract first result
    soup = BeautifulSoup(resp.text, "html.parser")
    result = soup.select_one(".tF2Cxc")

    if result:
      print(f"Top result for {prompt}:")
      print(result.text)
    else:
      print("No results found")

  else:
    break

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
