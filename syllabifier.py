import sys
import os
import numpy as np
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

def syllabifyHindi(word):
    # matras = [u'\u0900',u'\u0901',u'\u0902',u'\u0903',u'\u093A',u'\u093B',u'\u093C',u'\u093D',u'\u093E',u'\u093F',
    # u'\u0940',u'\u0941',u'\u0942',u'\u0943',u'\u0944',u'\u0945',u'\u0946',u'\u0947',u'\u0948',u'\u0949',u'\u094A',
    # u'\u094B',u'\u094C',u'\u094D',u'\u094E',u'\u094F',u'\u0950',u'\u0951',u'\u0952',u'\u0953',u'\u0954',u'\u0955',
    # u'\u0956',u'\u0957']

    matras = [u'\u0902', u'\u0903', u'\u093e', u'\u093f', u'\u0940',
                 u'\u0941', u'\u0942', u'\u0943', u'\u0944', u'\u0946',
                 u'\u0947', u'\u0948', u'\u094a', u'\u094b', u'\u094c',
                 u'\u094d']

    limiters = ['.', '\"', '\'', '`', '!', ';', ', ', '?']

    syllabifiedWord = []
    for char in word:
        if char in limiters:
            syllabifiedWord.append(char)
        elif char in matras:
            syllabifiedWord[-1] = syllabifiedWord[-1] + char
        else:
            try:
                if syllabifiedWord[-1][-1] == u'\u094d':
                    syllabifiedWord[-1] = syllabifiedWord[-1] + char
                else:
                    syllabifiedWord.append(char)
            except IndexError:
                syllabifiedWord.append(char)

    return np.array(syllabifiedWord)


def syllabify(hindi, english):

    sHindi = syllabifyHindi(hindi)
    sEnglish = ([transliterate(s,sanscript.DEVANAGARI,sanscript.ITRANS) for s in sHindi])

    if (len(sEnglish) > 1 and 'a' in sEnglish[-1]):
        if len(sEnglish[-1]) > 1:
            sEnglish[-1] = sEnglish[-1].strip('a')[0]
    
    for syllable in sEnglish:
        if 'A' in syllable:
            sEnglish[sEnglish.index(syllable)] = syllable.lower()
        elif 'M' in syllable:
            sEnglish[sEnglish.index(syllable)] = syllable.replace("M","n")
        elif 'I' in syllable:
            sEnglish[sEnglish.index(syllable)] = syllable.replace("I","i")
        else:
            sEnglish[sEnglish.index(syllable)] = syllable.lower()

    sdata = np.array([(sHindi[i], sEnglish[i].lower()) for i in range(len(sHindi))])

    return sdata

def syllable2word(syllist):
    return "".join(syllist)

