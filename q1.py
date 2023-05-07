from hashlib import sha512
import multiprocessing as mp
from multiprocessing import Pool
import time

WORDS = ['extra-large', 'invincible', 'furtive', 'stare', 'ruddy', 'adaptable', 'daily', 'letters', 'houses', 'grate', 'fog', 'stupendous']

def hash(word: str):
    hash_object = sha512()
    for _ in range(100):
        time.sleep(.01)
        byte_data = word.encode('utf-8')
        hash_object.update(byte_data)
        word = hash_object.hexdigest()
    return word

def main():

    #------------------------------------------ YOUR CODE GOES HERE ------------------------------------------

    # TODO: replace this code with your multiprocessed version
    start_time = time.time()
    with Pool(5) as p:
        #print(p.map(hash, WORDS))
        for e in p.map(hash, WORDS):
            print(e)
    end_time = time.time()
    print("time it takes for these tasks to run =", end_time - start_time)	



    #for word in WORDS:
    #    print(hash(word))
    #---------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()