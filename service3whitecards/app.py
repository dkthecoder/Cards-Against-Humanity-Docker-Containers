import pandas as pd
from flask import Flask, request, Response

app = Flask(__name__)
app.config.update(DEBUG=True)


print("importing white cards")
df = pd.read_csv (r'data\CAH - White Cards.csv', header=None)
print("importing white card COMPLETE")


#Return TRUE length of dataframe
@app.route('/get_wc_length', methods=['GET'])
def get_wc_length():
    event_name =  len(df) - 1
    return Response(event_name, mimetype='text/plain')


#read all
#NEED TO CHECK RETURN OF LIST
@app.route('/read_all_wc', methods=['GET'])
def read_all_wc():
    event_name = df.values.tolist()
    return Response(event_name, mimetype='text/plain')


#retrieve a card
@app.route('/retrieve_wc/<card_id>', methods=['GET', 'POST'])
def retrieve_wc(card_id):
    event_name = df.loc[card_id].values.tolist()
    return Response(event_name, mimetype='text/plain')


#delete card
#COULD SET TO POST
@app.route('/delete_wc/<card_id>', methods=['GET', 'POST'])
def delete_bwc(card_id):
    df.drop(df.index[(df[0] == card_id)], axis=0)


#add card
#COULD SET TO POST
@app.route('/add_wc/<card>', methods=['GET', 'POST'])
def add_wc(card):
    df.loc[len(df)] = card


if __name__ == '__main__':
    app.run(port = 5000, host = '0.0.0.0')