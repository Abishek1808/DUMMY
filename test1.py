import time

f=open('testlog.txt','r')
req=[]
resp=[]
test=[]
test1=[]
reqL=8
resL=7
c=0
rqF=1
rsF=0
crReq=0
crRes=0

while True:
        a= (f.read(2))
        c=c+1
        test.append(a)
        test1.append(a)
        if((rqF==1) and(c%reqL==0) and not (c%resL==0)):
            req=(test)
            if(req[1]=="03" and req[2]=="00" and req[5]=='01'):
                print ('Valid Req')
                print ('request :')
                print (req)
                rqF=0
                rsF=1
                test=[]
                c=0
                crReq=1
            else:
                c=0
                test=[]
                test1=[]
                crReq=0
        if((rsF==1) and(c%resL==0) and not (c%reqL==0)):
            resp=test
            rqF=1
            rsF=0
            test1=[]
            c=0
            if(resp[1]=="03" and resp[2]=="02"):
                crRes=1
                print ('Valid Resp')
                print ('response :')
                print (resp)
            else:
                test=[]
                crRes=0
                c=0
        time.sleep(0.05)



