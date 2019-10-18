from PIL import Image, ImageDraw

image = Image.new('RGBA', (600, 600), color=(0, 0, 0, 255))
draw = ImageDraw.Draw(image)
image.save('image.png')

with open('elevation_small.txt') as file: # Use file to refer to the file object
   data = file.read()

elevations = [[int(each) for each in line.split()] for line in data.split("\n")]

min = elevations[0][0]
max = elevations[0][0]
for each in elevations:
   for point in each:
      if point < min:
         min = point
         if point > max:
            max = point

coordinates_big_list = []
rows_of_coordinates = []

for rows in elevations:
   for coordinate in rows:
        color_int = round(((coordinate - min) / (max-min)) * 255)
        rows_of_coordinates.append(color_int)
   coordinates_big_list.append(rows_of_coordinates)
   rows_of_coordinates = []
