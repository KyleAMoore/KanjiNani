::Average Runtime:	28.2095s
::Standard Deviation:	 1.2715s

@echo off

if NOT exist "Data" mkdir Data & echo Created directory Data

cd BuildData

echo Processing Kanji...
python KanjiFromXML.py
echo. & echo Kanji data processed

echo Processing Words...
python WordsFromXML.py
echo. & echo Word data processed

echo Combining into Dictionary
python ToHiraDict.py
echo. & echo Data combined into Dictionary

::timeout 5
pause
