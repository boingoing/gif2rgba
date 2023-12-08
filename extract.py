from PIL import Image
from PIL import GifImagePlugin

header_number = 10
base_name = "zelda3_frame"
img = Image.open("/Users/taylor/Downloads/giphy.gif")

print("#ifndef __TEXTURE_DATA_%s_H__" % header_number)
print("#define __TEXTURE_DATA_%s_H__" % header_number)
print("")
print("#include <cstddef>")
print("")
print("const uint32_t %s_count = %s;" % (base_name, img.n_frames))
print("const uint32_t %s_time = %s;" % (base_name, 50))
print("const uint32_t %s_width = %s;" % (base_name, img.width))
print("const uint32_t %s_height = %s;" % (base_name, img.height))

for frame in range(0,img.n_frames):
  print("")
  print("const uint8_t %s_%s[] = {" % (base_name, frame))
  img.seek(frame)
  rgba = img.convert("RGBA")
  data = list(rgba.getdata())
  txt = "  "
  for pixel in data:
    for channel in pixel:
      txt += str(channel) + ", "
  print(txt)
  print("};")

print("")
print("const uint8_t* %s_data[] = {" % base_name)
for frame in range(0,img.n_frames):
  print("  %s_%s," % (base_name, frame))

print("};")
print("")
print("#endif  // __TEXTURE_DATA_%s_H__" % header_number)
