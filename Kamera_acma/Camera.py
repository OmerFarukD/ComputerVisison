import cv2
cap=cv2.VideoCapture(0) #default kamera için 0 yazılır.
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"yükseklik: {height} ")
print(f"genişlik: {width}")
writer=cv2.VideoWriter("video.mp4",cv2.VideoWriter_fourcc(*"DIVX"), 20, (width, height)) 
#fourcc windows kullanıcıları içindir.
while True:
    ret,frame=cap.read()
    cv2.imshow("video",frame)
    
    #kaydetme
    writer.write(frame)
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break
cap.release()
writer.release()
cv2.destroyAllWindows()   