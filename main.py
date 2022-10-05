import utils as u
import numpy as np
import pandas as pd
import functools
import os

# here I make the game

def main(player_1=u.player(),CPU=u.player(),sec_round=False):
   
   # if it is the first round
    
    if not sec_round: 
        
        player_1=u.player(boat_list=[4,3,3,2,2,2,1,1,1,1],enemy_boat_list=[4,3,3,2,2,2,1,1,1,1],grid=np.full((10,10)," "),enemy_grid=np.full((10,10)," "),n=0,attack_coord=[],Hit_coord=[],destroed_boats=[])
        
        player_1.grid_change()
        
        player_1.update_boat_list()
        
        CPU=u.player(boat_list=player_1.boat_list.copy(),grid=player_1.grid.copy(),enemy_grid=player_1.grid.copy(),enemy_boat_list=player_1.boat_list.copy(),n=0,attack_coord=[],Hit_coord=[],destroed_boats=[])
        
        player_1.place_boats()
        
        CPU.place_boats()
        
        os.system('cls')
        
        player_1.display_game()
    
    player_1_coords=player_1.player_attack(CPU)
    
    CPU.being_attack(player_1_coords,player_1)
    
    os.system('cls')
    
    player_1.display_game()
    
    input("press enter to continue")
    
    if len(CPU.grid[CPU.grid=="O"])==0:
        
        os.system('cls')
        
        print("you win...you Baysian God")
        
        new_game=input("wanna play again?(y/n)")
        
        if new_game=="y":
        
            sec_round=False
        
            main()
        
        elif new_game=="n":
        
            print("very well then, go outside it must be lovely:)")
        
        else:
        
            print("I don't understand what you are saying...may be you should go out side")
        
        return

    
    CPU_coord=CPU.auto_atack(player_1)
    
    player_1.being_attack(CPU_coord,CPU)
    
    os.system('cls')
    
    player_1.display_game()
    
    input("press enter to continue")
    
    if len(player_1.grid[player_1.grid=="O"])==0:
    
        print("you lose...")
        
        new_game=input("wanna play again?(y/n)")
        
        if new_game=="y":
        
            sec_round=False
        
            main()
        
        elif new_game=="n":
        
            print("very well then, go outside it must be lovely:)")
        
        else:
        
            print("I don't understand what you are saying...may be you should go out side")
    
        return

    
    sec_round=True
    
    stop=input("want to stop?")
    
    if stop=="y":
    
        return
    
    return main(player_1,CPU,sec_round)
    

        
main()