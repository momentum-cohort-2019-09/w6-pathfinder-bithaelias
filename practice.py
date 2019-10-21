from PIL import Image, ImageDraw
import random as random
draw = ImageDraw.Draw(my_map)

class Map:
   def__init__(self, file):
      self.file = file


   def creates_my_map(self):
      self.my_map = Image.new('RGB', (600, 600), color=(0, 0, 0))

   def open_file(self):
      with open(self.file) as file: # Use file to refer to the file object
         self.data = file.readlines()

   def splits_data(self)      
      self.elevations_rows = [[int(each) for each in line.split()] for line in data]   

   def get_max_and_min(self,elevations_rows):
      self.minimum = self.elevations_rows[0][0]
      self.maximum = self.elevations_rows[0][0]
      for each in self.elevations_rows:
         for point in each:
            if point < self.minimum:
               self.minimum = point
            if point > self.maximum:
               self.maximum = point
      return (self.minimum, self.maximum)

   def convert_elevations_to_brightness(elevations_rows, minimum, maximum):
      brightness_big_list = []
      row_of_brightness = []
      for row in elevations_rows:
         for elevation in row:
            brightness = round(((elevation - minimum) / (maximum-minimum)) * 255)
            row_of_brightness.append(brightness)
         brightness_big_list.append(row_of_brightness)
         row_of_brightness = [] 
      return brightness_big_list
         
   def draw_map(brightness_big_list):
      for y, row in enumerate(brightness_big_list, 0):
         for x, brightness in enumerate(row, 0):  
            my_map.putpixel((x, y), (brightness, brightness, brightness))
class Path:   
   def taking_greedy_path():
      x = 0
      y = random.randint(0, len(elevations_rows))
      point = (elevations_rows[x][y])
      while x < (len(elevations_rows) - 1):
         upper_right = abs((elevations_rows[x+1][y-1]) - point)
         middle_right = abs((elevations_rows[x+1][y]) - point)
         lower_right = abs((elevations_rows[x+1][y+1]) - point)
         choose_smallest_elevation = min(upper_right, middle_right, lower_right)
         if choose_smallest_elevation == upper_right:
            y -= 1
            x += 1
            point = (elevations_rows[x][y])
            my_map.putpixel((x, y), (255, 0, 0))   
         elif choose_smallest_elevation == middle_right:
            x += 1   
            point = (elevations[x][y])
            my_map.putpixel((x, y), (255, 0, 0))   
         elif choose_smallest_elevation == lower_right:
            y += 1
            x += 1  
            point = (elevations_rows[x][y])
            my_map.putpixel((x, y), (255, 0, 0))   
       
list_info = get_max_and_min(elevations_rows)
minimum = list_info[0]
maximum = list_info[1]
brightness = convert_elevations_to_brightness(elevations_rows, minimum, maximum)
draw_map(brightness)
taking_greedy_path()
my_map.save('map.png')

if __name__ == "__main__":
   map = Map('elevation_small.txt')
