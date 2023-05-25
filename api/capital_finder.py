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

        if country and capital:
            # stretch goal stopped working on it bc i could not do the testing bc api is down 
            # url = "https://restcountries.com/v3.1/name/" 
            # req = requests.get(url + country)
            # data = req.json()
            # if len(data) > 0:
            #     country_data = data[0]
            #     country_name = country_data.get("name").get("common")
            #     country_capitals = country_data.get("capital")
            #     country_currencies = country_data.get("currencies")
            #     country_languages = country_data.get("languages")
            #     if capital in country_capitals:
            #         currency_list = ", ".join(country_currencies.keys())
            #         language_list = ", ".join(country_languages.values())
            #         output = f"The capital of {country_name} is {capital}."
            #         output += f"\nCurrency: {currency_list}"
            #         output += f"\nLanguages: {language_list}"
            #         output += "\nIt is a correct country/capital match."
            #     else:
            #         output = f"The capital {capital} is not associated with the country {country_name}."
            # else:
            #     output = f"No information available for the country {country}."

        elif country:
            url= "https://restcountries.com/v3.1/name/"
            req = requests.get(url+country)
            data = req.json()
            if len(data) > 0:
                capital = data[0]["capital"][0]
                output = f"The capital of {country} is {capital}."
            else:
                output = f"No information available for the country {country}."

        elif capital:
            url= "https://restcountries.com/v3.1/capital/"
            req = requests.get(url+capital)
            data = req.json()
            if len(data) > 0:
                country = data[0]["name"]["common"]
                output = f"{capital} is the capital of {country}."
            else:
                output = f"No information available for the country {country}."
            

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(output.encode('utf-8'))
        return



