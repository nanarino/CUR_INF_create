# CUR-INF-create

鼠标个性化安装文件`.inf`自动生成脚本

含有两个脚本`CUR_inf_create.py`和`CUR_inf_auto.py`



- 如果运行`CUR_inf_create.py`会生成`Install.inf`并直接提示：

  Click on the file Install.inf right mouse button, the shortcut menu to choose - to install；

- 如果运行`CUR_inf_auto.py`会生成`Install.inf`生成结束后会询问是否自动安装，

  若按下Y或者直接回车而选择了确认，会直接执行cmd命令来安装inf



## 注意1

由于执行的安装命令是：`rundll32 syssetup,SetupInfObjectInstallAction DefaultInstall 128 ./Install.inf`可能只在**Windows7**版本可以使用



## 注意2

使用时必须保证`.cur`或`.ani`有一共**15**个，按文件名称**排序**后需要遵循如下顺序：

1. 正常选择
2. 帮助选择
3. 后台运行
4. 忙
5. 精确定位
6. 选定文本
7. 手写
8. 不可用
9. 垂直调整
10. 水平调整
11. 沿对角线调整1
12. 沿对角线调整2
13. 移动
14. 候选
15. 链接选择



## 注意3

~~DD专用一键导入~~

本脚本使用虚拟Youtuber【宝鐘マリン】的鼠标光标 来作为测试，

使用时请遵循`宝鐘マリンマウスカーソル/readme(はじめにお読みください).txt`文件上声明，

其他包括但不限于ホロライブ所属的虚拟形象的光标也可以通过其作者获得。