# -*- coding: utf-8 -*-
import win32com.client
import os
import sys
class Fila():
    def __init__(self):
        self.item = []

    def enfileira(self, i):
        self.item.append(i)

    def tirar(self):
        if not self.IsEmpty():
            return self.item.pop(0)
        else:
            raise Exception('A fila ja está vazia')

    def retornar(self):
        return self.item

    def IsEmpty(self):
        if self.item == []:
            return True

    def inverter(self):
        self.meti = []
        for i in self.item[::-1]:
            self.meti.append(i)
        self.item = self.meti
class Conversor(object):
    def __init__(self, endereco, nome=None):
        try:
            #criação de atributos e filas L (35-37) /e lendo arquivo da pasta L(38)
            self.endereco, self.nome = endereco, nome
            self.Fila_entrada = Fila()
            self.Fila_saida = Fila()
            self.list = os.listdir(self.endereco)
            #Chamando funcões de criação de pasta de destino L(39)
            self.destino = self.Criar_pasta(self.endereco,self.nome)
            #Conversão de power point para pdf L(44 - 56)
            for self.x in self.list:
                #lendo o endereço do arquivo
                self.endereco_arquivo = f"{self.endereco}\\{self.x}"
                print('é esse aqui ',self.endereco_arquivo)
                #Abrindo e convetendo
                self.nome_arquivo = self.x.replace(".pptx","")
                #endereço do pdf
                self.saida = f'{os.path.splitext(self.destino)[0]}\{self.nome_arquivo}'

                self.powerpoint = win32com.client.Dispatch("Powerpoint.Application")
                self.pdf = self.powerpoint.Presentations.Open(self.endereco_arquivo)
                self.pdf.SaveAs(self.saida, 32)
                self.pdf.Close()
                self.pdf = None

                #Salvando os nomes dos que foram salvos em pdf
        except FileNotFoundError:
            print("caminho invalido")
        except AttributeError:
            print("Erro")
        try:
            self.powerpoint.Quit()
        except:
            pass
    def Criar_pasta(self,endereco, nome):
        try:
            self.en,self.no = endereco, nome
            if self.no == None:
                if os.path.exists(self.en + "\\Certificados em PDF") == False:
                    self.endereco_destino = self.en + "\\Certificados em PDF"
                    os.mkdir(self.endereco_destino)
                    return self.endereco_destino
                else:
                    self.endereco_destino = self.en + "\\Certificados em PDF"
                    return self.endereco_destino
            else:
                if os.path.exists(self.en +"\\"+ self.no) == False:
                    self.endereco_destino = f'{self.en}\\{self.no}'
                    os.mkdir(self.endereco_destino)
                    return self.endereco_destino
                else:
                    self.endereco_destino = self.endereco + "\\" + self.no
                    return self.endereco_destino
        except OSError:
            print("Erro na criação da pasta")
        except ValueError:
            print("O no é invalido")





