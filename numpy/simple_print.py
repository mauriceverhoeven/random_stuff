import cv2


def open_grayscale_image(fname):
    """ open the image and return in grayscale"""
    return cv2.imread(fname, cv2.IMREAD_GRAYSCALE)


def thresholding(image, threshold_value=0):
    return cv2.threshold(
        image, threshold_value, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

def simple_print(image, print_width=3):
    ''' prints the grayscale values of the image '''
    output_list = ["\n"]
    (heigth, width) = image.shape
    pixel_list = image.ravel()
    for h in range(heigth):
        for w in range(width):
            pid = w + h * width
            char = f"{pixel_list[pid]:{print_width}}"
            output_list.append(char)
        output_list.append("\n")
    return "".join(output_list)

