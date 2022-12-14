import imdb
import sys
import sqlite3
import fileinput
import os

# DE ADAUGAT INTERFATA
# FACUT PROGRAM SEPARAT
# DE ADAUGAT SERIALE
# NOUTATI PE NETFLIX
# SETEZI CALENDAR CU FILME SI SERIALE SI CAND VREI SA LE VEZI


filename = "D:\\Projects\\lista_filme.txt"

def meniu():

    print("------ Commands -----")
    print("|   l = your list   |")
    print("|   t = top movies  |")
    print("|   n = add grade   |")
    print("|   a = add movie   |")
    print("|   s = remove movie|")
    print("|    q = quit       |")
    print("----------A.C---------")
    

def topFilme():
    x = input('Choose the list of top IMDb movies you want to see: ')
    ia = imdb.IMDb()
    search = ia.get_top250_movies()
    for i in range(int(x)):
        print(str(int(i+1)) + '.' + ' ' + str(search[i]))
    

def adaugaNota():
    f = open(filename,"r+")
    film = input("Which movie do you want to rate?: ")
    nota = input("What grade do you want to give the film?: ")
    contents = f.read().replace(film, film + " " + nota + "/10")
    f.seek(0)
    f.truncate()
    f.write(contents)
        
def adaugaFilm():
    film = input("What movie do you want to add to the list?: ")
    f= open(filename,"a")
    f.write("\n" + film + "\n")
    f.close

def stergeFilm():
    f = open(filename,"r+")
    film = input("Which movie do you want to delete from the list: ")
    contents = f.read().replace(film, str(0))
    f.seek(0)
    f.truncate()
    f.write(contents)


def listaTa():   
    filehandle = open(filename,"r")
    filedata = filehandle.read()
    print(filedata)
    

while True:
    os.system('clear')
    meniu()
    choice = input('What do you want to do:')
    if choice == "q":
        sys.exit()
    elif choice == "t":
        topFilme()
    elif choice == "l":
        listaTa()
    elif choice == "n":
        adaugaNota()
    elif choice == "a":
        adaugaFilm()
    elif choice =="s":
        stergeFilm()
    

