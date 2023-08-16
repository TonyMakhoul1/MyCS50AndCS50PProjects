import sys
def main():
    
        check_cmd()



def check_cmd():
    if len(sys.argv) < 3:
        print("Too few arguments")
        sys.exit(1)
    if len(sys.argv) > 3:
        print("Too many arguments")
        sys.exit(1)
    if ".csv" not in (sys.argv[1] or sys.argv[2]):
        print("Not csv file")
        sys.exit(1)


#def function_2():



#def function_n():


if __name__ == "__main__":
    main()