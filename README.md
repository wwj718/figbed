# figbed 
figbed is an easy to use fig bed when you writing with markdown

inspired by [cut](https://github.com/xiaochao/cut)

目前**只支持mac**下使用 ,其他操作系统请看文末

---

# 介绍
自动截图并上传到七牛的脚本

###依赖安装
* 安装[pngpaste](https://github.com/jcsalterego/pngpaste)
    * mac下: brew install pngpaste
* pip install figbed

### 使用方法
1. 登陆七牛，如果你没有七牛账号，请注册
2. 在账号设置页面，找到密钥标签，获取到AK和SK
3. 新建一个空间，在空间设置页面，获取到您的域名,和空间对于的域名

![figbed](http://oav6fgfj1.bkt.clouddn.com/figbed_md1.png)

上边这张截图就是采用fidbed处理的

4. 新建`cat ~/.qiniu.yml`,形如

```yml
AK: xxx
SK: xxx
YOUR_DOAMIN: http://oav6fgfj1.bkt.clouddn.com
YOUR_BUCKET: wwj-fig-bed
PATH_SAVEAS: /tmp
```

其中AK,SK,YOUR_DOAMIN,YOUR_BUCKET已在上边介绍过了，PATH_SAVEAS是图片将要保存的本地路径（默认为/tmp），建议保存到文章同属的git库里，做个备份

* 启动图床服务：figbed
* 选择截图工具开始截图，如QQ(我在用`jietu`)，只要这个截图工具截完图把图片放到剪切板就可以。
* 截图完成后，使用command+v即可以获取到url

### 注意
* 目前只支持上传到七牛
* 有时候command+v无法获取到url，那么请等一会，具体取决于您的网速
* 目前在mac测试通过，理论上可以运行pngpaste系统都可以




# 其他操作系统
### windows
(在windows下可以尝试直接调用截图库,如QQ截图：CameraDll.dll: `dll = ctypes.cdll.LoadLibrary('CameraDll.dll')`
