#!/usr/local/bin/python
# coding: latin-1-
import io
import urllib2
import json
import unicodedata
#from FileWorker import FileWorker
#from pymongo import MongoClient
#client = MongoClient('localhost', 27017)
#db = client['foursquare3_db']
#collection = db['venues_from_radiobase']


listaClientIDs = ["0125VG400XXUPPTHKROUI4BJBAYBAS4T1QL0WC0IQPBDP0M2",
                  "4FM5TWUUR5DTFJWLMAVUFPPF003K5EOHWOTPHDHEQVSDLJYL",
                  "X1VEOVHXX4SEHF3U5F0VR41JTWGF4JCWFSTPY42ZB1W2D4IG",
                  "31EXRFXXKZHCTXWZPZSMHUWA2XAAW54EJOGCTACWT3REPKCI",
                  "QETSDZBFBT4BXYUPYS0K2NN1MJJ4MM1ZALNVYSFQ5AYRF0JO",
                  "ZYC444ZB3GAIWL1RZHNMVMT3PY5WCQJIGTHG3DQYOLO1RU1T",
                  "FCWMSURYUQRSQHAFK43BUWPL032XO1AUGNPA1PR4EDCGGVFR",
                  "YKKBKQXTNDOZ2UGSH5DK4RBOYKAO0VS5BWOFMM0GBCYMRL4K",
                  "P5OH4OJSWORALBTV55LXHFZZQZ05WJXBZEIKKYWG4LKIE4MI",
                  "NYKGI5XX4GMBITG4ULA5QU0AFQBBSDNWL5LIQENTUTZUGTGI",
                  "BEYSSUOCQIF2ZQGYX5OZGIL5SNHE25SMEPAWSEQB5XV5AEEW"]


listaClientSecrets = ["SED3ZC05NNINFXU5FB1FEMHIGRFRECRMUKB4AALUSXE4DJOF",
                      "MGNKASEZGGVGKJB5ZI4LQKCYON534XSVY2LWCCT0FJTCNP10",
                      "NZ3CQ20XFCJ22LINI2INFKSV024YUUJ4DI4JABI3BQ04JCLO",
                      "FCH0HJGU50X04DQAPSDTQJZERK1KJQRBV5ZVB3DUR40QAUCD",
                      "B3Y2AK5XXXMNRBPNVDO40LZ20LBB0ZZXVTOQFOCMNLNABOML",
                      "ZJJQGQFZBEQJHUOCLQ1VGWOTDD55MDNXOERUKJBP0JQHVGWR",
                      "RA3DWJZJX2BTYCI1GDASLOHHEWBXD1YNYVV5JSFYZ1TJRR21",
                      "Z55UUPEPE1PNJHKAOTPFJ5DXS2FEYYTLKDIZYHLNUZ5BIOLN",
                      "N1F3CS5GXGGUNU2IWG33VBYIPN3KPMI3H1A144FNATVYVM5Q",
                      "H1QVKPKF13KGRMCICGZBKPW5EZG12QXHMW1LIKS1TWEBRMOV",
                      "I3HEXOZC2DXOKGHKWBB3WQVWHMKKOFMKJBYUCPIQDVSSDEEY"]

indice = 0

#fileworker = FileWorker()

venues_ids = set()
for i in range(10):
  #Filtramos venues de categoria 'Food'
  food_ID = '4d4b7105d754a06374d81259'

  #Filtramos venues de Guayaquil 
  near = 'Guayaquil'

  #limit representa la cantidad maxima de venues que se extraeran por requerimiento
  limit = '10'

  #fecha del dia actual
  v = "20170726"

  try:
    url = "https://api.foursquare.com/v2/venues/search?near="+ near +"&limit=" + limit + "&categoryId="+food_ID+"&client_id="+listaClientIDs[indice%11]+"&client_secret="+listaClientSecrets[indice%11]+"&v="+v
    raw_json = urllib2.urlopen(url)
    data = json.load(raw_json)

  except:
    print "\n\n\tCAMBIO DE API KEYS\n\n"
    indice += 1
    url = "https://api.foursquare.com/v2/venues/search?near="+ near +"&limit=" + limit + "&categoryId="+food_ID+"&client_id="+listaClientIDs[indice%11]+"&client_secret="+listaClientSecrets[indice%11]+"&v="+v

    raw_json = urllib2.urlopen(url)
    data = json.load(raw_json)

  if len(data["response"]["venues"]) > 0 :
    size=len(data["response"]["venues"])
    count=0
    type=""
    while(count<size):
      if(count>10):
          break
      id_lugar=data["response"]["venues"][count]["id"]
      place = data["response"]["venues"][count]["name"]

      place = unicodedata.normalize('NFKD', place)
      print place
      if(len(data["response"]["venues"][count]["categories"])>0):
          type = data["response"]["venues"][count]["categories"][0]["name"]
          print type

      print id_lugar
      count+=1

      id_lugar = str(id_lugar).strip()

      try:
        url2 = 'https://api.foursquare.com/v2/venues/' + id_lugar + '/tips?sort=recent' +"&client_id="+listaClientIDs[indice%11]+"&client_secret="+listaClientSecrets[indice%11] + '&v=' + v
        raw_json = urllib2.urlopen(url2)
        data2 = json.load(raw_json)
        items = data2["response"]['tips']['items']
        for item in items:
          print item['text']

      except:
        print 'Error'
      print '\n'


"""  
  #Writes in JSON
#  filename = 'jsonTEST'
#  useful_data = {'lat': lat, 'lng': lng, 'provincia': provincia, 'venues': infoLugares}
#  dictBase={idRadiobase:useful_data}
#  collection.insert(dictBase)
  #fileworker.writeJSON(filename, dictBase)
"""
