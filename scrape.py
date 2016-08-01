import csv
import requests
from BeautifulSoup import BeautifulSoup


url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('tbody', attrs={'class': 'stripe'})

list_of_rows = []
for row in table.findAll('tr'):
	list_of_cells = []
	for cell in row.findAll('td'):
		text = cell.text.replace('&nbsp;', '')
		#prevents the text Details from being added to the list of cells
		if(text == 'Details'):
			continue
		list_of_cells.append(text)
	list_of_rows.append(list_of_cells)
	
outputfile = open("./inmates.csv", "wb")
writer = csv.writer(outputfile)
writer.writerow(["Last Name", "First Name", "Middle Name", "Sex", "Race", "Age", "City", "State"])
writer.writerows(list_of_rows)
	
