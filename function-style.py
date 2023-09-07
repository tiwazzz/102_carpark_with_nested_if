def discount(hour, receipt):
    if receipt > 0:
        if hour <= 3:
            discount = 0
        elif hour <= 24:
            discount = 20 + ((hour-3)*20)
        else:
            hourMinus = hour-24
            discount = 20 + (21*20) + (hourMinus*10)
    else:
        if hour <= 3:
            discount = 0
        elif hour <= 24:
            discount = 20 + ((hour-3)*20) - (receipt*0.05)
        else:
            hourMinus = hour-24
            discount = 20 + (21*20) + (hourMinus*10) - (receipt*0.05)
    return discount