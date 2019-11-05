import os
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

AMI_GIT_URL = "https://megaracgit.ami.com"

cookies = {'__cfduid': 'd0269b8f63706340b350b4f38e06558301542807752',
'_gitlab_session': '21bbafaeb6b082a6642288c249ab074c',
'experimentation_subject_id': 'IjM2MDY5OTFiLTJjZjItNGYzNC05M2QyLTQ0M2U2MGU2MTI4MyI%3D--b7ecf780b7ab92f8190d72985743604a837789a6'}

def get_all_repository_link(url):
	# resp = urlopen(url)
	# html = BeautifulSoup(resp)
	# print(html)
	resp = requests.get(url, cookies=cookies)
	resp.raise_for_status()
	soup = BeautifulSoup(resp.text, 'html5lib')
	print(resp.text)
	#return soup

get_all_repository_link(AMI_GIT_URL)
