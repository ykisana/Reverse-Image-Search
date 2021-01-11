from index import write_index
import colourdescriptor
import os
import shutil
import glob


def main():
    # loop state program, performs actions based on user inputs

    # first create index.csv if it doesn't exist
    do_index()

    # variable to end while loop
    end = False

    # loop for program
    while not end:
        # prompt for user
        print("What would you like to do?")
        print("[1] Add image")
        print("[2] Search Image")
        print("[3] End program")
        print("Type a number from above and press enter.")

        # store user input
        input_number = input()

        # check input and run appropriate functions
        if input_number == '1':
            do_add()

        # runs do_search to perform a search
        elif input_number == '2':
            do_search()

        # terminates the program
        elif input_number == '3':
            print("Program Terminated")
            end = True

        # states invalid input and continues loop
        else:
            print("Not a valid Input.\n")


# function for search
def do_search():
    # done through shell commands (using os)

    # prompt user for path of images to be search
    print("Please enter the path of the image you are trying to look up")
    img_path = input()

    # check if the path is valid
    is_file = os.path.isfile(img_path)
    if not is_file:
        print("Path not valid.\n")
        return

    # image search done using search.py
    search_cmd = "python search.py --index index.csv --query " \
                 + img_path + " --result-path images"
    os.system(search_cmd)


def do_add():
    # done through shell commands (using os)
    # files copied using shutil

    # use colourdescriptor for features of new images
    cd = colourdescriptor.ColourDescriptor((8, 12, 3))

    output = open("index.csv", "w")

    # prompt user for single or bulk images
    print("How many images would you like to add?")
    print("[1] Single")
    print("[2] Bulk")
    input_number = input()

    # if single it adds and indexes a single images
    if input_number == "1":
        print("Please enter the path of the image you want to add")
        img_path = input()

        # check if path is valid
        is_image = os.path.isfile(img_path)
        if not is_image:
            print("Path not valid.\n")
            return

        write_index(img_path, cd, output)
        shutil.copy(img_path, "images")

    elif input_number == "2":
        print("Please enter the path of the folder containing the images to add")
        folder_path = input()

        # check if path is a valid directory
        is_folder = os.path.isdir(folder_path)
        if not is_folder:
            print("Path not valid.\n")
            return

        for path in glob.glob(folder_path + "/*.jpg"):
            write_index(path, cd, output)
            shutil.copy(path, "images")

    else:
        print("Not a valid Input.\n")

    output.close()


def do_index():
    # create index.csv using index.py if it doesn't already exist
    # done through shell commands (using os)
    is_index = os.path.isfile("index.csv")
    if not is_index:
        print("indexing...")
        index_cmd = "python index.py --dataset images --index index.csv"
        os.system(index_cmd)


main()
