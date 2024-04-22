#!/usr/bin/python3

import json
import argparse

def initialiseParser():
    parser = argparse.ArgumentParser(description="Programa utilizado para encontrar en una lista json de seguidores y seguidos, quien de los quer sigues no te sigue!")
    parser.add_argument('-f', '--followers', required=True, type=str, help='archivo de seguidores que tienes (followers_1.json)')
    parser.add_argument('-F', '--following', required=True, type=str, help='archivo de personas a las que sigues')
    return parser

def loadFileFollowers(filename, miListaFollowers):
    with open(filename, "r", encoding='utf-8') as fichero:
        file = json.load(fichero)
        extractNamesFollowers(file, miListaFollowers)

def loadFileFollowing(miJsonFollowing, miListaFollowing):
    with open(miJsonFollowing, "r", encoding='utf-8') as fichero:
        file = json.load(fichero)
        extractNamesFollowing(file, miListaFollowing)
    
def extractNamesFollowing(miJsonFollowing, miListaFollowing):
    relationships_following = miJsonFollowing.get('relationships_following', [])
    for item in relationships_following:
          string_list_data = item.get('string_list_data', [])
          for element in string_list_data:
              valor = element.get('value')
              miListaFollowing.append(valor)
    return miListaFollowing

def extractNamesFollowers(miJsonFollowers, miLista):
    for item in miJsonFollowers:
        string_list_data = item.get('string_list_data', [])
        for element in string_list_data:
            valor = element.get('value')
            miLista.append(valor)
    return miLista

def runList(listaSeguidos, listaSeguidores):
    notCommon = []
    iterador = 0
    while iterador < len(listaSeguidos):
        seguidoActual = listaSeguidos[iterador]
        if not checkList(seguidoActual, listaSeguidores):
            notCommon.append(seguidoActual)
        iterador += 1
    return notCommon

def checkList(seguidoActual, listaSeguidores):
    if seguidoActual not in listaSeguidores:
        return False
    else:
        return True


def main():
    parser = initialiseParser()
    args = parser.parse_args()
    listaSeguidos = []
    listaSeguidores = []
    loadFileFollowers(args.followers, listaSeguidores)
    loadFileFollowing(args.following,listaSeguidos)
    print(f" Aqui tienes la lista de peronsas a las que sigues y no te siguen!: \n{runList(listaSeguidos, listaSeguidores)}")


if __name__ == '__main__':
    main()
