import csv
import logging 
import datetime 
import urllib2
from StringIO import StringIO
import argparse
import sys
import re

logging.basicConfig(filename='error.log', level=loggin.DEBUG)

parser = argparse.ArgumentParser(description='we use this to pass cvs url from command line')
parser.add_argument('--url', action="store", dest="url", type=str)

def getURL(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    return response.read()
    
def processIMG(csvfile):
    reader = csv.reader(StringIO(csvfile))
    rowcount = 0
    imgcount = 0
    jpegcount = 0
    giftcount = 0
    pngcount = 0
    REI = re.IGNORECASE

    for row in reader:
        rowcount += 1
        filename = row[0]
        if re.search(r'(.PNG$|.JPG$|.GIF$|.JPEG$)', filename, REI):
            imgcount += 1
        elif re.search(r'(.JPG$|.JPEG$)', filename, REI):
            jpegcount += 1
        elif re.search(r'.PNG$', filename, REI):
            pngcount += 1
        else:
            gifcount += 1
    imgpercentage = round(float(imgcount) / float(rowcount) * 100, 2)
    jpegpercentage = round(float(jpegcount) / float(rowcount) * 100, 2)
    pngpercentage = round(float(pngcount) / float(rowcount) * 100, 2)
    gifpercentage = round(float(gifcount) / float(rowcount) * 100, 2)
    print 'Total # of hits : {}'.format(rowcount)
    print 'Total # of image hit: {}'.format(imgcount)
    print 'Image request account for {}% of all requests. JPEG has {}% PNG has {}% & GIF has {}% hits.'.format(imgpercentage, jpegpercentage, pngpercentage, gifpercentage)

def processBrowser(csvfile):
    reader = csv.reader(StringIO(csvfile))
    safaricount = 0
    chromecount = 0
    firefoxcount = 0
    iecount = 0
    linecount = 0
    REI = re.IGNORECASE
    
    for brow in reader:
        linecount += 1
        browser = brow[2]
        if re.search(r'Chrome+/\d{1,3}.\d{0,3}.\d{0,5}.\d\sSafari/537.36$', browser, REI):
            chromecount += 1
        elif re.search(r'Firefox/\d{0,2}.\d{0,2}$', browser, REI):
            firefoxcount += 1
        elif re.search(r'MSIE\s\d{0,2}.\d{0,2}', browser, REI):
            iecount += 1
        elif re.search(r'Safari/\d{0,4}.\d{0,4}$', browser, REI) != 'Safari/537.36':
            safaricount += 1
    firefoxper = round(float(firefoxcount) / float(linecount) * 100, 2)
    safariper = round(float(safaricount) / float(linecount) * 100, 2)
    chromeper = round(float(chromecount) / float(linecount) * 100, 2)
    ieper = round(float(iecount) / float(linecount) * 100, 2)
    print '\n'
    print 'Total # of Firefox browser Used : {} that is {}% of total usage.'.format(firefoxcount, firefoxper)
    print 'Total # of Safari browser Used : {} that is {}% of total usage.'.format(safaricount, safariper)
    print 'Total # of Chrome browser Used : {} that is {}% of total usage.'.format(chromecount, chromeper)
    print 'Total # of Microsoft Internet Explorer browser Used : {} that is {}% of total usage.'.format(iecount, ieper)    
 
#Extra credit
 def processHitsHourly(csvfile):
     reader = csv.reader(StringIO(csvfile))
     hour_one = 0
     hour_two = 0
     hour_three = 0
     hour_four = 0
     hour_five = 0
     hour_six = 0
     totalcount = 0
     REI = re.IGNORECASE

     for hhits in reader:
         totalcount += 1
         hourhit = hhits[1]
         if re.search(r'0:\d{0,2}$', hourhit, REI):
             hour_one += 1
         elif re.search(r'1:\d{0,2}$', hourhit, REI):
             hour_two += 1
         elif re.search(r'2:\d{0,2}$', hourhit, REI):
             hour_three += 1
         elif re.search(r'3:\d{0,2}$', hourhit, REI):
             hour_four += 1
         elif re.search(r'4:\d{0,2}$', hourhit, REI):
             hour_five += 1
         else:
             hour_six += 1
      totalhit = 
int(hour_one)+int(hour_two)+int(hour_three)+int(hour_four)+int(hour_five)+int(hour_six)
    print '\n'
    print 'Hour 12 has {} hits'.format(hour_one)
    print 'Hour 01 has {} hits'.format(hour_two)
    print 'Hour 02 has {} hits'.format(hour_three)
    print 'Hour 03 has {} hits'.format(hour_four)
    print 'Hour 04 has {} hits'.format(hour_five)
    print 'Hour 05 has {} hits'.format(hour_six)
    print 'All together , it has {} hits'.format(totalhit)            
            
def main():
    if args.url:
        try:
            urlparse = getURL(args.url)
            processIMG(urlparse)
            processBrowser(urlparse)
            processHitsHourly(urlparse)
        except Exception as e:
            logging.error('Error : {}'.format(e))
            print 'Something go wrong, check the logfile'
    else:
        print 'Please check your URL name'

if __name__ == "__main__":
    main()
            
          
