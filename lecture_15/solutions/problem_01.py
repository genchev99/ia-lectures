def cat_single_file(file_path: str):
    with open(file_path, "r") as fd:
        data = fd.read()
        print(data)


def cat(file_paths: list):
    for file_path in file_paths:
        cat_single_file(file_path)


if __name__ == '__main__':
    # file_path = input("Input file path: ")
    # cat_single_file(file_path)
    # Hint
    file_paths = []
    while True:
        file_path = input("Enter a file path: ")
        if not file_path:
            break
        # do something with file
        file_paths.append(file_path)

    cat(file_paths)
