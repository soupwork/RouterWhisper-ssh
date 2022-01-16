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

    def __init__(self, uname, pword, iplist, cmdlist, path ):
        """params username and password, device list, and commands list"""
        print("init Network Controller")
        self.uname = uname
        self.pword = pword
        print ("username is :", self.uname)
        self.iplist = iplist #device list list of IPs
        self.cmdlist = cmdlist #list of commands to use
        self.today = str(date.today())
        self.path=path


    def threads(self):
        
        starttime=time.perf_counter()

        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            connectdict = \
            {executor.submit(self.networkConnection, ipaddy):
                        ipaddy for ipaddy in self.iplist}
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
        hostname = hostname[:-1]  #trim the '#' off the end of the string
        outfilename=self.path + hostname + ipaddy[:-1] + '.txt'
        print(f"output filename will be {outfilename}")
        for cmd in self.cmdlist:
            cmdout += '\n' + cmd + '\n ' + net_connect.send_command(cmd)
        #net_connect.send_command('wr mem')
        net_connect.disconnect()
        print(f"{cmdout}")
        #outfilename = self.path + hostname + '1'
        # print (f" output file name is {outfilename}")
        # if outfilename exists, append to it, otherwise create it.
        with open(outfilename, 'a') as file_handler: 
            print(f"writing file  {outfilename}")
            delimiter = hostname + ipaddy + " access date " + self.today
            file_handler.write(delimiter)
            file_handler.write(cmdout)
            file_handler.write(delimiter)


        return(cmdout)
        #end NetworkConnection
        # 
        #     
if __name__ == '__main__':
    """ testing the controller """
    #iplist=['192.168.1.1', '192.168.1.1','192.168.1.1']
    iplist=['192.168.1.1']
    cmdlist=['sh ver', 'sh clock','show clock']
    up=UserPrompts()
    #create a new network controller
    networkJob=NetworkController(up.uname, up.pword, iplist,cmdlist)
    #networkJob.networkConnection(ipaddy='192.168.1.1')
    networkJob.threads()
