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


def calcValence(valence, rgb):
    high_valence = False
    color_value = 255 * valence
    randomColor = r.randint(0,1)

    if (valence <= .25):
        rgb[2] = int(color_value)
    elif (valence >= .25 and valence <= .5):
        # blue = 0
        # green = 1
        if (randomColor == 1):
            rgb[1] = int(color_value)
        else: 
            rgb[2] = int(color_value)
    elif (valence >= .5 and valence <= .75):
        # blue = 0
        # red = 1
        if (randomColor == 1):
            rgb[0] = int(color_value)
        else: 
            rgb[2] = int(color_value)
    else: 
        rgb[0] = int(color_value)
        high_valence = True
    
    return high_valence


def calcEnergy(energy, rgb):
    high_energy = False
    color_value = 255 * energy
    randomColor = r.randint(0,1)

    if (energy <= .25):
        rgb[1] = int(color_value)
    elif (energy >= .25 and energy <= .5):
        # blue = 0
        # green = 1
        if (randomColor == 1):
            rgb[1] = int(color_value)
        else: 
            rgb[2] = int(color_value)
    elif (energy >= .5 and energy <= .75):
        # green = 0
        # red = 1
        if (randomColor == 1):
            rgb[0] = int(color_value)
        else: 
            rgb[1] = int(color_value)
    else: 
        rgb[0] = int(color_value)
        high_energy = True
    
    return high_energy


def main():
    # rgb[0]= red 
    # rgb[1] = green
    # rgb[2] = blue
    dance_rgb = [0, 0, 0]
    danceability = 0.6
    calcDanceability(danceability, dance_rgb)
    print(dance_rgb)

    valence_rgb = [0, 0, 0]
    valence = 0.5
    calcValence(valence, valence_rgb)
    print(valence_rgb)
    # calculate avg among dance_rgb, valence_rgb, and energy_rgb 

if __name__ == "__main__":
    main()
