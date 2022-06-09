import re


def main():
    file_name = "access_log"
    new_file_name = "final_log"
    file = open(file_name, "r")
    new_file = open(new_file_name, "w")
    status_code = ' 304 '
    # for line in file.readlines():
    #     if re.search(status_code, line):
    #         new_file.write(line)
    # new_file.close()
    new_file.write(line for line in file.readlines() if re.search(status_code, line))


if __name__ == '__main__':
    main()
