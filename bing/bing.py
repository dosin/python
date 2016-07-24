#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Github https://github.com/dosin
# Some rights reserved
__author__ = 'dosin'

import sys
import re
import os
import urllib
import time

def download_to(market, path):

  # if path does not exist, create one
  if not os.path.exists(path):
    os.makedirs(path)

  # get images as many as possible
  indexs = range(-1, 30)

  # counter
  found = 0
  existed = 0
  downloaded = 0

  print '\nSearching images from ' + market.upper() + ' market'

  for index in indexs:
    # get url from http://global.bing.com/ using http GET method
    params = 'format=js&idx='+str(index)+'&n=1&nc='+str(int(time.time()))+'&setmkt='+market
    ufile = urllib.urlopen('http://global.bing.com/HPImageArchive.aspx?%s' % params)

    # stop for a while to make sure request succeed
    time.sleep(2)

    resp = ufile.read()
    if resp == 'null':
      # once you get 'null' as response which means there is no more image
      print 'Found ' + str(found) + ' images from ' + market.upper() + ' market'
      print str(existed) + ' existed'
      print str(downloaded) + ' downloaded'
      return

    url = re.search(r'url":"([:\/\w\.-]+)"', resp).group(1)

    # prefix for markets execpt zh-cn
    if not re.search('http', url):
      url = 'http://global.bing.com' + url

    found += 1
    print 'Found ' + url

    filename = re.search(r'rb\/([a-zA-Z0-9]+)_', url).group(1) + '.jpg'
    abspath = os.path.join(path, filename)

    # if image exists, skip, if doesn't, download it
    if os.path.exists(abspath):
      existed += 1
      print 'Image existed'
    else:
      downloaded += 1
      print 'Downloading ' + filename
      urllib.urlretrieve(url, abspath)
      

def main():

  # get markets from http://www.istartedsomething.com/bingimages/
  markets = ['zh-cn', 'en-us', 'en-gb', 'en-au', 'en-nz', 'en-ca', 'ja-jp', 'fr-fr']

  args = sys.argv[1:]

  # if no extra arguments download all to bing folder
  if not args:
    for market in markets:
      download_to(market, 'bing')

  # if arguments exist than usage is below
  if args and len(args) < 2:
    print '\nusage  : bing.py -path -market'
    print 'market : [cn, us, gb, au, nz, ca, jp, fr, all]'
    sys.exit(1)

  path = args[0][1:]

  if args[1] == '-cn':
    download_to(markets[0], path)
    sys.exit(1)

  if args[1] == '-us':
    download_to(markets[1], path)
    sys.exit(1)

  if args[1] == '-gb':
    download_to(markets[2], path)
    sys.exit(1)

  if args[1] == '-au':
    download_to(markets[3], path)
    sys.exit(1)

  if args[1] == '-nz':
    download_to(markets[4], path)
    sys.exit(1)

  if args[1] == '-ca':
    download_to(markets[5], path)
    sys.exit(1)

  if args[1] == '-jp':
    download_to(markets[6], path)
    sys.exit(1)

  if args[1] == '-fr':
    download_to(markets[7], path)
    sys.exit(1)

  if args[1] == '-all':
    for market in markets:
      download_to(market, path)

if __name__ == '__main__':
  main()
