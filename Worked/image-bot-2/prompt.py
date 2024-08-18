import pyautogui as pg
import time

# Time to switch to the input field where the prompts will be typed
time.sleep(2)

# Open the file containing the character names
with open('prompt.txt', 'r') as txt:
    characters = txt.readlines()

# Define the base prompts
prompts = [
    "/imagine [name] pfp",
    "/imagine [name] pfp, anime styled",
    "/imagine [name] pfp, portrait, looking center",
    "/imagine [name] pfp, Generate a captivating and highly detailed profile picture of [name]. The character should be posed dynamically, showcasing their most recognizable traits and abilities."
]

# Iterate over each character and generate the prompts
for character in characters:
    character = character.strip()  # Remove any leading/trailing whitespace
    for prompt in prompts:
        filled_prompt = prompt.replace("[name]", character)
        pg.write(filled_prompt)
        pg.press('Enter')
        time.sleep(100)
