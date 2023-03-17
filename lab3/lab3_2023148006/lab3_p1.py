# get input
usb_size = int(input("Enter USB size (GB): "))

# convert bytes to bits by multiplying by 8 as well
usb_size = usb_size * 1_000_000_000 * 8
# calculate pixel count
pixels = 800 * 600

# f-string is basically concatination
print(f"{format(usb_size//(pixels*8//5), '>5')} images in GIF format can be stored")
print(f"{format(usb_size//(pixels*24//25), '>5')} images in JPEG format can be stored")
print(f"{format(usb_size//(pixels*24//8), '>5')} images in PNG format can be stored")
print(f"{format(usb_size//(pixels*48), '>5')} images in TIFF format can be stored")
