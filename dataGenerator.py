import sys
import requests
import time

#--------------Generating more data if required---------------------------------------------------------------------#
def generateData():

    headers = {'user-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
        
    request_url = 'https://www.translate.com/translator/ajax_translate'

    names = []
    with open('names.txt', 'r', encoding="utf-8") as n:
        for name in n:
            name = name.split(" ")[0].strip("\n")
            data = {
                'text_to_translate': str.lower(name),
                'source_lang': 'en',
                'translated_lang': 'hi',
                'use_cache_only': 'false'
            }
            r = requests.post(url=request_url, headers=headers, data=data)
            nameT = (r.text.split(',')[2].split(":")[1])
            names.append(name + " " + str.encode(nameT, encoding="utf-8").decode(encoding="unicode-escape") + "\n")
            break

        return names
#-------------------------------------------------------------------------------------------------------------------#    

        