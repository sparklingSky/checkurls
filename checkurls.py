#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'sparklingSky'

import sys

reload(sys)
sys.setdefaultencoding('utf8')

import requests
import time
import progressbar

print "Enter the filename of the input data: "

input_file = raw_input()

with open(input_file) as f:
    num = len(f.readlines())

f = open(input_file, "r")

headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'accept-encoding': 'gzip, deflate, lzma, sdch',
           'accept-language': 'en-US,en;q=0.8',
           'upgrade-insecure-requests': '1',
           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36 OPR/32.0.1948.69'}

words = ["Removed for Copyright Infringement",
         "Not found",
         "No file",
         "No file(s) found",
         "THIS FILE WAS DELETED",
         "does not exist",
         "file was removed",
         "No results containing all your search terms were found",
         "This video is no longer available due to a copyright claim",
         "nothing found",
         "File no longer available",
         "file was not found",
         "This folder is no longer available",
         "removed due to DMCA Complaint",
         "Links have been permanently deleted",
         "Datei wurde wegen Urheberrechtsverletzung gelöscht",
         "Removed for DMCA",
         "Channel Banned",
         "dit bestand bestaat niet",
         "Links have been permanently deleted",
         "abuse removed",
         "this link to book was deleted",
         "File no longer available",
         "the file link that you requested is not valid",
         "cannot be found",
         "file removed",
         "no results found",
         "has been deleted",
         "bestand niet beschikbaar",
         "could not find any files",
         "link was deleted",
         "file is blocked",
         "page has been blocked",
         "file does not exist",
         "No files found",
         "File not found",
         "Link already expired",
         "file has been deleted",
         "Page not found",
         "file-not-found",
         "No links to show",
         "No related files",
         "file was deleted",
         "file is no longer available",
         "File not available",
         "content was removed",
         "file is not found",
         "Folder can not be found"]


def FHCheck():
    av_list = FilehostingsCheck(f)
    WriteToFile(av_list)
    print "\n"
    print "See the results in available.txt"


def FilehostingsCheck(f):
    pbar = progressbar.ProgressBar(maxval=num, \
        widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()
    av_list = []
    pbar_count = 0
    for url in f:
        time.sleep(0.5)
        try:
            req = requests.get(url, headers)
        except:
            pbar_count += 1
            pbar.update(pbar_count)
            continue
        for word in words:
            count = 0
            if word in req.text:
                count += 1
                break
            else:
                continue
        if count == 0:
            av_list.append(url)
        pbar_count += 1
        pbar.update(pbar_count)
    return av_list
    pbar.finish()


def WriteToFile(av_list):
    av = open("available.txt", "w")
    av.close()
    av = open("available.txt", "a")
    if av_list is []:
        av.write("Congrats! There're no available files.")
    else:
        for av_url in av_list:
            av.write(av_url)
    av.close()
    f.close()


FHCheck()
