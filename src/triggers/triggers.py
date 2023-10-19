import cv2
import math
from src.video_processing.mp1 import PoseDetector
from src.mechanics.damage import Fighter

cap = cv2.VideoCapture(0)

pose_detector = PoseDetector()

fight_mech = Fighter()

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring No Video in Camera frame")
        continue

    results, image = pose_detector.process_image(image)
    
    try:
        landmarks = pose_detector.get_landmarks(results)

        if landmarks:
            right_elbow_x = landmarks[pose_detector.mp_pose.PoseLandmark.RIGHT_ELBOW.value].x
            right_elbow_y = landmarks[pose_detector.mp_pose.PoseLandmark.RIGHT_ELBOW.value].y

            right_wrist_x = landmarks[pose_detector.mp_pose.PoseLandmark.RIGHT_WRIST.value].x
            right_wrist_y = landmarks[pose_detector.mp_pose.PoseLandmark.RIGHT_WRIST.value].y

            left_elbow_x = landmarks[pose_detector.mp_pose.PoseLandmark.LEFT_ELBOW.value].x
            left_elbow_y = landmarks[pose_detector.mp_pose.PoseLandmark.LEFT_ELBOW.value].y

            left_wrist_x = landmarks[pose_detector.mp_pose.PoseLandmark.LEFT_WRIST.value].x
            left_wrist_y = landmarks[pose_detector.mp_pose.PoseLandmark.LEFT_WRIST.value].y

            # Calculate the angle between the arms
            angle = math.degrees(math.atan2(left_wrist_y - left_elbow_y, left_wrist_x - left_elbow_x) -
                                 math.atan2(right_wrist_y - right_elbow_y, right_wrist_x - right_elbow_x))

            # Adjust angle to be between 0 and 360
            angle = (angle + 360) % 360

            print(angle)

            if 270 < angle < 359 and not fight_mech.low_power_attack and not fight_mech.high_power_attack:
                # Add logic to activate shield position
                fight_mech.apply_shield
                print("Shield position activated")
            if 100 < angle < 150 and not fight_mech.high_power_attack and not fight_mech.apply_shield:
                fight_mech.low_power_attack
                print("Low power attack")
            if 100 < angle < 150 and not fight_mech.low_power_attack:
                fight_mech.high_power_attack

    except Exception as e:
        print(f"Error: {e}")
    
    pose_detector.draw_landmarks(image, results)

    cv2.imshow('MediaPipeShow', cv2.flip(image, 1))

    if cv2.waitKey(5) & 0xFF == 27:
        break 

cap.release()
