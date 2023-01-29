# %%
import os
import re
import time
# twill for internetting
from twill import commands
from twill import browser
# pandas for csvs
import pandas as pd
#import eyed3 to check audio files
import eyed3

# %%
def url2file(url, filename):
    commands.go(url)
    with open(filename, 'wb') as f:
        print('writing to file')

        f.write(browser.dump)
        f.close()



# %%
csv_list = os.listdir('csv/')
# csv_list = csv_list[:2] #just use the first 2 for testing

df_list = []
for i,val in enumerate(csv_list):
    fname = os.path.join('~/git/anki-utils/csv/',val)
    # print(fname)
    df_list.append(pd.read_csv(fname,names=['english', 'tagalog']))

df = pd.concat(df_list)
df.reset_index()


# %%
# df_full = df
# df = df_full.iloc[:3]

i = 0
# for i in range(df.shape[0]):
while i < df.shape[0]:
    print(f'\n{i}')
    tstring = df.iloc[i, 1]
    try:
        sound_url = re.search("(?P<url>https?://[^\s]+.mp3)", tstring).group("url")
    except:
        sound_url = re.search("(?P<url>https?://[^\s]+.mp3)", tstring)
    fname = os.path.join('audio/',f'tagalog_audio_card_{str(i).zfill(4)}.mp3')
    url2file(sound_url,fname)
    if eyed3.load(fname):
        print('\tdownload success')
        i += 1
    else:
        print('\tdownload failed ... retrying')
        time.sleep(1)


   # i += 1
