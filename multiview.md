# Multi-view Human Pose Estimation

## Generalizable Human Pose Triangulation

### 介绍

常见的多视角方法，首先在多个视角内分别进行2dHPE,然后进行三角化，并采用RANSAC去除因遮挡而产生的错误估计，得到3dHPE。这种做法不是端到端的，因为	RANSAC是不能学习的。

还有的方法从多个视角中提取特征，譬如热图之类的，然后聚合起来估计3d姿态，以端到端的方式，这种被称为**可学习的三角化**。

然而这种可学习的三角化方法局限于特定设置的视角和相机位置，当相机数量，摆放关系发生改变后，效果大多会出现下滑



### 相关工作





### 方法

![image-20230210145305005](C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230210145305005.png)

pipeline





## Learnable Triangulation of Human Pose



