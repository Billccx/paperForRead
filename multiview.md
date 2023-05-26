# Multi-view

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







## Fast and Robust Multi-Person 3D Pose Estimation from Multiple Views

### pipeline

首先使用现成的检测器在各个视角下对人物进行检测和姿态估计，得到含有噪声的结果。

然后使用一个匹配算法，找到各视角下对应的人物，并丢弃错误结果

之后使用3DPS模型恢复3D姿态

最后使用追踪和滤波技术优化结果







### 跟踪与滤波

只对关键帧进行处理（人物检测、姿态估计、匹配）

其他帧通过平滑性假设来给出姿态，投影回各视角下生成外接检测框

采用黎曼扩展卡尔曼滤波来增强时间平滑性和骨长度约束















## MetaPose: Fast 3D Pose from Multiple Views without 3D Supervision





# Bottom Up









## Single-Stage Multi-Person Pose Machines

### 动机

传统人体表示中，人体位置和关节点位置是割裂的

两阶段方法仍存在计算冗余

SPM通过人体根节点+其余节点驱根节点偏移量，将人体位置与关节点位置关联在一起

首个单阶段多人姿态估计方法

### 方法

#### SPR表示

引入辅助关节点：root  用于表示场景中一个人物的位置

该人物身上的关节点j的位置由下式表示：
$$
\left(x_i^j, y_i^j\right)=\left(x_i^{\mathrm{r}}, y_i^{\mathrm{r}}\right)+\left(\delta x_i^j, \delta y_i^j\right)
$$
原点+位移的形式

SPR的核心思想是用root节点+j个位移来表示人体姿态
$$
\mathcal{P}=\left\{\left(x_i^{\mathrm{r}}, y_i^{\mathrm{r}}\right),\left(\delta x_i^1, \delta y_i^1\right),\left(\delta x_i^2, \delta y_i^2\right), \ldots,\left(\delta x_i^K, \delta y_i^K\right)\right\}_{i=1}^N .
$$


#### 单阶段网络结构









# VideoBased

## 3D human pose estimation in video with temporal convolutions and semi-supervised training





## DeciWatch: A Simple Baseline for 10× Efficient 2D and 3D Pose Estimation

### 动机

ImageBased计算开销过大