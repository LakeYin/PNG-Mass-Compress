import os
import cv2
import argparse

def compress(directory, level, subs=0, files=0):
    if not os.path.isdir(directory):
        print("Error: " + directory + " is not a valid directory.")
        return -1,-1

    for file in os.listdir(directory): # check through everything in the directory
        newpath = os.path.join(directory, file)

        if(os.path.isdir(newpath)): # recurse through subdirectories
            print("Recursing to subdirectory " + file)
            subs += 1
            record = compress(newpath, level) # keep track of the number of subdirectories and pngs
            subs += record[0]
            files += record[1]

        elif(file.lower().endswith(".png")): # compress pngs
            try:
                cv2.imwrite(newpath, cv2.imread(newpath, cv2.IMREAD_UNCHANGED), [cv2.IMWRITE_PNG_COMPRESSION, level])
                print("Compressed " + file)
                files += 1
            except:
                print("Error: could not compress " + file)

    return (subs,files)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="the path to a directory containing images")
    parser.add_argument("-l", "--level", type=int, default=9, help="the level of compression desired from 1 to 9 (default of 9)")
    args = parser.parse_args()

    if(args.level < 1 or args.level > 9):
        print("Error: invalid compression level")
        return

    print("Starting compression...")
    
    total = compress(args.path, args.level)

    if(total != (-1,-1)):
        print("\nFinished compression.")
        print("Navigated through " + str(total[0]) + " subdirectories")
        print("Compressed " + str(total[1]) + " PNGs")

if __name__ == "__main__":
    main()