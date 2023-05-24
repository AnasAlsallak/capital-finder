# from http.server import BaseHTTPRequestHandler
# from urllib import parse
# import requests


# class handler(BaseHTTPRequestHandler):
 
#     def do_GET(self):

#         s= self.path
        
#         url_com = parse.urlsplit(s)
#         query_list = parse.parse_qsl(url_com.query)
#         dic = dict(query_list)
#         country = dic.get("country")
#         capital = dic.get("capital")

#         if capital and country:
#             urlCo= "https://restcountries.com/v3.1/name/"
#             urlCa= "https://restcountries.com/v3.1/capital/"
#             reqCo = requests.get(urlCo+capital)
#             dataCo = reqCo.json()
#             print (dataCo)
#             reqCa = requests.get(urlCa+country)
#             dataCa = reqCa.json()
#             countryR = dataCo[0]["name"]["common"]
#             capitalR = dataCa[0]["capital"][0]
#             if capitalR == capital and countryR == country:
#                 output = f"True"
#                 return
#         elif country:
#             url= "https://restcountries.com/v3.1/name/"
#             req = requests.get(url+country)
#             data = req.json()
#             capital = data[0]["capital"][0]
#             output = f"The capital of {country} is {capital}."
#         elif capital:
#             url= "https://restcountries.com/v3.1/capital/"
#             req = requests.get(url+capital)
#             data = req.json()
#             country = data[0]["name"]["common"]
#             output = f"{capital} is the capital of {country}."
            

#         self.send_response(200)
#         self.send_header('Content-type','text/plain')
#         self.end_headers()
#         self.wfile.write(output.encode('utf-8'))
#         return

from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s = self.path

        url_com = parse.urlsplit(s)
        query_list = parse.parse_qsl(url_com.query)
        dic = dict(query_list)
        country = dic.get("country")
        capital = dic.get("capital")

        if capital and country:
            url = "https://restcountries.com/v3.1/name/"
            req = requests.get(url + country)
            data = req.json()
            matching_capitals = []

            for country_data in data:
                if capital in country_data.get("capital", []):
                    matching_capitals.append(country_data)

            if matching_capitals:
                output = generate_country_info(matching_capitals)
                output += "The provided country and capital match."
            else:
                output = "No match found for the given country and capital."
        elif country:
            url = "https://restcountries.com/v3.1/name/"
            req = requests.get(url + country)
            data = req.json()

            if data:
                output = generate_country_info(data)
            else:
                output = "No information found for the given country."
        elif capital:
            url = "https://restcountries.com/v3.1/capital/"
            req = requests.get(url + capital)
            data = req.json()

            if data:
                output = generate_country_info(data)
            else:
                output = "No information found for the given capital."
        else:
            output = "Please provide either the 'country' or 'capital' parameter."

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(output.encode('utf-8'))
        return


def generate_country_info(data):
    result = ""

    for country_data in data:
        country_name = country_data.get("name", {}).get("common")
        capital = country_data.get("capital", [])
        currencies = country_data.get("currencies", {})
        languages = country_data.get("languages", {}).keys()

        result += f"Country: {country_name}\n"
        result += f"Capital(s): {', '.join(capital)}\n"
        result += f"Currencies: {', '.join(currencies)}\n"
        result += f"Languages: {', '.join(languages)}\n"
        result += "\n"

    return result
