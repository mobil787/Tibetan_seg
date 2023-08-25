import pandas as pd 
import requests,json
import csv
import unicodedata
import html
from bs4 import BeautifulSoup
import re

# Insert your inputs of Tibetan words or sentences
tibetan_symbols = 'གཞན་གྱི་ཡོན་ཏན་མཐོང་ཙམ་གྱིས་མཐོང་ཆུང་དང་དམན་ལྟ་བྱེད་པས་སྡིག་པ་རྔམས་པོ་ཆེ་ཞིག་བསགས་པར་འགྱུར'

# URL of Online Tibetan to English Dictionary and Translation Tool
url = 'https://ttt.thlib.org/org.thdl.tib.scanner.OnLineScannerFilter'

# PAYLOAD of POST method of this website
payload = {
    'parrafo': tibetan_symbols,  # Input text
    'script': 'tibetan',  # Display results in Tibetan script
    'dict0': 'dict0',  # Search in English (JH-ENG) dictionary
    'dict1': 'dict1',  # Search in Other's English (JH-OE) dictionary
    'dict2': 'dict2',  # Search in Tenses (JH-T) dictionary   
    'dict3': 'dict3',  # Search in Sanskrit (JH-SKT) dictionary   
    'dict4': 'dict4',  # Search in Other Tibetan (OT)  dictionary   
    'dict5': 'dict5',  # Search in Def. Tibetan (JH-DEFT) dictionary
    'dict6': 'dict6',  # Search in Def. English (JH-DEFE)  dictionary   
    'dict7': 'dict7',  # Search in Div. Tibetan (JH-DIVT)  dictionary   
    'dict8': 'dict8',  # Search in Div. English (JH-DIVE)  dictionary   
    'dict9': 'dict9',  # Search in Syn. Tibetan (JH-ST) dictionary   
    'dict10': 'dict10',  # Search in Syn. English (JH-SE) dictionary   
    'dict11': 'dict11',  # Search in Comments (JH-C) dictionary   
    'dict12': 'dict12',  # Search in Ex. Tibetan (JH-EXT) dictionary   
    'dict13': 'dict13',  # Search in Ex. English (JH-EXE)  dictionary   
    'dict14': 'dict14',  # Search in Yogacara-bh. Gl. (YOGA) dictionary   
    'dict15': 'dict15',  # Search in Dan Martin (DM) dictionary   
    'dict16': 'dict16',  # Search in Jim Valby (JV) dictionary   
    'dict17': 'dict17',  # Search in Ives Waldo (IW) dictionary   
    'dict18': 'dict18',  # Search in Richard Barron (RB) dictionary   
    'dict19': 'dict19',  # Search in Rangjung Yeshe (RY) dictionary   
    'button': 'Translate'  # Submit the form with the "Translate" button
}

# Getting response from translation website
response = requests.post(url, data=payload, verify=False) # POST method
if response.status_code == 200:
    print("Success!")
else
    print("Failed!")

# Extract the final results as the table
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', attrs={'border': '1'})
table_content = str(table)
print(table_content)
html_file = open('table.html', 'w')
html_file.write(str(table))
html_file.close()




