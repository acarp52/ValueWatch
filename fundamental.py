import time
import urllib.request
import re
from bs4 import BeautifulSoup

stocks = ['GOOG', 'YHOO', 'AAPL']

def yahooKeyStats(stock):
    try:
        sourceCode = urllib.request.urlopen('http://finance.yahoo.com/quote/' + stock + '/key-statistics?p='+stock).read()
        pbr = sourceCode.split('Price/Book (mrq):</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
        print('price to book ratio:', stock, pbr)

    except Exception:
        print('failed yahoo', str(Exception))


def fidelityKeyStats(stock):
    url = 'http://eresearch.fidelity.com/eresearch/evaluate/fundamentals/keyStatistics.jhtml?stockspage=keyStatistics&symbols='
    page = urllib.request.urlopen(url+stock).read()
    soup = BeautifulSoup(page, "html.parser")
    td = soup.find_all('td')
    
    for tag in soup.find_all(re.compile("td class")):
        print(tag.name)
    
    
    #pbr = sourceCode.split('Price/Book</td><td class="lft-rt-border right ">')[1].split('</td>')[0]
    #print('price to book ratio:', stock, pbr)
    #pieces = sourceCode.split()
    #for piece in pieces:
    #print(sourceCode)
    
    #print(sourceCode.split(b'Price/Book</td><td class="lft-rt-border right ">\r\n\t\t\t')[0])#.split(b'</td>'[0]))
    
    #print(soup.title)
    for t in td:
        print(t)
	

for stock in stocks:
    fidelityKeyStats(stock)
    time.sleep(1)
