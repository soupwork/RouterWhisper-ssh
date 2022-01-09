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
        self.username = input("enter the username to authenticate to router/switch: ")
        self.pword=getpass.getpass("please enter password <hidden> :")
        print ("username is :", self.username)


    def getLoginID(self):
       """returns username and password"""

       return(self.username,self.pword)
    #End Class UserPrompts
    
  

if __name__ == "__main__":
    #up
    print ("CLI view is main")
    testview = UserPrompts()
    up = testview.getLoginID()
    print ('up is ', up)
    #print ('password is ', pword)
    # print("pwd is ", os.getcwd())
    
    #print(viewchoice)