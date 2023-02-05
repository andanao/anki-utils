# %%
import os
from glob import glob
from ankipandas.ankidf import _columns
import pandas as pd

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
    a = audio
    card_num = int(a[-8:-4])
    df.iloc[card_num, 2] = a


