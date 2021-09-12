import os
import mylib
import requests
def doIt():
    
    keyPath=os.path.join(os.getcwd(), 'src', 'key12.txt')
    key=mylib.getKey(keyPath)

    serviceKey='serviceKey='+key['gokr']
    title='title=파이썬'
    manageCd='manageCd=MA'
    numOfRows="numOfRows="+str(20)
    pageNo="pageNo="+str(1)
    
    params="&".join([serviceKey,title,manageCd,numOfRows,pageNo])
    
    _url='http://openapi-lib.sen.go.kr'
    url="/openapi/service/lib/openApi?".join([_url,params])
    response=requests.get(url).text
    
    fp=open('week2_homework.txt','w')
    fp.write(response)
    
if __name__ == "__main__":
    doIt()
