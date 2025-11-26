from bs4 import BeautifulSoup
import requests

url = "https://pt.wikipedia.org/wiki/Star_Wars"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
           
response = requests.get(url, headers=headers, timeout=10)

if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

#        titulo = soup.title.string
#        print(titulo)

        paragrafo_um = soup.find("p").text
#        print(paragrafo_um)
        
        paragrafos = soup.find_all("p")

        if len(paragrafos) > 1:
                print(paragrafos[1].text)
        else:
                print("Não existe")
                
        links = soup.find_all("a", href=True)[:5]

        for link in links:
            print(link["href"])
            
