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
    if reading_x_max == 300:
        reading_x_max = x
    elif reading_x_min == 300:
        reading_x_min = x
    elif reading_y_max == 300:
        reading_y_max = y
    elif reading_y_min == 300:
        reading_y_min = y
    #print("Reading Stored")
    #print(reading_x_max,  reading_x_min, reading_y_max, reading_y_min, sep="\n")

def run():
    import cv2
    import mediapipe as mp
    import pyautogui
    
    
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
            landmarks = [landmark_points[0].landmark[443], landmark_points[0].landmark[474]]
            global x
            global y
            x = (landmarks[0].x - landmarks[1].x)
            y = (landmarks[0].x - landmarks[1].x)
            x_range = reading_x_min - reading_x_max
            x_distance = x -reading_x_min
            x_percentage = (x_distance - x_range)
            y_range = reading_y_min - reading_y_max
            y_distance = y -reading_y_min
            y_percentage = (y_distance - y_range)
            #print(f"x: {x}\ny: {y}")
            print(y_percentage, x_percentage, sep="\n")
        '''
            left = [landmarks[145], landmarks[159]]
            for landmark in left:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 255))
            if (left[0].y - left[1].y) < 0.004:
                pyautogui.click()
                pyautogui.sleep(1)
        '''
        cv2.imshow('Eye Controlled Mouse', frame)
        cv2.waitKey(1)

