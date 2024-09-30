from Board import Board
from Section import Section
from Card import Card
from KanbanInterface import KanbanInterface

# Uso
board = Board()
interface = KanbanInterface(board)
interface.menu()