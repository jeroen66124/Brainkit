#!/usr/bin/env python3
# -.- coding: utf-8 -.-
# brainkit.py

import sys
import os
import subprocess
import time
from cursesmenu import *
from cursesmenu.items import *
from time import sleep
from termcolor import colored

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1/400)
slowprint(colored("""

   ██████╗ ██████╗  █████╗ ██╗███╗   ██╗██╗  ██╗██╗████████╗
   ██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║██║ ██╔╝██║╚══██╔══╝
   ██████╔╝██████╔╝███████║██║██╔██╗ ██║█████╔╝ ██║   ██║   
   ██╔══██╗██╔══██╗██╔══██║██║██║╚██╗██║██╔═██╗ ██║   ██║   
   ██████╔╝██║  ██║██║  ██║██║██║ ╚████║██║  ██╗██║   ██║   
   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝   ╚═╝                                             
                             
""", "red"))
time.sleep(1)

# Create the menu
menu = CursesMenu("Brainkit", "Select option")

# A SelectionMenu constructs a menu from a list of strings
selection_menu = SelectionMenu(["item1", "item2", "item3"])

# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

# Once we're done creating them, we just add the items to the menu
menu.append_item(submenu_item)
menu.append_item(submenu_item)
menu.append_item(submenu_item)
menu.append_item(submenu_item)

# Finally, we call show to show the menu and allow the user to interact
menu.show()
