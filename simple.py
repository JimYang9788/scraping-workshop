from urllib.request import urlopen ## Gives you url 
import requests  # gives you a response object
from bs4 import BeautifulSoup

def main():
    URL = "http://pythonscraping.com/pages/page1.html"
    html = urlopen('http://pythonscraping.com/pages/page1.html')
    print (html)
    print ("Running scraper...")
    html.read() ## Reads the actual file 
    
    
    ## Using bs4 to parse html objects
    bs = BeautifulSoup(html.read(), 'html.parser') # html parser is by default 
    bs2 = BeautifulSoup(html.read(), 'lxml') # html parser is by default 



    ## gets the h1
    bs.h1 
if __name__ == "__main__":
    main()    