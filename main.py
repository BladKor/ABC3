import sys

from container import Container


message1 = """
            Incorrect usage.
            Expected:
                command -f input_file output_file_1 output_file_2
            Or:
                command -n size output_file_1 output_file_2
           """


message2 = """
            Incorrect qualifier value.
            Expected:
                command -f input_file output_file_1 output_file_2
            Or:
                command -n size output_file_1 output_file_2
           """


def main(argc, argv):
    if argc != 5:
        print(message1)
        return 0

    container = Container()
    if argv[1] == "-f":
        with open(argv[2], 'r') as file:
            words = []
            for line in file:
                for word in line.split():
                    words.append(word.strip())
            words.reverse()
            container.in_from_file(words)
    elif argv[1] == "-n":
        container.in_rnd(int(argv[2]))
    else:
        print(message2)
        return 0

    with open(argv[3], "w+") as output:
        output.write("Container:\n")
        container.out(output)

    container.shaker_sort()

    with open(argv[4], "w+") as sorted_output:
        sorted_output.write("Sorted container:\n")
        container.out(sorted_output)


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
