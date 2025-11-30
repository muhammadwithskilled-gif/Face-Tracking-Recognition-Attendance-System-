#   ----->> Welcome in our Face Recognition System <<-----
#   ----->> Developed by : Muhammad Bin Mansoor <<-----

from PIL import Image
import face_recognition
import cv2
import numpy as np
import winsound
import pandas as pd
import os
from datetime import datetime
import time

#   ----->> Load the images and convert them to RGB format <<-----
video_capture = cv2.VideoCapture(0)

def facing_collecting(image_paths):
    known_faces = []
    known_names = []

    for path in image_paths:
        image = face_recognition.load_image_file(path)
        encoding = face_recognition.face_encodings(image)[0]
        known_faces.append(encoding)
        known_names.append(path.split("\\")[-1].split(".")[0])

    return known_faces, known_names

# insert image paths
image_list = [
# here inert your images path like this <---
  "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_46 (Muhammad).jpg",
]

known_faces, known_face_name = facing_collecting(image_list)

#   ----->> Prepare for attendance <<-----
students = known_face_name.copy()

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
excel_file = f"D:\\Face_recognition_Project\\Attandace\\{current_date}.xlsx"

# Create Excel file if not exists
if not os.path.exists(excel_file):
    empty_df = pd.DataFrame(columns=["Name", "Time", "Status"])
    empty_df.to_excel(excel_file, index=False)

attendance_data = pd.DataFrame(columns=["Name", "Time", "Status"])

#   ----->> Variables for face recognition delay <<-----
face_seen_time = {}        # Track when a face is first seen
recognition_delay = 2      # Delay in seconds before recognizing
frequency = 2000           # Beep frequency
duration = 800             # Beep duration

#   ----->> Start capturing video <<-----
while True:
    ret, frame = video_capture.read()
    if not ret:
        continue

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    current_time_sec = time.time()
    detected_names = []

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        face_distance = face_recognition.face_distance(known_faces, face_encoding)
        best_match_index = np.argmin(face_distance)

        name = "Unknown"
        if matches[best_match_index]:
            name = known_face_name[best_match_index]
            detected_names.append(name)

            # Initialize first seen time
            if name not in face_seen_time:
                face_seen_time[name] = current_time_sec

            # Recognize only after delay
            elif current_time_sec - face_seen_time[name] >= recognition_delay:
                df = pd.read_excel(excel_file)
                already_present = name in df.iloc[:, 0].values

                if not already_present:
                    winsound.Beep(frequency, duration)
                    current_time = datetime.now().strftime("%H:%M:%S")
                    new_row = [name, current_time, "Present"]
                    df.loc[len(df)] = new_row
                    df.to_excel(excel_file, index=False)

                if name in students:
                    students.remove(name)
                    current_time = datetime.now().strftime("%H:%M:%S")
                    attendance_data = pd.concat([
                        attendance_data,
                        pd.DataFrame([[name, current_time, "Present"]],
                                     columns=["Name", "Time", "Status"])
                    ], ignore_index=True)
                    attendance_data.to_excel(excel_file, index=False)

        # Draw rectangle and name on frame
        for (top, right, bottom, left) in face_locations:
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    # Remove faces that are no longer detected
    for seen_name in list(face_seen_time.keys()):
        if seen_name not in detected_names:
            del face_seen_time[seen_name]

    cv2.imshow("Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

#   ----->> Release the camera <<-----
video_capture.release()
cv2.destroyAllWindows()
