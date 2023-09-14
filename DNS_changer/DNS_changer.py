import os
import re
import numpy as np
import requests as req
from bs4 import BeautifulSoup as bs


def check(array):
    pattern = re.compile(r'^\d.*\d$')
    result = [item.text for item in array]
    result = [i for i in result if pattern.search(i)]
    return result


def get_DNS(arr, a):
    info = req.get(arr[a-1][0])
    response = bs(info.content, "html.parser")
    results = response.find_all(arr[a-1][1], attrs={"class": arr[a-1][2]})
    return results


resources = np.loadtxt('DNS_changer.txt', dtype=str)
resources = [item.split(',') for item in resources]

print('''1. Select\n2. Add''')
x = int(input('--: '))


if x == 1:
    print('''\n1. Electro\n2. Shekan''')
    a = int(input('--: '))
    DNSs = check(get_DNS(resources, a))
    os.system(f'netsh interface ip set dns name="Wi-Fi" static {DNSs[0]}')
    os.system(f'netsh interface ip add dns name="Wi-Fi" {DNSs[1]} index=2')


if x == 2:
    P = input('Enter Preferred DNS : ')
    A = input('Enter Alternate DNS : ')
    os.system(f'netsh interface ip set dns name="Wi-Fi" static {P}')
    os.system(f'netsh interface ip add dns name="Wi-Fi" {A} index=2')











