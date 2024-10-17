import cv2
import numpy as np

def lightness(image, factor):
    """_summary_ 调整图像的亮度

    Args:
        image (_type_):  np.adarry
        factor (_type_): float

    Returns:
        _type_: np.adarry
    """

    # 将图像转换为浮点型，以便进行亮度调整
    image = image.astype('float32')

    # 调整亮度
    image = image * factor

    # 将像素值裁剪到[0, 255]范围内，并转换回uint8类型
    image = np.clip(image, 0, 255).astype('uint8')

    return image

if __name__ == "__main__":
    
    image = cv2.imdecode(np.fromfile("utils/下载2.png", dtype=np.uint8), -1)
    
    image = lightness(image, 0.5)
    
    cv2.imencode('.jpg', image)[1].tofile("utils/下载2_l2.jpg")