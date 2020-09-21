import pandas as pd
import os


directory = './audiencia/'
programa=[]
media=[]
dia=[]
origem=[]


for file_name in os.listdir(directory):
    programa_aux=[]
    media_aux=[]
    print(file_name)
    df=pd.read_csv("./audiencia/"+file_name, encoding="utf-8")
    programa_aux.append(df.iloc[:,1].values)
    media_aux.append(df.iloc[:,2].values)
    for i,j in enumerate(programa_aux[0]):
        programa.append(j)
        media.append(media_aux[0][i])
        d= file_name.split('_')[1].replace('1°',"1").replace("1º","1")
        print(d)
        if int(d) < 10:
            d='0'+d
        m=file_name.split('_')[2]
        if int(m) < 10:
            m='0'+ m
        dia.append(file_name.split('_')[-1].replace('.csv','')+m+d)
        origem.append(file_name)


d = {'programa': programa,
'media':media,
'dia':dia,
"origem":origem
    }

df2 =  pd.DataFrame(data = d)

df2.to_csv("tudo.csv")