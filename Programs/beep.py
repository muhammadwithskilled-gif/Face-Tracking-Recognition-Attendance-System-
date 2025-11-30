# winsound_beep.py
import winsound
frequency = 1000  # Hz
duration = 800    # milliseconds
winsound.Beep(frequency, duration)

# def finding():
#     with open("D:\Face_recognition_Project\Attandace", "r") as f:
#         for line in f:
#             if line("Name"):
#                 print(line)
#                 break

import pandas as pd

df = pd.read_excel("D:\\Face_recognition_Project\\Attandace\\2025-11-12.xlsx")

print(df.iloc[:, 0].to_string(index=False))




