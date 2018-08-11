import argparse

##Basic operation
parser = argparse.ArgumentParser()
parser.add_argument("square", help = "display the square of a given integer", type = int)

##Different ways to include command line arguments
# parser.add_argument("-v", "--verbose", help = "perform operations verbosely", action = "store_true")
# parser.add_argument("-v", "--verbose", help = "perform operations verbosely", type = int, choices = [0,1,2], default = 0)

##Verbose or quiet output
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", help = "print the result verbosely", action="store_true")
group.add_argument("-q", "--quiet", help = "supress output", action="store_true", default = True)

args = parser.parse_args()

# if args.verbose:
#     print("{} x {} = {}".format(args.square, args.square, args.square**2))
# else:
#     print(args.square**2)

# if args.verbose == 2:
#     print("Running '{}'".format(__file__))
#     print("The square of {} is {}".format(args.square, args.square**2))
# elif args.verbose == 1:
#     print("{}^2 = {}".format(args.square, args.square**2))
# else:
#     print(args.square**2)

if args.verbose:
    print("Running '{}'".format(__file__))
    print("The square of {} is {}".format(args.square, args.square**2))
elif args.quiet:
    print(args.square**2)
else:
    print("\n")
