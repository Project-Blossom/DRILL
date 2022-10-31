class Player:
    name = 'Player'

    def __init__(my):
        my.x = 100

    def where(my):
        print(my.x)

player = Player()
player.where()

print(Player.name)
print(player.name)

Player.where(player)