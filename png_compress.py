import os
import cv2
import argparse

def compress(directory, level):
    if not os.path.isdir(directory):
        print("Error: " + directory + " is not a valid directory.")
        return 1

    for file in os.listdir(directory): # check for subdirectories and recurse
        newpath = os.path.join(directory, file)

        if(os.path.isdir(newpath)):
            print("Recursing to subdirectory " + file)
            compress(newpath, level)

    for file in os.listdir(directory): # now check for PNGs and run compression
        path = os.path.join(directory, file)

        if(file.lower().endswith(".png") and os.path.isfile(path)):
            try:
                cv2.imwrite(path, cv2.imread(path, cv2.IMREAD_UNCHANGED), [cv2.IMWRITE_PNG_COMPRESSION, level])
                print("Compressed " + file)
            except:
                print("Error: could not compress " + file)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="the top directory containing images")
    parser.add_argument("-l", "--level", type=int, default=9, help="the level of compression desired from 1 to 9 (default)")
    args = parser.parse_args()

    compress(args.directory, args.level)

if __name__ == "__main__":
    main()