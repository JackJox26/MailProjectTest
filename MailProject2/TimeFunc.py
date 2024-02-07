import time as tm

def StartDate(delay=0):
    #Declaration of variable
    dayInSeconds = 86400
    LocalTimeSeconds = tm.time() + delay*(365.2425/12)* dayInSeconds
    LocalTimeSecondsStart = LocalTimeSeconds
    result = tm.localtime(LocalTimeSecondsStart)

    #Fonction working
    while(result[2]!=1):
        if (result[2] <= 15):
            LocalTimeSecondsStart = LocalTimeSecondsStart - dayInSeconds
            result = tm.localtime(LocalTimeSecondsStart)
        else:
            LocalTimeSecondsStart = LocalTimeSecondsStart + dayInSeconds
            result = tm.localtime(LocalTimeSecondsStart)
    time_string = tm.strftime("%d/%m/%Y", result)
    return time_string


def EndDate(delay = 0):
    #Declaration of variable
    dayInSeconds = 86400
    LocalTimeSeconds = tm.time() + delay*(365.2425/12)* dayInSeconds
    LocalTimeSecondsEnd = LocalTimeSeconds
    result2 = tm.localtime(LocalTimeSecondsEnd)

    #Fonction Working
    if (LocalTimeSecondsEnd > 0):
        if (result2[2] <= 15):
            #special pour le premier jour
            if (result2[2] == 1):
                LocalTimeSecondsEnd = LocalTimeSecondsEnd + dayInSeconds
                result2 = tm.localtime(LocalTimeSecondsEnd)

            while(result2[2]!=1):
                LocalTimeSecondsEnd = LocalTimeSecondsEnd + dayInSeconds
                result2 = tm.localtime(LocalTimeSecondsEnd)

        else:
            LocalTimeSecondsEnd = LocalTimeSecondsEnd + 18 * dayInSeconds
            while(result2[2]!=1):
                LocalTimeSecondsEnd = LocalTimeSecondsEnd + dayInSeconds
                result2 = tm.localtime(LocalTimeSecondsEnd)

    #Print last days
    LocalTimeSecondsEnd= LocalTimeSecondsEnd-dayInSeconds
    results_aux = tm.localtime(LocalTimeSecondsEnd)
    time_string3 = tm.strftime("%d/%m/%Y", results_aux)
    return time_string3
