import math

data = []

def main(): 
    with open ("input2019.txt", "r") as input:
        global data
        data = input.readlines()
        transformArrayToNumbers()
        total_mass = 0
        for n in data:
            total_mass = total_mass + getMass(n, 0)
        print("Total Mass: " + str(total_mass))

def getMass(n, total_result):
    result = math.trunc(n / 3) - 2
    if result > 0:
        return getMass(result, total_result + result)
    else:
        print("n: " + str(n) + ", result: " + str(result))
        return total_result

def transformArrayToNumbers():
    global data
    i = 0
    for n in data:
        data[i] = int(n.replace('\n', ''))
        i+=1

if __name__ == "__main__":
    main()