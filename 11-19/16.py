#   https://edabit.com/challenge/gwqqc5p3oiFXRJAQm
#   Create a function that takes the number of wins draws and losses
#   calculates the number of points a football team has obtained so far.
#   win = 3 points, draw = 1 point, loss = 0 points


def points(wins: int, draws: int, losses: int) -> int:
    win_points = wins * 3
    draw_points = draws * 1
    loss_points = losses * 0
    total_points = win_points + draw_points + loss_points
    return total_points


print(points(3, 4, 2))
