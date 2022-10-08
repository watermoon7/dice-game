def reset():
    file = open("text.txt", "w") 
    file.write("Top scores")
    file.write("\n1: - at 0")
    file.write("\n2: - at 0")
    file.write("\n3: - at 0")
    file.write("\n4: - at 0")
    file.write("\n5: - at 0")
    file.close()

def topscores(user, score):
    global b, c, d, e, f, b2, c2, d2, e2, f2
    if score > int(b2):
        print(user + ": Input your name to be viewed on the leaderboards: ")
        usertemp = input()
        f = e
        e = d
        d = c
        c = b
        b = "1: " + usertemp + " at " + str(score) + "\n"
    elif score > int(c2):
        print(user + ": Input your name to be viewed on the leaderboards: ")
        usertemp = input()
        f = e
        e = d
        d = c
        c = "2: " + usertemp + " at " + str(score) + "\n"
    elif score > int(d2):
        print(user + ": Input your name to be viewed on the leaderboards: ")
        usertemp = input()
        f = e
        e = d
        d = "3: " + usertemp + " at " + str(score) + "\n"
    elif score > int(e2):
        print(user + ": Input your name to be viewed on the leaderboards: ")
        usertemp = input()
        f = e
        e = "4: " + usertemp + " at " + str(score) + "\n"
    elif score > int(f2):
        print(user + ": Input your name to be viewed on the leaderboards: ")
        usertemp = input()
        f = "5: " + usertemp + " at " + str(score) + "\n"
    cn, cn1 = c.split(": ", 1)
    dn, dn1 = d.split(": ", 1)
    en, en1 = e.split(": ", 1)
    fn, fn1 = f.split(": ", 1)
    c = "2: " + cn1
    d = "3: " + dn1
    e = "4: " + en1
    f = "5: " + fn1

def display():
    global b, c, d, e, f
    with open("text.txt", "r+") as file:
        file.write("Top scores\n")
        file.write(b)
        file.write(c)
        file.write(d)
        file.write(e)
        file.write(f)
    file.close()
    
    file = open("text.txt", "r+")
    a = file.readline()
    b = file.readline()
    c = file.readline()
    d = file.readline()
    e = file.readline()
    f = file.readline()
    print(a, b, c, d, e, f)
    file.close()
        
file = open("text.txt", "r")
a = file.readline()
b = file.readline()
c = file.readline()
d = file.readline()
e = file.readline()
f = file.readline()
b1, b2 = b.split("at ", 1)
c1, c2 = c.split("at ", 1)
d1, d2 = d.split("at ", 1)
e1, e2 = e.split("at ", 1)
f1, f2 = f.split("at ", 1)
file.close()
