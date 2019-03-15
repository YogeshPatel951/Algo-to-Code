filee=open("final.txt","w")
filee.close()
filee=open("variables.txt","w")
filee.close()









def isitcontrol(string):
    file=open("control.txt","r")
    for ko in file:
        kol=ko.split(" ")
        
        if(kol[0]==string):
            return 1
        else:
            continue
    file.close()    
    return 0

def getcntrlend(string):
    file=open("control.txt","r")
    for ko in file:
        kol=ko.split(" ")
        if(kol[0]==string):
            kols=kol[1]
            if(kol[1].find('\n')!=-1):
                kols=kol[1]
                sizel=len(kols)
                kols=kols[0:sizel-1]
            return kols
    file.close()
    return 0

def getcntrlsyn(string):
    file=open("controlsyn.txt","r")
    for ko in file:
        kol=ko.split(" ")
        if(kol[0]==string):
            kols=kol[1]
            if(kol[1].find('\n')!=-1):
                kols=kol[1]
                sizel=len(kols)
                kols=kols[0:sizel-1]
            return kols
    file.close()
        
        
    return 0




















def getending(string):
    rt="\n"+'}'
    return rt

def isitcondtn(string):
    #check from a file,where it checks whether it is a part of control statement or not
    
    file=open("condition.txt","r")
    for q in file:
        conlist=q.split(" ")
        if(conlist[0]==string):
            
            return 1
        else:
            
            continue
    
    file.close()
    return 0


def getloopendkey(string):
    #get the second part of line from the condtn file
    file=open("condtn.txt","r")
    for q in file:
        listof=q.split(" ")
        if(listof[0]==string):
            bb=listof[1]
            if(bb.find('\n')):
                aaa=len(bb)
                bb=bb[0:aaa-1]
            return bb
        else:
            continue   
    file.close()
    return 0

def getsynofcontrol(string):
    #return the start part of every control statetement from condition file
    file=open("condition.txt","r")
    
    for q in file:
        listo=q.split(" ")
        
        if(listo[0]==string):
            
            var=listo[1]
            
            actual=len(var)-1
            var1=var[0:actual]
            
            
            return var1
        else:
            continue
    

    file.close()
    return 0




def isitvariableforoperator(string):
    varfile=open("variables.txt","r")
    for z in varfile:
        ls=z.split(" ")
        key=ls[1]
        if(key.find(string)!=-1):
            return 1
        
    varfile.close()    
    return 0 


def isitfunc(string):
    funcfile=open("func.txt","r")
    for z in funcfile:
        size=len(z)
        if(z[0:size-1]==string):
            return 1
    funcfile.close()    
    return 0


def isitvariable(string):
    varfile=open("variables.txt","r")
    for z in varfile:
        ls=z.split(" ")
        if(ls[1]==string):
            return 1
        
    varfile.close()    
    return 0

def funcwithvar(string):
    file=open("functionswithvariable.txt","r")
    for z in file:
        ls=z.split()
        if(string==ls[0]):
            return ls[1]
        
    file.close()    
    return 0

def getdatatype(string):
    file=open("variables.txt","r")
    for z in file:
        ls=z.split()
        size=len(string)
        if(string[0:size-1]==ls[1]):
            return ls[0]
        
    file.close()        
    return 0


def getidenti(string):
    file=open("identi.txt","r")
    for z in file:
        ls=z.split()
        if(string==ls[0]):
            return ls[1]
    file.close()        
    return 0

def getvarname(string):
    return string

def getsynoffunc(string):
    file=open("functions.txt","r")
    for z in file:
        ls=z.split()
        if(string==ls[0]):
            return ls[1]
    file.close()        
    return 0

def getendof(string):
    
    
    if(string=="print" or "input"):
        rt='");'            
        return rt
    return 0

def getendofwithvar(string):
    if(string=="print" or "input"):
        rt=');'
        return rt
    return 0


def isitdatatype(string):
    file=open("datatypes.txt","r")
    for z in file:
        ls=z.split()
        print(ls[0])
        if(string==ls[0]):
            return 1
    file.close()
    return 0

def gettypeof(string):
    file=open("datatypes.txt","r")
    for z in file:
        ls=z.split()
        if(string==ls[0]):
            return ls[1]
    file.close()
    return 0

def getendtypeof(string):
    end=';'
    return end

    
    
def writetovariablefile(string):
    file=open("variables.txt","a")
    file.write(string)
    file.write("\n")
    file.close()
        

def finalfilewriter(string):
    file=open("final.txt","a")
    file.write(string)
    file.write("\n")
    file.close()

userfile=open("user.txt","r")
funcflag=0
dataflag=0
funcdone=0
syn=""
last=""
doflag=0
variableflag=0
linecom=0
condn=0
loopendkey=""
syntaxofif=""

for a in userfile:
    synelseif=""
    rstword=""
    hel=0
    endingofcontrol=""
    condn=0
    loopendkey=""
    user=""
    syntaxofif=""
    
    funcflag=0
    dataflag=0
    last=""
    funcdone=0
    syn=""
    variableflag=0
    userfunc=""
    userwords=a.split(" ")
    print("userwords",userwords)
    
    for b in userwords:
        if(funcflag==0):
            funcmutex=isitfunc(b)
            if(funcmutex==1):
                userfunc=b
                funcflag=1
            else:
                break
        else:
            variableflag=isitvariable(b)
              
            if(variableflag==1):
                synfuncwithvar=funcwithvar(userfunc)
                last=getendofwithvar(userfunc)
                datatype=getdatatype(b)
                identi=getidenti(datatype)
                varname=getvarname(b)
                synfuncwithvar=synfuncwithvar.replace('identi',identi)
                sizeeee=len(varname)
                synfuncwithvar=synfuncwithvar.replace('variable',varname[0:sizeeee-1])
                syn=synfuncwithvar
                
                linecom=1
                #this syn is ready with variable
                variableflag=0
                funcflag=0
                break
                
            elif(variableflag!=1 and funcdone==0):
                syn=getsynoffunc(userfunc)
                last=getendof(userfunc)
                syn=syn+b
                funcdone=1
            else:
                
                syn=syn+" "+b

    #syfunc is ready without variable func

    for c in userwords:
        if(dataflag==0):
            datamutex=isitdatatype(c)
            if(datamutex==1):
                dataflag=1
                userdatatype=c
                startdata=gettypeof(c)
                last=getendtypeof(c)
                syn=startdata
            else:
                break
                
        else:
            linecom=1
            syn=syn+" "+c
            size=len(syn)
            writetovariablefile(syn[0:size-1])
            
            
            
            #syn ready as datatype
            dataflag=0
            break
    for r in userwords:
        if(isitvariableforoperator(r)==1):
            syn=''.join(userwords)
            last=';'
            break
        else:
            break



    for y in userwords:
        if(y.find('\n')!=-1):
            lenth=len(y)
            
            y=y[0:lenth-1]
            
           
        condn=isitcondtn(y)
        
        if(condn==1):
            loopendkey=getloopendkey(y)
            
            if(loopendkey.find('none')==-1):
                syntaxofif=getsynofcontrol(y)
                user=userwords
                user.remove('if')
                  
                for l in user:
                    
                    if(l.find('\n')!=-1):
                        lenth=len(l)
                        l=l[0:lenth-1]
                    
                    if(l!=loopendkey):
                        
                        syntaxofif=syntaxofif+" "+l
                        
                        
                    elif(l.find(loopendkey)!=-1):
                        
                        
                        syntaxofif=syntaxofif+getsynofcontrol(loopendkey)
                        break
            else:
                if(y.find('elseif')!=-1):
                   
                   synelseif='else if('
                   userwords.pop(0)
                   rstword=''.join(userwords)
                   if(rstword.find('\n')!=-1):
                       hel=len(rstword)
                       rstword=rstword[0:hel-1]
                   syn=synelseif+rstword+'){'
                   break
                else:
           
                    syn=getsynofcontrol(y)+'\n'
                    
                
                    endingofcontrol=getending(y)
                
                
                    break
            
            syn=syntaxofif+'\n'
            break

                    





    for v in userwords:
        if(v.find('\n')!=-1):
            lenth=len(v)
            
            v=v[0:lenth-1]        
        cntrlmutex=isitcontrol(v)
        
        if(cntrlmutex==1):
            
            endkey=getcntrlend(v)
            
            if(endkey.find('none')==-1):
                syntaxofcntrl=getcntrlsyn(v)
                user=userwords
                user.pop(0)
                  
                for ll in user:
                    
                    if(ll.find('\n')!=-1):
                        lenth=len(ll)
                        ll=ll[0:lenth-1]
                    
                    if(ll!=endkey and doflag!=1):
                        
                        syntaxofcntrl=syntaxofcntrl+" "+ll
                        
                    elif(ll!=endkey and doflag==1):
                        joinedwords=''.join(user)
                        if(joinedwords.find('\n')!=-1):
                            sizeword=len(joinedwords)
                            joinedwords=joinedwords[0:sizeword-1]
                        syntaxofcntrl='}'+syntaxofcntrl+" "+joinedwords+');'
                        
                        doflag=0
                        break
                        
                    elif(ll.find(endkey)!=-1):
                        
                        if(endkey.find('this')!=-1):
                            doflag=1
                            
                            syntaxofcntrl=syntaxofcntrl+getcntrlsyn(endkey)
                            break

                        else:
                            
                            syntaxofcntrl=syntaxofcntrl+getcntrlsyn(endkey)
                            doflag=0
                            break
                        
            else:
                
                syn=getcntrlsyn(y)+'\n'
##                endingofcontrol=getending(y)
                
                
                break
            
            syn=syntaxofcntrl+'\n'
            break


    

    if(syn.find('\n')!=-1):
        size=len(syn)            
        syn=syn[0:size-1]+" "+last
    print(syn)
    finalfilewriter(syn)
        



    
userfile.close()
   
   
    
        


    
                
        
                
            
            
                    
                
