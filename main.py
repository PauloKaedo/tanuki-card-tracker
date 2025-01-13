import cv2

def start_webcam():
    cap = cv2.VideoCapture(0)
    print("Press Q to exit...")
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Capture Error!")
                break
            
            cv2.imshow("Webcam Frame", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                print("Finishing Tracker")
                break
            
    finally:
        cap.release()
        cv2.destroyAllWindows()
    
    
if __name__ == "__main__":
    start_webcam()