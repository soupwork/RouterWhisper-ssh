#testing Threads
#Douglas J. Sheehan
#2022 Jan 12nd

import argparse
import time
import logging
from viewSSH import UserPrompts
from controllerSSH import NetworkController


class CLIparams:
    def __init__(self):
        """set up initial switches/options to bring in from command line"""
        inputargs = argparse.ArgumentParser()
        inputargs.add_argument('-path',
            help='add path for files inside single quotes, use forward slash (near ?)')
        inputargs.add_argument('-ip',action='store_true',
            help='specify a single ip address to connect to') 
        inputargs.add_argument('-iplist',action='store_true',
            help='specify csv file with host IP addresses to remote to') 
        inputargs.add_argument('-cmd',action='store_true',
            help='specify single command to run on router') 
        inputargs.add_argument('-cmdlist',action='store_true',
            help='specify csv file with commands in order')     

        inputargs.add_argument('-test',action='store_true',
            help='load and run pre-defined test parameters') 
        self.path='e:/'        
        self.iplist=['']    
        self.cmdlist=['sh clock']
        self.outfile='outfile.txt'
        self.showOptions()
        
        #inputargs.add_argument('-log', action='store_true', 
        #    help='this will create a log file "Convert7to8_Log_datetime"')
        # inputargs.add_argument('-logfile', help='same as log, but allows user to set filename')    

        inputargs.add_argument('-outfile', action='store',
            help='This option allowers user to specify a file for saving output. filename in single quotes')
       
        cliargs = inputargs.parse_args()

        # cli argument processing
        if (cliargs.test):
            self.settest()
        else:    
            #self.filename = cliargs.f
            if (cliargs.path):
                self.path=cliargs.path

            if (cliargs.ip): #single IP in cli arguments
                self.ip=list(cliargs.ip)
                print(f"single IP {self.iplist}")
            elif (cliargs.iplist): #filename in cli arguments
                self.ipfile=cliargs.iplist
                filename = self.path + self.ipfile
                print(f"opening iplist {filename}")
                self.iplist=self.fileLoadList(filename,self.iplist)

            if (cliargs.cmd): #single command in cli arguments
                self.cmdlist=list(cliargs.cmd)
                print(f"single cmd {self.cmdlist}")
            elif (cliargs.cmdlist): #filename in cli arguments
                self.cmdfile=cliargs.cmdlist
                filename = self.path + self.cmdfile
                print(f"opening cmdlist {self.filename}")
                self.cmdlist=self.fileLoadList(filename,self.cmdlist)

            if (cliargs.outfile): #filename in cli arguments
                self.outfile=cliargs.outfile
            else:
                self.outfile='SSHout.txt'

        self.showOptions()
       


    def fileLoadList (self,filename,listname):
        """this takes in the filename, and loads the list"""   
        print("inside file load list")
        with open(filename, 'r') as file_handler: #open as read is the default
            for line in file_handler:
                listname.append(line)

        print(f"file load list {listname}") 
        return(listname)

    def settest(self):
        self.path='e:/CiscoWhisper-SSH/'
        self.iplist=['172.21.12.241']    
        self.cmdlist=['sh clock']
        self.outfile='testSSHout.txt'




    def showOptions(self):
        """for testing, display the options"""
        print("--- for testing, display options ---")
        print(f"path is {self.path}")
        print(f"IP Addresses are {self.iplist}")
        print(f"Commands list is {self.cmdlist}")
        print(f"Outfile is {self.outfile}")




def main():
    """Main sets up the program, and hands over to controller for the rest"""
    print('inside main')
    options=CLIparams()
    print(f"new settings {options.showOptions()}")
    up=UserPrompts()
    
    #
    ### Testing cli parameters ###
    # run from terminal window
    # d:/DougsProgs/RouterWhisper-ssh-main/mainSSH.py -path 'e:/CiscoWhisper-SSH/' -iplist 'ipaddys.csv' -cmdlist 'commands.csv'
     # d:/DougsProgs/RouterWhisper-ssh-main/mainSSH.py -path 'e:/CiscoWhisper-SSH/' 
     # d:/DougsProgs/RouterWhisper-ssh-main/mainSSH.py -path 'e:/CiscoWhisper-SSH/' -ip '10.0.0.2'
      # d:/DougsProgs/RouterWhisper-ssh-main/mainSSH.py -cmd 'show clock'
       # d:/DougsProgs/RouterWhisper-ssh-main/mainSSH.py -ip '10.0.0.1'
    # Run network job to launch the controller
    #  networkJob=NetworkController(up.uname, up.pword, devlist,cmdlist)
                
    print("Main Program complete")            
                
if __name__ == '__main__':
    """ testing the main program """
    print('__main__')

    main() #call the main method
