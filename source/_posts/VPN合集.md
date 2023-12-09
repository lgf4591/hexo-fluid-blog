
---
title: VPN合集 
date: 2023-12-09 13:11:52
index_img: https://fluid.s3.bitiful.net/hello-fluid/cover.png?w=480&fmt=webp
category: VPN
tags:
  - VPN
  - Github
  - hosts
math: true
mermaid: true
sticky: 100
---

> Last Update Time: 2023-12-09 13:11:52
---
# vless_node
```bash

None

```

# CloudFlare优质IP
```bash

电信172.64.93.47
电信172.64.100.203
电信172.64.196.249

联通198.41.209.132
联通172.64.103.218
联通172.67.225.183

移动172.67.2.16
移动172.67.67.120
移动172.67.199.122


```

# Github hosts
## [Github520](https://github.com/521xueweihan/GitHub520)
# GitHub520
<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/521xueweihan/img_logo@main/logo/readme.gif"/>
  <br><strong><a href="https://github.com/521xueweihan/HelloGitHub" target="_blank">HelloGitHub</a></strong> 分享 GitHub 上有趣、入门级的开源项目。<br>兴趣是最好的老师，这里能够帮你找到编程的兴趣！
</p>

服务器续费到 2024.12 共花了：1500+💰 [点击扫码赞助](https://cdn.jsdelivr.net/gh/521xueweihan/img_logo@main/logo/receiving_code.png)，感谢🙏

## 一、介绍
对 GitHub 说"爱"太难了：访问慢、图片加载不出来。

**本项目无需安装任何程序，仅需 5 分钟。**

通过修改本地 hosts 文件，试图解决：
- GitHub 访问速度慢的问题
- GitHub 项目中的图片显示不出的问题

让你"爱"上 GitHub。



*注：* 本项目还处于测试阶段，仅在本机测试通过，如有问题欢迎提 [issues](https://github.com/521xueweihan/GitHub520/issues/new)


## 二、使用方法

下面的地址无需访问 GitHub 即可获取到最新的 hosts 内容：

- 文件：`https://raw.hellogithub.com/hosts`
- JSON：`https://raw.hellogithub.com/hosts.json`

### 2.1 手动方式

#### 2.1.1 复制下面的内容

```bash
# GitHub520 Host Start
140.82.114.26                 alive.github.com
140.82.112.5                  api.github.com
185.199.110.153               assets-cdn.github.com
185.199.110.133               avatars.githubusercontent.com
185.199.110.133               avatars0.githubusercontent.com
185.199.110.133               avatars1.githubusercontent.com
185.199.110.133               avatars2.githubusercontent.com
185.199.110.133               avatars3.githubusercontent.com
185.199.110.133               avatars4.githubusercontent.com
185.199.110.133               avatars5.githubusercontent.com
185.199.110.133               camo.githubusercontent.com
140.82.112.21                 central.github.com
185.199.110.133               cloud.githubusercontent.com
140.82.114.9                  codeload.github.com
140.82.113.21                 collector.github.com
185.199.110.133               desktop.githubusercontent.com
185.199.110.133               favicons.githubusercontent.com
140.82.114.3                  gist.github.com
3.5.29.96                     github-cloud.s3.amazonaws.com
52.216.57.233                 github-com.s3.amazonaws.com
16.182.65.33                  github-production-release-asset-2e65be.s3.amazonaws.com
52.217.162.129                github-production-repository-file-5c1aeb.s3.amazonaws.com
52.217.237.1                  github-production-user-asset-6210df.s3.amazonaws.com
192.0.66.2                    github.blog
140.82.114.3                  github.com
140.82.112.17                 github.community
185.199.110.154               github.githubassets.com
151.101.193.194               github.global.ssl.fastly.net
185.199.110.153               github.io
185.199.110.133               github.map.fastly.net
185.199.110.153               githubstatus.com
140.82.114.26                 live.github.com
185.199.108.133               media.githubusercontent.com
185.199.108.133               objects.githubusercontent.com
13.107.42.16                  pipelines.actions.githubusercontent.com
185.199.108.133               raw.githubusercontent.com
185.199.108.133               user-images.githubusercontent.com
13.107.213.40                 vscode.dev
140.82.112.21                 education.github.com


# Update time: 2023-12-09T20:06:15+08:00
# Update url: https://raw.hellogithub.com/hosts
# Star me: https://github.com/521xueweihan/GitHub520
# GitHub520 Host End

```

该内容会自动定时更新， 数据更新时间：2023-12-09T20:06:15+08:00

#### 2.1.2 修改 hosts 文件

hosts 文件在每个系统的位置不一，详情如下：
- Windows 系统：`C:\Windows\System32\drivers\etc\hosts`
- Linux 系统：`/etc/hosts`
- Mac（苹果电脑）系统：`/etc/hosts`
- Android（安卓）系统：`/system/etc/hosts`
- iPhone（iOS）系统：`/etc/hosts`

修改方法，把第一步的内容复制到文本末尾：

1. Windows 使用记事本。
2. Linux、Mac 使用 Root 权限：`sudo vi /etc/hosts`。
3. iPhone、iPad 须越狱、Android 必须要 root。

#### 2.1.3 激活生效
大部分情况下是直接生效，如未生效可尝试下面的办法，刷新 DNS：

1. Windows：在 CMD 窗口输入：`ipconfig /flushdns`

2. Linux 命令：`sudo nscd restart`，如报错则须安装：`sudo apt install nscd` 或 `sudo /etc/init.d/nscd restart`

3. Mac 命令：`sudo killall -HUP mDNSResponder`

**Tips：** 上述方法无效可以尝试重启机器。

### 2.2 自动方式（SwitchHosts）

**Tip**：推荐 [SwitchHosts](https://github.com/oldj/SwitchHosts) 工具管理 hosts

以 SwitchHosts 为例，看一下怎么使用的，配置参考下面：

- Title: 随意

- Type: `Remote`

- URL: `https://raw.hellogithub.com/hosts`

- Auto Refresh: 最好选 `1 hour`

如图：

![](./img/switch-hosts.png)

这样每次 hosts 有更新都能及时进行更新，免去手动更新。

### 2.3 一行命令 (适用于类 Unix 系统)

#### GNU（Ubuntu/CentOS/Fedora）

`sudo sh -c 'sed -i "/# GitHub520 Host Start/Q" /etc/hosts && curl https://raw.hellogithub.com/hosts >> /etc/hosts'`

#### BSD/macOS

`sed -i "" "/# GitHub520 Host Start/,/# Github520 Host End/d" /etc/hosts && curl https://raw.hellogithub.com/hosts >> /etc/hosts`

将上面的命令添加到 cron，可定时执行。使用前确保 GitHub520 内容在该文件最后部分。

#### 在 Dcker 中运行，若遇到 `Device or resource busy` 错误，可使用以下命令执行

`cp /etc/hosts ~/hosts.new && sed -i "/# GitHub520 Host Start/Q" ~/hosts.new && curl https://raw.hellogithub.com/hosts >> ~/hosts.new && cp -f ~/hosts.new /etc/hosts`

### 2.4 AdGuard 用户（自动方式）

在 **过滤器>DNS 封锁清单>添加阻止列表>添加一个自定义列表**，配置如下：

- 名称：随意

- URL：`https://raw.hellogithub.com/hosts`（和上面 SwitchHosts 使用的一样）

如图：

![](./img/AdGuard-rules.png)

更新间隔在 **设置 > 常规设置 > 过滤器更新间隔（设置一小时一次即可）**，记得勾选上 **使用过滤器和 Hosts 文件以拦截指定域名**

![](./img/AdGuard-rules2.png)

**Tip**：不要添加在 **DNS 允许清单** 内，只能添加在 **DNS 封锁清单** 才管用。 另外，AdGuard for Mac、AdGuard for Windows、AdGuard for Android、AdGuard for IOS 等等 **AdGuard 家族软件** 添加方法均类似。


## 三、效果对比
之前的样子：

![](./img/old.png)

修改完 hosts 的样子：

![](./img/new.png)


## TODO
- [x] 定时自动更新 hosts 内容
- [x] hosts 内容无变动不会更新
- [x] 寻到最优 IP 解析结果

## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。


## [Fetch GitHub Hosts](https://hosts.gitcdn.top/)
<div align="center">
<h2>Fetch GitHub Hosts</h2>

![LOGO](assets/public/logo.png)

`fetch-github-hosts` 是主要为解决研究及学习人员访问 `Github` 过慢或其他问题而提供的 `Github Hosts` 同步工具

[![Release](https://img.shields.io/github/v/release/Licoy/fetch-github-hosts.svg?logo=git)](https://github.com/Licoy/fetch-github-hosts)
[![Build Linux & Windows](https://github.com/Licoy/fetch-github-hosts/workflows/Build%20for%20Linux%20&%20Windows/badge.svg)](https://github.com/Licoy/fetch-github-hosts)
[![Build MacOS](https://github.com/Licoy/fetch-github-hosts/workflows/Build%20for%20MacOS/badge.svg)](https://github.com/Licoy/fetch-github-hosts)

</div>

## 原理

此项目是通过部署此项目本身的服务器来获取 `github.com` 的 `hosts`，而不是通过第三方ip地址接口来进行获取，例如 `ipaddress.com` 等。

## 使用方法
### 图形化界面
到 [Releases](https://github.com/Licoy/fetch-github-hosts/releases)
或 [FastGit镜像](https://hub.fastgit.xyz/Licoy/fetch-github-hosts/releases) 中下载您的系统版本（目前支持`Windows`/`Linux`/`MacOS`
）

下载完成解压`tar.gz`压缩包，运行对应平台的执行文件即可运行（ ⚠️ 注意：Linux下需要用`sudo`进行启动，Windows和MacOS会自动进行提权操作。）

#### 客户端模式
![client](assets/public/docs/client.png)

#### 客户端启动
![client-start](assets/public/docs/client-start.png)

#### 客户端hosts源选择
![client-select](assets/public/docs/client-select.png)

#### 客户端hosts源自定义
![client-custom](assets/public/docs/client-custom.png)

#### 服务端模式
![server](assets/public/docs/server.png)

### 命令行终端

到 [Releases](https://github.com/Licoy/fetch-github-hosts/releases)
或 [FastGit镜像](https://hub.fastgit.xyz/Licoy/fetch-github-hosts/releases) 中下载您的系统版本（目前支持`Windows`/`Linux`/`MacOS`
）

#### 参数

| 参数名        | 缩写  | 默认值                                  | 必填  | 描述                                 |
|------------|-----|--------------------------------------|-----|------------------------------------|
| `mode`     | `m` | 无                                    | 是   | 启动模式 `server（服务端）` / `client（客户端）` |
| `interval` | `i` | 60                                   | 否   | 获取记录值间隔（分钟）                        |
| `port`     | `p` | 9898                                 | 否   | 服务模式监听端口以访问HTTP服务                  |
| `url`      | `u` | `https://hosts.gitcdn.top/hosts.txt` | 否   | 客户端模式远程hosts获取链接                   |

#### 启动客户端：

> 注意：
> 
> Linux下需要使用`sudo`运行；
> 
> Windows和MacOS会自动进行提权操作。

- 直接运行

```bash
# Linux/Macos
sudo fetch-github-hosts -m=client

# Windows
fetch-github-hosts.exe -m=client
```

- 自定义获取时间间隔

```bash
# Linux/Macos（10分钟获取一次）
sudo fetch-github-hosts -i=10

# Windows（10分钟获取一次）
fetch-github-hosts.exe -i=10
```

- 自定义获取链接

```bash
# Linux/Macos
sudo fetch-github-hosts -u=http://127.0.0.1:9898/hosts.json

# Windows
fetch-github-hosts.exe -u=http://127.0.0.1:9898/hosts.json
```

#### 启动服务端：

- 直接运行

```bash
# Linux/Macos
fetch-github-hosts -m=server

# Windows
fetch-github-hosts.exe -m=server
```

- 自定义监听端口

```bash
# Linux/Macos
fetch-github-hosts -m=server -p=6666

# Windows
fetch-github-hosts.exe -m=server -p=6666
```

### 手动

#### 添加hosts

访问 [https://hosts.gitcdn.top/hosts.txt](https://hosts.gitcdn.top/hosts.txt) ，
将其全部内容粘贴到你的hosts文件中，即可。

- `Linux / MacOS` hosts路径：`/etc/hosts`
- `Windows` hosts路径：`C:\Windows\System32\drivers\etc\hosts`

#### 刷新生效

- `Linux`: `/etc/init.d/network restart`
- `Windows`: `ipconfig /flushdns`
- `Macos`: `sudo killall -HUP mDNSResponder`

#### Unix/Linux 一键使用

```shell
sed -i "/# fetch-github-hosts begin/Q" /etc/hosts && curl https://hosts.gitcdn.top/hosts.txt >> /etc/hosts
```

> 提示：可以设置crontab定时任务定时获取更新即可，解放双手！

## 私有部署

下载最新的发行版（到 [Releases](https://github.com/Licoy/fetch-github-hosts/releases)
或 [FastGit镜像](https://hub.fastgit.xyz/Licoy/fetch-github-hosts/releases) 进行下载）
，并选择您的系统对应版本，直接以服务模式运行即可：`fetch-github-hosts -m=server -p=9898`，会自动监听`0.0.0.0:9898`，您可以直接浏览器访问 `http://127.0.0.1:9898`
以访问您自定义服务。
（具体方法可参见【启动服务端】小节详细说明）

> 注意：因网络影响，尽量部署到海外服务器节点！

## 趋势
[![Stargazers over time](https://starchart.cc/Licoy/fetch-github-hosts.svg)](https://starchart.cc/Licoy/fetch-github-hosts)

## 开源协议

[GPL 3.0](https://github.com/Licoy/fetch-github-hosts/blob/main/LICENSE)


# [freefq](https://github.com/freefq/free)
更新时间 2023-12-09 20:00  
所有免费节点都爬取自网络，请勿用于非法用途  
|  工具  | Android  | Windows  |  
|  ----  | ----   | ----  |  
| v2ray  | [v2rayNG](https://github.com/2dust/v2rayNG/releases/download/1.6.28/v2rayNG_1.6.28_arm64-v8a.apk) | [v2rayN](https://github.com/2dust/v2rayN/releases/download/3.27/v2rayN-Core.zip) |  
### v2rayN使用教程：[点击查看](https://github.com/freefq/tutorials)  
### 节点导入方法  
CTRL+A网页全选，CTRL+C复制，右键点击任务栏v2rayN客户端图标，左键点击从剪贴板批量导入URL，即可一键导入所有v2ray节点  
### 节点更新订阅  
- `https://bulinkbulink.com/freefq/free/master/v2`  
### 自建节点订阅  
[bulink.xyz](https://bulink.xyz)注册（要翻墙）除可订阅本页免费节点，还有每月5G自建节点免费流量，不用打卡签到长期有效，欢迎体验  
新开bulink镜像站[burstlinker.com](https://www.burstlinker.com)（不需要翻墙）  
## v2ray  
```  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTk2M2ZcdTkxY2NcdTRlOTEgMSIsICJhZGQiOiAibjE3MDE3NjE0NTYuZ3hwbm10Zy5jbiIsICJwb3J0IjogIjQ0MyIsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJ0bHMiOiAidGxzIiwgImlkIjogImJjZTQwNmVkLTE0MzUtNGFmZC1iYjgxLTU0ZWUyMWI2OTZhNyIsICJzbmkiOiAibjE3MDE3NjE0NTYuZ3hwbm10Zy5jbiIsICJob3N0IjogIiIsICJwYXRoIjogIi8ifQ==  
vmess://eyJhZGQiOiAiMTAzLjE1OS4xMzIuNTkiLCAiYWlkIjogMCwgImhvc3QiOiAiIiwgImlkIjogIjE5OGFkZDRhLTI1ZWItNDM0MC1jMjhlLWI5NjBhMjU1OGNkYSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0NjkyMywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU0ZTlhXHU1OTJhXHU1NzMwXHU1MzNhICAyIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTc0NWVcdTUxNzggIDMiLCAiYWRkIjogIjE0OC4xMzUuNzIuMTY5IiwgInBvcnQiOiAiODA4MCIsICJpZCI6ICJlNTE0YzNjOS03MDNkLTRlOTQtZTcxZi03M2Y5ZjM0ODk3ZWMiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=  
vmess://eyJhZGQiOiAiNDYuMjkuMTY2LjEyNCIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiMjkxYTVjNmEtNDQ3ZS00ZmM3LWIzZDctMjhlYmVjNWNiY2Q3IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6ICI0NzQxMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NGZjNFx1N2Y1N1x1NjVhZiAgNCIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggNSIsICJhZGQiOiAiMTgzLjI0MC4yMjIuMTcxIiwgInBvcnQiOiAiMzM1NjEiLCAiaWQiOiAiZTNhNDQwNzgtNTY2OS00MjMyLWEzMDYtZmZjZDYyN2Y3MTdiIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIxODMuMjQwLjIyMi4xNzEiLCAicGF0aCI6ICIvYXdzanBCIiwgInRscyI6ICIiLCAic25pIjogIiJ9  
vmess://eyJhZGQiOiAiYjIyLm50YnEuZHludS5uZXQiLCAiYWlkIjogMCwgImhvc3QiOiAiYjIyLm50YnEuZHludS5uZXQiLCAiaWQiOiAiNDQ1NDA1ZTctOGNiMi00YTBmLWJlNDgtNzcxNGM4ZjIzM2UyIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9iMjIiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1M2YwXHU2ZTdlXHU3NzAxXHU0ZTJkXHU1MzRlXHU3NTM1XHU0ZmUxIDYiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==  
vmess://eyJhZGQiOiAiNjQuMTc2LjQ3LjY5IiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICIzYTc5ZGUzMy1iZmEwLTRkNWEtZDY4MS0zYmZmYjNlYTBlNjIiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNTg3MDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YSA3IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUyYTBcdTYyZmZcdTU5MjdURUxVUyA4IiwgImFkZCI6ICI3NC40OC4xODMuMjQ2IiwgInBvcnQiOiAiNDAzMTAiLCAiaWQiOiAiNjM3MWVlNDgtOGIxOS00YTRjLWEzOTktODhmNjkyMjI4YWMzIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9  
vmess://eyJhZGQiOiAiNDcuMjM2LjE4LjI1MCIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiMWQxYTNkNjUtZWRkNi00M2FmLWU2M2YtYzg3YTg5ODk3Zjk1IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6ICI5MjIwIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU5NjNmXHU5MWNjXHU0ZTkxIDkiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiIiwgInYiOiAiMiJ9  
vmess://eyJhZGQiOiAiMTAzLjExNC4yMDIuMTU3IiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICI2OWM1ZWVlYS0zNzViLTRlMDYtYTNjZC01NzM0YzM5ZmJhZGIiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJwb3J0IjogIjM2ODc0IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzcwXHU1ZWE2ICAxMCIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=  
vmess://eyJhZGQiOiAiYjIzLm50YnEuZHludS5uZXQiLCAiYWlkIjogMCwgImhvc3QiOiAiYjIzLm50YnEuZHludS5uZXQiLCAiaWQiOiAiOGU1M2I4MzgtZTVhNC00NWZiLTk0YzItZjVkZDdmN2Y3MjlhIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9iMjMiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1M2YwXHU2ZTdlXHU3NzAxXHU2NWIwXHU3YWY5XHU1ZTAyXHU0ZTJkXHU1MzRlXHU3NTM1XHU0ZmUxIDExIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=  
ss://YWVzLTI1Ni1nY206ZG9uZ3RhaXdhbmcuY29t@64.31.55.5:11223#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%BE%97%E5%85%8B%E8%90%A8%E6%96%AF%E5%B7%9E%E8%BE%BE%E6%8B%89%E6%96%AFLimestone%E7%BD%91%E7%BB%9C%E5%85%AC%E5%8F%B8%2012  
vmess://eyJhZGQiOiAiMTcyLjk5LjE5MC4xMiIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiMDQ2MjFiYWUtYWIzNi0xMWVjLWI5MDktMDI0MmFjMTIwMDAyIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDIyMzI0LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDEzIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=  
ss://Y2hhY2hhMjAtcG9seTEzMDU6U0VadVlYZEdXakJEWW14eU5GaDVUSGhaTlc1Sk9WcERVa0ZKUVhKSVVUWjRSMUJuU1cwNFJYZFFNa2xUVTNoMGFsRmpNWEIxYXpOcGRXMU5XWEIzTXc9PQ@172.252.59.67:42572#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2014  
ss://Y2hhY2hhMjAtcG9seTEzMDU6YVRsQ2VGWXpTM0pTTUdabE1tTjNhRUYxVlZaS1dGWTVUbTUzVnpReFVIZEhTVm8zU0RkaFQzQlJWSE14Y21SSFpuSlhXVTVCWmtoSmNtSktZVGQ1UlE9PQ@37.128.253.52:51282#github.com/freefq%20-%20%E4%BC%8A%E6%9C%97%20%2015  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTgxN2VcdThiYWZcdTRlOTEgMTYiLCAiYWRkIjogIjQzLjEzMi4xNjQuOTkiLCAicG9ydCI6ICI4MDAyIiwgImlkIjogIjc1ZWQ2YzBkLWNkMzItNGIxMC1mNzFmLWNkMGI5YzZlZmEzZiIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=  
vmess://eyJhZGQiOiAiYjIxLm50YnEuZHludS5uZXQiLCAiYWlkIjogMCwgImhvc3QiOiAiYjIxLm50YnEuZHludS5uZXQiLCAiaWQiOiAiOGU1M2I4MzgtZTVhNC00NWZiLTk0YzItZjVkZDdmN2Y3MjlhIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9iMjEiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1M2YwXHU2ZTdlXHU3NzAxXHU1M2YwXHU1MzE3XHU1ZTAyXHU0ZTJkXHU1MzRlXHU3NTM1XHU0ZmUxIDE3IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=  
vmess://eyJhZGQiOiAiMjE3LjE2MC40NS4zMSIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiNGUxODY2NzgtZmNjYS00MzI1LWU0YmMtYjI5MTZiZGY2NzA4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIiIsICJwb3J0IjogIjg4ODAiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVmYjdcdTU2ZmRPbmVBbmRPbmVcdTUxNmNcdTUzZjggMTgiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiIiwgInYiOiAiMiJ9  
vmess://eyJhZGQiOiAiMTAzLjE3Ny45NC4xMzgiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiIiwgImlkIjogIjAwOWJhZTA1LTgwYmItNGUyNy1kMmMxLWVmZWE2MjllOTVhZSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAiMjI4NDMiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDE5IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIm5vbmUiLCAidiI6ICIyIn0=  
vmess://eyJhZGQiOiAiNzkuMTMyLjEyOC42MCIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiODM5MTAyYWQtODQyZi00M2U1LWU1ODktYWMxMGEzYzc4NTcxIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6ICIyMTUyNCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWZiN1x1NTZmZCAgMjAiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiIiwgInYiOiAiMiJ9  
ss://Y2hhY2hhMjAtcG9seTEzMDU6TXhadU9wcHBiWQ@175.178.55.243:33963#github.com/freefq%20-%20%E7%A6%8F%E5%BB%BA%E7%9C%81%E5%8E%A6%E9%97%A8%E5%B8%82%E9%87%91%E6%A1%A5%E7%BD%91%E7%BB%9C%E9%80%9A%E4%BF%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2021  
vmess://eyJhZGQiOiAiNjQuMTc2LjM5LjMxIiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICI1OTBmMjc0NC1lOWQxLTRmMmMtYTM4NC1kMzViNzM2YmNhNDEiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjU2MjYyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhIDIyIiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==  
vmess://eyJhZGQiOiAiMjEwLjYxLjIwNi4yMjUiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiIiwgImlkIjogIjA4M2FlZTIyLWY3YWUtNDMwNS1lZjlhLTUzMjQ4MmQ1YTcwOSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAiNDQ0NzMiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDFcdTlhZDhcdTk2YzRcdTVlMDJcdTRlMmRcdTUzNGVcdTc1MzVcdTRmZTEgMjMiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAibm9uZSIsICJ2IjogIjIifQ==  
ss://Y2hhY2hhMjAtcG9seTEzMDU6MTIzNDU2Nzg5@176.119.203.233:1111#github.com/freefq%20-%20%E4%BF%84%E7%BD%97%E6%96%AF%20%2024  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDI1IiwgImFkZCI6ICIxNzIuNjQuMTk1LjEwNyIsICJwb3J0IjogIjIwNTIiLCAiaWQiOiAiMDdjY2MzYjgtYzllZC00MDMwLWI2YWUtMDkzOTQ2N2VlMWIyIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ5dXl1aGFuZ3VvMDEudGd5dWpjY2hhbm5lbC5zaXRlIiwgInBhdGgiOiAiLz9lZD0yMDQ4IiwgInRscyI6ICIifQ==  
vmess://eyJhZGQiOiAiNjQuMTc2LjM3LjIxNiIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiYjI5MzBiMGQtMDJiNC00NWRjLTgwMjUtYTNjMTk4NzlkNGFiIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6ICI0NTkzMCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YSAyNiIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9  
vmess://eyJhZGQiOiAiNjIuMTMzLjYwLjEzNCIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiOTk4ZDBhZWEtOTU0MC0xMWVlLTkxMTEtM2ZlN2MxZDM0ZDcxIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi92cG5qYW50aXQiLCAicG9ydCI6IDEwMDAxLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRmYzRcdTdmNTdcdTY1YWYgIDI3IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTViNWZcdTUyYTBcdTYyYzkgIDI4IiwgImFkZCI6ICIxMDMuOTkuMTEuMTM3IiwgInBvcnQiOiAiNTMwNTIiLCAiaWQiOiAiZWNjNGEwYTctNDBiYy00MTU5LWU3MGItMDU3NDgzYmVlMjQ0IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9  
vmess://eyJhZGQiOiAiMTcyLjk5LjE5MC4xMDkiLCAiYWlkIjogMCwgImhvc3QiOiAiIiwgImlkIjogIjAzZmNjNjE4LWI5M2QtNjc5Ni02YWVkLThhMzhjOTc1ZDU4MSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICJsaW5rdndzIiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZCAgMjkiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICJudWxsIn0=  
vmess://eyJhZGQiOiAiMTQ2LjE5MC45Ny44IiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIm0ubGlua2VkaW4uY29tIiwgImlkIjogIjI2Yzk3NTcxLTI1NzMtNDRmZS1lNjJhLTIyOTk5NDM1ZDIxNyIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgInBvcnQiOiAiNDY1MDYiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDMwIiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==  
vmess://eyJhZGQiOiAibmJxMTIubnRicS5keW51Lm5ldCIsICJhaWQiOiAwLCAiaG9zdCI6ICJuYnExMi5udGJxLmR5bnUubmV0IiwgImlkIjogIjQ0NTQwNWU3LThjYjItNGEwZi1iZTQ4LTc3MTRjOGYyMzNlMiIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvYjEyIiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTNmMFx1NmU3ZVx1NzcwMVx1NTNmMFx1NTMxN1x1NWUwMlx1NGUyZFx1NTM0ZVx1NzUzNVx1NGZlMSAzMSIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDMyIiwgImFkZCI6ICJjb3Zlci5tYWMyd2luLnRvcCIsICJwb3J0IjogODA4MCwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgInRscyI6ICIiLCAiaWQiOiAiNjVhZTM1ZDEtMDFiOC00MmU0LTgzNzMtMDBkMDE2MjNjNmVkIiwgInNuaSI6ICIiLCAiaG9zdCI6ICJpY3UubWFjMndpbi50b3AiLCAicGF0aCI6ICIvIn0=  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNzBcdTVlYTYgIDMzIiwgImFkZCI6ICIxMDMuMTE0LjIwMS40NCIsICJwb3J0IjogIjQ1MjMzIiwgImlkIjogIjhlODc4MjFlLWMyMmEtNDRjNi1jNzQxLTQzYWI3OTFmNDdiNiIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==  
vmess://eyJhZGQiOiAiMTAzLjE1OS4yMDYuMzUiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiIiwgImlkIjogImUyZTUxMWIwLTdkZWYtNGUxYi1kMjM4LTZjYjUzOTFiMmUzZiIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgInBvcnQiOiAiMzE5NDUiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDM0IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRmMGFcdTY3MTcgIDM1IiwgImFkZCI6ICIzNy4xNTIuMTg2LjEwOSIsICJwb3J0IjogIjMxMzQxIiwgImlkIjogIjlkMzc5MTYxLWNiZWItNGVmNi1mMDIzLWNhMTc0MTc1ZWE2MiIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==  
vmess://eyJhZGQiOiAiMjEwLjYxLjIwNi4yMjkiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiIiwgImlkIjogIjM5ZDM5MDE3LWY5NTUtNGIxMC1iMjY5LWQxNjZlYzZiMTdjOSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAiMjE0MzMiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDFcdTlhZDhcdTk2YzRcdTVlMDJcdTRlMmRcdTUzNGVcdTc1MzVcdTRmZTEgMzYiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAibm9uZSIsICJ2IjogIjIifQ==  
vmess://eyJhZGQiOiAiMTgzLjE4MS4zNi4xOTQiLCAiYWlkIjogIjAiLCAiaG9zdCI6ICIiLCAiaWQiOiAiNGE2ZWFhMmQtNTYwMy00YzA1LWQ5NjctZmI2ZjQyMjUwYTVhIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6ICI0MTU5NyIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NjVlNVx1NjcyYyAgMzciLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiIiwgInYiOiAiMiJ9  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDM4IiwgImFkZCI6ICIxNjIuMTU5LjE0Mi4yMDQiLCAicG9ydCI6ICI4MCIsICJpZCI6ICI1YzM2ZGJhNC1kZTY4LTQyYmUtYTA3Zi05MzdkOWY5MjAzNTciLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImVyMy44ODk2MTEuY29tIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=  
vmess://eyJhZGQiOiAiYjIyLm50YnEuZHludS5uZXQiLCAiYWlkIjogMCwgImhvc3QiOiAiYjIyLm50YnEuZHludS5uZXQiLCAiaWQiOiAiOGU1M2I4MzgtZTVhNC00NWZiLTk0YzItZjVkZDdmN2Y3MjlhIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9iMjIiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1M2YwXHU2ZTdlXHU3NzAxXHU0ZTJkXHU1MzRlXHU3NTM1XHU0ZmUxIDM5IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=  
vmess://eyJhZGQiOiAiaGV4c2VuLmNvbSIsICJhaWQiOiAwLCAiaG9zdCI6ICJ3aWNrZWQtZGVsYXdhcmUtaG90ZWxzLWhpdC50cnljbG91ZGZsYXJlLmNvbSIsICJpZCI6ICJkZTA0YWRkOS01YzY4LThiYWItOTUwYy0wOGNkNTMyMGRmMTgiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL2FyZ28tdm1lc3M_ZWQ9MjA0OCIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDQwIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=  
vmess://eyJhZGQiOiAiMjEwLjYxLjIwNi4xOTYiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiIiwgImlkIjogIjMyYzI5MzcwLWNmZjMtNDliZS1hNTY1LWIzZjE2ZGZiYjg1ZCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAiMTgyMDYiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDFcdTlhZDhcdTk2YzRcdTVlMDJcdTRlMmRcdTUzNGVcdTc1MzVcdTRmZTEgNDEiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiIiwgInYiOiAiMiJ9  
ss://YWVzLTI1Ni1nY206dFU2dHRTR29kZw@89.185.30.233:48385#github.com/freefq%20-%20%E4%B9%8C%E5%85%8B%E5%85%B0%20%2042  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDQzIiwgImFkZCI6ICJzaW5nYXBvcmUuY29tIiwgInBvcnQiOiA4ODgwLCAiaWQiOiAiYjFlMzAzMzktYTYwMy00N2QxLWIzMWMtMWQwY2ViNTk5NTJlIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJzc3JzdWIudjAwMS5zc3JzdWIuY29tIiwgInBhdGgiOiAiL2FwaS92My9kb3dubG9hZC5nZXRGaWxlIiwgInRscyI6ICIifQ==  
vmess://eyJhZGQiOiAiYjI0Lm50YnEuZHludS5uZXQiLCAiYWlkIjogMCwgImhvc3QiOiAiYjI0Lm50YnEuZHludS5uZXQiLCAiaWQiOiAiNDQ1NDA1ZTctOGNiMi00YTBmLWJlNDgtNzcxNGM4ZjIzM2UyIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9iMjQiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1M2YwXHU2ZTdlXHU3NzAxXHU1M2YwXHU1MzE3XHU1ZTAyXHU0ZTJkXHU1MzRlXHU3NTM1XHU0ZmUxIDQ0IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDQ1IiwgImFkZCI6ICJ1cy0wMi5qaWt1YWkueHl6IiwgInBvcnQiOiAiMjA4MiIsICJpZCI6ICI3MDY2Njc3Ni00ZTlmLTQzNTAtYjNmMC1hZmFmZjZhNzBkYjAiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInVzLTAyLmppa3VhaS54eXoiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9  
ss://YWVzLTI1Ni1nY206Y2hHMEMyMFBhYg@185.151.146.169:38935#github.com/freefq%20-%20%E6%84%8F%E5%A4%A7%E5%88%A9%20%2046  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlMmRcdTU2ZmRcdTk2M2ZcdTkxY2NcdTRlOTEgNDciLCAiYWRkIjogIjguMjIyLjE4Ny4xMTIiLCAicG9ydCI6ICI0NDU3NCIsICJpZCI6ICJiMThkYzViYS02MmI3LTQ0MjMtYWFjYy1mMTg0ZGExNWMwMzMiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRmMGFcdTY3MTcgIDQ4IiwgImFkZCI6ICIxOTMuMTUxLjE1MS4yMjciLCAicG9ydCI6ICIxODkwNCIsICJpZCI6ICIyNzBjZTQ3NC02ODUwLTQxMDItODVhZi01YTc3ZmM2NjAzNTAiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNzBcdTVlYTYgIDQ5IiwgImFkZCI6ICIxMDMuMTA2LjIzMC4xNTMiLCAicG9ydCI6ICIzMjczMiIsICJpZCI6ICJlYjkzMTEwOC02NDZiLTRjZWItYTc0MS1kMzI0OTBjYjAwZjQiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=  
vmess://eyJhZGQiOiAiMTAzLjE4MC4xNjEuNDciLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiIiwgImlkIjogImFhYzMwYzRkLTEyZjgtNGRkZS1mZDIyLTBkMmVlZWI5Y2U4OSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAiMjM4OTgiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDUwIiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIm5vbmUiLCAidiI6ICIyIn0=  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTc5ZDFcdTc2YzhcdTc1MzVcdTRmZTFcdTk2YzZcdTU2ZTJcdTY3MDlcdTk2NTBcdTUxNmNcdTUzZjgoXHU2MjUzXHU3ODE2XHU1NzZhXHU4ODU3NDktNTNcdTUzZjdcdTUzNGVcdTU3ZmFcdTVkZTVcdTRlMWFcdTU5MjdcdTUzYTZcdTRlOGNcdTVlYTc4XHU1YzQyQ1x1NWJhNCkgNTEiLCAiYWRkIjogIjExNS4xMjYuNTAuMTExIiwgInBvcnQiOiAiMTYzOTkiLCAiaWQiOiAiMGE4MjQ2NjAtOGIxNy00NjY1LWQyYjQtYTg2YzdmMTVkMzJhIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==  
ss://YWVzLTEyOC1nY206a3ZlQUxZYmUxVFo1R0FsQXNmM1huakxOeG9VbXJyM0luYnp1bWJ0N0JEQXA@91.229.132.214:52210#github.com/freefq%20-%20%E4%BF%9D%E5%8A%A0%E5%88%A9%E4%BA%9A%20%2052  
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpkODljYTM3MS1lOTRiLTRkZmUtYWQ2Zi0wMmJkMTNlZGY3YzQ@service.ouluyun9803.com:26667#github.com/freefq%20-%20%E5%B9%BF%E4%B8%9C%E7%9C%81%E5%B9%BF%E5%B7%9E%E5%B8%82%E7%A7%BB%E5%8A%A8%2053  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWEgNTQiLCAiYWRkIjogIjY0LjE3Ni40Ni4zNiIsICJwb3J0IjogIjExMSIsICJpZCI6ICI3MjM1ZWIxOS1hYjU1LTRmMGQtY2IwYS1hNjIwOTMwYTViNTkiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDU1IiwgImFkZCI6ICIxMDQuMTcuMTkzLjE0NSIsICJwb3J0IjogIjgwODAiLCAiaWQiOiAiZTI2OTViZDAtOTQ1Zi00NDc2LWFhYzUtMGUzN2JjZGJkN2ZjIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJldTUub3BlbnhhaS5saW5rIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDU2IiwgImFkZCI6ICJjZjIuNDkyNzQ1Lnh5eiIsICJwb3J0IjogIjgwODAiLCAiaWQiOiAiNTc5ZmQ2ZjEtNzYxOC00ZmZmLTg2MzUtOWRiYTRhNjFkZjk2IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJjYy45OTI2ODgueHl6IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTk2M2ZcdTkxY2NcdTRlOTEgNTciLCAiYWRkIjogIjQ3LjIzNi4xMTEuODMiLCAicG9ydCI6ICIzMTA5MSIsICJpZCI6ICJmMGVhZmQ2Yi1hZDM5LTQ4NzUtOWIyOS03MjIyMzdkMTU1ZjMiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTk2M2ZcdTkxY2NcdTRlOTEgNTgiLCAiYWRkIjogIjQ3LjIzNi4yLjE0OSIsICJwb3J0IjogIjY2NjYiLCAiaWQiOiAiY2Q3NjEwMGUtM2E0YS00NjQ4LTk2YzAtYjIyMzc2ZGZhZmExIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDU5IiwgImFkZCI6ICIxMDQuMjEuNzUuMjQ2IiwgInBvcnQiOiA4MCwgImlkIjogImM0NTg2OTVkLTY5MDgtNDVjMy05NTEyLWUwYzQ2NDE4NDU0YyIsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAic2JsMi5zaGFiaWppY2hhbmcuY29tIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=  
ss://YWVzLTI1Ni1nY206MTIz@43.156.237.238:10000#github.com/freefq%20-%20%E6%97%A5%E6%9C%AC%20%2060  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDYxIiwgImFkZCI6ICJoeXRyb24uaW8iLCAicG9ydCI6ICI4MDgwIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICIwMTBjMjY1Zi01NDU1LTQxNDEtY2EyMy00ZDY5MzU3ZGVkMGQiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJob3N0IjogImFrdHcuZGFvemhhbmcubG92ZSIsICJ0bHMiOiAiIn0=  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY1YjBcdTUyYTBcdTU3NjFBbWF6b25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNjIiLCAiYWRkIjogInVzMS5jODg5ODQ5Ni1hZGI2LTQwNzMtOWVlNC1mZjRlNDk4NDQxNWIucG9seWNkbi5jb20iLCAicG9ydCI6ICI4MCIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiNzFkNWQ5NjktMWM1OC00YmM5LWIzNmMtMTExNjE2ZjAzYzAzIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICJkbC5kZWxpdmVyeS5tcC5taWNyb3NvZnQuY29tIiwgInRscyI6ICIifQ==  
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpkODljYTM3MS1lOTRiLTRkZmUtYWQ2Zi0wMmJkMTNlZGY3YzQ@service.ouluyun9803.com:20001#github.com/freefq%20-%20%E5%B9%BF%E4%B8%9C%E7%9C%81%E5%B9%BF%E5%B7%9E%E5%B8%82%E7%A7%BB%E5%8A%A8%2063  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY1YjBcdTUyYTBcdTU3NjFBbWF6b25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNjQiLCAiYWRkIjogImhrMS5jODg5ODQ5Ni1hZGI2LTQwNzMtOWVlNC1mZjRlNDk4NDQxNWIucG9seWNkbi5jb20iLCAicG9ydCI6ICI4MCIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiNzFkNWQ5NjktMWM1OC00YmM5LWIzNmMtMTExNjE2ZjAzYzAzIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICJkbC5kZWxpdmVyeS5tcC5taWNyb3NvZnQuY29tIiwgInRscyI6ICIifQ==  
vmess://eyJhZGQiOiAiNDUuMTIxLjQ4LjE5NiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDY1IiwgInBvcnQiOiAxMDAwMSwgImlkIjogIjBlZDM1NjI5LTkxOWEtNDg5MS1iYTBmLTEzY2QxOThmODYzYiIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDY2IiwgImFkZCI6ICIxMDMuMTc5LjE0Mi4xMTciLCAicG9ydCI6ICIyNDY0MCIsICJpZCI6ICIxMTlhMjViZi1lMzVlLTQ0YzItOGI4MS0yODdlYThiMmNhYzAiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDY3IiwgImFkZCI6ICJtb29uLmNoYW5lbGwubWNpLnYteDRzc2Quc3BhY2UiLCAicG9ydCI6ICI4MDgwIiwgImlkIjogIjZhZDdhZmQ3LTY5NTgtNDc4ZS05ZmZmLTg4ZjE2ZjlhMjAwOCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==  
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpkODljYTM3MS1lOTRiLTRkZmUtYWQ2Zi0wMmJkMTNlZGY3YzQ@service.ouluyun9803.com:50001#github.com/freefq%20-%20%E5%B9%BF%E4%B8%9C%E7%9C%81%E5%B9%BF%E5%B7%9E%E5%B8%82%E7%A7%BB%E5%8A%A8%2068  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlNGNcdTUxNGJcdTUxNzAgIDY5IiwgImFkZCI6ICI5NC4xMzEuMTQuMTc3IiwgInBvcnQiOiAiODAiLCAiaWQiOiAiMmM1ZmVlMTMtZjA4Yi00YmE4LTg2ZGItMjdkZDUxY2I5NzgxIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI5NC4xMzEuMTQuMTc3IiwgInBhdGgiOiAiL3ZtZXNzIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9  
```  



# ChromeGo_Merge Readme Content
## 简介

**注意：clash内核无法使用这些节点，你要用clashmeta**

开启浏览器自带doh以及客户端tun模式也可绕过封锁，参考：https://blog.mareep.net/posts/9993/


## 注意事项

套上warp可绕过chromego封锁的网站

## 如何修改为自己的warp节点

<details>
  <summary>点击展开/折叠</summary>

可以用warp+机器人和提取wg节点替换掉配置文件中的wg信息

[warp提取wireguard网站](https://replit.com/@misaka-blog/wgcf-profile-generator)

[warp+机器人](https://t.me/generatewarpplusbot)

然后本地创建一个yaml文件，参考：[issues #20](https://github.com/vveg26/chromego_merge/issues/20)

</details>

## 订阅链接分享
### 不套warp版本（clashmeta）
**不含hysteria2节点**
```
https://mareep.netlify.app/sub/merged_proxies.yaml
```
**含hysteria2节点(节点最全）**
```
https://mareep.netlify.app/sub/merged_proxies_new.yaml
```
### 套warp版本（clashmeta)
**不含hysteria2节点**
```
https://mareep.netlify.app/sub/merged_warp_proxies.yaml
```
**含hysteria2节点(节点最全）**
```
https://mareep.netlify.app/sub/merged_warp_proxies_new.yaml
```
### 通用链接 （shadowrocket和nekoray）
```
https://mareep.netlify.app/sub/shadowrocket_base64.txt
```

### sing-box订阅链接

```
https://sing-box-subscribe.vercel.app/config/https:/mareep.netlify.app/sub/merged_proxies_new.yaml
```

## 客户端推荐
### Windows
- [clash verge](https://github.com/zzzgydi/clash-verge/releases) 
- [nekoray](https://github.com/MatsuriDayo/nekoray)
### android
- [nekobox](https://github.com/MatsuriDayo/NekoBoxForAndroid)
- [clashmeta for android](https://github.com/MetaCubeX/ClashMetaForAndroid/releases)

### ios
- shadowrocket

### macos
- [clashx.meta](https://github.com/MetaCubeX/ClashX.Meta/releases)
- [clash verge](https://github.com/zzzgydi/clash-verge/releases) 
- shadowrocket

## 致谢
- [Alvin9999](https://github.com/Alvin9999/pac2/tree/master)
- [sing-box-subscribe](https://github.com/Toperlock/sing-box-subscribe)
## TODO
- 部分代码逻辑不够优雅
- sing-box节点的处理
- xray部分节点的处理
- 融合ss和ssr




# ChromeGo_Merge Detail Content
## 不套warp版本（clashmeta）
**不含hysteria2节点** (https://mareep.netlify.app/sub/merged_proxies.yaml)
```yaml
port: 7890
allow-lan: true
mode: rule
log-level: info
unified-delay: true
global-client-fingerprint: chrome
dns:
  enable: true
  listen: :53
  ipv6: true
  enhanced-mode: fake-ip
  fake-ip-range: 198.18.0.1/16
  default-nameserver:
  - 223.5.5.5
  - 8.8.8.8
  nameserver:
  - https://dns.alidns.com/dns-query
  - https://doh.pub/dns-query
  fallback:
  - https://1.0.0.1/dns-query
  - tls://dns.google
  fallback-filter:
    geoip: true
    geoip-code: CN
    ipcidr:
    - 240.0.0.0/4
proxies:
- name: meta_hysteria_01
  type: hysteria
  server: 167.160.90.251
  port: 48089
  auth-str: dongtaiwang.com
  alpn:
  - h3
  protocol: udp
  up: 11 Mbps
  down: 55 Mbps
  skip-cert-verify: true
- name: meta_tuic_02
  server: 109.104.152.219
  port: 11091
  type: tuic
  uuid: 62fc1c08-c2d7-4d35-8cb3-6289b4293679
  password: dongtaiwang.com
  sni: bing.com
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  skip-cert-verify: true
  congestion-controller: bbr
- name: meta_tuic_11
  server: tuic1.freeh1.xyz
  port: 40981
  type: tuic
  uuid: c2faac69-e1c1-4bf5-b8a8-d2ce4d834a66
  password: dongtaiwang
  sni: tuic1.freeh1.xyz
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  skip-cert-verify: false
  congestion-controller: bbr
- name: meta_tuic_21
  server: tuic3.dtku47.xyz
  port: 12255
  type: tuic
  uuid: ed6a538a-6e66-4f21-a769-4b389bb2f3ab
  password: dongtaiwang
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  congestion-controller: bbr
- name: meta_tuic_31
  server: 108.181.24.7
  port: 23450
  type: tuic
  uuid: 3618921b-adeb-4bd3-a2a0-f98b72a674b1
  password: dongtaiwang
  sni: bing.com
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  skip-cert-verify: true
  congestion-controller: bbr
- name: meta_hysteria_41
  type: hysteria
  server: www.dtku46.xyz
  port: 11223
  auth-str: mqoE9qSoyMFa
  alpn:
  - h3
  protocol: udp
  up: 11 Mbps
  down: 55 Mbps
  skip-cert-verify: true
- name: meta_tuic_51
  server: 108.181.22.205
  port: 50987
  type: tuic
  uuid: d6214437-e1b5-4334-9090-8f66b78bea89
  password: dongtaiwang
  sni: bing.com
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  skip-cert-verify: true
  congestion-controller: bbr
- name: meta_tuic_61
  server: 108.181.22.239
  port: 19988
  type: tuic
  uuid: 485ce799-da5f-46e8-a82b-8ef322d8602f
  password: dongtaiwang.com
  sni: bing.com
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  skip-cert-verify: true
  congestion-controller: bbr
- name: meta_tuic_71
  server: 109.104.152.180
  port: 22335
  type: tuic
  uuid: e78e1e93-a648-4974-b544-68f8b9fa0b81
  password: dongtaiwang.com
  sni: bing.com
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  skip-cert-verify: true
  congestion-controller: bb
- name: meta_hysteria_81
  type: hysteria
  server: www.dtku50.xyz
  port: 14751
  sni: www.microsoft.com
  skip-cert-verify: true
  alpn:
  - h3
  protocol: udp
  auth_str: 6qSZyyl4eTT8hqPMQxdhIgpxQfTyW1Oq6GBwQVhA2vBOw7QIGY
  up: 2
  down: 10
- name: meta_hysteria_91
  type: hysteria
  server: 62.204.54.81
  port: 42691
  sni: bing.com
  skip-cert-verify: true
  alpn:
  - h3
  protocol: udp
  auth_str: dongtaiwang.com
  up: 5
  down: 10
- name: hysteria_0
  type: hysteria
  server: 109.104.152.180
  port: 40522
  ports: 40522
  auth_str: dongtaiwang.com
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: www.microsoft.com
  skip-cert-verify: true
  alpn:
  - h3
- name: hysteria_1
  type: hysteria
  server: 173.234.25.52
  port: 20164
  ports: 20164
  auth_str: Ljg6NNEATDqP97hdAdHe1lJv7ggtKc0h7zmCCZKCX3qY0LR64F
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: www.microsoft.com
  skip-cert-verify: true
  alpn:
  - h3
- name: hysteria_2
  type: hysteria
  server: 109.104.152.149
  port: 48406
  ports: 48406
  auth_str: xfNhrunYJ9GvDXCTktY2bIwhc1EyeyyAbiUMx1UtBOWgI4cMVB
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: www.amazon.cn
  skip-cert-verify: true
  alpn:
  - h3
- name: hysteria_3
  type: hysteria
  server: 51.158.54.46
  port: 11926
  ports: 11926
  auth_str: Trz2alKwzCImRAXI3nXfpo1ylpHfqOL8s1vageWKoyjjvWeMVs
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: youku.com
  skip-cert-verify: true
  alpn:
  - h3
proxy-groups:
- name: 节点选择
  type: select
  proxies:
  - 自动选择
  - DIRECT
  - meta_hysteria_01
  - meta_tuic_02
  - meta_tuic_11
  - meta_tuic_21
  - meta_tuic_31
  - meta_hysteria_41
  - meta_tuic_51
  - meta_tuic_61
  - meta_tuic_71
  - meta_hysteria_81
  - meta_hysteria_91
  - hysteria_0
  - hysteria_1
  - hysteria_2
  - hysteria_3
- name: 自动选择
  type: url-test
  url: http://www.gstatic.com/generate_204
  interval: 300
  tolerance: 50
  proxies:
  - meta_hysteria_01
  - meta_tuic_02
  - meta_tuic_11
  - meta_tuic_21
  - meta_tuic_31
  - meta_hysteria_41
  - meta_tuic_51
  - meta_tuic_61
  - meta_tuic_71
  - meta_hysteria_81
  - meta_hysteria_91
  - hysteria_0
  - hysteria_1
  - hysteria_2
  - hysteria_3
rules:
- DOMAIN,clash.razord.top,DIRECT
- DOMAIN,yacd.haishan.me,DIRECT
- GEOIP,LAN,DIRECT
- GEOIP,CN,DIRECT
- MATCH,节点选择

```

**含hysteria2节点(节点最全）** (https://mareep.netlify.app/sub/merged_proxies_new.yaml)
```yaml
port: 7890
allow-lan: true
mode: rule
log-level: info
unified-delay: true
global-client-fingerprint: chrome
dns:
  enable: true
  listen: :53
  ipv6: true
  enhanced-mode: fake-ip
  fake-ip-range: 198.18.0.1/16
  default-nameserver:
  - 223.5.5.5
  - 8.8.8.8
  nameserver:
  - https://dns.alidns.com/dns-query
  - https://doh.pub/dns-query
  fallback:
  - https://1.0.0.1/dns-query
  - tls://dns.google
  fallback-filter:
    geoip: true
    geoip-code: CN
    ipcidr:
    - 240.0.0.0/4
proxies:
- name: meta_hysteria_01
  type: hysteria
  server: 167.160.90.251
  port: 48089
  auth-str: dongtaiwang.com
  alpn:
  - h3
  protocol: udp
  up: 11 Mbps
  down: 55 Mbps
  skip-cert-verify: true
- name: meta_tuic_02
  server: 109.104.152.219
  port: 11091
  type: tuic
  uuid: 62fc1c08-c2d7-4d35-8cb3-6289b4293679
  password: dongtaiwang.com
  sni: bing.com
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  skip-cert-verify: true
  congestion-controller: bbr
- name: meta_tuic_11
  server: tuic1.freeh1.xyz
  port: 40981
  type: tuic
  uuid: c2faac69-e1c1-4bf5-b8a8-d2ce4d834a66
  password: dongtaiwang
  sni: tuic1.freeh1.xyz
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  skip-cert-verify: false
  congestion-controller: bbr
- name: meta_tuic_21
  server: tuic3.dtku47.xyz
  port: 12255
  type: tuic
  uuid: ed6a538a-6e66-4f21-a769-4b389bb2f3ab
  password: dongtaiwang
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  congestion-controller: bbr
- name: meta_tuic_31
  server: 108.181.24.7
  port: 23450
  type: tuic
  uuid: 3618921b-adeb-4bd3-a2a0-f98b72a674b1
  password: dongtaiwang
  sni: bing.com
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  skip-cert-verify: true
  congestion-controller: bbr
- name: meta_hysteria_41
  type: hysteria
  server: www.dtku46.xyz
  port: 11223
  auth-str: mqoE9qSoyMFa
  alpn:
  - h3
  protocol: udp
  up: 11 Mbps
  down: 55 Mbps
  skip-cert-verify: true
- name: meta_tuic_51
  server: 108.181.22.205
  port: 50987
  type: tuic
  uuid: d6214437-e1b5-4334-9090-8f66b78bea89
  password: dongtaiwang
  sni: bing.com
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  skip-cert-verify: true
  congestion-controller: bbr
- name: meta_tuic_61
  server: 108.181.22.239
  port: 19988
  type: tuic
  uuid: 485ce799-da5f-46e8-a82b-8ef322d8602f
  password: dongtaiwang.com
  sni: bing.com
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  skip-cert-verify: true
  congestion-controller: bbr
- name: meta_tuic_71
  server: 109.104.152.180
  port: 22335
  type: tuic
  uuid: e78e1e93-a648-4974-b544-68f8b9fa0b81
  password: dongtaiwang.com
  sni: bing.com
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  skip-cert-verify: true
  congestion-controller: bb
- name: meta_hysteria_81
  type: hysteria
  server: www.dtku50.xyz
  port: 14751
  sni: www.microsoft.com
  skip-cert-verify: true
  alpn:
  - h3
  protocol: udp
  auth_str: 6qSZyyl4eTT8hqPMQxdhIgpxQfTyW1Oq6GBwQVhA2vBOw7QIGY
  up: 2
  down: 10
- name: meta_hysteria_91
  type: hysteria
  server: 62.204.54.81
  port: 42691
  sni: bing.com
  skip-cert-verify: true
  alpn:
  - h3
  protocol: udp
  auth_str: dongtaiwang.com
  up: 5
  down: 10
- name: hysteria_0
  type: hysteria
  server: 109.104.152.180
  port: 40522
  ports: 40522
  auth_str: dongtaiwang.com
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: www.microsoft.com
  skip-cert-verify: true
  alpn:
  - h3
- name: hysteria_1
  type: hysteria
  server: 173.234.25.52
  port: 20164
  ports: 20164
  auth_str: Ljg6NNEATDqP97hdAdHe1lJv7ggtKc0h7zmCCZKCX3qY0LR64F
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: www.microsoft.com
  skip-cert-verify: true
  alpn:
  - h3
- name: hysteria_2
  type: hysteria
  server: 109.104.152.149
  port: 48406
  ports: 48406
  auth_str: xfNhrunYJ9GvDXCTktY2bIwhc1EyeyyAbiUMx1UtBOWgI4cMVB
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: www.amazon.cn
  skip-cert-verify: true
  alpn:
  - h3
- name: hysteria_3
  type: hysteria
  server: 51.158.54.46
  port: 11926
  ports: 11926
  auth_str: Trz2alKwzCImRAXI3nXfpo1ylpHfqOL8s1vageWKoyjjvWeMVs
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: youku.com
  skip-cert-verify: true
  alpn:
  - h3
- name: hysteria2_0
  type: hysteria2
  server: www.dtku46.xyz
  port: 62580
  password: dongtaiwang.com
  fast-open: true
  sni: www.bing.com
  skip-cert-verify: true
- name: hysteria2_1
  type: hysteria2
  server: 108.181.22.155
  port: 15565
  password: dongtaiwang.com
  fast-open: true
  sni: www.bing.com
  skip-cert-verify: true
- name: hysteria2_3
  type: hysteria2
  server: 108.181.22.155
  port: 15565
  password: dongtaiwang.com
  fast-open: true
  sni: www.bing.com
  skip-cert-verify: true
proxy-groups:
- name: 节点选择
  type: select
  proxies:
  - 自动选择
  - DIRECT
  - meta_hysteria_01
  - meta_tuic_02
  - meta_tuic_11
  - meta_tuic_21
  - meta_tuic_31
  - meta_hysteria_41
  - meta_tuic_51
  - meta_tuic_61
  - meta_tuic_71
  - meta_hysteria_81
  - meta_hysteria_91
  - hysteria_0
  - hysteria_1
  - hysteria_2
  - hysteria_3
  - hysteria2_0
  - hysteria2_1
  - hysteria2_3
- name: 自动选择
  type: url-test
  url: http://www.gstatic.com/generate_204
  interval: 300
  tolerance: 50
  proxies:
  - meta_hysteria_01
  - meta_tuic_02
  - meta_tuic_11
  - meta_tuic_21
  - meta_tuic_31
  - meta_hysteria_41
  - meta_tuic_51
  - meta_tuic_61
  - meta_tuic_71
  - meta_hysteria_81
  - meta_hysteria_91
  - hysteria_0
  - hysteria_1
  - hysteria_2
  - hysteria_3
  - hysteria2_0
  - hysteria2_1
  - hysteria2_3
rules:
- DOMAIN,clash.razord.top,DIRECT
- DOMAIN,yacd.haishan.me,DIRECT
- GEOIP,LAN,DIRECT
- GEOIP,CN,DIRECT
- MATCH,节点选择

```

## 套warp版本（clashmeta)
**不含hysteria2节点** (https://mareep.netlify.app/sub/merged_warp_proxies.yaml)
```yaml
port: 7890
allow-lan: true
mode: rule
log-level: info
unified-delay: true
global-client-fingerprint: chrome
dns:
  enable: true
  listen: :53
  ipv6: true
  enhanced-mode: fake-ip
  fake-ip-range: 198.18.0.1/16
  default-nameserver:
  - 223.5.5.5
  - 8.8.8.8
  nameserver:
  - https://dns.alidns.com/dns-query
  - https://doh.pub/dns-query
  fallback:
  - https://1.0.0.1/dns-query
  - tls://dns.google
  fallback-filter:
    geoip: true
    geoip-code: CN
    ipcidr:
    - 240.0.0.0/4
proxies:
- name: WARP
  type: wireguard
  server: engage.cloudflareclient.com
  port: 2408
  ip: 172.16.0.2
  ipv6: 2606:4700:110:87c0:ba32:773a:8d44:e353
  private-key: +HpHpY/KjSv5hJdGrN2ok1A6CKhCmTQv5Unwyul9S1g=
  public-key: bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo=
  udp: true
  reserved:
  - 0
  - 0
  - 0
  remote-dns-resolve: true
  dns:
  - 1.1.1.1
  - 8.8.8.8
  dialer-proxy: WARP前置节点
- name: meta_hysteria_01
  type: hysteria
  server: 167.160.90.251
  port: 48089
  auth-str: dongtaiwang.com
  alpn:
  - h3
  protocol: udp
  up: 11 Mbps
  down: 55 Mbps
  skip-cert-verify: true
- name: meta_tuic_02
  server: 109.104.152.219
  port: 11091
  type: tuic
  uuid: 62fc1c08-c2d7-4d35-8cb3-6289b4293679
  password: dongtaiwang.com
  sni: bing.com
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  skip-cert-verify: true
  congestion-controller: bbr
- name: meta_tuic_11
  server: tuic1.freeh1.xyz
  port: 40981
  type: tuic
  uuid: c2faac69-e1c1-4bf5-b8a8-d2ce4d834a66
  password: dongtaiwang
  sni: tuic1.freeh1.xyz
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  skip-cert-verify: false
  congestion-controller: bbr
- name: meta_tuic_21
  server: tuic3.dtku47.xyz
  port: 12255
  type: tuic
  uuid: ed6a538a-6e66-4f21-a769-4b389bb2f3ab
  password: dongtaiwang
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  congestion-controller: bbr
- name: meta_tuic_31
  server: 108.181.24.7
  port: 23450
  type: tuic
  uuid: 3618921b-adeb-4bd3-a2a0-f98b72a674b1
  password: dongtaiwang
  sni: bing.com
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  skip-cert-verify: true
  congestion-controller: bbr
- name: meta_hysteria_41
  type: hysteria
  server: www.dtku46.xyz
  port: 11223
  auth-str: mqoE9qSoyMFa
  alpn:
  - h3
  protocol: udp
  up: 11 Mbps
  down: 55 Mbps
  skip-cert-verify: true
- name: meta_tuic_51
  server: 108.181.22.205
  port: 50987
  type: tuic
  uuid: d6214437-e1b5-4334-9090-8f66b78bea89
  password: dongtaiwang
  sni: bing.com
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  skip-cert-verify: true
  congestion-controller: bbr
- name: meta_tuic_61
  server: 108.181.22.239
  port: 19988
  type: tuic
  uuid: 485ce799-da5f-46e8-a82b-8ef322d8602f
  password: dongtaiwang.com
  sni: bing.com
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  skip-cert-verify: true
  congestion-controller: bbr
- name: meta_tuic_71
  server: 109.104.152.180
  port: 22335
  type: tuic
  uuid: e78e1e93-a648-4974-b544-68f8b9fa0b81
  password: dongtaiwang.com
  sni: bing.com
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  skip-cert-verify: true
  congestion-controller: bb
- name: meta_hysteria_81
  type: hysteria
  server: www.dtku50.xyz
  port: 14751
  sni: www.microsoft.com
  skip-cert-verify: true
  alpn:
  - h3
  protocol: udp
  auth_str: 6qSZyyl4eTT8hqPMQxdhIgpxQfTyW1Oq6GBwQVhA2vBOw7QIGY
  up: 2
  down: 10
- name: meta_hysteria_91
  type: hysteria
  server: 62.204.54.81
  port: 42691
  sni: bing.com
  skip-cert-verify: true
  alpn:
  - h3
  protocol: udp
  auth_str: dongtaiwang.com
  up: 5
  down: 10
- name: hysteria_0
  type: hysteria
  server: 109.104.152.180
  port: 40522
  ports: 40522
  auth_str: dongtaiwang.com
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: www.microsoft.com
  skip-cert-verify: true
  alpn:
  - h3
- name: hysteria_1
  type: hysteria
  server: 173.234.25.52
  port: 20164
  ports: 20164
  auth_str: Ljg6NNEATDqP97hdAdHe1lJv7ggtKc0h7zmCCZKCX3qY0LR64F
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: www.microsoft.com
  skip-cert-verify: true
  alpn:
  - h3
- name: hysteria_2
  type: hysteria
  server: 109.104.152.149
  port: 48406
  ports: 48406
  auth_str: xfNhrunYJ9GvDXCTktY2bIwhc1EyeyyAbiUMx1UtBOWgI4cMVB
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: www.amazon.cn
  skip-cert-verify: true
  alpn:
  - h3
- name: hysteria_3
  type: hysteria
  server: 51.158.54.46
  port: 11926
  ports: 11926
  auth_str: Trz2alKwzCImRAXI3nXfpo1ylpHfqOL8s1vageWKoyjjvWeMVs
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: youku.com
  skip-cert-verify: true
  alpn:
  - h3
proxy-groups:
- name: 节点选择
  type: select
  proxies:
  - WARP
  - 自动选择
  - 负载均衡
  - 手动选择
  - DIRECT
- name: WARP前置节点
  type: select
  proxies:
  - 自动选择
  - 负载均衡
  - 手动选择
- name: 自动选择
  type: url-test
  url: http://www.gstatic.com/generate_204
  interval: 300
  tolerance: 50
  proxies:
  - meta_hysteria_01
  - meta_tuic_02
  - meta_tuic_11
  - meta_tuic_21
  - meta_tuic_31
  - meta_hysteria_41
  - meta_tuic_51
  - meta_tuic_61
  - meta_tuic_71
  - meta_hysteria_81
  - meta_hysteria_91
  - hysteria_0
  - hysteria_1
  - hysteria_2
  - hysteria_3
- name: 手动选择
  type: select
  proxies:
  - meta_hysteria_01
  - meta_tuic_02
  - meta_tuic_11
  - meta_tuic_21
  - meta_tuic_31
  - meta_hysteria_41
  - meta_tuic_51
  - meta_tuic_61
  - meta_tuic_71
  - meta_hysteria_81
  - meta_hysteria_91
  - hysteria_0
  - hysteria_1
  - hysteria_2
  - hysteria_3
- name: 负载均衡
  type: load-balance
  proxies:
  - meta_hysteria_01
  - meta_tuic_02
  - meta_tuic_11
  - meta_tuic_21
  - meta_tuic_31
  - meta_hysteria_41
  - meta_tuic_51
  - meta_tuic_61
  - meta_tuic_71
  - meta_hysteria_81
  - meta_hysteria_91
  - hysteria_0
  - hysteria_1
  - hysteria_2
  - hysteria_3
  url: http://www.gstatic.com/generate_204
  interval: 300
  strategy: round-robin
rules:
- DOMAIN,clash.razord.top,DIRECT
- DOMAIN,yacd.haishan.me,DIRECT
- GEOIP,LAN,DIRECT
- GEOIP,CN,DIRECT
- MATCH,节点选择

```

**含hysteria2节点(节点最全）** (https://mareep.netlify.app/sub/merged_warp_proxies_new.yaml)
```yaml
port: 7890
allow-lan: true
mode: rule
log-level: info
unified-delay: true
global-client-fingerprint: chrome
dns:
  enable: true
  listen: :53
  ipv6: true
  enhanced-mode: fake-ip
  fake-ip-range: 198.18.0.1/16
  default-nameserver:
  - 223.5.5.5
  - 8.8.8.8
  nameserver:
  - https://dns.alidns.com/dns-query
  - https://doh.pub/dns-query
  fallback:
  - https://1.0.0.1/dns-query
  - tls://dns.google
  fallback-filter:
    geoip: true
    geoip-code: CN
    ipcidr:
    - 240.0.0.0/4
proxies:
- name: WARP
  type: wireguard
  server: engage.cloudflareclient.com
  port: 2408
  ip: 172.16.0.2
  ipv6: 2606:4700:110:87c0:ba32:773a:8d44:e353
  private-key: +HpHpY/KjSv5hJdGrN2ok1A6CKhCmTQv5Unwyul9S1g=
  public-key: bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo=
  udp: true
  reserved:
  - 0
  - 0
  - 0
  remote-dns-resolve: true
  dns:
  - 1.1.1.1
  - 8.8.8.8
  dialer-proxy: WARP前置节点
- name: meta_hysteria_01
  type: hysteria
  server: 167.160.90.251
  port: 48089
  auth-str: dongtaiwang.com
  alpn:
  - h3
  protocol: udp
  up: 11 Mbps
  down: 55 Mbps
  skip-cert-verify: true
- name: meta_tuic_02
  server: 109.104.152.219
  port: 11091
  type: tuic
  uuid: 62fc1c08-c2d7-4d35-8cb3-6289b4293679
  password: dongtaiwang.com
  sni: bing.com
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  skip-cert-verify: true
  congestion-controller: bbr
- name: meta_tuic_11
  server: tuic1.freeh1.xyz
  port: 40981
  type: tuic
  uuid: c2faac69-e1c1-4bf5-b8a8-d2ce4d834a66
  password: dongtaiwang
  sni: tuic1.freeh1.xyz
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  skip-cert-verify: false
  congestion-controller: bbr
- name: meta_tuic_21
  server: tuic3.dtku47.xyz
  port: 12255
  type: tuic
  uuid: ed6a538a-6e66-4f21-a769-4b389bb2f3ab
  password: dongtaiwang
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  congestion-controller: bbr
- name: meta_tuic_31
  server: 108.181.24.7
  port: 23450
  type: tuic
  uuid: 3618921b-adeb-4bd3-a2a0-f98b72a674b1
  password: dongtaiwang
  sni: bing.com
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  skip-cert-verify: true
  congestion-controller: bbr
- name: meta_hysteria_41
  type: hysteria
  server: www.dtku46.xyz
  port: 11223
  auth-str: mqoE9qSoyMFa
  alpn:
  - h3
  protocol: udp
  up: 11 Mbps
  down: 55 Mbps
  skip-cert-verify: true
- name: meta_tuic_51
  server: 108.181.22.205
  port: 50987
  type: tuic
  uuid: d6214437-e1b5-4334-9090-8f66b78bea89
  password: dongtaiwang
  sni: bing.com
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  skip-cert-verify: true
  congestion-controller: bbr
- name: meta_tuic_61
  server: 108.181.22.239
  port: 19988
  type: tuic
  uuid: 485ce799-da5f-46e8-a82b-8ef322d8602f
  password: dongtaiwang.com
  sni: bing.com
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  skip-cert-verify: true
  congestion-controller: bbr
- name: meta_tuic_71
  server: 109.104.152.180
  port: 22335
  type: tuic
  uuid: e78e1e93-a648-4974-b544-68f8b9fa0b81
  password: dongtaiwang.com
  sni: bing.com
  alpn:
  - h3
  request-timeout: 8000
  udp-relay-mode: native
  skip-cert-verify: true
  congestion-controller: bb
- name: meta_hysteria_81
  type: hysteria
  server: www.dtku50.xyz
  port: 14751
  sni: www.microsoft.com
  skip-cert-verify: true
  alpn:
  - h3
  protocol: udp
  auth_str: 6qSZyyl4eTT8hqPMQxdhIgpxQfTyW1Oq6GBwQVhA2vBOw7QIGY
  up: 2
  down: 10
- name: meta_hysteria_91
  type: hysteria
  server: 62.204.54.81
  port: 42691
  sni: bing.com
  skip-cert-verify: true
  alpn:
  - h3
  protocol: udp
  auth_str: dongtaiwang.com
  up: 5
  down: 10
- name: hysteria_0
  type: hysteria
  server: 109.104.152.180
  port: 40522
  ports: 40522
  auth_str: dongtaiwang.com
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: www.microsoft.com
  skip-cert-verify: true
  alpn:
  - h3
- name: hysteria_1
  type: hysteria
  server: 173.234.25.52
  port: 20164
  ports: 20164
  auth_str: Ljg6NNEATDqP97hdAdHe1lJv7ggtKc0h7zmCCZKCX3qY0LR64F
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: www.microsoft.com
  skip-cert-verify: true
  alpn:
  - h3
- name: hysteria_2
  type: hysteria
  server: 109.104.152.149
  port: 48406
  ports: 48406
  auth_str: xfNhrunYJ9GvDXCTktY2bIwhc1EyeyyAbiUMx1UtBOWgI4cMVB
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: www.amazon.cn
  skip-cert-verify: true
  alpn:
  - h3
- name: hysteria_3
  type: hysteria
  server: 51.158.54.46
  port: 11926
  ports: 11926
  auth_str: Trz2alKwzCImRAXI3nXfpo1ylpHfqOL8s1vageWKoyjjvWeMVs
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: youku.com
  skip-cert-verify: true
  alpn:
  - h3
- name: hysteria2_0
  type: hysteria2
  server: www.dtku46.xyz
  port: 62580
  password: dongtaiwang.com
  fast-open: true
  sni: www.bing.com
  skip-cert-verify: true
- name: hysteria2_1
  type: hysteria2
  server: 108.181.22.155
  port: 15565
  password: dongtaiwang.com
  fast-open: true
  sni: www.bing.com
  skip-cert-verify: true
- name: hysteria2_3
  type: hysteria2
  server: 108.181.22.155
  port: 15565
  password: dongtaiwang.com
  fast-open: true
  sni: www.bing.com
  skip-cert-verify: true
proxy-groups:
- name: 节点选择
  type: select
  proxies:
  - WARP
  - 自动选择
  - 负载均衡
  - 手动选择
  - DIRECT
- name: WARP前置节点
  type: select
  proxies:
  - 自动选择
  - 负载均衡
  - 手动选择
- name: 自动选择
  type: url-test
  url: http://www.gstatic.com/generate_204
  interval: 300
  tolerance: 50
  proxies:
  - meta_hysteria_01
  - meta_tuic_02
  - meta_tuic_11
  - meta_tuic_21
  - meta_tuic_31
  - meta_hysteria_41
  - meta_tuic_51
  - meta_tuic_61
  - meta_tuic_71
  - meta_hysteria_81
  - meta_hysteria_91
  - hysteria_0
  - hysteria_1
  - hysteria_2
  - hysteria_3
  - hysteria2_0
  - hysteria2_1
  - hysteria2_3
- name: 手动选择
  type: select
  proxies:
  - meta_hysteria_01
  - meta_tuic_02
  - meta_tuic_11
  - meta_tuic_21
  - meta_tuic_31
  - meta_hysteria_41
  - meta_tuic_51
  - meta_tuic_61
  - meta_tuic_71
  - meta_hysteria_81
  - meta_hysteria_91
  - hysteria_0
  - hysteria_1
  - hysteria_2
  - hysteria_3
  - hysteria2_0
  - hysteria2_1
  - hysteria2_3
- name: 负载均衡
  type: load-balance
  proxies:
  - meta_hysteria_01
  - meta_tuic_02
  - meta_tuic_11
  - meta_tuic_21
  - meta_tuic_31
  - meta_hysteria_41
  - meta_tuic_51
  - meta_tuic_61
  - meta_tuic_71
  - meta_hysteria_81
  - meta_hysteria_91
  - hysteria_0
  - hysteria_1
  - hysteria_2
  - hysteria_3
  - hysteria2_0
  - hysteria2_1
  - hysteria2_3
  url: http://www.gstatic.com/generate_204
  interval: 300
  strategy: round-robin
rules:
- DOMAIN,clash.razord.top,DIRECT
- DOMAIN,yacd.haishan.me,DIRECT
- GEOIP,LAN,DIRECT
- GEOIP,CN,DIRECT
- MATCH,节点选择

```

## 通用链接 （shadowrocket和nekoray）  (https://mareep.netlify.app/sub/shadowrocket_base64.txt)
```txt
aHlzdGVyaWE6Ly8xNjcuMTYwLjkwLjI1MTo0ODA4OT9wZWVyPSZhdXRoPWRvbmd0YWl3YW5nLmNvbSZpbnNlY3VyZT0xJnVwbWJwcz01MCZkb3dubWJwcz04MCZhbHBuPWgzJm1wb3J0PTQ4MDg5Jm9iZnM9JnByb3RvY29sPXVkcCZmYXN0b3Blbj0xI2h5c3RlcmlhX21ldGFfMAp0dWljOi8vNjJmYzFjMDgtYzJkNy00ZDM1LThjYjMtNjI4OWI0MjkzNjc5OmRvbmd0YWl3YW5nLmNvbUAxMDkuMTA0LjE1Mi4yMTk6MTEwOTE/c25pPWJpbmcuY29tJmNvbmdlc3Rpb25fY29udHJvbD1iYnImdWRwX3JlbGF5X21vZGU9bmF0aXZlJmFscG49aDMmYWxsb3dfaW5zZWN1cmU9MQp0dWljOi8vYzJmYWFjNjktZTFjMS00YmY1LWI4YTgtZDJjZTRkODM0YTY2OmRvbmd0YWl3YW5nQHR1aWMxLmZyZWVoMS54eXo6NDA5ODE/c25pPXR1aWMxLmZyZWVoMS54eXomY29uZ2VzdGlvbl9jb250cm9sPWJiciZ1ZHBfcmVsYXlfbW9kZT1uYXRpdmUmYWxwbj1oMyZhbGxvd19pbnNlY3VyZT0wCnR1aWM6Ly9lZDZhNTM4YS02ZTY2LTRmMjEtYTc2OS00YjM4OWJiMmYzYWI6ZG9uZ3RhaXdhbmdAdHVpYzMuZHRrdTQ3Lnh5ejoxMjI1NT9zbmk9JmNvbmdlc3Rpb25fY29udHJvbD1iYnImdWRwX3JlbGF5X21vZGU9bmF0aXZlJmFscG49aDMmYWxsb3dfaW5zZWN1cmU9MAp0dWljOi8vMzYxODkyMWItYWRlYi00YmQzLWEyYTAtZjk4YjcyYTY3NGIxOmRvbmd0YWl3YW5nQDEwOC4xODEuMjQuNzoyMzQ1MD9zbmk9YmluZy5jb20mY29uZ2VzdGlvbl9jb250cm9sPWJiciZ1ZHBfcmVsYXlfbW9kZT1uYXRpdmUmYWxwbj1oMyZhbGxvd19pbnNlY3VyZT0xCmh5c3RlcmlhOi8vd3d3LmR0a3U0Ni54eXo6MTEyMjM/cGVlcj0mYXV0aD1tcW9FOXFTb3lNRmEmaW5zZWN1cmU9MSZ1cG1icHM9NTAmZG93bm1icHM9ODAmYWxwbj1oMyZtcG9ydD0xMTIyMyZvYmZzPSZwcm90b2NvbD11ZHAmZmFzdG9wZW49MSNoeXN0ZXJpYV9tZXRhXzQKdHVpYzovL2Q2MjE0NDM3LWUxYjUtNDMzNC05MDkwLThmNjZiNzhiZWE4OTpkb25ndGFpd2FuZ0AxMDguMTgxLjIyLjIwNTo1MDk4Nz9zbmk9YmluZy5jb20mY29uZ2VzdGlvbl9jb250cm9sPWJiciZ1ZHBfcmVsYXlfbW9kZT1uYXRpdmUmYWxwbj1oMyZhbGxvd19pbnNlY3VyZT0xCnR1aWM6Ly80ODVjZTc5OS1kYTVmLTQ2ZTgtYTgyYi04ZWYzMjJkODYwMmY6ZG9uZ3RhaXdhbmcuY29tQDEwOC4xODEuMjIuMjM5OjE5OTg4P3NuaT1iaW5nLmNvbSZjb25nZXN0aW9uX2NvbnRyb2w9YmJyJnVkcF9yZWxheV9tb2RlPW5hdGl2ZSZhbHBuPWgzJmFsbG93X2luc2VjdXJlPTEKdHVpYzovL2U3OGUxZTkzLWE2NDgtNDk3NC1iNTQ0LTY4ZjhiOWZhMGI4MTpkb25ndGFpd2FuZy5jb21AMTA5LjEwNC4xNTIuMTgwOjIyMzM1P3NuaT1iaW5nLmNvbSZjb25nZXN0aW9uX2NvbnRyb2w9YmImdWRwX3JlbGF5X21vZGU9bmF0aXZlJmFscG49aDMmYWxsb3dfaW5zZWN1cmU9MQpoeXN0ZXJpYTovL3d3dy5kdGt1NTAueHl6OjE0NzUxP3BlZXI9d3d3Lm1pY3Jvc29mdC5jb20mYXV0aD0maW5zZWN1cmU9MSZ1cG1icHM9NTAmZG93bm1icHM9ODAmYWxwbj1oMyZtcG9ydD0xNDc1MSZvYmZzPSZwcm90b2NvbD11ZHAmZmFzdG9wZW49MSNoeXN0ZXJpYV9tZXRhXzgKaHlzdGVyaWE6Ly82Mi4yMDQuNTQuODE6NDI2OTE/cGVlcj1iaW5nLmNvbSZhdXRoPSZpbnNlY3VyZT0xJnVwbWJwcz01MCZkb3dubWJwcz04MCZhbHBuPWgzJm1wb3J0PTQyNjkxJm9iZnM9JnByb3RvY29sPXVkcCZmYXN0b3Blbj0xI2h5c3RlcmlhX21ldGFfOQphSFIwY0hNNkx5OWtiMjVuZEdGcGQyRnVaeTVqYjIwNlpHOXVaM1JoYVhkaGJtY3VZMjl0UUc1aGFYWmxNVFl1WTJaalpHNHpMbmg1ZWpvME5ETT0KYUhSMGNITTZMeTlrYjI1bmRHRnBkMkZ1Wnk1amIyMDZaRzl1WjNSaGFYZGhibWN1WTI5dFFHNWhhWFpsTVRRdVkyWmpaRzR6TG5oNWVqbzBORE09Cmh5c3RlcmlhOi8vMTA5LjEwNC4xNTIuMTgwOjQwNTIyP3BlZXI9d3d3Lm1pY3Jvc29mdC5jb20mYXV0aD1kb25ndGFpd2FuZy5jb20maW5zZWN1cmU9MSZ1cG1icHM9MTEmZG93bm1icHM9NTUmYWxwbj1oMyZvYmZzPSZwcm90b2NvbD11ZHAmZmFzdG9wZW49MSNoeXN0ZXJpYV8wCmh5c3RlcmlhOi8vMTczLjIzNC4yNS41MjoyMDE2ND9wZWVyPXd3dy5taWNyb3NvZnQuY29tJmF1dGg9TGpnNk5ORUFURHFQOTdoZEFkSGUxbEp2N2dndEtjMGg3em1DQ1pLQ1gzcVkwTFI2NEYmaW5zZWN1cmU9MSZ1cG1icHM9MTEmZG93bm1icHM9NTUmYWxwbj1oMyZvYmZzPSZwcm90b2NvbD11ZHAmZmFzdG9wZW49MSNoeXN0ZXJpYV8xCmh5c3RlcmlhOi8vMTA5LjEwNC4xNTIuMTQ5OjQ4NDA2P3BlZXI9d3d3LmFtYXpvbi5jbiZhdXRoPXhmTmhydW5ZSjlHdkRYQ1RrdFkyYkl3aGMxRXlleXlBYmlVTXgxVXRCT1dnSTRjTVZCJmluc2VjdXJlPTEmdXBtYnBzPTExJmRvd25tYnBzPTU1JmFscG49aDMmb2Jmcz0mcHJvdG9jb2w9dWRwJmZhc3RvcGVuPTEjaHlzdGVyaWFfMgpoeXN0ZXJpYTovLzUxLjE1OC41NC40NjoxMTkyNj9wZWVyPXlvdWt1LmNvbSZhdXRoPVRyejJhbEt3ekNJbVJBWEkzblhmcG8xeWxwSGZxT0w4czF2YWdlV0tveWpqdldlTVZzJmluc2VjdXJlPTEmdXBtYnBzPTExJmRvd25tYnBzPTU1JmFscG49aDMmb2Jmcz0mcHJvdG9jb2w9dWRwJmZhc3RvcGVuPTEjaHlzdGVyaWFfMwpoeXN0ZXJpYTI6Ly9kb25ndGFpd2FuZy5jb21Ad3d3LmR0a3U0Ni54eXo6NjI1ODA/aW5zZWN1cmU9MSZzbmk9d3d3LmJpbmcuY29tI2h5c3RlcmlhMl8wCmh5c3RlcmlhMjovL2Rvbmd0YWl3YW5nLmNvbUAxMDguMTgxLjIyLjE1NToxNTU2NT9pbnNlY3VyZT0xJnNuaT13d3cuYmluZy5jb20jaHlzdGVyaWEyXzEKaHlzdGVyaWEyOi8vZG9uZ3RhaXdhbmcuY29tQDE2Ny4xNjAuOTAuMjUyOjYzNTMwP2luc2VjdXJlPTEmc25pPXd3dy5iaW5nLmNvbSNoeXN0ZXJpYTJfMgpoeXN0ZXJpYTI6Ly9kb25ndGFpd2FuZy5jb21AMTA4LjE4MS4yMi4xNTU6MTU1NjU/aW5zZWN1cmU9MSZzbmk9d3d3LmJpbmcuY29tI2h5c3RlcmlhMl8zCnZsZXNzOi8vMDc3MzI1NmMtZDAyMC00MzZkLWFmZWEtNmVlZTdjYjZjODcyQGRvbmd0YWl3YW5nMy5jb206NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlPTAmZmxvdz0mdHlwZT13cyZmcD1jaHJvbWUmcGJrPSZzaWQ9JnNuaT14cmF5MS5mcmVlZ3JhZGVseS54eXomc2VydmljZU5hbWU9JnBhdGg9L2JvZGh3cyZob3N0PXhyYXkxLmZyZWVncmFkZWx5Lnh5eiN2bGVzc18wCnZsZXNzOi8vZjVjMTgwZWItZmJjZS00OWFjLTkwMjktNDgyZWNhOTM4NWMwQGRvbmd0YWl3YW5nMi5jb206NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlPTAmZmxvdz0mdHlwZT13cyZmcD1jaHJvbWUmcGJrPSZzaWQ9JnNuaT14cmF5MS5mcmVlaDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS9nem9nd3MmaG9zdD14cmF5MS5mcmVlaDEueHl6I3ZsZXNzXzEKdmxlc3M6Ly9mNWMxODBlYi1mYmNlLTQ5YWMtOTAyOS00ODJlY2E5Mzg1YzBAZG9uZ3RhaXdhbmcyLmNvbTo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmU9MCZmbG93PSZ0eXBlPXdzJmZwPWNocm9tZSZwYms9JnNpZD0mc25pPXhyYXkxLmZyZWVoMS54eXomc2VydmljZU5hbWU9JnBhdGg9L2d6b2d3cyZob3N0PXhyYXkxLmZyZWVoMS54eXojdmxlc3NfMgp2bGVzczovL2Y1YzE4MGViLWZiY2UtNDlhYy05MDI5LTQ4MmVjYTkzODVjMEBkb25ndGFpd2FuZzMuY29tOjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZT0wJmZsb3c9JnR5cGU9d3MmZnA9Y2hyb21lJnBiaz0mc2lkPSZzbmk9eHJheTEuZnJlZWgxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vZ3pvZ3dzJmhvc3Q9eHJheTEuZnJlZWgxLnh5eiN2bGVzc18z
```

## sing-box订阅链接 (https://sing-box-subscribe.vercel.app/config/https:/mareep.netlify.app/sub/merged_proxies_new.yaml)
```yaml
None
```


