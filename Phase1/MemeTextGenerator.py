from xpinyin import Pinyin
import Levenshtein
import numpy as np
import epitran
import pickle

class MemeTextGenerator:
    def __init__(self, word_file = None, delimiter = '\n', candidates_file = None):
        if candidates_file != None:
            with open(candidates_file, 'rb') as f:
                self.candidates = pickle.load(f)
                self.words = []
                for pair in self.candidates:
                    self.words.append(pair[0])
                self.words = np.array(self.words)
        elif word_file != None:
            with open(word_file, 'r') as f:
                self.words = f.read().strip().split(delimiter)
            self.words = np.array(self.words)
        else:
            print('Need either word_file or candidates_file')
            raise ValueError

    def build_candidates(self, word_file, delimiter = '\n', candidates_file = 'vocabulary.pickle'):
        with open(word_file, 'r') as f:
            self.words = f.read().strip().split(delimiter)
        self.words = np.array(self.words)
        epi = epitran.Epitran('eng-Latn', ligatures=True)
        vowels = ['ə', 'æ', 'ɪ', 'i', 'e', 'ɔ', 'a', 'ʌ', 'u', 'ɛ', 'ɑ', 'o', 'ʊ']
        consonants = ['b', 'n', 'd', 'l', 't', 'j', 'ɹ', 'ʃ', 'w', 'v', 's', 'z', 'k', 'm', 'p', 'ŋ', 'ɹ̩', 'ʤ', 'ʧ', 'ʒ', 'f', 'ɡ', 'h', 'ð', 'θ']
        ipa2py = {'-':[''],
                 'ə':['e', 'a'], 'æ':['e'], 'ɪ':['i'], 'i':['i'], 'e':['e'], 'ɔ':['o'], 'a':['a'], 'ʌ':['a'], 'u':['u'], 'ɛ':['e'], 'ɑ':['a'], 'o':['o'], 'ʊ':['u'], 
                 'ow':['ou'], 'aw':['ao'], 'iə':['ia'], 'əwə':['uo', 'wo'], 'əwəl':['uo', 'wo'], 'əl':['ou'], 
                 'j':['i'], 'ɹ':['r'], 'ʃ':['xi','sh'], 'v':['f'], 's':['s','sh'],'z':['z'], 'ŋ':['ng'], 'ɹ̩':['er'], 'ʤ':['ju', 'zhe'], 'ʧ':['qi', 'qu'], 'ʒ':['ju', 'zhe'], 'ð':['l'], 'θ':['s', 'sh'], 'l':['o'], 
                 'tɹ':['ch'], 'tɹ̩':['ter'], 'dɹ':['zh'], 'dɹ̩':['der'], 'lɹ̩':['ler'], 'kw':['ku'], "dz":['zi'], "ts":['ci']}

        def ipa_2_py(ipa):
            py = ['']
            index = 0
            L = len(ipa)
            while index < L:
                if index+3 < L and ipa[index:index+4] in ipa2py:
                    k = 4
                    py_num = len(py)
                    for i in range(1, len(ipa2py[ipa[index:index+k]])):
                        for j in range(py_num):
                            py.append(py[j] + ipa2py[ipa[index:index+k]][i])
                    for j in range(py_num):
                        py[j] += ipa2py[ipa[index:index+k]][0]
                    index += k
                elif index+2 < L and ipa[index:index+3] in ipa2py:
                    k = 3
                    py_num = len(py)
                    for i in range(1, len(ipa2py[ipa[index:index+k]])):
                        for j in range(py_num):
                            py.append(py[j] + ipa2py[ipa[index:index+k]][i])
                    for j in range(py_num):
                        py[j] += ipa2py[ipa[index:index+k]][0]
                    index += k
                elif index+1 < L and ipa[index:index+2] in ipa2py:
                    k = 2
                    py_num = len(py)
                    for i in range(1, len(ipa2py[ipa[index:index+k]])):
                        for j in range(py_num):
                            py.append(py[j] + ipa2py[ipa[index:index+k]][i])
                    for j in range(py_num):
                        py[j] += ipa2py[ipa[index:index+k]][0]
                    index += k
                elif ipa[index] == 'l' and index+1 < L and ipa[index+1] in vowels:
                    for i in range(len(py)):
                        py[i] += ipa[index]
                    index += 1
                elif ipa[index] in ipa2py:
                    py_num = len(py)
                    for i in range(1, len(ipa2py[ipa[index]])):
                        for j in range(py_num):
                            py.append(py[j] + ipa2py[ipa[index]][i])
                    for j in range(py_num):
                        py[j] += ipa2py[ipa[index]][0]
                    index += 1
                else:
                    for i in range(len(py)):
                        py[i] += ipa[index]
                    index += 1
            return py
        
        candidates = []
        for word in self.words:
            ipa = epi.transliterate(word)
            py = ipa_2_py(ipa)
            candidates.append((word, py))
        with open(candidates_file, 'wb') as f:
            pickle.dump(candidates, f)

    def load_candidates(self, candidates_file = 'vocabulary.pickle'):
        with open(candidates_file, 'rb') as f:
            self.candidates = pickle.load(f)

    def generate(self, s):
        if self.candidates == None:
            print('No candidates')
            return
        p = Pinyin()
        min_distance = float('inf')
        distances = []
        cand_words = []
        for i in range(len(s)-1):
            chs = p.get_pinyin(s[i:i+2]).split('-')
            target = ''.join(chs)
            target = target.replace('y', 'i')
            ds = []
            for cand in self.candidates:
                d = []
                for py in cand[1]:
                    if py[0] != target[0]: d.append(10)
                    else: d.append(Levenshtein.distance(py, target, weights=(1, 1, 2)))
                ds.append(min(d))
            ds = np.array(ds)
            cand_words.append(self.words[ds == min(ds)])
            distances.append(min(ds))
        min_distance = min(distances)
        if min_distance > 2:
            return None
        results = []
        replace_words = []
        for i in range(len(s)-1):
            if distances[i] == min_distance:
                for word in cand_words[i]:
                    results.append(s[:i] + word + s[i+2:])
                    replace_words.append(word)
        return results, replace_words

if __name__ == '__main__':
    s = u'有備而來'
    generator = MemeTextGenerator('vocabulary3000.txt')    
    result = generator.generate(s)
    if result == None:
        generator = MemeTextGenerator('vocabulary7000.txt')    
        result = generator.generate(s)
    print(result)