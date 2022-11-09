import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles=mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
# For webcam input:
cap = cv2.VideoCapture(0)
with mp_pose.Pose(min_detection_confidence=0.5,
                    min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, video = cap.read()
        video.flags.writeable = False
        video = cv2.cvtColor(video, cv2.COLOR_BGR2RGB)
        results = pose.process(video)
        #true- tracking lines
        video.flags.writeable = True
        video = cv2.cvtColor(video, cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            video,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    # Flip the video horizontally for a selfie-view display.
        cv2.imshow('Body Pose tracker', cv2.flip(video, 1))
        if cv2.waitKey(1)==ord("q"):
            break