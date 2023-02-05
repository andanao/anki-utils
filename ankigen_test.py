# %%
from ankipandas import Collection

col = Collection()



# %%
notes = col.notes
cards = col.cards

# %%

t_rec = notes[notes.nmodel == 'Recognition']

t_sub = t_rec[:10]
t_list = t_rec.nflds.to_list()[0:10]


a = t_sub[0:1].add_tag('pytest')

# %%
col.notes.update(a)
col.write(modify = True)
