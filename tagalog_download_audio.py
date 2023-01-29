# %%
import os
import re
import time
# twill for internetting
from twill import commands
from twill import browser
# pandas for anki and csvs
import pandas as pd
from ankipandas import Collection

# %%
csv_list = os.listdir('csv/')
# csv_list = csv_list[:2] #just use the first 2 for testing

df_list = []
for i,val in enumerate(csv_list):
    fname = os.path.join('~/git/anki-utils/csv/',val)
    # print(fname)
    df_list.append(pd.read_csv(fname,names=['english', 'tagalog']))

df = pd.concat(df_list)
df = df.reset_index()


# %%
# df_full = df
# df = df_full.iloc[:3]
for row in df.iterrows():
    tstring = row[1]['tagalog']
    sound_url = re.search("(?P<url>https?://[^\s]+.mp3)", tstring).group("url")
    # print(sound_url)
    fname = os.path.join('audio/',f'audio_card_{str(row[0]).zfill(4)}.mp3')
    # print(fname)
    commands.go(sound_url)
    with open(fname, 'wb') as f:
        print('writing to file')
        f.write(browser.dump)
        time.sleep(1)

