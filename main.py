from bs4 import BeautifulSoup

# Read the HTML file
with open('main.html', 'r') as file:
    html = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

row_class = "salary-row_collapsedSalaryRow__IQ3om"
level_class = "salary-row_levelName____tz6"
salary_class = "salary-row_totalCompCell__553Rk"
company_class = " salary-row_companyName__obLh0"

rows = soup.find_all('div', class_=row_class)
print(f'Found {len(rows)} rows')
for row in rows:
    level = row.find('div', class_=level_class).text
    salary = row.find('div', class_=salary_class).text
    company = row.find('div', class_=company_class).text
    print(f'{level} at {company} earns {salary}')
    break

