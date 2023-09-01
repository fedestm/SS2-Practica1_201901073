import pyodbc
from pyparsing import col
import mysql.connector
import os
from mysql.connector import Error
import subprocess

try:
    connSQLS = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;'
                            'SERVER=PC\SQLEXPRESS;'
                            'DATABASE=usacdelivery;'
                            'UID=sa;'
                            'PWD=root', autocommit=True)
    print("Conexión exitosa")
except mysql.connector.Error as error:
    print("Error al crear la conexión {}".format(error))


def menu():
    MENU = '''
    USAC Delivery
    1) Borrar Modelo
    2) Crear Modelo
    3) Extraer información
    4) Cargar información
    5) Consultas
    6) Salir
    '''
    print(MENU)
    while True:
        entrada = int(input('Ingrese opción: '))

        if entrada == 1:
            print("Borrar Modelo")
            os.system("sqlcmd -S PC\SQLEXPRESS -i C:\\Users\\gnitr\\Documents\\Github\\SS2-Practica1_201901073\\eliminar.sql")
            print("\n Borrado \n")
        elif entrada == 2:
            print("Crear modelo")
            os.system("sqlcmd -S PC\SQLEXPRESS -i C:\\Users\\gnitr\\Documents\\Github\\SS2-Practica1_201901073\\crear.sql")
            print("\n Creado \n")
        elif entrada == 3:
            print("Extraer información")
            os.system("sqlcmd -S PC\SQLEXPRESS -i C:\\Users\\gnitr\\Documents\\Github\\SS2-Practica1_201901073\\extraer.sql")
        elif entrada == 4:
            print("Cargar información")
            os.system("sqlcmd -S PC\SQLEXPRESS -i C:\\Users\\gnitr\\Documents\\Github\\SS2-Practica1_201901073\\cargar.sql")
        elif entrada == 5:
            print("Realizar consultas")

            print("Consulta 1")
            sql_command = "sqlcmd -S PC\SQLEXPRESS -i C:\\Users\\gnitr\\Documents\\Github\\SS2-Practica1_201901073\\consulta1.sql"
            result = subprocess.run(
                sql_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
            )
            print(result.stdout.decode())
            crear_archivo(result.stdout.decode(), 'Consulta1.txt')

            print("Consulta 2")
            sql_command = "sqlcmd -S PC\SQLEXPRESS -i C:\\Users\\gnitr\\Documents\\Github\\SS2-Practica1_201901073\\consulta2.sql"
            result = subprocess.run(
                sql_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, encoding='latin-1'
            )
            print(result.stdout)
            crear_archivo(result.stdout, 'Consulta2.txt')

            print("Consulta 3")
            sql_command = "sqlcmd -S PC\SQLEXPRESS -i C:\\Users\\gnitr\\Documents\\Github\\SS2-Practica1_201901073\\consulta3.sql"
            result = subprocess.run(
                sql_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, encoding='latin-1'
            )
            print(result.stdout)
            crear_archivo(result.stdout, 'Consulta3.txt')

            print("Consulta 4")
            sql_command = "sqlcmd -S PC\SQLEXPRESS -i C:\\Users\\gnitr\\Documents\\Github\\SS2-Practica1_201901073\\consulta4.sql"
            result = subprocess.run(
                sql_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, encoding='latin-1'
            )
            print(result.stdout)
            crear_archivo(result.stdout, 'Consulta4.txt')

            print("Consulta 5")
            sql_command = "sqlcmd -S PC\SQLEXPRESS -i C:\\Users\\gnitr\\Documents\\Github\\SS2-Practica1_201901073\\consulta5.sql"
            result = subprocess.run(
                sql_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, encoding='latin-1'
            )
            print(result.stdout)
            crear_archivo(result.stdout, 'Consulta5.txt')

            print("Consulta 6")
            sql_command = "sqlcmd -S PC\SQLEXPRESS -i C:\\Users\\gnitr\\Documents\\Github\\SS2-Practica1_201901073\\consulta6.sql"
            result = subprocess.run(
                sql_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, encoding='latin-1'
            )
            print(result.stdout)
            crear_archivo(result.stdout, 'Consulta6.txt')

            print("Consulta 7")
            sql_command = "sqlcmd -S PC\SQLEXPRESS -i C:\\Users\\gnitr\\Documents\\Github\\SS2-Practica1_201901073\\consulta7.sql"
            result = subprocess.run(
                sql_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, encoding='latin-1'
            )
            print(result.stdout)
            crear_archivo(result.stdout, 'Consulta7.txt')

            print("Consulta 8")
            sql_command = "sqlcmd -S PC\SQLEXPRESS -i C:\\Users\\gnitr\\Documents\\Github\\SS2-Practica1_201901073\\consulta8.sql"
            result = subprocess.run(
                sql_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, encoding='latin-1'
            )
            print(result.stdout)
            crear_archivo(result.stdout, 'Consulta8.txt')

            print("Consulta 9")
            sql_command = "sqlcmd -S PC\SQLEXPRESS -i C:\\Users\\gnitr\\Documents\\Github\\SS2-Practica1_201901073\\consulta9.sql"
            result = subprocess.run(
                sql_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, encoding='latin-1'
            )
            print(result.stdout)
            crear_archivo(result.stdout, 'Consulta9.txt')

            print("Consulta 10")
            sql_command = "sqlcmd -S PC\SQLEXPRESS -i C:\\Users\\gnitr\\Documents\\Github\\SS2-Practica1_201901073\\consulta10.sql"
            result = subprocess.run(
                sql_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, encoding='latin-1'
            )
            print(result.stdout)
            crear_archivo(result.stdout, 'Consulta10.txt')
        elif entrada == 6:
            exit(0)
        else:
            print("Opción incorrecta")

def crear_archivo(cadena, nombre):
    with open(nombre, "w", encoding='utf-8') as archivo:
        archivo.write(cadena)


if __name__ == '__main__':
    menu()