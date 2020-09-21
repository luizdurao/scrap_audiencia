import pandas as pd
import requests
from bs4 import BeautifulSoup

sbt=[]
globo=[]
record=[]
df = pd.read_csv("paginas2.csv", encoding="utf-8", sep=";")

for i in df.iterrows():
    url = str(i[1]["paginas"])
    print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    dia = soup.find_all(class_="cl_audiencias")[2].get_text()
    # dia = dia1.find_all("span").get_text()
    print(dia)
    df_list = pd.read_html(r.text,decimal=',',encoding="utf-8") # this parses all the tables in webpages to a list
    try:
        df_list[1].to_csv("./audiencia/globo_"+dia.split()[2].replace("/","_")+".csv", encoding="utf-8")
        df_list[2].to_csv("./audiencia/record_"+dia.split()[2].replace("/","_")+".csv", encoding="utf-8")
        df_list[3].to_csv("./audiencia/sbt_"+dia.split()[2].replace("/","_")+".csv", encoding="utf-8")
    except Exception as e:
        print(e)

