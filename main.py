#! /usr/bin/python3

import urllib2
import json
import requests

#http://api.wolframalpha.com/v2/query?appid=6QPQYJ-LHQPAEYTWW&input=population%20france
#  &output=json&format=plaintext&podtitle=Result


def main():
	url = "http://api.wolframalpha.com/v2/query?appid=6QPQYJ-LHQPAEYTWW&input="
	url_end = "&output=json&format=plaintext&podtitle=Result"
	operator = {'+':'%2B', '-':'%2D', '*':'%2A', '/':'%2F', '%':'%25', '^':'%5E','!':'%21', '$':'%24', '&':'%26', '(':'%28', ')':'%29', '{':'%7B','}':'%7D', '[':'%5B', ']':'%5D', '#':'%23'}
	print "HELLO !!"
	print "How may I help you"
	print "Please enter your query or enter @ to exit"
	inp = raw_input()
	while(inp != "@"):
		url_inp = ""
		word = inp.split(" ")
		for x in word:
			if(x.isalnum()):
				url_inp += x
			else:
				url_inp += operator[x]
			url_inp += '+'
		result_json = requests.get(url+url_inp+url_end)
		result = json.loads(result_json.text)
		if(result['queryresult']['success'] == 'False'):
			print "Query Failed"
		else:
			print result['queryresult']['pods'][0]['subpods'][0]['plaintext']


		inp = raw_input()


if __name__ == '__main__':
	main()