# %%
import os
from twill import commands
from twill import browser
import time

# %%
# Turns out I have to log in first and can't just spam the website :(
with open('tagalog.pass', 'r') as f:
    password = f.read()
with open('username.pass', 'r') as f:
    username = f.read()

# %% Login

commands.go('https://www.tagalog.com/login.php')
commands.fv('loginform', 'username', username)
commands.fv('loginform', 'pass', password)
commands.submit()

# %% now actually download all the csvs

for deck_num in range(1,126):
    i = deck_num+5760
    print(f'\nStarting Deck {deck_num}')
    csv_url = f"https://www.tagalog.com/flashcards/export_anki.php?flipped=0&flash_card_set_id={i}&confirmed=1"
    deck_name = os.path.join(os.getcwd(),f'csv/top_2000_{str(deck_num).zfill(3)}.csv')
    print('going to url')
    commands.go(csv_url)
    with open(deck_name, 'wb') as f:
        print('writing to file')
        f.write(browser.dump)
    time.sleep(1) # don't make too many requests or you'll get stopped


