import os


def main():
    # variable to end while loop
    end = False

    # loop for program and user input
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
            pass

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

    # create index.csv using index.py if it doesn't already exist
    is_index = os.path.isfile("index.csv")
    if not is_index:
        index_cmd = "python index.py --dataset images --index index.csv"
        os.system(index_cmd)

    # prompt user for path of images to be search
    print("Please enter the path of the image you are trying to look up")
    img_path = input()

    # check if the path is valid
    is_file = os.path.isfile(img_path)
    if not is_file:
        print("Path not valid.")
        return

    # image search done using search.py
    search_cmd = "python search.py --index index.csv --query "\
                 + img_path + " --result-path images"
    os.system(search_cmd)


def do_add():



main()
