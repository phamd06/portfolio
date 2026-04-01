from PIL import Image

def remove_image_metadata(input_file, output_file):
    img = Image.open(input_file)
    data = list(img.getdata())
    clean_img = Image.new(img.mode, img.size)
    clean_img.putdata(data)
    clean_img.save(output_file)
    return output_file

input_path = input("Enter image file name (e.g. photo.jpg): ")
output_path = "clean_" + input_path

remove_image_metadata(input_path, output_path)

print("Metadata removed. Clean file saved as:", output_path)