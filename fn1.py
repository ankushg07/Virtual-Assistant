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
su_pas = raw_input("PLease entee your password for sudo ")
su_pas=su_pas.strip()

#fn to find the path of folder

def path_finder(var):
	if (var in common.keys()):
		path = common[var]
	else:
		cmd = 'echo ' +su_pas+ "| sudo -S find / -iname  '" +var+ "'"
		out = commands.getoutput(cmd)
		#print out
		out = out.split()
		if(len(out) > 1):
			print("Please choose the Folder/File from the list")
			x=1
			for i in out:
				print x, i
				x+=1
			choice = int(raw_input("Enter the number of choice ") )
			path = out[choice-1]
		elif(len(out) == 1):
			path = out[0]
		else:
			path = ""
	return path




# ***** main fns *****

inp = raw_input()
inp=inp.lower()
inp = inp.split(" ")


# ***** Fn 1 ls command == open folder **********

if(inp[0] == 'open' and inp[1] =='folder'):
	var = inp[2]
	path = path_finder(var)
	
	if(path != ""):
		cmd = commands.getoutput("ls "+path)
	else:
		cmd = "No such Directory found !"
	print cmd 

# ***** Fn 2 cat command == open file **********
if(inp[0] == 'open' and inp[1] == 'file' ):
	#format : open file NAME in FOLDER
	if(len(inp)>3 and inp[3] == 'in'):
		#finding folder
		path = path_finder(inp[4])
		if (path == ""):
			print "Folder "+inp[4]+" not found "
		else:
			cmd = commands.getoutput("cat " +path+ "/"+inp[2])
			print cmd
	else:
		path = path_finder(inp[2])
		if(path == ""):
			print "File "+inp[2]+" not found !"
		else:
			cmd = commands.getoutput("cat "+path )
			print cmd 
	choice = raw_input("Do you want to edit the file [yes/no]?  ")
	if(choice == 'yes'):
		status = os.system("gedit "+path+"/"+inp[2])

# ***** Fn 3 create a new file 2 **********
if(inp[0] == 'create' and inp[1]== 'file'):
	if(len(inp) == 5):
		path = path_finder(inp[4])
	else:
		var = raw_input("please enter the name of Directory for new file  ")
		path = path_finder(var)
	if(path == ""):
	 	print "No such Directory found !"
	else:
	 	cmd = commands.getoutput("touch "+path+"/"+inp[2])
	 	choice = raw_input("Do you want to edit the file [yes/no]? ")
	 	if(choice == 'yes'):
	 		status = os.system("gedit "+path+"/"+inp[2])
