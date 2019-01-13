import cv2
import sqlite3
cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('../lib/haarcascade_frontalface_default.xml')

#insert/update data to sqlite
def insertOrUpdate(listInf):
	connect = sqlite3.connect('..//data//output//db3.db')
	c = connect.cursor()
    # cmd="SELECT * FROM People WHERE ID="+str(Id)
    # cursor=conn.execute(cmd)
    # isRecordExist=0
    # for row in cursor:
    #     isRecordExist=1
    # if(isRecordExist==1):
    #     cmd="UPDATE People SET Name="+str(Name_1)+"WHERE ID="+str(Id)
    # else:
    #     cmd="INSERT INTO People(Id,Name) Values("+str(Id)+","+str(Name_1)+")"
	c.executemany('INSERT INTO People VALUES (?,?,?,?)', listInf)
	connect.commit()

listInfor= ['1', 'minh', '23', 'nam']
insertOrUpdate(listInfor)
sampleNum=0
while(True):
    #camera read
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        #incrementing sample number 
        sampleNum=sampleNum+1
        #saving the captured face in the dataset folder
        cv2.imwrite("../data/temp/" +'congphuong' + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('frame',img)
    #wait for 100 miliseconds 
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    # break if the sample number is morethan 20
    break
cam.release()
cv2.destroyAllWindows()