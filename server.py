import json
from typing import List


class Player:
    __name: str
    __color: str
    __number_of_kill: int
    __possessed_terrain_count: int

    def __init__(self, json_string):
        self.__name = json_string['name']
        self.__color = json_string['color']
        self.__number_of_kill = json_string['numberOfKill']
        self.__possessed_terrain = json_string['possessedTerrainsCount']
        pass

    def name(self) -> str:
        """
        Name of the agent
        :return:
        """
        return self.__name

    def color(self) -> str:
        """
        Color of the agent
        :return:
        """
        return self.__color

    def number_of_kill(self) -> int:
        """
        Number of kill of the agent
        :return:
        """
        return self.__number_of_kill

    def possessed_terrain_count(self) -> int:
        """
        Number of terrain possessed by the agent
        :return:
        """
        return self.__possessed_terrain_count


class Terrain:
    __terrain_type: int
    __owner_index: int
    __number_of_soldier: int
    __terrain_id: str

    def __init__(self, json_string):
        self.__terrain_type = json_string['terrainType']
        self.__owner_index = json_string['ownerIndex']
        self.__number_of_soldier = json_string['numberOfSoldier']
        self.__terrain_id = json_string['terrainId']

    def type(self) -> int:
        """
        Type of the terrain. 0 - barricade, 1 - factory, 2 - nothing or 3 - in construction
        :return:
        """
        return self.__terrain_type

    def owner_index(self) -> int:
        """
        Index of the owner of the terrain
        :return:
        """
        return self.__owner_index

    def number_of_soldier(self) -> int:
        """
        Number of soldier in garrison
        :return:
        """
        return self.__number_of_soldier

    def id(self) -> str:
        """
        Id of the terrain
        :return:
        """
        return self.__terrain_id


class SoldierGroup:
    __owner_index: int
    __soldier_count: int
    __length: int

    def __init__(self, json_string):
        self.__owner_index = json_string['ownerIndex']
        self.__soldier_count = json_string['soldierCount']
        self.__length = json_string['length']

    def owner_index(self) -> int:
        """
        Index of the owner of the group
        :return:
        """
        return self.__owner_index

    def soldier_count(self) -> int:
        """
        Quantity of soldiers in the group
        :return:
        """
        return self.__soldier_count

    def length(self) -> int:
        """
        Position of the group on a pipe
        :return:
        """
        return self.__length


class Pipe:
    """
    A pipe connect two terrains
    """
    __length: int
    __first: int
    __second: int
    __soldiers: List[SoldierGroup]

    def __init__(self, json_string):
        self.__length = json_string['length']
        self.__first = json_string['first']
        self.__second = json_string['second']
        self.__soldiers = []
        for soldier in json_string['soldiers']:
            self.__soldiers.append(SoldierGroup(soldier))

    def length(self) -> int:
        """
        Total length of the pipe
        :return:
        """
        return self.__length

    def first(self) -> int:
        """
        First terrain index
        :return:
        """
        return self.__first

    def second(self) -> int:
        """
        Second terrain index
        :return:
        """
        return self.__second

    def soldiers(self) -> List[SoldierGroup]:
        """
        List of soldiers on the pipe
        :return:
        """
        return self.__soldiers


class Game:
    __players: List[Player]
    __terrains: List[Terrain]
    __pipes: List[Pipe]

    def __init__(self, json_string):
        self.__players = []

        for player in json_string['players']:
            self.__players.append(Player(player))

        self.__terrains = []

        for terrain in json_string['terrains']:
            self.__terrains.append(Terrain(terrain))

        self.__pipes = []

        for pipe in json_string['pipes']:
            self.__pipes.append(Pipe(pipe))

    def players(self) -> List[Player]:
        return self.__players

    def terrains(self) -> List[Terrain]:
        return self.__terrains

    def pipes(self) -> List[Pipe]:
        return self.__pipes


def convert_data(content: str) -> Game:
    json_data = json.loads(content)
    return Game(json_data)
