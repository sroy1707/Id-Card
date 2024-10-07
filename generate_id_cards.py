import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# Load student data
data = pd.read_csv('students.csv') 

# Load the ID card template
template = Image.open('template.png') 


font = ImageFont.truetype("arial.ttf", 28)  
name_position = (140, 255)  # Example position for the student's name
id_position = (90, 180)    # Example position for the student's ID
photo_position = (45, 45)   # Position where the student photo will be placed

# Iterate through each student's data to create an ID card
for index, row in data.iterrows():
    # Create a copy of the template for each student
    id_card = template.copy()
    draw = ImageDraw.Draw(id_card)

    # Add student name and ID to the template
    draw.text(name_position, f"{row['Name']}", fill='black', font=font)
    draw.text(id_position, f"{row['ID']}", fill='black', font=font)

    # Load student photo and paste it on the ID card
    photo = Image.open(row['PhotoPath'])
    photo = photo.resize((100, 100))  # Resize the photo to fit the template
    id_card.paste(photo, photo_position)  # Paste photo at the specified position

    # Save the generated ID card
    output_path = f"output/id_card_{row['ID']}.png"
    id_card.save(output_path)

    print(f"Generated ID card for {row['Name']} at {output_path}")

print("All ID cards generated successfully!")
