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
https://docs.python.org/2/library/xml.etree.elementtree.html
"""
import xml.etree.ElementTree as ET
import pickle
import os.path as pth
import sys

from convKana import convKana
from Kanji import Kanji

"""
XML Tree Structure:
<tree>
    <character>
        <literal>...</literal>

        <misc>
            <strokes>...</strokes>
            <freq>...</freq>
        </misc>

        <rmgroup>
            <reading r_type="ja_on">...<?reading>
            <reading r_type="ja_on">...<?reading>
            ...

            <reading r_type="ja_kun">...<?reading>
            <reading r_type="ja_kun">...<?reading>
            ...

            <meaning>...</meaning>
            <meaning>...</meaning>
            ...

            <nanori>...</nanori>
            <nanori>...</nanori>
            ...
        </rmgroup>
    </character>
</tree>
"""

#retrieve entire xml tree
tree = ET.parse("Kanji\kanjidic2.xml")
root = tree.getroot()

chars = []

#find all child trees that represent individual characters
charTrees = root.findall("character")
length = str(len(charTrees))
charNum = 0

#extract information about each kanji from xml trees and store in a list of Kanji objects
for character in charTrees:

    #progress reporting
    charNum += 1
    print(("\rProcessing Kanji " + str(charNum) + " of " + length), end="")

    #Find character literal
    literal = character.find("literal").text
    thisChar = Kanji(literal)

    misc = character.find("misc")

    #Find Stroke Count of character
    strokes = int(misc.find("stroke_count").text)

    #Find Freq of character
    try:
        freq = int(misc.find("freq").text)

    #freq >2500 is treated as having a frquency of 0
    except:
        freq = 0

    #only include Kanji that are of frequency <= 2500 (to improve usability and size)
    if freq == 0:
        continue

    if character.find("reading_meaning"):
        rm = character.find("reading_meaning")
        rmgroup = rm.find("rmgroup")

        onRead = []
        kunRead = []

        #find and store all pronunciations (kun and on)
        for reading in rmgroup.findall("reading"):
            if(reading.attrib["r_type"]== "ja_on"):
                onRead.append(reading.text)
            elif(reading.attrib["r_type"] == "ja_kun"):
                kunRead.append(reading.text)

        #find and store all meanings
        mean = []
        for meaning in rmgroup.findall("meaning"):
            if(not meaning.attrib):
                mean.append(meaning.text)

        #find and store all nanori (Name readings)
        nanori = []
        for nan in rm.findall("nanori"):
            nanori.append(nan.text)
    else:
        onReading = []
        kunReading = []
        mean = []
        nanori = []

    #add info to current object
    thisChar.setStrokes(strokes)
    thisChar.setKun(kunRead)
    thisChar.setOn(onRead)
    thisChar.setFreq(freq)
    thisChar.setMeaning(mean)
    thisChar.setNanori(nanori)

    chars.append(thisChar)

#store list in a separate file for later processing
serialFile = open(pth.pardir + "\Data\Kanji", "wb")
pickle.dump(chars, serialFile)
serialFile.close()
