import requests
from bs4 import BeautifulSoup
import time
#import pandas as pd


with open('iphone118.csv','a') as file:
    file.write('Modele,ETAT, Stockage,Secteur(Ville),description du telephone ,PRIX EN DH , plus dinfo Voir les liens suivants\n')
    for i in range(1,3):  #You can choose the number of pages that you want to scrape
        url='https://www.avito.ma/fr/maroc/t%C3%A9l%C3%A9phones/iphone_11--%C3%A0_vendre?'
        if i==1:
            url+='phone_brand=2'
        else:
            url+='o='+str(i)+'&phone_brand=2'
        headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
        response=requests.get(url,headers=headers)

        if response.ok:
            soup=BeautifulSoup(response.text,'html.parser')
            urlss=[u['href'] for u in soup.find_all('a',class_='oan6tk-1 fFOxTQ')]  #links for more infos
            descrr=[u.text for u in soup.find_all('span',class_='oan6tk-17 ewuNqy')]  #DEscription of each mobile
            prixx=[u.text for u in soup.find_all('span',class_='sc-1x0vz2r-0 izsKzL oan6tk-15 cdJtEx')] # iphone Prices
            
            for i in range(len(urlss)):
                d=dict()
                responsee=requests.get(urlss[i],headers=headers)
                print(responsee) #Just to 
                if responsee.ok:
                    soupp=BeautifulSoup(responsee.text,'html.parser')
                    configdata=list(zip(soupp.find_all('span',class_='sc-1x0vz2r-0 brylYP'),soupp.find_all('span',class_='sc-1x0vz2r-0 jsrimE')))
                    for a,b in configdata:
                        d[a.text]=b.text
                    if prixx[i]!='Prix non spécifié':
                        ll=['Modèle','État','Capacité de Stockage','Secteur']
                        for ii in ll:
                            if ii in d:
                                file.write(d[ii])
                                file.write(',')
                            else:
                                file.write('NONE')
                                file.write(',') 
                        file.write(descrr[i])
                        file.write(',')
                        file.write(str(int(prixx[i][0:len(prixx[i])-3].replace(',','')))) 
                        file.write(',')
                        file.write(urlss[i])
                        file.write('\n')
    time.sleep(2)



