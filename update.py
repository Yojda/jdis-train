from typing import List

from actions import Action, create_move_action, create_build_barricade_action, create_build_factory_action
from server import Game
import env


class Agent:
    def __init__(self):
        pass

    def update(self, game: Game) -> List[Action]:
        f"""
        Update function
        
        :param game: Game Data
        :return: {List[Action]}
        """
        player_name = env.PLAYER_NAME

        terrains = game.terrains()
        players = game.players()
        pipes = game.pipes()

        # Get the player
        player = [index for index in range(len(players)) if players[index].name() == player_name]

        if len(player) == 0:
            # If the player was not found, return no orders
            return []

        player_index = player[0]

        # Get the terrains of the player
        player_terrains = [(index, terrains[index]) for index in range(len(terrains)) if
                           terrains[index].owner_index() == player_index]
        player_terrains_index = [terrain[0] for terrain in player_terrains]
        involved_pipes = [pipe for pipe in pipes if pipe.first() in player_terrains_index or pipe.second() in player_terrains_index]

        print(f"{player_terrains_index=}")

        neighbouring_terrains = [k.first() for k in involved_pipes if k.first() not in player_terrains_index] + [k.second() for k in involved_pipes if k.second() not in player_terrains_index]
        print(f"{neighbouring_terrains=}")

        ##### ACTIONS

        orders = []
        # for pipe in pipes:
        #     # If the first terrain of a connection belongs to the player and have at least one soldier
        #     if (pipe.first() in player_terrains_index and
        #             pipe.second() not in player_terrains_index and
        #             terrains[pipe.first()].number_of_soldier() > 0):
        #         # Send one soldier to the end of the connection
        #         orders.append(create_move_action(terrains[pipe.first()].id(), terrains[pipe.second()].id(), 1))
        #
        #     # If the second terrain of a connection belongs to the player and have at least one soldier
        #     if (pipe.second() in player_terrains_index and
        #             pipe.first() not in player_terrains_index and
        #             terrains[pipe.second()].number_of_soldier() > 0):
        #         # Send one soldier to the end of the connection
        #         orders.append(create_move_action(terrains[pipe.second()].id(), terrains[pipe.first()].id(), 1))

        for ter in player_terrains_index:
            involved_pipes = [pipe for pipe in pipes if
                              pipe.first() == ter or pipe.second() == ter]
            neighbouring_terrains = [k.first() for k in involved_pipes if k.first() not in player_terrains_index] + [
                k.second() for k in involved_pipes if k.second() not in player_terrains_index]
            print(f"{ter=}, {neighbouring_terrains=}, {terrains[ter].number_of_soldier()=}, {terrains[ter].type()=}")
            numberSoldiers = terrains[ter].number_of_soldier()

            for neigh in neighbouring_terrains:
                if (terrains[ter].type() == 3):
                    print(f"{ter} under construction")
                # If the neighbour terrain is not a factory and have at least one soldier
                quantityOfEnemies = terrains[neigh].number_of_soldier()
                if (terrains[ter].type() == 2):
                    # Build a factory on the terrain
                    print(f"Building factory on {ter}")
                    orders.append(create_build_factory_action(ter))
                    break
                elif (quantityOfEnemies+1 < numberSoldiers):
                    orders.append(create_move_action(terrains[ter].id(), terrains[neigh].id(), quantityOfEnemies+1))
                    print(f"Moving {quantityOfEnemies+1} soldiers from {ter} to {neigh}")
                    numberSoldiers -= quantityOfEnemies+1
                    break


        print(f"{orders=}")
        # Returns the order for each terrain of the player
        return orders
