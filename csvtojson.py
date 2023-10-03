import csv
from os.path import exists
import sys

def main():

    print("-" * 25)
    print("RULES".center(25))
    print("-" * 25)
    print("  1. File must be CSV format, delimited by commas")
    print("  2. Remove ALL commas from cells")
    print("  3. Remove thousands-separator from numbers (e.g. 42,000 -> 42000)")
    print("  4. Make sure category columns have text in every cell")
    print("-" * 25)
    
    fileName = ""
    # Use filename given in CLI, otherwise ask user
    if ((len(sys.argv) > 1) and sys.argv[1]):
        fileName = sys.argv[1]
    else:
        fileName = input("What is the filename of the CSV you're converting? ")

    # Continue asking until valid file
    while (not exists(fileName)):
        fileName = input("Invalid file name. Please try again: ")

    with open(fileName, newline='') as csvfile:

        # Open csv and json
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        readerList = list(reader)
        writer = open(fileName.split(".")[0] + ".json", "w")

        # Get column names and # of columns
        headers = readerList[0]
        nCol = len(readerList[0]) - 1

        # Use nLevels from CLI, otherwise ask user
        nLevels = 0
        if (len(sys.argv) > 2 and sys.argv[2]):
            nLevels = int(sys.argv[2])
        else:
            nLevels = int(input("Is there 1 or 2 category columns? "))

        # Continue asking until valid nLevel
        while (nLevels < 1 or nLevels > 2):
            input("This program only supports 1 or 2 category columns. Please try again: ")

        writer.write("{\n")
        tab = "  "
        category = []
        for i in range(1, len(readerList)):
            for j in range(len(readerList[i])):
                # If category column and not already printed
                if (j < nLevels and readerList[i][j] not in category):
                    writer.write(tab + "\"" + readerList[i][j] + "\": {\n")
                    # Increment tabber and add category to list
                    tab += "  "
                    if (nLevels > 1):
                        category += [readerList[i][j]]
                elif (readerList[i][j] not in category):
                    # If last column
                    if (j == nCol):
                        writer.write(tab + "\"" + headers[j] + "\": " + "\"" + readerList[i][j] + "\"\n")
                        tab = tab[:-2]
                        # If last row in sheet
                        if (i + 1 >= len(readerList)):
                            writer.write(tab + "}\n")
                            while (tab != ""):
                                tab = tab[:-2]
                                writer.write(tab + "}\n")
                        else:
                            # If next row category not the same category, don't add comma
                            if (i + 1 < len(readerList) and (readerList[i + 1][0] not in category) and (nLevels > 1)):
                                writer.write(tab + "}\n")
                                tab = tab[:-2]
                                category = []
                            writer.write(tab + "},\n")
                    else:
                        writer.write(tab + "\"" + headers[j] + "\": " + "\"" + readerList[i][j] + "\",\n")

if __name__ == "__main__":
    main()
