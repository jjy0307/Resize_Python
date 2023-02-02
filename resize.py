from PIL import Image

def resize(input, output):
    img = Image.open(input)

    # resize width, height
    resize_img = img.resize((3000, 3000))
    filename = "resize.png"
    savename = output + filename
    resize_img.save(savename)


 
if __name__ == '__main__':
    resize(input image, output path)
