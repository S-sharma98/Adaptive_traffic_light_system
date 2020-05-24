import time
import sys

while True:
	n1=int(input('enter the value of n1='))
	if n1 == 0:
		t1=0;
		print(t1)
	elif n1<10:
		t1=30;
		print(t1)
	elif 10==n1 or n1<20 or n1==20:
		t1=60;
		print(t1)
	elif 20<n1:
		t1=90;
		print(t1)

	for remaining in range(t1, 0, -1):
	    sys.stdout.write("\r")
	    sys.stdout.write("{:2d} seconds remaining.".format(remaining))
	    sys.stdout.flush()
	    time.sleep(1)

	sys.stdout.write("\rComplete!            \n")
	



	n2=int(input('enter the value of n2='))
	if n2 == 0:
		t2=0;
		print(t2)
	elif n2<10:	
		t2=30;
		print(t2)
	elif 10==n2 or n2<20 or n2==20:
		t2=60;
		print(t2)
	elif 20<n2:
		t2=90;
		print(t2)

	for remaining in range(t2, 0, -1):
	    sys.stdout.write("\r")
	    sys.stdout.write("{:2d} seconds remaining.".format(remaining))
	    sys.stdout.flush()
	    time.sleep(1)

	sys.stdout.write("\rComplete!            \n")
	

	n3=int(input('enter the value of n3='))
	if n3 == 0:
		t3=0;
		print(t3)
	elif n3<10:
		t3=30;
		print(t3)
	elif 10==n3 or n3<20 or n3==20:
		t3=60;
		print(t3)
	elif 20<n3:
		t3=90;
		print(t3)

	for remaining in range(t3, 0, -1):
	    sys.stdout.write("\r")
	    sys.stdout.write("{:2d} seconds remaining.".format(remaining))
	    sys.stdout.flush()
	    time.sleep(1)

	sys.stdout.write("\rComplete!            \n")
	

	n4=int(input('enter the value of n4='))
	if n4 == 0:
		t4=0;
		print(t4)
	elif n4<10:
		t4=30;
		print(t4)
	elif 10==n4 or n4<20 or n4==20:
		t4=60;
		print(t4)
	elif 20<n4:
		t4=90;
		print(t4)

	for remaining in range(t4, 0, -1):
	    sys.stdout.write("\r")
	    sys.stdout.write("{:2d} seconds remaining.".format(remaining))
	    sys.stdout.flush()
	    time.sleep(1)

	sys.stdout.write("\rComplete!            \n")
	
