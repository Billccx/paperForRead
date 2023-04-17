## Spring项目结构

<img src="D:\paper\paperForRead\images\backend\spring.png" style="zoom:67%;" />

1.首先一个spring boot项目必须得有一个启动类（OnlineXdclassApplication），这个类的作用是标识这是一个spring boot项目，整个项目也是通过这个类集起来，spring boot容器启动后可以根据配置的信息扫描整个项目。为了方面容器扫描，一般启动类的位置在包名下一级目录。

2.resources目录下存放静态资源，比如xml文件，图片等，其中值得一提的是application.properties,这是项目的配置文件，可在其中配置端口号以及连接数据库的基本信息（也可选择新建.yml文件和.properties的作用一样，只不过在编写格式上稍作区别）。

3.pom.xml文件时整个项目添加依赖的文件，可以在pom.xml里添加需要的依赖，也可以在其中设置仓库镜像（一般默认依赖下载源为国外网站，可修改为国内镜像，提高下载速率，国内镜像地址推荐：http://maven.aliyun.com/nexus/content/repositories/central/）

4.最后一个文件也是整个项目的核心也就是实现具体业务逻辑的代码存放文件，位于包名一级目录下，一般根据业务逻辑可建立如下几个包：==**model（entity）**==(存放实体类以及自定义返回类型类，可以再一次划分问entity包以及request包)，**==mapper==**（作用于持久化层，和数据库打交道，根据业务逻辑建立相应的类），**==controller==**(作用于web层，通过访问相应的api接口调相应的实现具体业务的方法)，**==service==**(具体的逻辑代码实现层，连接mapper以及controller的中间层，一般建立相应的service接口以及impl实现类)，**==Utils==**(这是一个工具包，作用于全局的工具类可以建立在这个包中，一般建立本地缓存guava,MD5加密，自定义返回类，JWTS工具类等)，Interceptor(顾名思义这是一个拦截器的实现类，可以在此处实现逻辑拦截)，Config(配置类，拦截器的配置可以在此处实现，也可以添加一些特定类的配置)，Exception（自定义异常类，可以在此处自定义异常）