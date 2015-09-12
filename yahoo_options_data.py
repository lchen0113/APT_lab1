import re
import urllib
import locale
from bs4 import BeautifulSoup

def contractAsJson(filename):

   file=open(filename,'r')
   soup=BeautifulSoup(file,'html.parser')

   jsonQuoteData = {"currPrice":0.0,"dateUrls":[],"optionQuotes":[]}

   # find the currPrice
   currPrice=soup.find( attrs={"class","time_rtq_ticker"})
   jsonQuoteData["currPrice"]=float(currPrice.contents[0].contents[0])

   #find date Urls
   for item in soup.find_all( href=re.compile("(\/q\/[a-z]+\?s=)[a-zA-Z_0-9]*&m=[0-9-]+"   ) ):
      web_prefix="http://finance.yahoo.com"
      jsonQuoteData["dateUrls"].append( str(web_prefix + item['href'].replace('&','&amp;')))

   #find the individual contacts
   #my code could not pass this step!!!


   print jsonQuoteData
   return jsonQuoteData
