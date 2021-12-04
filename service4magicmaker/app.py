import random
import hashlib
from flask import Flask, request, Response, jsonify

app = Flask(__name__)
app.config.update(DEBUG=True)


#generates random numebrs
#INPUT: start of range, end of range, number of numbers to generate (default seed)
@app.route('/random_number_generator', methods=['GET', 'POST'])
def random_number_generator():
    data_json = request.get_json()
    data = data_json.json()

    random.seed()
    nums = []
    for i in range(data["num"]):
        nums.append(random.randint(data["start"], data["end"]))
    return jsonify(nums)



#same as above but uses a word as a seed
#INPUT: start of range, end of range, number of numbers to generate, word to generate hash and seed
@app.route('/rand_numbers_from_word', methods=['GET', 'POST'])
def rand_numbers_from_word():
    data_json = request.get_json()
    data = data_json.json()

    hashed = int(hashlib.sha256(data["word"].encode('UTF-8')).hexdigest(), base=16)
    random.seed(hashed)
    nums = []
    for i in range(data["num"]):
        nums.append(random.randint(data["start"], data["end"]))
    return jsonify(nums)


if __name__ == '__main__':
    app.run(port = 5003, host = '0.0.0.0')