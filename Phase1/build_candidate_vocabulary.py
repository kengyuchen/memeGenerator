from MemeTextGenerator import MemeTextGenerator
import pickle

generator = MemeTextGenerator(word_file = 'vocabulary3000.txt')
generator.build_candidates(word_file = 'vocabulary3000.txt', candidates_file = 'vocabulary3000.pickle')
generator = MemeTextGenerator(word_file = 'vocabulary7000.txt')
generator.build_candidates(word_file = 'vocabulary7000.txt', candidates_file = 'vocabulary7000.pickle')