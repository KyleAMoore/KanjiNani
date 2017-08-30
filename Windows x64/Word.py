#   This file is part of KanjiNani.
#
#   KanjiNani is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   KanjiNani is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with KanjiNani.  If not, see <http://www.gnu.org/licenses/>.

# -*- coding: utf-8 -*-

## A Word object containing relevant information about a given Japanese Word
# Each word can have multiple pronunciations, writings, meanings, and parts-of-speech
class Word:

    def __init__(self, kanArr=[], readArr=[], senArr=[]):
        if not(isinstance(kanArr, list)):
            raise TypeError("Kanji Readings must be a list")
        if not(isinstance(readArr, list)):
            raise TypeError("Hiragana Readings must be a list")
        if not(isinstance(senArr, list)):
            raise TypeError("Senses must be a list")

        self.kanji = kanArr
        self.reading = readArr
        self.sense = senArr

    def addSense(self, sen):
        if not(isinstance(sen, Sense)):
            raise TypeError("Sense must be a sense object")
        self.sense.append(sen)

    def addKanji(self, kan):
        if not(isinstance(kan, str)):
            raise TypeError("Kanji Reading must be a string")
        self.kanji.append(kan)

    def addReading(self, read):
        if not(isinstance(read, str)):
            raise TypeError("Hiragana Reading must be a string")
        self.reading.append(read)

    def setKanji(self, kanArr):
        if not(isinstance(kanArr, list)):
            raise TypeError("Kanji Readings must be a list")

        tempArr = []

        for i in range(len(kanArr)):
            if not(isinstance(kanArr[i], str)):
                raise TypeError("Kanji in list must be strings")
            tempArr.append(kanArr[i])
        self.kanji = tempArr

    def setReading(self, readArr):
        if not(isinstance(readArr, list)):
            raise TypeError("Hiragana Readings must be a list")

        tempArr = []

        for i in range(len(readArr)):
            if not(isinstance(readArr[i], str)):
                raise TypeError("Readings in list must be strings")
            tempArr.append(readArr[i])

        self.reading = tempArr

    def setSense(self, senArr):
        if not(isinstance(senArr, list)):
            raise TypeError("Senses must be a list")

        tempArr = []

        for i in range(len(senArr)):
            if not(isinstance(senArr[i], Sense)):
                raise TypeError("Senses in list must be sense object")
            tempArr.append(senArr[i])

        self.sense = tempArr

    def getKanji(self):
        return self.kanji

    def getReading(self):
        return self.reading

    def getSense(self):
        return self.sense

## A Sense is a specific meaning of a given word. Each word can have multiple
# Senses associated with it. A Sense is made up of meanings and parts of speech
class Sense:

    def __init__(self, mean=[], part=[]):
        if not(isinstance(mean, list)):
            raise TypeError("Meanings must be a list")
        if not(isinstance(part, list)):
            raise TypeError("Parts of Speech must be a list")
        self.meaning = mean
        self.pos = part

    def addMean(self, mean):
        if not(isinstance(mean, str)):
            raise TypeError("Meaning must be an string")
        self.meaning.append(mean)

    def setMean(self, mean):
        if not(isinstance(mean, list)):
            raise TypeError("Meanings must be a list")

        tempArr = []

        for i in range(len(mean)):
            if not(isinstance(mean[i], str)):
                raise TypeError("Meanings in list must be strings")
            tempArr.append(mean[i])

        self.meaning = tempArr

    def getMean(self):
        return self.meaning

    def addPos(self, ps):
        if not(isinstance(ps, str)):
            raise TypeError("Part of Speech must be an string")
        self.pos.append(ps)

    def setPos(self, part):
        if not(isinstance(part, list)):
            raise TypeError("Parts of Speech must be a list")

        tempArr = []

        for i in range(len(part)):
            if not(isinstance(part[i], str)):
                raise TypeError("Parts of Speech in list must be strings")
            tempArr.append(part[i])

        self.pos = tempArr

    def getPos(self):
        return self.pos
