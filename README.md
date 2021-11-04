# BuaaAutoDaka

北航疫情填报小程序自动打卡脚本
打你大爷的卡

## 使用

### 环境安装

```
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 配置相关

需要修改的只有config中的users部分，如果给多个人打卡，加到列表就行，

默认日志存放在/log/daka.log

打卡时间默认每日17点10分，在daka.py主函数中修改

### 使用

linux后台运行

```
nohup python daka.py &
```

windows的可以写一个服务开机自启