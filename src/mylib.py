def sayHello():
    print("hello")

def getKey(keyPath):
    d=dict() #딕셔너리 d
    f=open(keyPath,'r') #keypath read해서 open
    for line in f.readlines(): #파일 모든 줄 읽음
        row=line.split('=')#=를 기준으로 split
        row0=row[0]
        d[row0]=row[1].strip()
    return d
