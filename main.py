import sys
from MyContainer import Container


def err_message1():
    print("incorrect command line!\n"
          "  Waited:\n"
          "     command -f infile outfile01 outfile02\n"
          "  Or:\n"
          "     command -n number outfile01 outfile02\n")


def err_message2():
    print("incorrect qualifier value!\n"
          "  Waited:\n"
          "     command -f infile outfile01 outfile02\n"
          "  Or:\n"
          "     command -n number outfile01 outfile02\n")


if __name__ == '__main__':
    if len(sys.argv) != 5:
        err_message1()
        exit(1)
    print("Start")
    c = Container()
    if sys.argv[1] == '-f':
        file_input = open(sys.argv[2], 'r')
        c.file_in(file_input)
    elif sys.argv[1] == '-n':
        size = int(sys.argv[2])
        if size < 1 or size > 10000:
            print("incorrect number of figures = {}. Set 0 < number <= 10000".format(size))
            exit(3)
        c.rnd_in(size)
    else:
        err_message2()
        exit(2)
    file_out1 = open(sys.argv[3], 'w')
    file_out1.write("Filled Container:\n")
    c.out(file_out1)
    file_out2 = open(sys.argv[4], 'w')
    file_out2.write(c.shell_sort())
    c.out(file_out2)
    print("Stop")
    exit()
