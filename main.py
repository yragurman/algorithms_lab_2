def findMinPile(baskets, hours):
    sumBananasInBaskets = 0
    for bananaInOneBasket in baskets:
        sumBananasInBaskets += bananaInOneBasket
    minAmountOfBananas = sumBananasInBaskets // hours
    return minAmountOfBananas

def findMaxPile(baskets):
    maxAmountOfBananas = 0
    for bananas in baskets:
        if maxAmountOfBananas < bananas:
            maxAmountOfBananas = bananas
    return maxAmountOfBananas

def minEatingSpeed(baskets, hours):
    biggestPile = findMaxPile(baskets)
    smallestPile = findMinPile(baskets, hours)
    if len(baskets) > hours:
        return "impossible"
    elif len(baskets) == hours:
        return biggestPile
    else:
        while True:
            speedEating = smallestPile
            if checkSpeedSuitable(baskets, hours, speedEating):
                break
            else:
                smallestPile = speedEating + 1
    return smallestPile

def checkSpeedSuitable(baskets, hours, proposeSpeed):
    eatingTime = 0
    for pile in baskets:
        eatingTime += pile // proposeSpeed + (0 if pile % proposeSpeed == 0 else 1)
    return eatingTime <= hours

print(minEatingSpeed([30,11,23,4,20],6))
