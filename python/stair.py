def stair(steps: int):
    if steps == 0:
        print("__")
        return
    
    step_up = "_|"
    step_down = "|_"
    sep = "  "
    
    if steps < 0:
        steps *= -1
        for i in range((steps+1)):
            print((sep*i) + step_down)
        return

    while steps >= 0:
        print((sep*steps) + step_up)
        steps -= 1
    