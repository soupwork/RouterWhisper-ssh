#testing Threads
#Douglas J. Sheehan
#2022 Jan 12nd
#
#This is the controller module, that handles the threads and comms using netmiko
#

from netmiko import ConnectHandler
import time
from datetime import date
import logging
import concurrent.futures
# viewSSH is only needed if testing
from viewSSH import UserPrompts

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
        self.today = date.today()


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
        hostname=net_connect.find_prompt()
        outfilename=hostname+ipaddy
        print(f"output filename will be {outfilename}")
        for cmd in cmdlist:
            cmdout += '\n' + cmd + '\n ' + net_connect.send_command(cmd) + '\n'
        #net_connect.send_command('wr mem')
        net_connect.disconnect()
        print(f"{cmdout}")

        # if outfilename exists, append to it, otherwise create it.
        with open(outfilename, 'a') as file_handler: 
            file_handler.write(f"{hostname}  {ipaddy} access date {self.today}")
            file_handler.write(cmdout)
            file_handler.write(f"{hostname}  {ipaddy} access date {self.today}")


        return(cmdout)
        #end NetworkConnection
        # 
        #     
if __name__ == '__main__':
    """ testing the controller """
    #devlist=['192.168.1.1', '192.168.1.1','192.168.1.1']
    devlist=['192.168.1.1']
    cmdlist=['sh ver', 'sh clock','show clock']
    up=UserPrompts()
    #create a new network controller
    networkJob=NetworkController(up.uname, up.pword, devlist,cmdlist)
    #networkJob.networkConnection(ipaddy='192.168.1.1')
    networkJob.threads()
