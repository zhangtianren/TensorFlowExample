# TensorFlowExample
用于一些tensorflow训练的基础试验


---
### 1 安装tensorflow 的运行环境
 （这里选择了较为简单快捷的环境 linux + virtualEnv）

 * （1）装一些工具 ` $ sudo apt-get install python-pip python-dev python-virtualenv` 
 * （2）新建一个名字叫tensflow的virtualEnv ` $ virtualenv --system-site-packages ~/tensorflow` 
 * （3）激活并进入这个virtualEnv里 
     ` $ cd ~/tensflow` 
     ` $ source bin/activate` 
 * （4）在这个virtualEnv内安装tensflow (事先下载好这个.whl的文件)
      ` (tensorflow)$ pip install --upgrade http://192.168.118.39:8080/tensorflow-0.8.0-cp27-none-linux_x86_64.whl` 
      
 * （5）ok了，验证一下：运行一个有import tensflow的python脚本看看
 
     ![hello的python脚本,图未见](/image/hello_python.jpg "hello的python脚本") 
     
     ![hello的输出,图未见](/image/hello_output.jpg "hello的输出")
     
 *  （6）关闭virtualEnv ` (tensorflow)$ deactive `
