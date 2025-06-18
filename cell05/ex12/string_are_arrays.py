import sys

if len(sys.argv) != 2:
    print("none")
else:
    input_str = sys.argv[1]
    z_count = input_str.count('z')
    if z_count == 0:
        print("none")
    else:
        print("z" * z_count)
5.13
import sys

if len(sys.argv) == 1:
    print("none")
else:
    for arg in sys.argv[1:]:
        if not arg.endswith("ism"):
            print(arg + "ism")
            