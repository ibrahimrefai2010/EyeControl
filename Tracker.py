import keyboardGUI as GUI
import time
global reading_x_max, reading_x_min, reading_y_max, reading_y_min
reading_y_min = 1 #each one has a unique value to prevent zero division 
reading_y_max = 2
reading_x_min = 3
reading_x_max = 4
postion = 0
Current_char = ''
tracking_landmark_1 = 337
tracking_landmark_2 = 473
trigger_x = 0
invert_trigger_x = 0
calibration = True

def clamp(value, min_value, max_value):
    if value < min_value:
        return min_value
    elif value > max_value:
        return max_value
    else:
        return value



def store_Reading(count):
    global reading_x_max, reading_x_min, reading_y_max, reading_y_min, trigger_x, invert_trigger_x, postion
    if count == 1:
        reading_y_min = y
    elif count == 2:
        reading_y_max = y
    elif count == 3:
        reading_x_max = x
    elif count == 4:
        reading_x_min = x
        print("\nassigned\n")
        time.sleep(0.1)
        trigger_x = reading_x_max * (1 + (10)/100) #sets the triggers for the eyeboard once the calibration is done
        invert_trigger_x = reading_x_min * (1 + (-10)/100)
        postion = 0
        
    #print(f"reading_y_min: {reading_y_min} reading_y_max: {reading_y_max}\nreading_x_max: {reading_x_max} reading_x_min: {reading_x_min}\ny: {y} x:{x}\n\n")

def run():
    import cv2
    import mediapipe as mp
    import pyautogui
    global screen_h, screen_w, landmark_points, frame_h, frame_w, frame, Keyboard, KeyboardStr, x, y, y_distance, y_range, x_distance, x_range, y_percentage, x_percentage, postion, Current_char
    postion = 0
    Current_char = ''
    KeyboardStr = "abc0de1fgh2ij3kln4mo5pqr56tu7vwx78z9"
    Keyboard = ["delete", "enter", "backspace"]
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
            #print(f"y_percentage: {y_percentage} x_percentage: {x_percentage}\ny_distance: {y_distance} y_range: {y_range}\nx_distance: {x_distance} x_range: {x_range}\nreading_y_min: {reading_y_min} reading_y_max: {reading_y_max}\nreading_x_max: {reading_x_max} reading_x_min: {reading_x_min}\ny_pos: {y_pos} x_pos: {x_pos}\n x: {x} y: {y}\n\n")
            
            pyautogui.FAILSAFE = False
            pyautogui.moveTo(x_pos, y_pos)
            
            for landmark in landmarks:
                x_circle = int(landmark.x * frame_w)
                y_circle = int(landmark.y * frame_h)
                cv2.circle(frame, (x_circle, y_circle), 3, (0, 255, 255))
            if calibration == False:
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
            x_ = int(landmark.x * frame_w)
            y_ = int(landmark.y * frame_h)
            cv2.circle(frame, (x_, y_), 3, (0, 255, 255))
        if (left[0].y - left[1].y) < 0.004 and not isRightEyeBlinking:
            isLeftEyeBlinking = True
            postion = max(len(Keyboard), min((postion - 1), 0))
            Current_char = Keyboard[postion]
            print(Current_char)
        elif(not isRightEyeBlinking):
            isLeftEyeBlinking = False



        right = [landmark_points[0].landmark[374], landmark_points[0].landmark[386]]
        for landmark in right:
            x_local = int(landmark.x * frame_w)
            y_local = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if (right[0].y - right[1].y) < 0.004 and not isLeftEyeBlinking:
            isRightEyeBlinking = True
            postion = clamp(postion + 1, 0, len(Keyboard) - 1)
            print(postion)
            Current_char = Keyboard[postion]
            print(Current_char)
        elif(not isLeftEyeBlinking):
            isRightEyeBlinking = False


def CharacterDown():
    global postion, CurrentChar
    postion = clamp(postion + 1, 0, len(Keyboard) - 1)
    CurrentChar = Keyboard[postion]
    print(f"calling: {postion}")
    GUI.SetCurrentChar(CurrentChar)
    
def CharacterUp():
    global postion, CurrentChar
    try:
        postion = clamp(postion - 1, 0, len(Keyboard) - 1)
        CurrentChar = Keyboard[postion]
        GUI.SetCurrentChar(CurrentChar)
    except:
        print(f"{Exception} in CharacterUp")
    

def UpdateEdgeKeyboard():
    import pyautogui
    global postion, trigger_x, invert_trigger_x
    CurrentChar = ''
    #print(f"trigger_x: {trigger_x} x: {x} invert_trigger_x: {invert_trigger_x} condition 1: {x > trigger_x} condition 2: {x < invert_trigger_x}")
    if x > trigger_x:
        CharacterUp()
    if x < invert_trigger_x:
        CharacterDown()
    print(y, (reading_y_min * 0.1) ,y < (reading_y_min * 0.1))
    
    if y < (reading_y_min * 0.1):
        pyautogui.press(CurrentChar)
        print(f"typing  {CurrentChar}")