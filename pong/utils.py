def reset_game(ball, listOfPlayers):
    for player in listOfPlayers:
        player.reset()
    ball.reset()