import random as r


def calcDanceability(danceability, rgb):
    high_dance = False
    color_value = 255 * danceability
    randomColor = r.randint(0,1)
    # low danceability = more blue
    if (danceability <= .25):
        rgb[2] = int(color_value)
    elif (danceability >= .25 and danceability <= .5):
        # blue = 0
        # green = 1
        if (randomColor == 1):
            rgb[1] = int(color_value)
        else: 
            rgb[2] = int(color_value)
    elif (danceability >= .5 and danceability <= .75):
        # blue = 0
        # red = 1
        if (randomColor == 1):
            rgb[0] = int(color_value)
        else: 
            rgb[2] = int(color_value)
    else: 
        rgb[0] = int(color_value)
        high_dance = True
    
    return high_dance


def main():
    # rgb[0]= red 
    # rgb[1] = green
    # rgb[2] = blue
    dance_rgb = [0, 0, 0]
    danceability = 0.6
    calcDanceability(danceability, dance_rgb)
    print(dance_rgb)

    # calculate avg among dance_rgb, valence_rgb, and energy_rgb 

if __name__ == "__main__":
    main()
