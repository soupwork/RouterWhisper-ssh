#testing Threads
#Douglas J. Sheehan
#2022 Jan 11nd
#import sys
#sys.path.insert(1, 'c:/program files/python37/lib/site-packages/')

from netmiko import ConnectHandler
from getpass import getpass
import time
import logging
import concurrent.futures
from viewThreadsCLI import UserPrompts


def networkConnection(addy,uname,passwd):
    
    
    ciscorouter = {
    "device_type": "cisco_ios",
    "host": addy,
    "username": uname,
    "password": passwd,
        #multiply delay factors by 4
    "global_delay_factor": 4    
    }

    net_connect = ConnectHandler(**ciscorouter)
    
    net_connect.enable()
    #
    show=net_connect.send_command('show ip int brief')
    #net_connect.send_command('wr mem')
    net_connect.disconnect()
    print(f"{show}")
    return(show)
    #end NetworkConnection

def main():
    ipaddylist=['10.94.32.122', '10.94.32.121','10.94.32.120']
    #ipaddylist=['10.94.32.122']
    starttime=time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        connectdict = {executor.submit(networkConnection, ipaddy, up.username, up.pword):
                       ipaddy for ipaddy in ipaddylist}
        for future in concurrent.futures.as_completed(connectdict):
            print("connect dict IP Addy is ", connectdict[future])
            dataresult = connectdict[future]
            try:
                data = future.result()
            except Exception as exc:
                print(f"{connectdict[future]} generated exception: {exc}") 
            else:
                print(f"{connectdict[future]} \n {data}")       

   
    endtime=time.perf_counter()    
    elapsedtime=endtime-starttime
    print(f"total time is {elapsedtime} seconds")
if __name__ == '__main__':
    
    up=UserPrompts()
    #print (up.username, ' is the username before calling main')
    #print(up.pword, ' is the word before calling main')
    #x= input ('any key to continue')
    #up=('PyAdmin', 'password-here')
    main() #call the main method
