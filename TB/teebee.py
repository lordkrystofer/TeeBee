import time
import sys, getopt
import datetime




def main(argv):


	# Parse the options and arguments
	try:
		opts, args = getopt.getopt(argv,"hc:",["period=","currency=","points="])
	except getopt.GetoptError:
		print('teebee.py error parsing arguments')
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print('help message here')
			sys.exit()
		elif opt in ("-c", "--currency"):
			print(arg)






if __name__ == "__main__":
	main(sys.argv[1:])
