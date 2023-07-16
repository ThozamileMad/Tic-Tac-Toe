from grid_marker import MarkGrid
from brain import GameConfig

positions = [f"{num + 1}" for num in range(9)]
markgrid = MarkGrid(positions)
gamebrain = GameConfig(markgrid, positions)
print("TIC TAC TOE\n")
print(f"{markgrid.play_area}\n")
gamebrain.initiate_game()


                    
        
        
        


        




