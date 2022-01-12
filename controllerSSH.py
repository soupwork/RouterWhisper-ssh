#testing Threads
#Douglas J. Sheehan
#2022 Jan 12nd
#
#This is the controller module, that handles the threads and comms using netmiko
#

from netmiko import ConnectHandler
import time
import logging
import concurrent.futures
from viewThreadsCLI import UserPrompts

class NetworkController: 
    """This a class for Netmiko Connections and Threads"""

    def __init__(self, uname, pword, devlist, cmdlist ):
        """params username and password, device list, and commands list"""
        print("init Network Controller")
        self.uname = uname
        self.pword = pword
        print ("username is :", self.uname)
        self.devlist = devlist #device list list of IPs
        self.cmdlist = cmdlist #list of commands to use

    def threads(self):
        
        starttime=time.perf_counter()

        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            connectdict = \
            {executor.submit(self.networkConnection, ipaddy):
                        ipaddy for ipaddy in self.devlist}
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

        #end Threads

    def networkConnection(self,ipaddy):
        
        cmdout=''
        ciscorouter = {
        "device_type": "cisco_ios",
        "host": ipaddy,
        "username": self.uname,
        "password": self.pword,
        }

        net_connect = ConnectHandler(**ciscorouter)
        
        net_connect.enable()
        #
        for cmd in cmdlist:
            cmdout += '\n' + cmd + '\n ' + net_connect.send_command(cmd) + '\n'
        #net_connect.send_command('wr mem')
        net_connect.disconnect()
        print(f"{cmdout}")
        return(cmdout)
        #end NetworkConnection
        # 
        #     
if __name__ == '__main__':
    """ testing the controller """
    #devlist=['10.94.32.122', '10.94.32.121','10.94.32.120']
    devlist=['10.94.32.122']
    cmdlist=['sh ver', 'sh clock','show clock']
    up=UserPrompts()
    #create a new network controller
    networkJob=NetworkController(up.uname, up.pword, devlist,cmdlist)
    #networkJob.networkConnection(ipaddy='172.21.12.241')
    networkJob.threads()
