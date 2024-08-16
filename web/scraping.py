import requests
from bs4 import BeautifulSoup


r = requests.get('http://web-16.challs.olicyber.it/')
html_doc = r.text
soup = BeautifulSoup(html_doc, 'html.parser')
links = soup.find_all('a')
checked_links = []
while len(links) != 0:
	link = links.pop(0)
	link_to_request = link.get('href')
	h1 = soup.find_all('h1')
	for title in h1:
		print(title)
	checked_links.append(link)
	r = requests.get(f'http://web-16.challs.olicyber.it{link_to_request}')
	soup = BeautifulSoup(r.text, 'html.parser')

	nested_links = soup.find_all('a')
	for nested_link in nested_links:
		if not nested_link in checked_links:
			links.append(nested_link)
			


	