import cv2
import numpy as np

def Uscale(image, ratio):
    """_summary_ 放大图像

    Args:
        img (_type_): np.adarry
        angle (_type_): int
    
    return:
        _type_: np.adarry
    """
    
    # 获取原始图像的尺寸
    (h, w) = image.shape[:2]

    # 计算缩放后的新尺寸
    new_w = int(w * ratio)
    new_h = int(h * ratio)

    # 使用指定比例对图像进行缩放
    resized_image = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_LINEAR)

    return resized_image

def Dscale(image, ratio):
    """_summary_ 缩小图像

    Args:
        img (_type_): np.adarry
        angle (_type_): int
    
    return:
        _type_: np.adarry
    """
    
    # 获取原始图像的尺寸
    (h, w) = image.shape[:2]

    # 计算缩放后的新尺寸
    new_w = int(w * 1 / ratio)
    new_h = int(h * 1 / ratio)

    # 使用指定比例对图像进行缩放
    resized_image = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_LINEAR)

    return resized_image
    
    
    
if __name__ == "__main__":
    
    image = cv2.imdecode(np.fromfile("utils/下载2.png", dtype=np.uint8), -1)
    
    resized_image = Dscale(image, 2)
    
    cv2.imencode('.png', resized_image)[1].tofile("utils/下载2_u2.png")