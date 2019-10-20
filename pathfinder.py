from PIL import Image, ImageDraw
import random as random

my_map = Image.new('RGB', (600, 600), color=(0, 0, 0))
draw = ImageDraw.Draw(my_map)



with open('elevation_small.txt') as file: # Use file to refer to the file object
   data = file.readlines()
elevations = [[int(each) for each in line.split()] for line in data]

def get_max_and_min(elevations):
   minimum = elevations[0][0]
   maximum = elevations[0][0]
   for each in elevations:
      for point in each:
         if point < minimum:
            minimum = point
         if point > maximum:
            maximum = point
   return (minimum, maximum)

def convert_elevations_to_brightness(elevations, minimum, maximum):
   brightness_big_list = []
   row_of_brightness = []
   for row in elevations:
      for elevation in row:
         brightness = round(((elevation - minimum) / (maximum-minimum)) * 255)
         row_of_brightness.append(brightness)
      brightness_big_list.append(row_of_brightness)
      row_of_brightness = [] 
   return brightness_big_list
        
def draw_map(brightness_big_list):
   # my_map = image.copy()
   for y, row in enumerate(brightness_big_list, 0):
      for x, brightness in enumerate(row, 0):  
         my_map.putpixel((x, y), (brightness, brightness, brightness))
   # my_map.save('map.png')
   


def taking_greedy_path():
   x = 0
   y = random.randint(0, len(elevations))
   point = (elevations[x][y])
   while x < (len(elevations) - 1):
      upper_right = abs((elevations[x+1][y-1]) - point)
      middle_right = abs((elevations[x+1][y]) - point)
      lower_right = abs((elevations[x+1][y+1]) - point)
      choose_smallest_elevation = min(upper_right, middle_right, lower_right)
      if choose_smallest_elevation == upper_right:
         y -= 1
         x += 1
         point = (elevations[x][y])
         my_map.putpixel((x, y), (255, 0, 0))   
      elif choose_smallest_elevation == middle_right:
         x += 1   
         point = (elevations[x][y])
         my_map.putpixel((x, y), (255, 0, 0))   
      elif choose_smallest_elevation == lower_right:
         y += 1
         x += 1  
         point = (elevations[x][y])
         my_map.putpixel((x, y), (255, 0, 0))   
     
# def draw_path(x, y):
#    my_map = my_map.putpixel((x, y), (255, 0, 0))   
#    pass
  


   
list_info = get_max_and_min(elevations)
minimum = list_info[0]
maximum = list_info[1]
brightness = convert_elevations_to_brightness(elevations, minimum, maximum)

draw_map(brightness)
taking_greedy_path()
my_map.save('map.png')



