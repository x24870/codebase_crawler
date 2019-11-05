import os
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

AMI_GIT_URL = "https://megaracgit.ami.com"

def get_all_repository_link():
	resp = urlopen(AMI_GIT_URL)
	html = BeautifulSoup(resp)
	print(html)

get_all_repository_link()
