import requests
import threading
from threading import Thread
from queue import Queue, Empty
import json
from itertools import cycle
import random
import time
import queue
from termcolor import colored
import os
import subprocess
import tkinter
from tkinter import messagebox
import sys
import hashlib
import ctypes
import sys
import colorama
import configparser

with open('proxies.txt','r', encoding='utf-8') as f:
	ProxyPool = cycle(f.read().splitlines())
with open('cookies.txt','r', encoding='utf-8') as f:
	cooks = f.read().splitlines()


os.system('color')
def sendreqproxy(url, cookie, proxy):
    cookies = {
        ".ROBLOSECURITY": cookie
    }
    while True:
        r = requests.get(url, cookies=cookies, proxies=proxy)
        if r.status_code == 429:
            print('API is ratelimited.')
            pass
        elif r.status_code == 200:
            print('Successfully sent a request.')
            print(r.text)
        else:
            print(r.text)
            pass
def sendreqcookie(url, cookie):
    cookies = {
        ".ROBLOSECURITY": cookie
    }
    while True:
        r = requests.get(url, cookies=cookies)
        if r.status_code == 429:
            print('API is ratelimited via cookie.')
            pass
        elif r.status_code == 200:
            print('Successfully sent a request.')
            print(r.text)
        else:
            print(r.text)
            pass

api = input('API: ')
proxy = input('PROXY Y/N: ')
if "Y" in proxy:
    cookie = input('COOKIE: ')
    threadcount = input('THREADS: ')
    for i in range(int(threadcount)):
        proxy = {
            "https": "https://" + next(ProxyPool)
        }
        threading.Thread(target=sendreqproxy, args=[api, cookie, proxy]).start()
if "N" in proxy:
    for i in cooks:
        threading.Thread(target=sendreqcookie, args=[api, i]).start()