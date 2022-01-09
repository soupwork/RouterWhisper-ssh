#testing Threads
#Douglas J. Sheehan
#2022 Jan 06nd

from viewThreadsCLI import UserPrompts
from netmiko import ConnectHandler
from getpass import getpass
import time
import logging
import concurrent.futures


def networkConnection(addy,up):
    user,passwd=(up)
    
    ciscorouter = {
    "device_type": "cisco_ios",
    "host": addy,
    "username": user,
    "password": passwd,
    }

    net_connect = ConnectHandler(**ciscorouter)
    
    net_connect.enable()
    #shrun=net_connect.send_command('show tech')
    show=net_connect.send_command('show ip int brief')
    net_connect.send_command('wr mem')
    net_connect.disconnect()
    print(f"{show}")
    return(show)
    #end NetworkConnection

def main():
    ipaddylist=['172.21.12.241', '172.21.12.242','172.21.12.251']
    #ipaddylist=['172.21.12.241']
    starttime=time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        connectdict = {executor.submit(networkConnection, ipaddy, up): ipaddy for ipaddy in ipaddylist}
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
    #up=('PyAdmin', 'password-here')
    main() #call the main method