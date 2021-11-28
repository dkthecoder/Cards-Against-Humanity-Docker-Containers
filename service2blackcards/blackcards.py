import pandas as pd
from flask import Flask, request, Response

app = Flask(__name__)
app.config.update(DEBUG=True)


print("importing black cards")
df = pd.read_csv (r'data\CAH - Black Cards.csv', header=None)
print("importing black cards COMPLETE")

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


if __name__ == '__main__':
    app.run(port = 5000, host = '0.0.0.0')