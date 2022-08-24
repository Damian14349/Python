from rocket import Rocket_Board, Rocket

#board = Rocket_Board(2)
#board2 = Rocket_Board(3)

#board[0].x = 4

rocket1 = Rocket(altitude=6, speed=2)
rocket2 = Rocket(altitude=4, speed=5)
print("Distance between rockets is:", Rocket_Board.get_distance(rocket1, rocket2))


