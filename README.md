# Project: Lab 16/ Serverless Functions
## Author: Anas Alsallak
## Links and Resources
    - API: https://restcountries.com/v3.1https://restcountries.com/v3.1

## Setup

How to initialize/run your application 
    - First you need to clone the repo on your local machine using : git clone ssh-link
    - You need to create a venv using : python3.11 -m venv .venv
    - activate it : source .venv/bin/activate
    - download urllib3 in it : pip install urllib3
    - download requests lib using : pip install requests
    - download vercel locally using : npm i -g vercel
    - deploy the github project on vercel
    - run vercel locally using : vercel dev
    - ctrl+z to stop vercel

Tests
    - How do you run tests?
        - for capital finder : in the browser 
          https://capital-finder-anas-alsallak-4w7qmqene-anasalsallak.vercel.app/api/cpital_finder?country=country name
        - for country finder : in the browser 
          https://capital-finder-anas-alsallak-4w7qmqene-anasalsallak.vercel.app/api/cpital_finder?capital=capital name

    - Any tests of note?
        - for capital finder : in the browser 
          1. https://capital-finder-anas-alsallak-4w7qmqene-anasalsallak.vercel.app/api/cpital_finder?country=jordan
          2. https://capital-finder-anas-alsallak-4w7qmqene-anasalsallak.vercel.app/api/cpital_finder?country=spain
        - for country finder : in the browser 
          1. https://capital-finder-anas-alsallak-4w7qmqene-anasalsallak.vercel.app/api/cpital_finder?capital=amman
          2. https://capital-finder-anas-alsallak-4w7qmqene-anasalsallak.vercel.app/api/cpital_finder?capital=algeria

    - Describe any tests that you did not complete, skipped, etc
    stretch goal