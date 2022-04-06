# openvpn_as-logcrash
Vulnerability in openvpn_as that causes logs to quit syncing with sqlite  
Confirmed for openvpn-as 2.8.5 - 2.10.2   
*Disclosed to openvpn on Nov 7th 2021*

Issue: Logs will no longer sync with sqlite by sending many characters in the username field of the login post request causing a crash of pyovpn.log.logworker  

Logs will continue to populate in /var/log/openvpnas.log however the admin webgui will no longer show them as they will not be sent to sqlite after the post request  
It is possible to restart the pyovpn.log.logworker process by running ./usr/local/openvpn_as/scripts/sacli stop, and then start  
 

Usage: python3 oaslogwrk.py http(s)://openvpninstance.address.com
