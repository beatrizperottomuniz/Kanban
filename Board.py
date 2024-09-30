class Board:
    def __init__(self):
        self.sections=[]

    def show(self):
        print("________________B___O___A___R___D___________________")

    
    def showComplete(self):
        self.show()
        for secao in self.sections:
            secao.showComplete()

    def addSection(self,section):
        try:
            self.sections.append(section)
        except Exception as e:
            print("Erro:",e)

    def updateSection(self,tit,limite,section_index):
        try:
            self.sections[section_index].titulo=tit
            self.sections[section_index].limite=limite
        except Exception as e:
            print("Erro:",e)

    def updateSection1(self,tit,section_index):
        try:
            self.sections[section_index].titulo=tit
        except Exception as e:
            print("Erro:",e)

    def updateSection2(self,limite,section_index):
        try:
            self.sections[section_index].limite=limite
        except Exception as e:
            print("Erro:",e)

    def removeSection(self,section_index):
        try:
            self.sections.pop(section_index)
        except Exception as e:
            print("Erro:",e)
