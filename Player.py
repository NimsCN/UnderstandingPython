class player_class:
    def __init__(self,player_turn,health):
        self.health = health
        self.player_turn = player_turn
        self.hand = []
        self.deck = []
        self.discard = []
        self.banished = []
        self.resource_pool = []


