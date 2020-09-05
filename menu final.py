#program to perform text file operations

import os


#for display at end
def end():
    print("\npress enter to continue:")
    input()
    print()


#to check if file exists for reading or appending etc.
def file_check(name, loc=os.getcwd):
    return os.path.exists(os.path.join(str(loc), name + ".txt"))
    


#to take input of records and lines
def record_inp(norecord, write_list):
    line = 0
    while line == 0:
        i=0
        lis = [input("Enter the record:") for i in range(norecord)]
        inp = ",".join(lis) + "\n"
        write_list.append(inp)
        line = int(input("enter 1 to stopwriting\n0 to add one more line\n:"))
    return write_list


#to write into file
def write(name, writing_list, loc=os.getcwd()):
    with open(os.path.join(str(loc), name + ".txt"), "w") as f:
        f.writelines(writing_list)
        print("writting to file is done")


#to read from file, print line and return list of lines
def read(name, loc=os.getcwd()):
    with open(os.path.join(str(loc), name + ".txt"), "r") as f:
        original_list = f.readlines()
        y = 0
        for x in original_list:
            if y != 0:
                print("LINE", y - 1, ". ", x)
            y += 1
        return original_list


#to update an element in list and write it
def update(name, inputs, index, original_list, loc=os.getcwd()):
    inputs = inputs + "\n"
    original_list[index] = inputs
    with open(os.path.join(str(loc), name + ".txt"), "w") as f:
        f.writelines(original_list)
    print()
    print(inputs)
    print("has been updated to the text file\n")


#to append a list to a text file
def append(name, input_list, loc=os.getcwd()):
    with open(os.path.join(str(loc), name + ".txt"), "a") as f:
        f.writelines(input_list)
        print("appending to the file is done")


#to delete a line and write
def delete(name, index, original_list, loc=os.getcwd()):
    del original_list[index]
    with open(os.path.join(str(loc), name + ".txt"), "w") as f:
        f.writelines(original_list)
    print()
    print("respective line has been deleted\n")


#main program
def main():
    while True:
        print("Enter the corresponding number to access that function",
              "to make a new file enter into write mode and write a file,\na new file will be created\n",
              "1. Write into file",
              "2. Read  file",
              "3. Append file",
              "4. Update file",
              "5. delete something in file",
              "6. Quit", sep='\n')
        work = int(input("Enter number :"))
        if work not in range(1, 7):#for invalid input
            print("Invalid Option")

        else:

            if work == 6:#if quit
                break
            file_name = input("Enter the file name (text file):") + ".txt"
            print("the current working directory is:")
            print(os.getcwd())
            #to get the location of file and change the cwd to the location
            location = input("Enter location of file,leave blank for current working directory:")
            if (location != ""):
                locat = location.replace("\\", "/")
                os.chdir(locat)
            location = os.getcwd()
            print(os.getcwd())


            if work == 1:#if write mode
                records = int(input("enter number of fields to write into the file:"))
                write_list = [str(records) + "\n"]
                record_inp(records, write_list)
                write(file_name, write_list, location)
                end()


            elif work == 2:#if read mode
                if not file_check(file_name, location):
                    print("THE FILE DOES NOT EXIST")
                    break
                print("\nthe matter in the file is:")
                matter = read(file_name, location)
                end()


            elif work == 3:#if append mode
                if not file_check(file_name, location):
                    print("THE FILE DOES NOT EXIST")
                    break
                print("\nthe matter in the file is:")
                list = read(file_name)
                append_list=[]
                records = int(list[0])
                record_inp(records, append_list)
                append(file_name, append_list, location)
                end()


            elif work == 4:#if update mode
                if not file_check(file_name, location):
                    print("THE FILE DOES NOT EXIST")
                    break
                updat = 1
                while (updat == 1):
                    list = read(file_name, location)
                    ind = int(input("enter the no of line you want to update:")) + 1
                    records = int(list[0])
                    lis = [input("Enter record:") for i in range(records)]
                    inp = ",".join(lis)
                    update(file_name, inp, ind, list, location)
                    end()
                    updat = int(input("enter 1 to keep on updating in this file\nenter 2 to stop updating\n:"))
                    print()


            elif work == 5:#if delete mode
                if not file_check(file_name, location):
                    print("THE FILE DOES NOT EXIST")
                    break
                dele=1
                while(dele == 1):
                    original_list=read(file_name, location)
                    ind=int(input("enter the line which you want to delete:"))+1
                    delete(file_name, ind, original_list)
                    end()
                    dele=int(input("ënter 1 to delete one more file\nand 0 to end deleting process\n:"))    
                    print()


#running main
if __name__ == "__main__":
    main()

input("\npress enter to exit:")
