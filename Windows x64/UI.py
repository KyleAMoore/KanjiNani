from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.clock import Clock

from convKana import convKana
from Word import Word
from Kanji import Kanji

import pickle
import os.path as pth

class HomePage(Widget):
	searchButton = ObjectProperty(None)
	indexButton = ObjectProperty(None)
	infoButton = ObjectProperty(None)

	def initialize(self, pageMan):
		self.pm = pageMan
		self.searchButton.bind(on_release = self.showSearch)
		self.indexButton.bind(on_release = self.showIndex)
		self.infoButton.bind(on_release = self.showInfo)

	def showSearch(self, button):
		self.pm.showSearch()

	def showIndex(self, button):
		print("Not Yet Implemented")
		#self.pm.showIndex()

	def showInfo(self, button):
		self.pm.showInfo()

class InfoPage(Widget):

	backButton = ObjectProperty(None)

	def showHome(self, button):
		self.pm.showHome()

	def initialize(self, pageMan):
		self.pm = pageMan
		self.backButton.bind(on_release = self.showHome)

class IndexPage(Widget):

	def initialize(self, pageMan):
		self.pm = pageMan

class SearchPage(Widget):

	def initialize(self, pageMan):
		self.pm = pageMan
		self.searchButton.bind(on_release = self.create_buttons)
		self.homeButton.bind(on_release = self.showHome)

	def create_buttons(self, pressed):

		try:
			self.results.clear_widgets()

		except:
			print("Search list already empty")

		self.searchBar.text = self.searchBar.text.strip()
		if self.searchBar.text == "":
			return

		#converts Katakana to Hiragana (implies Romaji -> Hiragana) because
		#kataToHira converts katakana to romaji then converts to hiragana
		self.searchBar.text = convKana.romToHira(convKana, convKana.kataToRoma(convKana, self.searchBar.text))

		#prevent crash due to accessing non-pronouncable characters (converted text is empty (usually from inputting a non-syllable like "q"))
		if self.searchBar.text == "":
			return

		try:
			entryList = data[self.searchBar.text]
			if len(entryList) == 0:
				return
		except:
			return

		resGrid = GridLayout(cols=2, rows=len(entryList), padding=5, spacing= 5, size_hint=(None, None), width= 500)
		resGrid.bind(minimum_height=resGrid.setter("height"))

		for x in entryList:
			if isinstance(x, Kanji):
				button = Button(text = x.getLiteral())
			elif isinstance(x, Word):
				try:
					button = Button(text = x.getKanji()[0])
				except: #displays only if only written in Hiragana/Katakana
					button = Button(text = x.getReading()[0])

			button.size_hint = (None, None)
			button.size = (self.width * .9, 40)
			button.font_name = "YuGothM.ttc"
			button.bind(on_release=self.openEntry)
			button.obj = x
			resGrid.add_widget(button)

			if isinstance(x, Kanji):
				lab = Label(text="Kanji")
			elif isinstance(x, Word):
				lab = Label(text="Word")

			lab.size_hint = (None, None)
			lab.size = (self.width * .1, 40)
			lab.font_name = "CALLI___.TTF"
			lab.color = [0, 0, 0, 1]
			resGrid.add_widget(lab)

		self.results.add_widget(resGrid)

	def openEntry(self, button):

		if isinstance(button.obj, Kanji):
			self.pm.getKanji().setKanji(button.obj)
			self.pm.getKanji().fillInfo()
			self.pm.showKanji()
		elif isinstance(button.obj, Word):
			self.pm.getWord().setWord(button.obj)
			self.pm.getWord().fillInfo()
			self.pm.showWord()
		else:
			print("invalid")

	def showHome(self, pressed):
		self.pm.showHome()

	searchBar = ObjectProperty(None)
	homeButton = ObjectProperty(None)
	searchButton = ObjectProperty(None)
	results = ObjectProperty(None)

class KanjiPage(Widget):
	kanji = None
	homeButton = ObjectProperty(None)
	searchButton = ObjectProperty(None)
	kanLayout = ObjectProperty(None)
	strokes = ObjectProperty(None)
	freq = ObjectProperty(None)
	kunRead = ObjectProperty(None)
	onRead = ObjectProperty(None)
	meaning = ObjectProperty(None)
	nanori = ObjectProperty(None)

	def fillInfo(self):
		self.AddKanji(self.kanji.getLiteral())
		self.strokes.text = str(self.kanji.getStrokes())
		self.showFreq()
		self.fillReadGrid()
		self.fillMeanings()
		self.fillNanori()

	def AddKanji(self, kan):
		self.kanLayout.clear_widgets()
		label = Label(text = kan)
		label.font_name = "YuGothM.ttc"
		label.font_size = 115
		label.color = [0, 0, 0, 1]
		self.kanLayout.add_widget(label)

	def showFreq(self):
		try:
			freqNum = self.kanji.getFreq()
			if (freqNum % 10 == 1) and (not (freqNum == 11)):	#ends in 1 except 11
				self.freq.text = str(freqNum) + "st most common Kanji in newspapers"
			elif (freqNum % 10 == 2) and (not (freqNum == 12)):	#ends in 1 except 12
				self.freq.text = str(freqNum) + "nd most common Kanji in newspapers"
			elif (freqNum % 10 == 3) and (not (freqNum == 13)):	#ends in 1 except 13
				self.freq.text = str(freqNum) + "rd most common Kanji in newspapers"
			elif (freqNum == 0):								#frequency known to be >2500
				self.freq.text = ">2500th most common Kanji in newspapers"
			else:												#frequency data unavailable
				self.freq.text = str(freqNum) + "th most common Kanji in newspapers"
		except:
			self.freq.text = ">2500th most common Kanji in newspapers"

	def fillReadGrid(self):
		try:
			kunArr = self.kanji.getKun()
			kunStr = ""

			for kun in kunArr: kunStr += kun + "\n"
			self.kunRead.text = kunStr
		except:
			self.kunRead.text = "N/A"

		try:
			onArr = self.kanji.getOn()
			onStr = ""

			for on in onArr: onStr += on + "\n"
			self.onRead.text = onStr
		except:
			self.onRead.text = "N/A"
	def fillMeanings(self):
		try:
			meanArr = self.kanji.getMeaning()

			meanStr = ""
			for mean in meanArr:
				meanStr += mean + "\n"

			self.meaning.text = meanStr
		except:
			self.meaning.text = "N/A"

	def fillNanori(self):
		try:
			nanArr = self.kanji.getNanori()

			nanStr = ""
			for nan in nanArr:
				nanStr += nan + "\n"
			self.nanori.text = nanStr

		except:
			self.nanori.text = "N/A"

	def initialize(self, pageMan):
		self.pm = pageMan
		self.homeButton.bind(on_release=self.showHome)
		self.searchButton.bind(on_release=self.showSearch)

	def showHome(self, button):
		self.pm.showHome()

	def showSearch(self, button):
		self.pm.showSearch()

	def setKanji(self, kan):
		self.kanji = kan

	def getKanji(self):
		return self.kanji

class WordPage(Widget):

	word = None
	wordLabel = ObjectProperty(None)
	readings = ObjectProperty(None)
	meanings = ObjectProperty(None)
	homeButton = ObjectProperty(None)
	searchButton = ObjectProperty(None)

	def fillInfo(self):
		self.buildWordLabel(self.word.getKanji())
		self.buildReadLabel(self.word.getReading())
		self.buildMeanGrid(self.word.getSense())

	def buildWordLabel(self, litArr):
		litStr = ""
		for lit in litArr:
			litStr += (lit + " ")

		self.wordLabel.text = litStr

	def buildReadLabel(self, readArr):
		readStr = ""
		for read in readArr:
			readStr += (read + " ")

		self.readings.text = readStr

	def buildMeanGrid(self, senseArr):
		self.meanings.clear_widgets()
		self.meanings.rows = len(senseArr)
		for sense in senseArr:
			meanStr = ""
			posStr = ""
			for pos in sense.getPos():
				posStr += (pos + "\n")
			posLab = Label(text = posStr)
			posLab.color = [0, 0, 0, 1]
			self.meanings.add_widget(posLab)

			for mean in sense.getMean():
				meanStr += (mean + "\n")
			meanLab = Label(text = meanStr)
			meanLab.color = [0, 0, 0, 1]
			self.meanings.add_widget(meanLab)

	def initialize(self, pageMan):
		self.pm = pageMan
		self.homeButton.bind(on_release=self.showHome)
		self.searchButton.bind(on_release=self.showSearch)

	def setWord(self, wd):
		self.word = wd

	def getWord(self):
		return self.word

	def showHome(self, button):
		self.pm.showHome()

	def showSearch(self, button):
		self.pm.showSearch()

## Creates and manages transitions between each of the individual pages
class PageManager(BoxLayout):

	##runs on initialization of 
	def __init__(self, **kwargs):
		super(PageManager, self).__init__(**kwargs)

		self.home = HomePage()
		self.info = InfoPage()
		self.index = IndexPage()
		self.search = SearchPage()
		self.kanji = KanjiPage()
		self.word = WordPage()

		self.home.initialize(self)
		self.info.initialize(self)
		self.index.initialize(self)
		self.search.initialize(self)
		self.kanji.initialize(self)
		self.word.initialize(self)

		self.add_widget(self.home)

	def showHome(self):
		self.clear_widgets()
		self.add_widget(self.home)

	def showInfo(self):
		self.clear_widgets()
		self.add_widget(self.info)

	def showIndex(self):
		self.clear_widgets()
		self.add_widget(self.index)

	def showSearch(self):
		self.clear_widgets()
		self.add_widget(self.search)

	def showKanji(self):
		self.clear_widgets()
		self.add_widget(self.kanji)

	def showWord(self):
		self.clear_widgets()
		self.add_widget(self.word)

	def getHome(self):
		return self.home

	def getIndex(self):
		return self.index

	def getSearch(self):
		return self.search

	def getWord(self):
		return self.word

	def getKanji(self):
		return self.kanji

	def getInfo(self):
		return self.info

##Overall App class. Creates and runs an instance of the PageManager class
class UIApp(App):
	def build(self):
		page = PageManager()
		return page

#loads dictionary data. The file must be named Dict and must be located in the
#same directory as this file
dataFile = open("Dict" , "rb")
data = pickle.load(dataFile)
dataFile.close()

UIApp().run()
