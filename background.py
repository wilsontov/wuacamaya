from SimpleCV import *

def backg(images_path, extension, save_path):
    directory = os.path.join(images_path, extension)
    files = glob.glob(directory)

    i = 0
    for file in files:
        print(file)
        new_img = Image(file)
        mask = new_img.hueDistance(color=Color.WHITE).binarize()
        result = new_img - mask.invert()
        result.save(save_path + '/bk' + str(i) + ".jpg")
        i += 1

if __name__ == "__main__":
    import sys

    backg(sys.argv[1], sys.argv[2], sys.argv[3])

