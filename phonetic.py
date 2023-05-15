def phonetic(value):
    alphabet = {"A":"Alpha","B":"Bravo","C":"Charlie","D":"Delta","E":"Echo",
              "F":"Foxstrot","G":"Golf","H":"Hotel","I":"India","J":"Juliet",
              "K":"Kilo","L":"Lima","M":"Mike","N":"November","O":"Oscar",
              "P":"Papa","Q":"Quebec","R":"Romeo","S":"Sierra","T":"Tango",
              "U":"Uniform","V":"Victor","W":"Whiskey","X":"X-Ray","Y":"Yankee","Z":"Zulu" }
    result = []
    for i in value:
        result.append(alphabet[i])
    return ' '.join(result)