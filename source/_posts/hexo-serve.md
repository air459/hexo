---
title: 把 hexo 部署在 Github Pages 中
date: 2026-02-22 21:40
tags: [hexo, github]
---

# 环境准备
## nodejs

下载链接: [https://nodejs.org/zh-cn/download](https://nodejs.org/zh-cn/download)

### linux
划到最下方选择`linux`和架构下载`tzr.gz`压缩文件
```bash
$ tar -xvf node.tar.gz
$ sudo mv node /opt/
```
在文件.bashrc中添加
```bash
export $PATH="/opt/node/bin:$PATH"
```
```bash
$ source .bashrc
```

### window
划到最下方选择`window`和架构下载`msl`文件
运行`msl`安装完成

## npm
`npm`默认使用的镜像是国外的
所以需要切换镜像，除非你有代理
你可以进入[cnpm官网](https://npmmirror.com/)来查看各种方法来使用这个镜像
我一般都是直接修改镜像
```bash
$ npm config set registry https://registry.npmmirror.com
```

## hexo
安装`hexo`
```bash
$ npm i -g hexo
```

## git
### ubuntu/debian
```bash
$ sudo apt install git
```

### window
下载链接: [https://git-scm.cn/install/window](https://git-scm.cn/install/window)
选择跟系统架构相同的下载`独立`安装程序`exe`
安装时记得勾选`Use bundled Openssh`

# 创建项目
window 推荐使用 `PowerShell`
```bash
$ hexo init hexo #创建hexo项目
$ cd hexo
$ npm i
```

文章路径 `source/_posts`
- 创建文章可以在文章目录创建md文件
- 还有一种使用 `hexo new 文章名` 就会在文章路径创建md文件
这两种方法都一样，没有区别

## 运行
```bash
$ hexo g #生成静态文件
$ hexo s #运行服务 ctrl+c停止
```

# Github Pages 部署

## ssh配置
```bash
$ ssh-keygen -t rsa -b 4096 -C "的邮箱"
# ssh密钥名称是随机的
$ cat %USERPROFILE%\.ssh\id_xx.pud #window的
$ cat ~/.ssh/id_xx.pub #linux的
# 复制命令的输出
```

打开[github](https://github.com)注册/登陆
创建仓库 复制仓库链接https://hexo.io/themes/
+ -> New repository -> Repository name填仓库名称 -> Create repository(绿色按钮)
创建好仓库就先摆这
在github主页点击你的头像
settings -> SSH and GPS keys -> New SSH keys -> Title随便填 -> Key 剪贴你复制

设置好运行: 
```bash
$ ssh -T git@github.com
```

输入yes
如果输出有你的用户名，就是key配置成功

## hexo 配置
进入项目修改_config.yml

### 了解
`title`网站标题
`author`作者
`language`语言 中文填 `zh-CN`
`url`填域名 `https://xx.xx`
`theme`主题

### 需要修改的
`title` 改成你想要的标题
`author`修改成你的名字
`url`填你的域名
在`deploy`字典中
`type`填 `git`
`repository`填 `git@github.com:github用户名/仓库名.git`
`branch`填`main`
`message`填个git提交信息 这个可要可不要
实例: 
```yml
title: KongQi Blog
...
author: KongQi
languagep: zh-CN
...
url: https://kongqi-air.top
...
deploy:
  type: git
  repository: git@github.com:air459/hexo.git
  branch: main
  message: "aaaaaa"
```

## 提交
```bash
$ npm i --save hexo-deployer-git
$ hexo g
$ hexo d #提交
```

以后你在次提交只要运行
```bash
$ hexo g
$ hexo d
```

## 域名
### DNS记录
|类型|名称|目标|
|:---|:---|:---|
|CNAME|@|用户名.github.com|

@可以替换子域名

### github
进入你刚才创建的新仓库
settings -> Pages -> branch设置成main / -> Custom domain -> 你的域名 -> save
等待github检查域名
域名绑定成功

# 进阶

## 主题配置

### 怎么查找主题
- 网络搜索
- [hexo themes](https://hexo.io/themes/)

### 安装主题
在[hexo themes](https://hexo.io/themes/) 网站查找你看得上的主题
点击标题

每个主题的安装方法都有点不同
一般都是
下载主题到`themes` 文件夹中
然后在`_config.yml`文件中找到`theme`: 后面跟上你主题文件夹名称

## 评论
我以`utteranc`为主
安装[点我](https://github.com/apps/utterances) —> install -> 授权
进入[utteranc.es](https://utteranc.es/)
找到`repo`填写你 `用户名/仓库名`
其他保持默认
`Theme`这个可以修改评论的主题
复制`Enable Utterances里面的script标签`
把`script`标签放在`md文档`的最后面

<script src="https://utteranc.es/client.js"
        repo="air459/hexo"
        issue-term="pathname"
        label="评论"
        theme="github-dark"
        crossorigin="anonymous"
        async>
</script>
