

#number of pillars (≥ 1);
#distance between pillars (10 - 30 meters);
#width of the pillar (10 - 50 centimeters).
#Calculate the distance between the first and the last pillar in centimeters
#distance is in meters, answer must be in CM

def pillars(num_pill, dist, width):
    result = ((num_pill - 2) * width) + (((num_pill - 1) * dist) * 100)
    if result > 0:
        return result
    if result <= 0:
        return 0
