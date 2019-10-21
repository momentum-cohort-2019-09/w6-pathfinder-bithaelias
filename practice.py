from PIL import Image, ImageDraw
import random as random


class Map:
   def __init__(self, file):
      self.data = self.open_file(file)
      self.my_map = Image.new('RGB', (600, 600), color=(0, 0, 0))
      self.elevations_rows = self.splits_data()
      self.minimum = self.get_max_and_min()[0]
      self.maximum = self.get_max_and_min()[1]
      self.elevations_map = self.draw_map(self.convert_elevations_to_brightness())

   def open_file(self, file):
      with open(file) as file: # Use file to refer to the file object
         data = file.readlines()
         return data

   def splits_data(self):      
      elevations_rows = [[int(each) for each in line.split()] for line in self.data]
      return elevations_rows   

   def get_max_and_min(self):
      minimum = self.elevations_rows[0][0]
      maximum = self.elevations_rows[0][0]
      for each in self.elevations_rows:
         for point in each:
            if point < minimum:
               minimum = point
            if point > maximum:
               maximum = point
      return (minimum, maximum)

   def convert_elevations_to_brightness(self):
      brightness_big_list = []
      row_of_brightness = []
      for row in self.elevations_rows:
         for elevation in row:
            brightness = round(((elevation - self.minimum) / (self.maximum-self.minimum)) * 255)
            row_of_brightness.append(brightness)
         brightness_big_list.append(row_of_brightness)
         row_of_brightness = [] 
      return brightness_big_list
         
   def draw_map(self, brightness_big_list):
      for y, row in enumerate(brightness_big_list, 0):
         for x, brightness in enumerate(row, 0):  
            self.my_map.putpixel((x, y), (brightness, brightness, brightness))
      self.my_map.save('maps.png')
      return self.my_map   

# class Path:   
#    def taking_greedy_path():
#       x = 0
#       y = random.randint(0, len(elevations_rows))
#       point = (elevations_rows[x][y])
#       while x < (len(elevations_rows) - 1):
#          upper_right = abs((elevations_rows[x+1][y-1]) - point)
#          middle_right = abs((elevations_rows[x+1][y]) - point)
#          lower_right = abs((elevations_rows[x+1][y+1]) - point)
#          choose_smallest_elevation = min(upper_right, middle_right, lower_right)
#          if choose_smallest_elevation == upper_right:
#             y -= 1
#             x += 1
#             point = (elevations_rows[x][y])
#             my_map.putpixel((x, y), (255, 0, 0))   
#          elif choose_smallest_elevation == middle_right:
#             x += 1   
#             point = (elevations[x][y])
#             my_map.putpixel((x, y), (255, 0, 0))   
#          elif choose_smallest_elevation == lower_right:
#             y += 1
#             x += 1  
#             point = (elevations_rows[x][y])
#             my_map.putpixel((x, y), (255, 0, 0))   
       
# list_info = get_max_and_min(elevations_rows)
# minimum = list_info[0]
# maximum = list_info[1]
# brightness = convert_elevations_to_brightness(elevations_rows, minimum, maximum)
# draw_map(brightness)
# taking_greedy_path()
# my_map.save('map.png')

if __name__ == "__main__":
   map = Map('elevation_small.txt')
