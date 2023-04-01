

## DL经典论文











## 梯度消失 梯度爆炸

### 解决方案

1.  预训练加微调
2. 梯度剪切、权重正则（针对梯度爆炸
3. 使用不同的激活函数
4. 使用batchnorm
5. 使用残差结构
6. 使用LSTM网络





##  卷积、反卷积

### 卷积

w:特征图边长

f:卷积核边长

p:padding大小

s:stride

输出尺寸：（w-f+2p)/s+1



### 反卷积

```python
nn.ConvTranspose2d(in_channels=1,out_channels=1,kernel_size=3,stride=2,padding=1,output_padding=1)
```

实现是先对特征图进行padding，然后再进行卷积运算

**kernel_size**依旧是卷积核的大小

**stride**是将初始特征图中间查空，譬如stride=2表示在原始每个像素之间插入一个空像素

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230221163248220.png" alt="image-20230221163248220" style="zoom: 67%;" />

反卷积的**padding**与常规卷积的padding正好相反

padding=kernel_size-1时，相当于0填充

padding=0时，相当于填充kernel_size-1

具体公式为：填充像素=dilation * (kernel_size - 1) - padding

**output_padding**：是在输出特征图的右侧和下侧进行填充的行数，这是因为当stride>1时，不同尺寸的特征图经过卷积之后可能对应相同尺寸的输出，因此反卷积的时候，同样尺寸的输入有多种尺寸的输出，这是就需要output_padding进行控制。





## 循环神经网络









### 贝叶斯决策

















## Deep Residual Learning for Image Recognition

### 介绍

网络深度至关重要，但网络加深会带来梯度消失/爆炸等问题。









## Transformer











