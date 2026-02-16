import time
import argparse
from datetime import datetime
from colorama import Fore, Back, Style, init

#Initialize(autoreset=True)
init


def get_time_color(hour):
        """Return a color based on the time of date."""
    if 5 <= hour < 12:
      return Fore.YELLOW #Morning
    elif 12 <= hour < 17:
      return Fore.CYAN #Afternoon
    elif 17 <= hour < 
    

def main

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Display a digital clock with dynamic colors.")
    parser