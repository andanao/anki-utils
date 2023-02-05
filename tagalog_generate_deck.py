# %%
import os
from glob import glob
from ankipandas.ankidf import _columns
import pandas as pd
import re
from bs4 import BeautifulSoup as BS

import genanki
# %%
# Read out the downloaded csvs
csv_path = os.path.join(os.getcwd(), 'csv/')

df_list = []
for csv in glob(os.path.join(csv_path, '*.csv')):
    df_temp = pd.read_csv(csv, header = None, names = ['front', 'back'])
    df_list.append(df_temp)

df = pd.concat(df_list, ignore_index=True)


# %%
# add audios
df['audio'] = ''
for audio in glob(os.path.join(os.getcwd(), 'audio/*.mp3')):
    card_num = int(audio[-8:-4])
    df.iloc[card_num, 2] = audio


# %%
# cleanup html
# for i in range(10):
df['new_back'] = ''
for i in range(df.shape[0]):
    temp = re.sub(r'\[sound:.*\]','', df.back[i])

    bs = BS(temp)
    advertise = bs.findAll('span')[-1]
    if advertise.text == 'Flash cards by Tagalog.com':
        advertise.decompose()

    for tag in bs.recursiveChildGenerator():
        if hasattr(tag, 'attrs'):
            if hasattr(tag, 'style'):
                del tag['style']

    temp = bs.findAll('span')
    #this is really gross but whatever
    if temp:
        for i in temp:
            if i and len(i.text) < 4:
                i.name = 'u'
    # print(bs.prettify())
    df.new_back[i] = bs.prettify()
    # print(df.back[i] == df.new_back[i])

# %%
# Finally make the deck
