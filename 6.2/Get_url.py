from idea_test import Idea_test


def get_url(path_to_input_file, path_to_output_file):
    with open(path_to_input_file, 'r') as content_file:
        content = content_file.read().split(" ")

    length = len(content)
    for i in range(length):
        content.extend(content.pop(0).split('\n'))

    print(content)

    fout = open(path_to_output_file, "w")

    for it in content:
        it = it.strip("\n")
        if it[0:8] == "https://" or it[0:4] == "www.":
            fout.write(it + "\n")

Idea_test().test_simple_file()
get_url("test_input.txt", "test_output.txt")
