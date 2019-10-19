from PIL import Image, ImageDraw

image = Image.new('RGB', (600, 600), color=(0, 0, 0))
draw = ImageDraw.Draw(image)
image.save('image.png')

with open('elevation_small.txt') as file: # Use file to refer to the file object
   data = file.readlines()

elevations = [[int(each) for each in line.split()] for line in data]

   

def get_max_and_min(elevations):
   min = elevations[0][0]
   max = elevations[0][0]
   
   for each in elevations:
      for point in each:
         if point < min:
            min = point
         if point > max:
            max = point
   return (min, max)

def convert_elevations_to_brightness(elevations, min, max):
   brightness_big_list = []
   row_of_brightness = []

   for row in elevations:
      for elevation in row:
         brightness = round(((elevation - min) / (max-min)) * 255)
         row_of_brightness.append(brightness)
      brightness_big_list.append(row_of_brightness)
      row_of_brightness = []
      
   return brightness_big_list  

def draw_map(brightness_big_list):
   my_map = image.copy()
  
   for y, row in enumerate(brightness_big_list, 0):
      for x, brightness in enumerate(row, 0):
         
        
            
         my_map.putpixel((x, y), (brightness, brightness, brightness))
   my_map.save('map.png')

   
list_info = get_max_and_min(elevations)
min = list_info[0]
max = list_info[1]
brightness = convert_elevations_to_brightness(elevations, max, min)
print(len(brightness[0]))
draw_map(brightness)






   

