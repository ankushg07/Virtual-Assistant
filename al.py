#! /usr/bin/python

import urllib2
import urllib
import json
import requests
import os
import sys
import commands
from multiprocessing import Process
import webbrowser
from bs4 import BeautifulSoup
#http://api.wolframalpha.com/v2/query?appid=6QPQYJ-LHQPAEYTWW&input=population%20france
 # &output=json&format=plaintext&podtitle=Result
#fn to find the path of folder
#getting the name of user logged in fro his home folder


usr=commands.getoutput("whoami")
usr = usr.strip()
	#creating dictionary for common folders


tts_path = "/home/"+usr+"/tts.txt"
status = os.system("touch "+tts_path)


common={'desktop' : '/home/'+usr+'/Desktop' , 'documents' : '/home/'+usr+'/Documents' , 'download' : '/home/'+usr+'/Downloads'}
#sudo pass
os.system('echo "Please enter your password for sudo " > '+tts_path)
os.system("festival --tts "+tts_path)


su_pas = raw_input("Please enter your password for sudo ") 

su_pas=su_pas.strip()
def path_finder(var):
	if (var in common.keys()):
		path = common[var]
	else:
		cmd = 'echo ' +su_pas+ "| sudo -S find / -iname  '" +var+ "'"
		out = commands.getoutput(cmd)
		#print out
		out = out.split()
		if(len(out) > 1):
			os.system('echo "Please choose the Folder or File from the list " > '+tts_path)
			os.system("festival --tts "+tts_path)  
			
			print("Please choose the Folder/File from the list")
			x=1
			for i in out:
				print x, i
				x+=1

			os.system('echo "Enter the number of choice  " > '+tts_path)
			os.system("festival --tts "+tts_path)  	
			choice = int(raw_input("Enter the number of choice ") )
			path = out[choice-1]
		elif(len(out) == 1):
			path = out[0]
		else:
			path = ""
	return path





def main():

	url = "http://api.wolframalpha.com/v2/query?appid=6QPQYJ-LHQPAEYTWW&input="
	url_end = "&output=json&format=plaintext"
	operator = {'+':'%2B', '-':'%2D', '*':'%2A', '/':'%2F', '%':'%25', '^':'%5E','!':'%21', '$':'%24', '&':'%26', '(':'%28', ')':'%29', '{':'%7B','}':'%7D', '[':'%5B', ']':'%5D', '#':'%23'}

	os.system('echo "HELLO MASTER  " > '+tts_path)
	os.system("festival --tts "+tts_path) 		
	print "HELLO !!"
	os.system('echo "How may I help you  " > '+tts_path)
	os.system("festival --tts "+tts_path) 		
	
	print "How may I help you"
	os.system('echo "Please enter your query " > '+tts_path)
	os.system("festival --tts "+tts_path) 		
	print "Please enter your query or enter @ to exit"
	inp = raw_input(">\t")
	while(inp != "@"):
		inp=inp.lower()
		inp = inp.split(' ')

		# ***** Fn 1 ls command == open folder **********

		if(inp[0] == 'open' and inp[1] =='folder'):
			var = inp[2]
			path = path_finder(var)
			
			if(path != ""):
				cmd = commands.getoutput("ls "+path)
			else:
				cmd = "No such Directory found !"
			print cmd 
			os.system('echo "'+cmd+'" > '+tts_path)
			os.system("festival --tts "+tts_path) 		
			

		# ***** Fn 2 cat command == open file **********
		elif(inp[0] == 'open' and inp[1] == 'file' ):
			#format : open file NAME in FOLDER
			if(len(inp)>3 and inp[3] == 'in'):
				#finding folder
				path = path_finder(inp[4])
				if (path == ""):
					print "Folder "+inp[4]+" not found "
					os.system('echo "Folder Not found" > '+tts_path)
					os.system("festival --tts "+tts_path) 		
			
				else:
					cmd = commands.getoutput("cat " +path+ "/"+inp[2])
					print cmd
					# ask if wanted to read the content 
					os.system('echo "Do you want me to read teh file " > '+tts_path)
					os.system("festival --tts "+tts_path) 	

					ask = raw_input("Do you want me to read the file [yes/no]  : ")	
					if(ask == 'yes'):
						os.system('echo "'+cmd+'" > '+tts_path)
						os.system("festival --tts "+tts_path) 		
			
			else:
				path = path_finder(inp[2])
				if(path == ""):
					print "File "+inp[2]+" not found !"
					os.system('echo "File Not found" > '+tts_path)
					os.system("festival --tts "+tts_path) 		
			
				else:
					cmd = commands.getoutput("cat "+path )
					print cmd
							# ask if wanted to read the content 
					os.system('echo "Do you want me to read teh file " > '+tts_path)
					os.system("festival --tts "+tts_path) 	

					ask = raw_input("Do you want me to read the file [yes/no]  : ")	
					if(ask == 'yes'):
						os.system('echo "'+cmd+'" > '+tts_path)
						os.system("festival --tts "+tts_path) 		
			
			
			os.system('echo "Do you want to edit the file " > '+tts_path)
			os.system("festival --tts "+tts_path) 		

			choice = raw_input("Do you want to edit the file [yes/no]?  ")
			if(choice == 'yes'):
				status = os.system("gedit "+path+"/"+inp[2])

		# ***** Fn 3 create a new file 2 **********
		elif(inp[0] == 'create' and inp[1]== 'file'):
			if(len(inp) == 5):
				path = path_finder(inp[4])
			else:

				os.system('echo "please enter the name of Directory " > '+tts_path)
				os.system("festival --tts "+tts_path) 		

				var = raw_input("please enter the name of Directory for new file  ")
				path = path_finder(var)
			if(path == ""):

				os.system('echo "Folder Not found" > '+tts_path)
				os.system("festival --tts "+tts_path) 		

			 	print "No such Directory found !"
			else:
			 	cmd = commands.getoutput("touch "+path+"/"+inp[2])
			 	choice = raw_input("Do you want to edit the file [yes/no]? ")
			 	if(choice == 'yes'):
			 		status = os.system("gedit "+path+"/"+inp[2])

		#music and videos
		elif(inp[0] == 'play' and (inp[1] == 'song' or inp[1] == 'video') ):
			song_url1 = ""
			for it in inp[2:len(inp)]:

				song_url1+=it
				song_url1+=' '
			query = urllib.quote(song_url1)
			song_url = "https://www.youtube.com/results?search_query=" + query
			response = urllib2.urlopen(song_url)
			html = response.read()
			soup = BeautifulSoup(html,"lxml")
			vid = soup.find(attrs={'class':'yt-uix-tile-link'})
			webbrowser.open("https://www.youtube.com"+vid['href'] )
    
		# web serach and use of wolfame api 
		else:
			url_inp = ""
			word = inp
			for x in word:
				if(x.isalnum()):
					url_inp += x
				else:
					url_inp += operator[x]
				url_inp += '+'
			result_json = requests.get(url+url_inp+url_end+"&podtitle=Result")
			result = json.loads(result_json.text)
			if(result['queryresult']['success'] == 'False'):
				print "Query Failed"
				os.system('echo "Query Failed  " > '+tts_path)
				os.system("festival --tts "+tts_path)  	

			else:
				try:
					res = result['queryresult']['pods'][0]['subpods'][0]['plaintext']
					print res
					os.system('echo "'+res+'" > '+tts_path)
					os.system("festival --tts "+tts_path)
				except KeyError:
					if(inp[0] == 'who'  and inp[1] == 'is'):
						result_json = requests.get(url+url_inp+url_end+"&podtitle=Wikipedia+summary")
						result = json.loads(result_json.text)
						res = result['queryresult']['pods'][0]['infos']['links']['url']
						webbrowser.open(res)
					else:
						result_json = requests.get(url+url_inp+url_end+"&podtitle=Decimal+approximation")
						result = json.loads(result_json.text)
						#print result
						res = result['queryresult']['pods'][0]['subpods'][0]['plaintext']
						print res
						

											
				  	


		inp = raw_input(">\t")


if __name__ == '__main__':
	main()