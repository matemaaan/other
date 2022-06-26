def getEgrul(inn):
    import urllib.request
    import zlib
    import json
    
    try:
        url = 'https://egrul.itsoft.ru/'+inn+'.json.gz'
        response = urllib.request.urlopen(url)
        data = zlib.decompress(response.read(), 16+zlib.MAX_WBITS)
        text = json.loads(data.decode('utf-8'))
    except:
        text = 'not found'

    return text[list(text.keys())[1]]

print(getEgrul('8601065254'))