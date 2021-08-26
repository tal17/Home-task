import struct


def concat_lists(a, b, number_of_times):
    """
    Takes 2 lists and returns a list which contains all possible concatenations between elements from the first list
    and elements from the second list.
    :param a: (str list) first list.
    :param b: (str list) second list
    :param number_of_times: (int) number of times we want to concatenate b to a
    :return: (str list) list with all concatenations based on the parameters given before.
    """

    if number_of_times <= 0:  # stop condition: returning the first list that we got as a parameter.
        return a
    concat = []
    for element_a in a:
        for element_b in b:
            if element_a + "~" + element_b not in concat:  # checking whether the string is not already in the list.
                concat.append(element_a + "~" + element_b)  # adding the string into the list - taking the item from
                # a and the item from b and seperating them by '~'
    return concat_lists(concat, b, number_of_times - 1)  # calling the recursion with the new list that contains all
    # the possible concatenations from a and b as the first parameter, and decreasing the number of calls by 1 in the
    # third parameter.


def section_generator():
    """
    Generates all possible sections according to the instructions given in the task.
    :return: (str list) list that contains all possible sections, when each number that represents a byte
    is separated by '~'.
    """

    sections = []
    byte_values = []
    for number in range(2 ** 8):  # generating a list of numbers between 1-255 in a string format.
        byte_values.append(str(number))

    for tag in range(2 ** 8):
        sections.append(str(tag) + "~" + "0")  # case where the section value is in length = 0.
        for section_length in range(1, 2 ** 8):
            concat = concat_lists(byte_values, byte_values, section_length - 1)  # generating all possible sections
            # based on the value length.
            for i in range(len(concat)):  # adding the tag before each section.
                sections.append(str(tag) + "~" + str(section_length) + "~" + concat[i])
    sections = list(set(sections))  # removing duplicates.
    return sections


def main():
    """
    Main functions that calls the section_generator, and then creates all possible section combinations based on the
    number of sections which is between 0-255. then adds the magic, translates the sections into bytes using the
    seperator '~' and creates all possible files that match the requirements.
    :return: None.
    """

    magic = struct.pack('<I', 0xfee1900d)  # storing the magic constant in little endian format.
    results = []
    results.append("0")  # case where there are 0 sections.
    sections = section_generator()  # storing in a list all possible sections.
    for section_count in range(1, 2 ** 8):
        temp = concat_lists(sections, sections, section_count - 1)  # we make a list of possible section combinations
        # based on the number of sections
        for section in temp:
            results.append(str(section_count) + "~" + section)  # before the sections, adding the number of sections.
        results = list(set(results))  # removing duplicates.
    for i in range(len(results)):
        file_format = results[i]
        bytes_to_write = file_format.split("~")  # we make a list out of the results so that each item is a byte that
        # we need to write into the file.
        with open("file_number_" + str(i), "wb") as file_to_write:  # creating the file for binary writing.
            file_to_write.write(magic)  # writing the magic before the rest of the content.
            for byte in bytes_to_write:
                file_to_write.write(bytes([int(byte)]))  # writing the rest of the content in bytes into the file.
    print(results)


if __name__ == '__main__':
    main()
