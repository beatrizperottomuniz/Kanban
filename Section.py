class Section:
    def __init__(self,tit,limite,id):
        self.titulo=tit
        self.limite=limite
        self.id=id
        self.cards=[]

    def show(self):
        print("***************************************")
        print(f"Título: {self.titulo} ")
        print(f"ID: {self.id} ")
        print("***************************************")
    
    def showComplete(self):
        self.show()
        for card in self.cards:
            card.show()
    
    def addCard(self,card):
        try:
            sem_limite= ["TO DO","TO-DO","FAZER","NEW"]
            if (len(self.cards)+1<=self.limite) or self.titulo.upper() in sem_limite:
                card.secao_nome=self.titulo
                self.cards.append(card)
            else:
                raise Exception("Não foi possível adicionar esse cartão") 
        except Exception as e:
            print("Erro:",e)

    def updateCard(self,tit,sec,dono,card_index):
    #vai ser chamada essa função na seção que está com o card
        try:
            self.cards[card_index].titulo=tit
            self.cards[card_index].secao_id=sec
            self.cards[card_index].secao_nome=self.titulo
            self.cards[card_index].dono=dono
        except Exception as e:
            print("Erro:",e)

    def removeCard(self,card_index):
    #vai ser chamada essa função na seção que estava com o card
        try:
            self.cards.pop(card_index)
        except Exception as e:
            print("Erro:",e)