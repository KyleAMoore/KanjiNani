# -*- coding: utf-8 -*-
"""
@author: kmoore
"""

## Class containing information for a given kanji character.
# fields:
#   literal: the kanji character as it would be written. Unique to each kanji
#   strokes: the number of pen strokes required to write the character
#   freq: how common the kanji is in everyday use. Currently, only data for top 2500 characters is available
#   kunRead: a list of kun'yomi (native reading) for the kanji character
#   onRead: a list of on'yomi (Chinese reading) for the kanji character
#   nanori: a list of nanori for the kanji character (a nanori is the reading that a character can take when
#                                                     when being used in a name or other proper noun)
#   meaning: a list of meanings that the kanji character can take
class Kanji:

    def __init__(self, lit, stro=0, freq=0, kunArr=[], onArr=[], nanArr=[], meanArr=[]):
        if not isinstance(lit, str):
            raise TypeError("Literal must be a string")
        if not isinstance(stro, int):
            raise TypeError("Strokes must be an integer")
        if not isinstance(freq, int):
            raise TypeError("Frequency must be an integer")
        if not isinstance(kunArr, list):
            raise TypeError("Kun Readings must be a list")
        if not isinstance(onArr, list):
            raise TypeError("On Readings must be a list")
        if not isinstance(nanArr, list):
            raise TypeError("Nanori Readings must be a list")
        if not isinstance(meanArr, list):
            raise TypeError("Meanings must be a list")

        self.literal = lit
        self.strokes = stro
        self.freq = freq

        self.kunRead = []
        for k in range(len(kunArr)):
            if not(isinstance(kunArr[k], str)):
                raise TypeError("Kun Readings in list must be strings")
            self.kunRead.append(kunArr[k])

        self.onRead = []
        for o in range(len(onArr)):
            if not(isinstance(onArr[o], str)):
                raise TypeError("On Readings in list must be strings")
            self.onRead.append(onArr[o])

        self.nanori = []
        for n in range(len(nanArr)):
            if not(isinstance(nanArr[n], str)):
                raise TypeError("Nanori Readings in list must be strings")
            self.nanori.append(nanArr[n])

        self.meaning = []
        for m in range(len(meanArr)):
            if not(isinstance(meanArr[m], str)):
                raise TypeError("Meanings in list must be strings")
            self.meaning.append(meanArr[m])

    def addKun(self, kun):
        if not isinstance(kun, str):
            raise TypeError("Kun Reading must be a string")
        self.kunRead.append(kun)

    def addOn(self, on):
        if not isinstance(on, str):
            raise TypeError("On Reading must be a string")
        self.onRead.append(on)

    def addNanori(self, nan):
        if not isinstance(nan, str):
            raise TypeError("Nanori Reading must be a string")
        self.nanori.append(nan)

    def addMeaning(self, mean):
        if not isinstance(mean, str):
            raise TypeError("Meaning must be a string")
        self.meaning.append(mean)

    def setStrokes(self, stro):
        if not isinstance(stro, int):
            raise TypeError("Strokes must be an integer")
        self.strokes = stro

    def getStrokes(self):
        return self.strokes

    def setFreq(self, fr):
        if not isinstance(fr, int):
            raise TypeError("Frequency must be an integer")
        self.freq = fr

    def getFreq(self):
        return self.freq

    def setKun(self, kunArr):
        if not isinstance(kunArr, list):
            raise TypeError("Kun Readings must be a list")

        tempArr = []

        for i in range(len(kunArr)):
            if not(isinstance(kunArr[i], str)):
                raise TypeError("On Readings in list must be strings")
            tempArr.append(kunArr[i])

        self.kunRead = tempArr

    def getKun(self):
        return self.kunRead

    def setOn(self, onArr):
        if not isinstance(onArr, list):
            raise TypeError("On Readings must be a list")

        tempArr = []

        for i in range(len(onArr)):
            if not(isinstance(onArr[i], str)):
                raise TypeError("On Readings in list must be strings")
            tempArr.append(onArr[i])

        self.onRead = tempArr

    def getOn(self):
        return self.onRead

    def setNanori(self, nanArr):
        if not isinstance(nanArr, list):
            raise TypeError("Nanori Readings must be a list")

        tempArr = []

        for i in range(len(nanArr)):
            if not(isinstance(nanArr[i], str)):
                raise TypeError("Nanori Readings in list must be strings")
            tempArr.append(nanArr[i])

        self.nanori = tempArr

    def getNanori(self):
        return self.nanori

    def setMeaning(self, meanArr):
        if not isinstance(meanArr, list):
            raise TypeError("Meanings must be a list")

        tempArr = []

        for i in range(len(meanArr)):
            if not(isinstance(meanArr[i], str)):
                raise TypeError("Meanings in list must be strings")
            tempArr.append(meanArr[i])

        self.meaning = tempArr

    def getMeaning(self):
        return self.meaning

    def getLiteral(self):
        return self.literal
