import sys
import os
from PIL import Image, ImageOps
def main():
    check_command()
    try:
        imgfile = Image.open(sys.argv[1])
        shirtfile = Image.open("shirt.png")
        size = shirtfile.size
        # to do the size of the imgfile into the same size of the shirtfile
        new = ImageOps.fit(imgfile, size)
        # to paste the shirt file in our new photo
        new.paste(shirtfile,shirtfile)

        new.save(sys.argv[2])
    except FileNotFoundError:
        print("Input does not exist")
        sys.exit(1)

def check_command():
    if len(sys.argv) < 3 :
        print("Too few arguments")
        sys.exit(1)
    if len(sys.argv) > 3 :
        print("Too many arguments")
        sys.exit(1)
    file1 = os.path.splitext(sys.argv[1])
    file2 = os.path.splitext(sys.argv[2])
    if file1[1] not in [".jpeg", ".jpg",".png"]:
        print("Invalid input")
        sys.exit(1)
    if file2[1] not in [".jpeg", ".jpg",".png"]:
        print("Invalid output")
        sys.exit(1)

    if file1[1].lower() != file2[1].lower():
        print("Input and output have different extensions")
        sys.exit(1)



if __name__ == "__main__":
    main()