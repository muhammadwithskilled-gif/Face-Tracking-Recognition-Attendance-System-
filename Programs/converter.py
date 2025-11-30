import face_recognition
import dlib

detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")
face_rec_model = dlib.face_recognition_model_v1("models/dlib_face_recognition_resnet_model_v1.dat")
