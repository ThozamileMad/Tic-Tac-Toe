
class MarkGrid():
    def __init__(self, pos):
        self.play_area = "  1  |  2  |  3\n-----------------\n  4  |  5  |  6\n-----------------\n  7  |  8  |  9"
        self.positions = pos
        self.index_lst = [[2, 8, 14], [36, 42, 48], [70, 76, 82], [2, 36, 70], [8, 42, 76], [14, 48, 82], [2, 42, 82], [14, 42, 70]]

    def detect_win_draw(self, x_o, winner):
        win_draw = False
        for lst in self.index_lst:
            if self.play_area[lst[0]] == x_o and self.play_area[lst[1]] == x_o and self.play_area[lst[2]] == x_o:
                print(f"{winner} has won!!!")
                win_draw = True      
        if self.positions == [] and not win_draw:
            print("It's a draw")
            win_draw = True
        return win_draw 
       

    def mark_grid_position(self, p, x_o, winner):
        if self.positions != None:
            self.play_area = self.play_area.replace(p, x_o)
            display_area = self.play_area
            for position in self.positions:
                display_area = display_area.replace(position, " ")
            print(f"\n{display_area}\n\n")   
        return self.detect_win_draw(x_o, winner)


