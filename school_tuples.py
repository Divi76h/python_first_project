def appending_9():
    global tup
    tup += (9,)

    print(tup)


def appending_0():
    global tup
    tup = (0,) + tup

    print(tup)


def remove_last_element():
    global tup
    tup = tup[:len(tup) - 1]

    print(tup)


def remove_fist_element():
    global tup
    tup = tup[1:]

    print(tup)


def remove_third_element():
    global tup
    tup = tup[:2] + tup[3:]

    print(tup)


def remove_sixth_element():
    global tup
    temp = ()

    for i in range(len(tup)):
        if tup[i] == 6:
            pass
        else:
            temp += (tup[i],)

    print(temp)


def element_6equals100():
    global tup
    temp = ()

    for i in range(len(tup)):
        if i == 5:
            temp += (100,)
        else:
            temp += (tup[i],)

    print(temp)


def element_5equals50():
    global tup
    temp = ()

    for i in range(len(tup)):
        if tup[i] == 5:
            temp += (50,)
        else:
            temp += (tup[i],)

    print(temp)


tup = (1, 2, 3, 4, 5, 6, 7, 8)
print(tup)

appending_9()
appending_0()
remove_last_element()
remove_fist_element()
remove_third_element()
remove_sixth_element()
element_6equals100()
element_5equals50()
