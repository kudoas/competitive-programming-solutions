d, w = map(int, input().split())
w = w/60


def wind_direction(a):
    if 112.5 <= a < 337.5:
        d = "NNE"
    elif 337.5 <= a < 562.5:
        d = "NE"
    elif 562.5 <= a < 787.5:
        d = "ENE"
    elif 787.5 <= a < 1012.5:
        d = "E"
    elif 1012.5 <= a < 1237.5:
        d = "ESE"
    elif 1237.5 <= a < 1462.5:
        d = "SE"
    elif 1462.5 <= a < 1687.5:
        d = "SSE"
    elif 1687.5 <= a < 1912.5:
        d = "S"
    elif 1912.5 <= a < 2137.5:
        d = "SSW"
    elif 2137.5 <= a < 2362.5:
        d = "SW"
    elif 2362.5 <= a < 2587.5:
        d = "WSW"
    elif 2587.5 <= a < 2812.5:
        d = "W"
    elif 2812.5 <= a < 3037.5:
        d = "WNW"
    elif 3037.5 <= a < 3262.5:
        d = "NW"
    elif 3262.5 <= a < 3487.5:
        d = "NNW"
    else:
        d = "N"
    return d


def wind_speed(n):
    if n < 0.25:
        spe = 0
    elif n < 1.55:
        spe = 1
    elif n < 3.35:
        spe = 2
    elif n < 5.45:
        spe = 3
    elif n < 7.95:
        spe = 4
    elif n < 10.75:
        spe = 5
    elif n < 13.85:
        spe = 6
    elif n < 17.15:
        spe = 7
    elif n < 20.75:
        spe = 8
    elif n < 24.45:
        spe = 9
    elif n < 28.45:
        spe = 10
    elif n < 32.65:
        spe = 11
    elif 32.65 <= n:
        spe = 12
    return spe


if wind_speed(w) == 0:
    print('C', 0)
    exit()

print(wind_direction(d), wind_speed(w))
