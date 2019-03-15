import time;

localtime = time.asctime( time.localtime(time.time()) )

string = '''


        /* 
          
   ######## ASCG- Automatic Source Code Generator ########

'''
string8='''
   CREATED BY : Automatic source code generator

   DESCRIPTION: Any changes below may Alter the code and
		may not able to run or compile in the
		respective compiler
   	
   Thankyou For Using ASCG-Automatic Source Code Generator

'''
	
string=string+"\n"+"   CREATED ON : "+str(localtime) +"\n"+string8+"\n"+'*/'+"\n"+"\n"

string2='''
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<conio.h>
void main()
{
'''
string3=""
file=open("final.txt","r")
for i in file:
    string3=string3+str(i)


string4='''
getch();
}

'''   
finalstring=string+"\n"+string2+"\n"+string3+string4
print(finalstring)
filee=open("finaloutput.txt","w")
filee.write(finalstring)
filee.close()
file.close()
