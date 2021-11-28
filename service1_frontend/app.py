from flask import Flask, render_template, url_for, redirect, flash
from forms import AddBlackCard, AddWhiteCard, LetsPlay

import blackcards, whitecards, magicmaker



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
    num_of_bc = blackcards.length()
    num_of_wc = whitecards.length()

    if given_word == "feeling_lucky_punk":
        bc = magicmaker.random_number_generator(0, num_of_bc, 1)
        wc = magicmaker.random_number_generator(0, num_of_wc, 10)

        bc_return = blackcards.retrieve_card(bc[0])
        wc_return = []

        counter = 0
        for i in range(5):
            temp = []
            for j in range(2):
                temp.append(whitecards.retrieve_card(wc[counter]))
                counter = counter + 1
            wc_return.append(temp)
        return render_template("play.html", title="play", form=form, blackcard=bc_return, whitecards=wc_return)

    elif form.validate_on_submit():
            bc = magicmaker.rand_numbers_from_word(0, num_of_bc, 1, form.word.data)
            wc = magicmaker.rand_numbers_from_word(0, num_of_wc, 10, form.word.data)

            bc_return = blackcards.retrieve_card(bc[0])
            wc_return = []

            counter = 0
            for i in range(5):
                temp = []
                for j in range(2):
                    temp.append(whitecards.retrieve_card(wc[counter]))
                    counter = counter + 1
                wc_return.append(temp)
    return render_template("play.html", title="play", form=form, blackcard=bc_return, whitecards=wc_return)



#FUNCTION
#deletes black card
@app.route("/delete_bc/<index>", methods=['POST', 'GET'])
def delete_blackcard(index):
    blackcards.delete_card(index)
    flash ("Black card deleted", 'success')
    return redirect(url_for('black_cards'))


#FUNCTION
#deletes white card
@app.route("/delete_wc/<index>", methods=['POST', 'GET'])
def delete_whitecard(index):
    whitecards.delete_card(index)
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
        blackcards.add_card(form.card.data)
        flash(f'Black card added!', 'success')
        return redirect(url_for('black_cards'))
    
    cards = blackcards.read_all()

    print(black_cards)
    return render_template("black_cards.html", title="white cards", form=form, black_cards=cards)


#add white card
@app.route("/white_cards", methods=['POST', 'GET'])
def white_cards():
    form = AddWhiteCard()
    if form.validate_on_submit():
        whitecards.add_card(form.card.data)
        flash(f'White card added!', 'success')
        return redirect(url_for('white_cards'))

    cards = whitecards.read_all()
    print(cards)

    return render_template("white_cards.html", title="white cards", form=form, white_cards=cards)


if __name__ == '__main__':
    app.run()