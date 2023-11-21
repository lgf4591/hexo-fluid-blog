
---
title: VPN合集 
date: 2023-11-21 13:26:49
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

> Last Update Time: 2023-11-21 13:26:49
---
# vless_node
```bash

None

```

# CloudFlare优质IP
```bash

电信162.159.153.216
电信172.67.205.16
电信172.64.132.74

联通162.159.130.237
联通172.67.67.118
联通172.67.125.190

移动172.67.166.159
移动172.64.160.196
移动172.67.67.170



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
140.82.114.25                 alive.github.com
140.82.113.5                  api.github.com
185.199.110.153               assets-cdn.github.com
185.199.110.133               avatars.githubusercontent.com
185.199.108.133               avatars0.githubusercontent.com
185.199.110.133               avatars1.githubusercontent.com
185.199.108.133               avatars2.githubusercontent.com
185.199.108.133               avatars3.githubusercontent.com
185.199.108.133               avatars4.githubusercontent.com
185.199.108.133               avatars5.githubusercontent.com
185.199.110.133               camo.githubusercontent.com
140.82.112.22                 central.github.com
185.199.108.133               cloud.githubusercontent.com
140.82.114.9                  codeload.github.com
140.82.114.21                 collector.github.com
185.199.108.133               desktop.githubusercontent.com
185.199.108.133               favicons.githubusercontent.com
140.82.113.3                  gist.github.com
54.231.196.49                 github-cloud.s3.amazonaws.com
52.216.40.233                 github-com.s3.amazonaws.com
52.217.49.196                 github-production-release-asset-2e65be.s3.amazonaws.com
16.182.72.249                 github-production-repository-file-5c1aeb.s3.amazonaws.com
52.216.59.25                  github-production-user-asset-6210df.s3.amazonaws.com
192.0.66.2                    github.blog
140.82.114.3                  github.com
140.82.112.18                 github.community
185.199.109.154               github.githubassets.com
151.101.193.194               github.global.ssl.fastly.net
185.199.110.153               github.io
185.199.108.133               github.map.fastly.net
185.199.110.153               githubstatus.com
140.82.114.25                 live.github.com
185.199.110.133               media.githubusercontent.com
185.199.108.133               objects.githubusercontent.com
13.107.42.16                  pipelines.actions.githubusercontent.com
185.199.108.133               raw.githubusercontent.com
185.199.108.133               user-images.githubusercontent.com
13.107.213.40                 vscode.dev
140.82.113.22                 education.github.com


# Update time: 2023-11-21T20:07:26+08:00
# Update url: https://raw.hellogithub.com/hosts
# Star me: https://github.com/521xueweihan/GitHub520
# GitHub520 Host End

```

该内容会自动定时更新， 数据更新时间：2023-11-21T20:07:26+08:00

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
更新时间 2023-11-21 20:00  
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
vmess://eyJhZGQiOiAibmJxMTEubnRicS5keW51Lm5ldCIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNmJiZTMwMTQtOWZjZS00NzAwLTliMzktYWRjMmJkNjU3ZjYzIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9iMTEiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1M2YwXHU2ZTdlXHU3NzAxXHU0ZTJkXHU1MzRlXHU3NTM1XHU0ZmUxKEhpTmV0KVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAxIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=  
vmess://eyJhZGQiOiAibmJxMTEubnRicS5keW51Lm5ldCIsICJhaWQiOiAwLCAiaG9zdCI6ICJuYnExMS5udGJxLmR5bnUubmV0IiwgImlkIjogIjQ0MjA5ZTE0LTJhY2YtNGQ2Mi1hYzA2LTVmN2ZlNDNlMzU5MSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvYjExIiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTNmMFx1NmU3ZVx1NzcwMVx1NGUyZFx1NTM0ZVx1NzUzNVx1NGZlMShIaU5ldClcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIm5icTExLm50YnEuZHludS5uZXQifQ==  
vmess://eyJhZGQiOiAibmJxMTMubnRicS5keW51Lm5ldCIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiMzhmZjk5ZDgtZGJhZi00MzBhLTg2N2UtMjAwYjg5ZjRjNzBhIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9iMTMiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1M2YwXHU2ZTdlXHU3NzAxXHU0ZTJkXHU1MzRlXHU3NTM1XHU0ZmUxKEhpTmV0KVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAzIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAibmJxMTMubnRicS5keW51Lm5ldCJ9  
vmess://eyJhZGQiOiAiYjI0Lm50YnEuZHludS5uZXQiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiYjI0Lm50YnEuZHludS5uZXQiLCAiaWQiOiAiYTlhMzdmNzktMjMxYy00YjU3LTg0OWQtMzcxN2MxYjU2MWI0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9iMjQiLCAicG9ydCI6ICI0NDMiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDFcdTRlMmRcdTUzNGVcdTc1MzVcdTRmZTEoSGlOZXQpXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDQiLCAic2N5IjogImF1dG8iLCAic25pIjogImIyNC5udGJxLmR5bnUubmV0IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDFcdTY1YjBcdTUzMTdcdTVlMDJcdTRlMmRcdTUzNGVcdTc1MzVcdTRmZTEgNSIsICJhZGQiOiAiYjIxLm50YnEuZHludS5uZXQiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiNmJkNDc0MzgtZDY5Ni00OTlhLWJjZDUtMTM0ZTQxNDUxMzVhIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJiMjEubnRicS5keW51Lm5ldCIsICJwYXRoIjogIi9iMjEiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=  
vmess://eyJhZGQiOiAiMTEyLjI5Ljk0LjIzIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiMjFhOWJmZjItNzJkZS00ZTYyLTkzZmYtOGIxNTlmNjZkODc1IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ5MjI2LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTViODlcdTVmYmRcdTc3MDFcdTU0MDhcdTgwYTVcdTVlMDJcdTc5ZmJcdTUyYTggNiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9  
vmess://eyJhZGQiOiAibmJxMTIubnRicS5keW51Lm5ldCIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNmJkNDc0MzgtZDY5Ni00OTlhLWJjZDUtMTM0ZTQxNDUxMzVhIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9iMTIiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1M2YwXHU2ZTdlXHU3NzAxXHU0ZTJkXHU1MzRlXHU3NTM1XHU0ZmUxKEhpTmV0KVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA3IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAibmJxMTIubnRicS5keW51Lm5ldCJ9  
vmess://eyJhZGQiOiAiMTQyLjQuOTcuNjUiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlUEVHIFRFQ0ggOCIsICJwb3J0IjogMzAwMDAsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIiIsICJob3N0IjogInd3dy4zOTgzODI2Ni54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk5NjI0NzIzMjEzIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAic2N5IjogIiJ9  
vmess://eyJhZGQiOiAibmJxMTIubnRicS5keW51Lm5ldCIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiYjNkNDNhMGItOWVmOC00Zjg3LWE1YzYtOGRhMDYyZTAyNjIwIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9iMTIiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1M2YwXHU2ZTdlXHU3NzAxXHU0ZTJkXHU1MzRlXHU3NTM1XHU0ZmUxKEhpTmV0KVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA5IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAibmJxMTIubnRicS5keW51Lm5ldCJ9  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDFcdTUzZjBcdTUzMTdcdTVlMDJcdTRlMmRcdTUzNGVcdTc1MzVcdTRmZTEgMTAiLCAiYWRkIjogImIyMi5udGJxLmR5bnUubmV0IiwgInBvcnQiOiA0NDMsICJpZCI6ICJiMWZkNzg0NC00Yzk1LTQzMTYtOWExNS1jN2I0MTVlOWQ4NGMiLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogImIyMi5udGJxLmR5bnUubmV0IiwgInBhdGgiOiAiL2IyMiIsICJ0bHMiOiAidGxzIn0=  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDFcdTRlMmRcdTUzNGVcdTc1MzVcdTRmZTEoSGlOZXQpXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDExIiwgImFkZCI6ICJiMjQubnRicS5keW51Lm5ldCIsICJwb3J0IjogNDQzLCAiaWQiOiAiYjFmZDc4NDQtNGM5NS00MzE2LTlhMTUtYzdiNDE1ZTlkODRjIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJiMjQubnRicS5keW51Lm5ldCIsICJwYXRoIjogIi9iMjQiLCAidGxzIjogInRscyJ9  
vmess://eyJhZGQiOiAiOTUuMTY0LjM3LjE1IiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogInVrMS12bWVzcy5ncmVlbnNzaC54eXoiLCAiaWQiOiAiYjVhYWZlOGMtMzUyNy00NTAyLThhZGQtOWNhNzQxN2NmYzg4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi92bWVzcyIsICJwb3J0IjogIjgwIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU0ZTRjXHU1MTRiXHU1MTcwICAxMiIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=  
vmess://eyJhZGQiOiAiMzYuMTQxLjQwLjU5IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDM0OTk2LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzMTdcdTRlYWNcdTVlMDJcdTc5ZmJcdTUyYTggMTMiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE0IiwgImFkZCI6ICJ3d3cud3RvLm9yZyIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICJhZjI4Yzg1ZC1lMTJkLTQxZjEtYmYwNS1kMGEyNzRmYWU3NDkiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInN0YXJzbWVyY2hhbnQtd2lkZS1jdWx0dXJlLWdhcmxpYy50cnljbG91ZGZsYXJlLmNvbSIsICJwYXRoIjogImFmMjhjODVkLWUxMmQtNDFmMS1iZjA1LWQwYTI3NGZhZTc0OS12bSIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==  
vmess://eyJhZGQiOiAiMTU0Ljg1LjEuMTMwIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE2OTg4NDM1NTU0MDAiLCAicG9ydCI6IDMwMDAwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTUiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE2IiwgImFkZCI6ICI1NmM1ZDJiMS01NzVmLTQ3MTgtYWQzNy00Y2IxZmIwZDQ0ZGMuYXNvdWwtZGlhbmEueHl6IiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjVmNzI2ZmUzLWQ4MmUtNGRhNS1hNzExLThhZjBjYmIyYjY4MiIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiNTZjNWQyYjEtNTc1Zi00NzE4LWFkMzctNGNiMWZiMGQ0NGRjLmFzb3VsLWRpYW5hLnh5eiIsICJwYXRoIjogIi9henVtYXNlLnJlbiIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDFcdTY1YjBcdTUzMTdcdTVlMDJcdTRlMmRcdTUzNGVcdTc1MzVcdTRmZTEgMTciLCAiYWRkIjogImIyMS5udGJxLmR5bnUubmV0IiwgInBvcnQiOiA0NDMsICJpZCI6ICIzOGZmOTlkOC1kYmFmLTQzMGEtODY3ZS0yMDBiODlmNGM3MGEiLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogImIyMS5udGJxLmR5bnUubmV0IiwgInBhdGgiOiAiL2IyMSIsICJ0bHMiOiAidGxzIn0=  
ss://YWVzLTI1Ni1nY206WTZSOXBBdHZ4eHptR0M@54.36.174.181:5601#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2018  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE5IiwgImFkZCI6ICJjYzIuc2hhYmlqaWNoYW5nLmNvbSIsICJwb3J0IjogIjgwIiwgImlkIjogIjU2Mjc4YTFhLWM3Y2MtNDU5Zi1iMDBjLTMwMzdlNGY5OTU5MCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiY2MyLnNoYWJpamljaGFuZy5jb20iLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggMjAiLCAiYWRkIjogIjE4My4yMzMuMTg3LjIxNCIsICJwb3J0IjogIjMwOTcyIiwgImlkIjogIjc3MGVlNzMwLTI0NTAtNGUzYy1hNmM2LTM5MzJiZDMyYWZiZCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=  
vmess://eyJhZGQiOiAibmJxMTIubnRicS5keW51Lm5ldCIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNjE1MmRhYjItNWEwOS00NGZlLTljMTQtM2VjZTlkYmJjNGI4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9iMTIiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1M2YwXHU2ZTdlXHU3NzAxXHU0ZTJkXHU1MzRlXHU3NTM1XHU0ZmUxKEhpTmV0KVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAyMSIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9  
vmess://eyJhZGQiOiAibmJxMTEubnRicS5keW51Lm5ldCIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiYjkxZTJlNWMtNDdjZC00Y2IxLWJmZjMtZjRhMDYzYzJiZmQ3IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9iMTEiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1M2YwXHU2ZTdlXHU3NzAxXHU0ZTJkXHU1MzRlXHU3NTM1XHU0ZmUxKEhpTmV0KVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAyMiIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIm5icTExLm50YnEuZHludS5uZXQifQ==  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDFcdTRlMmRcdTUzNGVcdTc1MzVcdTRmZTEoSGlOZXQpXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDIzIiwgImFkZCI6ICJuYnExMy5udGJxLmR5bnUubmV0IiwgInBvcnQiOiAiNDQzIiwgImlkIjogImIzZDQzYTBiLTllZjgtNGY4Ny1hNWM2LThkYTA2MmUwMjYyMCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAibmJxMTMubnRicS5keW51Lm5ldCIsICJwYXRoIjogIi9iMTMiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=  
ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@54.36.174.181:7306#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2024  
ss://YWVzLTI1Ni1nY206WTZSOXBBdHZ4eHptR0M@54.36.174.181:3389#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2025  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDI2IiwgImFkZCI6ICJjZjIub3BlbnhhaS5saW5rIiwgInBvcnQiOiAiODA4MCIsICJpZCI6ICJmNDQwNTI3ZS01MjQzLTRjYTgtODkwYy01ZTA1ZTRiM2JiNDEiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImV1MS5vcGVueGFpLmxpbmsiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDI3IiwgImFkZCI6ICJjZjIub3BlbnhhaS5saW5rIiwgInBvcnQiOiAiODA4MCIsICJpZCI6ICI0NzM5NmY5Yy0zNjVkLTRiOTktYWQxZi1mNzkyNzE2NGI0YzUiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImV1My5vcGVueGFpLmxpbmsiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9  
vmess://eyJhZGQiOiAibmJxMTMubnRicS5keW51Lm5ldCIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiZDZiYzUzOGQtMjQ5Ni00ODE4LWIxNjAtMmQ1ODc1YmE5YTkxIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9iMTMiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1M2YwXHU2ZTdlXHU3NzAxXHU0ZTJkXHU1MzRlXHU3NTM1XHU0ZmUxKEhpTmV0KVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAyOCIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIm5icTEzLm50YnEuZHludS5uZXQifQ==  
ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@www.outline.network.ak1941.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou:7001#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2029  
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
- name: meta_hysteria_02
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
- name: meta_hysteria_71
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
- name: meta_hysteria_81
  type: hysteria
  server: 62.204.54.81
  port: 37899
  sni: www.microsoft.com
  skip-cert-verify: true
  alpn:
  - h3
  protocol: udp
  auth_str: OdHFS3zC3HlSYJmc0GLQNKLAlwDbJqEmonVBXmI07T0Ojb1bQB
  up: 5
  down: 10
- name: meta_hysteria_91
  type: hysteria
  server: www3.dtku49.xyz
  port: 58693
  sni: bing.com
  skip-cert-verify: true
  alpn:
  - h3
  protocol: udp
  auth_str: nbdyVMqucpFMmyRiwcRQFI7EeKzJWjPYuks3ZzEhCv6HjeZvbh
  up: 11
  down: 55
- name: hysteria_0
  type: hysteria
  server: 109.104.152.180
  port: 64502
  ports: 64502
  auth_str: kxeFKpB8fhGjP7cO7NNgXYr19ZsqKQMco612ZCfXiaJrojw571
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: bing.com
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
  - meta_hysteria_02
  - meta_tuic_11
  - meta_tuic_21
  - meta_tuic_31
  - meta_hysteria_41
  - meta_tuic_51
  - meta_tuic_61
  - meta_hysteria_71
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
  - meta_hysteria_02
  - meta_tuic_11
  - meta_tuic_21
  - meta_tuic_31
  - meta_hysteria_41
  - meta_tuic_51
  - meta_tuic_61
  - meta_hysteria_71
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
- name: meta_hysteria2_01
  type: hysteria2
  server: 109.104.152.219
  port: 22309
  password: dongtaiwang.com
  alpn:
  - h3
  sni: bing.com
  skip-cert-verify: true
  up: 100 Mbps
  down: 100 Mbps
- name: meta_hysteria_02
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
- name: meta_hysteria_71
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
- name: meta_hysteria_81
  type: hysteria
  server: 62.204.54.81
  port: 37899
  sni: www.microsoft.com
  skip-cert-verify: true
  alpn:
  - h3
  protocol: udp
  auth_str: OdHFS3zC3HlSYJmc0GLQNKLAlwDbJqEmonVBXmI07T0Ojb1bQB
  up: 5
  down: 10
- name: meta_hysteria_91
  type: hysteria
  server: www3.dtku49.xyz
  port: 58693
  sni: bing.com
  skip-cert-verify: true
  alpn:
  - h3
  protocol: udp
  auth_str: nbdyVMqucpFMmyRiwcRQFI7EeKzJWjPYuks3ZzEhCv6HjeZvbh
  up: 11
  down: 55
- name: hysteria_0
  type: hysteria
  server: 109.104.152.180
  port: 64502
  ports: 64502
  auth_str: kxeFKpB8fhGjP7cO7NNgXYr19ZsqKQMco612ZCfXiaJrojw571
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: bing.com
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
  port: 49730
  password: dongtaiwang.com
  fast-open: true
  sni: www.bing.com
  skip-cert-verify: true
- name: hysteria2_1
  type: hysteria2
  server: 108.181.22.155
  port: 44141
  password: dongtaiwang.com
  fast-open: true
  sni: www.bing.com
  skip-cert-verify: true
- name: hysteria2_2
  type: hysteria2
  server: www.dtku48.xyz
  port: 26806
  password: dongtaiwang.com
  fast-open: true
  sni: www.bing.com
  skip-cert-verify: true
- name: hysteria2_3
  type: hysteria2
  server: 108.181.22.155
  port: 44141
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
  - meta_hysteria2_01
  - meta_hysteria_02
  - meta_tuic_11
  - meta_tuic_21
  - meta_tuic_31
  - meta_hysteria_41
  - meta_tuic_51
  - meta_tuic_61
  - meta_hysteria_71
  - meta_hysteria_81
  - meta_hysteria_91
  - hysteria_0
  - hysteria_1
  - hysteria_2
  - hysteria_3
  - hysteria2_0
  - hysteria2_1
  - hysteria2_2
  - hysteria2_3
- name: 自动选择
  type: url-test
  url: http://www.gstatic.com/generate_204
  interval: 300
  tolerance: 50
  proxies:
  - meta_hysteria2_01
  - meta_hysteria_02
  - meta_tuic_11
  - meta_tuic_21
  - meta_tuic_31
  - meta_hysteria_41
  - meta_tuic_51
  - meta_tuic_61
  - meta_hysteria_71
  - meta_hysteria_81
  - meta_hysteria_91
  - hysteria_0
  - hysteria_1
  - hysteria_2
  - hysteria_3
  - hysteria2_0
  - hysteria2_1
  - hysteria2_2
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
- name: meta_hysteria_02
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
- name: meta_hysteria_71
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
- name: meta_hysteria_81
  type: hysteria
  server: 62.204.54.81
  port: 37899
  sni: www.microsoft.com
  skip-cert-verify: true
  alpn:
  - h3
  protocol: udp
  auth_str: OdHFS3zC3HlSYJmc0GLQNKLAlwDbJqEmonVBXmI07T0Ojb1bQB
  up: 5
  down: 10
- name: meta_hysteria_91
  type: hysteria
  server: www3.dtku49.xyz
  port: 58693
  sni: bing.com
  skip-cert-verify: true
  alpn:
  - h3
  protocol: udp
  auth_str: nbdyVMqucpFMmyRiwcRQFI7EeKzJWjPYuks3ZzEhCv6HjeZvbh
  up: 11
  down: 55
- name: hysteria_0
  type: hysteria
  server: 109.104.152.180
  port: 64502
  ports: 64502
  auth_str: kxeFKpB8fhGjP7cO7NNgXYr19ZsqKQMco612ZCfXiaJrojw571
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: bing.com
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
  - meta_hysteria_02
  - meta_tuic_11
  - meta_tuic_21
  - meta_tuic_31
  - meta_hysteria_41
  - meta_tuic_51
  - meta_tuic_61
  - meta_hysteria_71
  - meta_hysteria_81
  - meta_hysteria_91
  - hysteria_0
  - hysteria_1
  - hysteria_2
  - hysteria_3
- name: 手动选择
  type: select
  proxies:
  - meta_hysteria_02
  - meta_tuic_11
  - meta_tuic_21
  - meta_tuic_31
  - meta_hysteria_41
  - meta_tuic_51
  - meta_tuic_61
  - meta_hysteria_71
  - meta_hysteria_81
  - meta_hysteria_91
  - hysteria_0
  - hysteria_1
  - hysteria_2
  - hysteria_3
- name: 负载均衡
  type: load-balance
  proxies:
  - meta_hysteria_02
  - meta_tuic_11
  - meta_tuic_21
  - meta_tuic_31
  - meta_hysteria_41
  - meta_tuic_51
  - meta_tuic_61
  - meta_hysteria_71
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
- name: meta_hysteria2_01
  type: hysteria2
  server: 109.104.152.219
  port: 22309
  password: dongtaiwang.com
  alpn:
  - h3
  sni: bing.com
  skip-cert-verify: true
  up: 100 Mbps
  down: 100 Mbps
- name: meta_hysteria_02
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
- name: meta_hysteria_71
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
- name: meta_hysteria_81
  type: hysteria
  server: 62.204.54.81
  port: 37899
  sni: www.microsoft.com
  skip-cert-verify: true
  alpn:
  - h3
  protocol: udp
  auth_str: OdHFS3zC3HlSYJmc0GLQNKLAlwDbJqEmonVBXmI07T0Ojb1bQB
  up: 5
  down: 10
- name: meta_hysteria_91
  type: hysteria
  server: www3.dtku49.xyz
  port: 58693
  sni: bing.com
  skip-cert-verify: true
  alpn:
  - h3
  protocol: udp
  auth_str: nbdyVMqucpFMmyRiwcRQFI7EeKzJWjPYuks3ZzEhCv6HjeZvbh
  up: 11
  down: 55
- name: hysteria_0
  type: hysteria
  server: 109.104.152.180
  port: 64502
  ports: 64502
  auth_str: kxeFKpB8fhGjP7cO7NNgXYr19ZsqKQMco612ZCfXiaJrojw571
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: bing.com
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
  port: 49730
  password: dongtaiwang.com
  fast-open: true
  sni: www.bing.com
  skip-cert-verify: true
- name: hysteria2_1
  type: hysteria2
  server: 108.181.22.155
  port: 44141
  password: dongtaiwang.com
  fast-open: true
  sni: www.bing.com
  skip-cert-verify: true
- name: hysteria2_2
  type: hysteria2
  server: www.dtku48.xyz
  port: 26806
  password: dongtaiwang.com
  fast-open: true
  sni: www.bing.com
  skip-cert-verify: true
- name: hysteria2_3
  type: hysteria2
  server: 108.181.22.155
  port: 44141
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
  - meta_hysteria2_01
  - meta_hysteria_02
  - meta_tuic_11
  - meta_tuic_21
  - meta_tuic_31
  - meta_hysteria_41
  - meta_tuic_51
  - meta_tuic_61
  - meta_hysteria_71
  - meta_hysteria_81
  - meta_hysteria_91
  - hysteria_0
  - hysteria_1
  - hysteria_2
  - hysteria_3
  - hysteria2_0
  - hysteria2_1
  - hysteria2_2
  - hysteria2_3
- name: 手动选择
  type: select
  proxies:
  - meta_hysteria2_01
  - meta_hysteria_02
  - meta_tuic_11
  - meta_tuic_21
  - meta_tuic_31
  - meta_hysteria_41
  - meta_tuic_51
  - meta_tuic_61
  - meta_hysteria_71
  - meta_hysteria_81
  - meta_hysteria_91
  - hysteria_0
  - hysteria_1
  - hysteria_2
  - hysteria_3
  - hysteria2_0
  - hysteria2_1
  - hysteria2_2
  - hysteria2_3
- name: 负载均衡
  type: load-balance
  proxies:
  - meta_hysteria2_01
  - meta_hysteria_02
  - meta_tuic_11
  - meta_tuic_21
  - meta_tuic_31
  - meta_hysteria_41
  - meta_tuic_51
  - meta_tuic_61
  - meta_hysteria_71
  - meta_hysteria_81
  - meta_hysteria_91
  - hysteria_0
  - hysteria_1
  - hysteria_2
  - hysteria_3
  - hysteria2_0
  - hysteria2_1
  - hysteria2_2
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
aHlzdGVyaWEyOi8vZG9uZ3RhaXdhbmcuY29tQDEwOS4xMDQuMTUyLjIxOToyMjMwOT9pbnNlY3VyZT0xJnNuaT1iaW5nLmNvbSZvYmZzPSZvYmZzLXBhc3N3b3JkPSNoeXN0ZXJpYTJfbWV0YV8wCmh5c3RlcmlhOi8vMTY3LjE2MC45MC4yNTE6NDgwODk/cGVlcj0mYXV0aD1kb25ndGFpd2FuZy5jb20maW5zZWN1cmU9MSZ1cG1icHM9NTAmZG93bm1icHM9ODAmYWxwbj1oMyZtcG9ydD00ODA4OSZvYmZzPSZwcm90b2NvbD11ZHAmZmFzdG9wZW49MSNoeXN0ZXJpYV9tZXRhXzAKdHVpYzovL2MyZmFhYzY5LWUxYzEtNGJmNS1iOGE4LWQyY2U0ZDgzNGE2Njpkb25ndGFpd2FuZ0B0dWljMS5mcmVlaDEueHl6OjQwOTgxP3NuaT10dWljMS5mcmVlaDEueHl6JmNvbmdlc3Rpb25fY29udHJvbD1iYnImdWRwX3JlbGF5X21vZGU9bmF0aXZlJmFscG49aDMmYWxsb3dfaW5zZWN1cmU9MAp0dWljOi8vZWQ2YTUzOGEtNmU2Ni00ZjIxLWE3NjktNGIzODliYjJmM2FiOmRvbmd0YWl3YW5nQHR1aWMzLmR0a3U0Ny54eXo6MTIyNTU/c25pPSZjb25nZXN0aW9uX2NvbnRyb2w9YmJyJnVkcF9yZWxheV9tb2RlPW5hdGl2ZSZhbHBuPWgzJmFsbG93X2luc2VjdXJlPTAKdHVpYzovLzM2MTg5MjFiLWFkZWItNGJkMy1hMmEwLWY5OGI3MmE2NzRiMTpkb25ndGFpd2FuZ0AxMDguMTgxLjI0Ljc6MjM0NTA/c25pPWJpbmcuY29tJmNvbmdlc3Rpb25fY29udHJvbD1iYnImdWRwX3JlbGF5X21vZGU9bmF0aXZlJmFscG49aDMmYWxsb3dfaW5zZWN1cmU9MQpoeXN0ZXJpYTovL3d3dy5kdGt1NDYueHl6OjExMjIzP3BlZXI9JmF1dGg9bXFvRTlxU295TUZhJmluc2VjdXJlPTEmdXBtYnBzPTUwJmRvd25tYnBzPTgwJmFscG49aDMmbXBvcnQ9MTEyMjMmb2Jmcz0mcHJvdG9jb2w9dWRwJmZhc3RvcGVuPTEjaHlzdGVyaWFfbWV0YV80CnR1aWM6Ly9kNjIxNDQzNy1lMWI1LTQzMzQtOTA5MC04ZjY2Yjc4YmVhODk6ZG9uZ3RhaXdhbmdAMTA4LjE4MS4yMi4yMDU6NTA5ODc/c25pPWJpbmcuY29tJmNvbmdlc3Rpb25fY29udHJvbD1iYnImdWRwX3JlbGF5X21vZGU9bmF0aXZlJmFscG49aDMmYWxsb3dfaW5zZWN1cmU9MQp0dWljOi8vNDg1Y2U3OTktZGE1Zi00NmU4LWE4MmItOGVmMzIyZDg2MDJmOmRvbmd0YWl3YW5nLmNvbUAxMDguMTgxLjIyLjIzOToxOTk4OD9zbmk9YmluZy5jb20mY29uZ2VzdGlvbl9jb250cm9sPWJiciZ1ZHBfcmVsYXlfbW9kZT1uYXRpdmUmYWxwbj1oMyZhbGxvd19pbnNlY3VyZT0xCmh5c3RlcmlhOi8vd3d3LmR0a3U1MC54eXo6MTQ3NTE/cGVlcj13d3cubWljcm9zb2Z0LmNvbSZhdXRoPSZpbnNlY3VyZT0xJnVwbWJwcz01MCZkb3dubWJwcz04MCZhbHBuPWgzJm1wb3J0PTE0NzUxJm9iZnM9JnByb3RvY29sPXVkcCZmYXN0b3Blbj0xI2h5c3RlcmlhX21ldGFfNwpoeXN0ZXJpYTovLzYyLjIwNC41NC44MTozNzg5OT9wZWVyPXd3dy5taWNyb3NvZnQuY29tJmF1dGg9Jmluc2VjdXJlPTEmdXBtYnBzPTUwJmRvd25tYnBzPTgwJmFscG49aDMmbXBvcnQ9Mzc4OTkmb2Jmcz0mcHJvdG9jb2w9dWRwJmZhc3RvcGVuPTEjaHlzdGVyaWFfbWV0YV84Cmh5c3RlcmlhOi8vd3d3My5kdGt1NDkueHl6OjU4NjkzP3BlZXI9YmluZy5jb20mYXV0aD0maW5zZWN1cmU9MSZ1cG1icHM9NTAmZG93bm1icHM9ODAmYWxwbj1oMyZtcG9ydD01ODY5MyZvYmZzPSZwcm90b2NvbD11ZHAmZmFzdG9wZW49MSNoeXN0ZXJpYV9tZXRhXzkKYUhSMGNITTZMeTlrYjI1bmRHRnBkMkZ1Wnk1amIyMDZaRzl1WjNSaGFYZGhibWN1WTI5dFFIZDNkeTVrZEd0MU5EZ3VlSGw2T2pRME13PT0KYUhSMGNITTZMeTlrYjI1bmRHRnBkMkZ1Wnk1amIyMDZaRzl1WjNSaGFYZGhibWN1WTI5dFFHNWhhWFpsTVRRdVkyWmpaRzR6TG5oNWVqbzBORE09Cmh5c3RlcmlhOi8vMTA5LjEwNC4xNTIuMTgwOjY0NTAyP3BlZXI9YmluZy5jb20mYXV0aD1reGVGS3BCOGZoR2pQN2NPN05OZ1hZcjE5WnNxS1FNY282MTJaQ2ZYaWFKcm9qdzU3MSZpbnNlY3VyZT0xJnVwbWJwcz0xMSZkb3dubWJwcz01NSZhbHBuPWgzJm9iZnM9JnByb3RvY29sPXVkcCZmYXN0b3Blbj0xI2h5c3RlcmlhXzAKaHlzdGVyaWE6Ly8xNzMuMjM0LjI1LjUyOjIwMTY0P3BlZXI9d3d3Lm1pY3Jvc29mdC5jb20mYXV0aD1Mamc2Tk5FQVREcVA5N2hkQWRIZTFsSnY3Z2d0S2MwaDd6bUNDWktDWDNxWTBMUjY0RiZpbnNlY3VyZT0xJnVwbWJwcz0xMSZkb3dubWJwcz01NSZhbHBuPWgzJm9iZnM9JnByb3RvY29sPXVkcCZmYXN0b3Blbj0xI2h5c3RlcmlhXzEKaHlzdGVyaWE6Ly8xMDkuMTA0LjE1Mi4xNDk6NDg0MDY/cGVlcj13d3cuYW1hem9uLmNuJmF1dGg9eGZOaHJ1bllKOUd2RFhDVGt0WTJiSXdoYzFFeWV5eUFiaVVNeDFVdEJPV2dJNGNNVkImaW5zZWN1cmU9MSZ1cG1icHM9MTEmZG93bm1icHM9NTUmYWxwbj1oMyZvYmZzPSZwcm90b2NvbD11ZHAmZmFzdG9wZW49MSNoeXN0ZXJpYV8yCmh5c3RlcmlhOi8vNTEuMTU4LjU0LjQ2OjExOTI2P3BlZXI9eW91a3UuY29tJmF1dGg9VHJ6MmFsS3d6Q0ltUkFYSTNuWGZwbzF5bHBIZnFPTDhzMXZhZ2VXS295amp2V2VNVnMmaW5zZWN1cmU9MSZ1cG1icHM9MTEmZG93bm1icHM9NTUmYWxwbj1oMyZvYmZzPSZwcm90b2NvbD11ZHAmZmFzdG9wZW49MSNoeXN0ZXJpYV8zCmh5c3RlcmlhMjovL2Rvbmd0YWl3YW5nLmNvbUB3d3cuZHRrdTQ2Lnh5ejo0OTczMD9pbnNlY3VyZT0xJnNuaT13d3cuYmluZy5jb20jaHlzdGVyaWEyXzAKaHlzdGVyaWEyOi8vZG9uZ3RhaXdhbmcuY29tQDEwOC4xODEuMjIuMTU1OjQ0MTQxP2luc2VjdXJlPTEmc25pPXd3dy5iaW5nLmNvbSNoeXN0ZXJpYTJfMQpoeXN0ZXJpYTI6Ly9kb25ndGFpd2FuZy5jb21Ad3d3LmR0a3U0OC54eXo6MjY4MDY/aW5zZWN1cmU9MSZzbmk9d3d3LmJpbmcuY29tI2h5c3RlcmlhMl8yCmh5c3RlcmlhMjovL2Rvbmd0YWl3YW5nLmNvbUAxMDguMTgxLjIyLjE1NTo0NDE0MT9pbnNlY3VyZT0xJnNuaT13d3cuYmluZy5jb20jaHlzdGVyaWEyXzMKdmxlc3M6Ly8wNzczMjU2Yy1kMDIwLTQzNmQtYWZlYS02ZWVlN2NiNmM4NzJAZG9uZ3RhaXdhbmczLmNvbTo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmU9MCZmbG93PSZ0eXBlPXdzJmZwPWNocm9tZSZwYms9JnNpZD0mc25pPXhyYXkxLmZyZWVncmFkZWx5Lnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vYm9kaHdzJmhvc3Q9eHJheTEuZnJlZWdyYWRlbHkueHl6I3ZsZXNzXzAKdmxlc3M6Ly9mNWMxODBlYi1mYmNlLTQ5YWMtOTAyOS00ODJlY2E5Mzg1YzBAZG9uZ3RhaXdhbmcyLmNvbTo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmU9MCZmbG93PSZ0eXBlPXdzJmZwPWNocm9tZSZwYms9JnNpZD0mc25pPXhyYXkxLmZyZWVoMS54eXomc2VydmljZU5hbWU9JnBhdGg9L2d6b2d3cyZob3N0PXhyYXkxLmZyZWVoMS54eXojdmxlc3NfMgp2bGVzczovL2Y1YzE4MGViLWZiY2UtNDlhYy05MDI5LTQ4MmVjYTkzODVjMEBkb25ndGFpd2FuZzMuY29tOjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZT0wJmZsb3c9JnR5cGU9d3MmZnA9Y2hyb21lJnBiaz0mc2lkPSZzbmk9eHJheTEuZnJlZWgxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vZ3pvZ3dzJmhvc3Q9eHJheTEuZnJlZWgxLnh5eiN2bGVzc18z
```

## sing-box订阅链接 (https://sing-box-subscribe.vercel.app/config/https:/mareep.netlify.app/sub/merged_proxies_new.yaml)
```yaml
None
```


