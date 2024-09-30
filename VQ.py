#Validation & Query

def validaSection(sections,id_section):
    if len(sections)==0:
        raise Exception("Não existe seção cadastrada")
    for section in sections:
        if section.id==id_section:
            return True
    return False

def validaCard(sections,id_card):
    for section in sections:
        if len(section.cards)==0:
            raise Exception("Não existe card cadastrado")
        for card in section.cards:
            if card.id==id_card:
                return True
    return False

def indexSection(sections,id_section):
    #sabendo que foi validada e existe com esse id
    k=0
    for section in sections:
        if section.id==id_section:
            return k
        k+=1

def indexCard(cards,id_card):
    #sabendo que foi validada e existe com esse id
    k=0
    for card in cards:
        if card.id==id_card:
            return k
        k+=1

'''-validar seção
-validar card
-achar seção
-achar card'''