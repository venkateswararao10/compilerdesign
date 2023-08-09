import argparse
a=argparse.ArgumentParser()
a.add_argument('sourcefilename')
a.add_argument('-c',nargs=1)
args=a.parse_args()
f1=open(args.sourcefilename,'r')
x=f1.read()
f2=open(args.c[0],'w')
f2.write(x)
f1.close()
f2.close()

python3 copycontent.py level1.tinyc -c copy1.txt
