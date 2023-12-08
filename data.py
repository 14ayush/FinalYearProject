import os
import time 
import requests
import sys

# creating a function
def retrieve_html():
    for year in range(2015,2023):
        for month in range(1,13):
            if(month<10):
               url='https://en.tutiempo.net/climate/0{}-{}/ws-421390.html'.format(month,year)
            else:
                url='https://en.tutiempo.net/climate/{}-{}/ws-421390.html'.format(month,year)
            text=requests.get(url)
            text_utf=text.text.encode('utf=8')


            if not os.path.exists("Data/Html_Data/{}".format(year)):
                  os.makedirs("Data/Html_Data/{}".format(year))
            with open("Data/Html_Data/{}/{}.html".format(year,month),"wb") as output:
                  output.write(text_utf)
        
            sys.stdout.flush()

if __name__=="__main__":
    start_time=time.time()
    retrieve_html()
    stop_time=time.time()
    print("Time is {}".format(stop_time-start_time))
