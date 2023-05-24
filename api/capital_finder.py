from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):

        s= self.path
        
        url_com = parse.urlsplit(s)
        query_list = parse.parse_qsl(url_com.query)
        dic = dict(query_list)
        country = dic.get("country")
        capital = dic.get("capital")

        if capital and country:
            urlCo= "https://restcountries.com/v3.1/name/"
            urlCa= "https://restcountries.com/v3.1/capital/"
            reqCo = requests.get(urlCo+capital)
            dataCo = reqCo.json()
            print (dataCo)
            reqCa = requests.get(urlCa+country)
            dataCa = reqCa.json()
            countryR = dataCo[0]["name"]["common"]
            capitalR = dataCa[0]["capital"][0]
            if capitalR == capital and countryR == country:
                output = f"True"
                return
        elif country:
            url= "https://restcountries.com/v3.1/name/"
            req = requests.get(url+country)
            data = req.json()
            capital = data[0]["capital"][0]
            output = f"The capital of {country} is {capital}."
        elif capital:
            url= "https://restcountries.com/v3.1/capital/"
            req = requests.get(url+capital)
            data = req.json()
            country = data[0]["name"]["common"]
            output = f"{capital} is the capital of {country}."
            

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(output.encode('utf-8'))
        return