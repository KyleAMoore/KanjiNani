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
"""
This script takes two lists: one populated with Kanji objects, and the other Word objects.
These lists are converted into a dictionary that has Hiragana strings as keys and sets
as values. Each set is composed of every Kanji and Word object that can have the
pronunciation specified by the key. Each object can (and probably will) appear in
multiple sets, because each can have multiple acceptable pronunciations.
"""

#!usr/bin/python
import pickle
import os
import sys

from convKana import convKana
import Word
import Kanji

kanFile = open(os.path.pardir + "\Data\Kanji", "rb")
kanji = pickle.load(kanFile)
kanFile.close()
os.remove(os.path.pardir + "\Data\Kanji")

kana = {}

#steps through every Kanji object and stores them in the dictionary
for i in range(len(kanji)):
    print(("\rProcessing Kanji " + str(i + 1) + " of " + str(len(kanji))), end="")

    #steps through each reading of the current Kanji
    for kunr in kanji[i].getKun():
        #tries to add Kanji to set at the position represented in the dictionary by
        #the pronunciation. Converts all to Hiragana temporarily so that there are not
        #duplicate sets using the same pronunciation with different character sets
        try:
            kana[convKana.kataToHira(convKana, kunr)].add(kanji[i])
        #creates a new set a the current pronunciation if it does not already exist
        except:
            kana[convKana.kataToHira(convKana, kunr)] = {kanji[i]}

    for onr in kanji[i].getOn():
        #tries to add Kanji to set at the position represented in the dictionary by
        #the pronunciation. Converts all to Hiragana temporarily so that there are not
        #duplicate sets using the same pronunciation with different character sets
        try:
            kana[convKana.kataToHira(convKana, onr)].add(kanji[i])
        #creates a new set a the current pronunciation if it does not already exist
        except:
            kana[convKana.kataToHira(convKana, onr)] = {kanji[i]}

wordFile = open(os.path.pardir + "\Data\Words", "rb")
words = pickle.load(wordFile)
wordFile.close()
os.remove(os.path.pardir + "\Data\Words")

print()

#steps through every Kanji object and stores them in the dictionary
for j in range(len(words)):
    print(("\rProcessing Word " + str(j + 1) + " of " + str(len(words))), end="")

    #steps through each reading of the current word
    for read in words[j].getReading():
        if(not(read == "")):    #prevent adding of words (usually punctuation) that have no pronunciation
            #tries to add Word to set at the position represented in the dictionary by
            #the pronunciation. Converts all to Hiragana temporarily so that there are not
            #duplicate sets using the same pronunciation with different character sets
            try:
                kana[convKana.kataToHira(convKana, read)].add(words[j])
            #creates a new set a the current pronunciation if it does not already exist
            except:
                kana[convKana.kataToHira(convKana, read)] = {words[j]}

#store dictionary in a separate file
outFile = open(os.path.pardir + "\Data\Dict", "wb")
pickle.dump(kana, outFile)
outFile.close()
