import lec13
from lec13 import print_hello

# stuff only to run when not called via 'import' here

print("help on file 'lec13':")
help(lec13)
print("help on function 'print_hello':")
help(print_hello)

print("rest:")
for _ in range(3):
    print_hello()
print("whats your name[main]:",__name__)
help(__name__)
