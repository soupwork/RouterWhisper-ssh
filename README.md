# CiscoWhisper-SSH
Python Program to ssh into cisco devices
--------------------
This is the start of a framework for a program to SSH into cisco Devices.
It could be used as-is, or could be built out into a Model-View-Controller OOP Design Patter.

The list of devices is presently a simple list in the program, but it would be easy to bring in an external list from a file, such as a csv.

Presently there is only one command sent to the device. a list could be read in, possibly from a csv. 

Results could be stored in either a csv file, text file, or a json dictionary, for example.

The framework was meant to be easy for the network team to extend upon and make it their own.
This could be fun and rewarding. With many smiles resulting from the reduction in manual work and multiple handling.

doug. 2022 Jan 10th.

Other Future Thoughts

argparse can accept arguments passed in to the program at run time.
  one use would be to specify a 'filepath' for all the files
  one use would be to specify a 'commandfile' that lists the commands to be ran
  one use would be to specify a 'host list' -a list of ip's to ssh into
  
Since the program lends itself to Object Oriented Programming (OOP)
  typically, there is are at least three files, one for the view, one for the model, one for the controller.
  a model would be a class that contains data and methods (functions)
  each device would have a class instance created based on the model 
  
While not really consistent with MVC, I like to have a Main file that handles setting up everything.
  I have a separate controller that manages comms to the router through netmiko.
  this keeps the clutter from argparse out of the controller.
  
