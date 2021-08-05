#! /usr/bin/python3

import googletrans
from googletrans import Translator
translator = Translator()
result = translator.translate('Hello World, you are my man!', src='en', dest='fr')
print(result.text)
