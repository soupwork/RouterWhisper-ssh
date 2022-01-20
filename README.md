# CiscoWhisper-SSH
Python Program to ssh into cisco devices
--------------------
This is the start of a framework for a program to SSH into cisco Devices.
It could be used as-is, or could be built out into a Model-View-Controller OOP Design Pattern.

run " python mainSSH.py --help " to see all the command line options and descriptions.

IP Address(es) can be brought in as a single IP, a list of IP's, or as a csv.

Router command(s) can be brought in as a single command, or as a csv.

Results are stored in a single text file for each device

The framework was meant to be easy for the network team to extend upon and make it their own.
This could be fun and rewarding. With many smiles resulting from the reduction in manual work and multiple handling.

doug. 2022 Jan 17th.

Other Future Thoughts

argparse used to accept arguments passed in to the program at run time.
    
Since the program lends itself to Object Oriented Programming (OOP)
  typically, there is are at least three files, one for the view, one for the model, one for the controller.
  a model would be a class that contains data and methods (functions)
  each device would have a class instance created based on the model 
  
While not really consistent with MVC, I like to have a Main file that handles setting up everything.
  I have a separate controller that manages comms to the router through netmiko.
  this keeps the clutter from argparse out of the controller.
  
Kirk Byers has awesome documentation
https://github.com/ktbyers/netmiko/blob/develop/EXAMPLES.md
