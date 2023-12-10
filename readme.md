# CUR_INF_create

Windows10的鼠标个性化安装文件 `.inf` 自动生成python3脚本，用于减少重复的机械性操作



## 描述

含有两个脚本 `CUR_inf_create.py` 和 `CUR_inf_auto.py`

- 如果运行 `CUR_inf_auto.py` 会生成 `Install.inf` 并询问是否自动安装，若按下Y或者直接回车而选择了确认，会直接执行cmd命令来安装inf
- 如果运行 `CUR_inf_create.py` 会生成 `Install.inf` ，跳过询问



## 注意1

由于执行的安装命令是：`rundll32 syssetup,SetupInfObjectInstallAction DefaultInstall 128 ./Install.inf` 可能只在**部分Windows版本**可以使用



## 注意2

脚本同级目录中 `.cur` 或 `.ani` 有一共**15**个，且默认**排序**（按文件名称递增）后需要遵循如下顺序：

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

本脚本使用一组光标（【宝鐘マリン】）来作为测试，使用时请遵循 `宝鐘マリンマウスカーソル/readme(はじめにお読みください).txt` 文件上声明

![宝鐘マリン](./img/宝鐘マリン.jpg)
