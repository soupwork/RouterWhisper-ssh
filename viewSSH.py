# Program to validate threads

# 2022 Jan 02nd
# 
# #Douglas J. Sheehan
#This is the CLI view. no GUI elements.

import getpass
import datetime
import os.path


class UserPrompts:
    def __init__(self):
        """set username and password"""
        print("init UserPrompts")
        self.uname = input("enter the username to authenticate to router/switch: ")
        self.pword=getpass.getpass("please enter password <hidden> :")
        print ("username is :", self.uname)


    #End Class UserPrompts
    
  

if __name__ == "__main__":
    """testing cli View for CiscoWhisper-SSH"""
    print ("CLI view is main")
    testview = UserPrompts()
    up = testview.getLoginID()
 

    

