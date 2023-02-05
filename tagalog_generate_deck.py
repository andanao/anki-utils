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
print(len(df.new_back.unique()))
for i in range(df.shape[0]):
    temp = df.back[i]
    temp = re.sub(r'\[sound:.*\]','', temp)

    bs = BS(temp)
    advertise = bs.findAll('span')[-1]
    if advertise.text == 'Flash cards by Tagalog.com':
        advertise.decompose()

    for tag in bs.recursiveChildGenerator():
        if hasattr(tag, 'attrs'):
            if hasattr(tag, 'style'):
                del tag['style']

    # temp = bs.findAll('span')
    #this is really gross but whatever
    # if temp:
        # for i in temp:
            # if i and len(i.text) < 4:
                # i.name = 'u'
    # print(bs.prettify())
    df.new_back[i] = bs.prettify()
    # print(df.back[i] == df.new_back[i])

print(len(df.new_back.unique()))
# %%
# Finally make the deck
# random.randrange(1 << 30, 1 << 31) # to generate a random number
deck_id = 1894819615 #hardcoded as reccomended in the docs

my_model = genanki.Model(
  1511670166, #hardcoded as reccomended in the docs
  'Test Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
    {'name': 'Audio'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}<br>[sound:{{Audio}}]',
    },
  ])


my_deck = genanki.Deck(deck_id = deck_id,
                      name = 'Tagalog python Test',
                      description = 'tests autogeneration of decks')


# %%
# Add entries

for i in range(df.shape[0]):
    card = genanki.Note(
        model = my_model,
        fields = [
            df.front[i],
            df.new_back[i],
            df.audio[i],
        ]
    )
    my_deck.add_note(card)

genanki.Package(my_deck).write_to_file('tagalog_test.apkg')
