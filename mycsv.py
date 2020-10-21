# -*- coding: utf-8 -*-

# mycsv.py

def read_csv(path_to_csv_file, delimiter=","): #<FINISHED>
    try:
        res = list()
        fileToRead = open(path_to_csv_file,"r")
        for line in fileToRead.readlines():
            res.append(line.split(delimiter)) #on separe avec le délimiteur
        for i in range(len(res)): #on supprime le guillemet dans les entrées
            for j in range(len(res[i])):
                res[i][j] = res[i][j].replace("\"","")
                res[i][j] = res[i][j].replace("\n","")
        return res
        fileToRead.close()
    except:
        print("Error, such file doesn't exist")

def write_csv(path_to_csv_file, data, delimiter=','): #<FINISHED>
    try:
        fileToWrite = open(path_to_csv_file,"w")
        for line in data:
            for i in range(len(line)): #tant qu'il a une entrée à ajouter sur la ligne
                if i != (len(line) - 1): #ce n'est pas le dernier element de la ligne
                    fileToWrite.write(line[i] + delimiter)
                else: #c'est bien le dernier element de la ligne donc on met pas de séparateur mais un saut de ligne
                    fileToWrite.write(line[i] + "\n")
        fileToWrite.close()
    except:
        print("Error, such file can't be write")
