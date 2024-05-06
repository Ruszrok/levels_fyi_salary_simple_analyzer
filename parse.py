from bs4 import BeautifulSoup
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python parse.py <html_file>')
        sys.exit(1) 

    file_name = sys.argv[1]
    with open(file_name, 'r') as file:
        html = file.read()

    soup = BeautifulSoup(html, 'html.parser')

    row_class = "salary-row_collapsedSalaryRow__IQ3om"
    level_class = "salary-row_levelName____tz6"
    salary_class = "salary-row_totalCompCell__553Rk"
    company_class = "salary-row_companyName__obLh0"

    rows = soup.find_all('tr', class_=row_class)
    print(f'Level, Company, Salary')
    for row in rows:
        level = row.find('p', class_=level_class).text
        salary = 'Unknown'
        salary_td = row.find('td', class_=salary_class)
        if salary_td:
            salary = salary_td.find('p').text
            
        company = row.find('a', class_=company_class).text if row.find('a', class_=company_class) else 'Unknown'
        
        #Clean level from multiple spaces and new lines
        level = ' '.join(level.split())
        print(f'{level}, {company.strip()}, "{salary.strip()}"')
    

