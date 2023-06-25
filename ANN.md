# 人工神经网络基础

## 第一章

人工智能（Artificial Intelligence，AI）研究的目标是用机器实现 人类的部分智能。

“神经网络是由多个非常简单的处理单元彼此按某种方式相 互连接而形成的计算系统，该系统是靠其状态对外部输入 信息的动态响应来处理信息的。

人工神经网络是一种旨在模仿人脑结构及其功能的信息处理系统

深度学习的好处是用非监督式或半监督式的特征学习和分层特 征提取高效算法来替代手工获取特征。



同机器学习方法一样，深度机器学习方法也有监督学习与无监督学习之分．不同的学习框架下建立的学习模型很不同。 Ø 卷积神经网络（Convolutional neural networks，CNNs）就 是一种深度的监督学习下的机器学习模型； Ø 深度置信网络（Deep Belief Nets，DBNs）就是一种无监督 学习下的机器学习模型



高级别的神经元的刺激是源于相邻低级别神经元的反应。这种 强有力的视觉构架使得能够去检测视野中的复杂的特征

![image-20230618221254127](C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230618221254127.png)



### 人工神经网络的特点

固有的并行结构和并行处理特性

 知识的分布存储特性

 良好的容错特性

高度非线性及计算的非精确性

 自学习、自组织和自适应性

![image-20230618221430360](C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230618221430360.png)



## 第二章

### 生物学基础

一个神经元可以以突触的形式与许多神经元发生 联系，影响许多神经元的活动，也可接受许多神经元的影响 ，因此，突触是信息传递和整合的关键部位。

神经元可看作一个多输入单输出的器件

由多个生物神经元以确定方式和拓扑结构相互连接即形成 生物神经网络，它是一种更为灵巧、复杂的生物信息处理 系统。 n 每一个生物神经网络系统均是一个有多层次、多单元的动态信 息处理系统； n 生物神经系统的功能不是单个神经元信息处理功能的简单叠加； n 神经元之间突触连接方式和连接强度的不同并且具有可塑性。

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230619011744236.png" alt="image-20230619011744236" style="zoom:50%;" />

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230619012045927.png" alt="image-20230619012045927" style="zoom:50%;" />

### 神经网络的类型

#### 前馈型网络

各神经元接受前一层的输入，并输出给下一层， 没有反馈。

#### 反馈型网络

所有节点都是计算单元，同时也可接受输入，并向 外界输出。它可画成一个无向图(图1)，其中每个连 接线都是双向的，也可画成图2形式、若总单元数为 n，则每一节点有n-1个输入和1个输出。

### 学习

通过向环境学习获取知识并改进自身性能是 ANN的一个重要特点。在一般情况下、性能的 改善是按某种预定的度量通过调节自身参数 (如权值)随时间逐步达到的



监督学习

自学习： 当外部环境发生变化时，经过一段时间的训练和感知，神经网络能够对给定 输入产生期望的输出。



无监督学习

非监督学习时不存在外部教师，学习系统**完全按照环境提供数据的某些统计规律**来调节自身参数或结构(这是一种 **自组织**过程)。以表示出外部输入的某种固有特性(如聚类 或某种统计上的分布特征)

自组织： 神经网络通过训练可以**自行调节**连接权值，使其具有可塑性，以逐步构建适应 于不同信息处理要求的神经网络。



### 生物与人工的区别

生物神经元：影响神经激活电位的因素很多、很复杂

人工神经元：对输入信号的响应过程十分简单，以对神经 元所有输入所求的加权和，作为非线性响应函数的输入， 即可得到神经元的输出结果。

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230619014038777.png" alt="image-20230619014038777" style="zoom:50%;" />

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230619014054101.png" alt="image-20230619014054101" style="zoom:50%;" />



## 第三章

### 感知器

感知器(Perceptron)是模拟人的视觉,接受环境信息．并由 神经冲动进行信息传递的神经网络。感知器分单层与多层， 它们是具有学习能力的神经网络。是第一个用算法来精确定 义神经网络，第一个具有自组织自学习能力的数学模型

整个学习和记忆过程，就是根据实际输出与希望输出之间 的不同调整参数W和θ，即调整截割平面的空间位置使 之不断移动，直到它能将两类模式恰当划分的过程。

若函数是线性可分的，感知器的学习过程在有限次 数迭代后可以收敛到正确的数值(指的是权值或权向量)。

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230619212709675.png" alt="image-20230619212709675" style="zoom:50%;" />

只要是单层网络， 不论用什么样的非线性函数其分类能力都一样，即只能解决线 性可分的问题。

采用非线性连续函数作为神经元节点的激活函数，可以 使区域边界线的基本线素变成曲线，

增强分类能力的唯一出路是采用多层网络，即在输入及输出层 之间加上隐层构成多层前馈网络



理论分析表明：具有**单隐层**的前馈网络可以映射所有的连续函数，只有学习不连续函数（如锯齿波等）时 ，才需要**两个隐层**。

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230620013202354.png" alt="image-20230620013202354" style="zoom:50%;" />

### RBF网络

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230620025109524.png" alt="image-20230620025109524" style="zoom:50%;" />



<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230620025207297.png" alt="image-20230620025207297" style="zoom:50%;" />

### BP网络的学习

对于较复杂的多层前馈网络，标准BP算法能否收敛 是无法预报知的。 

 网络训练进入局部极小还是全局最小与网络权 值的初始状态有关，而初始权值是随机确定的

#### 提升收敛速度

(1)加动量项 (2)对sigmoid函数说，反对称函数比不对称 函数更好 (6)每一周期的训练样本输入顺序都要随机排序

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230620031101892.png" alt="image-20230620031101892" style="zoom:50%;" />

#### 避免局部极小点的全局优化算法

##### 随机梯度法

随机梯度法是对目标函数加噪声扰动



##### 模拟退火

跳出局部最小



##### 遗传算法

遗传算法(GA)是模拟上述生物的遗传和长期进 化过程建立起来的一种搜索和优化算法．它模 拟了生物界”生存竞争，优胜劣汰，适者生存” 的机制．用逐次迭代法搜索寻优。

选择：是从旧种群中 选择优质个体，淘汰部分个体，产生新种群的过程。个体的选择概率正比于其适应度

 GA的有效性，主要是选择和交叉操作 交叉后： （1）子代的基因链是父代的继承与重组； （2）子代中之一的适应度比父代双亲的都高。



GA的训练

适应度调整



约束问题：放在编码解码时排除、对不可行解降低适应度

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230620151432837.png" alt="image-20230620151432837" style="zoom:50%;" />



GA的改进（主要围绕着提高求得全局最优解的概率和 效率进行）

交叉、变异率的自适应调整、高级算子、静态繁殖、本地算子

并行GA

岛模型、近旁模型

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230620152400754.png" alt="image-20230620152400754" style="zoom:50%;" />

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230620152410692.png" alt="image-20230620152410692" style="zoom:50%;" />

### GA与神经网络的结合

(1) 由GA进行神经网络拓扑结构的优化设计； (2) 在网络结构固定的前提下，由GA进行网络权系 的训练，优化其权系值

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230620152830604.png" alt="image-20230620152830604" style="zoom:50%;" />

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230620152840611.png" alt="image-20230620152840611" style="zoom:50%;" />

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230620152849350.png" alt="image-20230620152849350" style="zoom:50%;" />

### 进化计算

二元进化策略：只有变异和选择两个自然进化过程被考虑， 自然进化过程被大大简化。

多元进化策略：每个群体由多个个体组成。个体数的增加是对生 物群体进化过程的更好模拟

进化计算与神经网络作为计算智能的两大分支经过融合 之后产生了一种全新的神经网络模型-进化神经网络。 l 这种模型把进化计算的进化自适应机制与神经网络的学习 计算机机制有机结合在一起，有效地克服了传统人工神经 网络的几乎所有缺点，是一种很有发展前途新模型。

进化神经网络模型的一个主要特点就是它对动态环境 的自适应性。这种自适应性过程通过进化的三个等级 实现，即连接权值、网络结构和学习规则的进化，他 们以不同的时间尺度进化，在自适应中也起着不同的 作用。

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230620155939068.png" alt="image-20230620155939068" style="zoom:50%;" />

## 第四章

深度神经网络

神经网络隐含层数越多，越能学习到输入数据的高层隐含特征

### 小样本学习

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230620163639650.png" alt="image-20230620163639650" style="zoom:67%;" />

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230620165230104.png" alt="image-20230620165230104" style="zoom:50%;" />

## 第五章 

反馈式神经网络

采用静态神经网络建模不能准确描述系统的动态性能

它用与阶层型神经网络不同的结构特征和学习 方法，模拟生物神经网络的记忆机理，获得了 令人满意的结果

### 离散型Hopfield网络

工作原理：对网络给定初始输入x时，网络就处于特定的初始状态，由此初始状态开始运行，可以得到网络输出即 网络的下一状态；

然后，这个输出状态通过反馈回送到网络的输入端， 作为网络下一阶段运行的输入信号，而这个输入信号可能与初始输入信号不同，由这个新的输入又可得到下步的输出，这个输出也可能与上一步的输出不同；

**Hopfield网络的各个神经元都是相互连接的**，即每一个神经元都**将自己的输出通过连接权传送给所有其它神经元**，同时每个神经元**又都接收所有其它神经元传递过来的信息**

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230620174155694.png" alt="image-20230620174155694" style="zoom:50%;" />

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230620174204576.png" alt="image-20230620174204576" style="zoom:50%;" />

当更新进行到一定程度之后，我们会发现无论再怎样更新下去，网络各 神经元的输出状态不再改变，这就是Hopfield网络的稳定状态

当网络的状态随时间发生变化时，网络能量沿其减小的方向变化，最后落入能量的极小点。一旦能量落入某个极小点之后，按Hopfield工作运行规则，网络能量函数将会“冻结”在那里。也就是说网络不见得一定收敛到全局的最小点，这是Hopfield网络的 一个很大缺陷

### 联想记忆

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230620175733208.png" alt="image-20230620175733208" style="zoom:50%;" />

### Hopfield网络的学习

Hebb学习：当某一突触(连接)两端的神经元同步激活 (同为激活或同为抑制)时，该连接的强度应增强，反之应减弱

### 缺点

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230620191351838.png" alt="image-20230620191351838" style="zoom:50%;" />

Hopfield网络的存贮能力决定于由ωij和θi 的适当组合而能够形成网络能量函数稳定平衡点的个数

一个具有N个神经元的Hopfield网络，信息存贮容量的上限值为0.15N， 当超过这个上限后，记忆错误将明显增多

### 连续时间型Hopfield神经网络

连续时间型Hopfield神经网络是以**模拟量**作为网络的输入、输出量，各神经元采用**同步工作**方式，因而它比离散型网络在信息处理的 并行性、联想性、存贮分布性、实时性、协同性等方 面更接近于生物神经网络。

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230620200245681.png" alt="image-20230620200245681" style="zoom:50%;" />

### 人工神经网络在三个主要方面的应用

模式识别与分类

联想记忆 

最优化

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230620200836854.png" alt="image-20230620200836854" style="zoom:50%;" />

可以发现:这三方面的应用实际上都是在利用神经网络能 量的收敛特性的基础上得以实现的，只不过利用的角度不 同而已



## 第六章

随机型神经网络：跳出局部极值点

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230620201307494.png" alt="image-20230620201307494" style="zoom:50%;" />

解决网络收敛问题的途径就只能从第二点入手，即不但让网络的误差或能量函数向减小的方向变化，而且，还可按某种方式向增大的方向变化，目的是使网络有可能跳出局部极小值而向全局最小点收敛。这就是**随机型神经网络算法的基本思想**

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230620202820412.png" alt="image-20230620202820412" style="zoom:50%;" />

温度高时，更加活跃，有能力跳出极小值点



### 模拟退火

先用高温将其加热熔化，使其中的粒子可以自由运动；逐渐降低温度，粒子的自由运动趋势也逐渐减弱，并逐渐形成低能态晶格。若在凝结点附近温度下降的速度足够慢，则金属 或固体物质一定会形成最低能量的基态，即最稳定结构状态。

且更新次数N足够大以 后，网络某状态出现的概率将服从玻尔兹曼分布

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230621005053118.png" alt="image-20230621005053118" style="zoom:50%;" />

Boltzmann机网络一般把整个神经元分为可视层与隐含层两 大部分，可视层又可分为输入部分和输出部分。

但它与一般的阶层网络结构不同之处是网络没有明显的层次界限，且神经元之间不是单向连接而是**双向连接**的



Boltzmann机网络工作规则与Hopfield网络工作规则十分相似， 只是以**概率方式取代阶跃函数**方式来决定网络根据其神经元 的内部状态而进行的状态更新，并且**网络的温度**参数随着网络状态更新的进行而逐渐减小。实际上，可以说Boltzmann机网络工作规则就是**模拟退火算法**的具体体现。

H是内部状态

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230621005332653.png" alt="image-20230621005332653" style="zoom:50%;" />



<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230621005405425.png" alt="image-20230621005405425" style="zoom:50%;" />





由于Boltzmann机网络的工作规则可使网络的状态转移， 无论从任何初始状态出发，**都可以收敛到网络能量函数 的最小值**，能量函数的各个局部极小值无法被利用来作 为记忆模式的存贮点。所以Boltzmann机网络不能充当一 般意义上的多记忆模式的联想记忆器使用



Boltzmann机网络除了可以解决**优化组合问题**外，还可以通过网络训练模拟外界给出的概率分布， Boltzmann网络训练模拟外界给出的概率分布，实现概率意义上的**联想记忆**。

38页



## 第七章

自组织神经网络

自组织神经网络的**无导师学习**方式更类似于人类大脑中生物神 经网络的学习



### 竞争型神经网络

是一种以无教师示教方式（无监督学习、 Unsupervised learning）进行网络训练的网络。网络通过自身训练，自动对输入模式进行分类，这一点 与Hopfield网络的模式分类功能十分相似

**网络结构**:  既不象阶层型网络那样各层神经元之间只有单向连接，也不 象全连接型网络那样网络结构上没有明显的层次界限。一般由输入层和竞争层构成的两层网络。两层之间各 神经元实现双向全连接，而且网络中没有隐含层。 有时竞争层各神经元之间还存在横向连接



网络竞争层各神经元**竞争对输入模式的响应机会**，最 后仅一个神经元成为竞争的胜者，并将与获胜神经元 有关的各连接权朝着更有利于它竞争的方向调整。 这一获胜的神经元则表示**对输入模式的分类**。

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230621012625019.png" alt="image-20230621012625019" style="zoom:50%;" />

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230621012145005.png" alt="image-20230621012145005" style="zoom:50%;" />

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230621012511233.png" alt="image-20230621012511233" style="zoom:50%;" />

### 抑制型神经网络

这一算法与基本竞争型神经网络的算法的主要区别是 某个竞争层神经元的输入值大于其它所有神经元的输 入值时，并不象基本竞争型学习规则那样，将其自身 的输出状态置为1，将其它所有神经元的输出状态置为 0，而是**保持其本身的输出值不变，将其它所有神经 元的输出值靠抑制作用逐渐减小**。这样，竞争层各 神经元的输出就形成连续变化的模拟值。

这种学习方式更接近生物神经系统的记忆动力 学过程,从而使得网络的非线性记忆性能更加优越。 为用模拟电路实现网络提供了可能性。



### 自适应共振理论网络

网络分输入／输出两层，一般根据各层所具 有的功能特征还称输入层为比较层，输出层为识别层。

网络不但有从输入层至输出层的前馈连接权，还有从输出层 至输入层的反馈连接权。

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230621014104724.png" alt="image-20230621014104724" style="zoom:50%;" />

ART1网络的学习及工作过程： 

通过反复地将输入学习模式由输入层向输出层自下而上地识 别和由输出层向输入层自上而下的比较过程来实现的。 

当这种自下而上的识别和自上而下的比较达到共振，即输出 向量可以正确反映输入学习模式的分类，且网络原有记忆没 有受到不良影响时，网络对一个输入学习模式的记忆和分类 则告完成



初始化阶段：按照特定模式

识别阶段

比较阶段：将当前模式与已经学习过的模式进行比对

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230621014507257.png" alt="image-20230621014507257" style="zoom:50%;" />

寻找阶段：找一个输出向量中未曾使用过的单元表示新的模式

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230621014708639.png" alt="image-20230621014708639" style="zoom:50%;" />



### 自组织特征映射神经网络

自组织特征映射(Self-Organizing Feature Map)神 经网络(简称SOM网络)方案。由输入层和竞争 层组成

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230621015002141.png" alt="image-20230621015002141" style="zoom:50%;" />

它不是以一个神经元或者一个神经元向量来反映分类结果， 而是以**若干神经元同时反映分类结果**。与这若干神经元相连 接的连接权向量虽略有差别，但这些神经元的分类作用基本 上是并列的，即其中任何一个神经元都可以代表分类结果或 近似分类结果

另外，这种网络之所以被称为特征映射网络，是因 为网络对输入学习模式的记忆不是一次性完 成的，而是通过反复学习

###  对向传播神经网络

网络结构如图所示。网络分输入、竞争、输出三层。 l

输入层与竞争层构成SOM网络，竞争与输出层构成基本竞争 型网络。

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230621015224532.png" alt="image-20230621015224532" style="zoom:50%;" />



## 第八章

### 脉冲神经网络

被誉为第 三代人工神经网络。实现了更高级的生物神经模拟水平。其模 拟神经元更加接近实际，除了神经元和突触状态之外，它把时 间信息的影响也考虑其中

脉冲神经元（ Spiking Neuron ）在某个特定的时间点产生一个脉冲 ，然后通过神经元的轴突传递到下一个神经元。脉冲的大小和形状与神 经元的输入无关，但是神经元产生脉冲的时间依赖于神经元的输入

非常适合大脑神经信号的处理，是进行复杂 时空信号处理的有效工具。

第一代：感知机 第二代：各种BP网络

由于**脉冲神经网络传递的是一个个脉冲**，它们组成了 一个脉冲**序列**，单个脉冲之间的时间间隔不一定，脉 冲序列中蕴含了**temporal information**，这是传统的人工 神经网络所不能表达的（处理复杂时空信息）

<img src="C:\Users\ChenxiCui\AppData\Roaming\Typora\typora-user-images\image-20230621015701386.png" alt="image-20230621015701386" style="zoom:50%;" />

