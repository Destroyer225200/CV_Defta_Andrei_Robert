from math import floor


def gregorian_to_julian(y, m, d, hh, mm, ss):

    if m <= 2:
        y -= 1
        m += 12
    JD = floor(365.25 * y) + floor(30.6001 * (m + 1)) + d + (hh / 24 + mm / 1440 + ss / 86400) + 1720981.5
    return JD


def julian_to_modified_julian(JD):
    # Conversie din JD în MJD
    return JD - 2400000.5


def julian_to_gregorian(JD):
    # Conversie inversă din JD la data gregoriană
    a = floor(JD + 0.5)
    b = a + 1537
    c = floor((b - 122.1) / 365.25)
    d = floor(365.25 * c)
    e = floor((b - d) / 30.6001)
    D = b - d - floor(30.6001 * e)
    M = e - 1 - 12 * floor(e / 14)
    Y = c - 4715 - floor((7 + M) / 10)
    return Y, M, D


def day_of_week(JD):

    N_star = int(floor(JD + 0.5) % 7)
    days = ["L", "M", "Mi", "J", "V", "S", "D"]
    return days[N_star]


def gps_week_and_day(JD):
    # Calculul săptămânii GPS și al zilei GPS
    if 2444244.5 <= JD < 2451412.5:
        GPSWEEK = int((JD - 2444244.5) / 7)
    elif 2451412.5 <= JD < 2458580.5:
        GPSWEEK = int((JD - 2451412.5) / 7)
    elif JD >= 2458580.5:
        GPSWEEK = int((JD - 2458580.5) / 7)
    else:
        GPSWEEK = None
    GPSDAY = int((JD + 0.5) % 7)
    return GPSWEEK, GPSDAY


def gps_seconds_of_week(JD, hh, mm, ss):
    GPSDAY = (JD + 0.5) % 7
    N_star = day_of_week(JD)
    GPST = N_star * 86400 + hh * 3600 + mm * 60 + ss
    return GPST


def seconds_of_day(hh, mm, ss):
    # Calculul secundei zilei
    return hh * 3600 + mm * 60 + ss


def main():

    day = int(input("Ziua (zz): "))
    month = int(input("Luna (ll): "))
    year = int(input("Anul (aaaa): "))
    hour = int(input("Ora (hh): "))
    minute = int(input("Minutul (mm): "))
    second = int(input("Secunda (ss): "))

    JD = gregorian_to_julian(year, month, day, hour, minute, second)
    MJD = julian_to_modified_julian(JD)

    y, m, d = julian_to_gregorian(JD)

    day_of_week_str = day_of_week(JD)

    GPSWEEK, GPSDAY = gps_week_and_day(JD)

    GPST = gps_seconds_of_week(JD, hour, minute, second)
    sec_of_day = seconds_of_day(hour, minute, second)

    print("\nRezultate:")
    print(f"Julian Date (JD): {JD}")
    print(f"Modified Julian Date (MJD): {MJD}")
    print(f"Data inversă (Gregoriană): {d}-{m}-{y}")
    print(f"Ziua săptămânii: {day_of_week_str}")
    print(f"Săptămâna GPS: {GPSWEEK}")
    print(f"Ziua GPS: {GPSDAY}")
    print(f"Secunda săptămânii GPS: {GPST}")
    print(f"Secunda zilei: {sec_of_day}")


# Apelul funcției principale
if __name__ == "__main__":
    main()
