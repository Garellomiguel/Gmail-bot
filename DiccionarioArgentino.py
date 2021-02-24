import requests
from requests_html import HTML

def palabra_del_dia():
    palabra={}

    URL = "https://www.diccionarioargentino.com/"
    res = requests.get(URL)
    res.raise_for_status()

    #en la pagina principal encuentro el link de la primera palabra para ver todas sus definiciones
    #obtengo el link y hago el request de ese link
    html_obj = HTML(html = res.text)
    random_url = html_obj.find("strong>a")
    link = next(iter(random_url[0].absolute_links), None)
    res = requests.get(link)
    res.raise_for_status()

    #tomo toda la pagina y busco el titulo y el cuerpo, selecciono solo el primero porque hay muchos en la pagina
    html_obj = HTML(html = res.text)
    title_obj = html_obj.find(".panel-title>strong>a", first = True)
    body_obj = html_obj.find(".panel-body>p")

    #Formateo los textos para sacar lo q no quiero y lo guardo todo en un diccionario
    titulos = title_obj.text.split(".")
    palabra["titulo"] = titulos[1]
    palabra["cuerpo"] = body_obj[0].text
    palabra["ejem"] = body_obj[1].text
 
    
    return palabra

