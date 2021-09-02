import subprocess
import sys
x=input("x?")
y=input("y?")
directory=input("directory?")
div=input("diviso quanto?")
output=input("output directory?")

x=str((int(x))/(int(div)))

y=str((int(y))/(int(div)))
x_off="0"
y_off="0"

bash=open('bash.sh','w')
print("#!/bin/bash",file=bash)
for i in range(0,int(div)):
    y_off=str(float(y)*i)
    for j in range(0,int(div)):
        x_off=str(float(x)*j)
        output_loop=output+str(i)+str(j)+".jpg"
        print("convert -extract {}x{}+{}+{} {} {}".format(x,y,x_off,y_off,directory,output_loop),file=bash)
bash.close()
subprocess.run("/home/daniele/Documents/Programming/TimBuchalka/Python/image_cropper/bash.sh")