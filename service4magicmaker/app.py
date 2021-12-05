from os import startfile
import random
import hashlib
from flask import Flask, request, Response, jsonify

app = Flask(__name__)
app.config.update(DEBUG=True)


#generates random numebrs
#INPUT: start of range, end of range, number of numbers to generate (default seed)
@app.route('/random_number_generator', methods=['GET', 'POST'])
def random_number_generator():
    data = request.get_json()

    start = int(data["start"])
    end = int(data["end"])

    random.seed()
    event_name = random.randrange(start, end)
    return jsonify({"number": event_name})


#same as above but uses a word as a seed
#INPUT: start of range, end of range, number of numbers to generate, word to generate hash and seed
@app.route('/rand_numbers_from_word', methods=['GET', 'POST'])
def rand_numbers_from_word():
    data = request.get_json()
    start = int(data["start"])
    end = int(data["end"])
    word = data["word"].encode('UTF-8')

    hashed = int(hashlib.sha256(word).hexdigest(), base=16)
    random.seed(hashed)
    event_name = random.randrange(start, end)
    return jsonify({"number": event_name})


if __name__ == '__main__':
    app.run(port = 5003, host = '0.0.0.0')