## 0、写在前面

本项目用于学习RL基础算法，主要面向对象为RL初学者、需要结合RL的非专业学习者，尽量做到: **(中文)注释详细**，**结构清晰**。

注意本项目为实战内容，建议首先掌握相关算法的一些理论基础，再来享用本项目，理论教程参考本人参与编写的[蘑菇书](https://github.com/datawhalechina/easy-rl)。

未来开发计划包括但不限于：多智能体算法、强化学习Python包以及强化学习图形化编程平台等等。

## 1、项目说明

项目内容主要包含以下几个部分：
* [Jupyter Notebook](./notebooks/)：使用Notebook写的算法，有比较详细的实战引导，推荐新手食用
* [codes](./assets/)：这些是基于Python脚本写的算法，风格比较接近实际项目的写法，推荐有一定代码基础的人阅读，下面会说明其具体的一些架构
* [parl](./PARL/)：应业务需求，写了一些基于百度飞浆平台和```parl```模块的RL实例
* [附件](./assets/)：目前包含强化学习各算法的中文伪代码


[codes](./assets/)结构主要分为以下几个脚本：
* ```[algorithm_name].py```：即保存算法的脚本，例如```dqn.py```，每种算法都会有一定的基础模块，例如```Replay Buffer```、```MLP```(多层感知机)等等；
* ```task.py```: 即保存任务的脚本，基本包括基于```argparse```模块的参数，训练以及测试函数等等；
* ```utils.py```：该脚本用于保存诸如存储结果以及画图的软件，在实际项目或研究中，推荐大家使用```Tensorboard```来保存结果，然后使用诸如```matplotlib```以及```seabron```来进一步画图。

## 2、运行环境

python 3.7、pytorch 1.10.0、gym 0.21.0

在项目根目录下执行以下命令复现环境：
```bash
pip install -r requirements.txt
```
如果需要使用CUDA，则需另外安装```cudatoolkit```，推荐```10.2```或者```11.3```版本的CUDA，如下：
```bash
conda install cudatoolkit=11.3 -c pytorch
```
如果conda需要镜像加速安装的话，点击[该清华镜像链接](https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/)，选择对应的操作系统，比如```win-64```，然后复制链接，执行如下命令：
```bash
conda install cudatoolkit=11.3 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/win-64/
```
执行以下Python脚本，如果返回True说明cuda安装成功:
```python
import torch
print(torch.cuda.is_available())
```
如果还是不成功，可以使用pip安装：
```bash
pip install torch==1.10.0+cu113 torchvision==0.11.0+cu113 torchaudio==0.10.0 --extra-index-url https://download.pytorch.org/whl/cu113
```
## 3、使用说明

对于[codes](./assets/)：
* 运行带有task的py脚本

对于[Jupyter Notebook](./notebooks/)]：
* 直接运行对应的ipynb文件就行