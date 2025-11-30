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

#   ----->> Load the images and convert them to RGB format <<-----
video_capture = cv2.VideoCapture(0)
address = "http://192.168.100.42:8080/video"
video_capture.open(address)

def facing_collecting(image_paths):
    known_faces = []
    known_names = []

    for path in image_paths:
        image = face_recognition.load_image_file(path)
        encoding = face_recognition.face_encodings(image)[0]
        known_faces.append(encoding)
        known_names.append(path.split("\\")[-1].split(".")[0])

    return known_faces, known_names

# insert image pathsweee
image_list = [
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_01 (Aatika).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_05 (Wasay).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_09 (Anil).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_12 (Arooba).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_16 (Asifa).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_17 (Ayesha).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_18 (Bisma).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_19 (Damni).jpg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_22 (Habibullah).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_24 (Hamid Ali).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_27 (Humaira).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_28 (Maham Urooj).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_29 (Mahtab).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_31 (Maqbool).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_32 (Maryam).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_34 (Mahek).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_35 (Memoona).jpg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_37 (Asharab).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_38 (Fazil).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_39 (Anas).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_41 (Anas).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_43 (Aziz).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_44 (Bakhsh).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_46 (Muhammad).jpg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_49 (Hussain).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_50 (Mashooque).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_51 (Mubashir).jpg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_54 (Sinan).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_55 (Taha).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_57 (Musabbiha).jpg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_58 (Nimarta).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_59 (Nasir).jpg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_61 (Nirmala).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_62 (Paras Rai).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_63 (Ghafoor).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_64 (Prerna).jpg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_66 (Ramesh).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_67 (Ramesh).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_69 (Saad).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_76 (Shoaib).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_80 (Tanzeela).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_83 (Waheed).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_89 (Rajesh).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_90 (Irtaza).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_91 (Ahmed Raza).jpeg",
    "D:\\Face_recognition_Project\\Faces_Student\\2k25_CS_92 (Abdullah).jpeg"
]

known_faces, known_face_name = facing_collecting(image_list)

#   ----->> Prepare for attendance <<-----
students = known_face_name.copy()

face_locations = []
face_encodings = []

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

excel_file = f"D:\\Face_recognition_Project\\Attandace\\{current_date}.xlsx"

# Create Excel file if not exists
if not os.path.exists(excel_file):
    empty_df = pd.DataFrame(columns=["Name", "Time", "Status"])
    empty_df.to_excel(excel_file, index=False)

attendance_data = pd.DataFrame(columns=["Name", "Time", "Status"])

#   ----->> Start capturing video <<-----
while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    name = "Unknown"
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        face_distance = face_recognition.face_distance(known_faces, face_encoding)
        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            name = known_face_name[best_match_index]

        frequency = 2000
        duration = 800
        
        df = pd.read_excel(excel_file)

        # Add text if student is present
        if name in known_face_name:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10, 30)
            fontScale = 1
            fontColor = (0, 255, 0)
            thickness = 3
            lineType = 2

            cv2.putText(frame, name + " Present ", bottomLeftCornerOfText,
                        font, fontScale, fontColor, thickness, lineType)

            df = pd.read_excel(excel_file)

            # Check if name is already recorded
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

    cv2.imshow("Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

#   ----->> Release the camera <<-----
video_capture.release()
cv2.destroyAllWindows()
