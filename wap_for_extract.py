import requests
import re
from bs4 import BeautifulSoup as bs
social="https://www.[lfi][ian][ncs][ket][eba][dog][ior][nka].com/[a-zA-Z1-9/-]+/*"
phone="\d{10}|\d{3}\-\d{3}\-\d{4}|\(\d{3}\)\d{3}\-\d{4}|\(\d{3}\)\-\d{3}\-\d{4}|\d{3}\.\d{3}\.\d{4}|\d{3}\ \d{3}\ \d{4}|\+\d{11}|\+\d{1}\ \d{3}\.\d{3}\.\d{4}|\+\d{3}\-\d{3}\-\d{3}|\d{1}\-\d{3}\-\d{3}\-\d{4}"
url="https://ful.io"
req = requests.get(url)
soup = bs(req.content, "html.parser")
links = soup.find_all("a")
links_ = []
print("Social Link:")
for link in links:

    links_.append(link.get("href"))
for ele in links_:
  if  "@" in ele:
    print("Email:","\n",  ele)
    
  elif re.search(social,ele):
    print(ele)
  elif re.search(phone, ele):
    tel = ele
    if "+" in tel:
      tel = "+" + tel.split("+")[-1]
    print("Contact:","\n", tel)
    
