from Board import Board
from Section import Section
from Card import Card
from VQ import *
class KanbanInterface:
    def __init__(self,board):
        self.board = board

    def menu(self):
        self.board.addSection(Section("Section1",2,1))
        self.board.sections[0].addCard(Card("t1","eu",1,1))
        self.board.sections[0].addCard(Card("t2","eu",1,2))
        self.board.addSection(Section("Section2",1,2))
        self.board.sections[1].addCard(Card("t3","eu",2,1))
        while True:
            print("\n--- MENU ---")
            print("1. Adicionar Card")
            print("2. Atualizar Card")
            print("3. Remover Card")
            print("4. Adicionar Seção")
            print("5. Atualizar Seção")
            print("6. Remover Seção")
            print("7. Mostrar Seções e Cartões")
            print("8. Sair")
            
            op = input("Escolha uma opção: ")
            if op=="8":
                print("Saindo")
                break
            if op == "1":
                self.addCard()
            elif op == "2":
                self.updateCard()
            elif op == "3":
                self.removeCard()
            elif op == "4":
                self.addSection()
            elif op == "5":
                self.updateSection()
            elif op == "6":
                self.removeSection()
            elif op == "7":
                self.printBoard()
            else:
                print("Opção inválida. Por favor, escolha uma opção de 1 a 8.")



    def addCard(self):
        card=None
        titulo=""
        dono=""
        secao_id=""
        try:
            while True:
                titulo=input("Título do cartão:")
                dono=input("Dono do cartão:")
                secao_id=int(input("Seção do cartão [id]:"))
                if validaSection(self.board.sections,secao_id):
                    break
                print("Seção inválida")
            secao_id2=indexSection(self.board.sections,secao_id)
            card=Card(titulo,dono,secao_id,len(self.board.sections[secao_id2].cards)+1)
            self.board.sections[secao_id2].addCard(card)
            self.board.sections[secao_id2].cards[-1].show()
        except Exception as e:
            print("Erro: ",e)
        
    def updateCard(self):
        #se o card esta na seção= muda campos
        #se não= remove da antiga e add na nova
        secao_id=""
        card_id=""
        titulo_novo=""
        dono_novo=""
        secao_nova =""
        secao_index=""
        card_index =""
        try:
            while True:
                secao_id=int(input("Qual a seção: "))
                card_id=int(input("Qual o card: "))
                if validaCard(self.board.sections,card_id) or validaSection(self.board.sections,secao_id) :
                    break
                print("Seção inválida")
            secao_index=indexSection(self.board.sections,secao_id)
            card_index=indexCard(self.board.sections[secao_index].cards,card_id)
            card=self.board.sections[secao_index].cards[card_index]
            secao_antiga=indexSection(self.board.sections,card.secao_id)
            while True:
                print("Digite o valor se quiser mudar ou enter para pular o campo")
                titulo_novo=input("Novo título:")
                if titulo_novo!="":
                    card.titulo=titulo_novo
                dono_novo=input("Novo dono:")
                if dono_novo!="":
                    card.dono=dono_novo   
                secao_nova=input("Nova seção [id]:")
                if secao_nova=="" :
                    self.board.sections[secao_index].updateCard(card.titulo,card.secao_id,card.dono,card_index)
                    break
                elif int(secao_nova)==card.secao_id:
                    self.board.sections[secao_index].updateCard(card.titulo,card.secao_id,card.dono,card_index)
                    break
                else:
                    if validaSection(self.board.sections,int(secao_nova)) :

                        secao_index=indexSection(self.board.sections,int(secao_nova))
                        card.secao_id=int(secao_nova)
                        self.board.sections[secao_index].addCard(card)
                        self.board.sections[secao_antiga].removeCard(card_index)
                        break
                    else:
                        print("Seção inválida")
        except Exception as e :
            print("Erro :",e)

    def removeCard(self):
        try:
            while True:
                    id_delete_card=int(input("Qual o id do card a ser deletado:"))
                    id_delete_section=int(input("Qual o id da section :"))
                    if validaCard(self.board.sections,id_delete_card) or validaSection(self.board.sections,id_delete_section) :
                        break
                    else:
                        print("Card inválido ou seção inválida")

            self.board.sections[indexSection(self.board.sections,id_delete_section)].removeCard(indexCard(self.board.sections[indexSection(self.board.sections,id_delete_section)].cards,id_delete_card))
            self.board.sections[indexSection(self.board.sections,id_delete_section)].showComplete()
        except Exception as e:
            print("Erro:",e)         

    def addSection(self):
        titulo=""
        limite=""
        section=None
        try:
            while True:

                    titulo=input("Título da seção :")
                    limite=int(input("Limite da seção:"))
                    if limite>0:
                        break
                    print("Limite precisa ser maior que zero")

            section=Section(titulo,limite,len(self.board.sections)+1)
            section.showComplete()
            self.board.addSection(section)
        except Exception as e:
            print("Erro: ",e)

    def updateSection(self):
        secao_id=""
        titulo_novo=""
        limite_novo=""
        secao_index=""
        try:
            while True:
                secao_id=int(input("Qual a seção: "))
                if validaSection(self.board.sections,secao_id) :
                    break
                print("Seção inválida")
            secao_index=indexSection(self.board.sections,secao_id)
            while True:
                print("Digite o valor se quiser mudar ou enter para pular o campo")
                titulo_novo=input("Novo título:")
                limite_novo=input("Novo limite:")
                if limite_novo!="":
                    limite_novo=int(limite_novo)
                    if limite_novo>0:
                        self.board.updateSection1(titulo_novo,secao_index)  
                    else:
                        print("Limite tem que ser maior que zero") 
                if titulo_novo!="":
                    self.board.updateSection2(titulo_novo,secao_index)   
                self.board.updateSection(titulo_novo,limite_novo,secao_index)
                break
        except Exception as e :
            print("Erro :",e)

    def removeSection(self):
        try:
            while True:
                    id_delete_section=int(input("Qual o id da section :"))
                    if validaSection(self.board.sections,id_delete_section) :
                        break
                    else:
                        print("Seção inválida")

            self.board.removeSection(indexSection(self.board.sections,id_delete_section))
            self.board.showComplete()

        except Exception as e:
            print("Erro:",e)         

    def printBoard(self):
        self.board.showComplete()
