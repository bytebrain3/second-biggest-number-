array = [873, 891, 78, 353, 504, 315, 452, 493, 887, 596, 742, 780, 653, 767, 299, 440, 453, 47, 757, 876, 605, 821, 927, 476, 544, 275, 813, 358, 481, 776, 49, 214, 518, 622, 982, 510, 499, 446, 85, 947, 910, 818, 75, 784, 14, 773, 525, 628, 643, 341, 53, 236, 233, 45, 685, 306, 899, 204, 661, 941, 752, 623, 21, 433, 256, 666, 194, 130, 496, 973, 521, 90, 103, 856, 15, 437, 487, 65, 647, 787, 603, 459, 470, 974, 307, 35, 997, 761, 851, 843, 989, 153, 109, 263, 415, 918, 826, 195, 486, 207]

def main(list):
	max_number = array[0]
	biggest = []
	for i in range(len(array)):
		if array[i] > max_number:
			max_number = array[i]
			biggest.append(max_number)
	print("second biggest number is : ",biggest[len(biggest)-2])
main(array)
# output second biggest number is 982
