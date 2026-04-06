def fine(authorized_speed, actual_speed):
    speed = actual_speed - authorized_speed
    if authorized_speed  > actual_speed:
        return 0
    else:
        if 0 < speed <= 10:
            return max(12.5,speed*5)
        elif speed > 10:
            return max(12.5,speed*5)*2
print(fine(12,10))
print(fine(10,25))