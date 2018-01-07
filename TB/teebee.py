import time
import sys, getopt
import datetime



# understanding this fucking command line garbage
# There are three types of arguments
# 1 - a dashed single letter option  such as -c -q or -h  with NO argument
# 2 - a dashed single letter option  such as -c -q or -h  WITH an argument    eg.   -c 1000  or -q dog
# 3 - a double dashed option word like --period=1000  or --pettype=dog

# the way you tell getopt the "allowable single letter options is in the second parameter of getopt.
# the option letters go in a sequence  abcd one right after the other
# eg... opts, args = getopt.getopt(argv, "abcd", [])
# call with prog -a -b -c -d

# the way you handle single letter options with arguments is to put a colon after the letter
# for example to support an option called 'c' with an argument would look like this
# eg... opts, args = getopt.getopt(argv, "abc:d", [])
# call with prog -a -b -c 1000 -d

# the way you handle double dash options is like this
# opts, args = getopt.getopt(argv, "hc:", ["period=", "currency=", "points="])
# call like this  prog -a -c 1000 --period=100 --currency=USD --points=30000


def main(argv):
    # Parse the options and arguments

    period = 1;
    startTime = False
    endTime = False

    try:
        opts, args = getopt.getopt(argv, "hc:p:", ["period=", "currency=", "points="])
    except getopt.GetoptError:
        print('teebee.py error parsing arguments')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('help message here')
            sys.exit()

        elif opt in ("-p", "--period"):
            #if (int(arg) in [300,900,1800,7200,14400,86400]):
            period = arg
            #else:
            # #	print 'Poloniex requires periods in 300,900,1800,7200,14400, or 86400 second increments'
			#	sys.exit(2)
        elif opt in ("-c", "--currency"):
            print(arg)


    while True:
        print("{} Ok I'm doing Stuff".format(datetime.datetime.now()))

        if (not startTime):
            time.sleep(int(period))

if __name__ == "__main__":
    main(sys.argv[1:])
