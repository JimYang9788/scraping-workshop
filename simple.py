from urllib.request import urlopen 

def main():
    html = urlopen('http://pythonscraping.com/pages/page1.html')
    print (html)
    print ("Running scraper...")


if __name__ == "__main__":
    main()    