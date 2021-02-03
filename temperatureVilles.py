# coding: UTF-8
"""
Script: pythonProject6/temperatureVilles
Création: admin, le 15/01/2021
"""


# Imports
import requests
import mysql.connector
import time

# Fonctions


def get_temperature(ville):
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + ville + ",fr&units=metric&lang= fr&appid=0a73790ec47f53b9e1f2e33088a0f7d0"
    return float(requests.get(url).json()['main']['temp'])


def get_pression(ville):
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + ville + ",fr&units=metric&lang= fr&appid=0a73790ec47f53b9e1f2e33088a0f7d0"
    return float(requests.get(url).json()['main']['pressure'])


def set_temperature_bdd(ville, temperature, pression):
    cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='bdd_temperaturevilles')
    cursor = cnx.cursor()
    update_temp = ("UPDATE temperaturevilles SET temperature = (%s), pression = (%s) WHERE ville = (%s)")
    data = (temperature, pression, ville)
    cursor.execute(update_temp, data)
    cnx.commit()
    cursor.close()
    cnx.close()

    print("execution ok !")


# Programme principal
def main():

    villes = ["voiron","dijon", "caro", "bordeaux"]

    while 1:
        for ville in villes:
            set_temperature_bdd(ville, get_temperature(ville), get_pression(ville))
        time.sleep(300)


    #temperature = get_temperature("ruoms")
    #print("La temperature de la ville:", temperature)

    #set_bdd("ruoms", temperature)

    #set_temperature_bdd("voiron", get_temperature("voiron"))
    #set_temperature_bdd("dijon", get_temperature("dijon"))
    #set_temperature_bdd("caro", get_temperature("caro"))
    #set_temperature_bdd("bordeaux", get_temperature("bordeaux"))

    #print("La temperature de la ville de VOIRON:", get_temperature("voiron"))
    #print("La temperature de la ville de DIJON:", get_temperature("dijon"))
    #print("La temperature de la ville de CARO:", get_temperature("caro"))
    #print("La temperature de la ville de BORDEAUX:", get_temperature("bordeaux"))

if __name__ == '__main__':
    main()
    # Fin
