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

import xml.etree.ElementTree as ET
import pickle
import os.path as pth
import sys

from Word import Word, Sense
from convKana import convKana

"""
XML Tree Structure:
<tree>
    <entry>
        <k_ele>...</k_ele>
        <k_ele>...</k_ele>
        ...

        <r_ele>...</r_ele>
        <r_ele>...</r_ele>
        ...

        <sense>
            <gloss>...</gloss>
            <gloss>...</gloss>
            ...

            <pos>...</pos>
            <pos>...</pos>
            ...
        </sense>
        <sense>
        ...
        </sense>
        ...
    </entry>
</tree>
"""

#retrieve entire xml tree
tree = ET.parse("Words\JMdict_e.xml")
root = tree.getroot()

words = []

#find all child trees that represent individual words
wordTrees = root.findall("entry")
length = str(len(wordTrees))
wordNum = 0

#extract information about each word from xml trees and store in a list of Word objects
for entry in wordTrees:

    #progress reporting
    wordNum += 1
    print(("\rProcessing Word " + str(wordNum) + " of " + length), end="")

    #find and store all ways of writing the word, with or without kanji
    kanji= []
    for kele in entry.findall("k_ele"):
        kanji.append(kele.find("keb").text)

    #find and store all pronunciations for the word
    reading = []
    for rele in entry.findall("r_ele"):
        reading.append(rele.find("reb").text) #not adding words to dict correctly original: reading.append(rele.find("reb").text)

    #finds all senses and stores as a list of sense objects
    sense = []
    for thisSense in entry.findall("sense"):
        #find and store list of meanings for given sense
        meaning = []
        for gloss in thisSense.findall("gloss"):
            meaning.append(gloss.text)

        #find and store list of parts of speech for a given sense
        pos = []
        for part in thisSense.findall("pos"):
            pos.append(part.text)
        sense.append(Sense(meaning, pos))

    #create word object
    thisWord = Word(kanji, reading, sense)

    words.append(thisWord)

#store list in a separate file for later processing
serialFile = open(pth.pardir + "\Data\Words", "wb")
pickle.dump(words, serialFile)
serialFile.close()
