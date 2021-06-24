import requests
from bs4 import BeautifulSoup

URL='https://www.amazon.in/HP-Pavilion-Processor-16-1-inch-16-a0022TX/dp/B08CGJ5K3V/ref=pd_sbs_4/262-0866954-8706964?pd_rd_w=XeP8Q&pf_rd_p=458377ad-f0e1-4b16-b359-07fb8404ce8b&pf_rd_r=KNXVS2626K5GAV3TSNGW&pd_rd_r=3c998042-3664-46a6-8e43-a8059b22190b&pd_rd_wg=GQHog&pd_rd_i=B08CGJ5K3V&psc=1'
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}

page=requests.get(URL,headers=headers)

soup=BeautifulSoup(page.content,'html.parser')
title=soup.find(id='title').get_text()
print(title.strip())
price=soup.find(id='unifiedPrice_feature_div').get_text()
print(price)