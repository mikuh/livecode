# livecode
二维码活码裂变

支持python3+

依赖： aiohttp、qrcode、yaml

## 使用方法：

1.将项目`clone` 到本地

2.设置自己的配置文件

[livecode](https://github.com/mikuh/livecode)/[livecode](https://github.com/mikuh/livecode/tree/master/livecode)/[configs](https://github.com/mikuh/livecode/tree/master/livecode/configs)/**base.yaml** 

3.初始化数据库：
在init目录下执行
```
python init_db.py
```
可以调用其中的`insert_user()`函数往数据库插入新用户。

4.启动服务

```
python service.py
```

