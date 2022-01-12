#testing Threads
#Douglas J. Sheehan
#2022 Jan 12nd

import argparse
import time
import logging
from viewThreadsCLI import UserPrompts
from controller import blahblahblah


class CLIparams:
    def __init__(self):
        inputargs = argparse.ArgumentParser()
        inputargs.add_argument('-path',
            help='add path for files inside single quotes, use forward slash (near ?)')
        inputargs.add_argument('-hosts',action='store_true',
            help='specify csv file with host IP addresses to remote to') 
        inputargs.add_argument('-cmd',action='store_true',
            help='specify csv file with commands in order') 
        
        
        inputargs.add_argument('-tr',
            help='this is a testrouter or sharouter to generate/verify the sha256 secret works')     
        inputargs.add_argument('-log', action='store_true', 
            help='this will create a log file "Convert7to8_Log_datetime"')
        inputargs.add_argument('-logfile', help='same as log, but allows user to set filename')    
        inputargs.add_argument('-verbose',action='store_true',
            help='this will store extra detail in log and plaintext passwords \
                in datafile as well as hashes')

        inputargs.add_argument('-f', action='store',
            help='This option allowers user to specify a file for input or append.')

        inputargs.add_argument('-change', action='store_true', 
            help='when true(default), this flag will attempt to apply the change to router "')
        inputargs.add_argument('-verify', action='store_true', 
            help='when true(default), this flag will attempt to ssh into the router to verify \
                the changed password. It probably won\'t work with Tacacs or Radius')
        
        inputargs.add_argument('-ip',action='append',
            help='use this option to specify one or more ip addresses to change')

        cliargs = inputargs.parse_args()
        self.filename = cliargs.f
        #testing
        #self.filename = "testdata728.csv"
       
        self.pass7 = cliargs.p7
        self.cliDict={'IPADDRESS':cliargs.ip, 'TESTROUTER':cliargs.tr, 'LOG':cliargs.log , \
             'LOGFILE':cliargs.logfile ,'VERBOSE': cliargs.verbose, 'CHANGE':cliargs.change,'VERIFIY':cliargs.verify, 'FILENAME':cliargs.f ,'GUI':cliargs.gui}

       

def main():
    up=UserPrompts()
 
    ipaddylist=['192.168.1.1', '192.168.1.1,'192.168.1.1']
    #ipaddylist=['192.168.1.1]
    
if __name__ == '__main__':
    """ testing the main program """
    
    main() #call the main method
