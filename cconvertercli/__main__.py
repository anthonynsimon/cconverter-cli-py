import cmd
import os

if __name__ == '__main__':
    args = cmd.parse_args()

    if "CCONVERTER_DEBUG" in os.environ:
        print(args)

    print(cmd.apply(args))
