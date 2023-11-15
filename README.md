本仓库是 Fluid 项目组官方创建，用于 [Fluid 主题](https://github.com/fluid-dev/hexo-theme-fluid)展示以及发布一些 Hexo 与主题相关的文章。

如果你有相关文章想投稿，可以通过 [Pull Request](https://github.com/fluid-dev/hexo-fluid-blog/pulls) 方式提交（文中图片可暂时使用自己的外链或存放在 source 里），不要忘记文章头部留下自己的原文链接（[格式参考](https://raw.githubusercontent.com/fluid-dev/hexo-fluid-blog/master/source/_posts/hexo-darkmode.md)）。


# 如何使用
## 1. 更新themes下的git子模块
当使用git clone下来的工程中带有submodule时，初始的时候，submodule的内容并不会自动下载下来的，此时，只需执行如下命令：
```bash

git submodule init
git submodule update

或：
git submodule update --init --recursive

```

## 安装pandoc
windows
```powershell

choco install -y pandoc

```

linux
```bash



```
## 修改 package.json, 将hexo的版本改到7.0以下，

```json

{
  "name": "hexo-fluid-blog",
  "version": "0.0.0",
  "private": true,
  "scripts": {
    "build": "hexo generate",
    "clean": "hexo clean",
    "deploy": "hexo deploy",
    "server": "hexo server"
  },
  "hexo": {
    "version": "6.3.0"
  },
  "dependencies": {
    "hexo": "^6.1.0",
    "hexo-filter-nofollow": "^2.0.2",
    "hexo-generator-archive": "^1.0.0",
    "hexo-generator-category": "^1.0.0",
    "hexo-generator-index": "^2.0.0",
    "hexo-generator-sitemap": "^2.0.0",
    "hexo-generator-tag": "^1.0.0",
    "hexo-memorial-day": "^0.3.0",
    "hexo-renderer-ejs": "^1.0.0",
    "hexo-renderer-pandoc": "^0.3.0",
    "hexo-renderer-stylus": "^1.1.0",
    "hexo-server": "^2.0.0",
    "hexo-tag-echarts": "^1.0.0"
  }
}

```
## 安装node模块

```bash

npm install


```

## 启动

```bash

hexo clean -- hexo c
hexo generate -- hexo g
hexo server -- hexo s or hexo s -p 5555

```
## 部署
### 安装插件
```bash
# 安装部署到github的插件
npm i --save hexo-deployer-git
```

### 修改配置文件 _config.yml
```json

# Deployment
## Docs: https://hexo.io/docs/deployment.html
# deploy:
#   - type: baidu_url_submitter
# 参考： https://www.bilibili.com/video/BV1Yb411a7ty/?spm_id_from=333.788.recommend_more_video.2&vd_source=6cecd1f17a6c0ef08a944dd92199a516
deploy:
  type: git
  repo: git@github.com:lgf4591/lgf4591.github.io.git
  branch: main


```

### 执行部署到 github pages
```bash
# hexo deploy -- hexo d

hexo clean
hexo g
hexo d

```


# git submodule添加、更新和删除
## 添加[#](https://www.cnblogs.com/jyroy/p/14367776.html#idx_0)

```
Copygit submodule add <url> <path>

```

-   url：替换为自己要引入的子模块仓库地址
-   path：要存放的本地路径

执行添加命令成功后，可以在当前路径中看到一个.gitsubmodule文件，里面的内容就是我们刚刚add的内容

如果在添加子模块的时候想要指定分支，可以利用 -b 参数

```
Copygit submodule add -b <branch> <url> <path>

```

## 例子[#](https://www.cnblogs.com/jyroy/p/14367776.html#idx_1)

### 未指定分支[#](https://www.cnblogs.com/jyroy/p/14367776.html#idx_2)

```
Copygit submodule add https://github.com/tensorflow/benchmarks.git 3rdparty/benchmarks

```

.gitsubmodule内容

```
Copy[submodule "3rdparty/benchmarks"]
path = 3rdparty/benchmarks
url = https://github.com/tensorflow/benchmarks.git

```

### 指定分支[#](https://www.cnblogs.com/jyroy/p/14367776.html#idx_3)

```
Copygit submodule add -b cnn_tf_v1.10_compatible https://github.com/tensorflow/benchmarks.git 3rdparty/benchmarks

```

.gitsubmodule内容

```
Copy[submodule "3rdparty/benchmarks"]
path = 3rdparty/benchmarks
url = https://github.com/tensorflow/benchmarks.git
branch = cnn_tf_v1.10_compatible

```

## 使用[#](https://www.cnblogs.com/jyroy/p/14367776.html#idx_4)

当我们add子模块之后，会发现文件夹下没有任何内容。这个时候我们需要再执行下面的指令添加源码。

```
Copygit submodule update --init --recursive

```

这个命令是下面两条命令的合并版本

```
Copygit submodule init
git submodule update

```

## 更新[#](https://www.cnblogs.com/jyroy/p/14367776.html#idx_5)

我们引入了别人的仓库之后，如果该仓库作者进行了更新，我们需要手动进行更新。即进入子模块后，执行

```
Copygit pull

```

进行更新。

## 删除[#](https://www.cnblogs.com/jyroy/p/14367776.html#idx_6)

1.  删除子模块目录及源码

```
Copyrm -rf 子模块目录

```

2.  删除.gitmodules中的对应子模块内容

```
Copyvi .gitmodules

```

3.  删除.git/config配置中的对应子模块内容

```
Copyvi .git/config

```

4.  删除.git/modules/下对应子模块目录

```
Copyrm -rf .git/modules/子模块目录

```

5.  删除git索引中的对应子模块

```
Copygit rm --cached 子模块目录

```
