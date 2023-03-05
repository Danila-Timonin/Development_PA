def reformat_timestamp(timestamp):
    t_otsch = 1970
    flag = 0
    month = [31, 28, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31]
    days_in_ts = timestamp // (24 * 60 * 60)
    sec_in_ts = timestamp % (24 * 60 * 60)

    while days_in_ts >= 365:
        if (t_otsch % 400 == 0 or
                (t_otsch % 4 == 0 and
                 t_otsch % 100 != 0)):
            if days_in_ts < 366:
                break
            days_in_ts -= 366

        else:
            days_in_ts -= 365

        t_otsch += 1
    ves_d = days_in_ts + 1

    if t_otsch % 400 == 0 or (t_otsch % 4 == 0 and t_otsch % 100 != 0):
        flag = 1
    m = 0
    index = 0

    if flag == 1:
        while True:
            if index == 1:
                if ves_d - 29 < 0:
                    break
                m += 1
                ves_d -= 29
            else:
                if ves_d - month[index] < 0:
                    break
                m += 1
                ves_d -= month[index]
            index += 1
    else:
        while True:
            if ves_d - month[index] < 0:
                break
            m += 1
            ves_d -= month[index]
            index += 1
    if ves_d > 0:
        m += 1
        date = ves_d
    else:
        if m == 2 and flag == 1:
            date = 29
        else:
            date = month[m - 1]
    hours = sec_in_ts // 3600
    minutes = (sec_in_ts % 3600) // 60
    seconds = (sec_in_ts % 3600) % 60

    return str(t_otsch) + "-" + str(m) + "-" + str(date) + "\t" + str(hours + 4) +\
        ":" + str(minutes) + ":" + str(seconds)

