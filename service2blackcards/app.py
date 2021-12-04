import pandas as pd
from flask import Flask, request, Response, json

app = Flask(__name__)
app.config.update(DEBUG=True)


print("importing black cards")
df = pd.read_csv (r'CAH_Black_Cards.csv', header=None)
print("importing black cards COMPLETE")


#Return TRUE length of dataframe
@app.route('/get_bc_length', methods=['GET'])
def get_bc_length():
    event_name =  str(len(df) - 1)
    return Response(event_name, mimetype='text/plain')


#read all
#NEED TO CHECK RETURN OF LIST
@app.route('/read_all', methods=['GET'])
def read_all():
    event_name = df.values.tolist()
    return Response(json.dumps(event_name), mimetype='application/json')


#retrieve a card
@app.route('/retrieve_bc', methods=['GET', 'POST'])
def retrieve_bc():
    card_id = request.card_id.decode('utf-8')
    event_name = df.loc[int(card_id)].values.tolist()
    return Response(json.dumps(event_name), mimetype='application/json')


#delete card
#COULD SET TO POST
@app.route('/delete_bc', methods=['GET', 'POST'])
def delete_bc():
    card_id = request.card_id.decode('utf-8')
    df.drop(df.index[(df[0] == int(card_id))], axis=0)


#add card
#COULD SET TO POST
@app.route('/add_bc', methods=['GET', 'POST'])
def add_bc(card):
    card = request.card.decode('utf-8')
    df.loc[len(df)] = str(card)


if __name__ == '__main__':
    app.run(port = 5001, host = '0.0.0.0')