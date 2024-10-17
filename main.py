import cv2
import os
import numpy as np
import yaml

from utils.lightness import lightness
from utils.scale import Uscale, Dscale
from utils.rotation import rotation


def crete_multilevel_dirs(config):
    
    file_names = os.listdir(config["samples_path"])
    
    # 使用集合存储不重复的名称
    unique_names = set()
    
    # 遍历文件名，根据"_"分隔符提取前缀部分并添加到集合中
    for file_name in file_names:
        if "_" in file_name:
            prefix = file_name.split("_")[0]
            unique_names.add(prefix)
            
     # 在输出文件夹下创建不重复名称的子文件夹
    for name in unique_names:
        folder_path = os.path.join(config["output_path"], name)
        os.makedirs(folder_path, exist_ok=True)
    
        print("已在{}文件夹中创建了以下文件夹：{}".format(config["output_path"], name))


def sample_aug(config):
    
    for file_name in os.listdir(config["samples_path"]):
        class_name = file_name.split("_")[0]
        image_path = os.path.join(config["samples_path"], file_name)
        image = cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), -1)
        
        output_img_path = os.path.join(config["output_path"], class_name, f"{file_name.split('.')[0]}_none.png")
        cv2.imencode('.png', image)[1].tofile(output_img_path)
        
        # 进行图像增强操作
        for angle in config["rotation_angle"]:
            rotated_image = rotation(image, angle)
            output_img_path = os.path.join(config["output_path"], class_name, f"{file_name.split('.')[0]}_r{angle}.png")
            cv2.imencode('.png', rotated_image)[1].tofile(output_img_path)
        
        # 进行放大增强
        for ratio in config["up_ratio"]:
            scaled_image = Uscale(image, ratio)
            output_img_path = os.path.join(config["output_path"], class_name, f"{file_name.split('.')[0]}_u{ratio}.png")
            cv2.imencode('.png', scaled_image)[1].tofile(output_img_path)
        
        # 进行缩小增强
        for ratio in config["down_ratio"]:
            scaled_image = Dscale(image, ratio)
            output_img_path = os.path.join(config["output_path"], class_name, f"{file_name.split('.')[0]}_d{ratio}.png")
            cv2.imencode('.png', scaled_image)[1].tofile(output_img_path)
            
        # 进行亮度增强
        for factor in config["light_factor"]:
            light_image = lightness(image, factor)
            output_img_path = os.path.join(config["output_path"], class_name, f"{file_name.split('.')[0]}_l{factor}.png")
            cv2.imencode('.png', light_image)[1].tofile(output_img_path)
                


if __name__ == '__main__':

    with open('config/config.yml', 'r', encoding="utf-8") as file:
            user_config = yaml.safe_load(file)
    
    crete_multilevel_dirs(user_config)
    
    sample_aug(user_config)