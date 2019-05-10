'''
Created on Mar 20, 2019

@author: subharad
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
from urllib.request import urlopen



from urllib import request as urlrequest

proxy_host = 'blrproxy.igate.com:8080'    # host and port of your proxy
url = 'https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'

import requests

proxies = {"https":"https://subharad:pswd@blrproxy.igate.com:8080"}

r = requests.get(url, proxies=proxies)

print(r.content)
