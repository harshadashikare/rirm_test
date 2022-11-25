# Q 1
import re
contact_list = ["2124567890", "212-456-7890", "(212)456-7890", "(212)-456-7890",
                "212.456.7890", "212 456 7890", "+12124567890", "+12124567890", "+1 212.456.7890", "+212-456-7890"]


"""
It takes a string and returns a match object if the string contains a phone number

:param contact: The contact number to be checked
:return: The result of the search.
"""
def check_contact(contact):
    result = re.search("([+(]?\d[-0-9 ().]{9,13})", contact)
    return result


for contact in contact_list:
    result = check_contact(contact)
    if result:
        print(contact, '-- is valid contact')
    else:
        print(contact, '-- not valid contact')

# or using user input

contact = input('enter number to check : ')
result = check_contact(contact)
if result:
    print(contact, '-- is valid contact')
else:
    print(contact, '-- not valid contact')


# Q 2

from bs4 import BeautifulSoup
import requests
import re
social_links = []
emails = []
contact = []
url = input('enter website url : ')

if not url.startswith('http'):
    url = 'http://'+url

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
response = requests.get(url=url, headers=headers)

if response.status_code >= 400:
    print('website is not accessible')
else:
    soup = BeautifulSoup(response.content, 'html.parser')

    social_platforms = ['facebook', 'linkedin', 'youtube', 'instagram']

    link_fetched = soup.find_all('a', href=True)
    for l in link_fetched:
        for social in social_platforms:
            if social in l['href']:
                social_links.append(l['href'])

    email_fetched = re.findall(
        '([\w\.-]+@[\w\.-]+(\.[\w]+))', str(soup.contents))
    for e in email_fetched:
        emails.append(e[0])

    contact_fetched = re.findall('([+(]?\d[-0-9 ().]{9,13})', soup.text)
    for c in contact_fetched:
        contact.append(c)

print('\n', 'Social links:')
for social in social_links:
    print(social)

print('\n', "Email:")
for email in emails:
    print(email)

print('\n', "Contact:")
for cont in contact:
    print(cont)
