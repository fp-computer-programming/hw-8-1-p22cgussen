# Author CCG 12/9/21

def score_counter(free_throw,two_points,three_points):
    total_pts = (int(free_throw)) + (int(two_points) * 2) + (int(three_points) * 3)
    return(total_pts)

print(score_counter(1,2,3) == 14)
print(score_counter(6,4,3) == 23)
print(score_counter(0,0,3) == 9)
