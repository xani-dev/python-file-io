import re


def read_words():

    print('Opening Our text: origin.txt')

    with open('origin.txt', 'r') as in_stream:
        print('Opening origin_out.txt')

        # CHALLENGE COMPLETED!! Search only after HEADER and before FOOTER:
        regex = r"([*])\1\1"
        star_counter = 0

        with open('origin_out.txt', 'w') as out_stream:
            for index, line_number in enumerate(in_stream):
                matches = re.search(regex, line_number)
                if matches:
                    star_counter += 1
                if star_counter >= 1 and star_counter < 2:
                    if re.search(r"herit|HERIT", line_number):
                        for word in re.split(r'\s|--', line_number):
                            if re.search(r"herit|HERIT", word):
                                pure_word = re.sub(r'[^a-zA-Z]', '', word)
                                out_stream.write(f"{index+1}  \t{pure_word}\n")

    print("Homework is Finished!")
    print('origin.txt is closed?', in_stream.closed)
    print('origin_out.txt is closed?', out_stream.closed)


read_words()


# Original
# with open('origin_out.txt', 'w') as out_stream:
#     for index, line_number in enumerate(in_stream):
#         if re.search(r"herit|HERIT", line_number):
#             for word in re.split(r'\s|--',line_number):
#                 if re.search(r"herit|HERIT", word):
#                     pure_word = re.sub(r'[^a-zA-Z]', '', word)
#                     out_stream.write(f"{index+1}  \t{pure_word}\n"
