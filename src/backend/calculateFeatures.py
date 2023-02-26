import random as r
import json

# [blue, red, green, yellow, orange, pink, purple, white, black, gray, brown, tan]
colors = ["#0000FF", "#FF0000", "#00FF00", "#FFFF00", "#ffa500", "#ff69b4", "#a020f0", "#FFFFFF", "#000000", "#7a7a7a", "#8b4513", "#f5deb3"]

readfile = open('colorWeights.json', 'r')
colorWeights = json.load(readfile)
readfile.close()

#writefile = open('colorWeights.json', 'w')
#writefile.close()
def hexToRgb(hexColor, rgb):
    rgb[0] = int(hexColor[1:3], 16)
    rgb[1] = int(hexColor[3:5], 16)
    rgb[2] = int(hexColor[5:], 16)

def calcColor(danceability, valence, rgb):
    if (danceability <= .25):
        if (valence <= .25):
            hexColor = colors[0]    # blue
            hexToRgb(hexColor, rgb)
        elif (valence <= .75):
            chooseColor = r.choices(colors, weights= colorWeights.get("lowDance_midVal"))
            hexColor = chooseColor[0]
            hexToRgb(hexColor, rgb)
        else:
            hexColor = colors[2]    # green
            hexToRgb(hexColor, rgb)
    elif (danceability <= .75):
        if (valence <= .25):
            chooseColor = r.choices(colors, weights= colorWeights.get("midDance_lowVal"))
            hexColor = chooseColor[0]
            hexToRgb(hexColor, rgb)
        elif (valence <= .75):
            chooseColor = r.choices(colors, weights= colorWeights.get("midDance_midVal"))
            hexColor = chooseColor[0]
            hexToRgb(hexColor, rgb)
        else:
            chooseColor = r.choices(colors, weights= colorWeights.get("midDance_highVal"))
            hexColor = chooseColor[0]
            hexToRgb(hexColor, rgb)
    else:
        if (valence <= .25):
            hexColor = colors[1]  # red
            hexToRgb(hexColor, rgb)
        elif (valence <= .75):
            chooseColor = r.choices(colors, weights= colorWeights.get("highDance_midVal"))
            hexColor = chooseColor[0]
            hexToRgb(hexColor, rgb)
        else:
            hexColor = colors[3]    # yellow
            hexToRgb(hexColor, rgb)
    

def calcBrightness(energy, rgb):
    if (energy < .6):
        adjustedEnergy = energy + 0.4
        red = rgb[0] * adjustedEnergy
        green = rgb[1] * adjustedEnergy
        blue = rgb[2] * adjustedEnergy
        rgb[0] = int(red)
        rgb[1] = int(green)
        rgb[2] = int(blue)


def main():
    # rgb[0]= red 
    # rgb[1] = green
    # rgb[2] = blue
    rgb = [0, 0, 0]
    danceability = .2
    valence = .5
    energy = .2
    calcColor(danceability, valence, rgb)
    print(rgb)
    calcBrightness(energy, rgb)
    print(rgb)

if __name__ == "__main__":
    main()
