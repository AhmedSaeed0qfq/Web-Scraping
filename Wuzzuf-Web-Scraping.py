import requests 
from bs4 import BeautifulSoup
import csv 
from itertools import zip_longest
job_title=[]
company_name=[]
location=[]
skill=[]
links=[]
salary=[]

#2nd use requsts to reach url
result=requests.get('https://wuzzuf.net/search/jobs/?q=data+scientist&a=hpb')

#3rh save page content
page_content= result.content

#4 creat soup object to phrase content
soup=BeautifulSoup(page_content,'lxml')
#print(soup)

#5 find the elements containing the info
#-- jop titles,jop skills,company names,locations
job_titles=soup.find_all("h2",{"class":"css-m604qf"})
company_names=soup.find_all("a",{'class':"css-17s97q8"})
locations=soup.find_all('span',{'class':'css-5wys0k'})
job_skills=soup.find_all("div",{"class":"css-y4udm8"})
#6 loop to get text from soup
for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    links.append(job_titles[i].find('a').attrs['href'])
    company_name.append(company_names[i].text)
    location.append(locations[i].text)
    skill.append(job_skills[i].text)    
#7 creat csv file
for link in links:
    result=requests.get(link)
    scr=result.content
    soup=BeautifulSoup(scr,"lxml")
    
'''       
file_list=[job_title,company_name,location,skill,links,salary]
ziped_lists=zip_longest(*file_list)
with open('/Users/Eslam hosam/Documents/datascience.csv','w') as file:
    writer=csv.writer(file)
    writer.writerow(['job title','company name','location','skills','link','salary'])
    writer.writerows(ziped_lists)
'''