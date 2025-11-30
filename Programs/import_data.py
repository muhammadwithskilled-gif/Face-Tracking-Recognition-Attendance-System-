import os
import pandas as pd


base_path = r"C:\Users\sabah computer\Desktop\face reorganization\images"

data = []

for person in os.listdir(base_path):
    person_path = os.path.join(base_path, person)
    if os.path.isdir(person_path):  
        for img in os.listdir(person_path):
            if img.lower().endswith(('.webp', '.jpg', )):  
                full_path = os.path.join(person_path, img)
                print("Found:", person, "->", img)  
                data.append({
                    "person": person,          
                    "image_filename": img,          
                    "image_path": full_path         
                })


df = pd.DataFrame(data)
csv_path = os.path.join(base_path, "metadata.csv")
excel_path = os.path.join(base_path, "metadata.xlsx")

df.to_csv(csv_path, index=False)
df.to_excel(excel_path, index=False)

print("✅ Metadata saved successfully!")
print("CSV file:", csv_path)
print("Excel file:", excel_path)