import random
import hashlib
from flask import Flask, request, Response

app = Flask(__name__)
app.config.update(DEBUG=True)


#generates random numebrs
#INPUT: start of range, end of range, number of numbers to generate (default seed)
@app.route('/random_number_generator', methods=['GET', 'POST'])
def random_number_generator():
    start = request.start.decode('utf-8')
    end = request.end.decode('utf-8')
    num = request.num.decode('utf-8')

    random.seed()
    nums = []
    for i in range(num):
        nums.append(random.randint(start, end))
    event_name = nums
    return Response(event_name, mimetype='text/plain')


#same as above but uses a word as a seed
#INPUT: start of range, end of range, number of numbers to generate, word to generate hash and seed
@app.route('/rand_numbers_from_word', methods=['GET', 'POST'])
def rand_numbers_from_word():
    start = request.start.decode('utf-8')
    end = request.end.decode('utf-8')
    num = request.num.decode('utf-8')
    word = request.word.decode('utf-8')

    hashed = int(hashlib.sha256(word.encode('UTF-8')).hexdigest(), base=16)
    random.seed(hashed)
    nums = []
    for i in range(num):
        nums.append(random.randint(start, end))
    event_name = nums
    return Response(event_name, mimetype='text/plain')


if __name__ == '__main__':
    app.run(port = 5003, host = '0.0.0.0')