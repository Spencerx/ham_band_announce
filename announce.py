#!/usr/bin/python3
from urllib.request import urlopen
import subprocess
import xml.etree.ElementTree as ET
from datetime import datetime

# Any string passed will pass to fesival for speech
def say(phrase):
    subprocess.call('echo '+phrase+'|/usr/bin/festival --tts',shell=True)

if (datetime.now().hour >= 7 and datetime.now().hour <=20):
    url = "http://www.hamqsl.com/solarxml.php"
    html = urlopen(url)
    xml=(bytes.decode(html.read()))
    root = ET.fromstring(xml)
    for band in root[0][16]:
        print(band.attrib,band.text)
        if(band.text=='Good'):
            phrase = "Ham Radio Band. " + band.attrib['name'] + ". have good conditions"
            phrase = phrase.replace('-',' and ')
            phrase = phrase.replace('80m','80 meter ')
            phrase = phrase.replace('40m','40 meter ')
            phrase = phrase.replace('30m','30 meter ')
            phrase = phrase.replace('20m','20 meter ')
            phrase = phrase.replace('17m','17 meter ')
            phrase = phrase.replace('12m','12 meter ')
            phrase = phrase.replace('10m','10 meter ')
            print(phrase)
            say(phrase)
