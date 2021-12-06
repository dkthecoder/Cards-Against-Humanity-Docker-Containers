import pandas as pd
from flask import Flask, request, Response, jsonify
import json

app = Flask(__name__)
app.config.update(DEBUG=True)


print("importing white cards")
df = pd.read_csv (r'CAH_White_Cards.csv', header=None)
print("importing white card COMPLETE")


#Return TRUE length of dataframe
@app.route('/get_wc_length', methods=['GET', 'POST'])
def get_wc_length():
    event_name =  str(len(df) - 1)
    return Response(event_name, mimetype='text/plain')


#read all
#NEED TO CHECK RETURN OF LIST
@app.route('/read_all', methods=['GET', 'POST'])
def read_all():
    event_name = df.values.tolist()
    return jsonify(event_name)


#retrieve a card
@app.route('/retrieve_wc', methods=['GET', 'POST'])
def retrieve_wc():
    index = int(request.args.get('index'))
    event_name = str(df.loc[index].values.tolist())
    return Response(event_name, mimetype='text/plain')


#delete card
#COULD SET TO POST
@app.route('/delete_wc', methods=['GET', 'POST'])
def delete_wc():
    index = int(request.args.get('index'))
    df.drop(df.index[(df[0] == index)], axis=0)


#add card
#COULD SET TO POST
@app.route('/add_wc', methods=['GET', 'POST'])
def add_wc():
    card = str(request.args.get('card'))
    df.loc[len(df)] = str(card)
    return.response(200)


if __name__ == '__main__':
    app.run(port = 5002, host = '0.0.0.0')