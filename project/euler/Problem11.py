# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
#
# 08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
# 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
# 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
# 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
# 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
# 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
# 32 98 81 28 64 23 67 10 *26 38 40 67 59 54 70 66 18 38 64 70
# 67 26 20 68 02 62 12 20 95 *63 94 39 63 08 40 91 66 49 94 21
# 24 55 58 05 66 73 99 26 97 17 *78 78 96 83 14 88 34 89 63 72
# 21 36 23 09 75 00 76 44 20 45 35 *14 00 61 33 97 34 31 33 95
# 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
# 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
# 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
# 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
# 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
# 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
# 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
# 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
# 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
# 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
#
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
#
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
import timeit
grid = []

def main():
    print("Loading Grid")
    loadGrid();
    print("Timing new BruteForce Method:")
    print(timeit.repeat("bruteForce()", "from __main__ import bruteForce", number =1))

    print("Timing memoize Method:")
    print(timeit.repeat("memoized()", "from __main__ import memoized", number = 1))


def bruteForce():
    mults = 0;
    max =0;
    #print("Check Horizontals")
    for i in range(0, 20):
        for j in range (0, 17):
            #print("Trying: " +grid[i][j] + " "+ grid[i][j+1] + " " + grid[i][j+2] +" " + grid[i][j+3])
            value = int(grid[i][j]) * int(grid[i][j+1]) * int(grid[i][j+2]) * int(grid[i][j+3])
            mults += 3
            if value > max:
                max = value

    #print("Check Verticles")
    for i in range(0, 17):
        for j in range (0, 20):
            #print("Trying: " +grid[i][j] + " "+ grid[i+1][j] + " " + grid[i+2][j] +" " + grid[i+3][j])
            value = int(grid[i][j]) * int(grid[i+1][j]) * int(grid[i+2][j]) * int(grid[i+3][j])
            mults += 3
            if value > max:
                max = value

    #print("Check Diagonal Up")
    for i in range(3, 17):
        for j in range(0, 17):
            #print("Trying: " +grid[i][j] + " "+ grid[i-1][j+1] + " " + grid[i-2][j+2] +" " + grid[i-3][j+3])
            value = int(grid[i][j]) * int(grid[i-1][j+1]) * int(grid[i-2][j+2]) * int(grid[i-3][j+3])
            mults += 3
            if value > max:
                max = value

    #print("Check Diagonal Down")
    for i in range(0, 17):
        for j in range(0, 17):
            #print("Trying: " +grid[i][j] + " "+ grid[i+1][j+1] + " " + grid[i+2][j+2] +" " + grid[i+3][j+3])
            value = int(grid[i][j]) * int(grid[i+1][j+1]) * int(grid[i+2][j+2]) * int(grid[i+3][j+3])
            mults += 3
            if value > max:
                max = value

    print("Max Product:" + str(max))
    print("Took this many multiplication operations:" + str(mults))
    print("")

#Note:  Treating this as i = y, j = x....
def memoized():
    #Initalize m table
    m =[[0]*20 for i in range(20)]

    maxVal =0
    numOpts=0

    for i in range (0,20):
        for j in range(0,20):
            mEntry  ={}
            currLoc = int(grid[i][j])
            
            # if currLoc < 0:
            #     mEntry['zv'] += 1
            #     mEntry['zh'] += 1
            #     mEntry['zdb'] += 1
            #     mEntry['zdf'] += 1

            #vertical case
            if i == 0:
                mEntry['v'] = currLoc
            elif i >= 3: #Vertical Exists
                win_front = int(grid[i-3][j])
                #mEntry['zv'] += m[i-1][j]['zv']
                val = currLoc * m[i-1][j]['v']
                if val > maxVal: # and mEntry['zv'] == 0:
                    maxVal = val
                mEntry['v'] = val / win_front
                # if win_front < 0:
                #     mEntry['zv'] -= 1
                numOpts += 2
            else:
                #mEntry['zv'] += m[i - 1][j]['zv']
                mEntry['v'] = m[i-1][j]['v'] * currLoc
                numOpts +=1

            #horizontal case
            if j == 0:
                mEntry['h'] = currLoc
            elif j >= 3: #Horizontal Exists
                win_front =  int(grid[i][j-3])
               # mEntry['zh'] += m[i][j-1]['zh']
                val = currLoc * m[i][j-1]['h'];
                if val > maxVal: #and mEntry['zh'] == 0:
                    maxVal = val
                mEntry['h'] = val / win_front
                # if win_front < 0:
                #     mEntry['zh'] -= 1
                numOpts += 2
            else:
                #mEntry['zh'] += m[i][j - 1]['zh']
                mEntry['h'] = m[i][j-1]['h'] * currLoc
                numOpts +=1

            #Diagonal back
            if j ==0 or i == 0:
                mEntry['db'] = currLoc
            elif j >= 3 and i >=3:
                win_front = int(grid[i-3][j - 3])
                #mEntry['zdb'] += m[i-1][j - 1]['zdb']
                val = currLoc * m[i-1][j -1]['db'];
                if val > maxVal: # and mEntry['zdb'] == 0:
                    maxVal = val
                mEntry['db'] = val / win_front
                # if win_front < 0:
                #     mEntry['zdb'] -= 1
                numOpts += 2
            else:
                # mEntry['zdb'] += m[i - 1][j - 1]['zdb']
                mEntry['db'] = m[i-1][j - 1]['db'] * currLoc
                numOpts += 1

            #Diagonal forwards
            if j == 19 or i ==0:
                mEntry['df'] = currLoc;
            elif j < 17 and i >= 3:
                win_front = int(grid[i - 3][j + 3])
                # mEntry['zdf'] += m[i - 1][j + 1]['zdf']
                val = currLoc * m[i - 1][j + 1]['df'];
                if val > maxVal: # and mEntry['zdf'] == 0:
                    maxVal = val
                mEntry['df'] = val / win_front
                # if win_front < 0:
                #     mEntry['zdf'] -= 1
                numOpts += 2
            else:
                # mEntry['zdf'] += m[i - 1][j + 1]['zdf']
                mEntry['df'] = m[i - 1][j + 1]['df'] * currLoc
                numOpts += 1

            m[i][j] = mEntry


    print("Max Product:" + str(maxVal))
    print("Took this many  operations:" + str(numOpts))
    print("")


def loadGrid():
    f = open ('Problem11Grid.txt', 'r')
    for line in f:
        # Replace all 00 with -1.  It allows for division for memoization solution, and because we are looking for a maximum it shouldn't effect the result
        line = line.replace("00", "01") # Replace with 1 (which wont contribute with an increase) assumes at least one section without a 00 and it should still be correct.
        split_line = line.split();
        grid.append(split_line);


if __name__ == "__main__":
    main()