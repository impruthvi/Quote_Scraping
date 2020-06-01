# http://quotes.toscrape.com

import requests
from time import sleep
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader

BASE_URL = "http://quotes.toscrape.com"

def read_quotes(filename):
    with open(filename,"r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)


def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print("Heae a quote:")
    print(quote["text"])
    print(quote["author"])
    guess =''

    while guess.lower() != quote["author"].lower() and remaining_guesses>0:
        guess = input(f"Who said this quote?Guesses remaining: {remaining_guesses}\n")
        if guess.lower() == quote["author"].lower():
            print("YOU GOT IT RIGHT")
            break
        remaining_guesses-=1

        if remaining_guesses ==3:
            res = requests.get(f"{BASE_URL}{quote['bio-link']}")
            soup = BeautifulSoup(res.text,"html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here's a hint: The author was born on {birth_date} {birth_place} ") 
        elif remaining_guesses ==2:
            print(f" Here's a hint: The author's first name starets with: {quote['author'][0]}")
        elif remaining_guesses == 1:
            last_name = quote['author'].split(" ")[1][0]
            print(f" Here's a hint: The author's last name starets with: {last_name}")
        else:
            print(f"sorry you ran out of gursses.The answer was {quote['author']}")

    again =''

    while again.lower() not in ('y','yes','n','no'):
        again = input("You want to play again?(y/n)?")
    if again.lower() in ('y','yes'):
        start_game(quotes)
    else:
        print("Thanks for playing")
quotes =  read_quotes("quotes.csv")

start_game(quotes)