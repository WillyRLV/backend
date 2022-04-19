#requests, bs4
## pip install request
## pip install bs4
from cgitb import html
import requests
from bs4 import BeautifulSoup

datos = {}
url = requests.get("https://www.sbs.gob.pe/app/pp/sistip_portal/paginas/publicacion/tipocambiopromedio.aspx")
if url.status_code == 200:
    # print(url.text)
    html = BeautifulSoup(url.text, "html.parser")
    tabla = html.find_all('table',{'id':'ctl00_cphContent_rgTipoCambio_ctl00'})
    # print(tabla)

    for i in range(7):
        filas = html.find_all('tr', {'id':'ctl00_cphContent_rgTipoCambio_ctl00__'+str(i)})

        for fila in filas:
            moneda = fila.find('td',{'class':'APLI_fila3'})
            compra = fila.find('td',{'class':'APLI_fila2'})
            venta = fila.find('td',{'class':'APLI_fila2'}).findNext('td')


            
        print(moneda.get_text(), " - ",compra.get_text(), " - ", venta.get_text())

        # datos = moneda.get_text()
        # print(datos)
else:
    print("error al abrir la pagina: " + str(url.status_code))
    