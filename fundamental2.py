from bs4 import BeautifulSoup
import requests


def betterFidelitySearch(stock):
#    url = 'http://apps.cnbc.com/view.asp?country=US&uid=stocks/ownership&symbol=YHOO.O'
    url = 'http://eresearch.fidelity.com/eresearch/evaluate/fundamentals/keyStatistics.jhtml?stockspage=keyStatistics&symbols='

    response = requests.get(url+stock).content
    soup = BeautifulSoup(response, 'lxml')
    
    datatables = soup.find_all('table', class_="datatable-component")
    for table in datatables:
        #print(table)
    
        tbls = table.find_all('tbody')
        for tbody in tbls:
            print(tbody)
            trs = tbody.find_all('tr')
            for tr in trs:
                tds = tr.find_all('td')
                print(tds)
            
betterFidelitySearch("YHOO")
