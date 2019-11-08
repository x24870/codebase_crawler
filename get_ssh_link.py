import os, requests, datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen

### URL pattern
# https://megaracgit.ami.com/?non_archived=true&page=2&sort=created_desc
AMI_GIT_URL = 'https://megaracgit.ami.com/'
non_arch = 'non_archived=true'
page = 'page='
sort = 'sort=created_desc'

REC_PATH = 'record'

cookies = {'__cfduid': 'd0269b8f63706340b350b4f38e06558301542807752',
'_gitlab_session': '21bbafaeb6b082a6642288c249ab074c',
'experimentation_subject_id': 'IjM2MDY5OTFiLTJjZjItNGYzNC05M2QyLTQ0M2U2MGU2MTI4MyI%3D--b7ecf780b7ab92f8190d72985743604a837789a6'}

def initial():
	if not os.path.exists(REC_PATH):
		os.makedirs(REC_PATH)

def get_record_path():
	date = datetime.datetime.now().strftime("%Y%m%d")
	return os.path.join(REC_PATH, date+'.txt')
	

def check_next_page(soup):
	e_next_btn = soup.find('a', {'rel': 'next'})
	if e_next_btn['href'] == '#':
		return False
	return True

def get_clone_http_url(url):
	resp = requests.get(url, cookies=cookies)
	resp.raise_for_status()
	soup = BeautifulSoup(resp.text, 'html5lib')
	e = soup.find('a', {'data-clone-type': 'http'})
	print(e['href'])
	return e['href']

def get_page_repository_link(url):
	url_lst = []
	resp = requests.get(url, cookies=cookies)
	resp.raise_for_status()
	soup = BeautifulSoup(resp.text, 'html5lib')
	e_lst = soup.find_all('a', {"class": "text-plain"})

	for e in e_lst:
		url_lst.append( get_clone_http_url(AMI_GIT_URL + e['href']) )

	next_page = check_next_page(soup)

	return url_lst, next_page

def save_all_link(f_path):
	https_link_lst = []

	for page_num in range(5, 10):#TODO: change to 1
		print('--------------------- Page {} ---------------------'.format(page_num))
		url = '{}/?{}&{}{}&{}'.format(AMI_GIT_URL, non_arch, page, page_num, sort)
		print('URL: ' + url)
		one_page_link_lst ,next_page = get_page_repository_link(url)
		https_link_lst.extend(one_page_link_lst)
		if not next_page:
			break

	with open(f_path, 'w+') as f:
		f.write( "\n".join(link for link in https_link_lst) )
	print('*** Saved all clone https links successully!: '.format(f_path))
	

def clone_all_repositiry(f_path):
	url_lst = []
	with open(f_path, 'r') as f:
		url_lst = f.readlines()
	print(url_lst)

if __name__ == '__main__':
	initial()
	save_all_link( get_record_path() )
	clone_all_repositiry( get_record_path() )

		
	
