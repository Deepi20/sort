class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        object_dict = {
            "name": self.name,
            "score": self.score
        }
        return json.dumps(object_dict)
        

    def comparator(player_1, player_2):
        ''' Custom comparator '''
        if player_1.score > player_2.score:
            return -1

        if player_1.score < player_2.score:
            return 1

        if player_1.name < player_2.name:
            return -1

        if player_1.name > player_2.name:
            return 1

        return 0

n = int(raw_input())
data = []
for i in range(n):
    name, score = raw_input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, cmp=Player.comparator)
for i in data:
    print i.name, i.score
