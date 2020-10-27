from plyer import notification
import requests
from bs4 import BeautifulSoup


def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon = "G:\Shubh\Python\icon.ico",
        timeout= 10
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    # notifyMe("Shubham", "Conrona")      
    MyData = getData('https://www.mohfw.gov.in/') 
    soup = BeautifulSoup(MyData, 'html.parser') 
    # print(soup.prettify()) 
    myDataStr = "" 
    for tr in soup.find_all('table'):
        myDataStr += tr.get_text()
    newData = myDataStr.split('\n')[12:227]
    for item in newData:
        print(item)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             