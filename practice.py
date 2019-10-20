from PIL import Image, ImageDraw

im = Image.new('RGBA', (400, 400))
im.getpixel((0, 0)) 
(0, 0, 0, 0)
for x in range(100):
   for y in range(50):
      im.putpixel((x, y), (0, 210, 100))
from PIL import ImageColor
for x in range(100):
   for y in range(50, 100):
      im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
im.getpixel((0, 0)) 
(210, 210, 210, 255)
im.getpixel((0, 50)) 
(169, 169, 169, 255)
im.save('putPixel.png')

# class Map:
#     def __init__(self, file):
#         self.file = file
#         self.elevations = elevations
# image = Image.new('RGB', (600, 600), color=(0, 0, 0))
# draw = ImageDraw.Draw(image)
# image.save('image.png')

# with open('elevation_small.txt') as file: # Use file to refer to the file object
#    data = file.readlines()
# elevations = [[int(each) for each in line.split()] for line in data]

# def get_max_and_min(elevations):
#    min = elevations[0][0]
#    max = elevations[0][0]
#    for each in elevations:
#       for point in each:
#          if point < min:
#             min = point
#          if point > max:
#             max = point
#    return (min, max)

# def convert_elevations_to_brightness(elevations, min, max):
#    brightness_big_list = []
#    row_of_brightness = []
#    for row in elevations:
#       for elevation in row:
#          brightness = round(((elevation - min) / (max-min)) * 255)
#          row_of_brightness.append(brightness)
#       brightness_big_list.append(row_of_brightness)
#       row_of_brightness = []   
#    return brightness_big_list  

# def draw_map(brightness_big_list):
#    my_map = image.copy()
#    for y, row in enumerate(brightness_big_list, 0):
#       for x, brightness in enumerate(row, 0):  
#          my_map.putpixel((x, y), (brightness, brightness, brightness))
#    my_map.save('map.png')

   
# list_info = get_max_and_min(elevations)
# min = list_info[0]
# max = list_info[1]
# brightness = convert_elevations_to_brightness(elevations, max, min)
# print(len(brightness[0]))
# draw_map(brightness)



# import math
# from PIL import Image
# import numpy as np
# import random as r


# class Map:
#     def __init__(self, file):
#         self.file = file
#         self.elevations = []
#         self.min_elevation = []
#         self.max_elevation = []
#         self.text_contents = []
#         self.colors_big_list = []
#         self.little_rows_of_colors = []
#         self.paths = []

#     def read_file(self):
#         with open(self.file) as text_file:
#             self.text_contents = text_file.read()

#     def find_elevations(self):
#         self.elevations = [[int(each) for each in line.split()]
#                            for line in self.text_contents.split("\n")]

#     def find_min_and_max(self):
#         self.min_elevation = self.elevations[0][0]
#         self.max_elevation = self.elevations[0][0]

#         for each in self.elevations:
#             for integer in each:
#                 if integer < self.min_elevation:
#                     self.min_elevation = integer
#                 if integer > self.max_elevation:
#                     self.max_elevation = integer

#     def get_colors_from_elevations(self):
#         for rows in self.elevations:
#             for number in rows:
#                 color_int = round(
#                     ((number - self.min_elevation) / (self.max_elevation-self.min_elevation)) * 255)
#                 self.little_rows_of_colors.append(color_int)
#             self.colors_big_list.append(self.little_rows_of_colors)
#             self.little_rows_of_colors = []
#         print("i am running")
#         # print(self.colors_big_list)

#     def create_map_image(self):
#         print("create_map")
#         img = Image.fromarray(np.uint8(self.colors_big_list))
#         img.save("test.png")

#         # print(self.elevations[0])


# class Path:
#     def __init__(self, elevations):
#         self.position = 0
#         self.elevations = elevations
#         self.previous_points = []

#     def find_next_point(self):
#         y = r.randint(0, 600)
#         x = 0
#         while x < 599:
#             NE = abs((self.elevations[y-1][x+1]) - self.position)
#             E = abs((self.elevations[y][x+1]) - self.position)
#             SE = abs((self.elevations[y+1][x+1]) - self.position)
#             smallest_delta = min(NE, E, SE)
#             if smallest_delta == NE:
#                 y -= 1
#                 x += 1
#                 self.position = self.elevations[y][x]
#             elif smallest_delta == E:
#                 x += 1
#                 self.position = self.elevations[y][x]
#             else:
#                 y += 1
#                 x += 1
#                 self.position = self.elevations[y][x]
#         print(x)


# if __name__ == "__main__":
#     map = Map("elevation_small.txt")
#     map.read_file()
#     map.find_elevations()
#     map.find_min_and_max()
#     map.get_colors_from_elevations()
#     map.create_map_image()
#     path = Path(map.elevations)
#     path.find_next_point()