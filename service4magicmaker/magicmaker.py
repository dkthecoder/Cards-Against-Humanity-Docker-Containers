import random
import hashlib

#generates random numebrs
#INPUT: start of range, end of range, number of numbers to generate (default seed)
def random_number_generator(start, end, num):
    random.seed()
    nums = []
    for i in range(num):
        nums.append(random.randint(start, end))
    return nums

#same as above but uses a word as a seed
#INPUT: start of range, end of range, number of numbers to generate, word to generate hash and seed
def rand_numbers_from_word(start, end, num, word):
    hashed = int(hashlib.sha256(word.encode('UTF-8')).hexdigest(), base=16)
    random.seed(hashed)
    nums = []
    for i in range(num):
        nums.append(random.randint(start, end))
    return nums