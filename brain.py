import random

class GameConfig():
    def __init__(self, mk_grid, pos):
        self.mark_grid = mk_grid
        self.mark_position = self.mark_grid.mark_grid_position
        self.positions = pos

    def game_mode_config(self, p1_p2, is_bot, x_o=None):
        player = input(f"\n{p1_p2} select which grid block to mark: ").upper()
        if player not in self.positions:
            print(f"\nInvalid input, select one of the numbers in the list: {self.positions}")
            self.game_mode_config(p1_p2, is_bot, x_o)
        else:
            if is_bot:
                self.positions.remove(player)          
                if self.positions != None:
                    rand_select = random.choice(self.positions)
                else:
                    rand_select = None
                if self.mark_position(player, "X", "Player") or self.mark_position(rand_select, "O", "Bot"):
                    return True
                self.positions.remove(rand_select)
            else:
                self.positions.remove(player)
                if self.mark_position(player, x_o, p1_p2):
                    return True

    def initiate_game(self):
        option = input("Play with a human or bot: ")
        won_drew = False
        error = False
        while not won_drew and not error:
            if option == "bot":
                if self.game_mode_config(p1_p2="Player", is_bot=True):
                    won_drew = True
            elif option == "human":
                if self.game_mode_config(p1_p2="Player 1", is_bot=False, x_o="X"):
                    won_drew = True
                elif self.game_mode_config(p1_p2="Player 2", is_bot=False, x_o="O"):
                    won_drew = True
            else:
                print("Invalid input type human or bot")
                error = True

        if error:
            print("\nTIC TAC TOE\n")
            print(f"{self.mark_grid.play_area}\n")
            self.initiate_game()

                
        
        

            
            
            

            
