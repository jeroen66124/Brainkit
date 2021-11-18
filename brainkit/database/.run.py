#!/usr/bin/env python3
# -.- coding: utf-8 -.-
# brainkit.py

import sys
import os
import subprocess
import time
from time import sleep
from termcolor import colored
from pygments import formatters, highlight, lexers
from pygments.util import ClassNotFound
from simple_term_menu import TerminalMenu


def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
slowprint(colored("""

   ██████╗ ██████╗  █████╗ ██╗███╗   ██╗██╗  ██╗██╗████████╗
   ██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║██║ ██╔╝██║╚══██╔══╝
   ██████╔╝██████╔╝███████║██║██╔██╗ ██║█████╔╝ ██║   ██║   
   ██╔══██╗██╔══██╗██╔══██║██║██║╚██╗██║██╔═██╗ ██║   ██║   
   ██████╔╝██║  ██║██║  ██║██║██║ ╚████║██║  ██╗██║   ██║   
   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝   ╚═╝                                             
""", "red"))

from simple_term_menu import TerminalMenu


def list_files(directory="."):
    return (file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file)))


def main():
    terminal_menu = TerminalMenu(list_files(), preview_command="batcat --color=always {}", preview_size=0.75)
    menu_entry_index = terminal_menu.show()


if __name__ == "__main__":
    main()
