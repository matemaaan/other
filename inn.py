def getEgrul(inn):
    import urllib.request
    import zlib
    import json

    while len(inn)<10: inn = '0'+inn
    try:
        url = 'https://egrul.itsoft.ru/'+inn+'.json.gz'
        response = urllib.request.urlopen(url)
        data = zlib.decompress(response.read(), 16+zlib.MAX_WBITS)
        text = json.loads(data.decode('utf-8'))
        org = dict()
        org['name'] = text[list(text.keys())[1]]["СвНаимЮЛ"]["@attributes"]["НаимЮЛПолн"]
        org['sname'] = text[list(text.keys())[1]]["СвНаимЮЛ"]["@attributes"]["НаимЮЛСокр"]
        org['msrn'] = text[list(text.keys())[1]]["@attributes"]["ОГРН"]
        org["tin"] = text[list(text.keys())[1]]["@attributes"]["ИНН"]
        org["state_regis"] = text[list(text.keys())[1]]["СвОбрЮЛ"]["@attributes"]["ОГРН"]
        org["state_regis_date"] = text[list(text.keys())[1]]["СвОбрЮЛ"]["@attributes"]["ДатаОГРН"]
    except:
        org = 'not found'
    return org

print(getEgrul('8601065254'))
