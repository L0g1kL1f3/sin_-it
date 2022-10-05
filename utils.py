# I would like to start to say that I am sorry for going over board with this if you are reading this 
# this is the last oportunaty you have to avoid madness
# everything I imported
import numpy as np
import pandas as pd
import functools
import os

# I will start by calculating de vectors
# this calculater will gather a list of numbers where each number is a boat and its value is a dimention, and a direction_vector that is a direction

def vector_calculator(size_boat,direction_vector):

    # to make atomatic coordinates calculations it is needed a try to prevent errors when the position in the directions vector is 0
     # the size of the boat is use in reshape
    try:
        
        vector_1=np.arange(0,size_boat*direction_vector[0],direction_vector[0]).reshape(size_boat,1)
        
    except:
    
# when the value is 0 in the index directed value the value  is change to [ ]

        vector_1=[]

# the same happens in the 2º coordinat
    try:
        
        vector_2=np.arange(0,size_boat*direction_vector[1],direction_vector[1]).reshape(size_boat,1)
        
    except:
        
        vector_2=[]

    # then depending wich direction the vector is at this is the formula that will calculate the vector
    # by joining the 2 coordinates
    if len(vector_1)==0:
        return np.array(list(map(lambda x,y=[0]: y+x ,vector_2.tolist())))
    else:
        return np.array(list(map(lambda x,y=[0]: x+y ,vector_1.tolist())))



def confirm_coor(vector,empty_list,list_boats,number_loops):
    
    # here I use the vector that resolted from the previos calculations and I add a coordinate from the empty_list
    # this is a list of empty coordinats in the list, this way I have possible positions


    possible_vectors=list(map(lambda x : (x+vector).tolist() ,empty_list ))

    # after that I will I check if all coordinates from the resulting vector are in
    # empty_list if they are the vector is left in the output else is taken out
    
    confirm_vectores=list(filter(lambda x : x if len(list(filter(lambda y: y if y in empty_list else None,x)))==list_boats[number_loops] else None,possible_vectors))

    return confirm_vectores


def find_hole(grid,hole):
     
    # here is where I make the list of empty coordinates, by using an array of coords using where
    
        empty_tuple=np.array(np.where(grid==hole))

        
        # and then transform the resulting tuple array in a list of coordinates


        empty_list=list(map(lambda x: [int(empty_tuple[0,x])]+[int(empty_tuple[1,x])],range(int(len(empty_tuple[0])))))

        return empty_list


# here is the a returcive function do map all the boats in the player's grid
def change_grid(final_list,grid):
    
    grid[final_list[0][0]][final_list[0][1]]="O"
    
    final_list.pop(0)
    
    if len(final_list)!=0:
        
        change_grid(final_list,grid)
 
    else:
        
        return grid

# simple boat object
class Boat:
    def __init__(self,size,coord):
        self.size=size
        self.coord=coord

# here is where I make 2 dicionaries 
# one dicionary have has a key of a string coord and a generated value name
# the second one has a key of the genereated name and a value of an object boat with the size and coordinates of the boat

def dic_maker(choose_position,dic_1,dic_2,n,boat_list,num,number_loops):
    
    key=str(choose_position[len(choose_position)-num])
    
    name="boat_"+str(n)
    
    dic_1.update({key:name})
    
    
    num-=1
    
    if num==0:
        dic_2.update({name:Boat(size=boat_list[number_loops],coord=choose_position[:])})
        return 
    else:
        
        return dic_maker(choose_position,dic_1,dic_2,n,boat_list,num,number_loops)

# this is a funcion that verifies the coords chosen by the player
def coord_verify(grid):

    coord_1=1
    
    coord_2=1
    
    try:
    
        coord_1=int(input("give me a coordinate for row between 1 and "+str(len(grid[0]))))
    
        coord_2=int(input("give me a coordinate for column between 1 and "+str(len(grid[:][0]))))
    
        if 1>coord_1>len(grid[0]) or 1>coord_2>len(grid[:][0]):
    
            int("a")
    
    except:
    
        print("incorrect input, try again")
    
        return coord_verify(grid)
    
    coord=[coord_1-1,coord_2-1]

    return coord

def all_posible_position(boat_list,number_loops,grid):

# here i calculate using vector_calculater all possible position that a boat can take in the grid from all possible direction


        down=vector_calculator(boat_list[number_loops],[1,0])
        up=vector_calculator(boat_list[number_loops],[-1,0])
        right=vector_calculator(boat_list[number_loops],[0,1])
        left=vector_calculator(boat_list[number_loops],[0,-1])

        # with diagonals

        d_up_rg=up+right
        d_up_lf=up+left
        d_down_rg=down+right
        d_down_lf=down+left

        # make a list of empty coordinates
        empty_list=find_hole(grid," ")

        # check what boat positions are in the empty_list and kept those
        
        down_coord=confirm_coor(vector=down,empty_list=empty_list,list_boats=boat_list,number_loops=number_loops)
        up_coord=confirm_coor(vector=up,empty_list=empty_list,list_boats=boat_list,number_loops=number_loops)
        left_coord=confirm_coor(vector=left,empty_list=empty_list,list_boats=boat_list,number_loops=number_loops)
        right_coord=confirm_coor(vector=right,empty_list=empty_list,list_boats=boat_list,number_loops=number_loops)
        up_rg_coord=confirm_coor(vector=d_up_rg,empty_list=empty_list,list_boats=boat_list,number_loops=number_loops)
        up_lf_coord=confirm_coor(vector=d_up_lf,empty_list=empty_list,list_boats=boat_list,number_loops=number_loops)
        dow_rg_coord=confirm_coor(vector=d_down_rg,empty_list=empty_list,list_boats=boat_list,number_loops=number_loops)
        dow_lf_coord=confirm_coor(vector=d_down_lf,empty_list=empty_list,list_boats=boat_list,number_loops=number_loops)

        # here I join all direction

        all_directions=down_coord+up_coord+left_coord+right_coord+up_lf_coord+up_rg_coord+dow_lf_coord+dow_rg_coord
        return all_directions


# here I filter of all individual coordinats that are not in the empty list
def second_filter_X(grid,first_filter):

    empty_coords=find_hole(grid," ")

    second_filter=list(map(lambda x : list(filter(lambda y: y if y in empty_coords else None,x)),first_filter))

    return second_filter




# here I filter of position that do not have a choose coordinat
# then filter coordinates from those positions that are ocupided
def hit_coords(grid,all_direction,coord,hit_list=[],number_loops2=0):
    
    first_filter=list(filter(lambda x : x if coord[number_loops2] in x else None,all_direction))
    
    second_filter=second_filter_X(grid,first_filter)
    first_filter=[]
    hit_list+=second_filter

    if len(coord)==number_loops2+1:
        return hit_list

    number_loops2+=1

    return hit_coords(grid,all_direction,coord,hit_list,number_loops2)


def baysian_hammer(grid,coord,list_boats,number_loops=0,baysian_hit_list=[],hit_list=[],number_loops2=0):
        
        # here I have to set to 0 all values that will be recursive
        
        number_loops2=0
        
        hit_list=[]

        # here I make a copy of a grid, this grid will be the players attack grid
        grid_empty=grid.copy()
        
        # change all the coordinates ocupied by a boat to empty
        grid_empty[np.where(grid_empty=="X")]=" "

        # check all possible position in that grid
        all_directions=all_posible_position(grid=grid_empty,boat_list=list_boats,number_loops=number_loops)

        # filter of the position without a chosen coordinate and filter of the coordinates in those position
        #  that are ocupided by X and add this in a list
        baysian_hit_list+=hit_coords(grid,all_directions,coord,hit_list=hit_list,number_loops2=number_loops2)
       
        
        if len(list_boats)==number_loops+1:

            # this part I am sure is redudent but I have to be sure when I take it out

                empty_list=find_hole(grid," ")
                
                baysian_list=list(map(lambda y: list(filter(lambda x: x if x in empty_list else None,y)) ,baysian_hit_list))

                # where I change the list from a list of position to a list of coordinates losing one dimention
                
                baysian_list=list(functools.reduce(lambda x, y: x+y,baysian_list))

                # then I make a list of mode coordinates
                
                baysian_list=pd.Series(baysian_list,list(map(str,np.arange(len(baysian_list)))))
            
                baysian_list=pd.DataFrame({"coord":baysian_list})
                
                baysian_coords=baysian_list["coord"].mode().tolist()
                
                return baysian_coords
        
        
        number_loops+=1
        return baysian_hammer(grid,coord,list_boats,number_loops,baysian_hit_list)


# don't use this funcion yet maybe my teacher can help
class display(object):
    """Display HTML representation of multiple objects"""
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""
    def __init__(self, *args):
        self.args = args
        
    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                         for a in self.args)
    
    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))
                           for a in self.args)

# here I have my player object with these atributes:

# boat_list, a list of number where the number is a boat a the value is the size 
# enemy_boat_list, the same but for the player to keep tabs of the enemy's boats 
# grid the player's grid where his boats are placed
# destroed_boats list of player's destroid boats
# attack_coord list of player's attack coordinats
# Hit_coord list of player's hit coordinats
# enemy_grid player's attack grid where enemy's boat's are at
# boat_coord dictionary where the key is a string of the coord and the value is the name of the boat
# boat_obj dictionary where the name of the boat is the key and the value is the object boat
# n is a value that increasses as boat objs are made in dictionary, the value is use to to generate a name in the dictionary

class player:
    def __init__(self, boat_list=[4,3,3,2,2,2,1,1,1,1],enemy_boat_list=[4,3,3,2,2,2,1,1,1,1],grid=np.full((10,10)," "),enemy_grid=np.full((10,10)," "),n=0,attack_coord=[],Hit_coord=[],destroed_boats=[]):
        self.boat_list=boat_list
        self.enemy_boat_list=enemy_boat_list
        self.destroed_boats=destroed_boats
        self.grid=grid
        self.attack_coord=attack_coord
        self.Hit_coord=Hit_coord
        self.enemy_grid=enemy_grid
        self.boat_coord={}
        self.boat_obj={}
        self.n=n
        
        
    # here the player can change the size and number of boats
    def update_boat_list(self,want_change="n",more_boats="y",range_of_boat=[],number_boats=0):
        
        
        if want_change=="n":
            
            want_change=input("do you want a costum fleet?(y/n)")
            
            if want_change=="y":
            
                self.boat_list=[]
                
      
        if want_change=="y":
           
            
            
            if range_of_boat==[] or more_boats=="y":
                
                
                try:
                    
                    range_of_boat= int(input("how big you want these boats to be?"))
                
                except:
                   
                    
                    print("can't read it give me a interger")
                    
                    return player.update_boat_list(self,want_change,more_boats,range_of_boat,number_boats)
            
           

            if  number_boats==[] or more_boats=="y":
                
                try:
                    number_boats=int(input("how many of these size boats you want?"))

                except:

                    print("can't read it give me a interger")

                    return player.update_boat_list(self,want_change,more_boats,range_of_boat,number_boats)

        
        elif want_change!="n":
            
            want_change="n"
            
            print("don't understand what you are saying? Let's try again with y or n.")
            
            return player.update_boat_list(self,want_change,more_boats,range_of_boat,number_boats)


       
        else:

            self.boat_list=[4,3,3,2,2,2,1,1,1,1]

            return 
        
     

        self.boat_list=self.boat_list+[range_of_boat]*number_boats
         

        
        more_boats=input("want more boats?(y/n)")
        
      
        if more_boats=="y":
        
           return player.update_boat_list(self,want_change,more_boats,range_of_boat,number_boats)
        
        
        elif more_boats!="n":
            
            more_boats="n"
            
            print("don't understand what you are saying? Let's try again with y or n.")
            
            return player.update_boat_list(self,want_change,more_boats,range_of_boat,number_boats)
        
        # after the list of boats of the player is made the player wil also change the list of boats 
        # of the enemy
        else:
            
            self.boat_list.sort(reverse=True)
            
            self.enemy_boat_list=self.boat_list.copy()
            
            return 

# here is to change the size of the grid
    def grid_change(self,number_rows=0,number_columns=0):
            
            want_change=input("do you want a costum your grid?(y/n)")
               
            
            if want_change not in ["n","y"]:

                    print("please y or n...")

                    player.grid_change(self,number_rows,number_columns)
                
            elif want_change=="y":
                

                    try:
                        number_rows=int(input("what is the number of rows you would like your grid to have? (max 28)"))

                        if 0>=number_rows>28:

                            print("please give me a number bigger then 0 and smaller then 29")

                            return player.grid_change(self,number_rows,number_columns)
                    except:

                        print("can't read it give me a interger")

                        return player.grid_change(self,number_rows,number_columns)

                    try:
                        number_columns=int(input("what is the number of columns you would like your grid to have? (max 18)"))

                        if 0>=number_rows>18:

                            print("please give me a number bigger then 0 and smaller then 19")

                            return player.grid_change(self,number_rows,number_columns)
                    except:

                        print("can't read it give me a interger")

                        return player.grid_change(self,number_rows,number_columns)

               
            else:
                    self.grid=np.full((10,10)," ")
                    
                    
                    return 
            
            # here like before both the players grid and the player's enemy's grid is  updated
            self.grid=np.full((number_rows,number_columns)," ")

            self.enemy_grid=self.grid.copy()



# here I place the boats
    def place_boats(self,number_loops=0):

        # using all_posible_positions() I get all possible direction 

        all_directions=all_posible_position(self.boat_list,number_loops,self.grid)

        # in case the boat is to big or there are too many boats there is no problem
        # if there are no all_direction

        if len(all_directions)==0:

            # I check if the boat I am looking at is size 1
            if self.boat_list[number_loops]==1:

                # if so I can't place any more boats
                
                print("we can't fit any more boats")
                return self.grid

            else:

                # seno lo es entoces lle digo que no puedo collocar un barco de esse tamaño

                print("we can't fit anymore boats size "+str(self.boat_list[number_loops])+" lets try again." )

                # transform a copy of list in array

                temp_array=np.array(self.boat_list)

                # slice of the list of boats above the number_loops

                self.boat_list=self.boat_list[:number_loops]

                # keep the values smaller in the array and transform it to a list

                temp_array=temp_array[temp_array<self.boat_list[number_loops]].tolist()

                # add the temp_array to the sliced boat_list

                self.boat_list=self.boat_list+temp_array

                
                # return to the funcion

                return player.place_boats(self,number_loops)
            
        
        # if there are direction choose one at random

        choose_position=all_directions[np.random.randint(len(all_directions))]

        # add that to the dictionaries

        self.n+=1
        dic_maker(choose_position,self.boat_coord,self.boat_obj,self.n,self.boat_list,len(choose_position),number_loops)

        # change the player's grid
        
        change_grid(grid=self.grid,final_list=choose_position)

        
        # if the len of boat_list is equal to the number_loop+1 it stops the process
        
        if len(self.boat_list)==number_loops+1:
            return self.grid
        else:
            
        # else it add the number_loops and re runs the funcion   
            number_loops+=1
            return player.place_boats(self,number_loops=number_loops)


    
        
       
    # attack method
    def attack(self,coord,enemy):

        # append the coord

            self.attack_coord.append([coord[0],coord[1]])
            
        # if the enemy was hit
        # append the coords to hit_coord 
        # and changes the player's attack grid   
            if enemy.grid[coord[0]][coord[1]]=="O":
                self.enemy_grid[coord[0]][coord[1]]="X"
                self.Hit_coord.append([coord[0],coord[1]])
                
                
        # else it changes the player's attack grid with |
                
            elif enemy.grid[coord[0]][coord[1]]==" ":
                self.enemy_grid[coord[0]][coord[1]]="|"
                
            return coord
            
            
# being attack method
    def being_attack(self,coord,enemy):
        
        # changes the player's grid

            if self.grid[coord[0]][coord[1]]=="O":
                self.grid[coord[0]][coord[1]]="X"

            # if hit changes player's obj dictionary to remove the coord from the obj

                self.boat_obj[self.boat_coord[str(coord)]].coord.remove(coord)


            # if the obj coords list len is 0
                
                if len(self.boat_obj[self.boat_coord[str(coord)]].coord)==0:

            # presents a msg to every one of what boat size was sunk
                    print("Boat size "+str(self.boat_obj[self.boat_coord[str(coord)]].size)+" has sunk")

            # appends to player's destroed_boat list the size atribute from the player's dic obj
                    self.destroed_boats.append(self.boat_obj[self.boat_coord[str(coord)]].size)
            
            # and removes that size from boat_list 
                    self.boat_list.remove(self.boat_obj[self.boat_coord[str(coord)]].size)

            # and also removes the same from the enemy's enemy_boat_list
                    enemy.enemy_boat_list.remove(self.boat_obj[self.boat_coord[str(coord)]].size)
                    
            # if the enemy's attack grid with only hit coords has the same len as the sum of the player's destroed_boats list
            # then the enemy removes all values from the hit_coord because all the previously hit_coord are from already destroed boats     
                if len(enemy.enemy_grid[enemy.enemy_grid=="X"])==sum(self.destroed_boats):
                    enemy.Hit_coord=[]
                
                    
                # then dels the player's coord that was hit in the dic of coords
                del self.boat_coord[str(coord)]
            

            # if it fail's it does the same as always
            elif self.grid[coord[0]][coord[1]]==" ":
                self.grid[coord[0]][coord[1]]="|"



    # method of attack for the player using coord_verify
    def player_attack(self,enemy):
        coord=player.attack(self,coord=coord_verify(self.grid),enemy=enemy)
        return coord
    

    # atomatic attack method
    def auto_atack(self,enemy):

        # first it checks if the biggest boat in the enemy_boat_list is size one
        # if so there is no point in complicated calculations because it's complitly random
        # just check the available spots in the attack grid a choose at random
        
        if self.enemy_boat_list[0]==1:
            
            empty_list=find_hole(self.enemy_grid," ")
            
            coord=empty_list[np.random.randint(len(empty_list))]
            
            coord=player.attack(self,coord,enemy)
            return coord
        
        # if len of hit_coord doesn't have any value
        # it will pick all posible_positions and check the mode coord and pick at random one 

        if len(self.Hit_coord)==0:
            
            possible_positions=all_posible_position(self.enemy_boat_list,0,self.enemy_grid)
            
            all_coord=list(functools.reduce(lambda x, y: x+y,possible_positions))
            
            coord_data=pd.Series(all_coord,list(map(str,np.arange(len(all_coord)))))
            
            coord_data=pd.DataFrame({"coord":all_coord})
            
            baysian_coords=coord_data["coord"].mode().tolist()

            bay_coord=baysian_coords[np.random.randint(len(baysian_coords))]

            coord=player.attack(self,bay_coord,enemy)
            return coord
            
        else:
            # if there is a coord in hit_coord
            # all these values are set to 0 to start the baysian_hammer
            # and get the mode of all possible positions with each hit_coord

            number_loops=0
            
            number_loops2=0
            
            baysian_hit_list=[]
            
            hit_list=[]
            
            coord=baysian_hammer(self.enemy_grid,self.Hit_coord,self.enemy_boat_list,baysian_hit_list=baysian_hit_list,number_loops=number_loops,hit_list=hit_list,number_loops2=number_loops2)
            
            # if there is no coord with this method 
            # sets hit_coord to empty list
            # and restarts the method
            if coord==[]:
            
                self.Hit_coord=[]
            
                player.auto_atack(self,enemy)
            
           
            # if there is a coord it pick one at random and sends that to attack method
            coord=coord[np.random.randint(len(coord))]
            
            coord=player.attack(self,coord,enemy)
            
            return coord
                    
    def display_game(self):
        # and this is my display method
        player_grid=self.grid.copy()
        player_grid=pd.DataFrame(player_grid)
        player_grid=player_grid.rename(columns=lambda x:x+1,index=lambda x: x+1)

        player_enemy_grid=self.enemy_grid.copy()
        player_enemy_grid=pd.DataFrame(player_enemy_grid)
        player_enemy_grid=player_enemy_grid.rename(columns=lambda x:x+1,index=lambda x: x+1)

        player_stats=pd.DataFrame({"player's stats":["num_players_boats","num_players_coords","player's_hit_rate"],
        "values":[len(self.boat_list),len(self.boat_coord),
        len(self.grid[self.enemy_grid=="X"])/ (len(self.grid[self.enemy_grid=="X"])+len(self.grid[self.enemy_grid=="|"]))if(len(self.grid[self.enemy_grid=="X"])+len(self.grid[self.enemy_grid=="|"]))>0 else 0]})
        

        
        print(player_grid,"\n", player_enemy_grid,"\n",player_stats)