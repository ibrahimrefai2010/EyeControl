global y_pos, x_pos, counter, reading_y_min, reading_y_max, reading_x_min, reading_x_max
reading_y_min = 1 #each one has a unique value to prevent zero division 
reading_y_max = 2
reading_x_max = 3 
reading_x_min = 4
postion = 0
tracking_landmark_1 = 340
tracking_landmark_2 = 473
y_pos = 1
x_pos = 1
counter = 0

def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)



def store_Reading():
    global reading_x_max, reading_x_min, reading_y_max, reading_y_min, x_pos, y_pos, counter
    print("\nstore reading called\n")
    print(f"reading_y_min: {reading_y_min == 1} reading_y_max: {reading_y_max == 2}\nreading_x_max: {reading_y_max == 2} reading_x_min: {reading_x_min}\n\n")
    if counter == 0:
        reading_y_min = y_pos
    elif counter == 1:
        reading_y_max = y_pos
    elif counter == 2:
        reading_x_max = x_pos
    elif counter == 3:
        reading_x_min = x_pos
    counter += 1

def run():
    import cv2
    import mediapipe as mp
    import pyautogui
    
    global screen_h, screen_w, landmark_points, frame_h, frame_w, frame, Keyboard, KeyboardStr, x, y, y_distance, y_range, x_distance, x_range
    postion = 0
    KeyboardStr = "abc0de1fgh2ij3kln4mo5pqr56tu7vwx78z9"
    Keyboard = []
    for Char in KeyboardStr:
        Keyboard.append(Char)
    
    cam = cv2.VideoCapture(0)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    #KeyboardThread = threading.Thread(target=StartBlinkKeyboard)
    #KeyboardThread.start()  
    screen_w, screen_h = pyautogui.size()
    while True:
        _, frame = cam.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape  
        if landmark_points:
            landmarks = [landmark_points[0].landmark[tracking_landmark_1], landmark_points[0].landmark[tracking_landmark_2]]
            x = (landmarks[1].x - landmarks[0].x)
            y = (landmarks[1].y - landmarks[0].y)
            
            
            x_range = reading_x_max - reading_x_min
            x_distance = x - reading_x_min
            x_percentage = (x_distance / x_range)
            y_range = reading_y_max - reading_y_min
            y_distance = y - reading_y_min
            y_percentage = (y_distance / y_range)
            x_pos = (screen_w * x_percentage)
            y_pos = (screen_h * y_percentage)
            #print(f"y: y_distance: {y_distance} y_range: {y_range}\nx_distance: {x_distance} x_range: {x_range}\nreading_y_min: {reading_y_min} reading_y_max: {reading_y_max}\nreading_x_max: {reading_x_max} reading_x_min: {reading_x_min}\n\n")
            
            pyautogui.FAILSAFE = False
            pyautogui.moveTo(x_pos, y_pos)
            
            for landmark in landmarks:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 255))       
            UpdateEdgeKeyboard()
            
        cv2.imshow('Eye Controlled Mouse', frame)
        cv2.waitKey(1)


def StartBlinkKeyboard():
    import cv2
    import mediapipe as mp
    import pyautogui
    import ctypes
    while True:
        CurrentChar = ''
        isLeftEyeBlinking = False
        isRightEyeBlinking = False
        print(isRightEyeBlinking, isLeftEyeBlinking)
        left = [landmark_points[0].landmark[145], landmark_points[0].landmark[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if (left[0].y - left[1].y) < 0.004 and not isRightEyeBlinking:
            isLeftEyeBlinking = True
            postion = max(len(Keyboard), min((postion - 1), 0))
            Current_char = Keyboard[postion]
            print(Current_char)
        elif(not isRightEyeBlinking):
            isLeftEyeBlinking = False



        right = [landmark_points[0].landmark[374], landmark_points[0].landmark[386]]
        for landmark in right:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if (right[0].y - right[1].y) < 0.004 and not isLeftEyeBlinking:
            isRightEyeBlinking = True
            postion = clamp(postion + 1, 0, len(Keyboard) - 1)
            print(postion)
            Current_char = Keyboard[postion]
            print(Current_char)
        elif(not isLeftEyeBlinking):
            isRightEyeBlinking = False
            
            
            
def UpdateEdgeKeyboard():
    import cv2
    import mediapipe as mp
    import pyautogui
    import ctypes
    CurrentChar = ''
        
    trigger_x = x_pos * (1 + 10/100)
    trigger_y = y_pos * (1 + 10/100)