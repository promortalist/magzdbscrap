import os
import re
import requests

def wget4(url):
    try:
        os.system('wget --user-agent=Mozilla --content-disposition -E -c ' +'"'+url+'"')
    except:
        print ("Wget zwrócił błąd")

url = "https://magzdb.org/j/2684"
response = requests.get(url)
match = re.findall("(/num/[0-9]*)", str(response.content))
for numlink in match:
  url2 = "https://magzdb.org"+numlink
  print("Estrakcja linku: "+url2)
  response2 = requests.get(url2)
  match2 = re.findall("(/file/[0-9]*/dl)", str(response2.content))
  for filelink in match2:
      url3 = "https://magzdb.org"+filelink
      wget4(url3)
            
          
