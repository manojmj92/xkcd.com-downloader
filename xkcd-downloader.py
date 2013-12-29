#-------------------------------------------------------------------------------
# Name:        xkcd downloader
# Purpose:
#
# Author:      Manoj
#
# Created:
# Copyright:   (c) www.manojmj.com
# Licence:
#-------------------------------------------------------------------------------


import urllib
import sys
from bs4 import BeautifulSoup
import os

dir = os.path.dirname(os.path.abspath(__file__))
xkcd_dir = dir +"\\xkcd"
if not os.path.exists(xkcd_dir):
    os.makedirs(xkcd_dir)

def download(startpagenumber):

    main_url = "http://www.xkcd.com/"
    mainbreaker=False
    for pageno in xrange(startpagenumber,0,-1):
        url_response = urllib.urlopen(main_url+str(pageno)).read()
        soup = BeautifulSoup(url_response)

        for imagelink in soup.findAll('img'):
            if imagelink['src'].split('/')[3] == "comics":
                filename = imagelink['src'].split('/')[4]
                path = os.path.join(xkcd_dir,filename)
                if os.path.exists(path):
                    print "Duplicate" #check for duplicate
                    continue
                image_response = urllib.urlopen(imagelink['src']).read()
                with open (path,"wb") as image:
                    image.write(image_response)
                    print "Downloaded file "+filename
        if mainbreaker==True:
            break

def startpagechecker():



    url="http://xkcd.com/archive/"
    response = urllib.urlopen(url)
    mysoup = BeautifulSoup(response)
    counter = 0

    for link in mysoup.findAll('a'):
        counter=counter+1
        if counter == 8:
            startpage = link['href'].split("/")[1]
            nooffiles = len(os.walk(xkcd_dir).next()[2])
            if nooffiles!= startpage:
                newstartpage = int(startpage)-nooffiles-1
                download(int(newstartpage))
            else:
                print "All files are downloaded"
                break
            #download(int(startpage))
            #break




startpagechecker()