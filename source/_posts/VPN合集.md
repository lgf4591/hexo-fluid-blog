
---
title: VPN合集
date: 2024-02-14 06:49:08
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

> Last Update Time: 2024-02-14 06:49:08
---
# vless_node
```bash

None

```

# CloudFlare优质IP
```bash

电信172.64.109.113
电信172.64.110.210
电信172.67.152.212

联通172.67.128.20
联通172.67.132.80
联通172.64.168.50

移动172.67.131.56
移动172.67.167.157
移动172.64.105.14


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
140.82.113.26                 alive.github.com
140.82.113.5                  api.github.com
185.199.109.153               assets-cdn.github.com
185.199.111.133               avatars.githubusercontent.com
185.199.111.133               avatars0.githubusercontent.com
185.199.111.133               avatars1.githubusercontent.com
185.199.111.133               avatars2.githubusercontent.com
185.199.111.133               avatars3.githubusercontent.com
185.199.111.133               avatars4.githubusercontent.com
185.199.111.133               avatars5.githubusercontent.com
185.199.111.133               camo.githubusercontent.com
140.82.112.21                 central.github.com
185.199.111.133               cloud.githubusercontent.com
140.82.112.9                  codeload.github.com
140.82.113.22                 collector.github.com
185.199.111.133               desktop.githubusercontent.com
185.199.111.133               favicons.githubusercontent.com
140.82.113.4                  gist.github.com
52.216.9.35                   github-cloud.s3.amazonaws.com
52.217.141.137                github-com.s3.amazonaws.com
54.231.161.153                github-production-release-asset-2e65be.s3.amazonaws.com
54.231.170.49                 github-production-repository-file-5c1aeb.s3.amazonaws.com
52.216.38.233                 github-production-user-asset-6210df.s3.amazonaws.com
192.0.66.2                    github.blog
140.82.113.3                  github.com
140.82.113.18                 github.community
185.199.109.154               github.githubassets.com
151.101.193.194               github.global.ssl.fastly.net
185.199.109.153               github.io
185.199.111.133               github.map.fastly.net
185.199.109.153               githubstatus.com
140.82.113.26                 live.github.com
185.199.111.133               media.githubusercontent.com
185.199.111.133               objects.githubusercontent.com
13.107.42.16                  pipelines.actions.githubusercontent.com
185.199.111.133               raw.githubusercontent.com
185.199.111.133               user-images.githubusercontent.com
13.107.253.40                 vscode.dev
140.82.112.21                 education.github.com


# Update time: 2024-02-14T14:06:28+08:00
# Update url: https://raw.hellogithub.com/hosts
# Star me: https://github.com/521xueweihan/GitHub520
# GitHub520 Host End

```

该内容会自动定时更新， 数据更新时间：2024-02-14T14:06:28+08:00

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

- Hosts 类型: `Remote`

- Hosts 标题: 随意

- URL: `https://raw.hellogithub.com/hosts`

- 自动刷新: 最好选 `1 小时`

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
简体中文 | [English](./README_EN.md)

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
到 [Releases](https://github.com/Licoy/fetch-github-hosts/releases) 中下载您的系统版本（目前支持`Windows`/`Linux`/`MacOS`
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

到 [Releases](https://github.com/Licoy/fetch-github-hosts/releases) 中下载您的系统版本（目前支持`Windows`/`Linux`/`MacOS`
）

#### 参数

| 参数名        | 缩写  | 默认值                                  | 必填  | 描述                                 |
|------------|-----|--------------------------------------|-----|------------------------------------|
| `mode`     | `m` | 无                                    | 是   | 启动模式 `server（服务端）` / `client（客户端）` |
| `interval` | `i` | 60                                   | 否   | 获取记录值间隔（分钟）                        |
| `port`     | `p` | 9898                                 | 否   | 服务模式监听端口以访问HTTP服务                  |
| `url`      | `u` | `https://hosts.gitcdn.top/hosts.txt` | 否   | 客户端模式远程hosts获取链接                   |
| `lang`     | `l` | `zh-CN`                              | 否   | 界面语言                               |

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

下载最新的发行版（到 [Releases](https://github.com/Licoy/fetch-github-hosts/releases) 进行下载）
，并选择您的系统对应版本，直接以服务模式运行即可：`fetch-github-hosts -m=server -p=9898`，会自动监听`0.0.0.0:9898`，您可以直接浏览器访问 `http://127.0.0.1:9898`
以访问您自定义服务。
（具体方法可参见【启动服务端】小节详细说明）

> 注意：因网络影响，尽量部署到海外服务器节点！

## 趋势
[![Stargazers over time](https://starchart.cc/Licoy/fetch-github-hosts.svg)](https://starchart.cc/Licoy/fetch-github-hosts)

## 开源协议

[GPL 3.0](https://github.com/Licoy/fetch-github-hosts/blob/main/LICENSE)


# [freefq](https://github.com/freefq/free)
更新时间 2024-02-07 04:00  
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
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTozNlpDSGVhYlVTZktqZlFFdko0SERW@185.242.86.156:54170#github.com/freefq%20-%20%E4%BF%84%E7%BD%97%E6%96%AF%20%201  
vmess://eyJhZGQiOiAiMjAyLjc4LjE2Mi41IiwgImFpZCI6IDAsICJob3N0IjogImlyc29mdC5zeXRlcy5uZXQiLCAiaWQiOiAiMmZmOTdjNmQtODU1Ny00MmE0LWI0M2YtMTljNzdjNTk1OWVhIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9AZm9yd2FyZHYycmF5IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM3MFx1NWVhNiAgMiIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9  
vmess://eyJhZGQiOiAiMjAyLjc4LjE2Mi41IiwgImFpZCI6IDAsICJob3N0IjogInNhaGFuZC5zZXJ2ZW1pbmVjcmFmdC5uZXQiLCAiaWQiOiAiMTE4Mjg3ZDItZTk2OC00MmUxLTgwZDAtMTJmYTJmNWQzOGQ2IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9AZm9yd2FyZHYycmF5IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM3MFx1NWVhNiAgMyIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDQiLCAiYWRkIjogInd3dy5kYXJrcm9vbS5sb2wiLCAicG9ydCI6IDgwODAsICJpZCI6ICIyMjgyNmI0NC01YzFhLTRiNGItZGJhYS04M2EyZThiZDk1ZjAiLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy5kYXJrcm9vbS5sb2wiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==  
ss://YWVzLTI1Ni1nY206N0JjTGRzTzFXd2VvR0QwWA@193.243.147.128:40368#github.com/freefq%20-%20%E6%B3%A2%E5%85%B0%20%205  
vmess://eyJhZGQiOiAic2VydmVyMzEuYmVoZXNodGJhbmVoLmNvbSIsICJhaWQiOiAwLCAiaG9zdCI6ICJzZXJ2ZXIzMS5iZWhlc2h0YmFuZWguY29tIiwgImlkIjogIjQxNTQxNDNjLWJiYmEtNDdhNC05Zjc5LWMyZWQwODdjYmNjOSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgInBvcnQiOiA4ODgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDYiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==  
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggNyIsICJhZGQiOiAiZGF0YS11cy12MS5zaHdqZmt3LmNuIiwgInBvcnQiOiAiMjA0MDEiLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAidGxzIjogIiIsICJpZCI6ICJiMTQ3OGUyNC00OTE2LTNhYmUtOGYxNy0xNTkzMTAxMmVjYmUiLCAic25pIjogIiIsICJob3N0IjogImRhdGEtdXMtdjEuc2h3amZrdy5jbiIsICJwYXRoIjogIi9kZWJpYW4ifQ==  
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpkNjEwNWJiZC1iZTBkLTQ1YjItODJhZC0zMWZkMTA3MWMxZDI@service.ouluyun9803.com:20003#github.com/freefq%20-%20%E5%B9%BF%E4%B8%9C%E7%9C%81%E6%B1%9F%E9%97%A8%E5%B8%82%E7%A7%BB%E5%8A%A8%208  
vmess://eyJhZGQiOiAiMTA0LjIxLjgyLjE4MyIsICJhaWQiOiAwLCAiaG9zdCI6ICJzZXJ2ZXIyNi5iZWhlc2h0YmFuZWguY29tIiwgImlkIjogIjVhNzAyMWUwLTI2YjQtNDVkNi1iMTc1LWZlNTUxNjAxY2E5NyIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgInBvcnQiOiA4ODgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDkiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==  
vmess://eyJhZGQiOiAiMjAyLjc4LjE2Mi41IiwgImFpZCI6IDAsICJob3N0IjogInBlbmRhci5vbnRoZXdpZmkuY29tIiwgImlkIjogIjcxNmVkZWQ2LTIyMDEtNGRiZC05ZDYzLTE2MzhjOWU4ZTY3NyIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvQGZvcndhcmR2MnJheSIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNzBcdTVlYTYgIDEwIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=  
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpkNjEwNWJiZC1iZTBkLTQ1YjItODJhZC0zMWZkMTA3MWMxZDI@service.ouluyun9803.com:26667#github.com/freefq%20-%20%E5%B9%BF%E4%B8%9C%E7%9C%81%E6%B1%9F%E9%97%A8%E5%B8%82%E7%A7%BB%E5%8A%A8%2011  
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpkNjEwNWJiZC1iZTBkLTQ1YjItODJhZC0zMWZkMTA3MWMxZDI@service.ouluyun9803.com:20005#github.com/freefq%20-%20%E5%B9%BF%E4%B8%9C%E7%9C%81%E6%B1%9F%E9%97%A8%E5%B8%82%E7%A7%BB%E5%8A%A8%2012  
vmess://eyJhZGQiOiAiZ292LnVrIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZEZhc3RseVx1NTE2OFx1NzQwM0FueWNhc3RcdTgyODJcdTcwYjkgMTMiLCAicG9ydCI6IDQ0MywgImlkIjogIjc3ODQ4ODI0LTkzYjctNGI4OS1mZmQwLWU5MWFmZmY0MDZjZSIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJ6aGVzaGlzY3AuY29tIiwgInBhdGgiOiAiLzc3ODQ4ODI0IiwgInRscyI6ICJ0bHMifQ==  
vmess://eyJhZGQiOiAic2VydmVyMzIuYmVoZXNodGJhbmVoLmNvbSIsICJhaWQiOiAwLCAiaG9zdCI6ICJzZXJ2ZXIzMi5iZWhlc2h0YmFuZWguY29tIiwgImlkIjogIjA0NGJhOGVkLTcyODUtNDcyYS1iYzE0LWZiOTFkYzZiZTRjOSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgInBvcnQiOiA4ODgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE0IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=  
```  



# ChromeGo_Merge Readme Content
## 简介

油管：[绵阿羊](https://www.youtube.com/channel/UC9xYHJIRj7oXTPYYrTv2U2A)

## 注意事项

套上warp可绕过chromego封锁的网站（P，X）

开启浏览器自带doh以及客户端tun模式也可绕过封锁，参考：[开启chrome自带doh](https://blog.mareep.net/posts/9993/)

## 如何修改为自己的warp节点

<details>
  <summary>点击展开/折叠</summary>

可以用warp+机器人和提取wg节点替换掉配置文件中的wg信息

[warp提取wireguard网站](https://replit.com/@misaka-blog/wgcf-profile-generator)

[warp+机器人](https://t.me/generatewarpplusbot)

然后本地创建一个yaml文件，参考：[issues #20](https://github.com/mianayang/chromego_merge/issues/20)

</details>

## 订阅链接分享
### 不套warp版本（clashmeta）

```
https://mareep.netlify.app/sub/merged_proxies_new.yaml
```
### 套warp版本（clashmeta）

```
https://mareep.netlify.app/sub/merged_warp_proxies_new.yaml
```

### 通用base64链接 （shadowrocket和nekoray系列）
```
https://mareep.netlify.app/sub/shadowrocket_base64.txt
```

### sing-box订阅链接（1.8.0以上）

```
https://mareep.netlify.app/sub/sb.json
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

区域设置代码截取自:
- [chromegopacs](https://github.com/markbang/chromegopacs)





# ChromeGo_Merge Detail Content
## 不套warp版本（clashmeta）

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
- name: 油管绵阿羊_United States_hysteria2_01
  type: hysteria2
  server: 64.31.55.30
  port: 20011
  password: dongtaiwang.com
  alpn:
  - h3
  sni: bing.com
  skip-cert-verify: true
  up: 11 Mbps
  down: 55 Mbps
- name: 油管绵阿羊_United States_tuic_11
  type: tuic
  server: 109.104.152.144
  port: 44411
  udp: true
  uuid: 7bda06fd-e4af-4115-8aa3-f021832cfa78
  password: dongtaiwang.com
  alpn:
  - h3
  disable-sni: true
  reduce-rtt: true
  udp-relay-mode: native
  congestion-controller: bbr
- name: 油管绵阿羊_Taiwan_vmess_12
  type: vmess
  server: www.dtku40.xyz
  port: 18840
  cipher: auto
  uuid: afb1ad76-0f6f-4cb8-983a-95f5b4708321
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /9tEYTPFN/
- name: 油管绵阿羊_United States_hysteria_21
  type: hysteria
  server: 109.104.152.101
  port: 32200
  sni: bing.com
  skip-cert-verify: true
  alpn:
  - h3
  protocol: udp
  auth_str: dongtaiwang.com
  up: 11
  down: 55
- name: 油管绵阿羊_United States_vmess_22
  type: vmess
  server: 108.181.5.18
  port: 40010
  cipher: auto
  uuid: 44bee251-795d-4d7a-8ecb-c4322aec05be
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /xajVDSGJ/
- name: 油管绵阿羊_United States_tuic_31
  type: tuic
  server: 109.104.152.101
  port: 22288
  udp: true
  uuid: 7bda06fd-e4af-4115-8aa3-f021832cfa78
  password: dongtaiwang.com
  alpn:
  - h3
  disable-sni: true
  reduce-rtt: true
  udp-relay-mode: native
  congestion-controller: bbr
- name: 油管绵阿羊_United States_vless_41
  type: vless
  server: 109.104.152.101
  port: 11111
  udp: true
  uuid: 9cc39477-0d85-4419-84d4-fb7fc77668b3
  tls: true
  servername: m.media-amazon.com
  flow: xtls-rprx-vision
  network: tcp
  reality-opts:
    public-key: yKXmLTmXAi-BHBg3JpCz-NWUmVcKlfm7iMmVoq7YQx0
    short-id: 6ba85179e30d4fc2
  client-fingerprint: chrome
- name: 油管绵阿羊_None_vless_51
  type: vless
  server: 198.41.193.226
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_52
  type: vless
  server: 104.27.97.91
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_53
  type: vless
  server: 108.162.196.107
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_54
  type: vless
  server: 104.22.46.253
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_France_vless_55
  type: vless
  server: 173.245.49.56
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_56
  type: vless
  server: 198.41.195.168
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_57
  type: vless
  server: 103.21.244.189
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_58
  type: vless
  server: 104.21.35.228
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_59
  type: vless
  server: 162.159.38.71
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_510
  type: vless
  server: 104.19.7.150
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_511
  type: vless
  server: 108.162.196.74
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_512
  type: vless
  server: 104.18.9.181
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_513
  type: vless
  server: 190.93.245.188
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_514
  type: vless
  server: 198.41.218.199
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_515
  type: vless
  server: 104.18.110.163
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Costa Rica_vless_516
  type: vless
  server: 190.93.246.114
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_517
  type: vless
  server: 103.21.244.236
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_518
  type: vless
  server: 162.159.24.166
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_519
  type: vless
  server: 104.25.69.69
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_520
  type: vless
  server: 104.16.196.143
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_521
  type: vless
  server: 103.21.244.162
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_522
  type: vless
  server: 172.66.138.14
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_523
  type: vless
  server: 172.64.49.33
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_524
  type: vless
  server: 104.25.113.186
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_525
  type: vless
  server: 104.20.5.9
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_526
  type: vless
  server: 104.25.211.145
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_527
  type: vless
  server: 172.67.209.51
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_528
  type: vless
  server: 104.18.141.86
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Netherlands_vless_529
  type: vless
  server: 188.114.97.19
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_530
  type: vless
  server: 104.27.16.75
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_531
  type: vless
  server: 104.18.95.234
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_532
  type: vless
  server: 198.41.202.98
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_533
  type: vless
  server: 162.159.24.244
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_534
  type: vless
  server: 104.24.132.228
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_535
  type: vless
  server: 198.41.209.249
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_536
  type: vless
  server: 104.24.88.199
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_537
  type: vless
  server: 103.21.244.248
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_538
  type: vless
  server: 104.20.253.93
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_539
  type: vless
  server: 173.245.58.18
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_540
  type: vless
  server: 104.17.11.252
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_541
  type: vless
  server: 104.24.18.7
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_542
  type: vless
  server: 104.16.38.162
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_543
  type: vless
  server: 108.162.194.144
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_544
  type: vless
  server: 190.93.244.218
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_545
  type: vless
  server: 104.19.45.11
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Netherlands_vless_546
  type: vless
  server: 188.114.96.211
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_547
  type: vless
  server: 172.67.152.22
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_548
  type: vless
  server: 104.16.75.128
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_549
  type: vless
  server: 198.41.202.169
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_550
  type: vless
  server: 104.24.57.248
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_France_vless_551
  type: vless
  server: 173.245.49.207
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_552
  type: vless
  server: 104.24.226.143
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_553
  type: vless
  server: 173.245.59.17
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_554
  type: vless
  server: 104.17.2.38
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_555
  type: vless
  server: 162.159.6.199
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_556
  type: vless
  server: 141.101.113.239
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_557
  type: vless
  server: 172.64.173.200
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_558
  type: vless
  server: 104.21.235.122
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Costa Rica_vless_559
  type: vless
  server: 190.93.246.107
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Netherlands_vless_560
  type: vless
  server: 188.114.97.27
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_561
  type: vless
  server: 190.93.244.47
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_562
  type: vless
  server: 173.245.58.237
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_563
  type: vless
  server: 172.67.166.72
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_564
  type: vless
  server: 190.93.245.106
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_565
  type: vless
  server: 104.27.107.221
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_566
  type: vless
  server: 103.21.244.137
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_567
  type: vless
  server: 104.22.71.28
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_568
  type: vless
  server: 104.17.123.53
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_569
  type: vless
  server: 104.21.25.95
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_570
  type: vless
  server: 104.24.190.226
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_571
  type: vless
  server: 104.27.61.67
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_572
  type: vless
  server: 104.24.171.195
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_France_vless_573
  type: vless
  server: 173.245.49.195
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Costa Rica_vless_574
  type: vless
  server: 190.93.247.5
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_575
  type: vless
  server: 108.162.192.179
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_576
  type: vless
  server: 198.41.216.62
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_577
  type: vless
  server: 104.17.6.218
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_578
  type: vless
  server: 103.21.244.219
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_579
  type: vless
  server: 141.101.121.69
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_580
  type: vless
  server: 104.25.12.88
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_581
  type: vless
  server: 104.24.74.248
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_582
  type: vless
  server: 104.18.9.239
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_583
  type: vless
  server: 104.16.247.95
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_584
  type: vless
  server: 104.25.19.37
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_585
  type: vless
  server: 104.18.238.119
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_586
  type: vless
  server: 104.24.214.188
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_587
  type: vless
  server: 172.66.142.115
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_588
  type: vless
  server: 103.21.244.126
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_589
  type: vless
  server: 103.21.244.74
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_590
  type: vless
  server: 103.21.244.94
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_591
  type: vless
  server: 104.20.87.76
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_592
  type: vless
  server: 104.25.122.116
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_593
  type: vless
  server: 190.93.245.66
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_594
  type: vless
  server: 104.18.23.136
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_595
  type: vless
  server: 104.25.254.11
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_596
  type: vless
  server: 104.25.94.175
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_597
  type: vless
  server: 141.101.121.18
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_598
  type: vless
  server: 162.159.133.78
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_599
  type: vless
  server: 173.245.59.173
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Costa Rica_vless_5100
  type: vless
  server: 190.93.247.107
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5101
  type: vless
  server: 162.159.252.249
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5102
  type: vless
  server: 104.17.12.96
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5103
  type: vless
  server: 162.159.21.6
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_5104
  type: vless
  server: 103.21.244.125
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5105
  type: vless
  server: 104.16.137.106
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_5106
  type: vless
  server: 172.64.149.192
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5107
  type: vless
  server: 104.24.16.226
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_5108
  type: vless
  server: 172.67.103.221
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Netherlands_vless_5109
  type: vless
  server: 188.114.97.111
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_5110
  type: vless
  server: 172.67.109.53
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5111
  type: vless
  server: 104.20.252.36
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5112
  type: vless
  server: 104.20.125.193
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Netherlands_vless_5113
  type: vless
  server: 188.114.99.120
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_5114
  type: vless
  server: 108.162.193.37
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5115
  type: vless
  server: 104.17.103.194
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5116
  type: vless
  server: 198.41.200.139
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Netherlands_vless_5117
  type: vless
  server: 188.114.97.222
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Costa Rica_vless_5118
  type: vless
  server: 190.93.247.68
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5119
  type: vless
  server: 104.17.87.110
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_5120
  type: vless
  server: 172.67.155.77
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5121
  type: vless
  server: 162.159.26.15
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5122
  type: vless
  server: 198.41.217.152
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5123
  type: vless
  server: 104.18.244.225
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_5124
  type: vless
  server: 190.93.245.73
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5125
  type: vless
  server: 104.27.41.157
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5126
  type: vless
  server: 141.101.121.106
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5127
  type: vless
  server: 104.24.31.205
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5128
  type: vless
  server: 198.41.220.53
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5129
  type: vless
  server: 104.24.178.127
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5130
  type: vless
  server: 162.159.240.167
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_5131
  type: vless
  server: 103.21.244.141
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_5132
  type: vless
  server: 172.67.19.224
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5133
  type: vless
  server: 104.25.225.101
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Netherlands_vless_5134
  type: vless
  server: 188.114.96.162
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5135
  type: vless
  server: 104.18.135.212
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5136
  type: vless
  server: 104.19.246.22
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_5137
  type: vless
  server: 172.64.164.162
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Taiwan_hysteria_61
  type: hysteria
  server: www2.dtku48.xyz
  port: 22334
  auth-str: dongtaiwang.com
  alpn:
  - h3
  protocol: udp
  up: 11 Mbps
  down: 55 Mbps
  skip-cert-verify: true
- name: 油管绵阿羊_France_hysteria2_71
  type: hysteria2
  server: 51.158.54.46
  port: 44550
  password: dongtaiwang.com
  sni: bing.com
  skip-cert-verify: true
- name: 油管绵阿羊_United States_hysteria2_81
  type: hysteria2
  server: 45.150.165.84
  port: 8881
  password: d017e316-82cb-441c-8eea-7b5e9de64a20
  obfs: salamander
  obfs-password: d017e316-82cb-441c-8eea-7b5e9de64a20
  skip-cert-verify: true
  up: 2 Mbps
  down: 10 Mbps
- name: 油管绵阿羊_Taiwan_hysteria_91
  type: hysteria
  server: www.dtku50.xyz
  port: 18470
  sni: www.amazon.cn
  skip-cert-verify: true
  alpn:
  - h3
  protocol: udp
  auth_str: dongtaiwang.com
  up: 2
  down: 10
- name: 油管绵阿羊_France_hy_0
  type: hysteria
  server: 51.158.54.46
  port: 55396
  ports: 55396
  auth_str: dongtaiwang.com
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: youku.com
  skip-cert-verify: true
  alpn:
  - h3
- name: 油管绵阿羊_United States_hy_1
  type: hysteria
  server: 173.234.25.52
  port: 48919
  ports: 48919
  auth_str: dongtaiwang.com
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: bing.com
  skip-cert-verify: true
  alpn:
  - h3
- name: 油管绵阿羊_Taiwan_hy_2
  type: hysteria
  server: www.dtku40.xyz
  port: 18490
  ports: 18490
  auth_str: dongtaiwang.com
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: bing.com
  skip-cert-verify: true
  alpn:
  - h3
- name: 油管绵阿羊_United States_hy_3
  type: hysteria
  server: 167.160.91.115
  port: 41189
  ports: 41189
  auth_str: bWAwIqINo7XDm1fUlXQGBifVIXoYs1ylgVKqWFKzK1XyDKuwNF
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: www.amazon.cn
  skip-cert-verify: true
  alpn:
  - h3
- name: 油管绵阿羊_France_hy2_0
  type: hysteria2
  server: 62.210.103.0
  port: 22483
  password: dongtaiwang.com
  fast-open: true
  sni: www.bing.com
  skip-cert-verify: true
- name: 油管绵阿羊_United States_hy2_1
  type: hysteria2
  server: 64.110.25.11
  port: 33337
  password: dongtaiwang.com
  fast-open: true
  sni: www.bing.com
  skip-cert-verify: true
- name: 油管绵阿羊_France_hy2_2
  type: hysteria2
  server: 62.210.103.0
  port: 22483
  password: dongtaiwang.com
  fast-open: true
  sni: www.bing.com
  skip-cert-verify: true
- name: 油管绵阿羊_France_hy2_3
  type: hysteria2
  server: 51.159.77.198
  port: 29277
  password: dongtaiwang.com
  fast-open: true
  sni: www.bing.com
  skip-cert-verify: true
- name: 油管绵阿羊_France_reality_2
  type: vless
  server: 62.210.101.0
  port: 18700
  uuid: e659661d-8439-46e0-b1ab-d75ceaf73404
  network: tcp
  tls: true
  udp: true
  flow: xtls-rprx-vision
  client-fingerprint: chrome
  servername: update.microsoft
  reality-opts:
    public-key: PBRc2v9SSXpG4jjQRYNa-kgs8w9V4U3MNLuncd2d0hw
    short-id: 6ba85179e30d4fc2
- name: 油管绵阿羊_France_reality_3
  type: vless
  server: 62.210.101.0
  port: 18700
  uuid: e659661d-8439-46e0-b1ab-d75ceaf73404
  network: tcp
  tls: true
  udp: true
  flow: xtls-rprx-vision
  client-fingerprint: chrome
  servername: update.microsoft
  reality-opts:
    public-key: PBRc2v9SSXpG4jjQRYNa-kgs8w9V4U3MNLuncd2d0hw
    short-id: 6ba85179e30d4fc2
proxy-groups:
- name: 节点选择
  type: select
  proxies:
  - 自动选择
  - DIRECT
  - 油管绵阿羊_United States_hysteria2_01
  - 油管绵阿羊_United States_tuic_11
  - 油管绵阿羊_Taiwan_vmess_12
  - 油管绵阿羊_United States_hysteria_21
  - 油管绵阿羊_United States_vmess_22
  - 油管绵阿羊_United States_tuic_31
  - 油管绵阿羊_United States_vless_41
  - 油管绵阿羊_None_vless_51
  - 油管绵阿羊_None_vless_52
  - 油管绵阿羊_United States_vless_53
  - 油管绵阿羊_None_vless_54
  - 油管绵阿羊_France_vless_55
  - 油管绵阿羊_None_vless_56
  - 油管绵阿羊_United States_vless_57
  - 油管绵阿羊_None_vless_58
  - 油管绵阿羊_None_vless_59
  - 油管绵阿羊_None_vless_510
  - 油管绵阿羊_United States_vless_511
  - 油管绵阿羊_None_vless_512
  - 油管绵阿羊_United States_vless_513
  - 油管绵阿羊_None_vless_514
  - 油管绵阿羊_None_vless_515
  - 油管绵阿羊_Costa Rica_vless_516
  - 油管绵阿羊_United States_vless_517
  - 油管绵阿羊_None_vless_518
  - 油管绵阿羊_None_vless_519
  - 油管绵阿羊_None_vless_520
  - 油管绵阿羊_United States_vless_521
  - 油管绵阿羊_United States_vless_522
  - 油管绵阿羊_United States_vless_523
  - 油管绵阿羊_None_vless_524
  - 油管绵阿羊_None_vless_525
  - 油管绵阿羊_None_vless_526
  - 油管绵阿羊_United States_vless_527
  - 油管绵阿羊_None_vless_528
  - 油管绵阿羊_Netherlands_vless_529
  - 油管绵阿羊_None_vless_530
  - 油管绵阿羊_None_vless_531
  - 油管绵阿羊_None_vless_532
  - 油管绵阿羊_None_vless_533
  - 油管绵阿羊_None_vless_534
  - 油管绵阿羊_None_vless_535
  - 油管绵阿羊_None_vless_536
  - 油管绵阿羊_United States_vless_537
  - 油管绵阿羊_None_vless_538
  - 油管绵阿羊_United States_vless_539
  - 油管绵阿羊_None_vless_540
  - 油管绵阿羊_None_vless_541
  - 油管绵阿羊_None_vless_542
  - 油管绵阿羊_United States_vless_543
  - 油管绵阿羊_United States_vless_544
  - 油管绵阿羊_None_vless_545
  - 油管绵阿羊_Netherlands_vless_546
  - 油管绵阿羊_United States_vless_547
  - 油管绵阿羊_None_vless_548
  - 油管绵阿羊_None_vless_549
  - 油管绵阿羊_None_vless_550
  - 油管绵阿羊_France_vless_551
  - 油管绵阿羊_None_vless_552
  - 油管绵阿羊_United States_vless_553
  - 油管绵阿羊_None_vless_554
  - 油管绵阿羊_None_vless_555
  - 油管绵阿羊_None_vless_556
  - 油管绵阿羊_United States_vless_557
  - 油管绵阿羊_None_vless_558
  - 油管绵阿羊_Costa Rica_vless_559
  - 油管绵阿羊_Netherlands_vless_560
  - 油管绵阿羊_United States_vless_561
  - 油管绵阿羊_United States_vless_562
  - 油管绵阿羊_United States_vless_563
  - 油管绵阿羊_United States_vless_564
  - 油管绵阿羊_None_vless_565
  - 油管绵阿羊_United States_vless_566
  - 油管绵阿羊_None_vless_567
  - 油管绵阿羊_None_vless_568
  - 油管绵阿羊_None_vless_569
  - 油管绵阿羊_None_vless_570
  - 油管绵阿羊_None_vless_571
  - 油管绵阿羊_None_vless_572
  - 油管绵阿羊_France_vless_573
  - 油管绵阿羊_Costa Rica_vless_574
  - 油管绵阿羊_United States_vless_575
  - 油管绵阿羊_None_vless_576
  - 油管绵阿羊_None_vless_577
  - 油管绵阿羊_United States_vless_578
  - 油管绵阿羊_None_vless_579
  - 油管绵阿羊_None_vless_580
  - 油管绵阿羊_None_vless_581
  - 油管绵阿羊_None_vless_582
  - 油管绵阿羊_None_vless_583
  - 油管绵阿羊_None_vless_584
  - 油管绵阿羊_None_vless_585
  - 油管绵阿羊_None_vless_586
  - 油管绵阿羊_United States_vless_587
  - 油管绵阿羊_United States_vless_588
  - 油管绵阿羊_United States_vless_589
  - 油管绵阿羊_United States_vless_590
  - 油管绵阿羊_None_vless_591
  - 油管绵阿羊_None_vless_592
  - 油管绵阿羊_United States_vless_593
  - 油管绵阿羊_None_vless_594
  - 油管绵阿羊_None_vless_595
  - 油管绵阿羊_None_vless_596
  - 油管绵阿羊_None_vless_597
  - 油管绵阿羊_None_vless_598
  - 油管绵阿羊_United States_vless_599
  - 油管绵阿羊_Costa Rica_vless_5100
  - 油管绵阿羊_None_vless_5101
  - 油管绵阿羊_None_vless_5102
  - 油管绵阿羊_None_vless_5103
  - 油管绵阿羊_United States_vless_5104
  - 油管绵阿羊_None_vless_5105
  - 油管绵阿羊_United States_vless_5106
  - 油管绵阿羊_None_vless_5107
  - 油管绵阿羊_United States_vless_5108
  - 油管绵阿羊_Netherlands_vless_5109
  - 油管绵阿羊_United States_vless_5110
  - 油管绵阿羊_None_vless_5111
  - 油管绵阿羊_None_vless_5112
  - 油管绵阿羊_Netherlands_vless_5113
  - 油管绵阿羊_United States_vless_5114
  - 油管绵阿羊_None_vless_5115
  - 油管绵阿羊_None_vless_5116
  - 油管绵阿羊_Netherlands_vless_5117
  - 油管绵阿羊_Costa Rica_vless_5118
  - 油管绵阿羊_None_vless_5119
  - 油管绵阿羊_United States_vless_5120
  - 油管绵阿羊_None_vless_5121
  - 油管绵阿羊_None_vless_5122
  - 油管绵阿羊_None_vless_5123
  - 油管绵阿羊_United States_vless_5124
  - 油管绵阿羊_None_vless_5125
  - 油管绵阿羊_None_vless_5126
  - 油管绵阿羊_None_vless_5127
  - 油管绵阿羊_None_vless_5128
  - 油管绵阿羊_None_vless_5129
  - 油管绵阿羊_None_vless_5130
  - 油管绵阿羊_United States_vless_5131
  - 油管绵阿羊_United States_vless_5132
  - 油管绵阿羊_None_vless_5133
  - 油管绵阿羊_Netherlands_vless_5134
  - 油管绵阿羊_None_vless_5135
  - 油管绵阿羊_None_vless_5136
  - 油管绵阿羊_United States_vless_5137
  - 油管绵阿羊_Taiwan_hysteria_61
  - 油管绵阿羊_France_hysteria2_71
  - 油管绵阿羊_United States_hysteria2_81
  - 油管绵阿羊_Taiwan_hysteria_91
  - 油管绵阿羊_France_hy_0
  - 油管绵阿羊_United States_hy_1
  - 油管绵阿羊_Taiwan_hy_2
  - 油管绵阿羊_United States_hy_3
  - 油管绵阿羊_France_hy2_0
  - 油管绵阿羊_United States_hy2_1
  - 油管绵阿羊_France_hy2_2
  - 油管绵阿羊_France_hy2_3
  - 油管绵阿羊_France_reality_2
  - 油管绵阿羊_France_reality_3
- name: 自动选择
  type: url-test
  url: http://www.gstatic.com/generate_204
  interval: 300
  tolerance: 50
  proxies:
  - 油管绵阿羊_United States_hysteria2_01
  - 油管绵阿羊_United States_tuic_11
  - 油管绵阿羊_Taiwan_vmess_12
  - 油管绵阿羊_United States_hysteria_21
  - 油管绵阿羊_United States_vmess_22
  - 油管绵阿羊_United States_tuic_31
  - 油管绵阿羊_United States_vless_41
  - 油管绵阿羊_None_vless_51
  - 油管绵阿羊_None_vless_52
  - 油管绵阿羊_United States_vless_53
  - 油管绵阿羊_None_vless_54
  - 油管绵阿羊_France_vless_55
  - 油管绵阿羊_None_vless_56
  - 油管绵阿羊_United States_vless_57
  - 油管绵阿羊_None_vless_58
  - 油管绵阿羊_None_vless_59
  - 油管绵阿羊_None_vless_510
  - 油管绵阿羊_United States_vless_511
  - 油管绵阿羊_None_vless_512
  - 油管绵阿羊_United States_vless_513
  - 油管绵阿羊_None_vless_514
  - 油管绵阿羊_None_vless_515
  - 油管绵阿羊_Costa Rica_vless_516
  - 油管绵阿羊_United States_vless_517
  - 油管绵阿羊_None_vless_518
  - 油管绵阿羊_None_vless_519
  - 油管绵阿羊_None_vless_520
  - 油管绵阿羊_United States_vless_521
  - 油管绵阿羊_United States_vless_522
  - 油管绵阿羊_United States_vless_523
  - 油管绵阿羊_None_vless_524
  - 油管绵阿羊_None_vless_525
  - 油管绵阿羊_None_vless_526
  - 油管绵阿羊_United States_vless_527
  - 油管绵阿羊_None_vless_528
  - 油管绵阿羊_Netherlands_vless_529
  - 油管绵阿羊_None_vless_530
  - 油管绵阿羊_None_vless_531
  - 油管绵阿羊_None_vless_532
  - 油管绵阿羊_None_vless_533
  - 油管绵阿羊_None_vless_534
  - 油管绵阿羊_None_vless_535
  - 油管绵阿羊_None_vless_536
  - 油管绵阿羊_United States_vless_537
  - 油管绵阿羊_None_vless_538
  - 油管绵阿羊_United States_vless_539
  - 油管绵阿羊_None_vless_540
  - 油管绵阿羊_None_vless_541
  - 油管绵阿羊_None_vless_542
  - 油管绵阿羊_United States_vless_543
  - 油管绵阿羊_United States_vless_544
  - 油管绵阿羊_None_vless_545
  - 油管绵阿羊_Netherlands_vless_546
  - 油管绵阿羊_United States_vless_547
  - 油管绵阿羊_None_vless_548
  - 油管绵阿羊_None_vless_549
  - 油管绵阿羊_None_vless_550
  - 油管绵阿羊_France_vless_551
  - 油管绵阿羊_None_vless_552
  - 油管绵阿羊_United States_vless_553
  - 油管绵阿羊_None_vless_554
  - 油管绵阿羊_None_vless_555
  - 油管绵阿羊_None_vless_556
  - 油管绵阿羊_United States_vless_557
  - 油管绵阿羊_None_vless_558
  - 油管绵阿羊_Costa Rica_vless_559
  - 油管绵阿羊_Netherlands_vless_560
  - 油管绵阿羊_United States_vless_561
  - 油管绵阿羊_United States_vless_562
  - 油管绵阿羊_United States_vless_563
  - 油管绵阿羊_United States_vless_564
  - 油管绵阿羊_None_vless_565
  - 油管绵阿羊_United States_vless_566
  - 油管绵阿羊_None_vless_567
  - 油管绵阿羊_None_vless_568
  - 油管绵阿羊_None_vless_569
  - 油管绵阿羊_None_vless_570
  - 油管绵阿羊_None_vless_571
  - 油管绵阿羊_None_vless_572
  - 油管绵阿羊_France_vless_573
  - 油管绵阿羊_Costa Rica_vless_574
  - 油管绵阿羊_United States_vless_575
  - 油管绵阿羊_None_vless_576
  - 油管绵阿羊_None_vless_577
  - 油管绵阿羊_United States_vless_578
  - 油管绵阿羊_None_vless_579
  - 油管绵阿羊_None_vless_580
  - 油管绵阿羊_None_vless_581
  - 油管绵阿羊_None_vless_582
  - 油管绵阿羊_None_vless_583
  - 油管绵阿羊_None_vless_584
  - 油管绵阿羊_None_vless_585
  - 油管绵阿羊_None_vless_586
  - 油管绵阿羊_United States_vless_587
  - 油管绵阿羊_United States_vless_588
  - 油管绵阿羊_United States_vless_589
  - 油管绵阿羊_United States_vless_590
  - 油管绵阿羊_None_vless_591
  - 油管绵阿羊_None_vless_592
  - 油管绵阿羊_United States_vless_593
  - 油管绵阿羊_None_vless_594
  - 油管绵阿羊_None_vless_595
  - 油管绵阿羊_None_vless_596
  - 油管绵阿羊_None_vless_597
  - 油管绵阿羊_None_vless_598
  - 油管绵阿羊_United States_vless_599
  - 油管绵阿羊_Costa Rica_vless_5100
  - 油管绵阿羊_None_vless_5101
  - 油管绵阿羊_None_vless_5102
  - 油管绵阿羊_None_vless_5103
  - 油管绵阿羊_United States_vless_5104
  - 油管绵阿羊_None_vless_5105
  - 油管绵阿羊_United States_vless_5106
  - 油管绵阿羊_None_vless_5107
  - 油管绵阿羊_United States_vless_5108
  - 油管绵阿羊_Netherlands_vless_5109
  - 油管绵阿羊_United States_vless_5110
  - 油管绵阿羊_None_vless_5111
  - 油管绵阿羊_None_vless_5112
  - 油管绵阿羊_Netherlands_vless_5113
  - 油管绵阿羊_United States_vless_5114
  - 油管绵阿羊_None_vless_5115
  - 油管绵阿羊_None_vless_5116
  - 油管绵阿羊_Netherlands_vless_5117
  - 油管绵阿羊_Costa Rica_vless_5118
  - 油管绵阿羊_None_vless_5119
  - 油管绵阿羊_United States_vless_5120
  - 油管绵阿羊_None_vless_5121
  - 油管绵阿羊_None_vless_5122
  - 油管绵阿羊_None_vless_5123
  - 油管绵阿羊_United States_vless_5124
  - 油管绵阿羊_None_vless_5125
  - 油管绵阿羊_None_vless_5126
  - 油管绵阿羊_None_vless_5127
  - 油管绵阿羊_None_vless_5128
  - 油管绵阿羊_None_vless_5129
  - 油管绵阿羊_None_vless_5130
  - 油管绵阿羊_United States_vless_5131
  - 油管绵阿羊_United States_vless_5132
  - 油管绵阿羊_None_vless_5133
  - 油管绵阿羊_Netherlands_vless_5134
  - 油管绵阿羊_None_vless_5135
  - 油管绵阿羊_None_vless_5136
  - 油管绵阿羊_United States_vless_5137
  - 油管绵阿羊_Taiwan_hysteria_61
  - 油管绵阿羊_France_hysteria2_71
  - 油管绵阿羊_United States_hysteria2_81
  - 油管绵阿羊_Taiwan_hysteria_91
  - 油管绵阿羊_France_hy_0
  - 油管绵阿羊_United States_hy_1
  - 油管绵阿羊_Taiwan_hy_2
  - 油管绵阿羊_United States_hy_3
  - 油管绵阿羊_France_hy2_0
  - 油管绵阿羊_United States_hy2_1
  - 油管绵阿羊_France_hy2_2
  - 油管绵阿羊_France_hy2_3
  - 油管绵阿羊_France_reality_2
  - 油管绵阿羊_France_reality_3
rules:
- DOMAIN,clash.razord.top,DIRECT
- DOMAIN,yacd.haishan.me,DIRECT
- GEOIP,LAN,DIRECT
- GEOIP,CN,DIRECT
- MATCH,节点选择

```

## 套warp版本（clashmeta)
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
  server: 162.159.192.1
  port: 2408
  ip: 172.16.0.2
  ipv6: 2606:4700:110:87ad:b400:91:eadb:887f
  private-key: wIC19yRRSJkhVJcE09Qo9bE3P3PIwS3yyqyUnjwNO34=
  public-key: bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo=
  udp: true
  ip-version: ipv6-prefer
  reserved: XiBe
  remote-dns-resolve: true
  dns:
  - 1.1.1.1
  - 8.8.8.8
  dialer-proxy: WARP前置节点
- name: 油管绵阿羊_United States_hysteria2_01
  type: hysteria2
  server: 64.31.55.30
  port: 20011
  password: dongtaiwang.com
  alpn:
  - h3
  sni: bing.com
  skip-cert-verify: true
  up: 11 Mbps
  down: 55 Mbps
- name: 油管绵阿羊_United States_tuic_11
  type: tuic
  server: 109.104.152.144
  port: 44411
  udp: true
  uuid: 7bda06fd-e4af-4115-8aa3-f021832cfa78
  password: dongtaiwang.com
  alpn:
  - h3
  disable-sni: true
  reduce-rtt: true
  udp-relay-mode: native
  congestion-controller: bbr
- name: 油管绵阿羊_Taiwan_vmess_12
  type: vmess
  server: www.dtku40.xyz
  port: 18840
  cipher: auto
  uuid: afb1ad76-0f6f-4cb8-983a-95f5b4708321
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /9tEYTPFN/
- name: 油管绵阿羊_United States_hysteria_21
  type: hysteria
  server: 109.104.152.101
  port: 32200
  sni: bing.com
  skip-cert-verify: true
  alpn:
  - h3
  protocol: udp
  auth_str: dongtaiwang.com
  up: 11
  down: 55
- name: 油管绵阿羊_United States_vmess_22
  type: vmess
  server: 108.181.5.18
  port: 40010
  cipher: auto
  uuid: 44bee251-795d-4d7a-8ecb-c4322aec05be
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /xajVDSGJ/
- name: 油管绵阿羊_United States_tuic_31
  type: tuic
  server: 109.104.152.101
  port: 22288
  udp: true
  uuid: 7bda06fd-e4af-4115-8aa3-f021832cfa78
  password: dongtaiwang.com
  alpn:
  - h3
  disable-sni: true
  reduce-rtt: true
  udp-relay-mode: native
  congestion-controller: bbr
- name: 油管绵阿羊_United States_vless_41
  type: vless
  server: 109.104.152.101
  port: 11111
  udp: true
  uuid: 9cc39477-0d85-4419-84d4-fb7fc77668b3
  tls: true
  servername: m.media-amazon.com
  flow: xtls-rprx-vision
  network: tcp
  reality-opts:
    public-key: yKXmLTmXAi-BHBg3JpCz-NWUmVcKlfm7iMmVoq7YQx0
    short-id: 6ba85179e30d4fc2
  client-fingerprint: chrome
- name: 油管绵阿羊_None_vless_51
  type: vless
  server: 198.41.193.226
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_52
  type: vless
  server: 104.27.97.91
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_53
  type: vless
  server: 108.162.196.107
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_54
  type: vless
  server: 104.22.46.253
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_France_vless_55
  type: vless
  server: 173.245.49.56
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_56
  type: vless
  server: 198.41.195.168
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_57
  type: vless
  server: 103.21.244.189
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_58
  type: vless
  server: 104.21.35.228
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_59
  type: vless
  server: 162.159.38.71
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_510
  type: vless
  server: 104.19.7.150
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_511
  type: vless
  server: 108.162.196.74
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_512
  type: vless
  server: 104.18.9.181
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_513
  type: vless
  server: 190.93.245.188
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_514
  type: vless
  server: 198.41.218.199
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_515
  type: vless
  server: 104.18.110.163
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Costa Rica_vless_516
  type: vless
  server: 190.93.246.114
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_517
  type: vless
  server: 103.21.244.236
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_518
  type: vless
  server: 162.159.24.166
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_519
  type: vless
  server: 104.25.69.69
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_520
  type: vless
  server: 104.16.196.143
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_521
  type: vless
  server: 103.21.244.162
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_522
  type: vless
  server: 172.66.138.14
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_523
  type: vless
  server: 172.64.49.33
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_524
  type: vless
  server: 104.25.113.186
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_525
  type: vless
  server: 104.20.5.9
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_526
  type: vless
  server: 104.25.211.145
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_527
  type: vless
  server: 172.67.209.51
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_528
  type: vless
  server: 104.18.141.86
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Netherlands_vless_529
  type: vless
  server: 188.114.97.19
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_530
  type: vless
  server: 104.27.16.75
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_531
  type: vless
  server: 104.18.95.234
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_532
  type: vless
  server: 198.41.202.98
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_533
  type: vless
  server: 162.159.24.244
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_534
  type: vless
  server: 104.24.132.228
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_535
  type: vless
  server: 198.41.209.249
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_536
  type: vless
  server: 104.24.88.199
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_537
  type: vless
  server: 103.21.244.248
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_538
  type: vless
  server: 104.20.253.93
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_539
  type: vless
  server: 173.245.58.18
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_540
  type: vless
  server: 104.17.11.252
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_541
  type: vless
  server: 104.24.18.7
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_542
  type: vless
  server: 104.16.38.162
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_543
  type: vless
  server: 108.162.194.144
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_544
  type: vless
  server: 190.93.244.218
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_545
  type: vless
  server: 104.19.45.11
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Netherlands_vless_546
  type: vless
  server: 188.114.96.211
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_547
  type: vless
  server: 172.67.152.22
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_548
  type: vless
  server: 104.16.75.128
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_549
  type: vless
  server: 198.41.202.169
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_550
  type: vless
  server: 104.24.57.248
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_France_vless_551
  type: vless
  server: 173.245.49.207
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_552
  type: vless
  server: 104.24.226.143
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_553
  type: vless
  server: 173.245.59.17
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_554
  type: vless
  server: 104.17.2.38
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_555
  type: vless
  server: 162.159.6.199
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_556
  type: vless
  server: 141.101.113.239
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_557
  type: vless
  server: 172.64.173.200
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_558
  type: vless
  server: 104.21.235.122
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Costa Rica_vless_559
  type: vless
  server: 190.93.246.107
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Netherlands_vless_560
  type: vless
  server: 188.114.97.27
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_561
  type: vless
  server: 190.93.244.47
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_562
  type: vless
  server: 173.245.58.237
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_563
  type: vless
  server: 172.67.166.72
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_564
  type: vless
  server: 190.93.245.106
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_565
  type: vless
  server: 104.27.107.221
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_566
  type: vless
  server: 103.21.244.137
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_567
  type: vless
  server: 104.22.71.28
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_568
  type: vless
  server: 104.17.123.53
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_569
  type: vless
  server: 104.21.25.95
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_570
  type: vless
  server: 104.24.190.226
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_571
  type: vless
  server: 104.27.61.67
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_572
  type: vless
  server: 104.24.171.195
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_France_vless_573
  type: vless
  server: 173.245.49.195
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Costa Rica_vless_574
  type: vless
  server: 190.93.247.5
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_575
  type: vless
  server: 108.162.192.179
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_576
  type: vless
  server: 198.41.216.62
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_577
  type: vless
  server: 104.17.6.218
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_578
  type: vless
  server: 103.21.244.219
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_579
  type: vless
  server: 141.101.121.69
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_580
  type: vless
  server: 104.25.12.88
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_581
  type: vless
  server: 104.24.74.248
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_582
  type: vless
  server: 104.18.9.239
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_583
  type: vless
  server: 104.16.247.95
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_584
  type: vless
  server: 104.25.19.37
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_585
  type: vless
  server: 104.18.238.119
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_586
  type: vless
  server: 104.24.214.188
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_587
  type: vless
  server: 172.66.142.115
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_588
  type: vless
  server: 103.21.244.126
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_589
  type: vless
  server: 103.21.244.74
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_590
  type: vless
  server: 103.21.244.94
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_591
  type: vless
  server: 104.20.87.76
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_592
  type: vless
  server: 104.25.122.116
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_593
  type: vless
  server: 190.93.245.66
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_594
  type: vless
  server: 104.18.23.136
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_595
  type: vless
  server: 104.25.254.11
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_596
  type: vless
  server: 104.25.94.175
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_597
  type: vless
  server: 141.101.121.18
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_598
  type: vless
  server: 162.159.133.78
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_599
  type: vless
  server: 173.245.59.173
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Costa Rica_vless_5100
  type: vless
  server: 190.93.247.107
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5101
  type: vless
  server: 162.159.252.249
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5102
  type: vless
  server: 104.17.12.96
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5103
  type: vless
  server: 162.159.21.6
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_5104
  type: vless
  server: 103.21.244.125
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5105
  type: vless
  server: 104.16.137.106
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_5106
  type: vless
  server: 172.64.149.192
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5107
  type: vless
  server: 104.24.16.226
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_5108
  type: vless
  server: 172.67.103.221
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Netherlands_vless_5109
  type: vless
  server: 188.114.97.111
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_5110
  type: vless
  server: 172.67.109.53
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5111
  type: vless
  server: 104.20.252.36
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5112
  type: vless
  server: 104.20.125.193
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Netherlands_vless_5113
  type: vless
  server: 188.114.99.120
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_5114
  type: vless
  server: 108.162.193.37
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5115
  type: vless
  server: 104.17.103.194
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5116
  type: vless
  server: 198.41.200.139
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Netherlands_vless_5117
  type: vless
  server: 188.114.97.222
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Costa Rica_vless_5118
  type: vless
  server: 190.93.247.68
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5119
  type: vless
  server: 104.17.87.110
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_5120
  type: vless
  server: 172.67.155.77
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5121
  type: vless
  server: 162.159.26.15
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5122
  type: vless
  server: 198.41.217.152
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5123
  type: vless
  server: 104.18.244.225
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_5124
  type: vless
  server: 190.93.245.73
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5125
  type: vless
  server: 104.27.41.157
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5126
  type: vless
  server: 141.101.121.106
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5127
  type: vless
  server: 104.24.31.205
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5128
  type: vless
  server: 198.41.220.53
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5129
  type: vless
  server: 104.24.178.127
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5130
  type: vless
  server: 162.159.240.167
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_5131
  type: vless
  server: 103.21.244.141
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_5132
  type: vless
  server: 172.67.19.224
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5133
  type: vless
  server: 104.25.225.101
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Netherlands_vless_5134
  type: vless
  server: 188.114.96.162
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5135
  type: vless
  server: 104.18.135.212
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_None_vless_5136
  type: vless
  server: 104.19.246.22
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_United States_vless_5137
  type: vless
  server: 172.64.164.162
  port: 443
  uuid: 95878aa5-a695-4b88-b502-55c05c998cf2
  tls: true
  servername: lg1.dtku41.xyz
  network: ws
  ws-opts:
    path: /ugrlws
    headers:
      host: lg1.dtku41.xyz
- name: 油管绵阿羊_Taiwan_hysteria_61
  type: hysteria
  server: www2.dtku48.xyz
  port: 22334
  auth-str: dongtaiwang.com
  alpn:
  - h3
  protocol: udp
  up: 11 Mbps
  down: 55 Mbps
  skip-cert-verify: true
- name: 油管绵阿羊_France_hysteria2_71
  type: hysteria2
  server: 51.158.54.46
  port: 44550
  password: dongtaiwang.com
  sni: bing.com
  skip-cert-verify: true
- name: 油管绵阿羊_United States_hysteria2_81
  type: hysteria2
  server: 45.150.165.84
  port: 8881
  password: d017e316-82cb-441c-8eea-7b5e9de64a20
  obfs: salamander
  obfs-password: d017e316-82cb-441c-8eea-7b5e9de64a20
  skip-cert-verify: true
  up: 2 Mbps
  down: 10 Mbps
- name: 油管绵阿羊_Taiwan_hysteria_91
  type: hysteria
  server: www.dtku50.xyz
  port: 18470
  sni: www.amazon.cn
  skip-cert-verify: true
  alpn:
  - h3
  protocol: udp
  auth_str: dongtaiwang.com
  up: 2
  down: 10
- name: 油管绵阿羊_France_hy_0
  type: hysteria
  server: 51.158.54.46
  port: 55396
  ports: 55396
  auth_str: dongtaiwang.com
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: youku.com
  skip-cert-verify: true
  alpn:
  - h3
- name: 油管绵阿羊_United States_hy_1
  type: hysteria
  server: 173.234.25.52
  port: 48919
  ports: 48919
  auth_str: dongtaiwang.com
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: bing.com
  skip-cert-verify: true
  alpn:
  - h3
- name: 油管绵阿羊_Taiwan_hy_2
  type: hysteria
  server: www.dtku40.xyz
  port: 18490
  ports: 18490
  auth_str: dongtaiwang.com
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: bing.com
  skip-cert-verify: true
  alpn:
  - h3
- name: 油管绵阿羊_United States_hy_3
  type: hysteria
  server: 167.160.91.115
  port: 41189
  ports: 41189
  auth_str: bWAwIqINo7XDm1fUlXQGBifVIXoYs1ylgVKqWFKzK1XyDKuwNF
  up: 80
  down: 100
  fast-open: true
  protocol: udp
  sni: www.amazon.cn
  skip-cert-verify: true
  alpn:
  - h3
- name: 油管绵阿羊_France_hy2_0
  type: hysteria2
  server: 62.210.103.0
  port: 22483
  password: dongtaiwang.com
  fast-open: true
  sni: www.bing.com
  skip-cert-verify: true
- name: 油管绵阿羊_United States_hy2_1
  type: hysteria2
  server: 64.110.25.11
  port: 33337
  password: dongtaiwang.com
  fast-open: true
  sni: www.bing.com
  skip-cert-verify: true
- name: 油管绵阿羊_France_hy2_2
  type: hysteria2
  server: 62.210.103.0
  port: 22483
  password: dongtaiwang.com
  fast-open: true
  sni: www.bing.com
  skip-cert-verify: true
- name: 油管绵阿羊_France_hy2_3
  type: hysteria2
  server: 51.159.77.198
  port: 29277
  password: dongtaiwang.com
  fast-open: true
  sni: www.bing.com
  skip-cert-verify: true
- name: 油管绵阿羊_France_reality_2
  type: vless
  server: 62.210.101.0
  port: 18700
  uuid: e659661d-8439-46e0-b1ab-d75ceaf73404
  network: tcp
  tls: true
  udp: true
  flow: xtls-rprx-vision
  client-fingerprint: chrome
  servername: update.microsoft
  reality-opts:
    public-key: PBRc2v9SSXpG4jjQRYNa-kgs8w9V4U3MNLuncd2d0hw
    short-id: 6ba85179e30d4fc2
- name: 油管绵阿羊_France_reality_3
  type: vless
  server: 62.210.101.0
  port: 18700
  uuid: e659661d-8439-46e0-b1ab-d75ceaf73404
  network: tcp
  tls: true
  udp: true
  flow: xtls-rprx-vision
  client-fingerprint: chrome
  servername: update.microsoft
  reality-opts:
    public-key: PBRc2v9SSXpG4jjQRYNa-kgs8w9V4U3MNLuncd2d0hw
    short-id: 6ba85179e30d4fc2
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
  - 油管绵阿羊_United States_hysteria2_01
  - 油管绵阿羊_United States_tuic_11
  - 油管绵阿羊_Taiwan_vmess_12
  - 油管绵阿羊_United States_hysteria_21
  - 油管绵阿羊_United States_vmess_22
  - 油管绵阿羊_United States_tuic_31
  - 油管绵阿羊_United States_vless_41
  - 油管绵阿羊_None_vless_51
  - 油管绵阿羊_None_vless_52
  - 油管绵阿羊_United States_vless_53
  - 油管绵阿羊_None_vless_54
  - 油管绵阿羊_France_vless_55
  - 油管绵阿羊_None_vless_56
  - 油管绵阿羊_United States_vless_57
  - 油管绵阿羊_None_vless_58
  - 油管绵阿羊_None_vless_59
  - 油管绵阿羊_None_vless_510
  - 油管绵阿羊_United States_vless_511
  - 油管绵阿羊_None_vless_512
  - 油管绵阿羊_United States_vless_513
  - 油管绵阿羊_None_vless_514
  - 油管绵阿羊_None_vless_515
  - 油管绵阿羊_Costa Rica_vless_516
  - 油管绵阿羊_United States_vless_517
  - 油管绵阿羊_None_vless_518
  - 油管绵阿羊_None_vless_519
  - 油管绵阿羊_None_vless_520
  - 油管绵阿羊_United States_vless_521
  - 油管绵阿羊_United States_vless_522
  - 油管绵阿羊_United States_vless_523
  - 油管绵阿羊_None_vless_524
  - 油管绵阿羊_None_vless_525
  - 油管绵阿羊_None_vless_526
  - 油管绵阿羊_United States_vless_527
  - 油管绵阿羊_None_vless_528
  - 油管绵阿羊_Netherlands_vless_529
  - 油管绵阿羊_None_vless_530
  - 油管绵阿羊_None_vless_531
  - 油管绵阿羊_None_vless_532
  - 油管绵阿羊_None_vless_533
  - 油管绵阿羊_None_vless_534
  - 油管绵阿羊_None_vless_535
  - 油管绵阿羊_None_vless_536
  - 油管绵阿羊_United States_vless_537
  - 油管绵阿羊_None_vless_538
  - 油管绵阿羊_United States_vless_539
  - 油管绵阿羊_None_vless_540
  - 油管绵阿羊_None_vless_541
  - 油管绵阿羊_None_vless_542
  - 油管绵阿羊_United States_vless_543
  - 油管绵阿羊_United States_vless_544
  - 油管绵阿羊_None_vless_545
  - 油管绵阿羊_Netherlands_vless_546
  - 油管绵阿羊_United States_vless_547
  - 油管绵阿羊_None_vless_548
  - 油管绵阿羊_None_vless_549
  - 油管绵阿羊_None_vless_550
  - 油管绵阿羊_France_vless_551
  - 油管绵阿羊_None_vless_552
  - 油管绵阿羊_United States_vless_553
  - 油管绵阿羊_None_vless_554
  - 油管绵阿羊_None_vless_555
  - 油管绵阿羊_None_vless_556
  - 油管绵阿羊_United States_vless_557
  - 油管绵阿羊_None_vless_558
  - 油管绵阿羊_Costa Rica_vless_559
  - 油管绵阿羊_Netherlands_vless_560
  - 油管绵阿羊_United States_vless_561
  - 油管绵阿羊_United States_vless_562
  - 油管绵阿羊_United States_vless_563
  - 油管绵阿羊_United States_vless_564
  - 油管绵阿羊_None_vless_565
  - 油管绵阿羊_United States_vless_566
  - 油管绵阿羊_None_vless_567
  - 油管绵阿羊_None_vless_568
  - 油管绵阿羊_None_vless_569
  - 油管绵阿羊_None_vless_570
  - 油管绵阿羊_None_vless_571
  - 油管绵阿羊_None_vless_572
  - 油管绵阿羊_France_vless_573
  - 油管绵阿羊_Costa Rica_vless_574
  - 油管绵阿羊_United States_vless_575
  - 油管绵阿羊_None_vless_576
  - 油管绵阿羊_None_vless_577
  - 油管绵阿羊_United States_vless_578
  - 油管绵阿羊_None_vless_579
  - 油管绵阿羊_None_vless_580
  - 油管绵阿羊_None_vless_581
  - 油管绵阿羊_None_vless_582
  - 油管绵阿羊_None_vless_583
  - 油管绵阿羊_None_vless_584
  - 油管绵阿羊_None_vless_585
  - 油管绵阿羊_None_vless_586
  - 油管绵阿羊_United States_vless_587
  - 油管绵阿羊_United States_vless_588
  - 油管绵阿羊_United States_vless_589
  - 油管绵阿羊_United States_vless_590
  - 油管绵阿羊_None_vless_591
  - 油管绵阿羊_None_vless_592
  - 油管绵阿羊_United States_vless_593
  - 油管绵阿羊_None_vless_594
  - 油管绵阿羊_None_vless_595
  - 油管绵阿羊_None_vless_596
  - 油管绵阿羊_None_vless_597
  - 油管绵阿羊_None_vless_598
  - 油管绵阿羊_United States_vless_599
  - 油管绵阿羊_Costa Rica_vless_5100
  - 油管绵阿羊_None_vless_5101
  - 油管绵阿羊_None_vless_5102
  - 油管绵阿羊_None_vless_5103
  - 油管绵阿羊_United States_vless_5104
  - 油管绵阿羊_None_vless_5105
  - 油管绵阿羊_United States_vless_5106
  - 油管绵阿羊_None_vless_5107
  - 油管绵阿羊_United States_vless_5108
  - 油管绵阿羊_Netherlands_vless_5109
  - 油管绵阿羊_United States_vless_5110
  - 油管绵阿羊_None_vless_5111
  - 油管绵阿羊_None_vless_5112
  - 油管绵阿羊_Netherlands_vless_5113
  - 油管绵阿羊_United States_vless_5114
  - 油管绵阿羊_None_vless_5115
  - 油管绵阿羊_None_vless_5116
  - 油管绵阿羊_Netherlands_vless_5117
  - 油管绵阿羊_Costa Rica_vless_5118
  - 油管绵阿羊_None_vless_5119
  - 油管绵阿羊_United States_vless_5120
  - 油管绵阿羊_None_vless_5121
  - 油管绵阿羊_None_vless_5122
  - 油管绵阿羊_None_vless_5123
  - 油管绵阿羊_United States_vless_5124
  - 油管绵阿羊_None_vless_5125
  - 油管绵阿羊_None_vless_5126
  - 油管绵阿羊_None_vless_5127
  - 油管绵阿羊_None_vless_5128
  - 油管绵阿羊_None_vless_5129
  - 油管绵阿羊_None_vless_5130
  - 油管绵阿羊_United States_vless_5131
  - 油管绵阿羊_United States_vless_5132
  - 油管绵阿羊_None_vless_5133
  - 油管绵阿羊_Netherlands_vless_5134
  - 油管绵阿羊_None_vless_5135
  - 油管绵阿羊_None_vless_5136
  - 油管绵阿羊_United States_vless_5137
  - 油管绵阿羊_Taiwan_hysteria_61
  - 油管绵阿羊_France_hysteria2_71
  - 油管绵阿羊_United States_hysteria2_81
  - 油管绵阿羊_Taiwan_hysteria_91
  - 油管绵阿羊_France_hy_0
  - 油管绵阿羊_United States_hy_1
  - 油管绵阿羊_Taiwan_hy_2
  - 油管绵阿羊_United States_hy_3
  - 油管绵阿羊_France_hy2_0
  - 油管绵阿羊_United States_hy2_1
  - 油管绵阿羊_France_hy2_2
  - 油管绵阿羊_France_hy2_3
  - 油管绵阿羊_France_reality_2
  - 油管绵阿羊_France_reality_3
- name: 手动选择
  type: select
  proxies:
  - 油管绵阿羊_United States_hysteria2_01
  - 油管绵阿羊_United States_tuic_11
  - 油管绵阿羊_Taiwan_vmess_12
  - 油管绵阿羊_United States_hysteria_21
  - 油管绵阿羊_United States_vmess_22
  - 油管绵阿羊_United States_tuic_31
  - 油管绵阿羊_United States_vless_41
  - 油管绵阿羊_None_vless_51
  - 油管绵阿羊_None_vless_52
  - 油管绵阿羊_United States_vless_53
  - 油管绵阿羊_None_vless_54
  - 油管绵阿羊_France_vless_55
  - 油管绵阿羊_None_vless_56
  - 油管绵阿羊_United States_vless_57
  - 油管绵阿羊_None_vless_58
  - 油管绵阿羊_None_vless_59
  - 油管绵阿羊_None_vless_510
  - 油管绵阿羊_United States_vless_511
  - 油管绵阿羊_None_vless_512
  - 油管绵阿羊_United States_vless_513
  - 油管绵阿羊_None_vless_514
  - 油管绵阿羊_None_vless_515
  - 油管绵阿羊_Costa Rica_vless_516
  - 油管绵阿羊_United States_vless_517
  - 油管绵阿羊_None_vless_518
  - 油管绵阿羊_None_vless_519
  - 油管绵阿羊_None_vless_520
  - 油管绵阿羊_United States_vless_521
  - 油管绵阿羊_United States_vless_522
  - 油管绵阿羊_United States_vless_523
  - 油管绵阿羊_None_vless_524
  - 油管绵阿羊_None_vless_525
  - 油管绵阿羊_None_vless_526
  - 油管绵阿羊_United States_vless_527
  - 油管绵阿羊_None_vless_528
  - 油管绵阿羊_Netherlands_vless_529
  - 油管绵阿羊_None_vless_530
  - 油管绵阿羊_None_vless_531
  - 油管绵阿羊_None_vless_532
  - 油管绵阿羊_None_vless_533
  - 油管绵阿羊_None_vless_534
  - 油管绵阿羊_None_vless_535
  - 油管绵阿羊_None_vless_536
  - 油管绵阿羊_United States_vless_537
  - 油管绵阿羊_None_vless_538
  - 油管绵阿羊_United States_vless_539
  - 油管绵阿羊_None_vless_540
  - 油管绵阿羊_None_vless_541
  - 油管绵阿羊_None_vless_542
  - 油管绵阿羊_United States_vless_543
  - 油管绵阿羊_United States_vless_544
  - 油管绵阿羊_None_vless_545
  - 油管绵阿羊_Netherlands_vless_546
  - 油管绵阿羊_United States_vless_547
  - 油管绵阿羊_None_vless_548
  - 油管绵阿羊_None_vless_549
  - 油管绵阿羊_None_vless_550
  - 油管绵阿羊_France_vless_551
  - 油管绵阿羊_None_vless_552
  - 油管绵阿羊_United States_vless_553
  - 油管绵阿羊_None_vless_554
  - 油管绵阿羊_None_vless_555
  - 油管绵阿羊_None_vless_556
  - 油管绵阿羊_United States_vless_557
  - 油管绵阿羊_None_vless_558
  - 油管绵阿羊_Costa Rica_vless_559
  - 油管绵阿羊_Netherlands_vless_560
  - 油管绵阿羊_United States_vless_561
  - 油管绵阿羊_United States_vless_562
  - 油管绵阿羊_United States_vless_563
  - 油管绵阿羊_United States_vless_564
  - 油管绵阿羊_None_vless_565
  - 油管绵阿羊_United States_vless_566
  - 油管绵阿羊_None_vless_567
  - 油管绵阿羊_None_vless_568
  - 油管绵阿羊_None_vless_569
  - 油管绵阿羊_None_vless_570
  - 油管绵阿羊_None_vless_571
  - 油管绵阿羊_None_vless_572
  - 油管绵阿羊_France_vless_573
  - 油管绵阿羊_Costa Rica_vless_574
  - 油管绵阿羊_United States_vless_575
  - 油管绵阿羊_None_vless_576
  - 油管绵阿羊_None_vless_577
  - 油管绵阿羊_United States_vless_578
  - 油管绵阿羊_None_vless_579
  - 油管绵阿羊_None_vless_580
  - 油管绵阿羊_None_vless_581
  - 油管绵阿羊_None_vless_582
  - 油管绵阿羊_None_vless_583
  - 油管绵阿羊_None_vless_584
  - 油管绵阿羊_None_vless_585
  - 油管绵阿羊_None_vless_586
  - 油管绵阿羊_United States_vless_587
  - 油管绵阿羊_United States_vless_588
  - 油管绵阿羊_United States_vless_589
  - 油管绵阿羊_United States_vless_590
  - 油管绵阿羊_None_vless_591
  - 油管绵阿羊_None_vless_592
  - 油管绵阿羊_United States_vless_593
  - 油管绵阿羊_None_vless_594
  - 油管绵阿羊_None_vless_595
  - 油管绵阿羊_None_vless_596
  - 油管绵阿羊_None_vless_597
  - 油管绵阿羊_None_vless_598
  - 油管绵阿羊_United States_vless_599
  - 油管绵阿羊_Costa Rica_vless_5100
  - 油管绵阿羊_None_vless_5101
  - 油管绵阿羊_None_vless_5102
  - 油管绵阿羊_None_vless_5103
  - 油管绵阿羊_United States_vless_5104
  - 油管绵阿羊_None_vless_5105
  - 油管绵阿羊_United States_vless_5106
  - 油管绵阿羊_None_vless_5107
  - 油管绵阿羊_United States_vless_5108
  - 油管绵阿羊_Netherlands_vless_5109
  - 油管绵阿羊_United States_vless_5110
  - 油管绵阿羊_None_vless_5111
  - 油管绵阿羊_None_vless_5112
  - 油管绵阿羊_Netherlands_vless_5113
  - 油管绵阿羊_United States_vless_5114
  - 油管绵阿羊_None_vless_5115
  - 油管绵阿羊_None_vless_5116
  - 油管绵阿羊_Netherlands_vless_5117
  - 油管绵阿羊_Costa Rica_vless_5118
  - 油管绵阿羊_None_vless_5119
  - 油管绵阿羊_United States_vless_5120
  - 油管绵阿羊_None_vless_5121
  - 油管绵阿羊_None_vless_5122
  - 油管绵阿羊_None_vless_5123
  - 油管绵阿羊_United States_vless_5124
  - 油管绵阿羊_None_vless_5125
  - 油管绵阿羊_None_vless_5126
  - 油管绵阿羊_None_vless_5127
  - 油管绵阿羊_None_vless_5128
  - 油管绵阿羊_None_vless_5129
  - 油管绵阿羊_None_vless_5130
  - 油管绵阿羊_United States_vless_5131
  - 油管绵阿羊_United States_vless_5132
  - 油管绵阿羊_None_vless_5133
  - 油管绵阿羊_Netherlands_vless_5134
  - 油管绵阿羊_None_vless_5135
  - 油管绵阿羊_None_vless_5136
  - 油管绵阿羊_United States_vless_5137
  - 油管绵阿羊_Taiwan_hysteria_61
  - 油管绵阿羊_France_hysteria2_71
  - 油管绵阿羊_United States_hysteria2_81
  - 油管绵阿羊_Taiwan_hysteria_91
  - 油管绵阿羊_France_hy_0
  - 油管绵阿羊_United States_hy_1
  - 油管绵阿羊_Taiwan_hy_2
  - 油管绵阿羊_United States_hy_3
  - 油管绵阿羊_France_hy2_0
  - 油管绵阿羊_United States_hy2_1
  - 油管绵阿羊_France_hy2_2
  - 油管绵阿羊_France_hy2_3
  - 油管绵阿羊_France_reality_2
  - 油管绵阿羊_France_reality_3
- name: 负载均衡
  type: load-balance
  proxies:
  - 油管绵阿羊_United States_hysteria2_01
  - 油管绵阿羊_United States_tuic_11
  - 油管绵阿羊_Taiwan_vmess_12
  - 油管绵阿羊_United States_hysteria_21
  - 油管绵阿羊_United States_vmess_22
  - 油管绵阿羊_United States_tuic_31
  - 油管绵阿羊_United States_vless_41
  - 油管绵阿羊_None_vless_51
  - 油管绵阿羊_None_vless_52
  - 油管绵阿羊_United States_vless_53
  - 油管绵阿羊_None_vless_54
  - 油管绵阿羊_France_vless_55
  - 油管绵阿羊_None_vless_56
  - 油管绵阿羊_United States_vless_57
  - 油管绵阿羊_None_vless_58
  - 油管绵阿羊_None_vless_59
  - 油管绵阿羊_None_vless_510
  - 油管绵阿羊_United States_vless_511
  - 油管绵阿羊_None_vless_512
  - 油管绵阿羊_United States_vless_513
  - 油管绵阿羊_None_vless_514
  - 油管绵阿羊_None_vless_515
  - 油管绵阿羊_Costa Rica_vless_516
  - 油管绵阿羊_United States_vless_517
  - 油管绵阿羊_None_vless_518
  - 油管绵阿羊_None_vless_519
  - 油管绵阿羊_None_vless_520
  - 油管绵阿羊_United States_vless_521
  - 油管绵阿羊_United States_vless_522
  - 油管绵阿羊_United States_vless_523
  - 油管绵阿羊_None_vless_524
  - 油管绵阿羊_None_vless_525
  - 油管绵阿羊_None_vless_526
  - 油管绵阿羊_United States_vless_527
  - 油管绵阿羊_None_vless_528
  - 油管绵阿羊_Netherlands_vless_529
  - 油管绵阿羊_None_vless_530
  - 油管绵阿羊_None_vless_531
  - 油管绵阿羊_None_vless_532
  - 油管绵阿羊_None_vless_533
  - 油管绵阿羊_None_vless_534
  - 油管绵阿羊_None_vless_535
  - 油管绵阿羊_None_vless_536
  - 油管绵阿羊_United States_vless_537
  - 油管绵阿羊_None_vless_538
  - 油管绵阿羊_United States_vless_539
  - 油管绵阿羊_None_vless_540
  - 油管绵阿羊_None_vless_541
  - 油管绵阿羊_None_vless_542
  - 油管绵阿羊_United States_vless_543
  - 油管绵阿羊_United States_vless_544
  - 油管绵阿羊_None_vless_545
  - 油管绵阿羊_Netherlands_vless_546
  - 油管绵阿羊_United States_vless_547
  - 油管绵阿羊_None_vless_548
  - 油管绵阿羊_None_vless_549
  - 油管绵阿羊_None_vless_550
  - 油管绵阿羊_France_vless_551
  - 油管绵阿羊_None_vless_552
  - 油管绵阿羊_United States_vless_553
  - 油管绵阿羊_None_vless_554
  - 油管绵阿羊_None_vless_555
  - 油管绵阿羊_None_vless_556
  - 油管绵阿羊_United States_vless_557
  - 油管绵阿羊_None_vless_558
  - 油管绵阿羊_Costa Rica_vless_559
  - 油管绵阿羊_Netherlands_vless_560
  - 油管绵阿羊_United States_vless_561
  - 油管绵阿羊_United States_vless_562
  - 油管绵阿羊_United States_vless_563
  - 油管绵阿羊_United States_vless_564
  - 油管绵阿羊_None_vless_565
  - 油管绵阿羊_United States_vless_566
  - 油管绵阿羊_None_vless_567
  - 油管绵阿羊_None_vless_568
  - 油管绵阿羊_None_vless_569
  - 油管绵阿羊_None_vless_570
  - 油管绵阿羊_None_vless_571
  - 油管绵阿羊_None_vless_572
  - 油管绵阿羊_France_vless_573
  - 油管绵阿羊_Costa Rica_vless_574
  - 油管绵阿羊_United States_vless_575
  - 油管绵阿羊_None_vless_576
  - 油管绵阿羊_None_vless_577
  - 油管绵阿羊_United States_vless_578
  - 油管绵阿羊_None_vless_579
  - 油管绵阿羊_None_vless_580
  - 油管绵阿羊_None_vless_581
  - 油管绵阿羊_None_vless_582
  - 油管绵阿羊_None_vless_583
  - 油管绵阿羊_None_vless_584
  - 油管绵阿羊_None_vless_585
  - 油管绵阿羊_None_vless_586
  - 油管绵阿羊_United States_vless_587
  - 油管绵阿羊_United States_vless_588
  - 油管绵阿羊_United States_vless_589
  - 油管绵阿羊_United States_vless_590
  - 油管绵阿羊_None_vless_591
  - 油管绵阿羊_None_vless_592
  - 油管绵阿羊_United States_vless_593
  - 油管绵阿羊_None_vless_594
  - 油管绵阿羊_None_vless_595
  - 油管绵阿羊_None_vless_596
  - 油管绵阿羊_None_vless_597
  - 油管绵阿羊_None_vless_598
  - 油管绵阿羊_United States_vless_599
  - 油管绵阿羊_Costa Rica_vless_5100
  - 油管绵阿羊_None_vless_5101
  - 油管绵阿羊_None_vless_5102
  - 油管绵阿羊_None_vless_5103
  - 油管绵阿羊_United States_vless_5104
  - 油管绵阿羊_None_vless_5105
  - 油管绵阿羊_United States_vless_5106
  - 油管绵阿羊_None_vless_5107
  - 油管绵阿羊_United States_vless_5108
  - 油管绵阿羊_Netherlands_vless_5109
  - 油管绵阿羊_United States_vless_5110
  - 油管绵阿羊_None_vless_5111
  - 油管绵阿羊_None_vless_5112
  - 油管绵阿羊_Netherlands_vless_5113
  - 油管绵阿羊_United States_vless_5114
  - 油管绵阿羊_None_vless_5115
  - 油管绵阿羊_None_vless_5116
  - 油管绵阿羊_Netherlands_vless_5117
  - 油管绵阿羊_Costa Rica_vless_5118
  - 油管绵阿羊_None_vless_5119
  - 油管绵阿羊_United States_vless_5120
  - 油管绵阿羊_None_vless_5121
  - 油管绵阿羊_None_vless_5122
  - 油管绵阿羊_None_vless_5123
  - 油管绵阿羊_United States_vless_5124
  - 油管绵阿羊_None_vless_5125
  - 油管绵阿羊_None_vless_5126
  - 油管绵阿羊_None_vless_5127
  - 油管绵阿羊_None_vless_5128
  - 油管绵阿羊_None_vless_5129
  - 油管绵阿羊_None_vless_5130
  - 油管绵阿羊_United States_vless_5131
  - 油管绵阿羊_United States_vless_5132
  - 油管绵阿羊_None_vless_5133
  - 油管绵阿羊_Netherlands_vless_5134
  - 油管绵阿羊_None_vless_5135
  - 油管绵阿羊_None_vless_5136
  - 油管绵阿羊_United States_vless_5137
  - 油管绵阿羊_Taiwan_hysteria_61
  - 油管绵阿羊_France_hysteria2_71
  - 油管绵阿羊_United States_hysteria2_81
  - 油管绵阿羊_Taiwan_hysteria_91
  - 油管绵阿羊_France_hy_0
  - 油管绵阿羊_United States_hy_1
  - 油管绵阿羊_Taiwan_hy_2
  - 油管绵阿羊_United States_hy_3
  - 油管绵阿羊_France_hy2_0
  - 油管绵阿羊_United States_hy2_1
  - 油管绵阿羊_France_hy2_2
  - 油管绵阿羊_France_hy2_3
  - 油管绵阿羊_France_reality_2
  - 油管绵阿羊_France_reality_3
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
aHlzdGVyaWEyOi8vZG9uZ3RhaXdhbmcuY29tQDY0LjMxLjU1LjMwOjIwMDExP2luc2VjdXJlPTEmc25pPWJpbmcuY29tJm9iZnM9Jm9iZnMtcGFzc3dvcmQ9I1VuaXRlZCBTdGF0ZXNfaHkyXzAKdHVpYzovLzdiZGEwNmZkLWU0YWYtNDExNS04YWEzLWYwMjE4MzJjZmE3ODpkb25ndGFpd2FuZy5jb21AMTA5LjEwNC4xNTIuMTQ0OjQ0NDExP3NuaT0mY29uZ2VzdGlvbl9jb250cm9sPWJiciZ1ZHBfcmVsYXlfbW9kZT1uYXRpdmUmYWxwbj1oMyZhbGxvd19pbnNlY3VyZT0wI1VuaXRlZCBTdGF0ZXNfdHVpY18xCmh5c3RlcmlhOi8vMTA5LjEwNC4xNTIuMTAxOjMyMjAwP3BlZXI9YmluZy5jb20mYXV0aD0maW5zZWN1cmU9MSZ1cG1icHM9NTAmZG93bm1icHM9ODAmYWxwbj1oMyZtcG9ydD0zMjIwMCZvYmZzPSZwcm90b2NvbD11ZHAmZmFzdG9wZW49MSNVbml0ZWQgU3RhdGVzX2h5XzIKdHVpYzovLzdiZGEwNmZkLWU0YWYtNDExNS04YWEzLWYwMjE4MzJjZmE3ODpkb25ndGFpd2FuZy5jb21AMTA5LjEwNC4xNTIuMTAxOjIyMjg4P3NuaT0mY29uZ2VzdGlvbl9jb250cm9sPWJiciZ1ZHBfcmVsYXlfbW9kZT1uYXRpdmUmYWxwbj1oMyZhbGxvd19pbnNlY3VyZT0wI1VuaXRlZCBTdGF0ZXNfdHVpY18zCnZsZXNzOi8vOWNjMzk0NzctMGQ4NS00NDE5LTg0ZDQtZmI3ZmM3NzY2OGIzQDEwOS4xMDQuMTUyLjEwMToxMTExMT9zZWN1cml0eT1yZWFsaXR5JmFsbG93SW5zZWN1cmUwJmZsb3c9eHRscy1ycHJ4LXZpc2lvbiZ0eXBlPXRjcCZmcD1jaHJvbWUmcGJrPXlLWG1MVG1YQWktQkhCZzNKcEN6LU5XVW1WY0tsZm03aU1tVm9xN1lReDAmc2lkPTZiYTg1MTc5ZTMwZDRmYzImc25pPW0ubWVkaWEtYW1hem9uLmNvbSZzZXJ2aWNlTmFtZT0mcGF0aD0maG9zdD0jVW5pdGVkIFN0YXRlc192bGVzc180CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDE5OC40MS4xOTMuMjI2OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDQuMjcuOTcuOTE6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jTm9uZV92bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDEwOC4xNjIuMTk2LjEwNzo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNVbml0ZWQgU3RhdGVzX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTA0LjIyLjQ2LjI1Mzo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTczLjI0NS40OS41Njo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNGcmFuY2Vfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxOTguNDEuMTk1LjE2ODo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTAzLjIxLjI0NC4xODk6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jVW5pdGVkIFN0YXRlc192bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDEwNC4yMS4zNS4yMjg6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jTm9uZV92bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDE2Mi4xNTkuMzguNzE6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jTm9uZV92bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDEwNC4xOS43LjE1MDo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTA4LjE2Mi4xOTYuNzQ6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jVW5pdGVkIFN0YXRlc192bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDEwNC4xOC45LjE4MTo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTkwLjkzLjI0NS4xODg6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jVW5pdGVkIFN0YXRlc192bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDE5OC40MS4yMTguMTk5OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDQuMTguMTEwLjE2Mzo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTkwLjkzLjI0Ni4xMTQ6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jQ29zdGEgUmljYV92bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDEwMy4yMS4yNDQuMjM2OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I1VuaXRlZCBTdGF0ZXNfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxNjIuMTU5LjI0LjE2Njo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTA0LjI1LjY5LjY5OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDQuMTYuMTk2LjE0Mzo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTAzLjIxLjI0NC4xNjI6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jVW5pdGVkIFN0YXRlc192bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDE3Mi42Ni4xMzguMTQ6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jVW5pdGVkIFN0YXRlc192bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDE3Mi42NC40OS4zMzo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNVbml0ZWQgU3RhdGVzX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTA0LjI1LjExMy4xODY6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jTm9uZV92bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDEwNC4yMC41Ljk6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jTm9uZV92bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDEwNC4yNS4yMTEuMTQ1OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxNzIuNjcuMjA5LjUxOjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I1VuaXRlZCBTdGF0ZXNfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDQuMTguMTQxLjg2OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxODguMTE0Ljk3LjE5OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05ldGhlcmxhbmRzX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTA0LjI3LjE2Ljc1OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDQuMTguOTUuMjM0OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxOTguNDEuMjAyLjk4OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxNjIuMTU5LjI0LjI0NDo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTA0LjI0LjEzMi4yMjg6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jTm9uZV92bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDE5OC40MS4yMDkuMjQ5OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDQuMjQuODguMTk5OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDMuMjEuMjQ0LjI0ODo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNVbml0ZWQgU3RhdGVzX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTA0LjIwLjI1My45Mzo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTczLjI0NS41OC4xODo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNVbml0ZWQgU3RhdGVzX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTA0LjE3LjExLjI1Mjo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTA0LjI0LjE4Ljc6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jTm9uZV92bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDEwNC4xNi4zOC4xNjI6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jTm9uZV92bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDEwOC4xNjIuMTk0LjE0NDo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNVbml0ZWQgU3RhdGVzX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTkwLjkzLjI0NC4yMTg6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jVW5pdGVkIFN0YXRlc192bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDEwNC4xOS40NS4xMTo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTg4LjExNC45Ni4yMTE6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jTmV0aGVybGFuZHNfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxNzIuNjcuMTUyLjIyOjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I1VuaXRlZCBTdGF0ZXNfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDQuMTYuNzUuMTI4OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxOTguNDEuMjAyLjE2OTo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTA0LjI0LjU3LjI0ODo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTczLjI0NS40OS4yMDc6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jRnJhbmNlX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTA0LjI0LjIyNi4xNDM6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jTm9uZV92bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDE3My4yNDUuNTkuMTc6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jVW5pdGVkIFN0YXRlc192bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDEwNC4xNy4yLjM4OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxNjIuMTU5LjYuMTk5OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxNDEuMTAxLjExMy4yMzk6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jTm9uZV92bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDE3Mi42NC4xNzMuMjAwOjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I1VuaXRlZCBTdGF0ZXNfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDQuMjEuMjM1LjEyMjo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTkwLjkzLjI0Ni4xMDc6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jQ29zdGEgUmljYV92bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDE4OC4xMTQuOTcuMjc6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jTmV0aGVybGFuZHNfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxOTAuOTMuMjQ0LjQ3OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I1VuaXRlZCBTdGF0ZXNfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxNzMuMjQ1LjU4LjIzNzo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNVbml0ZWQgU3RhdGVzX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTcyLjY3LjE2Ni43Mjo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNVbml0ZWQgU3RhdGVzX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTkwLjkzLjI0NS4xMDY6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jVW5pdGVkIFN0YXRlc192bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDEwNC4yNy4xMDcuMjIxOjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDMuMjEuMjQ0LjEzNzo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNVbml0ZWQgU3RhdGVzX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTA0LjIyLjcxLjI4OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDQuMTcuMTIzLjUzOjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDQuMjEuMjUuOTU6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jTm9uZV92bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDEwNC4yNC4xOTAuMjI2OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDQuMjcuNjEuNjc6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jTm9uZV92bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDEwNC4yNC4xNzEuMTk1OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxNzMuMjQ1LjQ5LjE5NTo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNGcmFuY2Vfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxOTAuOTMuMjQ3LjU6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jQ29zdGEgUmljYV92bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDEwOC4xNjIuMTkyLjE3OTo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNVbml0ZWQgU3RhdGVzX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTk4LjQxLjIxNi42Mjo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTA0LjE3LjYuMjE4OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDMuMjEuMjQ0LjIxOTo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNVbml0ZWQgU3RhdGVzX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTQxLjEwMS4xMjEuNjk6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jTm9uZV92bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDEwNC4yNS4xMi44ODo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTA0LjI0Ljc0LjI0ODo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTA0LjE4LjkuMjM5OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDQuMTYuMjQ3Ljk1OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDQuMjUuMTkuMzc6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jTm9uZV92bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDEwNC4xOC4yMzguMTE5OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDQuMjQuMjE0LjE4ODo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTcyLjY2LjE0Mi4xMTU6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jVW5pdGVkIFN0YXRlc192bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDEwMy4yMS4yNDQuMTI2OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I1VuaXRlZCBTdGF0ZXNfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDMuMjEuMjQ0Ljc0OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I1VuaXRlZCBTdGF0ZXNfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDMuMjEuMjQ0Ljk0OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I1VuaXRlZCBTdGF0ZXNfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDQuMjAuODcuNzY6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jTm9uZV92bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDEwNC4yNS4xMjIuMTE2OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxOTAuOTMuMjQ1LjY2OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I1VuaXRlZCBTdGF0ZXNfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDQuMTguMjMuMTM2OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDQuMjUuMjU0LjExOjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDQuMjUuOTQuMTc1OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxNDEuMTAxLjEyMS4xODo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTYyLjE1OS4xMzMuNzg6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jTm9uZV92bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDE3My4yNDUuNTkuMTczOjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I1VuaXRlZCBTdGF0ZXNfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxOTAuOTMuMjQ3LjEwNzo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNDb3N0YSBSaWNhX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTYyLjE1OS4yNTIuMjQ5OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDQuMTcuMTIuOTY6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jTm9uZV92bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDE2Mi4xNTkuMjEuNjo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTAzLjIxLjI0NC4xMjU6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jVW5pdGVkIFN0YXRlc192bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDEwNC4xNi4xMzcuMTA2OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxNzIuNjQuMTQ5LjE5Mjo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNVbml0ZWQgU3RhdGVzX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTA0LjI0LjE2LjIyNjo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTcyLjY3LjEwMy4yMjE6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jVW5pdGVkIFN0YXRlc192bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDE4OC4xMTQuOTcuMTExOjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05ldGhlcmxhbmRzX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTcyLjY3LjEwOS41Mzo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNVbml0ZWQgU3RhdGVzX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTA0LjIwLjI1Mi4zNjo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTA0LjIwLjEyNS4xOTM6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jTm9uZV92bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDE4OC4xMTQuOTkuMTIwOjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05ldGhlcmxhbmRzX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTA4LjE2Mi4xOTMuMzc6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jVW5pdGVkIFN0YXRlc192bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDEwNC4xNy4xMDMuMTk0OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxOTguNDEuMjAwLjEzOTo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTg4LjExNC45Ny4yMjI6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jTmV0aGVybGFuZHNfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxOTAuOTMuMjQ3LjY4OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I0Nvc3RhIFJpY2Ffdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDQuMTcuODcuMTEwOjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxNzIuNjcuMTU1Ljc3OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I1VuaXRlZCBTdGF0ZXNfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxNjIuMTU5LjI2LjE1OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxOTguNDEuMjE3LjE1Mjo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTA0LjE4LjI0NC4yMjU6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jTm9uZV92bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDE5MC45My4yNDUuNzM6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jVW5pdGVkIFN0YXRlc192bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDEwNC4yNy40MS4xNTc6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jTm9uZV92bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDE0MS4xMDEuMTIxLjEwNjo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTA0LjI0LjMxLjIwNTo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTk4LjQxLjIyMC41Mzo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTA0LjI0LjE3OC4xMjc6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jTm9uZV92bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDE2Mi4xNTkuMjQwLjE2Nzo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOb25lX3ZsZXNzXzUKdmxlc3M6Ly85NTg3OGFhNS1hNjk1LTRiODgtYjUwMi01NWMwNWM5OThjZjJAMTAzLjIxLjI0NC4xNDE6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jVW5pdGVkIFN0YXRlc192bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDE3Mi42Ny4xOS4yMjQ6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWxnMS5kdGt1NDEueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS91Z3Jsd3MmaG9zdD0jVW5pdGVkIFN0YXRlc192bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDEwNC4yNS4yMjUuMTAxOjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxODguMTE0Ljk2LjE2Mjo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNOZXRoZXJsYW5kc192bGVzc181CnZsZXNzOi8vOTU4NzhhYTUtYTY5NS00Yjg4LWI1MDItNTVjMDVjOTk4Y2YyQDEwNC4xOC4xMzUuMjEyOjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxMDQuMTkuMjQ2LjIyOjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1sZzEuZHRrdTQxLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0vdWdybHdzJmhvc3Q9I05vbmVfdmxlc3NfNQp2bGVzczovLzk1ODc4YWE1LWE2OTUtNGI4OC1iNTAyLTU1YzA1Yzk5OGNmMkAxNzIuNjQuMTY0LjE2Mjo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bGcxLmR0a3U0MS54eXomc2VydmljZU5hbWU9JnBhdGg9L3Vncmx3cyZob3N0PSNVbml0ZWQgU3RhdGVzX3ZsZXNzXzUKaHlzdGVyaWE6Ly93d3cyLmR0a3U0OC54eXo6MjIzMzQ/cGVlcj0mYXV0aD1kb25ndGFpd2FuZy5jb20maW5zZWN1cmU9MSZ1cG1icHM9NTAmZG93bm1icHM9ODAmYWxwbj1oMyZtcG9ydD0yMjMzNCZvYmZzPSZwcm90b2NvbD11ZHAmZmFzdG9wZW49MSNUYWl3YW5faHlfNgpoeXN0ZXJpYTI6Ly9kb25ndGFpd2FuZy5jb21ANTEuMTU4LjU0LjQ2OjQ0NTUwP2luc2VjdXJlPTEmc25pPWJpbmcuY29tJm9iZnM9Jm9iZnMtcGFzc3dvcmQ9I0ZyYW5jZV9oeTJfNwpoeXN0ZXJpYTI6Ly9kMDE3ZTMxNi04MmNiLTQ0MWMtOGVlYS03YjVlOWRlNjRhMjBANDUuMTUwLjE2NS44NDo4ODgxP2luc2VjdXJlPTEmc25pPSZvYmZzPXNhbGFtYW5kZXImb2Jmcy1wYXNzd29yZD1kMDE3ZTMxNi04MmNiLTQ0MWMtOGVlYS03YjVlOWRlNjRhMjAjVW5pdGVkIFN0YXRlc19oeTJfOApoeXN0ZXJpYTovL3d3dy5kdGt1NTAueHl6OjE4NDcwP3BlZXI9d3d3LmFtYXpvbi5jbiZhdXRoPSZpbnNlY3VyZT0xJnVwbWJwcz01MCZkb3dubWJwcz04MCZhbHBuPWgzJm1wb3J0PTE4NDcwJm9iZnM9JnByb3RvY29sPXVkcCZmYXN0b3Blbj0xI1RhaXdhbl9oeV85CmFIUjBjSE02THk5a2IyNW5kR0ZwZDJGdVp5NWpiMjA2Wkc5dVozUmhhWGRoYm1jdVkyOXRRRzVoYVhabE1Ua3VZMlpqWkc0ekxuaDVlam8wTkRNPQphSFIwY0hNNkx5OWtiMjVuZEdGcGQyRnVaeTVqYjIwNlpHOXVaM1JoYVhkaGJtY3VZMjl0UUhkM2R5NWtkR3QxTlRBdWVIbDZPalEwTXc9PQpoeXN0ZXJpYTovLzUxLjE1OC41NC40Njo1NTM5Nj9wZWVyPXlvdWt1LmNvbSZhdXRoPWRvbmd0YWl3YW5nLmNvbSZpbnNlY3VyZT0xJnVwbWJwcz0xMSZkb3dubWJwcz01NSZhbHBuPWgzJm9iZnM9JnByb3RvY29sPXVkcCZmYXN0b3Blbj0xI0ZyYW5jZV9oeXN0ZXJpYV8wCmh5c3RlcmlhOi8vMTczLjIzNC4yNS41Mjo0ODkxOT9wZWVyPWJpbmcuY29tJmF1dGg9ZG9uZ3RhaXdhbmcuY29tJmluc2VjdXJlPTEmdXBtYnBzPTExJmRvd25tYnBzPTU1JmFscG49aDMmb2Jmcz0mcHJvdG9jb2w9dWRwJmZhc3RvcGVuPTEjVW5pdGVkIFN0YXRlc19oeXN0ZXJpYV8xCmh5c3RlcmlhOi8vd3d3LmR0a3U0MC54eXo6MTg0OTA/cGVlcj1iaW5nLmNvbSZhdXRoPWRvbmd0YWl3YW5nLmNvbSZpbnNlY3VyZT0xJnVwbWJwcz0xMSZkb3dubWJwcz01NSZhbHBuPWgzJm9iZnM9JnByb3RvY29sPXVkcCZmYXN0b3Blbj0xI1RhaXdhbl9oeXN0ZXJpYV8yCmh5c3RlcmlhOi8vMTY3LjE2MC45MS4xMTU6NDExODk/cGVlcj13d3cuYW1hem9uLmNuJmF1dGg9YldBd0lxSU5vN1hEbTFmVWxYUUdCaWZWSVhvWXMxeWxnVktxV0ZLeksxWHlES3V3TkYmaW5zZWN1cmU9MSZ1cG1icHM9MTEmZG93bm1icHM9NTUmYWxwbj1oMyZvYmZzPSZwcm90b2NvbD11ZHAmZmFzdG9wZW49MSNVbml0ZWQgU3RhdGVzX2h5c3RlcmlhXzMKaHlzdGVyaWEyOi8vZG9uZ3RhaXdhbmcuY29tQDYyLjIxMC4xMDMuMDoyMjQ4Mz9pbnNlY3VyZT0xJnNuaT13d3cuYmluZy5jb20jRnJhbmNlX2h5c3RlcmlhMl8wCmh5c3RlcmlhMjovL2Rvbmd0YWl3YW5nLmNvbUA2NC4xMTAuMjUuMTE6MzMzMzc/aW5zZWN1cmU9MSZzbmk9d3d3LmJpbmcuY29tI1VuaXRlZCBTdGF0ZXNfaHlzdGVyaWEyXzEKaHlzdGVyaWEyOi8vZG9uZ3RhaXdhbmcuY29tQDYyLjIxMC4xMDMuMDoyMjQ4Mz9pbnNlY3VyZT0xJnNuaT13d3cuYmluZy5jb20jRnJhbmNlX2h5c3RlcmlhMl8yCmh5c3RlcmlhMjovL2Rvbmd0YWl3YW5nLmNvbUA1MS4xNTkuNzcuMTk4OjI5Mjc3P2luc2VjdXJlPTEmc25pPXd3dy5iaW5nLmNvbSNGcmFuY2VfaHlzdGVyaWEyXzMKdmxlc3M6Ly9lNjU5NjYxZC04NDM5LTQ2ZTAtYjFhYi1kNzVjZWFmNzM0MDRANjIuMjEwLjEwMS4wOjE4NzAwP3NlY3VyaXR5PXJlYWxpdHkmYWxsb3dJbnNlY3VyZT0wJmZsb3c9eHRscy1ycHJ4LXZpc2lvbiZ0eXBlPXRjcCZmcD1jaHJvbWUmcGJrPVBCUmMydjlTU1hwRzRqalFSWU5hLWtnczh3OVY0VTNNTkx1bmNkMmQwaHcmc2lkPTZiYTg1MTc5ZTMwZDRmYzImc25pPXVwZGF0ZS5taWNyb3NvZnQmc2VydmljZU5hbWU9JnBhdGg9Jmhvc3Q9I0ZyYW5jZV92bGVzc18yCnZsZXNzOi8vZTY1OTY2MWQtODQzOS00NmUwLWIxYWItZDc1Y2VhZjczNDA0QDYyLjIxMC4xMDEuMDoxODcwMD9zZWN1cml0eT1yZWFsaXR5JmFsbG93SW5zZWN1cmU9MCZmbG93PXh0bHMtcnByeC12aXNpb24mdHlwZT10Y3AmZnA9Y2hyb21lJnBiaz1QQlJjMnY5U1NYcEc0ampRUllOYS1rZ3M4dzlWNFUzTU5MdW5jZDJkMGh3JnNpZD02YmE4NTE3OWUzMGQ0ZmMyJnNuaT11cGRhdGUubWljcm9zb2Z0JnNlcnZpY2VOYW1lPSZwYXRoPSZob3N0PSNGcmFuY2Vfdmxlc3NfMw==
```

## sing-box订阅链接 (https://sing-box-subscribe.vercel.app/config/https:/mareep.netlify.app/sub/merged_proxies_new.yaml)
```yaml
{
  "log": {
    "level": "debug",
    "timestamp": true
  },
  "experimental": {
    "clash_api": {
      "external_controller": "127.0.0.1:9090",
      "external_ui": "ui",
      "secret": "",
      "external_ui_download_url": "https://mirror.ghproxy.com/https://github.com/MetaCubeX/Yacd-meta/archive/gh-pages.zip",
      "external_ui_download_detour": "direct",
      "default_mode": "rule"
    },
    "cache_file": {
      "enabled": true,
      "store_fakeip": false
    }
  },
  "dns": {
    "servers": [
      {
        "tag": "proxyDns",
        "address": "tls://8.8.8.8",
        "detour": "proxy"
      },
      {
        "tag": "localDns",
        "address": "https://223.5.5.5/dns-query",
        "detour": "direct"
      },
      {
        "tag": "block",
        "address": "rcode://success"
      }
    ],
    "rules": [
      {
        "domain": [
          "ghproxy.com",
          "cdn.jsdelivr.net",
          "testingcf.jsdelivr.net"
        ],
        "server": "localDns"
      },
      {
        "rule_set": "geosite-category-ads-all",
        "server": "block"
      },
      {
        "outbound": "any",
        "server": "localDns",
        "disable_cache": true
      },
      {
        "rule_set": "geosite-cn",
        "server": "localDns"
      },
      {
        "clash_mode": "direct",
        "server": "localDns"
      },
      {
        "clash_mode": "global",
        "server": "proxyDns"
      },
      {
        "rule_set": "geosite-geolocation-!cn",
        "server": "proxyDns"
      }
    ],
    "final": "localDns",
    "strategy": "ipv4_only"
  },
  "inbounds": [
    {
      "type": "tun",
      "inet4_address": "172.19.0.1/30",
      "mtu": 9000,
      "auto_route": true,
      "strict_route": true,
      "sniff": true,
      "endpoint_independent_nat": false,
      "stack": "system",
      "platform": {
        "http_proxy": {
          "enabled": true,
          "server": "127.0.0.1",
          "server_port": 2080
        }
      }
    },
    {
      "type": "mixed",
      "listen": "127.0.0.1",
      "listen_port": 2080,
      "sniff": true,
      "users": []
    }
  ],
  "outbounds": [
    {
      "tag": "proxy",
      "type": "selector",
      "outbounds": [
        "auto",
        "direct",
        "🇺🇸 United States_hy2_0",
        "🇺🇸 United States_tuic_1",
        "🇺🇸 United States_tuic_3",
        "🇺🇸 United States_vless_4",
        "None_vless_5",
        "None_vless_52",
        "🇺🇸 United States_vless_5",
        "None_vless_53",
        "🇫🇷 France_vless_5",
        "None_vless_54",
        "🇺🇸 United States_vless_52",
        "None_vless_55",
        "None_vless_56",
        "None_vless_57",
        "🇺🇸 United States_vless_53",
        "None_vless_58",
        "🇺🇸 United States_vless_54",
        "None_vless_59",
        "None_vless_510",
        "🇨🇷 Costa Rica_vless_5",
        "🇺🇸 United States_vless_55",
        "None_vless_511",
        "None_vless_512",
        "None_vless_513",
        "🇺🇸 United States_vless_56",
        "🇺🇸 United States_vless_57",
        "🇺🇸 United States_vless_58",
        "None_vless_514",
        "None_vless_515",
        "None_vless_516",
        "🇺🇸 United States_vless_59",
        "None_vless_517",
        "🇳🇱 Netherlands_vless_5",
        "None_vless_518",
        "None_vless_519",
        "None_vless_520",
        "None_vless_521",
        "None_vless_522",
        "None_vless_523",
        "None_vless_524",
        "🇺🇸 United States_vless_510",
        "None_vless_525",
        "🇺🇸 United States_vless_511",
        "None_vless_526",
        "None_vless_527",
        "None_vless_528",
        "🇺🇸 United States_vless_512",
        "🇺🇸 United States_vless_513",
        "None_vless_529",
        "🇳🇱 Netherlands_vless_52",
        "🇺🇸 United States_vless_514",
        "None_vless_530",
        "None_vless_531",
        "None_vless_532",
        "🇫🇷 France_vless_52",
        "None_vless_533",
        "🇺🇸 United States_vless_515",
        "None_vless_534",
        "None_vless_535",
        "None_vless_536",
        "🇺🇸 United States_vless_516",
        "None_vless_537",
        "🇨🇷 Costa Rica_vless_52",
        "🇳🇱 Netherlands_vless_53",
        "🇺🇸 United States_vless_517",
        "🇺🇸 United States_vless_518",
        "🇺🇸 United States_vless_519",
        "🇺🇸 United States_vless_520",
        "None_vless_538",
        "🇺🇸 United States_vless_521",
        "None_vless_539",
        "None_vless_540",
        "None_vless_541",
        "None_vless_542",
        "None_vless_543",
        "None_vless_544",
        "🇫🇷 France_vless_53",
        "🇨🇷 Costa Rica_vless_53",
        "🇺🇸 United States_vless_522",
        "None_vless_545",
        "None_vless_546",
        "🇺🇸 United States_vless_523",
        "None_vless_547",
        "None_vless_548",
        "None_vless_549",
        "None_vless_550",
        "None_vless_551",
        "None_vless_552",
        "None_vless_553",
        "None_vless_554",
        "🇺🇸 United States_vless_524",
        "🇺🇸 United States_vless_525",
        "🇺🇸 United States_vless_526",
        "🇺🇸 United States_vless_527",
        "None_vless_555",
        "None_vless_556",
        "🇺🇸 United States_vless_528",
        "None_vless_557",
        "None_vless_558",
        "None_vless_559",
        "None_vless_560",
        "None_vless_561",
        "🇺🇸 United States_vless_529",
        "🇨🇷 Costa Rica_vless_54",
        "None_vless_562",
        "None_vless_563",
        "None_vless_564",
        "🇺🇸 United States_vless_530",
        "None_vless_565",
        "🇺🇸 United States_vless_531",
        "None_vless_566",
        "🇺🇸 United States_vless_532",
        "🇳🇱 Netherlands_vless_54",
        "🇺🇸 United States_vless_533",
        "None_vless_567",
        "None_vless_568",
        "🇳🇱 Netherlands_vless_55",
        "🇺🇸 United States_vless_534",
        "None_vless_569",
        "None_vless_570",
        "🇳🇱 Netherlands_vless_56",
        "🇨🇷 Costa Rica_vless_55",
        "None_vless_571",
        "🇺🇸 United States_vless_535",
        "None_vless_572",
        "None_vless_573",
        "None_vless_574",
        "🇺🇸 United States_vless_536",
        "None_vless_575",
        "None_vless_576",
        "None_vless_577",
        "None_vless_578",
        "None_vless_579",
        "None_vless_580",
        "🇺🇸 United States_vless_537",
        "🇺🇸 United States_vless_538",
        "None_vless_581",
        "🇳🇱 Netherlands_vless_57",
        "None_vless_582",
        "None_vless_583",
        "🇺🇸 United States_vless_539",
        "🇹🇼 Taiwan_hy_6",
        "🇫🇷 France_hy2_7",
        "🇺🇸 United States_hy2_8",
        "🇹🇼 Taiwan_hy_9",
        "🇫🇷 France_hysteria_0",
        "🇺🇸 United States_hysteria_1",
        "🇹🇼 Taiwan_hysteria_2",
        "🇺🇸 United States_hysteria_3",
        "🇫🇷 France_hysteria2_0",
        "🇺🇸 United States_hysteria2_1",
        "🇫🇷 France_hysteria2_2",
        "🇫🇷 France_hysteria2_3",
        "🇫🇷 France_vless_2",
        "🇫🇷 France_vless_3"
      ]
    },
    {
      "tag": "OpenAI",
      "type": "selector",
      "outbounds": [
        "TaiWan",
        "Singapore",
        "Japan",
        "America",
        "Others"
      ],
      "default": "America"
    },
    {
      "tag": "Google",
      "type": "selector",
      "outbounds": [
        "HongKong",
        "TaiWan",
        "Singapore",
        "Japan",
        "America",
        "Others"
      ]
    },
    {
      "tag": "Telegram",
      "type": "selector",
      "outbounds": [
        "HongKong",
        "TaiWan",
        "Singapore",
        "Japan",
        "America",
        "Others"
      ]
    },
    {
      "tag": "Twitter",
      "type": "selector",
      "outbounds": [
        "HongKong",
        "TaiWan",
        "Singapore",
        "Japan",
        "America",
        "Others"
      ]
    },
    {
      "tag": "Facebook",
      "type": "selector",
      "outbounds": [
        "HongKong",
        "TaiWan",
        "Singapore",
        "Japan",
        "America",
        "Others"
      ]
    },
    {
      "tag": "BiliBili",
      "type": "selector",
      "outbounds": [
        "direct",
        "HongKong",
        "TaiWan"
      ]
    },
    {
      "tag": "Bahamut",
      "type": "selector",
      "outbounds": [
        "HongKong",
        "TaiWan",
        "Singapore",
        "Japan",
        "America",
        "Others"
      ],
      "default": "TaiWan"
    },
    {
      "tag": "Spotify",
      "type": "selector",
      "outbounds": [
        "HongKong",
        "TaiWan",
        "Singapore",
        "Japan",
        "America",
        "Others"
      ]
    },
    {
      "tag": "TikTok",
      "type": "selector",
      "outbounds": [
        "HongKong",
        "TaiWan",
        "Singapore",
        "Japan",
        "America"
      ],
      "default": "Singapore"
    },
    {
      "tag": "NETFLIX",
      "type": "selector",
      "outbounds": [
        "HongKong",
        "TaiWan",
        "Singapore",
        "Japan",
        "America",
        "Others"
      ]
    },
    {
      "tag": "Disney+",
      "type": "selector",
      "outbounds": [
        "HongKong",
        "TaiWan",
        "Singapore",
        "Japan",
        "America",
        "Others"
      ]
    },
    {
      "tag": "Apple",
      "type": "selector",
      "outbounds": [
        "direct",
        "HongKong",
        "TaiWan",
        "Singapore",
        "Japan",
        "America",
        "Others"
      ]
    },
    {
      "tag": "Microsoft",
      "type": "selector",
      "outbounds": [
        "direct",
        "HongKong",
        "TaiWan",
        "Singapore",
        "Japan",
        "America",
        "Others"
      ]
    },
    {
      "tag": "Games",
      "type": "selector",
      "outbounds": [
        "direct",
        "HongKong",
        "TaiWan",
        "Singapore",
        "Japan",
        "America",
        "Others"
      ]
    },
    {
      "tag": "Streaming",
      "type": "selector",
      "outbounds": [
        "HongKong",
        "TaiWan",
        "Singapore",
        "Japan",
        "America",
        "Others"
      ]
    },
    {
      "tag": "Global",
      "type": "selector",
      "outbounds": [
        "direct",
        "HongKong",
        "TaiWan",
        "Singapore",
        "Japan",
        "America",
        "Others"
      ],
      "default": "HongKong"
    },
    {
      "tag": "China",
      "type": "selector",
      "outbounds": [
        "direct",
        "proxy"
      ]
    },
    {
      "tag": "AdBlock",
      "type": "selector",
      "outbounds": [
        "block",
        "direct"
      ]
    },
    {
      "tag": "HongKong",
      "type": "selector",
      "outbounds": [
        "proxy"
      ]
    },
    {
      "tag": "TaiWan",
      "type": "selector",
      "outbounds": [
        "🇹🇼 Taiwan_hy_6",
        "🇹🇼 Taiwan_hy_9",
        "🇹🇼 Taiwan_hysteria_2",
        "proxy"
      ]
    },
    {
      "tag": "Singapore",
      "type": "selector",
      "outbounds": [
        "proxy"
      ]
    },
    {
      "tag": "Japan",
      "type": "selector",
      "outbounds": [
        "proxy"
      ]
    },
    {
      "tag": "America",
      "type": "selector",
      "outbounds": [
        "🇺🇸 United States_hy2_0",
        "🇺🇸 United States_tuic_1",
        "🇺🇸 United States_tuic_3",
        "🇺🇸 United States_vless_4",
        "🇺🇸 United States_vless_5",
        "🇺🇸 United States_vless_52",
        "🇺🇸 United States_vless_53",
        "🇺🇸 United States_vless_54",
        "🇺🇸 United States_vless_55",
        "🇺🇸 United States_vless_56",
        "🇺🇸 United States_vless_57",
        "🇺🇸 United States_vless_58",
        "🇺🇸 United States_vless_59",
        "🇺🇸 United States_vless_510",
        "🇺🇸 United States_vless_511",
        "🇺🇸 United States_vless_512",
        "🇺🇸 United States_vless_513",
        "🇺🇸 United States_vless_514",
        "🇺🇸 United States_vless_515",
        "🇺🇸 United States_vless_516",
        "🇺🇸 United States_vless_517",
        "🇺🇸 United States_vless_518",
        "🇺🇸 United States_vless_519",
        "🇺🇸 United States_vless_520",
        "🇺🇸 United States_vless_521",
        "🇺🇸 United States_vless_522",
        "🇺🇸 United States_vless_523",
        "🇺🇸 United States_vless_524",
        "🇺🇸 United States_vless_525",
        "🇺🇸 United States_vless_526",
        "🇺🇸 United States_vless_527",
        "🇺🇸 United States_vless_528",
        "🇺🇸 United States_vless_529",
        "🇺🇸 United States_vless_530",
        "🇺🇸 United States_vless_531",
        "🇺🇸 United States_vless_532",
        "🇺🇸 United States_vless_533",
        "🇺🇸 United States_vless_534",
        "🇺🇸 United States_vless_535",
        "🇺🇸 United States_vless_536",
        "🇺🇸 United States_vless_537",
        "🇺🇸 United States_vless_538",
        "🇺🇸 United States_vless_539",
        "🇺🇸 United States_hy2_8",
        "🇺🇸 United States_hysteria_1",
        "🇺🇸 United States_hysteria_3",
        "🇺🇸 United States_hysteria2_1",
        "proxy"
      ]
    },
    {
      "tag": "Others",
      "type": "selector",
      "outbounds": [
        "None_vless_5",
        "None_vless_52",
        "None_vless_53",
        "🇫🇷 France_vless_5",
        "None_vless_54",
        "None_vless_55",
        "None_vless_56",
        "None_vless_57",
        "None_vless_58",
        "None_vless_59",
        "None_vless_510",
        "🇨🇷 Costa Rica_vless_5",
        "None_vless_511",
        "None_vless_512",
        "None_vless_513",
        "None_vless_514",
        "None_vless_515",
        "None_vless_516",
        "None_vless_517",
        "🇳🇱 Netherlands_vless_5",
        "None_vless_518",
        "None_vless_519",
        "None_vless_520",
        "None_vless_521",
        "None_vless_522",
        "None_vless_523",
        "None_vless_524",
        "None_vless_525",
        "None_vless_526",
        "None_vless_527",
        "None_vless_528",
        "None_vless_529",
        "🇳🇱 Netherlands_vless_52",
        "None_vless_530",
        "None_vless_531",
        "None_vless_532",
        "🇫🇷 France_vless_52",
        "None_vless_533",
        "None_vless_534",
        "None_vless_535",
        "None_vless_536",
        "None_vless_537",
        "🇨🇷 Costa Rica_vless_52",
        "🇳🇱 Netherlands_vless_53",
        "None_vless_538",
        "None_vless_539",
        "None_vless_540",
        "None_vless_541",
        "None_vless_542",
        "None_vless_543",
        "None_vless_544",
        "🇫🇷 France_vless_53",
        "🇨🇷 Costa Rica_vless_53",
        "None_vless_545",
        "None_vless_546",
        "None_vless_547",
        "None_vless_548",
        "None_vless_549",
        "None_vless_550",
        "None_vless_551",
        "None_vless_552",
        "None_vless_553",
        "None_vless_554",
        "None_vless_555",
        "None_vless_556",
        "None_vless_557",
        "None_vless_558",
        "None_vless_559",
        "None_vless_560",
        "None_vless_561",
        "🇨🇷 Costa Rica_vless_54",
        "None_vless_562",
        "None_vless_563",
        "None_vless_564",
        "None_vless_565",
        "None_vless_566",
        "🇳🇱 Netherlands_vless_54",
        "None_vless_567",
        "None_vless_568",
        "🇳🇱 Netherlands_vless_55",
        "None_vless_569",
        "None_vless_570",
        "🇳🇱 Netherlands_vless_56",
        "🇨🇷 Costa Rica_vless_55",
        "None_vless_571",
        "None_vless_572",
        "None_vless_573",
        "None_vless_574",
        "None_vless_575",
        "None_vless_576",
        "None_vless_577",
        "None_vless_578",
        "None_vless_579",
        "None_vless_580",
        "None_vless_581",
        "🇳🇱 Netherlands_vless_57",
        "None_vless_582",
        "None_vless_583",
        "🇫🇷 France_hy2_7",
        "🇫🇷 France_hysteria_0",
        "🇫🇷 France_hysteria2_0",
        "🇫🇷 France_hysteria2_2",
        "🇫🇷 France_hysteria2_3",
        "🇫🇷 France_vless_2",
        "🇫🇷 France_vless_3",
        "proxy"
      ]
    },
    {
      "tag": "auto",
      "type": "urltest",
      "outbounds": [
        "🇺🇸 United States_hy2_0",
        "🇺🇸 United States_tuic_1",
        "🇺🇸 United States_tuic_3",
        "🇺🇸 United States_vless_4",
        "None_vless_5",
        "None_vless_52",
        "🇺🇸 United States_vless_5",
        "None_vless_53",
        "🇫🇷 France_vless_5",
        "None_vless_54",
        "🇺🇸 United States_vless_52",
        "None_vless_55",
        "None_vless_56",
        "None_vless_57",
        "🇺🇸 United States_vless_53",
        "None_vless_58",
        "🇺🇸 United States_vless_54",
        "None_vless_59",
        "None_vless_510",
        "🇨🇷 Costa Rica_vless_5",
        "🇺🇸 United States_vless_55",
        "None_vless_511",
        "None_vless_512",
        "None_vless_513",
        "🇺🇸 United States_vless_56",
        "🇺🇸 United States_vless_57",
        "🇺🇸 United States_vless_58",
        "None_vless_514",
        "None_vless_515",
        "None_vless_516",
        "🇺🇸 United States_vless_59",
        "None_vless_517",
        "🇳🇱 Netherlands_vless_5",
        "None_vless_518",
        "None_vless_519",
        "None_vless_520",
        "None_vless_521",
        "None_vless_522",
        "None_vless_523",
        "None_vless_524",
        "🇺🇸 United States_vless_510",
        "None_vless_525",
        "🇺🇸 United States_vless_511",
        "None_vless_526",
        "None_vless_527",
        "None_vless_528",
        "🇺🇸 United States_vless_512",
        "🇺🇸 United States_vless_513",
        "None_vless_529",
        "🇳🇱 Netherlands_vless_52",
        "🇺🇸 United States_vless_514",
        "None_vless_530",
        "None_vless_531",
        "None_vless_532",
        "🇫🇷 France_vless_52",
        "None_vless_533",
        "🇺🇸 United States_vless_515",
        "None_vless_534",
        "None_vless_535",
        "None_vless_536",
        "🇺🇸 United States_vless_516",
        "None_vless_537",
        "🇨🇷 Costa Rica_vless_52",
        "🇳🇱 Netherlands_vless_53",
        "🇺🇸 United States_vless_517",
        "🇺🇸 United States_vless_518",
        "🇺🇸 United States_vless_519",
        "🇺🇸 United States_vless_520",
        "None_vless_538",
        "🇺🇸 United States_vless_521",
        "None_vless_539",
        "None_vless_540",
        "None_vless_541",
        "None_vless_542",
        "None_vless_543",
        "None_vless_544",
        "🇫🇷 France_vless_53",
        "🇨🇷 Costa Rica_vless_53",
        "🇺🇸 United States_vless_522",
        "None_vless_545",
        "None_vless_546",
        "🇺🇸 United States_vless_523",
        "None_vless_547",
        "None_vless_548",
        "None_vless_549",
        "None_vless_550",
        "None_vless_551",
        "None_vless_552",
        "None_vless_553",
        "None_vless_554",
        "🇺🇸 United States_vless_524",
        "🇺🇸 United States_vless_525",
        "🇺🇸 United States_vless_526",
        "🇺🇸 United States_vless_527",
        "None_vless_555",
        "None_vless_556",
        "🇺🇸 United States_vless_528",
        "None_vless_557",
        "None_vless_558",
        "None_vless_559",
        "None_vless_560",
        "None_vless_561",
        "🇺🇸 United States_vless_529",
        "🇨🇷 Costa Rica_vless_54",
        "None_vless_562",
        "None_vless_563",
        "None_vless_564",
        "🇺🇸 United States_vless_530",
        "None_vless_565",
        "🇺🇸 United States_vless_531",
        "None_vless_566",
        "🇺🇸 United States_vless_532",
        "🇳🇱 Netherlands_vless_54",
        "🇺🇸 United States_vless_533",
        "None_vless_567",
        "None_vless_568",
        "🇳🇱 Netherlands_vless_55",
        "🇺🇸 United States_vless_534",
        "None_vless_569",
        "None_vless_570",
        "🇳🇱 Netherlands_vless_56",
        "🇨🇷 Costa Rica_vless_55",
        "None_vless_571",
        "🇺🇸 United States_vless_535",
        "None_vless_572",
        "None_vless_573",
        "None_vless_574",
        "🇺🇸 United States_vless_536",
        "None_vless_575",
        "None_vless_576",
        "None_vless_577",
        "None_vless_578",
        "None_vless_579",
        "None_vless_580",
        "🇺🇸 United States_vless_537",
        "🇺🇸 United States_vless_538",
        "None_vless_581",
        "🇳🇱 Netherlands_vless_57",
        "None_vless_582",
        "None_vless_583",
        "🇺🇸 United States_vless_539",
        "🇹🇼 Taiwan_hy_6",
        "🇫🇷 France_hy2_7",
        "🇺🇸 United States_hy2_8",
        "🇹🇼 Taiwan_hy_9",
        "🇫🇷 France_hysteria_0",
        "🇺🇸 United States_hysteria_1",
        "🇹🇼 Taiwan_hysteria_2",
        "🇺🇸 United States_hysteria_3",
        "🇫🇷 France_hysteria2_0",
        "🇺🇸 United States_hysteria2_1",
        "🇫🇷 France_hysteria2_2",
        "🇫🇷 France_hysteria2_3",
        "🇫🇷 France_vless_2",
        "🇫🇷 France_vless_3"
      ],
      "url": "http://www.gstatic.com/generate_204",
      "interval": "10m",
      "tolerance": 50
    },
    {
      "type": "direct",
      "tag": "direct"
    },
    {
      "type": "dns",
      "tag": "dns-out"
    },
    {
      "type": "block",
      "tag": "block"
    },
    {
      "tag": "🇺🇸 United States_hy2_0",
      "type": "hysteria2",
      "server": "64.31.55.30",
      "server_port": 20011,
      "password": "dongtaiwang.com",
      "up_mbps": 10,
      "down_mbps": 100,
      "tls": {
        "enabled": true,
        "server_name": "bing.com",
        "insecure": true,
        "alpn": [
          "h3"
        ]
      }
    },
    {
      "tag": "🇺🇸 United States_tuic_1",
      "type": "tuic",
      "server": "109.104.152.144",
      "server_port": 44411,
      "uuid": "7bda06fd-e4af-4115-8aa3-f021832cfa78",
      "password": "dongtaiwang.com",
      "congestion_control": "bbr",
      "udp_relay_mode": "native",
      "zero_rtt_handshake": false,
      "heartbeat": "10s",
      "tls": {
        "enabled": true,
        "alpn": [
          "h3"
        ]
      }
    },
    {
      "tag": "🇺🇸 United States_tuic_3",
      "type": "tuic",
      "server": "109.104.152.101",
      "server_port": 22288,
      "uuid": "7bda06fd-e4af-4115-8aa3-f021832cfa78",
      "password": "dongtaiwang.com",
      "congestion_control": "bbr",
      "udp_relay_mode": "native",
      "zero_rtt_handshake": false,
      "heartbeat": "10s",
      "tls": {
        "enabled": true,
        "alpn": [
          "h3"
        ]
      }
    },
    {
      "tag": "🇺🇸 United States_vless_4",
      "type": "vless",
      "server": "109.104.152.101",
      "server_port": 11111,
      "uuid": "9cc39477-0d85-4419-84d4-fb7fc77668b3",
      "packet_encoding": "xudp",
      "flow": "xtls-rprx-vision",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "m.media-amazon.com",
        "utls": {
          "enabled": true,
          "fingerprint": "chrome"
        },
        "reality": {
          "enabled": true,
          "public_key": "yKXmLTmXAi-BHBg3JpCz-NWUmVcKlfm7iMmVoq7YQx0",
          "short_id": "6ba85179e30d4fc2"
        }
      }
    },
    {
      "tag": "None_vless_5",
      "type": "vless",
      "server": "198.41.193.226",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_52",
      "type": "vless",
      "server": "104.27.97.91",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_5",
      "type": "vless",
      "server": "108.162.196.107",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_53",
      "type": "vless",
      "server": "104.22.46.253",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇫🇷 France_vless_5",
      "type": "vless",
      "server": "173.245.49.56",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_54",
      "type": "vless",
      "server": "198.41.195.168",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_52",
      "type": "vless",
      "server": "103.21.244.189",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_55",
      "type": "vless",
      "server": "104.21.35.228",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_56",
      "type": "vless",
      "server": "162.159.38.71",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_57",
      "type": "vless",
      "server": "104.19.7.150",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_53",
      "type": "vless",
      "server": "108.162.196.74",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_58",
      "type": "vless",
      "server": "104.18.9.181",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_54",
      "type": "vless",
      "server": "190.93.245.188",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_59",
      "type": "vless",
      "server": "198.41.218.199",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_510",
      "type": "vless",
      "server": "104.18.110.163",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇨🇷 Costa Rica_vless_5",
      "type": "vless",
      "server": "190.93.246.114",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_55",
      "type": "vless",
      "server": "103.21.244.236",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_511",
      "type": "vless",
      "server": "162.159.24.166",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_512",
      "type": "vless",
      "server": "104.25.69.69",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_513",
      "type": "vless",
      "server": "104.16.196.143",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_56",
      "type": "vless",
      "server": "103.21.244.162",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_57",
      "type": "vless",
      "server": "172.66.138.14",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_58",
      "type": "vless",
      "server": "172.64.49.33",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_514",
      "type": "vless",
      "server": "104.25.113.186",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_515",
      "type": "vless",
      "server": "104.20.5.9",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_516",
      "type": "vless",
      "server": "104.25.211.145",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_59",
      "type": "vless",
      "server": "172.67.209.51",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_517",
      "type": "vless",
      "server": "104.18.141.86",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇳🇱 Netherlands_vless_5",
      "type": "vless",
      "server": "188.114.97.19",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_518",
      "type": "vless",
      "server": "104.27.16.75",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_519",
      "type": "vless",
      "server": "104.18.95.234",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_520",
      "type": "vless",
      "server": "198.41.202.98",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_521",
      "type": "vless",
      "server": "162.159.24.244",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_522",
      "type": "vless",
      "server": "104.24.132.228",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_523",
      "type": "vless",
      "server": "198.41.209.249",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_524",
      "type": "vless",
      "server": "104.24.88.199",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_510",
      "type": "vless",
      "server": "103.21.244.248",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_525",
      "type": "vless",
      "server": "104.20.253.93",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_511",
      "type": "vless",
      "server": "173.245.58.18",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_526",
      "type": "vless",
      "server": "104.17.11.252",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_527",
      "type": "vless",
      "server": "104.24.18.7",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_528",
      "type": "vless",
      "server": "104.16.38.162",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_512",
      "type": "vless",
      "server": "108.162.194.144",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_513",
      "type": "vless",
      "server": "190.93.244.218",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_529",
      "type": "vless",
      "server": "104.19.45.11",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇳🇱 Netherlands_vless_52",
      "type": "vless",
      "server": "188.114.96.211",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_514",
      "type": "vless",
      "server": "172.67.152.22",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_530",
      "type": "vless",
      "server": "104.16.75.128",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_531",
      "type": "vless",
      "server": "198.41.202.169",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_532",
      "type": "vless",
      "server": "104.24.57.248",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇫🇷 France_vless_52",
      "type": "vless",
      "server": "173.245.49.207",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_533",
      "type": "vless",
      "server": "104.24.226.143",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_515",
      "type": "vless",
      "server": "173.245.59.17",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_534",
      "type": "vless",
      "server": "104.17.2.38",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_535",
      "type": "vless",
      "server": "162.159.6.199",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_536",
      "type": "vless",
      "server": "141.101.113.239",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_516",
      "type": "vless",
      "server": "172.64.173.200",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_537",
      "type": "vless",
      "server": "104.21.235.122",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇨🇷 Costa Rica_vless_52",
      "type": "vless",
      "server": "190.93.246.107",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇳🇱 Netherlands_vless_53",
      "type": "vless",
      "server": "188.114.97.27",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_517",
      "type": "vless",
      "server": "190.93.244.47",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_518",
      "type": "vless",
      "server": "173.245.58.237",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_519",
      "type": "vless",
      "server": "172.67.166.72",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_520",
      "type": "vless",
      "server": "190.93.245.106",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_538",
      "type": "vless",
      "server": "104.27.107.221",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_521",
      "type": "vless",
      "server": "103.21.244.137",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_539",
      "type": "vless",
      "server": "104.22.71.28",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_540",
      "type": "vless",
      "server": "104.17.123.53",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_541",
      "type": "vless",
      "server": "104.21.25.95",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_542",
      "type": "vless",
      "server": "104.24.190.226",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_543",
      "type": "vless",
      "server": "104.27.61.67",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_544",
      "type": "vless",
      "server": "104.24.171.195",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇫🇷 France_vless_53",
      "type": "vless",
      "server": "173.245.49.195",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇨🇷 Costa Rica_vless_53",
      "type": "vless",
      "server": "190.93.247.5",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_522",
      "type": "vless",
      "server": "108.162.192.179",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_545",
      "type": "vless",
      "server": "198.41.216.62",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_546",
      "type": "vless",
      "server": "104.17.6.218",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_523",
      "type": "vless",
      "server": "103.21.244.219",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_547",
      "type": "vless",
      "server": "141.101.121.69",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_548",
      "type": "vless",
      "server": "104.25.12.88",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_549",
      "type": "vless",
      "server": "104.24.74.248",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_550",
      "type": "vless",
      "server": "104.18.9.239",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_551",
      "type": "vless",
      "server": "104.16.247.95",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_552",
      "type": "vless",
      "server": "104.25.19.37",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_553",
      "type": "vless",
      "server": "104.18.238.119",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_554",
      "type": "vless",
      "server": "104.24.214.188",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_524",
      "type": "vless",
      "server": "172.66.142.115",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_525",
      "type": "vless",
      "server": "103.21.244.126",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_526",
      "type": "vless",
      "server": "103.21.244.74",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_527",
      "type": "vless",
      "server": "103.21.244.94",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_555",
      "type": "vless",
      "server": "104.20.87.76",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_556",
      "type": "vless",
      "server": "104.25.122.116",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_528",
      "type": "vless",
      "server": "190.93.245.66",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_557",
      "type": "vless",
      "server": "104.18.23.136",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_558",
      "type": "vless",
      "server": "104.25.254.11",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_559",
      "type": "vless",
      "server": "104.25.94.175",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_560",
      "type": "vless",
      "server": "141.101.121.18",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_561",
      "type": "vless",
      "server": "162.159.133.78",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_529",
      "type": "vless",
      "server": "173.245.59.173",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇨🇷 Costa Rica_vless_54",
      "type": "vless",
      "server": "190.93.247.107",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_562",
      "type": "vless",
      "server": "162.159.252.249",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_563",
      "type": "vless",
      "server": "104.17.12.96",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_564",
      "type": "vless",
      "server": "162.159.21.6",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_530",
      "type": "vless",
      "server": "103.21.244.125",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_565",
      "type": "vless",
      "server": "104.16.137.106",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_531",
      "type": "vless",
      "server": "172.64.149.192",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_566",
      "type": "vless",
      "server": "104.24.16.226",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_532",
      "type": "vless",
      "server": "172.67.103.221",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇳🇱 Netherlands_vless_54",
      "type": "vless",
      "server": "188.114.97.111",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_533",
      "type": "vless",
      "server": "172.67.109.53",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_567",
      "type": "vless",
      "server": "104.20.252.36",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_568",
      "type": "vless",
      "server": "104.20.125.193",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇳🇱 Netherlands_vless_55",
      "type": "vless",
      "server": "188.114.99.120",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_534",
      "type": "vless",
      "server": "108.162.193.37",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_569",
      "type": "vless",
      "server": "104.17.103.194",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_570",
      "type": "vless",
      "server": "198.41.200.139",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇳🇱 Netherlands_vless_56",
      "type": "vless",
      "server": "188.114.97.222",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇨🇷 Costa Rica_vless_55",
      "type": "vless",
      "server": "190.93.247.68",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_571",
      "type": "vless",
      "server": "104.17.87.110",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_535",
      "type": "vless",
      "server": "172.67.155.77",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_572",
      "type": "vless",
      "server": "162.159.26.15",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_573",
      "type": "vless",
      "server": "198.41.217.152",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_574",
      "type": "vless",
      "server": "104.18.244.225",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_536",
      "type": "vless",
      "server": "190.93.245.73",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_575",
      "type": "vless",
      "server": "104.27.41.157",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_576",
      "type": "vless",
      "server": "141.101.121.106",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_577",
      "type": "vless",
      "server": "104.24.31.205",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_578",
      "type": "vless",
      "server": "198.41.220.53",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_579",
      "type": "vless",
      "server": "104.24.178.127",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_580",
      "type": "vless",
      "server": "162.159.240.167",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_537",
      "type": "vless",
      "server": "103.21.244.141",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_538",
      "type": "vless",
      "server": "172.67.19.224",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_581",
      "type": "vless",
      "server": "104.25.225.101",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇳🇱 Netherlands_vless_57",
      "type": "vless",
      "server": "188.114.96.162",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_582",
      "type": "vless",
      "server": "104.18.135.212",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "None_vless_583",
      "type": "vless",
      "server": "104.19.246.22",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_vless_539",
      "type": "vless",
      "server": "172.64.164.162",
      "server_port": 443,
      "uuid": "95878aa5-a695-4b88-b502-55c05c998cf2",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "lg1.dtku41.xyz"
      },
      "transport": {
        "type": "ws",
        "path": "/ugrlws",
        "headers": {
          "Host": "lg1.dtku41.xyz"
        }
      }
    },
    {
      "tag": "🇹🇼 Taiwan_hy_6",
      "type": "hysteria",
      "server": "www2.dtku48.xyz",
      "server_port": 22334,
      "up_mbps": 50,
      "down_mbps": 80,
      "auth_str": "dongtaiwang.com",
      "tls": {
        "enabled": true,
        "server_name": "",
        "alpn": [
          "h3"
        ],
        "insecure": true
      }
    },
    {
      "tag": "🇫🇷 France_hy2_7",
      "type": "hysteria2",
      "server": "51.158.54.46",
      "server_port": 44550,
      "password": "dongtaiwang.com",
      "up_mbps": 10,
      "down_mbps": 100,
      "tls": {
        "enabled": true,
        "server_name": "bing.com",
        "insecure": true,
        "alpn": [
          "h3"
        ]
      }
    },
    {
      "tag": "🇺🇸 United States_hy2_8",
      "type": "hysteria2",
      "server": "45.150.165.84",
      "server_port": 8881,
      "password": "d017e316-82cb-441c-8eea-7b5e9de64a20",
      "up_mbps": 10,
      "down_mbps": 100,
      "tls": {
        "enabled": true,
        "insecure": true,
        "alpn": [
          "h3"
        ]
      },
      "obfs": {
        "type": "salamander",
        "password": "d017e316-82cb-441c-8eea-7b5e9de64a20"
      }
    },
    {
      "tag": "🇹🇼 Taiwan_hy_9",
      "type": "hysteria",
      "server": "www.dtku50.xyz",
      "server_port": 18470,
      "up_mbps": 50,
      "down_mbps": 80,
      "auth_str": "",
      "tls": {
        "enabled": true,
        "server_name": "www.amazon.cn",
        "alpn": [
          "h3"
        ],
        "insecure": true
      }
    },
    {
      "tag": "🇫🇷 France_hysteria_0",
      "type": "hysteria",
      "server": "51.158.54.46",
      "server_port": 55396,
      "up_mbps": 11,
      "down_mbps": 55,
      "auth_str": "dongtaiwang.com",
      "tls": {
        "enabled": true,
        "server_name": "youku.com",
        "alpn": [
          "h3"
        ],
        "insecure": true
      }
    },
    {
      "tag": "🇺🇸 United States_hysteria_1",
      "type": "hysteria",
      "server": "173.234.25.52",
      "server_port": 48919,
      "up_mbps": 11,
      "down_mbps": 55,
      "auth_str": "dongtaiwang.com",
      "tls": {
        "enabled": true,
        "server_name": "bing.com",
        "alpn": [
          "h3"
        ],
        "insecure": true
      }
    },
    {
      "tag": "🇹🇼 Taiwan_hysteria_2",
      "type": "hysteria",
      "server": "www.dtku40.xyz",
      "server_port": 18490,
      "up_mbps": 11,
      "down_mbps": 55,
      "auth_str": "dongtaiwang.com",
      "tls": {
        "enabled": true,
        "server_name": "bing.com",
        "alpn": [
          "h3"
        ],
        "insecure": true
      }
    },
    {
      "tag": "🇺🇸 United States_hysteria_3",
      "type": "hysteria",
      "server": "167.160.91.115",
      "server_port": 41189,
      "up_mbps": 11,
      "down_mbps": 55,
      "auth_str": "bWAwIqINo7XDm1fUlXQGBifVIXoYs1ylgVKqWFKzK1XyDKuwNF",
      "tls": {
        "enabled": true,
        "server_name": "www.amazon.cn",
        "alpn": [
          "h3"
        ],
        "insecure": true
      }
    },
    {
      "tag": "🇫🇷 France_hysteria2_0",
      "type": "hysteria2",
      "server": "62.210.103.0",
      "server_port": 22483,
      "password": "dongtaiwang.com",
      "up_mbps": 10,
      "down_mbps": 100,
      "tls": {
        "enabled": true,
        "server_name": "www.bing.com",
        "insecure": true,
        "alpn": [
          "h3"
        ]
      }
    },
    {
      "tag": "🇺🇸 United States_hysteria2_1",
      "type": "hysteria2",
      "server": "64.110.25.11",
      "server_port": 33337,
      "password": "dongtaiwang.com",
      "up_mbps": 10,
      "down_mbps": 100,
      "tls": {
        "enabled": true,
        "server_name": "www.bing.com",
        "insecure": true,
        "alpn": [
          "h3"
        ]
      }
    },
    {
      "tag": "🇫🇷 France_hysteria2_2",
      "type": "hysteria2",
      "server": "62.210.103.0",
      "server_port": 22483,
      "password": "dongtaiwang.com",
      "up_mbps": 10,
      "down_mbps": 100,
      "tls": {
        "enabled": true,
        "server_name": "www.bing.com",
        "insecure": true,
        "alpn": [
          "h3"
        ]
      }
    },
    {
      "tag": "🇫🇷 France_hysteria2_3",
      "type": "hysteria2",
      "server": "51.159.77.198",
      "server_port": 29277,
      "password": "dongtaiwang.com",
      "up_mbps": 10,
      "down_mbps": 100,
      "tls": {
        "enabled": true,
        "server_name": "www.bing.com",
        "insecure": true,
        "alpn": [
          "h3"
        ]
      }
    },
    {
      "tag": "🇫🇷 France_vless_2",
      "type": "vless",
      "server": "62.210.101.0",
      "server_port": 18700,
      "uuid": "e659661d-8439-46e0-b1ab-d75ceaf73404",
      "packet_encoding": "xudp",
      "flow": "xtls-rprx-vision",
      "tls": {
        "enabled": true,
        "insecure": false,
        "server_name": "update.microsoft",
        "utls": {
          "enabled": true,
          "fingerprint": "chrome"
        },
        "reality": {
          "enabled": true,
          "public_key": "PBRc2v9SSXpG4jjQRYNa-kgs8w9V4U3MNLuncd2d0hw",
          "short_id": "6ba85179e30d4fc2"
        }
      }
    },
    {
      "tag": "🇫🇷 France_vless_3",
      "type": "vless",
      "server": "62.210.101.0",
      "server_port": 18700,
      "uuid": "e659661d-8439-46e0-b1ab-d75ceaf73404",
      "packet_encoding": "xudp",
      "flow": "xtls-rprx-vision",
      "tls": {
        "enabled": true,
        "insecure": false,
        "server_name": "update.microsoft",
        "utls": {
          "enabled": true,
          "fingerprint": "chrome"
        },
        "reality": {
          "enabled": true,
          "public_key": "PBRc2v9SSXpG4jjQRYNa-kgs8w9V4U3MNLuncd2d0hw",
          "short_id": "6ba85179e30d4fc2"
        }
      }
    }
  ],
  "route": {
    "auto_detect_interface": true,
    "final": "proxy",
    "rules": [
      {
        "protocol": "dns",
        "outbound": "dns-out"
      },
      {
        "port": 53,
        "outbound": "dns-out"
      },
      {
        "network": "udp",
        "port": 443,
        "outbound": "block"
      },
      {
        "rule_set": "geosite-category-ads-all",
        "outbound": "AdBlock"
      },
      {
        "clash_mode": "direct",
        "outbound": "direct"
      },
      {
        "clash_mode": "global",
        "outbound": "proxy"
      },
      {
        "domain": [
          "clash.razord.top",
          "yacd.metacubex.one",
          "yacd.haishan.me",
          "d.metacubex.one"
        ],
        "outbound": "direct"
      },
      {
        "rule_set": "geosite-openai",
        "outbound": "OpenAI"
      },
      {
        "rule_set": "geosite-youtube",
        "outbound": "Google"
      },
      {
        "rule_set": "geoip-google",
        "outbound": "Google"
      },
      {
        "rule_set": "geosite-google",
        "outbound": "Google"
      },
      {
        "rule_set": "geosite-github",
        "outbound": "Google"
      },
      {
        "rule_set": "geoip-telegram",
        "outbound": "Telegram"
      },
      {
        "rule_set": "geosite-telegram",
        "outbound": "Telegram"
      },
      {
        "rule_set": "geoip-twitter",
        "outbound": "Twitter"
      },
      {
        "rule_set": "geosite-twitter",
        "outbound": "Twitter"
      },
      {
        "rule_set": "geoip-facebook",
        "outbound": "Facebook"
      },
      {
        "rule_set": [
          "geosite-facebook",
          "geosite-instagram"
        ],
        "outbound": "Facebook"
      },
      {
        "rule_set": "geoip-bilibili",
        "outbound": "BiliBili"
      },
      {
        "rule_set": "geosite-bilibili",
        "outbound": "BiliBili"
      },
      {
        "rule_set": "geosite-bahamut",
        "outbound": "Bahamut"
      },
      {
        "rule_set": "geosite-spotify",
        "outbound": "Spotify"
      },
      {
        "rule_set": "geosite-tiktok",
        "outbound": "TikTok"
      },
      {
        "rule_set": "geoip-netflix",
        "outbound": "NETFLIX"
      },
      {
        "rule_set": "geosite-netflix",
        "outbound": "NETFLIX"
      },
      {
        "rule_set": "geosite-disney",
        "outbound": "Disney+"
      },
      {
        "rule_set": "geosite-apple",
        "outbound": "Apple"
      },
      {
        "rule_set": "geosite-amazon",
        "outbound": "Apple"
      },
      {
        "rule_set": "geosite-microsoft",
        "outbound": "Microsoft"
      },
      {
        "rule_set": "geosite-category-games",
        "outbound": "Games"
      },
      {
        "rule_set": "geosite-hbo",
        "outbound": "Streaming"
      },
      {
        "rule_set": "geosite-primevideo",
        "outbound": "Streaming"
      },
      {
        "rule_set": "geosite-geolocation-!cn",
        "outbound": "Global"
      },
      {
        "rule_set": "geosite-private",
        "outbound": "direct"
      },
      {
        "ip_is_private": true,
        "outbound": "direct"
      },
      {
        "rule_set": "geoip-cn",
        "outbound": "China"
      },
      {
        "rule_set": "geosite-cn",
        "outbound": "China"
      }
    ],
    "rule_set": [
      {
        "tag": "geoip-google",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geoip/google.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geoip-telegram",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geoip/telegram.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geoip-twitter",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geoip/twitter.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geoip-facebook",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geoip/facebook.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geoip-netflix",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geoip/netflix.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geoip-apple",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo-lite/geoip/apple.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geoip-bilibili",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo-lite/geoip/bilibili.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geoip-cn",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geoip/cn.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geosite-private",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/private.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geosite-openai",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/openai.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geosite-youtube",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/youtube.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geosite-google",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/google.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geosite-github",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/github.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geosite-telegram",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/telegram.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geosite-twitter",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/twitter.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geosite-facebook",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/facebook.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geosite-instagram",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/instagram.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geosite-bilibili",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/bilibili.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geosite-bahamut",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/bahamut.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geosite-spotify",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/spotify.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geosite-tiktok",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/tiktok.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geosite-netflix",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/netflix.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geosite-disney",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/disney.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geosite-apple",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/apple.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geosite-amazon",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/amazon.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geosite-microsoft",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/microsoft.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geosite-category-games",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/category-games.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geosite-hbo",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/hbo.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geosite-primevideo",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/primevideo.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geosite-cn",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/cn.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geosite-geolocation-!cn",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/geolocation-!cn.srs",
        "download_detour": "direct"
      },
      {
        "tag": "geosite-category-ads-all",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/category-ads-all.srs",
        "download_detour": "direct"
      }
    ]
  }
}
```


