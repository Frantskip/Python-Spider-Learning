from bs4 import BeautifulSoup
soup = BeautifulSoup(open('01_study.html', encoding='utf-8'), 'lxml')
# print(soup.a)
# print(soup.find('a'))
# print(soup.find('a', class_='a2'))
# print(soup.find_all(['a','span']))
# print(soup.find_all('li',limit=2))

# print(soup.select('.a1'))
