---
title: GitHub Actions 来自动部署 Hexo
date: 2020-04-22 22:22:22
index_img: https://fluid.s3.bitiful.net/hello-fluid/cover.png?w=480&fmt=webp
category: 编程
tags:
  - 编程
  - GitHub Actions
  - Hexo
math: true
mermaid: true
sticky: 100
---

## 背景

最近发现了一个好东西：[GitHub Actions](https://link.zhihu.com/?target=https%3A//github.com/features/actions)，GitHub 提供的自动集成（[Continuous Integration](https://link.zhihu.com/?target=https%3A//en.wikipedia.org/wiki/Continuous_integration)）工具，从此以后可以跟 [Travis CI](https://link.zhihu.com/?target=https%3A//travis-ci.org/) 说拜拜了。

为什么会发现 GitHub Actions 这个东西呢，主要是我的路由器装了 [OpenWrt](https://link.zhihu.com/?target=https%3A//openwrt.org/)，有几个想用的插件没有 MIPS 架构的包，只能自己编译。

而我电脑的性能几乎（其实是根本 ）无法编译 OpenWrt 这么庞大的代码，本来想说买个云服务器编译一下，结果就发现了 GitHub Actions 这么个好东西。

当然今天主要不是介绍如何使用 GitHub Actions 来编译 OpenWrt，而是介绍下如何用它来自动部署基于 Hexo 的 Blog。

建议大家先看一下 [GitHub Actions](https://link.zhihu.com/?target=https%3A//github.com/features/actions) 官方的介绍，不然对于下面的内容可能没有办法很好的理解。

首先我们先要在本地确保 Hexo 是可以正确运行的，比如：

```
$ hexo clean
$ hexo deploy
```

至于如何设置和使用 Hexo，请参考 [https://hexo.io/](https://link.zhihu.com/?target=https%3A//hexo.io/)

此外我的 Hexo 同时部署在 GitHub Pages 和自己的服务器上，考虑大家的使用场景，我这里只介绍 GitHub Pages 相关的设置。

至于如何使用 GitHub Pages 部署自己的网站，请参考：[https://pages.github.com/](https://link.zhihu.com/?target=https%3A//pages.github.com/)

确认 `_config.yml` 文件中有类似如下的 `GitHub Pages` 配置：

```
deploy:
  type: git
  repository: git@github.com:TommyLau/Demo.git
  branch: master
```

> 注意：请将 `repository` 修改为你自己的仓库地址。

## 生成秘钥

如果你的 Hexo 可以正常地部署到 GitHub，那么实际上你原来的秘钥是可以正常使用的。

但是我的私钥还用于不同的服务器的 SSH 访问和其他身份验证，因此，我们生成一个新的秘钥对来专门部署 Hexo。

以下为 macOS 下的操作，Linux 下操作方法相同，Windows 10 用户可以在市场中安装 Ubuntu 以后执行：

```
ssh-keygen -t rsa -b 4096 -C "Hexo Deploy Key" -f github-deploy-key -N ""
```

这会在当前目录生成两个文件：

-   github-deploy-key —— 私钥
-   github-deploy-key.pub —— 公钥

## GitHub 配置秘钥

我们把`私钥`放到我们存放 Hexo 原始文件的代码仓库里面，用于触发 Actions 时使用。

把`公钥`放到 GitHub Pages 对应的代码仓库里面，用于 Hexo 部署时的写入工作。

### 配置私钥

首先在 GitHub 上打开保存 Hexo 的仓库，访问 `Settings -> Secrets`，画面如下：

![](https://pic3.zhimg.com/v2-78fca9d3aecf4fef4cdbc759dd4d827e_b.jpg)

然后选择 `New secret`

![](https://pic1.zhimg.com/v2-9c37b4488b83579e01e58ef3b0f34fd8_b.jpg)

名字部分填写：`HEXO_DEPLOY_KEY`，注意大小写，这个后面的 GitHub Actions Workflow 要用到，一定不能写错。

在 `Value` 的部分填入 `github-deploy-key` 中的内容：

![](https://pic3.zhimg.com/v2-d963d2f26452fa39ec6b7187926a48de_b.jpg)

添加了私钥以后的界面显示如下：

![](https://pic4.zhimg.com/v2-e7990155f2bf12eecb521c3968379987_b.jpg)

### 添加公钥

接下来我们需要访问存放网页的仓库，也就是 Hexo 部署以后的仓库，比如：`yourname.github.io` 这种，访问 `Settings -> Deploy keys`：

![](https://pic1.zhimg.com/v2-f8d27de9af570b8a3bcb70ca0a4983fc_b.jpg)

按 `Add deploy key` 来添加一个新的公钥：

![](https://pic1.zhimg.com/v2-1f3873d498087fb7334dd49b16bc0d48_b.jpg)

在 `Title` 中输入：`HEXO_DEPLOY_PUB` 字样，当然也可以填写其它自定义的名字。

在 `Key` 中粘贴 `github-deploy-key.pub` 文件的内容。

> 注意：一定要勾选 `Allow write access` 来打开写权限，否则无法写入会导致部署失败。

![](https://pic3.zhimg.com/v2-247aaf40961d62979658d47abfb56686_b.jpg)

最后添加好了公钥的界面如下：

![](https://pic2.zhimg.com/v2-e85375698b274f6bc6b61d10c7609019_b.jpg)

## 创建 Workflow

首先在 Hexo 的仓库中创建一个新文件：`.github/workflows/deploy.yml`，文件名可以自己取，但是一定要放在 `.github/workflows` 目录中，文件的内容如下：

```
name: Hexo Deploy

on:
  push:
    branches:
      - master

jobs:
  build:
    runs-on: ubuntu-18.04
    if: github.event.repository.owner.id == github.event.sender.id

    steps:
      - name: Checkout source
        uses: actions/checkout@v2
        with:
          ref: master

      - name: Setup Node.js
        uses: actions/setup-node@v1
        with:
          node-version: '12'

      - name: Setup Hexo
        env:
          ACTION_DEPLOY_KEY: ${{ secrets.HEXO_DEPLOY_KEY }}
        run: |
          mkdir -p ~/.ssh/
          echo "$ACTION_DEPLOY_KEY" > ~/.ssh/id_rsa
          chmod 700 ~/.ssh
          chmod 600 ~/.ssh/id_rsa
          ssh-keyscan github.com >> ~/.ssh/known_hosts
          git config --global user.email "john@doe.com"
          git config --global user.name "John Doe"
          npm install hexo-cli -g
          npm install

      - name: Deploy
        run: |
          hexo clean
          hexo deploy
```

简单解释一下，当我们推送内容到远程 `master` 分支的时候，就会触发这个 Workflow。

使用 `Ubuntu 18.04` 作为 `hexo deploy` 的系统。

首先 checkout 源代码，然后设置使用最新的 Node.js v12 LTS 作为 node 解释器。

接下来就是创建 SSH 相关的配置文件，注意 `secrets.HEXO_DEPLOY_KEY` 就是对应我们之前设置的私钥，所以名字一定不要搞错。

`git config` 相关的名字和邮件地址替换成大家自己使用的就好了。

最后就是安装 Hexo CLI，各个依赖模块和部署了。

## 验证

下面就是 GitHub Actions 页面显示的运行结果：

![](https://pic1.zhimg.com/v2-3046f9fb7bae9e4c528574ecdd253778_b.jpg)

前面有绿色钩钩的，就表示部署成功，红色叉叉的表示失败。如果部署失败，还会收到 GitHub 的邮件提醒。

好了，以上就是利用 GitHub Actions 自动部署 Hexo 到 GitHub Pages 的方法，谢谢观赏。