class Card:
    def __init__(self,tit,dono,secao_id,id):
        self.titulo=tit
        self.dono=dono
        self.secao_id=secao_id
        self.secao_nome=""
        self.id=id

    def show(self):
        print("_______________________________________")
        print(f"Título: {self.titulo} ")
        print(f"ID: {self.id} ")
        print(f"Seção : {self.secao_nome}")
        print(f"Dono : {self.dono}")
