import cv2
import numpy as np

def rotation(image, angle):
    
    """_summary_: Rotate the image by the given angle

    Args:
        img (_type_): np.adarry
        angle (_type_): int
    
    return:
        _type_: np.adarry
    """
    
    # 获取图像的高度和宽度
    (h, w) = image.shape[:2]

    # 计算图像中心
    center = (w // 2, h // 2)

    # 获取旋转矩阵
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    # 计算旋转后图像的新边界尺寸
    cos = np.abs(rotation_matrix[0, 0])
    sin = np.abs(rotation_matrix[0, 1])

    new_w = int((h * sin) + (w * cos))
    new_h = int((h * cos) + (w * sin))

    # 调整旋转矩阵中的平移部分，以使旋转后的图像居中
    rotation_matrix[0, 2] += (new_w / 2) - center[0]
    rotation_matrix[1, 2] += (new_h / 2) - center[1]

    # 执行仿射变换，并将新出现的像素填充为0
    rotated_image = cv2.warpAffine(image, rotation_matrix, (new_w, new_h), borderValue=(0, 0, 0))

    return rotated_image
    
    
    
if __name__ == "__main__":
    
    image = cv2.imdecode(np.fromfile("utils/下载2.png", dtype=np.uint8), -1)
    
    rotated_iamge = rotation(image, 45)
    
    cv2.imencode('.png', rotated_iamge)[1].tofile("utils/下载2_r45.png")