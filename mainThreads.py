#testing Threads
#Douglas J. Sheehan
#2022 Jan 12nd

import argparse
import time
import logging
from viewThreadsCLI import UserPrompts
from controller-SSH import NetworkController


class CLIparams:
    def __init__(self):
        inputargs = argparse.ArgumentParser()
        inputargs.add_argument('-path',
            help='add path for files inside single quotes, use forward slash (near ?)')
        inputargs.add_argument('-hosts',action='store_true',
            help='specify csv file with host IP addresses to remote to') 
        inputargs.add_argument('-cmd',action='store_true',
            help='specify csv file with commands in order') 
        inputargs.add_argument('-ip',action='store_true',
            help='specify a single ip address to connect to') 
        
        #inputargs.add_argument('-log', action='store_true', 
        #    help='this will create a log file "Convert7to8_Log_datetime"')
        # inputargs.add_argument('-logfile', help='same as log, but allows user to set filename')    
        

        inputargs.add_argument('-outfile', action='store',
            help='This option allowers user to specify a file for saving output. filename in single quotes')

       

        cliargs = inputargs.parse_args()
        #self.filename = cliargs.f
        self.path=cliargs.path
        print(f"path is {self.path}")
        self.hosts=cliargs.hosts
        print(f"hosts is {self.hosts}")
        self.cmd=cliargs.cmd
        print(f"cmd {self.cmd}")
        self.ip=cliargs.ip
        print(f"single ip is {self.ip}")
        self.outfile=cliargs.outfile
        print(f"Outfile is {self.outfile}")
        

def main():
    """Main sets up the program, and hands over to controller for the rest"""
    options=CLIparams()
    print(f"{options} brought in from command line")
    up=UserPrompts()
 
    ipaddylist=['192.168.1.1', '192.168.1.1,'192.168.1.1']
    #ipaddylist=['192.168.1.1]
    #
    #  networkJob=NetworkController(up.uname, up.pword, devlist,cmdlist)
                
    print("Main Program complete")            
                
if __name__ == '__main__':
    """ testing the main program """
    
    main() #call the main method
