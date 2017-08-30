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

class convKana:
	#dict for mapping romaji(roman) syllables to Hiragana
	romHirMap = {
				"a":"あ", "i":"い", "u":"う", "e":"え", "o":"お", "vu":"ゔ",
				"ka":"か", "ki":"き", "ku":"く", "ke":"け", "ko":"こ",
				"ga":"が", "gi":"ぎ", "gu":"ぐ", "ge":"げ", "go":"ご",
				"sa":"さ", "shi":"し", "su":"す", "se":"せ", "so":"そ",
				"za":"ざ", "ji":"じ", "zu":"ず", "ze":"ぜ", "zo":"ぞ",
				"ta":"た", "chi":"ち", "tsu":"つ", "te":"て", "to":"と",
				"da":"だ", "di":"ぢ", "du":"づ", "dzu":"づ", "de":"で", "do":"ど",
				"na":"な", "ni":"に", "nu":"ぬ", "ne":"ね", "no":"の",
				"ha":"は", "hi":"ひ", "fu":"ふ", "hu":"ふ", "he":"へ", "ho":"ほ",
				"ba":"ば", "bi":"び", "bu":"ぶ", "be":"べ", "bo":"ぼ",
				"pa":"ぱ", "pi":"ぴ", "pu":"ぷ", "pe":"ぺ", "po":"ぽ",
				"ma":"ま", "mi":"み", "mu":"む", "me":"め", "mo":"も",
				"ya":"や", "yu":"ゆ", "yo":"よ",
				"ra":"ら", "ri":"り", "ru":"る", "re":"れ", "ro":"ろ",
				"la":"ら", "li":"り", "lu":"る", "le":"れ", "lo":"ろ",
				"wa":"わ", "wo":"を",
				"kya":"きゃ", "kyu":"きゅ", "kyo":"きょ",
				"sha":"しゃ", "shu":"しゅ", "sho":"しょ", "shya":"しゃ", "shyu":"しゅ", "shyo":"しょ", "she":"しぇ",
				"cha":"ちゃ", "chu":"ちゅ", "cho":"ちょ", "chya":"ちゃ", "chyu":"ちゅ", "chyo":"ちょ", "che":"ちぇ",
				"nya":"にゃ", "nyu":"にゅ", "nyo":"にょ",
				"hya":"ひゃ", "hyu":"ひゅ", "hyo":"ひょ",
				"bya":"びゃ", "byu":"びゅ", "byo":"びょ",
				"pya":"ぴゃ", "pyu":"ぴゅ", "pyo":"ぴょ",
				"mya":"みゃ", "myu":"みゅ", "myo":"みょ",
				"rya":"りゃ", "ryu":"りゅ", "ryo":"りょ",
				"lya":"りゃ", "lyu":"りゅ", "lyo":"りょ",
				"gya":"ぎゃ", "gyu":"ぎゅ", "gyo":"ぎょ",
				"ja":"じゃ", "ju":"じゅ", "jo":"じょ", "jya":"じゃ", "jyu":"じゅ", "jyo":"じょ", "je":"じぇ",
				"n":"ん",
				"wi":"うぃ", "we":"うぇ",
				"tsa":"つぁ", "tsi":"つぃ", "tse":"つぇ", "tso":"つぉ",
				"ti":"てィ", "tu":"とぅ",
				"fa":"ふぁ", "fi":"ふぃ", "fyu":"ふゅ", "fe":"ふぇ", "fo":"ふぉ",
				"di":"でぃ", "dyu":"でゅ",
				"va":"ヴぁ", "vi":"ヴぃ", "ve":"ヴぇ", "vo":"ヴぉ", "vyu": "ヴゅ"
				}

	#dict for converting katakana characters to romaji (roman) syllables
	kataRomMap = {
				"ア":"a", "イ":"i", "ウ":"u", "エ":"e", "オ":"o", "ヴ": "vu",
				"カ":"ka", "キ":"ki", "ク":"ku", "ケ":"ke", "コ":"ko",
				"サ":"sa", "シ":"shi", "ス":"su", "セ":"se", "ソ":"so",
				"タ":"ta", "チ":"chi", "ツ":"tsu", "テ":"te", "ト":"to",
				"ナ":"na", "ニ":"ni", "ヌ":"nu", "ネ":"ne", "ノ":"no",
				"ハ":"ha", "ヒ":"hi", "フ":"fu", "ヘ":"he", "ホ":"ho",
				"マ":"ma", "ミ":"mi", "ム":"mu", "メ":"me", "モ":"mo",
				"ヤ":"ya", "ユ":"yu", "ヨ":"yo",
				"ラ":"ra", "リ":"ri", "ル":"ru", "レ":"re", "ロ":"ro",
				"ワ":"wa", "ヲ":"wo",
				"ン":"n",
				"ガ":"ga", "ギ":"gi", "グ":"gu", "ゲ":"ge", "ゴ":"go",
				"ザ":"za", "ジ":"ji", "ズ":"zu", "ゼ":"ze", "ゾ":"zo",
				"ダ":"da", "ヂ":"di", "ヅ":"du", "デ":"de", "ド":"do",
				"バ":"ba", "ビ":"bi", "ブ":"bu", "ベ":"be", "ボ":"bo",
				"パ":"pa", "ピ":"pi", "プ":"pu", "ペ":"pe", "ポ":"po"
				}

	## Convert Katakana strings to equivalent Romaji(roman) strings ##
	# removes or replaces punctuation where appropriate. Does not
	# alter characters that already exist as Katakana
	#
	# input: a string of Katakana characters (can include punctuation/romaji)
	# output: an equivalent string of romaji characters
	# ex: kataToRoma(カイル・ムーア) -> "kairumuua"
	def kataToRoma(self, kata):
		retStr = ""

		for i in range(len(kata)):
			try:
				#for the following three cases, the character replaces the vowel
				#in the syllable with ya, yu, or yo
				if kata[i] == "ャ":
					retStr = retStr[:-1] + "ya"
				elif kata[i] == "ュ":
					retStr = retStr[:-1] + "yu"
				elif kata[i] == "ョ":
					retStr = retStr[:-1] + "yo"

				#for the following case, the vowel in the syllable is repeated
				elif kata[i] == "ー":
					if retStr[len(retStr) - 1] == "a":
						retStr += "a"
					elif retStr[len(retStr) - 1] == "e":
						retStr += "i"
					elif retStr[len(retStr) - 1] == "i":
						retStr += "i"
					elif retStr[len(retStr) - 1] == "o":
						retStr += "u"
					elif retStr[len(retStr) - 1] == "u":
						retStr += "u"

				#for the following three cases, the character replaces the vowel
				#in the syllable with another vowel
				elif kata[i] == "ィ":
					retStr = retStr[:-1] + "i"
				elif kata[i] == "ァ":
					retStr = retStr[:-1] + "a"
				elif kata[i] == "ォ":
					retStr = retStr[:-1] + "o"
				elif kata[i] == "ェ":
					retStr = retStr[:-1] + "e"
				elif kata[i] == "ゥ":
					retStr = retStr[:-1] + "u"

				#for the following case, the consonant in the following syllable is repeated
				elif kata[i] == "ッ":
					retStr += self.kataRomMap[kata[i + 1]][0]

				#the ・ character is removed and ignored (roughly equivalent to a Katakana only space)
				elif kata[i] == "・":
					continue;

				#all standard characters are directly mapped here
				else:
					retStr += self.kataRomMap[kata[i]]

			#the character is not a Katakana acceptable character and is passed through for later
			#handling. This character could be romaji, unhandled punctuation, etc.
			except:
				retStr += kata[i]

		return retStr

	## Convert Katakana strings to equivalent Romaji(roman) strings ##
	# Does not alter characters that already exist as Hiragana
	#
	# input: a string of Romaji characters
	# output: an equivalent string of Hiragana
	# ex: romToHira(kairumuua) -> "かいるむうあ"
	def romToHira(self, romaji):

		syllables = []

		tempStr = ""
		hirStr = ""

		#convert string to an array of syllables, where syllable is defined as
		#any number (including 0) of consonants followed by a vowel
		for i in range(len(romaji)):

			#character is already Hiragana/Katakana, added directly to output string
			if(romaji[i] >= "\u3040" and romaji[i] <= "\u3096"):
				hirStr += romaji[i]
			else:
				tempStr += romaji[i] #syllables all end with a vowel (except ん, which is handled separately below)

				#only converts letters (no punctuation)
				if(romaji[i].isalpha()):
					#vowel encountered, terminate syllable and add to list
					if(romaji[i] == "a" or romaji[i] == "e" or romaji[i] == "i" or romaji[i] == "o" or romaji[i] == "u"):

						syllables.append(tempStr)
						tempStr = ""

					#handles special case of ん which is the only syllable without an associated vowel sound
					#appends syllable "n" to list if n is at the end of the word or if the characrter after the "n" is not a vowel
					elif(romaji[i] == "n" and ((i == len(romaji) - 1) or #ん at the end of word
						(not(romaji[i+1] == "a" or romaji[i+1] == "e" or romaji[i+1] == "i" or
						romaji[i+1] == "o" or romaji[i+1] == "u")))):	#ん anywhere else in word (n not followed by a vowel)

						syllables.append(tempStr)
						tempStr = ""

		#convert each syllable in list of syllables to Hiragana character
		for i in range(len(syllables)):

			#Deals with syllables with repeat consonant, which must be preceeded by a "っ" character
			#Only runs if the # of consonants is >1  and the two consonants are the same
			if (len(syllables[i]) > 2) and (syllables[i][0] == syllables[i][1]): #repeat consonants indicates small tsu
				hirStr += "っ"
				syllables[i] = syllables[i][1:] #remove first character (repeat) from string

				#add converted string to output str if it is a legal syllable (exists in conversion table romHirMap)
				#otherwise, adds syllable
				try:
					hirStr += self.romHirMap[str.lower(newSyllable)]
				except:
					hirStr += syllables[i]
			else:
				#add converted string to output str if it is a legal syllable (exists in conversion table romHirMap)
				#otherwise, adds syllable
				try:
					hirStr += self.romHirMap[str.lower(syllables[i])]
				except:
					hirStr += syllables[i]
		return hirStr

	## Converts Katakana string to Hiragana string.
	# alias method for running string through both kataToRoma and romToHira
	# input: a string of Romaji, Katakana, or Hiragana (or any combination)
	# output: a string of equivalent Hiragana characters
	# example: kataToHira(カイル・ムーア) -> "かいるむうあ"
	def kataToHira(self, kata):
		return self.romToHira(self, self.kataToRoma(self, kata))
