# -*- coding: utf-8 -*-

import requests
import json
import base64
import subprocess
import time

def importation(cmd):
    
    subprocess.Popen(['/bin/bash', '-c', cmd])


file = input("What file do you want to convert to audio ? No extension please :")

url = 'https://cxl-services.appspot.com/proxy?url=https://texttospeech.googleapis.com/v1beta1/text:synthesize&token=03AOLTBLTTGuVDbT6tPMGAnlnZRlGDAjOnyJURgRW5t2I4f1ODzIo9oxBVBw1OmpumAtSG3kJQAWc5je-W6twNad8jUwMEbOHh-3J0b96mw-Gbk83gPBBLCWXWlwvKlVT4zKTV6l-w0pcWV44XQHi5DRKVrXo7Vdh5uaiS1xZZY05EHIGpqOjhuwqH6nwp5DATZEvoK4RBkuA_rmpXh-cYY34go4isF7nO-2T3e5r59hiKfJD4AmuoO0COyojrbGt-Kmc1gq42Q4ATPOSb-M0644_WhD06pZOYHIg5NMFCiszLfOppOtanWatV1oQFeZl36VDXQKx1WsIP'

# Headers of Google TTS translations
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Referer': 'https://cloud.google.com/text-to-speech/',
    'Origin': 'https://cloud.google.com'
}

# Choice of language
print('In what language is the text ?')
print("1. French -> 'fr'")
print("2. US -> 'us'")
print("3. British -> 'uk'")
print("4. Japanese -> 'jp'") # To try :)
langue = str(input())
choix = ('1', 'fr', '2', 'us', '3', 'uk', '4', 'jp')
man_voice = input("If available, do you prefer a man's voice (default is woman) ? If yes, type y : ")

nom = ""

if langue in choix:
    if langue in ('1', 'fr'):
        langue = "fr-FR"
        if man_voice == "y":
            nom = "fr-FR-Wavenet-D" # Best voices C (woman) and D (man)
        else:
            nom = "fr-FR-Wavenet-C" # Best voices C (woman) and D (man)
    if langue in ('2', 'us'):
        langue = "en-US"
        if man_voice == "y":
            nom = "en-US-Wavenet-D" # Best voices C or E (woman) and B or D (man)
        else:
            nom = "en-US-Wavenet-C" # Best voices C or E (woman) and B or D (man)
    if langue in ('3', 'uk'):
        langue = "en-GB"
        if man_voice == "y":
            nom = "en-GB-Wavenet-D" # Best voices A (woman) and D (man)
        else:
            nom = "en-GB-Wavenet-A" # Best voices A (woman) and D (man)
    if langue in ('4', 'jp'):
        langue = "ja-JP"
        nom = "ja-JP-Wavenet-A"
else:
    langue = "en-US"
    nom = "en-US-Wavenet-D"
    print("Putting default, american man.")

# Use Google API for each file
for num in range (2, 999):
    try:
        with open(f"x1{num:03}.txt", 'r') as source:
            texte = source.read()
    

# Params of Google TTS translations
            params = {"input": {"text": texte},
                    "voice":{"languageCode": langue,"name": nom},
                    "audioConfig":{"audioEncoding":"LINEAR16","pitch":"0.00","speakingRate":"1.00"}}

# Response from the API, recover the base64 from json.
            response = requests.post(url,headers=headers,data=json.dumps(params))
            response.raise_for_status()
            prepros = response.json()

            value_b64 = ""

            for i, (k, v) in enumerate(prepros.items()):
                value_b64 += v

# Decoding the base64 and creating the wav files.
            with open(f'{file}_{num:03}.wav', 'wb') as fichier:
                decoded = base64.b64decode(value_b64)
                fichier.write(decoded)
    except:
        print("No more files")
        break

