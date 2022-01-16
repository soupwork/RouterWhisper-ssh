#testing Threads
#Douglas J. Sheehan
#2022 Jan 12nd

import argparse

from viewSSH import UserPrompts
from controllerSSH import NetworkController


class CLIparams:
    def __init__(self):
        """set up initial switches/options to bring in from command line
            single dash is short option (single letter), double dash is long option 
            action='store_true' is a flag, action='store' is default for passed param """
        
          #Initialize possible parameters
        self.path='e:/'        
        self.iplist=[]    
        self.cmdlist=['sh clock']
        self.outfile='outfile.txt'
        self.showOptions()
        self.test=False
        
        inputargs = argparse.ArgumentParser()
        inputargs.add_argument('--path',action='store', 
            help='add path for files inside single quotes, use forward slash (near "?")')
        inputargs.add_argument('--ip',action='store',
            help='specify a single ip address to connect to') 
        inputargs.add_argument('--iplist',action='store',
            help='specify csv file with host IP addresses to remote to') 

        inputargs.add_argument('--cmd',action='store',
            help='specify single command to run on router') 
        inputargs.add_argument('--cmdlist',action='store',
            help='specify csv file with commands in order') 

        inputargs.add_argument('--outfile',action='store',
            help='Set output filename ') 
        inputargs.add_argument('-t','--test',action='store_true',
            help='load and run pre-defined test parameters') 

              
        #inputargs.add_argument('-log', action='store_true', 
        #    help='this will create a log file "Convert7to8_Log_datetime"')
        # inputargs.add_argument('-logfile', help='same as log, but allows user to set filename')    


      
        self.cliargs = inputargs.parse_args()
        print(f"command line arguments are {self.cliargs}")
  
    
    def setargs(self,cliargs):
        # cli argument processing
        if (cliargs.test):
            self.settest()
        else:    
            #self.filename = cliargs.f
            if (cliargs.path):
                self.path=cliargs.path

            if (cliargs.ip): #single IP in cli arguments
                self.iplist=[cliargs.ip]
            elif (cliargs.iplist): #filename in cli arguments
                self.ipfile=cliargs.iplist
                filename = self.path + self.ipfile
                self.iplist=self.fileLoadList(filename,self.iplist)

            if (cliargs.cmd): #single command in cli arguments
                self.cmdlist=[cliargs.cmd]
            elif (cliargs.cmdlist): #filename in cli arguments
                self.cmdfile=cliargs.cmdlist
                self.filename = self.path + self.cmdfile
                self.cmdlist=self.fileLoadList(self.filename,self.cmdlist)

            if (cliargs.outfile): #filename in cli arguments
                self.outfile=cliargs.outfile
            else:
                self.outfile='SSHout.txt'

        # self.showOptions()
       
       
    def fileLoadList (self,filename,listname):
        """this takes in the filename, and loads the list"""   
        with open(filename, 'r') as file_handler: #open as read is the default
            for line in file_handler:
                linelist=line.split(',')
                for element in linelist:
                    listname.append(element)

        return(listname)

    def settest(self):
        # self.path='e:/CiscoWhisper-SSH/'
        # self.iplist=['172.21.12.241']    
        # self.cmdlist=['sh clock']
        # self.outfile='testSSHout.txt'

        self.path='e:/CiscoWhisper-SSH/'
        ipfile=self.path + 'ipaddys.csv'
        self.iplist=self.fileLoadList(ipfile,self.iplist)  
        cmdfile=self.path + 'commands.csv'
        self.cmdlist=self.fileLoadList(cmdfile,self.cmdlist)
        self.outfile='testSSHout.txt'


    def showOptions(self):
        """for testing, display the options"""
        print("--- for testing, display options ---")
        print(f"path is {self.path}")
        print(f"IP Addresses are {self.iplist}")
        print(f"Commands list is {self.cmdlist}")
        print(f"Outfile is {self.outfile}")
## End Class CLIparams



def main():
    """Main sets up the program, and hands over to controller for the rest"""
    # print('inside main')
    options=CLIparams()
    options.setargs(options.cliargs)
    print("new settings")
    options.showOptions()
    up=UserPrompts()
    
    #
    ### Testing cli parameters ###
    # run from terminal window
    # d:/DougsProgs/RouterWhisper-ssh-main/mainSSH.py -path 'e:/CiscoWhisper-SSH/' -iplist 'ipaddys.csv' -cmdlist 'commands.csv'
     # d:/DougsProgs/RouterWhisper-ssh-main/mainSSH.py -path 'e:/CiscoWhisper-SSH/' 
     # d:/DougsProgs/RouterWhisper-ssh-main/mainSSH.py -path 'e:/CiscoWhisper-SSH/' -ip '10.0.0.2'
      # d:/DougsProgs/RouterWhisper-ssh-main/mainSSH.py -cmd 'show clock'
       # d:/DougsProgs/RouterWhisper-ssh-main/mainSSH.py -ip '10.0.0.1'
    # Run network job to launch the controller by networkJob.threads()
    networkJob=NetworkController(up.uname, up.pword, options.iplist,options.cmdlist,options.path)
    networkJob.threads()

    print("Main Program complete")            
                
if __name__ == '__main__':
    """ testing the main program """
    

    main() #call the main method
