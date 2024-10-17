## 0.环境配置

创建虚拟环境；

激活虚拟环境

安装第三方库

```cmd
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirement.txt
```



## 1.抠图样本存放于文件夹

将抠图样本按照`{类别名称}_{序号}`命名，例如`施工车辆_1.png`,`施工车辆_2.png`，统一置于文件夹`samples`下，



## 2.修改配置文件

按需修改`config/config.yml`



## 3.执行增强主程序

```python
python main.py
```



## 4.查看结果

查看输出文件夹`AugSamples`下的结果