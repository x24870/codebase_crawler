import os, requests, datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen

AMI_GIT_URL = "https://megaracgit.ami.com"

cookies = {'__cfduid': 'd0269b8f63706340b350b4f38e06558301542807752',
'_gitlab_session': '21bbafaeb6b082a6642288c249ab074c',
'experimentation_subject_id': 'IjM2MDY5OTFiLTJjZjItNGYzNC05M2QyLTQ0M2U2MGU2MTI4MyI%3D--b7ecf780b7ab92f8190d72985743604a837789a6'}

def initial():
	date = datetime.datetime.now().strftime("%Y%m%d")
	

def get_clone_http_url(url):
	resp = requests.get(url, cookies=cookies)
	resp.raise_for_status()
	soup = BeautifulSoup(resp.text, 'html5lib')
	e = soup.find('a', {'data-clone-type': 'http'})
	return e['href']

def get_all_repository_link(url):
	url_lst = []
	resp = requests.get(url, cookies=cookies)
	resp.raise_for_status()
	soup = BeautifulSoup(resp.text, 'html5lib')
	e_lst = soup.find_all('a', {"class": "text-plain"})

	for e in e_lst:
		url_lst.append( get_clone_http_url(AMI_GIT_URL + e['href']) )

	return url_lst


if __name__ == '__main__':
	#get_all_repository_link(AMI_GIT_URL)
	initial()
