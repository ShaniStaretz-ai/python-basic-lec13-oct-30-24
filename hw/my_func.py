def print_starts():
    """ print 13 *"""
    print('*************')


def get_answer_char_by_index(index):
    match index:
        case 0:
            return 'a'
        case 1:
            return 'b'
        case 2:
            return 'c'
        case _:
            return 'd'

def get_answer_index_by_char (char):
    match char:
        case 'a':
            return 0
        case 'b':
            return 1
        case 'c':
            return 2
        case _:
            return 3


if __name__ == "__main__":
    print("whats your name:", __name__)
