def discount(hours, receipt):
    if receipt > 0:
        if hours <= 3:
            discount = 0
        elif hours <= 24:
            discount = 20 + ((hours-3)*20)
        else:
            hoursMinus = hours-24
            discount = 20 + (21*20) + (hoursMinus*10)
    else:
        if hours <= 3:
            discount = 0
        elif hours <= 24:
            discount = 20 + ((hours-3)*20) - (receipt*0.05)
        else:
            hoursMinus = hours-24
            discount = 20 + (21*20) + (hoursMinus*10) - (receipt*0.05)
    return discount

def result(hours, discount):
    pass