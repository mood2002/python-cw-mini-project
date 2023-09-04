# write your code here
def padel_court_cost(court_type):
    if court_type == "indoor":
        return 30
    elif court_type == "out door":
        return 20

def rackets_cost (racket_brand):
    if racket_brand ==" bullpadel":
        return 120
    elif racket_brand == "nox":
        return 140
    elif racket_brand == "siux":
        return 200


def padel_ball_cost(ball_boxes):
    if ball_boxes == 1 :
        return (2)
    elif ball_boxes == 2 :
        return (3.5)
    elif ball_boxes == 3:
        return (5)

def padel_game_cost ():
    courts_type=input("enter the court type")
    rackets_brand=input("enter the racket brand")
    balls_boxes=int(input("enter the number of ball boxes"))
    total= padel_court_cost(courts_type) + rackets_cost (rackets_brand) + padel_ball_cost(balls_boxes)
    return total
print(padel_game_cost ())
