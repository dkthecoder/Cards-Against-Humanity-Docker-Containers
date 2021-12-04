import pandas as pd
from flask import Flask, request, Response, json

app = Flask(__name__)
app.config.update(DEBUG=True)


print("importing white cards")
df_pre = pd.read_csv (r'CAH_White_Cards.csv', header=None)
df = df_pre.to_list()
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
    return Response(json.dumps(event_name), mimetype='application/json')


#retrieve a card
@app.route('/retrieve_wc', methods=['GET', 'POST'])
def retrieve_wc():
    card_id = request.data.decode('utf-8')
    event_name = df.loc[int(card_id)].values.tolist()
    return Response(json.dumps(event_name), mimetype='application/json')


#delete card
#COULD SET TO POST
@app.route('/delete_wc', methods=['GET', 'POST'])
def delete_wc():
    card_id = request.data.decode('utf-8')
    df.drop(df.index[(df[0] == int(card_id))], axis=0)


#add card
#COULD SET TO POST
@app.route('/add_wc', methods=['GET', 'POST'])
def add_wc():
    card = request.data.decode('utf-8')
    df.loc[len(df)] = str(card)


if __name__ == '__main__':
    app.run(port = 5002, host = '0.0.0.0')