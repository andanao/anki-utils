# %%
import os
from twill import commands
from twill import browser

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

# for i in range(5761,5763):
for i in range(5761,5886):
    deck_num = i-5760
    print(f'\nStarting Deck {deck_num}')
    csv_url = f"https://www.tagalog.com/flashcards/export_anki.php?flipped=0&flash_card_set_id={i}&confirmed=1"
    deck_name = os.path.join(os.getcwd(),f'csv/top_2000_{str(deck_num).zfill(3)}.csv')
    print('going to url')
    commands.go(csv_url)
    with open(deck_name, 'wb') as f:
        print('writing to file')
        f.write(browser.dump)


