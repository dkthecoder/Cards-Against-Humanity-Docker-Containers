from flask import Flask, render_template, url_for, redirect, flash
from requests.api import request
from forms import AddBlackCard, AddWhiteCard, LetsPlay
import requests

app = Flask(__name__)


app.config.update(DEBUG=True)
app.config['SECRET_KEY'] = '66ea3dab727dfa20322ca91c32854073'


#landing page
@app.route("/", methods=['POST', 'GET'])
def index():
    form = LetsPlay()
    if form.validate_on_submit():
        return redirect(url_for('play', given_word=form.word.data))
       
    return render_template("index.html", title="welcome", form=form)


#play
#TAKES A INPUT
@app.route('/play', defaults={'given_word': None}, methods=['POST', 'GET'])
@app.route('/play/<given_word>', methods=['POST', 'GET'])
def play(given_word):
    form = LetsPlay()
    num_of_bc = requests.get('http://blackcards:5001/get_bc_length')
    num_of_wc = requests.get('http://whitecards:5002/get_wc_length')
    #num_of_bc = blackcards.length()
    #num_of_wc = whitecards.length()

    if given_word == "feeling_lucky_punk":
        bc = requests.get('http://magicmaker:5003/random_number_generator/0/' + num_of_bc.text + '/1')
        wc = requests.get('http://magicmaker:5003/random_number_generator/0/' + num_of_bc.text + '/10')
        #bc = magicmaker.random_number_generator(0, num_of_bc, 1)
        #wc = magicmaker.random_number_generator(0, num_of_wc, 10)

        bc_return = requests.get('http://blackcards:5001/retrieve_bc/' + str(bc[0]))
        #bc_return = blackcards.retrieve_card(bc[0])
        wc_return = []

        counter = 0
        for i in range(5):
            temp = []
            for j in range(2):

                responce_return = requests.get('http://whitecards:5002/retrieve_wc/' + str(wc[counter]))
                temp.append(responce_return)
                #temp.append(whitecards.retrieve_card(wc[counter]))

                counter = counter + 1
            wc_return.append(temp)
        return render_template("play.html", title="play", form=form, blackcard=bc_return, whitecards=wc_return)

    elif form.validate_on_submit():
        bc = requests.get('http://magicmaker:5003/random_number_generator/0/' + num_of_bc.text + '/1/' + form.word.data.text)
        wc = requests.get('http://magicmaker:5003/random_number_generator/0/' + num_of_bc.text + '/10/' + form.word.data.text)
        #bc = magicmaker.rand_numbers_from_word(0, num_of_bc, 1, form.word.data)
        #wc = magicmaker.rand_numbers_from_word(0, num_of_wc, 10, form.word.data)

        bc_return = requests.get('http://blackcards:5001/retrieve_bc/' + str(bc[0]))
        #bc_return = blackcards.retrieve_card(bc[0])
        wc_return = []

        counter = 0
        for i in range(5):
            temp = []
            for j in range(2):

                responce_return = requests.get('http://whitecards:5002/retrieve_wc/' + str(wc[counter]))
                temp.append(responce_return)
                #temp.append(whitecards.retrieve_card(wc[counter]))
                

                counter = counter + 1
            wc_return.append(temp)
    return render_template("play.html", title="play", form=form, blackcard=bc_return, whitecards=wc_return)



#FUNCTION
#deletes black card
@app.route("/delete_bc/<index>", methods=['POST', 'GET'])
def delete_blackcard(index):
    requests.post('http://blackcards:5001/delete_bc/' + index.text)
    #blackcards.delete_card(index)

    flash ("Black card deleted", 'success')
    return redirect(url_for('black_cards'))


#FUNCTION
#deletes white card
@app.route("/delete_wc/<index>", methods=['POST', 'GET'])
def delete_whitecard(index):
    requests.post('http://whitecards:5002/delete_wc/' + index.text)
    #whitecards.delete_card(index)

    flash ("White card deleted", 'success')
    return redirect(url_for('white_cards'))


#Rules
@app.route("/rules", methods=['POST', 'GET'])
def rules():
    return render_template("rules.html", title="rules")


#add black card
@app.route("/black_cards", methods=['POST', 'GET'])
def black_cards():
    form = AddBlackCard()
    if form.validate_on_submit():

        requests.post('http://blackcards:5001/add_bc/' + form.text.data)
        #blackcards.add_card(form.card.data)

        flash(f'Black card added!', 'success')
        return redirect(url_for('black_cards'))
    
    cards = requests.get('http://blackcards:5001/read_all')
    #cards = blackcards.read_all()

    return render_template("black_cards.html", title="white cards", form=form, black_cards=cards)


#add white card
@app.route("/white_cards", methods=['POST', 'GET'])
def white_cards():
    form = AddWhiteCard()
    if form.validate_on_submit():

        requests.post('http://whitecards:5002/add_wc/' + form.text.data)
        #whitecards.add_card(form.card.data)

        flash(f'White card added!', 'success')
        return redirect(url_for('white_cards'))
        
    cards = requests.get('http://whitecards:5002/read_all')
    #cards = whitecards.read_all()

    return render_template("white_cards.html", title="white cards", form=form, white_cards=cards)


if __name__ == '__main__':
    app.run(port = 5000, host = '0.0.0.0')