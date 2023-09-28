"""
So far i got into the point that i can use the camera and trace the joints but i just couldnt find a optimal way for shiled stage or other stages in that matter. 
For some reason when i try to calcualte the distance between joints it just doesnt calculate them and i can't create a print statement to see whether it does work or not cause it doesnt print the line
But other than that camera works fine
"""

import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose 

cap = cv2.VideoCapture(0)

stageShield = None
stageIdle = 1
stageLa = None
stageHa = None

# def calculate_angle(a,b,c):
#     a = np.array(a)
#     b = np.array(b)
#     c = np.array(c)

#     radians = np.arctan2(c[1] - b[1], c[0]-b[0]) - np.arctan2(a[1] - b[1], a[0]- b[1])
#     angle = np.abs(radians*180.0/np.pi)

#     if angle > 180.0:
#         angle = 360 - angle
#     return angle

def findDistance(x1, y1, x2, y2):
    dist = np.sqrt((x2-x1)**2+(y2-y1)**2)
    return dist

with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as pose:
    while cap.isOpened():
        success, image= cap.read()
        if not success:
            print("Ignoring No Video in Camera frame")
            continue

        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        results = pose.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        try:
            landmarks = results.pose.landmarks.landmark

            right_elbow_x = landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x
            right_elbow_y = landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y

            right_wrist_x = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x
            right_wrist_y = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y

            left_elbow_y = landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y
            left_elbow_x = landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x

            left_wrist_y = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y
            left_wrist_x = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x
            
            distance_wrist = findDistance(right_wrist_x, right_wrist_y, left_wrist_x, left_wrist_y)
            distance_elbow = findDistance(right_elbow_x, right_elbow_y, left_elbow_x, left_elbow_y)

            print(distance_wrist, distance_elbow)
            
            if (distance_wrist < 70 and distance_elbow < 100) and stageHa == None and stageLa == None:
                stageShield = "active"
                stageIdle = 0
                stageHa = None
                stageLa = None
                print("Shield is active")
            if distance_wrist >70 and distance_elbow>100:
                stageShield = "inactive"
                print('Shield is inactive')
            if (stageShield == "inactive" or None) and stageHa == None and stageLa == None: 
                stageIdle = 1



            # angleL = calculate_angle(left_elbow, left_shoulder, right_shoulder)
            # angleR = calculate_angle(right_elbow, right_shoulder, left_shoulder)
            
            # cv2.putText(image, str(angleL),
            #             tuple(np.multiply(left_shoulder, [640, 480])).astype(int),
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
            #             )

            # cv2.putText(image, str(angleR),
            #             tuple(np.multiply(right_shoulder, [640, 480])).astype(int),
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2, cv2.LINE_AA
            #             )
            # if stageIdle == 1:
            #     print("Idle")
            # if angleR and angleL <100:
            #     stageShield = "active"
            #     stageIdle = 0
            #     stageHa = None
            #     stageLa = None
            #     print("Shield is active")
            # if angleR and angleL >100:
            #     stageShield = "inactive"
            #     print("Shield is inactive")
            

        except:
            pass
        
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
        )

        cv2.imshow('MediaPipeShow', cv2.flip(image, 1))

        if cv2.waitKey(5) & 0xFF == 27:
            break 

cap.release()