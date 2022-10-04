# Me gostarias empezar pedindo perdon a quem vai redigir isto...me passei um pouco
# aqui esta tudo o que importei
import numpy as np
import pandas as pd
import functools
from IPython.display import clear_output



# empezamos com un calculador de vectores este calculador recolhe una lista de numberos com as dimenciones de los barcos cada numero sendo un barco y su valor sendo su tamanho
def vector_calculator(size_boat,direction_vector):

     # para poder hacer coordinadas del vector de forma automatica uno tendra que hacer un try para los numeros 0 que no me permitiriam hacelo
     # el tamaño del barco es usado para hacer el reshape
    try:
        
        vector_1=np.arange(0,size_boat*direction_vector[0],direction_vector[0]).reshape(size_boat,1)
        
    except:
    
# quando isso ocurre passo pra aqui y le dou este valor

        vector_1=[]

# o mismo acontece com esta coordinada de vector 
    try:
        
        vector_2=np.arange(0,size_boat*direction_vector[1],direction_vector[1]).reshape(size_boat,1)
        
    except:
        
        vector_2=[]

    # despois dependendo de que cordinada es 0  junto as duas coordinadas vectories y hago un vector com essas coordinadas
    if len(vector_1)==0:
        return np.array(list(map(lambda x,y=[0]: y+x ,vector_2.tolist())))
    else:
        return np.array(list(map(lambda x,y=[0]: x+y ,vector_1.tolist())))



def confirm_coor(vector,empty_list,list_boats,number_loops):
    
    # aqui collo el vector resultante y lle añado una cordinada, creada desde las posiciones vacias explicado mais abajo como lo hice, tendo assim la possible posicion del barco 


    possible_vectors=list(map(lambda x : (x+vector).tolist() ,empty_list ))


    #checkeo que la posicion el valida partindo del numero dela lista de barco correspondente com el loop y el len de la lista de coordinadas de antes se el valor se encontra dentro de la lista
    #de coordinadas vacias esse valor passa senon no passa el filtro y la lista de coordinadas quedara mas pequeña que el numero en la lista de barcos indexada por el numero de loops

    confirm_vectores=list(filter(lambda x : x if len(list(filter(lambda y: y if y in empty_list else None,x)))==list_boats[number_loops] else None,possible_vectors))

    return confirm_vectores


def find_hole(grid,hole):

    # aqui es donde hago la lista de coordinadas vacias, quando uno hace un array de un where le sale una tupla de array quando tiene mas de una dimencion
    # y isso para mi no me valia

        empty_tuple=np.array(np.where(grid==hole))

        
        # enton criei un mecanismo pra transformar essa tupla de arrays en una lista de listas que era mas pratico, 
        # esta funcion pode dizer onde esta las coordinadas de qualquer coisa en un array de 2D
        # dando un output de una lista con listas

        empty_list=list(map(lambda x: [int(empty_tuple[0,x])]+[int(empty_tuple[1,x])],range(int(len(empty_tuple[0])))))

        return empty_list


        # aqui esta un mecanismo recursivo para cambiar un valor en la matrix
        # isto lo hice porque mi juego pode coller barcos de qualquer tamaño creados por el jugador
def change_grid(final_list,grid):
    
    grid[final_list[0][0]][final_list[0][1]]="O"
    
    final_list.pop(0)
    
    if len(final_list)!=0:
        
        change_grid(final_list,grid)
 
    else:
        
        return grid

# aqui un objeto barco nada especial
class Boat:
    def __init__(self,size,coord):
        self.size=size
        self.coord=coord


# nesta funcion hago update de 2 dicionarios un que vai tener como key las coordinadas delos barcos en str indexadas por un counter negativo
# y un valor nombre que esta condicionado por los loops que vai a coller
# y outro que tiene una key que es el valor del anterior
# y un valor que es la class boat de antes donde vai a tener el tamaño y sus coordinadas
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

# isto es una funcion para verificar las coordinadas de ataque del usuario
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

# aqui utilizo el previamente explicado calculador de vector y para calcular dependendo del barco que esta a ser recollido en la lista
# de barcos el vector de todas las directiones
    

        down=vector_calculator(boat_list[number_loops],[1,0])
        up=vector_calculator(boat_list[number_loops],[-1,0])
        right=vector_calculator(boat_list[number_loops],[0,1])
        left=vector_calculator(boat_list[number_loops],[0,-1])

        # incluindo en diagonal

        d_up_rg=up+right
        d_up_lf=up+left
        d_down_rg=down+right
        d_down_lf=down+left

        # aqui hago la lista de coordinadas vacias

        empty_list=find_hole(grid," ")

        # y aqui checo se todas las coordinadas del vector entao en essa listas as que no estan son filtradas
        
        down_coord=confirm_coor(vector=down,empty_list=empty_list,list_boats=boat_list,number_loops=number_loops)
        up_coord=confirm_coor(vector=up,empty_list=empty_list,list_boats=boat_list,number_loops=number_loops)
        left_coord=confirm_coor(vector=left,empty_list=empty_list,list_boats=boat_list,number_loops=number_loops)
        right_coord=confirm_coor(vector=right,empty_list=empty_list,list_boats=boat_list,number_loops=number_loops)
        up_rg_coord=confirm_coor(vector=d_up_rg,empty_list=empty_list,list_boats=boat_list,number_loops=number_loops)
        up_lf_coord=confirm_coor(vector=d_up_lf,empty_list=empty_list,list_boats=boat_list,number_loops=number_loops)
        dow_rg_coord=confirm_coor(vector=d_down_rg,empty_list=empty_list,list_boats=boat_list,number_loops=number_loops)
        dow_lf_coord=confirm_coor(vector=d_down_lf,empty_list=empty_list,list_boats=boat_list,number_loops=number_loops)

        # y aqui junto totas los vectores possibles en todas as coordinadas vacias

        all_directions=down_coord+up_coord+left_coord+right_coord+up_lf_coord+up_rg_coord+dow_lf_coord+dow_rg_coord
        return all_directions

# y aqui es que empeza la locura, este es un de las peças de mi algoritmo de calculo de probabilidades de posiciones
# para el ordenador
# lo que hace es filtar todo las coordinades que vienen del primeiro filtro y deja solo los valores que estan en coordinadas vacias
def second_filter_X(grid,first_filter):

    empty_coords=find_hole(grid," ")

    second_filter=list(map(lambda x : list(filter(lambda y: y if y in empty_coords else None,x)),first_filter))

    return second_filter


# esta seguinte funcion lo que hace es coller todas las possible coordinadas de la grella de attack del ordenador, 
# esta grella teria sido limpia y so teria las marcas de fallar alvo sin los acertos
# mira de todas las aquelles vectores que tienen una coordinada expecifica, esta coordinada vai a ser una coordinada que
# foi acertada por el ordenador pero que ainda no pode eliminar por no ter passado alguna condicion( mais explicado a diante),
# todos los vectorees que tienen essa coordinada quedan los demais son filtrados
# coord es el conjunto de coordinadas acertadas que el ordenador ainda no apagou y esta sendo indexado por el loop
# assim chequea todas las coordinadas y se queda solo con los vectores que tenien ao menos una de essas coordinadas pero se queda
# com copias de coordinadas feitas por vectores diferentes pero que tiene algumas de las mismas coordinadas.
# isto despois passa por el seguinte filtro (hablado anteriormente que saca de esses vectores todas as coordinadas onde haja una X)


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
        
        # y aqui esta el mecanismo completo, casi, falta el objecto y sus metodos, del agoritmo
        # estes valores eu los renicio aqui porque me din conta que lo recursivo queda com memoria de tudo,
        # y despois es un lio
        number_loops2=0
        
        hit_list=[]

        # aqui hago una copia da grella que el ordenador usa para atacar
        grid_empty=grid.copy()
        
        # y lle cambio todos los valores de X por " " com explicado anteriormente
        grid_empty[np.where(grid_empty=="X")]=" "

        # collo todas las directions possibles dessa gella
        all_directions=all_posible_position(grid=grid_empty,boat_list=list_boats,number_loops=number_loops)

        # filtro las dos vezes como explicado antes e adajunto al baysian_hit_list
        baysian_hit_list+=hit_coords(grid,all_directions,coord,hit_list=hit_list,number_loops2=number_loops2)
       
        
        if len(list_boats)==number_loops+1:

            # esta parte aqui creo que es redundate pero despois de toda a locura no voy a tocar a nada

                empty_list=find_hole(grid," ")
                
                baysian_list=list(map(lambda y: list(filter(lambda x: x if x in empty_list else None,y)) ,baysian_hit_list))

                # aqui reduzo un [ ] para esta lista tenter solo 2 dimenciones
                
                baysian_list=list(functools.reduce(lambda x, y: x+y,baysian_list))

                # y collo a sua moda
                
                baysian_list=pd.Series(baysian_list,list(map(str,np.arange(len(baysian_list)))))
            
                baysian_list=pd.DataFrame({"coord":baysian_list})
                
                baysian_coords=baysian_list["coord"].mode().tolist()
                
                return baysian_coords
        
        
        number_loops+=1
        return baysian_hammer(grid,coord,list_boats,number_loops,baysian_hit_list)


# esta funcio yo la queria usar pero no funciona no sei porque quizas me poda esplicar Alberto, ou tu ....:)
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

# y agora chegamos a class jugador pero primeiro vou beber un cafe:)
# de volta..hahha.
# aqui tenemos varios atributos tenemos:
# boat_list, una lista composta de numero cada numero es un barco y su valor o espacio que ocupa
# enemy_boat_list, o mesmo pero para o enimigo isto tem utilidade pra o jugador pero foi creado pra ayudar el algoritmo
# grid es la matrix donde estan los barcos del jugador
# destroed_boats es la lista de barcos destruidos
# attack_coord cordinadas donde se atacou
# Hit_coord coordinadas que se atingio
# enemy_grid es la matrix de enemigo donde se ve los ataque hechos
# boat_coord es el dicionario con el key de coordinadas y valor nombre
# boat_obj es el dicionario con el key de nombre y valor objecto boat
# y n que esta ai pra dar nombre a los barcos (esplico despois)


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
        
        
    # primeiro metodo aqui tengo el metodo de cambiar los barcos con valores self , valores de condiciones y valores que usarei para deteminar
    # quantos y quan grandes son los barcos del jugador
    def update_boat_list(self,want_change="n",more_boats="y",range_of_boat=[],number_boats=0):
        
        # perguntamos se querem cambiar de flota
        if want_change=="n":
            
            want_change=input("do you want a costum fleat?(y/n)")
            
            if want_change=="y":
            
                self.boat_list=[]
                
        # se si
        if want_change=="y":
           
            # y se querem mas barcos 
            
            if range_of_boat==[] or more_boats=="y":
                
                # perguntamos o quan grande de barco querem y checkamos se nos dan numeros
                try:
                    
                    range_of_boat= int(input("how big you want these boats to be?"))
                
                except:
                    # senon volvemos a ententar
                    
                    print("can't read it give me a interger")
                    
                    return player.update_boat_list(self,want_change,more_boats,range_of_boat,number_boats)
            
            # hacemos lo mismo para el numero de barcos

            if  number_boats==[] or more_boats=="y":
                
                try:
                    number_boats=int(input("how many of these size boats you want?"))

                except:

                    print("can't read it give me a interger")

                    return player.update_boat_list(self,want_change,more_boats,range_of_boat,number_boats)

        # senon se entende lo se querem cambiar de flota volvemos a ententar
        elif want_change!="n":
            
            want_change="n"
            
            print("don't understand what you are saying? Let's try again with y or n.")
            
            return player.update_boat_list(self,want_change,more_boats,range_of_boat,number_boats)


        # pero se si que se entende que no querem cambiar lhe designamos su flota
        else:

            self.boat_list=[4,3,3,2,2,2,1,1,1,1]

            return 
        
        # aqui vamos sumado los barcos a su flota

        self.boat_list=self.boat_list+[range_of_boat]*number_boats
         

        # y aqui perguntamos se querem mas barcos 
        more_boats=input("want more boats?(y/n)")
        
        # se si volvemos a hacelo
        if more_boats=="y":
        
            player.update_boat_list(self,want_change,more_boats,range_of_boat,number_boats)
        
        # senon se sabe se pergunta outra vez
        elif more_boats!="n":
            
            more_boats="n"
            
            print("don't understand what you are saying? Let's try again with y or n.")
            
            return player.update_boat_list(self,want_change,more_boats,range_of_boat,number_boats)
        
        # y se ja acabou definomos los barcos del jugador y su enemigo en la lista de barcos del jugador
        # coloco con sort revertido por el agoritmo, funciona mellor previndo los barcos mas grandes
        else:
            
            self.boat_list.sort(reverse=True)
            
            self.enemy_boat_list=self.boat_list.copy()
            
            return 

# aqui hacemos lo mismo para a grella
    def grid_change(self,number_rows=0,number_columns=0):
            
            want_change=input("do you want a costum your grid?(y/n)")
               
            
            if want_change not in ["n","y"]:

                    print("please y or n...")

                    player.grid_change(self,number_rows,number_columns)
                
            elif want_change=="y":
                
                # lles coloquei limite basiado en una sola gella pero agora como no tengo display()
                #  a funcionar estas dimenciones ja son demasiado grandes:(

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
            
            # aqui como antes definimos la gella del jugador y la grella que el usara para atacar
            self.grid=np.full((number_rows,number_columns)," ")

            self.enemy_grid=self.grid.copy()



# aqui coloco los barcos
    def place_boats(self,number_loops=0):

        # usando all_poible_position() me quedo con todos los vectores possibles de la grella

        all_directions=all_posible_position(self.boat_list,number_loops,self.grid)

        #se el jugador colocou demasiados barcos no ai problema 
        # senon ai posisiones possible 

        if len(all_directions)==0:

            # chekeo se el barco que estou mirando en el loop es uno
            if self.boat_list[number_loops]==1:

                # se el es uno entonce acabo el loop
                
                print("we can't fit any more boats")
                return self.grid

            else:

                # seno lo es entoces lle digo que no puedo collocar un barco de esse tamaño

                print("we can't fit anymore boats size "+str(self.boat_list[number_loops])+" lets try again." )

                # transformo la lista de barcos en un array

                temp_array=np.array(self.boat_list)

                # saco todos los barcos que sean maiores ou iguales y volvo a tener una lista
                # REVENDO O CODIGO ME DI CONTA DE UNA MANEIRA DE LIAR ME AQUI O ALGORITMO:( PERO AGORA E TARDE Y NO VOY A CAMBIAR
                # ADEMAS QUEM VAI A LER ISTO JAJJAJJA

                self.boat_list=temp_array[temp_array<self.boat_list[number_loops]].tolist()

                # volvo a cambiar el numero de loops a zero por los cambios de la lista
                
                number_loops=0
                
                # y lo delvolvo a la funcion

                return player.place_boats(self,number_loops)
            
        
        # se por outro lado no houve problem con los barcos y sus posisiones
        # escollo una posicion al random
    
        choose_position=all_directions[np.random.randint(len(all_directions))]

        # lhe añado 1 a n que como tenia dicho solo esta aqui para dar nombre en los valores y keys de los 
        # dicionarios coord_boat y obj_boat, y hago los dicionarios de co la position escollida

        self.n+=1
        dic_maker(choose_position,self.boat_coord,self.boat_obj,self.n,self.boat_list,len(choose_position),number_loops)

        # y cambio la grella usando essa misma posicion
        
        change_grid(grid=self.grid,final_list=choose_position)

        
        # quando el len de la lista de barcos es igual al numeber_loops+1 pra
        
        if len(self.boat_list)==number_loops+1:
            return self.grid
        else:
            
        # seno continua    
            number_loops+=1
            player.place_boats(self,number_loops=number_loops)


    
        
       
    # metodo simples de atack
    def attack(self,coord,enemy):

        # appenda a coordinada a lista de attacks

            self.attack_coord.append([coord[0],coord[1]])
            
        # se acerta na grid del enimigo marca en su grid de atack
        # y appenda el valor a Hit_coord    
            if enemy.grid[coord[0]][coord[1]]=="O":
                self.enemy_grid[coord[0]][coord[1]]="X"
                self.Hit_coord.append([coord[0],coord[1]])
                
                
        # seno cambia su grid de atack
                
            elif enemy.grid[coord[0]][coord[1]]==" ":
                self.enemy_grid[coord[0]][coord[1]]="|"
                
            return coord
            
            
# metodo de ser attackado
    def being_attack(self,coord,enemy):
        
        # se lle acertan cambia su grid 

            if self.grid[coord[0]][coord[1]]=="O":
                self.grid[coord[0]][coord[1]]="X"

            # y remove en su dicionario la coordinada en el objecto boat atingido

                self.boat_obj[self.boat_coord[str(coord)]].coord.remove(coord)


            # se el len de la lista de coordinadas del barco_obj atingido for 0 
                
                if len(self.boat_obj[self.boat_coord[str(coord)]].coord)==0:

            # se deja una mensajen que no sale no notebook por falta de espacio del tamaño de barco fundido
                    print("Boat size "+str(self.boat_obj[self.boat_coord[str(coord)]].size)+" has sunk")

            # se apenda na lista destroed_boats el barco fundido
                    self.destroed_boats.append(self.boat_obj[self.boat_coord[str(coord)]].size)
            
            # y se remove el numero corresponde a lista boat_list del jugador atingido
                    self.boat_list.remove(self.boat_obj[self.boat_coord[str(coord)]].size)

            # y a lista de barcos que ten su enemigo de el
                    enemy.enemy_boat_list.remove(self.boat_obj[self.boat_coord[str(coord)]].size)
                    
            # aqui esta outra coisa del algoritmo en que quando en su grid de atake tenga el mismo numero de X
            # que la suma de la lista delos barcos detruido se saca las coordinadas atingidas para buscar novas       
                if len(enemy.enemy_grid[enemy.enemy_grid=="X"])==sum(self.destroed_boats):
                    enemy.Hit_coord=[]
                
                    
                # despois se saca a coordinada key del dicionario boat_coord
                del self.boat_coord[str(coord)]
            

            # se falla lo mismo de siempre
            elif self.grid[coord[0]][coord[1]]==" ":
                self.grid[coord[0]][coord[1]]="|"



    # metodo de pedir coordinada usando o coord_verify 
    def player_attack(self,enemy):
        coord=player.attack(self,coord=coord_verify(self.grid),enemy=enemy)
        return coord
    

    # metodo automatico de attack
    def auto_atack(self,enemy):

        # se el primeiro valor de enemy_boat_list es 1 quer dizer que hacer calculos no ten sentido
        # como tal lo que hace es coller la lista vacia de su grid de attack y hacer random no mas
        
        if self.enemy_boat_list[0]==1:
            
            empty_list=find_hole(self.enemy_grid," ")
            
            coord=empty_list[np.random.randint(len(empty_list))]
            
            coord=player.attack(self,coord,enemy)
            return coord
        
        # se el len de Hit_coord es 0 ou seja no tiene ninguna coordinada atingida entoces lo que hace es
        # coller todas las posiciones possible de el barco maior enemigo porque ai menos random en esses barcos
        # reducir esses vectores a coordinadas y sacar la moda y acer un random da lista que queda

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
            # caso que si que aya valores en hit_coord reprograma todas las variable a 0 y hace recursion con mi baysian_hammer()
            #se mismo assim no sale nada saca todas las coordinadas de Hit_coord y volve a ententar el auto_atack
            
            number_loops=0
            
            number_loops2=0
            
            baysian_hit_list=[]
            
            hit_list=[]
            
            coord=baysian_hammer(self.enemy_grid,self.Hit_coord,self.enemy_boat_list,baysian_hit_list=baysian_hit_list,number_loops=number_loops,hit_list=hit_list,number_loops2=number_loops2)
            
            if coord==[]:
            
                self.Hit_coord=[]
            
                player.auto_atack(self,enemy)
            
           
            # colle una coordinada y vai por el attack()
            coord=coord[np.random.randint(len(coord))]
            
            coord=player.attack(self,coord,enemy)
            
            return coord
                    
    def display_game(self):
        # y aqui se Alberto me ayudara lo haria mellor:(
        # er para hacer display en pandas pero no lo consegui hacer
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

    
def main(player_1=player(),CPU=player(),sec_round=False):
   
    
    if not sec_round: 
        
        player_1=player(boat_list=[4,3,3,2,2,2,1,1,1,1],enemy_boat_list=[4,3,3,2,2,2,1,1,1,1],grid=np.full((10,10)," "),enemy_grid=np.full((10,10)," "),n=0,attack_coord=[],Hit_coord=[],destroed_boats=[])
        
        player_1.grid_change()
        
        player_1.update_boat_list()
        
        CPU=player(boat_list=player_1.boat_list.copy(),grid=player_1.grid.copy(),enemy_grid=player_1.grid.copy(),enemy_boat_list=player_1.boat_list.copy(),n=0,attack_coord=[],Hit_coord=[],destroed_boats=[])
        
        player_1.place_boats()
        
        CPU.place_boats()
        
        clear_output()
        
        player_1.display_game()
    
    player_1_coords=player_1.player_attack(CPU)
    
    CPU.being_attack(player_1_coords,player_1)
    
    clear_output()
    
    player_1.display_game()
    
    input("press enter to continue")
    
    if len(CPU.grid[CPU.grid=="O"])==0:
        
        clear_output()
        
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
    
    clear_output()
    
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

        


        
        

