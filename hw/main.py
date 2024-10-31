from my_func import print_starts
import  my_func
for _ in range(5):
    my_func.print_starts()
print("call function only:")
for _ in range(5):
    print_starts()
help(print_starts)