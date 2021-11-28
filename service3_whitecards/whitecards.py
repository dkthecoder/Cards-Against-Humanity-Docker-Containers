import pandas as pd

print("importing white cards")
df = pd.read_csv (r'data\CAH - White Cards.csv', header=None)
print("importing white card COMPLETE")

#Return TRUE length of dataframe
def length():
    return len(df) - 1

#read all
def read_all():
    return df.values.tolist()

#retrieve a card
def retrieve_card(card_id):
    return df.loc[card_id].values.tolist()

#delete card
def delete_card(card_id):
    df.drop(df.index[(df[0] == card_id)], axis=0)

#add card
def add_card(card):
    df.loc[len(df)] = card
