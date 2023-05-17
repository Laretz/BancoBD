from unittest import TestCase

import sys
sys.path.insert(0, '..')
from Prova1.conexaoDB import *

BD = "TestDB.db"

class MockBD(TestCase):
    @classmethod
    def setUpClass(cls):
        con = conectar(BD)
        cursor = con.cursor()



        query_create_professor = """CREATE TABLE Professor (
                                  id int NOT NULL PRIMARY KEY ,
                                  nome text NOT NULL
                                )"""
        query_create_turma = """CREATE TABLE Turma (
                                  id int NOT NULL PRIMARY KEY ,
                                  nome text NOT NULL,
                                  codigo text not NULL
                                )"""
        query_create_aluno = """CREATE TABLE Aluno (
                                  id int NOT NULL PRIMARY KEY,
                                  nome text NOT NULL
                                 
                                )"""
        query_create_media_aluno_turma = """CREATE TABLE Media_aluno_turma (
                                  id int NOT NULL PRIMARY KEY ,
                                  id_aluno int NOT NULL,
                                  id_turma int NOT NULL,
                                  nota1 float NOT NULL,
                                  nota2 float NOT NULL,
                                  nota3 float NOT NULL,
                                  media float NOT NULL,
                                  FOREIGN KEY (id_aluno) REFERENCES Aluno(id),
                                  FOREIGN KEY (id_turma) REFERENCES Turma(id)
                                )"""
        try:
            cursor.execute(query_create_professor)
            cursor.execute(query_create_turma)
            cursor.execute(query_create_aluno)
            cursor.execute(query_create_media_aluno_turma)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na criação das tabelas:", error)
        else:
            print("Criação das tabelas: OK")

        query_insert_professor = """INSERT INTO Professor (id, nome) VALUES
                                    (1, 'Kuramer'),
                                    (2, 'Arthurito'),
                                    (3, 'Lucas'),
                                    (4, 'Jubilema')"""

        query_insert_turma = """INSERT INTO Turma (id, nome, codigo) VALUES
                                    (1, 'Matematica', 'TAD0203'),
                                    (2, 'Geografia', 'MEUC1923' ),
                                    (3, 'Artes', 'MEUC1313' ), 
                                    (4, 'Ciencias', 'MEUC1945')"""

        query_insert_aluno = """INSERT INTO Aluno (id, nome) VALUES
                                    (1, 'Carla'),
                                    (2, 'Taniro'),
                                    (3, 'Alessandra'),
                                    (4, 'Tasia'),
                                    (5, 'Leonardo'),
                                    (6, 'Edson')                  
                                    """

        query_insert_media_aluno_turma = """INSERT INTO Exames (id, id_aluno, id_turma, nota1, nota2, nota3, media) VALUES
                                    (1, 1, 'TAD0203', 9, 9, 9, 9),
                                    (2, 1, 'MEUC1945', 9, 9, 9, 9),
                                    (3, 1, 'MEUC1923', 10, 10, 10, 10),
                                    (4, 2, 'TAD0203', 5,5, 5,5, 5,5, 5,5),
                                    (5, 6, 'TAD0203', 1, 1, 1, 1),
                                    (6, 4, 'TAD0203', 1, 1, 1, 1),
                                    (7, 2, 'TAD0203', 1, 1, 1, 1),
                                    (8, 4, 'MEUC1923', 1, 1, 1, 1),
                                    (9, 3, 'TAD0203', 1, 1, 1, 1),
                                    (10, 2,'MEUC1923', 1, 1, 1, 1)
                                    """
        try:
            cursor.execute(query_insert_professor)
            cursor.execute(query_insert_turma)
            cursor.execute(query_insert_aluno)
            cursor.execute(query_insert_media_aluno_turma)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na inserção de dados:", error)
        else:
            print("Inserção dos dados: OK")

        cursor.close()

        desconectar(con)

        testconfig ={
            'bd': BD
        }
        cls.mock_db_config = testconfig

    @classmethod
    def tearDownClass(cls):
        print("TearDown")
        con = conectar(BD)
        cursor = con.cursor()

        try:
            cursor.execute("DROP TABLE Professor")
            cursor.execute("DROP TABLE Turma")
            cursor.execute("DROP TABLE Aluno")
            cursor.execute("DROP TABLE Exames")
            con.commit()
            cursor.close()
            print("Removeu os dados das tabelas.")
        except sqlite3.Error as error:
            print("Banco de dados não existe. Erro na remoção do BD.", error)
        finally:
            desconectar(con)
