import pyfiglet
from termcolor import colored
import random


def eid_al_fitr_wishes():
    colors = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan', 'white']
    ascii_art = pyfiglet.figlet_format("Eid Mubarak!", font="slant")
    print(colored(ascii_art, color=random.choice(colors)))


# Call the function to display Eid-al-Fitr wishes
eid_al_fitr_wishes()