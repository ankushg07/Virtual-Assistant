#! /usr/bin/python
import sys
import commands
import os

#getting the name of user logged in fro his home folder
usr=commands.getoutput("whoami")
usr = usr.strip()

#creating dictionary for common folders
common={'desktop' : '/home/'+usr+'/Desktop' , 'documents' : '/home/'+usr+'/Documents' , 'download' : '/home/'+usr+'/Downloads'}
#sudo pass
su_pas = raw_input("PLease entee your password for sudo")
su_pas=su_pas.strip()
inp = raw_input()
inp=inp.lower()
inp = inp.split(' ')


# ***** Fn 1 ls command == open folder **********

if(inp[0] == 'open' and inp[1] =='folder'):
	var = inp[2]
	#check if exixst in common 
	if (var in common.keys()):
		path = common[var]
	else:
		cmd = 'echo ' +su_pas+ "| sudo -S find / -iname  '" +var+ "'"
		out = commands.getoutput(cmd)
		#print out
		out = out.split()
		if(len(out) > 1):
			print("Please choose the folder from the list")
			x=1
			for i in out:
				print x,i
				x+=1
			choice = raw_input("Enter the number of choice ")
			path = out[choice-1]
		else:
			path = out[0]

	cmd = commands.getoutput("ls "+path)
	print cmd 
