# BTL
```bledner BLT 插件```
## 1.需求
### 需求1. blender 插件的目录规范
由于Blender 的插件是由Python 实现的,大致分为以下几个阶段
```
\
 |
 | Blender 插件注册前
 |
 _   
 |
 | Blender 插件注册
 |
/ 
```
所以在Blender 插件注册前的阶段进行兼容性检测处理.
根据计算机分层的思想对其进行层级的划分
```
+----------------------+
|       OS   检查       |
+----------------------+
|      Python 检查      |
+----------------------+
| Blender Base API 检查 | <----- 仅保证插件的UI、部分功能正常
|                      |    
+----------------------+ <----- 如果发生异常则需要手工适配，因为如bpy.app这样的模块被更改时很可能意味重大功能更新
| Blender Core API 检查 |
+----------------------+ <----- 获取Core兼容patch
| bledner Extra API 检查| <----- 可选 比如提供不受支持的内部API
+----------------------+ <----- 获取Extra兼容性patch
|       兼容性调整       | <----- 等价API替换
+----------------------+
```
通过设计，将其版本更新的API改动局限在compatible模块中,避免改动过多
首先在实现创建compatible模块
```bledner
OS层的检查由compatibleb的os_probe模块执行
检查当前运行的系统是否为'linux' 'darwin' 'win32'
不提供其他系统(unix、AIX)或以奇怪方式运行起来的blender(wine，你跑起来算你赢)
提供以下API

    get_platform()
        返回OS类型 'linux' 'darwin' 'win32'
    
    get_current_os_user()
        返回当前登录系统的用户
    
    get_platform_tmp_dir()
        返回平台推荐的临时目录
```


## 2.设计
## 3.实现