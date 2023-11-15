---
title: Hexo+GitHub Actions搭建博客，实现云端写作、一键发布
date: 2023-11-15 12:29:35
index_img:
category: 编程
tags:
  - 编程
  - GitHub Actions
  - Hexo
math: true
mermaid: true
sticky: 100
---

携手创作，共同成长！这是我参与「掘金日新计划 · 8 月更文挑战」的第14天，[点击查看活动详情](https://juejin.cn/post/7123120819437322247 "https://juejin.cn/post/7123120819437322247")

> 操作环境：Windows10、Node、Git、ssh
> 
> 前置准备: `<username>github.io` 仓库已建立，预计托管博客网址为`<username>github.io/blog`（可以绑定个人域名）

先对hexo有个清晰的认识，不至于稀里糊涂的跟着步骤走。

## 1、Hexo发布博客流程概览

1.  搭建hexo环境
    
2.  `hexo new "title"` (创建新文章)
    
3.  编写md文档
    
4.  `hexo clean`
    

-   清除缓存文件 (db.json) 和已生成的静态文件 (public)

5.  `hexo generate` (生成静态文件)
    
6.  `hexo deploy` (Hexo 会将 public 目录中的文件和目录推送至 `_config.yml` 中指定的远端仓库和分支中，并且完全覆盖该分支下的已有内容。)
    
7.  本地仓库同步到GitHub (不同步的话，文章源码只会保留在本地，不易管理)
    

> 由于 Hexo 的部署默认使用分支 master，所以如果你同时正在使用 Git 管理你的站点目录，你应当注意你的部署分支应当不同于写作分支。
> 
> Hexo 在部署你的站点生成的文件时并不会更新你的站点目录。因此你应该手动提交并推送你的写作分支。

一般来说第一步环境搭建只需要在最开始创建博客网站的时候进行，写文的话只需要重复第2-7步就可以了，这种使用方式强烈依赖于本地环境。但是，有时候我们并不只是固定在一台电脑上写文，（比如：一直写文的电脑坏了，需要换新电脑；电脑重装系统等等）这样就需要在另一台电脑上搭建环境，这样非常的麻烦，而且难免会带来一些其它依赖版本兼容问题。所以，可以采用`GitHub Actions`持续集成平台来简化发布文章的流程。

简化后的流程如下：

1.  `hexo new "title"` (创建新文章)
    
2.  编写md文档
    
3.  本地仓库同步到GitHub
    

-   push到GitHub上之后，`GitHub Actions`会监听分支文件变动，触发发布流程（跟Jenkins 构建流程类似）

下文整体分为两个步骤：

1.  借助`GitHub Pages`手动部署。
    
2.  增加`GitHub Actions`配置，完成自动部署
    

## 2、Hexo 搭建博客

Hexo 是一个快速、简洁且高效的博客框架。Hexo 使用 Markdown（或其他渲染引擎）解析文章，在几秒内，即可利用靓丽的主题生成静态网页。

[文档](https://link.juejin.cn/?target=https%3A%2F%2Fhexo.io%2Fdocs%2F "https://hexo.io/docs/")

```
npm install -g hexo-cli
cd [workspace]
hexo init <folder:blog>
cd <folder:blog>
npm install
hexo s
```

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cf31d07d9bb4ecb8844aebb0f35e4fb~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)

网站基础配置修改参考[这里](https://link.juejin.cn/?target=https%3A%2F%2Fhexo.io%2Fdocs%2Fconfiguration "https://hexo.io/docs/configuration")

## 3、GitHub 托管 Hexo 博客

> 可以采取`分支管理`的方式，也可以新建repo，在ci配置上略有不同，这里我采用的是将`hexo`博客源码托管到`独立的repo上`，将 `Hexo` 项目编译生成静态页面，部署到 `gh-pages` 分支

1.  新建仓库：`blog` （名字自己起）
    
2.  本地hexo仓库关联远程GitHub仓库 将本地仓库推送到远端
    
3.  本地仓库一些必要的修改配置
    

-   安装 [hexo-deployer-git](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fhexojs%2Fhexo-deployer-git "https://github.com/hexojs/hexo-deployer-git")。

```
https://github.com/hexojs/hexo-deployer-git
```

-   修改`_config.yml`配置，如下：

```
url: https://all-smile.github.io/blog
root: /blog/

# ...

deploy:
  type: 'git'
  repo: git@github.com:all-smile/blog.git
  branch: gh-pages
```

-   提交到远程仓库

3.  创建 `gh-pages` 分支

hexo结合GitHub创建个人网站指定的分支名，hexo 内默认设置的分支也是叫这个名字

```
git checkout -b gh-pages
git push -u origin gh-pages
```

4.  远程仓库开启 github pages

指定部署分支：gh-pages

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05e6946151324a009154f110112f2897~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)

## 4、手动部署

本地项目执行命令：

```
hexo clean
hexo g
hexo deploy
```

hexo模板引擎生成静态文件，并推送到`gh-pages`分支下（替换原先分支下的所有文件）

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6feea9e984a94454888b7d9abf1821d0~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)

到这里就已经完成了博客的搭建

> 需要注意的是：`hexo deploy` 命令并不会帮助我们同步本地的修改到远程仓库，所以当在本地写完博文之后，要做两件事：一是发布站点，二是同步远程仓库，这样做比较麻烦，下面会讲解如何配置`持续集成`

## 4.1、查看效果

这里我配置了自定义域名

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b3eb6d151384050b1e2754287dd6dad~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)

## 5、自动部署

> 就是DevOps，可以理解成 `GitHub` 通过一些`流水线`的配置（CI/CD），然后在本地推送代码的时候触发`流水线`执行，自动部署站点。

由于 `GitHub Actions` 也可以实现CI/CD，`travis-ci` 的市场被挤压了，所以他们改变了运营策略，变成收费使用了！我们换用 `GitHub Actions`

`GitHub Actions` 是开源持续集成构建项目，用来持续集成托管在GitHub上的代码，使用起来也非常的简单方便。

使用 `GitHub Actions` 后，可以将前面部署的步骤自动化，我们只需要将本地修改的文件推送到 `github` 仓库，`GitHub Actions` 检测到 `master` 分支代码有变动，会自动执行脚本命令，将 `Hexo` 项目编译生成静态页面，部署到 `gh-pages` 分支，very good！

## 6、GitHub Actions

`GitHub Actions`文档请点击[这里](https://link.juejin.cn/?target=https%3A%2F%2Fdocs.github.com%2Fcn%2Factions "https://docs.github.com/cn/actions")

> 使用`Github Action`来部署`hexo`，这样电脑本地就不需要安装npm相关的东西了。另外利用`github.dev`也可以实现在页面上编辑了。
> 
> **在线编辑**: `Github`有提供一个在线编辑的页面，在Repo页面按下按键`.`就可以打开编辑页面了

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cd986c96ab046d38a10dfdab716730e~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)

每个 `action` 就是一个独立脚本，因此可以做成代码仓库，使用`userName/repoName`的语法引用 `action`。比如，`actions/setup-node`就表示[`github.com/actions/setup-node`](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Factions%2Fsetup-node "https://github.com/actions/setup-node")这个仓库，它代表一个 `action`，作用是安装 Node.js。事实上，GitHub 官方的 actions 都放在 [`github.com/actions`](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Factions "https://github.com/actions") 里面。

## 6.1、支持的令牌

支持三个令牌。

| 令牌 | 私人仓库 | 公开仓库 | 协议 | 设置 |
| --- | --- | --- | --- | --- |
| github\_token | ✅️ | ✅️ | HTTPS | 不必要 |
| deploy\_key | ✅️ | ✅️ | SSH | 必要的 |
| personal\_token | ✅️ | ✅️ | HTTPS | 必要的 |

> 注意：`GITHUB_TOKEN`不是个人访问令牌，`GitHub Actions` 运行器会自动创建一个`GITHUB_TOKEN`密钥以在您的工作流程中进行身份验证。因此，您无需任何配置即可立即开始部署

## 6.2、支持的平台

所有 `Actions` 运行器：支持 Linux (Ubuntu)、macOS 和 Windows。

| 环境 | github\_token | deploy\_key | personal\_token |
| --- | --- | --- | --- |
| ubuntu-20.04 | ✅️ | ✅️ | ✅️ |
| ubuntu-18.04 | ✅️ | ✅️ | ✅️ |
| macos-最新 | ✅️ | ✅️ | ✅️ |
| windows-最新 | ✅️ | (2) | ✅️ |

## 7、为Hexo配置GitHub Actions

具体步骤：

## 7.1、设置 SSH 私钥 `deploy_key`

创建 SSH 部署密钥，使用以下命令生成部署密钥。

```
ssh-keygen -t rsa -b 4096 -C "$(git config user.email)" -f gh-pages -N ""
```

您将获得 2 个文件：

-   gh-pages.pub是公钥
    
-   gh-pages是私钥
    

接下来，转到博客源码存储库设置

-   转到`Deploy Keys`并使用`Allow write access`添加您的公钥 `gh-pages.pub`，name写为`public key of ACTIONS_DEPLOY_KEY`，指定用途，方便后面维护

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c989e68f4dcd449ea23a315967a6522f~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)

-   转到`Actions secrets`并将您的私钥 `gh-pages` 添加为 `ACTIONS_DEPLOY_KEY`（这个名称在yml文件中需要使用）

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6283a8f19bdc47d484b5070935872f04~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)

## 7.2、新建 .github/workflows/pages.yml 文件

`yml`文件通过缩进（空格，不是tab）来表示层级关系。

`yaml`不会的，可以去看一下[这里](https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fw3cnote%2Fyaml-intro.html "https://www.runoob.com/w3cnote/yaml-intro.html")，了解一下语法即可。

以下文件是我个人的配置的一部分，不建议直接使用

```
name: Pages

# 触发器、分支
on:
  push:
    branches:
      - master  # default branch
jobs:
  # 子任务
  pages:
    runs-on: ubuntu-latest # 定运行所需要的虚拟机环境
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v2
        # with:
        #   submodules: true
        #   fetch-depth: 0
      # 每个name表示一个步骤:step
      - name: Use Node.js 16.x
        uses: actions/setup-node@v2
        with:
          node-version: '16.14.1' # 自己正在使用的node版本即可
      # - run: node -v # 查看node版本号
      # 缓存依赖项: https://docs.github.com/cn/actions/using-workflows/caching-dependencies-to-speed-up-workflows
      - name: Cache NPM dependencies
        uses: actions/cache@v2
        with:
          # npm cache files are stored in `~/.npm` on Linux/macOS
          path: ~/.npm
          # path: node_modules
          key: ${{ runner.OS }}-npm-cache
          restore-keys: |
            ${{ runner.OS }}-npm-cache
      # 查看路径 : /home/runner/work/blog/blog
      # - name: Look Path
      #   run: pwd
      # 查看文件
      - name: Look Dir List
        run: tree -L 3 -a
      # 第一次或者依赖发生变化的时候执行 Install Dependencies，其它构建的时候不需要这一步
      - name: Install Dependencies
        run: npm install
      - name: Look Dir List
        run: tree -L 3 -a
      # - name: clean theme cache
      #   run: git rm -f --cached themes/tenacity
        # run: git submodule deinit themes/tenacity && git rm themes/tenacity
      # 安装主题
      - name: Install Theme
        run: git submodule add https://github.com/all-smile/tenacity.git themes/tenacity
      - name: Clean
        run: npm run clean
      - name: Build
        run: npm run build
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          deploy_key: ${{ secrets.ACTIONS_DEPLOY_KEY  }}
          user_name: xiao
          user_email: allblue95@126.com
          # 获取提交文章源码时的commit message，作为发布gh-pages分支的信息
          commit_message: ${{ github.event.head_commit.message }}
          full_commit_message: ${{ github.event.head_commit.message }}
          github_token: ${{ secrets.GITHUB_TOKEN }}
          # GITHUB_TOKEN不是个人访问令牌，GitHub Actions 运行器会自动创建一个GITHUB_TOKEN密钥以在您的工作流程中进行身份验证。因此，您无需任何配置即可立即开始部署
          publish_dir: ./public
          allow_empty_commit: true # 允许空提交
      # Use the output from the `deploy` step(use for test action)
      - name: Get the output
        run: |
          echo "${{ steps.deploy.outputs.notify }}"

```

## 7.3、修改 `_config.yml` 文件中的`Deploy`配置

```
# Deployment
## Docs: https://hexo.io/docs/one-command-deployment
deploy:
  type: 'git'
  repo: git@github.com:all-smile/blog.git
  branch: gh-pages
  # 默认提交信息： Site updated: {{ now('YYYY-MM-DD HH:mm:ss') }}
  message: ${{ github.event.head_commit.message }} # 直接将提交消息传输到 GitHub Pages 存储库
```

## 发布效果

本地仓库直接`push`，触发 `GitHub Actions` 自动构建发布

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0727ebf023fe4522aa1d502364da0d3e~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98b72d96552d43b0af0cd55614b825f5~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13570cbc56f94f6c8d65303e7c468f6b~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)

网站截图：

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80566cf915904c258a3634a13da5be4b~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)

## Hexo主题

请查看[文档](https://link.juejin.cn/?target=https%3A%2F%2Fhexo.io%2Fzh-cn%2Fdocs%2Fthemes.html "https://hexo.io/zh-cn/docs/themes.html") ，自行安装配置

## 8、GitHub Actions问题解决

## 8.1、非法输入值

在 `pages.yml` 文件的 `Deploy` 步骤下，发布的时候需要一些参数配置，这些参数名是指定好的，不可以随便写，比如 `commit_msg`应该使用 `commit_message`

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9f52efabb8141569f915e92ac874070~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)

```
commit_message: ${{ github.event.head_commit.message }}
```

> Warning: Unexpected input(s) 'commit\_msg', valid inputs are \['deploy\_key', 'github\_token', 'personal\_token', 'publish\_branch', 'publish\_dir', 'destination\_dir', 'external\_repository', 'allow\_empty\_commit', 'keep\_files', 'force\_orphan', 'user\_name', 'user\_email', 'commit\_message', 'full\_commit\_message', 'tag\_name', 'tag\_message', 'enable\_jekyll', 'disable\_nojekyll', 'cname', 'exclude\_assets'\]

## 8.2、The process '/usr/bin/git' failed with exit code 128

这个问题大概率是 `GITHUB_TOKEN` 造成的，参考[配置文档](https://link.juejin.cn/?target=https%3A%2F%2Fdocs.github.com%2Fen%2Factions%2Fsecurity-guides%2Fautomatic-token-authentication "https://docs.github.com/en/actions/security-guides/automatic-token-authentication")

`GITHUB_TOKEN` 是一种 `GitHub` 应用程序安装访问令牌。 可以使用安装访问令牌代表仓库中安装的 `GitHub` 应用程序进行身份验证。令牌的权限仅限于包含您的工作流程的仓库。

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8cfc6de2ea8a411c95da5b169d8a40ae~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)

解决：

-   查看 `yml` 文件中的名字是否写错

```
github_token: ${{ secrets.GITHUB_TOKEN }}
```

-   在 仓库 `Settings/Actions/general` 下，修改 `GITHUB_TOKEN` 的权限

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3908f54d1e8470286a22f7972d0b874~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)

## 8.3、deploy key问题

```
ERROR: Permission to all-smile/blog.git denied to deploy key
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

解决：

-   查看 `pages.yml` 中引用的变量名称是否跟 GitHub 仓库上设置的一样
    
-   公私钥是否匹配，如果不匹配，则重新生成添加即可
    

👉👉 如果还有其它问题也可以看一下[这里](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpeaceiris%2Factions-gh-pages%23readme "https://github.com/peaceiris/actions-gh-pages#readme")，应该会有帮助的😊

## 最后

-   本地写文只需要在写完之后`push`到远程仓库即可发布
    
-   其它电脑本地使用，有git就可以了，直接拉取远程仓库源码，在本地创建文件、编辑、推送远端，即可发布
    
-   也可以用`github.dev`在线创建、编辑、发文
    


