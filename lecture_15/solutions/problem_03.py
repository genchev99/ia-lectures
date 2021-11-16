def grep_single_file(keyword: str, file_path: str):
    with open(file_path, "r") as fd:
        line_counter = 1
        for line in fd.readlines():
            if keyword in line:
                print(f"{file_path}:{line_counter}:{line}")

            line_counter += 1


def grep(keyword: str, file_paths: list):
    for file_path in file_paths:
        grep_single_file(keyword, file_path)


if __name__ == '__main__':
    file_paths = []

    keyword = input("Enter keyword: ")
    while True:
        file_path = input("Enter file path: ")

        if not file_path:
            break

        file_paths.append(file_path)

    grep(keyword, file_paths)
