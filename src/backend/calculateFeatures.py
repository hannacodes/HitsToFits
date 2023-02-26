import random as r
import json
import hits

import fits

# [blue, red, green, yellow, orange, pink, purple, white, black, gray, brown, tan]
colors = ["#0000FF", "#FF0000", "#00FF00", "#FFFF00", "#ffa500", "#ff69b4", "#a020f0", "#FFFFFF", "#000000", "#7a7a7a", "#8b4513", "#f5deb3"]
chooseColor = []



def hexToRgb(hexColor, rgb):
    rgb[0] = int(hexColor[1:3], 16)
    rgb[1] = int(hexColor[3:5], 16)
    rgb[2] = int(hexColor[5:], 16)

def initialUpdate(dance_val, color, colorWeights):
    writefile = open('colorWeights.json', 'w')
    colorWeights["currentDanceAndVal"] = dance_val
    colorWeights["currentColor"] = color
    json.dump(colorWeights, writefile)
    writefile.close()

def calcColor(danceability, valence, rgb):
    readfile = open('colorWeights.json', 'r')
    colorWeights = json.load(readfile)
    readfile.close()
    if (danceability <= .5):
        if (valence <= .25):
            hexColor = colors[0]    # blue
            hexToRgb(hexColor, rgb)
            initialUpdate(0, hexColor, colorWeights)
        elif (valence <= .75):
            chooseColor = r.choices(colors, weights= colorWeights.get("lowDance_midVal"))
            hexColor = chooseColor[0]
            hexToRgb(hexColor, rgb)
            initialUpdate(1, hexColor, colorWeights)
        else:
            hexColor = colors[2]    # green
            hexToRgb(hexColor, rgb)
            initialUpdate(2, hexColor, colorWeights)
    elif (danceability <= .75):
        if (valence <= .25):
            chooseColor = r.choices(colors, weights= colorWeights.get("midDance_lowVal"))
            hexColor = chooseColor[0]
            hexToRgb(hexColor, rgb)
            initialUpdate(3, hexColor, colorWeights)
        elif (valence <= .75):
            chooseColor = r.choices(colors, weights= colorWeights.get("midDance_midVal"))
            hexColor = chooseColor[0]
            hexToRgb(hexColor, rgb)
            initialUpdate(4, hexColor, colorWeights)
        else:
            chooseColor = r.choices(colors, weights= colorWeights.get("midDance_highVal"))
            hexColor = chooseColor[0]
            hexToRgb(hexColor, rgb)
            initialUpdate(5, hexColor, colorWeights)
    else:
        if (valence <= .25):
            hexColor = colors[1]  # red
            hexToRgb(hexColor, rgb)
            initialUpdate(6, hexColor, colorWeights)
        elif (valence <= .75):
            chooseColor = r.choices(colors, weights= colorWeights.get("highDance_midVal"))
            hexColor = chooseColor[0]
            hexToRgb(hexColor, rgb)
            initialUpdate(7, hexColor, colorWeights)
        else:
            hexColor = colors[3]    # yellow
            hexToRgb(hexColor, rgb)
            initialUpdate(8, hexColor, colorWeights)
    

def calcBrightness(energy, rgb):
    if (energy < .6):
        adjustedEnergy = energy + 0.4
        red = rgb[0] * adjustedEnergy
        green = rgb[1] * adjustedEnergy
        blue = rgb[2] * adjustedEnergy
        rgb[0] = int(red)
        rgb[1] = int(green)
        rgb[2] = int(blue)


def calcTempo(tempo, rgb):
    if (tempo > .5):
        rgb[0] = 255 - rgb[0]
        rgb[1] = 255 - rgb[1]
        rgb[2] = 255 - rgb[2]

def searchClosetForTops(rgb):
    closet = fits.getShirtColors("hit2fit")
    bestFitValues = [1000, 1000]
    bestFit = [[], []]
    for article in closet:
        value = abs(rgb[0] - article[0]) + abs(rgb[1] - article[1]) + abs(rgb[2] - article[2])
        if value < bestFitValues[0]:
            bestFitValues[1] = bestFitValues[0]
            bestFitValues[0] = value
            bestFit[1] = bestFit[0]
            bestFit[0] = article
        elif value < bestFitValues[1]: 
            bestFitValues[1] = value
            bestFit[1] = article
    return r.choice(bestFit)

def searchClosetForBottoms(rgb):
    closet = fits.getPantColors("hit2fit")
    bestFitValue = 1000
    bestFit = []
    for article in closet:
        value = abs(rgb[0] - article[0]) + abs(rgb[1] - article[1]) + abs(rgb[2] - article[2])
        if value < bestFitValue:
            bestFitValue = value
            bestFit = article
    return bestFit

def updateWeights(opinion):
    readfile = open('colorWeights.json', 'r')
    colorWeights = json.load(readfile)
    readfile.close()
    danceval = colorWeights.get("currentDanceAndVal")
    if (danceval == 0 or danceval == 2 or danceval == 6 or danceval == 8):
        return
    else:
        dancevalKey = ""
        if (danceval == 1):
            dancevalKey = "lowDance_midVal"
        elif (danceval == 3):
            dancevalKey = "midDance_lowVal"
        elif (danceval == 4):
            dancevalKey = "midDance_midVal"
        elif (danceval == 5):
            dancevalKey = "midDance_highVal"
        else:
            dancevalKey = "highDance_midVal"

        colorIndex = colors.index(colorWeights.get("currentColor"))
        
        if opinion == "yes":
            colorWeights.get(dancevalKey)[colorIndex] += 1
        else:
            colorWeights.get(dancevalKey)[colorIndex] -= 1
        
        writefile = open('colorWeights.json', 'w')
        json.dump(colorWeights, writefile)
        writefile.close()


def main():
    # rgb[0]= red 
    # rgb[1] = green
    # rgb[2] = blue
    rgb = [0, 0, 0]
    features = hits.getAllData("https://open.spotify.com/track/0G21yYKMZoHa30cYVi1iA8?si=94d7d28d8d2d44f2")
    danceability = hits.getDanceability(features)
    valence = hits.getValence(features)
    energy = hits.getEnergy(features)
    #loudness = hits.getLoudness(features)

    #print(danceability)
    #print(valence)
    #print(energy)
    #print(loudness)

    calcColor(danceability, valence, rgb)
    #print(rgb)
    calcBrightness(energy, rgb)
    #print(rgb)
    
    print(searchClosetForTops(rgb))
    bot_rgb = rgb
    #calcLoudness(loudness, bot_rgb)
    #print(bot_rgb)
    print(searchClosetForBottoms(bot_rgb))

    

    opinion = "yes"
    #updateWeights(opinion)


if __name__ == "__main__":
    main()
