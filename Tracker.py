global reading_x_max
global reading_x_min
global reading_y_max
global reading_y_min
reading_x_max = 300
reading_x_min = 300
reading_y_max = 300
reading_y_min = 300

def store_Reading():
    global reading_x_max
    global reading_x_min
    global reading_y_max
    global reading_y_min
    global x
    global y
    if reading_y_min == 300:
        reading_y_min = y
    elif reading_y_max == 300:
        reading_y_max = y
    elif reading_x_max == 300:
        reading_x_max = x
    elif reading_x_min == 300:
        reading_x_min = x
    #print("Reading Stored")
    #print(reading_x_max,  reading_x_min, reading_y_max, reading_y_min, sep="\n")

def run():
    import cv2
    import mediapipe as mp
    import pyautogui
    import ctypes
    
    global position
    postion = 0
    KeyboardStr = "abcdefghijklnmopqrstuvwxyz0123456789"
    Keyboard = []
    for Char in KeyboardStr:
        Keyboard.append(Char)
        print(Char)
    print(Keyboard, "\n", Keyboard[postion])
    
    cam = cv2.VideoCapture(0)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    screen_w, screen_h = pyautogui.size()
    while True:
        _, frame = cam.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape
        if landmark_points:
            landmarks = [landmark_points[0].landmark[450], landmark_points[0].landmark[477]]
            global x
            global y
            x = (landmarks[1].x - landmarks[0].x)
            y = (landmarks[1].y - landmarks[0].y)
            print(x)
            print(y)
            try:
                x_range = reading_x_max - reading_x_min
                x_distance = x - reading_x_min
                x_percentage = (x_distance / x_range)
                
                y_range = reading_y_max - reading_y_min
                y_distance = y - reading_y_min
                y_percentage = (y_distance / y_range)
                
                x_pos = (screen_w * x_percentage)
                y_pos = (screen_h * y_percentage)
                #y_pos = 600
                
                pyautogui.FAILSAFE = False
                pyautogui.moveTo(x_pos, y_pos)
                #print(f"x:{x_percentage * 100}\ny:{y_percentage * 100}")
                #print(f"x: {x}   y: {y}")
                #print(y_percentage, x_percentage, sep="\n")
                '''
                for landmark in landmarks:
                    x = int(landmark.x * frame_w)
                    y = int(landmark.y * frame_h)
                    cv2.circle(frame, (x, y), 3, (0, 255, 255))
                '''
            except ZeroDivisionError:
                print(Exception)

            CurrentChar = ''
            left = [landmark_points[0].landmark[145], landmark_points[0].landmark[159]]
            for landmark in left:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 255))
            if (left[0].y - left[1].y) < 0.004:
                postion -= 1
                Current_char = Keyboard[postion]
                print(Current_char)
            
            right = [landmark_points[0].landmark[374], landmark_points[0].landmark[386]]
            for landmark in right:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 255))
            if (right[0].y - right[1].y) < 0.004:
                postion += 1
                Current_char = Keyboard[postion]
                print(Current_char)
        cv2.imshow('Eye Controlled Mouse', frame)
        cv2.waitKey(1)