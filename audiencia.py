import requests
import pandas as pd

def download_pdf(lnk):

    from selenium import webdriver

    from time import sleep

    options = webdriver.ChromeOptions()     

    print("Downloading file from link: {}".format(lnk))

    driver = webdriver.Chrome('./chromedriver.exe',chrome_options = options)

    driver.get(lnk)

    imp_by1 = driver.find_elements_by_class_name('automaticas-canais')
    
    # form_element = driver.find_element_by_xpath('//*[@id="buttons"]/ul/li/a')
    
    # form_element.click()
    elementos = []

    for elemento in imp_by1:
        elementos.append(imp_by1.find_elements_by_css_selector('a.href'))
        print(imp_by1.find_elements_by_css_selector('a.href'))

       print("Status: Download Complete.")

    sleep(6)

    driver.close()


df = pd.read_csv("artigos2.csv", sep=";")
df["baixou"]=""
j=1

# for i in df.iterrows():
    
#     print(j)
#     url = 'https://sci-hub.tw/' + str(i[1]["DI"])
#     print(url)
#     try:
#         download_pdf(url)
#         i[1]["baixou"]=1
#     except:
#         i[1]["baixou"]=0
#     j=j+1
# pd.to_csv("novo.csv", sep=";")
url = "https://noticiasdatv.uol.com.br/canal/audiencias-4"
download_pdf(url)



# "https://noticiasdatv.uol.com.br/canal/audiencias-4?pagina=" + 2

#    lista_bandas = []


    
    

#     for banda in lista_bandas:
        
#         if banda[1].text != "":
#             data_aux = banda[1].text
#         palco.append(x_arg)
#         data.append(data_aux)
#         apres.append(banda[0][0].find_element_by_tag_name("h2").text)


#            lista_bandas = []

#     for banda in bandas:
#         lista_bandas.append((banda.find_elements_by_class_name('item'),banda.find_element_by_tag_name('span')))

#     print(x_arg)
    
    

#     for banda in lista_bandas:
        
#         if banda[1].text != "":
#             data_aux = banda[1].text
#         palco.append(x_arg)
#         data.append(data_aux)
#         apres.append(banda[0][0].find_element_by_tag_name("h2").text)


        
#     post = driver.find_elements_by_id('conteudo-resultado')

#     bandas = post[0].find_elements_by_class_name('bloco-artista')
