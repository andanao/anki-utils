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

# %%

# for i in range(5761,5886):
for i in range(5761,5763):
    deck_num = i-5760
    csv_url = f"https://www.tagalog.com/flashcards/export_anki.php?flipped=0&flash_card_set_id={i}&confirmed=1"
    deck_name = os.path.join(os.getcwd(),f'csv/top_2000_dump_{str(deck_num).zfill(3)}.csv')
    deck_dump = os.path.join(os.getcwd(),f'csv/top_2000_show_{str(deck_num).zfill(3)}.csv')
    commands.go(csv_url)
    with open(deck_name, 'w+', encoding="UTF-8") as f:
        f.write(commands.show())
    with open(deck_name, 'w+', encoding="UTF-8") as f:
        f.write(commands.show())


