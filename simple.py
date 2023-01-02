from urllib.request import urlopen ## Gives you url 
import requests  # gives you a response object
def main():
    URL = "http://pythonscraping.com/pages/page1.html"
    html = urlopen('http://pythonscraping.com/pages/page1.html')
    print (html)
    import pdb; pdb.set_trace()
    print ("Running scraper...")


if __name__ == "__main__":
    main()    