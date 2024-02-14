
---
title: VPN合集
date: 2024-02-14 22:18:39
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

> Last Update Time: 2024-02-14 22:18:39
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
185.199.109.133               avatars.githubusercontent.com
185.199.109.133               avatars0.githubusercontent.com
185.199.109.133               avatars1.githubusercontent.com
185.199.109.133               avatars2.githubusercontent.com
185.199.109.133               avatars3.githubusercontent.com
185.199.109.133               avatars4.githubusercontent.com
185.199.109.133               avatars5.githubusercontent.com
185.199.109.133               camo.githubusercontent.com
140.82.112.21                 central.github.com
185.199.109.133               cloud.githubusercontent.com
140.82.112.10                 codeload.github.com
140.82.113.22                 collector.github.com
185.199.109.133               desktop.githubusercontent.com
185.199.109.133               favicons.githubusercontent.com
140.82.113.4                  gist.github.com
52.216.9.35                   github-cloud.s3.amazonaws.com
52.217.141.137                github-com.s3.amazonaws.com
54.231.161.153                github-production-release-asset-2e65be.s3.amazonaws.com
54.231.170.49                 github-production-repository-file-5c1aeb.s3.amazonaws.com
52.217.230.249                github-production-user-asset-6210df.s3.amazonaws.com
192.0.66.2                    github.blog
140.82.113.3                  github.com
140.82.113.18                 github.community
185.199.109.154               github.githubassets.com
151.101.193.194               github.global.ssl.fastly.net
185.199.109.153               github.io
185.199.109.133               github.map.fastly.net
185.199.109.153               githubstatus.com
140.82.113.26                 live.github.com
185.199.109.133               media.githubusercontent.com
185.199.109.133               objects.githubusercontent.com
13.107.42.16                  pipelines.actions.githubusercontent.com
185.199.109.133               raw.githubusercontent.com
185.199.109.133               user-images.githubusercontent.com
13.107.253.40                 vscode.dev
140.82.112.21                 education.github.com


# Update time: 2024-02-15T06:05:06+08:00
# Update url: https://raw.hellogithub.com/hosts
# Star me: https://github.com/521xueweihan/GitHub520
# GitHub520 Host End

```

该内容会自动定时更新， 数据更新时间：2024-02-15T06:05:06+08:00

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
  port: 18810
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
- name: 油管绵阿羊_None_vmess_51
  type: vmess
  server: 104.27.100.158
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_52
  type: vmess
  server: 172.71.191.55
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_53
  type: vmess
  server: 173.245.53.36
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_54
  type: vmess
  server: 103.22.201.156
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_55
  type: vmess
  server: 103.21.245.212
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_56
  type: vmess
  server: 103.21.246.99
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_57
  type: vmess
  server: 104.16.247.113
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Brazil_vmess_58
  type: vmess
  server: 172.70.101.28
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_59
  type: vmess
  server: 103.21.247.250
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_510
  type: vmess
  server: 173.245.56.169
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_511
  type: vmess
  server: 104.25.108.118
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_512
  type: vmess
  server: 108.162.235.211
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_513
  type: vmess
  server: 172.68.140.197
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_514
  type: vmess
  server: 103.22.202.12
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_515
  type: vmess
  server: 162.158.174.197
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Italy_vmess_516
  type: vmess
  server: 162.158.130.24
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_517
  type: vmess
  server: 108.162.205.223
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_518
  type: vmess
  server: 103.31.7.84
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Singapore_vmess_519
  type: vmess
  server: 103.22.200.144
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_520
  type: vmess
  server: 104.27.2.100
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Singapore_vmess_521
  type: vmess
  server: 103.22.200.178
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_522
  type: vmess
  server: 104.21.183.7
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_523
  type: vmess
  server: 190.93.251.226
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_524
  type: vmess
  server: 190.93.249.156
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_525
  type: vmess
  server: 103.22.201.147
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_526
  type: vmess
  server: 104.26.254.37
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_527
  type: vmess
  server: 104.19.224.51
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_528
  type: vmess
  server: 103.21.247.54
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_529
  type: vmess
  server: 198.41.132.133
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_530
  type: vmess
  server: 108.162.197.250
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_531
  type: vmess
  server: 162.159.148.101
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_532
  type: vmess
  server: 197.234.241.108
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_533
  type: vmess
  server: 131.0.72.103
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Netherlands_vmess_534
  type: vmess
  server: 188.114.99.214
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_535
  type: vmess
  server: 190.93.240.255
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_536
  type: vmess
  server: 190.93.248.186
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_537
  type: vmess
  server: 108.162.194.168
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_538
  type: vmess
  server: 188.114.111.9
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_539
  type: vmess
  server: 103.21.247.149
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_540
  type: vmess
  server: 172.65.50.58
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_541
  type: vmess
  server: 190.93.252.24
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_542
  type: vmess
  server: 190.93.243.54
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Netherlands_vmess_543
  type: vmess
  server: 188.114.97.10
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_544
  type: vmess
  server: 197.234.241.220
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_545
  type: vmess
  server: 188.114.109.114
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_546
  type: vmess
  server: 198.41.221.172
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_547
  type: vmess
  server: 104.20.34.65
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_548
  type: vmess
  server: 141.101.115.83
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_549
  type: vmess
  server: 103.31.4.142
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_550
  type: vmess
  server: 104.25.238.161
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_551
  type: vmess
  server: 197.234.243.213
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_552
  type: vmess
  server: 104.26.80.152
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_553
  type: vmess
  server: 141.101.103.145
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_554
  type: vmess
  server: 197.234.241.170
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_555
  type: vmess
  server: 131.0.75.123
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_556
  type: vmess
  server: 190.93.240.5
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Singapore_vmess_557
  type: vmess
  server: 103.22.200.14
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_558
  type: vmess
  server: 162.159.185.156
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Italy_vmess_559
  type: vmess
  server: 188.114.101.14
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Rwanda_vmess_560
  type: vmess
  server: 197.234.244.0
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_561
  type: vmess
  server: 173.245.60.72
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_562
  type: vmess
  server: 198.41.168.157
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_563
  type: vmess
  server: 141.101.81.8
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_564
  type: vmess
  server: 198.41.150.222
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_565
  type: vmess
  server: 173.245.63.169
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United Arab Emirates_vmess_566
  type: vmess
  server: 162.158.56.82
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_567
  type: vmess
  server: 103.31.7.104
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_568
  type: vmess
  server: 162.159.47.234
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Germany_vmess_569
  type: vmess
  server: 198.41.240.118
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_570
  type: vmess
  server: 173.245.62.53
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_571
  type: vmess
  server: 188.114.108.244
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_572
  type: vmess
  server: 131.0.72.55
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_573
  type: vmess
  server: 104.18.72.220
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_574
  type: vmess
  server: 131.0.75.75
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_575
  type: vmess
  server: 197.234.242.120
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_576
  type: vmess
  server: 104.17.202.31
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_577
  type: vmess
  server: 104.22.127.181
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_578
  type: vmess
  server: 190.93.246.52
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_579
  type: vmess
  server: 103.22.201.135
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_580
  type: vmess
  server: 103.31.6.42
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Netherlands_vmess_581
  type: vmess
  server: 188.114.96.176
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_582
  type: vmess
  server: 172.67.147.235
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Singapore_vmess_583
  type: vmess
  server: 103.22.200.20
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_584
  type: vmess
  server: 104.26.71.143
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_585
  type: vmess
  server: 197.234.243.175
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_586
  type: vmess
  server: 103.31.4.89
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Canada_vmess_587
  type: vmess
  server: 108.162.241.204
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_588
  type: vmess
  server: 198.41.213.177
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_589
  type: vmess
  server: 131.0.73.214
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_590
  type: vmess
  server: 162.158.62.179
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_591
  type: vmess
  server: 197.234.240.102
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_592
  type: vmess
  server: 103.21.247.104
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_593
  type: vmess
  server: 173.245.50.171
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_594
  type: vmess
  server: 190.93.242.13
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_595
  type: vmess
  server: 108.162.204.246
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_596
  type: vmess
  server: 197.234.241.141
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_597
  type: vmess
  server: 198.41.167.243
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_598
  type: vmess
  server: 198.41.149.172
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_599
  type: vmess
  server: 103.22.201.183
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5100
  type: vmess
  server: 173.245.48.104
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Italy_vmess_5101
  type: vmess
  server: 188.114.102.50
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5102
  type: vmess
  server: 104.16.179.215
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5103
  type: vmess
  server: 108.162.255.194
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5104
  type: vmess
  server: 103.21.246.136
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_5105
  type: vmess
  server: 188.114.110.12
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_India_vmess_5106
  type: vmess
  server: 198.41.245.136
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5107
  type: vmess
  server: 197.234.240.71
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5108
  type: vmess
  server: 141.101.72.166
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5109
  type: vmess
  server: 198.41.138.80
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Netherlands_vmess_5110
  type: vmess
  server: 141.101.64.90
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5111
  type: vmess
  server: 198.41.167.75
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5112
  type: vmess
  server: 172.69.115.24
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5113
  type: vmess
  server: 141.101.101.197
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5114
  type: vmess
  server: 104.23.144.174
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5115
  type: vmess
  server: 188.114.105.231
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5116
  type: vmess
  server: 108.162.208.228
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5117
  type: vmess
  server: 172.67.124.71
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5118
  type: vmess
  server: 103.31.4.12
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5119
  type: vmess
  server: 190.93.250.184
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5120
  type: vmess
  server: 104.26.134.119
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5121
  type: vmess
  server: 108.162.204.20
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5122
  type: vmess
  server: 162.159.127.42
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5123
  type: vmess
  server: 197.234.243.27
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5124
  type: vmess
  server: 104.25.39.131
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5125
  type: vmess
  server: 197.234.243.221
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5126
  type: vmess
  server: 188.114.104.26
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5127
  type: vmess
  server: 104.23.28.91
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5128
  type: vmess
  server: 104.25.127.175
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5129
  type: vmess
  server: 103.31.6.6
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5130
  type: vmess
  server: 197.234.240.17
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5131
  type: vmess
  server: 108.162.231.169
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Oman_vmess_5132
  type: vmess
  server: 162.158.30.253
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Netherlands_vmess_5133
  type: vmess
  server: 172.71.33.232
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5134
  type: vmess
  server: 141.101.117.0
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5135
  type: vmess
  server: 162.159.21.221
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5136
  type: vmess
  server: 131.0.75.157
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5137
  type: vmess
  server: 198.41.237.218
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5138
  type: vmess
  server: 141.101.115.108
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_France_vmess_5139
  type: vmess
  server: 141.101.69.145
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5140
  type: vmess
  server: 108.162.200.150
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5141
  type: vmess
  server: 104.26.124.107
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5142
  type: vmess
  server: 103.21.246.243
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5143
  type: vmess
  server: 173.245.60.253
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5144
  type: vmess
  server: 103.21.247.150
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5145
  type: vmess
  server: 103.22.202.166
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5146
  type: vmess
  server: 197.234.242.87
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Belgium_vmess_5147
  type: vmess
  server: 162.158.234.135
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5148
  type: vmess
  server: 104.26.67.200
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5149
  type: vmess
  server: 108.162.254.119
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5150
  type: vmess
  server: 108.162.247.50
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5151
  type: vmess
  server: 103.21.245.40
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Singapore_vmess_5152
  type: vmess
  server: 103.22.200.195
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5153
  type: vmess
  server: 108.162.230.241
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Czechia_vmess_5154
  type: vmess
  server: 141.101.94.232
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Hong Kong_vmess_5155
  type: vmess
  server: 103.22.203.206
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5156
  type: vmess
  server: 103.31.4.8
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5157
  type: vmess
  server: 103.31.4.183
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5158
  type: vmess
  server: 197.234.243.83
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5159
  type: vmess
  server: 162.159.174.65
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5160
  type: vmess
  server: 172.71.65.156
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5161
  type: vmess
  server: 172.65.47.50
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5162
  type: vmess
  server: 131.0.72.181
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5163
  type: vmess
  server: 103.31.6.183
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5164
  type: vmess
  server: 104.20.168.253
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5165
  type: vmess
  server: 172.71.169.103
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5166
  type: vmess
  server: 104.18.210.222
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5167
  type: vmess
  server: 131.0.72.107
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5168
  type: vmess
  server: 198.41.164.109
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5169
  type: vmess
  server: 103.21.247.211
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5170
  type: vmess
  server: 104.16.26.237
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5171
  type: vmess
  server: 108.162.211.129
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5172
  type: vmess
  server: 104.17.73.225
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5173
  type: vmess
  server: 103.22.201.121
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5174
  type: vmess
  server: 104.27.53.186
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5175
  type: vmess
  server: 162.158.81.180
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5176
  type: vmess
  server: 172.64.43.54
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5177
  type: vmess
  server: 141.101.126.126
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5178
  type: vmess
  server: 104.27.236.105
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5179
  type: vmess
  server: 103.31.5.56
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_5180
  type: vmess
  server: 188.114.111.22
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5181
  type: vmess
  server: 190.93.255.176
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Hong Kong_vmess_5182
  type: vmess
  server: 103.22.203.197
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5183
  type: vmess
  server: 108.162.193.186
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5184
  type: vmess
  server: 162.159.3.105
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5185
  type: vmess
  server: 197.234.243.209
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5186
  type: vmess
  server: 173.245.50.86
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5187
  type: vmess
  server: 173.245.51.74
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5188
  type: vmess
  server: 190.93.245.201
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5189
  type: vmess
  server: 141.101.113.233
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5190
  type: vmess
  server: 173.245.50.43
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Hong Kong_vmess_5191
  type: vmess
  server: 103.22.203.42
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5192
  type: vmess
  server: 103.31.7.68
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5193
  type: vmess
  server: 104.25.187.144
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5194
  type: vmess
  server: 103.22.201.219
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5195
  type: vmess
  server: 141.101.117.240
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5196
  type: vmess
  server: 108.162.216.2
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5197
  type: vmess
  server: 131.0.72.154
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5198
  type: vmess
  server: 190.93.248.59
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_5199
  type: vmess
  server: 188.114.107.39
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Ecuador_vmess_5200
  type: vmess
  server: 162.158.255.144
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Netherlands_vmess_5201
  type: vmess
  server: 188.114.97.79
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5202
  type: vmess
  server: 103.21.245.1
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5203
  type: vmess
  server: 104.25.53.152
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Netherlands_vmess_5204
  type: vmess
  server: 141.101.75.187
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5205
  type: vmess
  server: 188.114.105.9
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5206
  type: vmess
  server: 197.234.240.39
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_5207
  type: vmess
  server: 188.114.109.98
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5208
  type: vmess
  server: 198.41.192.45
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Italy_vmess_5209
  type: vmess
  server: 188.114.100.224
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Brazil_vmess_5210
  type: vmess
  server: 172.69.147.103
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5211
  type: vmess
  server: 198.41.178.32
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5212
  type: vmess
  server: 103.31.4.238
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5213
  type: vmess
  server: 131.0.72.30
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5214
  type: vmess
  server: 197.234.242.22
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5215
  type: vmess
  server: 172.64.50.224
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5216
  type: vmess
  server: 104.27.124.207
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5217
  type: vmess
  server: 190.93.242.26
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5218
  type: vmess
  server: 172.70.22.17
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5219
  type: vmess
  server: 197.234.240.106
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5220
  type: vmess
  server: 104.26.197.150
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5221
  type: vmess
  server: 173.245.51.137
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_5222
  type: vmess
  server: 188.114.110.115
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5223
  type: vmess
  server: 103.22.202.124
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5224
  type: vmess
  server: 197.234.242.202
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5225
  type: vmess
  server: 197.234.242.180
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5226
  type: vmess
  server: 103.22.202.43
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5227
  type: vmess
  server: 172.70.35.202
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5228
  type: vmess
  server: 103.22.201.182
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5229
  type: vmess
  server: 172.70.126.41
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5230
  type: vmess
  server: 197.234.240.113
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5231
  type: vmess
  server: 103.21.246.201
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5232
  type: vmess
  server: 141.101.116.197
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Italy_vmess_5233
  type: vmess
  server: 188.114.100.206
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5234
  type: vmess
  server: 173.245.60.225
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5235
  type: vmess
  server: 198.41.147.162
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5236
  type: vmess
  server: 141.101.103.244
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5237
  type: vmess
  server: 104.21.150.131
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5238
  type: vmess
  server: 131.0.75.189
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5239
  type: vmess
  server: 103.31.4.127
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5240
  type: vmess
  server: 190.93.251.106
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5241
  type: vmess
  server: 190.93.250.239
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5242
  type: vmess
  server: 103.22.201.155
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5243
  type: vmess
  server: 172.67.146.122
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5244
  type: vmess
  server: 104.25.70.12
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5245
  type: vmess
  server: 172.64.161.49
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_5246
  type: vmess
  server: 188.114.106.244
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5247
  type: vmess
  server: 172.64.20.161
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5248
  type: vmess
  server: 190.93.247.25
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5249
  type: vmess
  server: 103.21.245.53
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5250
  type: vmess
  server: 104.26.28.199
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5251
  type: vmess
  server: 198.41.144.73
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5252
  type: vmess
  server: 103.21.245.82
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5253
  type: vmess
  server: 108.162.213.55
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5254
  type: vmess
  server: 172.66.67.222
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5255
  type: vmess
  server: 173.245.51.243
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5256
  type: vmess
  server: 108.162.207.216
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_France_vmess_5257
  type: vmess
  server: 173.245.49.96
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5258
  type: vmess
  server: 141.101.72.37
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5259
  type: vmess
  server: 103.31.4.99
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5260
  type: vmess
  server: 108.162.198.160
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5261
  type: vmess
  server: 108.162.214.193
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5262
  type: vmess
  server: 173.245.56.255
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5263
  type: vmess
  server: 103.21.246.32
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5264
  type: vmess
  server: 188.114.104.209
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5265
  type: vmess
  server: 190.93.252.107
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Hong Kong_vmess_5266
  type: vmess
  server: 103.22.203.67
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5267
  type: vmess
  server: 190.93.248.126
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5268
  type: vmess
  server: 198.41.217.250
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5269
  type: vmess
  server: 103.21.244.162
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5270
  type: vmess
  server: 141.101.123.118
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5271
  type: vmess
  server: 173.245.52.216
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5272
  type: vmess
  server: 103.21.245.135
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5273
  type: vmess
  server: 198.41.151.2
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Brazil_vmess_5274
  type: vmess
  server: 172.71.2.250
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5275
  type: vmess
  server: 103.22.201.195
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5276
  type: vmess
  server: 162.158.187.78
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Austria_vmess_5277
  type: vmess
  server: 108.162.220.59
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5278
  type: vmess
  server: 190.93.249.193
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5279
  type: vmess
  server: 198.41.208.175
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5280
  type: vmess
  server: 104.27.111.75
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5281
  type: vmess
  server: 103.31.7.146
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5282
  type: vmess
  server: 131.0.72.149
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5283
  type: vmess
  server: 173.245.51.23
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5284
  type: vmess
  server: 103.21.246.130
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5285
  type: vmess
  server: 197.234.243.25
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5286
  type: vmess
  server: 173.245.48.139
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5287
  type: vmess
  server: 103.22.202.212
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5288
  type: vmess
  server: 141.101.80.108
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5289
  type: vmess
  server: 104.20.28.184
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_5290
  type: vmess
  server: 188.114.107.12
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Singapore_vmess_5291
  type: vmess
  server: 103.22.200.203
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5292
  type: vmess
  server: 108.162.209.41
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Canada_vmess_5293
  type: vmess
  server: 108.162.240.45
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5294
  type: vmess
  server: 104.18.216.212
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5295
  type: vmess
  server: 162.159.103.149
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5296
  type: vmess
  server: 104.25.148.207
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5297
  type: vmess
  server: 103.31.7.189
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5298
  type: vmess
  server: 108.162.251.114
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5299
  type: vmess
  server: 198.41.128.243
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5300
  type: vmess
  server: 103.31.5.233
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5301
  type: vmess
  server: 131.0.73.54
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5302
  type: vmess
  server: 103.31.4.19
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5303
  type: vmess
  server: 131.0.75.29
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5304
  type: vmess
  server: 197.234.240.142
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5305
  type: vmess
  server: 104.17.17.78
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5306
  type: vmess
  server: 190.93.250.199
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Singapore_vmess_5307
  type: vmess
  server: 162.158.171.93
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5308
  type: vmess
  server: 104.25.106.201
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5309
  type: vmess
  server: 162.158.177.127
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5310
  type: vmess
  server: 141.101.113.229
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5311
  type: vmess
  server: 103.31.5.205
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5312
  type: vmess
  server: 104.21.175.247
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Italy_vmess_5313
  type: vmess
  server: 162.158.131.177
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5314
  type: vmess
  server: 197.234.243.68
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Singapore_vmess_5315
  type: vmess
  server: 103.22.200.71
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Hong Kong_vmess_5316
  type: vmess
  server: 103.22.203.70
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5317
  type: vmess
  server: 104.25.149.63
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5318
  type: vmess
  server: 104.24.112.113
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5319
  type: vmess
  server: 104.25.81.142
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5320
  type: vmess
  server: 104.17.123.43
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5321
  type: vmess
  server: 173.245.48.208
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5322
  type: vmess
  server: 103.31.4.62
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5323
  type: vmess
  server: 131.0.72.121
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5324
  type: vmess
  server: 103.21.247.42
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5325
  type: vmess
  server: 131.0.74.255
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5326
  type: vmess
  server: 141.101.117.164
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5327
  type: vmess
  server: 103.22.201.133
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5328
  type: vmess
  server: 198.41.202.129
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_5329
  type: vmess
  server: 188.114.110.237
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5330
  type: vmess
  server: 162.159.71.101
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5331
  type: vmess
  server: 188.114.105.253
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5332
  type: vmess
  server: 172.67.126.180
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_India_vmess_5333
  type: vmess
  server: 172.69.118.194
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United Kingdom_vmess_5334
  type: vmess
  server: 141.101.70.231
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5335
  type: vmess
  server: 172.68.84.232
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5336
  type: vmess
  server: 103.21.244.255
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Hong Kong_vmess_5337
  type: vmess
  server: 103.22.203.245
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5338
  type: vmess
  server: 131.0.73.192
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5339
  type: vmess
  server: 103.31.4.214
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5340
  type: vmess
  server: 104.16.43.142
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5341
  type: vmess
  server: 141.101.109.248
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5342
  type: vmess
  server: 103.21.246.1
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5343
  type: vmess
  server: 190.93.242.178
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5344
  type: vmess
  server: 131.0.72.53
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5345
  type: vmess
  server: 104.19.217.124
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5346
  type: vmess
  server: 104.25.191.172
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5347
  type: vmess
  server: 198.41.217.201
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5348
  type: vmess
  server: 108.162.194.78
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5349
  type: vmess
  server: 172.64.156.232
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5350
  type: vmess
  server: 104.17.202.186
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5351
  type: vmess
  server: 172.71.189.182
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5352
  type: vmess
  server: 172.65.151.57
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5353
  type: vmess
  server: 103.21.245.208
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5354
  type: vmess
  server: 198.41.157.190
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5355
  type: vmess
  server: 162.159.64.132
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5356
  type: vmess
  server: 172.65.174.157
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5357
  type: vmess
  server: 197.234.241.241
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5358
  type: vmess
  server: 104.26.87.35
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5359
  type: vmess
  server: 173.245.58.249
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Czechia_vmess_5360
  type: vmess
  server: 141.101.96.43
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5361
  type: vmess
  server: 103.31.5.127
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5362
  type: vmess
  server: 104.22.169.204
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5363
  type: vmess
  server: 104.22.145.104
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5364
  type: vmess
  server: 173.245.56.143
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5365
  type: vmess
  server: 197.234.240.162
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5366
  type: vmess
  server: 104.23.61.193
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5367
  type: vmess
  server: 141.101.123.178
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5368
  type: vmess
  server: 190.93.241.223
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5369
  type: vmess
  server: 104.25.149.178
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Netherlands_vmess_5370
  type: vmess
  server: 188.114.99.31
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5371
  type: vmess
  server: 103.21.245.218
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5372
  type: vmess
  server: 197.234.242.7
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5373
  type: vmess
  server: 131.0.74.43
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5374
  type: vmess
  server: 190.93.244.172
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5375
  type: vmess
  server: 190.93.248.108
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5376
  type: vmess
  server: 173.245.53.60
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Italy_vmess_5377
  type: vmess
  server: 188.114.101.98
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United Kingdom_vmess_5378
  type: vmess
  server: 141.101.98.11
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5379
  type: vmess
  server: 103.21.246.7
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5380
  type: vmess
  server: 103.31.6.52
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5381
  type: vmess
  server: 131.0.73.202
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5382
  type: vmess
  server: 104.24.41.195
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5383
  type: vmess
  server: 197.234.240.205
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5384
  type: vmess
  server: 103.21.246.189
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5385
  type: vmess
  server: 141.101.114.179
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5386
  type: vmess
  server: 198.41.203.91
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5387
  type: vmess
  server: 198.41.161.104
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5388
  type: vmess
  server: 131.0.73.247
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5389
  type: vmess
  server: 198.41.165.178
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_5390
  type: vmess
  server: 188.114.106.136
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5391
  type: vmess
  server: 131.0.73.205
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5392
  type: vmess
  server: 108.162.230.132
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5393
  type: vmess
  server: 103.22.202.140
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5394
  type: vmess
  server: 103.21.246.254
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Hong Kong_vmess_5395
  type: vmess
  server: 103.22.203.105
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5396
  type: vmess
  server: 103.31.5.69
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5397
  type: vmess
  server: 198.41.156.253
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5398
  type: vmess
  server: 198.41.158.146
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5399
  type: vmess
  server: 198.41.171.79
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5400
  type: vmess
  server: 103.21.245.235
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5401
  type: vmess
  server: 197.234.242.179
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5402
  type: vmess
  server: 173.245.60.108
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5403
  type: vmess
  server: 131.0.73.244
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5404
  type: vmess
  server: 172.71.195.141
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5405
  type: vmess
  server: 103.21.245.210
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5406
  type: vmess
  server: 198.41.144.37
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5407
  type: vmess
  server: 103.21.247.184
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Singapore_vmess_5408
  type: vmess
  server: 172.70.141.93
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5409
  type: vmess
  server: 103.31.4.124
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5410
  type: vmess
  server: 104.27.3.220
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5411
  type: vmess
  server: 104.17.57.138
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_5412
  type: vmess
  server: 188.114.106.127
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Hong Kong_vmess_5413
  type: vmess
  server: 103.22.203.110
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5414
  type: vmess
  server: 141.101.119.56
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5415
  type: vmess
  server: 198.41.148.103
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5416
  type: vmess
  server: 103.21.247.93
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5417
  type: vmess
  server: 172.66.178.100
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5418
  type: vmess
  server: 188.114.105.48
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5419
  type: vmess
  server: 131.0.74.22
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5420
  type: vmess
  server: 131.0.72.23
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5421
  type: vmess
  server: 172.70.11.190
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5422
  type: vmess
  server: 190.93.252.191
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5423
  type: vmess
  server: 103.22.202.86
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5424
  type: vmess
  server: 197.234.243.94
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5425
  type: vmess
  server: 108.162.192.90
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5426
  type: vmess
  server: 103.31.4.235
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Korea_vmess_5427
  type: vmess
  server: 141.101.83.236
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5428
  type: vmess
  server: 141.101.73.233
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5429
  type: vmess
  server: 108.162.235.207
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5430
  type: vmess
  server: 104.23.46.116
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5431
  type: vmess
  server: 198.41.199.133
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5432
  type: vmess
  server: 173.245.59.231
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5433
  type: vmess
  server: 103.31.4.133
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5434
  type: vmess
  server: 141.101.107.227
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5435
  type: vmess
  server: 103.22.201.96
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5436
  type: vmess
  server: 131.0.72.187
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5437
  type: vmess
  server: 103.31.5.78
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5438
  type: vmess
  server: 108.162.205.155
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5439
  type: vmess
  server: 108.162.245.83
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5440
  type: vmess
  server: 173.245.61.105
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5441
  type: vmess
  server: 104.22.148.29
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Netherlands_vmess_5442
  type: vmess
  server: 141.101.64.153
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5443
  type: vmess
  server: 103.21.247.226
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5444
  type: vmess
  server: 104.24.46.240
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5445
  type: vmess
  server: 197.234.243.15
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5446
  type: vmess
  server: 131.0.72.135
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5447
  type: vmess
  server: 173.245.56.49
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5448
  type: vmess
  server: 103.31.4.162
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5449
  type: vmess
  server: 198.41.247.90
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Kenya_vmess_5450
  type: vmess
  server: 162.158.40.96
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5451
  type: vmess
  server: 173.245.50.11
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5452
  type: vmess
  server: 141.101.89.12
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5453
  type: vmess
  server: 104.19.250.206
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_5454
  type: vmess
  server: 188.114.109.168
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5455
  type: vmess
  server: 131.0.74.69
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5456
  type: vmess
  server: 173.245.51.60
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Germany_vmess_5457
  type: vmess
  server: 198.41.242.150
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5458
  type: vmess
  server: 108.162.244.5
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5459
  type: vmess
  server: 104.23.194.210
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5460
  type: vmess
  server: 190.93.242.203
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5461
  type: vmess
  server: 198.41.198.197
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Paraguay_vmess_5462
  type: vmess
  server: 162.158.147.180
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5463
  type: vmess
  server: 108.162.248.57
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5464
  type: vmess
  server: 103.21.246.158
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5465
  type: vmess
  server: 197.234.242.187
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5466
  type: vmess
  server: 162.159.144.195
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5467
  type: vmess
  server: 108.162.223.111
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5468
  type: vmess
  server: 103.31.5.225
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_5469
  type: vmess
  server: 188.114.110.83
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5470
  type: vmess
  server: 108.162.232.20
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5471
  type: vmess
  server: 173.245.63.226
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5472
  type: vmess
  server: 198.41.218.111
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5473
  type: vmess
  server: 104.26.241.105
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5474
  type: vmess
  server: 104.25.132.70
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Germany_vmess_5475
  type: vmess
  server: 162.158.112.108
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_India_vmess_5476
  type: vmess
  server: 172.70.63.62
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5477
  type: vmess
  server: 131.0.73.5
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5478
  type: vmess
  server: 141.101.124.147
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Germany_vmess_5479
  type: vmess
  server: 162.158.87.59
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Netherlands_vmess_5480
  type: vmess
  server: 172.71.46.11
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5481
  type: vmess
  server: 108.162.233.73
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5482
  type: vmess
  server: 173.245.58.183
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Italy_vmess_5483
  type: vmess
  server: 188.114.102.26
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5484
  type: vmess
  server: 103.21.245.55
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5485
  type: vmess
  server: 172.65.226.175
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5486
  type: vmess
  server: 141.101.114.104
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5487
  type: vmess
  server: 162.159.244.158
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5488
  type: vmess
  server: 190.93.245.147
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5489
  type: vmess
  server: 198.41.189.192
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5490
  type: vmess
  server: 131.0.72.158
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5491
  type: vmess
  server: 104.21.16.29
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5492
  type: vmess
  server: 104.22.174.180
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5493
  type: vmess
  server: 131.0.74.204
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5494
  type: vmess
  server: 108.162.246.49
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5495
  type: vmess
  server: 103.31.4.186
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5496
  type: vmess
  server: 141.101.79.187
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Netherlands_vmess_5497
  type: vmess
  server: 188.114.98.87
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5498
  type: vmess
  server: 103.22.201.107
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5499
  type: vmess
  server: 131.0.74.245
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
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
  - 油管绵阿羊_None_vmess_51
  - 油管绵阿羊_United States_vmess_52
  - 油管绵阿羊_United States_vmess_53
  - 油管绵阿羊_Japan_vmess_54
  - 油管绵阿羊_Australia_vmess_55
  - 油管绵阿羊_United States_vmess_56
  - 油管绵阿羊_None_vmess_57
  - 油管绵阿羊_Brazil_vmess_58
  - 油管绵阿羊_United States_vmess_59
  - 油管绵阿羊_United States_vmess_510
  - 油管绵阿羊_None_vmess_511
  - 油管绵阿羊_United States_vmess_512
  - 油管绵阿羊_South Africa_vmess_513
  - 油管绵阿羊_Japan_vmess_514
  - 油管绵阿羊_United States_vmess_515
  - 油管绵阿羊_Italy_vmess_516
  - 油管绵阿羊_United States_vmess_517
  - 油管绵阿羊_United States_vmess_518
  - 油管绵阿羊_Singapore_vmess_519
  - 油管绵阿羊_None_vmess_520
  - 油管绵阿羊_Singapore_vmess_521
  - 油管绵阿羊_None_vmess_522
  - 油管绵阿羊_Costa Rica_vmess_523
  - 油管绵阿羊_Costa Rica_vmess_524
  - 油管绵阿羊_Japan_vmess_525
  - 油管绵阿羊_None_vmess_526
  - 油管绵阿羊_None_vmess_527
  - 油管绵阿羊_United States_vmess_528
  - 油管绵阿羊_United States_vmess_529
  - 油管绵阿羊_United States_vmess_530
  - 油管绵阿羊_None_vmess_531
  - 油管绵阿羊_South Africa_vmess_532
  - 油管绵阿羊_Costa Rica_vmess_533
  - 油管绵阿羊_Netherlands_vmess_534
  - 油管绵阿羊_Costa Rica_vmess_535
  - 油管绵阿羊_Costa Rica_vmess_536
  - 油管绵阿羊_United States_vmess_537
  - 油管绵阿羊_Spain_vmess_538
  - 油管绵阿羊_United States_vmess_539
  - 油管绵阿羊_United States_vmess_540
  - 油管绵阿羊_Costa Rica_vmess_541
  - 油管绵阿羊_Costa Rica_vmess_542
  - 油管绵阿羊_Netherlands_vmess_543
  - 油管绵阿羊_South Africa_vmess_544
  - 油管绵阿羊_Spain_vmess_545
  - 油管绵阿羊_None_vmess_546
  - 油管绵阿羊_None_vmess_547
  - 油管绵阿羊_None_vmess_548
  - 油管绵阿羊_United States_vmess_549
  - 油管绵阿羊_None_vmess_550
  - 油管绵阿羊_South Africa_vmess_551
  - 油管绵阿羊_None_vmess_552
  - 油管绵阿羊_United States_vmess_553
  - 油管绵阿羊_South Africa_vmess_554
  - 油管绵阿羊_Costa Rica_vmess_555
  - 油管绵阿羊_Costa Rica_vmess_556
  - 油管绵阿羊_Singapore_vmess_557
  - 油管绵阿羊_None_vmess_558
  - 油管绵阿羊_Italy_vmess_559
  - 油管绵阿羊_Rwanda_vmess_560
  - 油管绵阿羊_United States_vmess_561
  - 油管绵阿羊_United States_vmess_562
  - 油管绵阿羊_United States_vmess_563
  - 油管绵阿羊_United States_vmess_564
  - 油管绵阿羊_United States_vmess_565
  - 油管绵阿羊_United Arab Emirates_vmess_566
  - 油管绵阿羊_United States_vmess_567
  - 油管绵阿羊_None_vmess_568
  - 油管绵阿羊_Germany_vmess_569
  - 油管绵阿羊_United States_vmess_570
  - 油管绵阿羊_Spain_vmess_571
  - 油管绵阿羊_Costa Rica_vmess_572
  - 油管绵阿羊_None_vmess_573
  - 油管绵阿羊_Costa Rica_vmess_574
  - 油管绵阿羊_South Africa_vmess_575
  - 油管绵阿羊_None_vmess_576
  - 油管绵阿羊_None_vmess_577
  - 油管绵阿羊_Costa Rica_vmess_578
  - 油管绵阿羊_Japan_vmess_579
  - 油管绵阿羊_United States_vmess_580
  - 油管绵阿羊_Netherlands_vmess_581
  - 油管绵阿羊_United States_vmess_582
  - 油管绵阿羊_Singapore_vmess_583
  - 油管绵阿羊_None_vmess_584
  - 油管绵阿羊_South Africa_vmess_585
  - 油管绵阿羊_United States_vmess_586
  - 油管绵阿羊_Canada_vmess_587
  - 油管绵阿羊_None_vmess_588
  - 油管绵阿羊_Costa Rica_vmess_589
  - 油管绵阿羊_United States_vmess_590
  - 油管绵阿羊_South Africa_vmess_591
  - 油管绵阿羊_United States_vmess_592
  - 油管绵阿羊_United States_vmess_593
  - 油管绵阿羊_Costa Rica_vmess_594
  - 油管绵阿羊_United States_vmess_595
  - 油管绵阿羊_South Africa_vmess_596
  - 油管绵阿羊_United States_vmess_597
  - 油管绵阿羊_United States_vmess_598
  - 油管绵阿羊_Japan_vmess_599
  - 油管绵阿羊_United States_vmess_5100
  - 油管绵阿羊_Italy_vmess_5101
  - 油管绵阿羊_None_vmess_5102
  - 油管绵阿羊_Australia_vmess_5103
  - 油管绵阿羊_United States_vmess_5104
  - 油管绵阿羊_Spain_vmess_5105
  - 油管绵阿羊_India_vmess_5106
  - 油管绵阿羊_South Africa_vmess_5107
  - 油管绵阿羊_United States_vmess_5108
  - 油管绵阿羊_United States_vmess_5109
  - 油管绵阿羊_Netherlands_vmess_5110
  - 油管绵阿羊_United States_vmess_5111
  - 油管绵阿羊_United States_vmess_5112
  - 油管绵阿羊_United States_vmess_5113
  - 油管绵阿羊_None_vmess_5114
  - 油管绵阿羊_United States_vmess_5115
  - 油管绵阿羊_United States_vmess_5116
  - 油管绵阿羊_United States_vmess_5117
  - 油管绵阿羊_United States_vmess_5118
  - 油管绵阿羊_Costa Rica_vmess_5119
  - 油管绵阿羊_None_vmess_5120
  - 油管绵阿羊_United States_vmess_5121
  - 油管绵阿羊_None_vmess_5122
  - 油管绵阿羊_South Africa_vmess_5123
  - 油管绵阿羊_None_vmess_5124
  - 油管绵阿羊_South Africa_vmess_5125
  - 油管绵阿羊_United States_vmess_5126
  - 油管绵阿羊_None_vmess_5127
  - 油管绵阿羊_None_vmess_5128
  - 油管绵阿羊_United States_vmess_5129
  - 油管绵阿羊_South Africa_vmess_5130
  - 油管绵阿羊_United States_vmess_5131
  - 油管绵阿羊_Oman_vmess_5132
  - 油管绵阿羊_Netherlands_vmess_5133
  - 油管绵阿羊_None_vmess_5134
  - 油管绵阿羊_None_vmess_5135
  - 油管绵阿羊_Costa Rica_vmess_5136
  - 油管绵阿羊_United States_vmess_5137
  - 油管绵阿羊_None_vmess_5138
  - 油管绵阿羊_France_vmess_5139
  - 油管绵阿羊_United States_vmess_5140
  - 油管绵阿羊_None_vmess_5141
  - 油管绵阿羊_United States_vmess_5142
  - 油管绵阿羊_United States_vmess_5143
  - 油管绵阿羊_United States_vmess_5144
  - 油管绵阿羊_Japan_vmess_5145
  - 油管绵阿羊_South Africa_vmess_5146
  - 油管绵阿羊_Belgium_vmess_5147
  - 油管绵阿羊_None_vmess_5148
  - 油管绵阿羊_Australia_vmess_5149
  - 油管绵阿羊_Australia_vmess_5150
  - 油管绵阿羊_Australia_vmess_5151
  - 油管绵阿羊_Singapore_vmess_5152
  - 油管绵阿羊_United States_vmess_5153
  - 油管绵阿羊_Czechia_vmess_5154
  - 油管绵阿羊_Hong Kong_vmess_5155
  - 油管绵阿羊_United States_vmess_5156
  - 油管绵阿羊_United States_vmess_5157
  - 油管绵阿羊_South Africa_vmess_5158
  - 油管绵阿羊_None_vmess_5159
  - 油管绵阿羊_United States_vmess_5160
  - 油管绵阿羊_United States_vmess_5161
  - 油管绵阿羊_Costa Rica_vmess_5162
  - 油管绵阿羊_United States_vmess_5163
  - 油管绵阿羊_None_vmess_5164
  - 油管绵阿羊_United States_vmess_5165
  - 油管绵阿羊_None_vmess_5166
  - 油管绵阿羊_Costa Rica_vmess_5167
  - 油管绵阿羊_United States_vmess_5168
  - 油管绵阿羊_United States_vmess_5169
  - 油管绵阿羊_None_vmess_5170
  - 油管绵阿羊_United States_vmess_5171
  - 油管绵阿羊_None_vmess_5172
  - 油管绵阿羊_Japan_vmess_5173
  - 油管绵阿羊_None_vmess_5174
  - 油管绵阿羊_Costa Rica_vmess_5175
  - 油管绵阿羊_United States_vmess_5176
  - 油管绵阿羊_None_vmess_5177
  - 油管绵阿羊_None_vmess_5178
  - 油管绵阿羊_United States_vmess_5179
  - 油管绵阿羊_Spain_vmess_5180
  - 油管绵阿羊_Costa Rica_vmess_5181
  - 油管绵阿羊_Hong Kong_vmess_5182
  - 油管绵阿羊_United States_vmess_5183
  - 油管绵阿羊_None_vmess_5184
  - 油管绵阿羊_South Africa_vmess_5185
  - 油管绵阿羊_United States_vmess_5186
  - 油管绵阿羊_United States_vmess_5187
  - 油管绵阿羊_United States_vmess_5188
  - 油管绵阿羊_None_vmess_5189
  - 油管绵阿羊_United States_vmess_5190
  - 油管绵阿羊_Hong Kong_vmess_5191
  - 油管绵阿羊_United States_vmess_5192
  - 油管绵阿羊_None_vmess_5193
  - 油管绵阿羊_Japan_vmess_5194
  - 油管绵阿羊_None_vmess_5195
  - 油管绵阿羊_United States_vmess_5196
  - 油管绵阿羊_Costa Rica_vmess_5197
  - 油管绵阿羊_Costa Rica_vmess_5198
  - 油管绵阿羊_Spain_vmess_5199
  - 油管绵阿羊_Ecuador_vmess_5200
  - 油管绵阿羊_Netherlands_vmess_5201
  - 油管绵阿羊_Australia_vmess_5202
  - 油管绵阿羊_None_vmess_5203
  - 油管绵阿羊_Netherlands_vmess_5204
  - 油管绵阿羊_United States_vmess_5205
  - 油管绵阿羊_South Africa_vmess_5206
  - 油管绵阿羊_Spain_vmess_5207
  - 油管绵阿羊_None_vmess_5208
  - 油管绵阿羊_Italy_vmess_5209
  - 油管绵阿羊_Brazil_vmess_5210
  - 油管绵阿羊_United States_vmess_5211
  - 油管绵阿羊_United States_vmess_5212
  - 油管绵阿羊_Costa Rica_vmess_5213
  - 油管绵阿羊_South Africa_vmess_5214
  - 油管绵阿羊_United States_vmess_5215
  - 油管绵阿羊_None_vmess_5216
  - 油管绵阿羊_Costa Rica_vmess_5217
  - 油管绵阿羊_United States_vmess_5218
  - 油管绵阿羊_South Africa_vmess_5219
  - 油管绵阿羊_None_vmess_5220
  - 油管绵阿羊_United States_vmess_5221
  - 油管绵阿羊_Spain_vmess_5222
  - 油管绵阿羊_Japan_vmess_5223
  - 油管绵阿羊_South Africa_vmess_5224
  - 油管绵阿羊_South Africa_vmess_5225
  - 油管绵阿羊_Japan_vmess_5226
  - 油管绵阿羊_United States_vmess_5227
  - 油管绵阿羊_Japan_vmess_5228
  - 油管绵阿羊_United States_vmess_5229
  - 油管绵阿羊_South Africa_vmess_5230
  - 油管绵阿羊_United States_vmess_5231
  - 油管绵阿羊_None_vmess_5232
  - 油管绵阿羊_Italy_vmess_5233
  - 油管绵阿羊_United States_vmess_5234
  - 油管绵阿羊_United States_vmess_5235
  - 油管绵阿羊_United States_vmess_5236
  - 油管绵阿羊_None_vmess_5237
  - 油管绵阿羊_Costa Rica_vmess_5238
  - 油管绵阿羊_United States_vmess_5239
  - 油管绵阿羊_Costa Rica_vmess_5240
  - 油管绵阿羊_Costa Rica_vmess_5241
  - 油管绵阿羊_Japan_vmess_5242
  - 油管绵阿羊_United States_vmess_5243
  - 油管绵阿羊_None_vmess_5244
  - 油管绵阿羊_United States_vmess_5245
  - 油管绵阿羊_Spain_vmess_5246
  - 油管绵阿羊_United States_vmess_5247
  - 油管绵阿羊_Costa Rica_vmess_5248
  - 油管绵阿羊_Australia_vmess_5249
  - 油管绵阿羊_None_vmess_5250
  - 油管绵阿羊_United States_vmess_5251
  - 油管绵阿羊_Australia_vmess_5252
  - 油管绵阿羊_United States_vmess_5253
  - 油管绵阿羊_United States_vmess_5254
  - 油管绵阿羊_United States_vmess_5255
  - 油管绵阿羊_United States_vmess_5256
  - 油管绵阿羊_France_vmess_5257
  - 油管绵阿羊_United States_vmess_5258
  - 油管绵阿羊_United States_vmess_5259
  - 油管绵阿羊_United States_vmess_5260
  - 油管绵阿羊_United States_vmess_5261
  - 油管绵阿羊_United States_vmess_5262
  - 油管绵阿羊_United States_vmess_5263
  - 油管绵阿羊_United States_vmess_5264
  - 油管绵阿羊_Costa Rica_vmess_5265
  - 油管绵阿羊_Hong Kong_vmess_5266
  - 油管绵阿羊_Costa Rica_vmess_5267
  - 油管绵阿羊_None_vmess_5268
  - 油管绵阿羊_United States_vmess_5269
  - 油管绵阿羊_None_vmess_5270
  - 油管绵阿羊_United States_vmess_5271
  - 油管绵阿羊_Australia_vmess_5272
  - 油管绵阿羊_United States_vmess_5273
  - 油管绵阿羊_Brazil_vmess_5274
  - 油管绵阿羊_Japan_vmess_5275
  - 油管绵阿羊_United States_vmess_5276
  - 油管绵阿羊_Austria_vmess_5277
  - 油管绵阿羊_Costa Rica_vmess_5278
  - 油管绵阿羊_None_vmess_5279
  - 油管绵阿羊_None_vmess_5280
  - 油管绵阿羊_United States_vmess_5281
  - 油管绵阿羊_Costa Rica_vmess_5282
  - 油管绵阿羊_United States_vmess_5283
  - 油管绵阿羊_United States_vmess_5284
  - 油管绵阿羊_South Africa_vmess_5285
  - 油管绵阿羊_United States_vmess_5286
  - 油管绵阿羊_Japan_vmess_5287
  - 油管绵阿羊_United States_vmess_5288
  - 油管绵阿羊_None_vmess_5289
  - 油管绵阿羊_Spain_vmess_5290
  - 油管绵阿羊_Singapore_vmess_5291
  - 油管绵阿羊_United States_vmess_5292
  - 油管绵阿羊_Canada_vmess_5293
  - 油管绵阿羊_None_vmess_5294
  - 油管绵阿羊_None_vmess_5295
  - 油管绵阿羊_None_vmess_5296
  - 油管绵阿羊_United States_vmess_5297
  - 油管绵阿羊_Australia_vmess_5298
  - 油管绵阿羊_United States_vmess_5299
  - 油管绵阿羊_United States_vmess_5300
  - 油管绵阿羊_Costa Rica_vmess_5301
  - 油管绵阿羊_United States_vmess_5302
  - 油管绵阿羊_Costa Rica_vmess_5303
  - 油管绵阿羊_South Africa_vmess_5304
  - 油管绵阿羊_None_vmess_5305
  - 油管绵阿羊_Costa Rica_vmess_5306
  - 油管绵阿羊_Singapore_vmess_5307
  - 油管绵阿羊_None_vmess_5308
  - 油管绵阿羊_United States_vmess_5309
  - 油管绵阿羊_None_vmess_5310
  - 油管绵阿羊_United States_vmess_5311
  - 油管绵阿羊_None_vmess_5312
  - 油管绵阿羊_Italy_vmess_5313
  - 油管绵阿羊_South Africa_vmess_5314
  - 油管绵阿羊_Singapore_vmess_5315
  - 油管绵阿羊_Hong Kong_vmess_5316
  - 油管绵阿羊_None_vmess_5317
  - 油管绵阿羊_None_vmess_5318
  - 油管绵阿羊_None_vmess_5319
  - 油管绵阿羊_None_vmess_5320
  - 油管绵阿羊_United States_vmess_5321
  - 油管绵阿羊_United States_vmess_5322
  - 油管绵阿羊_Costa Rica_vmess_5323
  - 油管绵阿羊_United States_vmess_5324
  - 油管绵阿羊_Costa Rica_vmess_5325
  - 油管绵阿羊_None_vmess_5326
  - 油管绵阿羊_Japan_vmess_5327
  - 油管绵阿羊_None_vmess_5328
  - 油管绵阿羊_Spain_vmess_5329
  - 油管绵阿羊_None_vmess_5330
  - 油管绵阿羊_United States_vmess_5331
  - 油管绵阿羊_United States_vmess_5332
  - 油管绵阿羊_India_vmess_5333
  - 油管绵阿羊_United Kingdom_vmess_5334
  - 油管绵阿羊_Australia_vmess_5335
  - 油管绵阿羊_United States_vmess_5336
  - 油管绵阿羊_Hong Kong_vmess_5337
  - 油管绵阿羊_Costa Rica_vmess_5338
  - 油管绵阿羊_United States_vmess_5339
  - 油管绵阿羊_None_vmess_5340
  - 油管绵阿羊_United States_vmess_5341
  - 油管绵阿羊_United States_vmess_5342
  - 油管绵阿羊_Costa Rica_vmess_5343
  - 油管绵阿羊_Costa Rica_vmess_5344
  - 油管绵阿羊_None_vmess_5345
  - 油管绵阿羊_None_vmess_5346
  - 油管绵阿羊_None_vmess_5347
  - 油管绵阿羊_United States_vmess_5348
  - 油管绵阿羊_United States_vmess_5349
  - 油管绵阿羊_None_vmess_5350
  - 油管绵阿羊_United States_vmess_5351
  - 油管绵阿羊_United States_vmess_5352
  - 油管绵阿羊_Australia_vmess_5353
  - 油管绵阿羊_United States_vmess_5354
  - 油管绵阿羊_None_vmess_5355
  - 油管绵阿羊_United States_vmess_5356
  - 油管绵阿羊_South Africa_vmess_5357
  - 油管绵阿羊_None_vmess_5358
  - 油管绵阿羊_United States_vmess_5359
  - 油管绵阿羊_Czechia_vmess_5360
  - 油管绵阿羊_United States_vmess_5361
  - 油管绵阿羊_None_vmess_5362
  - 油管绵阿羊_None_vmess_5363
  - 油管绵阿羊_United States_vmess_5364
  - 油管绵阿羊_South Africa_vmess_5365
  - 油管绵阿羊_None_vmess_5366
  - 油管绵阿羊_None_vmess_5367
  - 油管绵阿羊_Costa Rica_vmess_5368
  - 油管绵阿羊_None_vmess_5369
  - 油管绵阿羊_Netherlands_vmess_5370
  - 油管绵阿羊_Australia_vmess_5371
  - 油管绵阿羊_South Africa_vmess_5372
  - 油管绵阿羊_Costa Rica_vmess_5373
  - 油管绵阿羊_United States_vmess_5374
  - 油管绵阿羊_Costa Rica_vmess_5375
  - 油管绵阿羊_United States_vmess_5376
  - 油管绵阿羊_Italy_vmess_5377
  - 油管绵阿羊_United Kingdom_vmess_5378
  - 油管绵阿羊_United States_vmess_5379
  - 油管绵阿羊_United States_vmess_5380
  - 油管绵阿羊_Costa Rica_vmess_5381
  - 油管绵阿羊_None_vmess_5382
  - 油管绵阿羊_South Africa_vmess_5383
  - 油管绵阿羊_United States_vmess_5384
  - 油管绵阿羊_None_vmess_5385
  - 油管绵阿羊_None_vmess_5386
  - 油管绵阿羊_United States_vmess_5387
  - 油管绵阿羊_Costa Rica_vmess_5388
  - 油管绵阿羊_United States_vmess_5389
  - 油管绵阿羊_Spain_vmess_5390
  - 油管绵阿羊_Costa Rica_vmess_5391
  - 油管绵阿羊_United States_vmess_5392
  - 油管绵阿羊_Japan_vmess_5393
  - 油管绵阿羊_United States_vmess_5394
  - 油管绵阿羊_Hong Kong_vmess_5395
  - 油管绵阿羊_United States_vmess_5396
  - 油管绵阿羊_United States_vmess_5397
  - 油管绵阿羊_United States_vmess_5398
  - 油管绵阿羊_United States_vmess_5399
  - 油管绵阿羊_Australia_vmess_5400
  - 油管绵阿羊_South Africa_vmess_5401
  - 油管绵阿羊_United States_vmess_5402
  - 油管绵阿羊_Costa Rica_vmess_5403
  - 油管绵阿羊_United States_vmess_5404
  - 油管绵阿羊_Australia_vmess_5405
  - 油管绵阿羊_United States_vmess_5406
  - 油管绵阿羊_United States_vmess_5407
  - 油管绵阿羊_Singapore_vmess_5408
  - 油管绵阿羊_United States_vmess_5409
  - 油管绵阿羊_None_vmess_5410
  - 油管绵阿羊_None_vmess_5411
  - 油管绵阿羊_Spain_vmess_5412
  - 油管绵阿羊_Hong Kong_vmess_5413
  - 油管绵阿羊_None_vmess_5414
  - 油管绵阿羊_United States_vmess_5415
  - 油管绵阿羊_United States_vmess_5416
  - 油管绵阿羊_United States_vmess_5417
  - 油管绵阿羊_United States_vmess_5418
  - 油管绵阿羊_Costa Rica_vmess_5419
  - 油管绵阿羊_Costa Rica_vmess_5420
  - 油管绵阿羊_United States_vmess_5421
  - 油管绵阿羊_Costa Rica_vmess_5422
  - 油管绵阿羊_Japan_vmess_5423
  - 油管绵阿羊_South Africa_vmess_5424
  - 油管绵阿羊_United States_vmess_5425
  - 油管绵阿羊_United States_vmess_5426
  - 油管绵阿羊_South Korea_vmess_5427
  - 油管绵阿羊_United States_vmess_5428
  - 油管绵阿羊_United States_vmess_5429
  - 油管绵阿羊_None_vmess_5430
  - 油管绵阿羊_None_vmess_5431
  - 油管绵阿羊_United States_vmess_5432
  - 油管绵阿羊_United States_vmess_5433
  - 油管绵阿羊_United States_vmess_5434
  - 油管绵阿羊_Japan_vmess_5435
  - 油管绵阿羊_Costa Rica_vmess_5436
  - 油管绵阿羊_United States_vmess_5437
  - 油管绵阿羊_United States_vmess_5438
  - 油管绵阿羊_United States_vmess_5439
  - 油管绵阿羊_United States_vmess_5440
  - 油管绵阿羊_None_vmess_5441
  - 油管绵阿羊_Netherlands_vmess_5442
  - 油管绵阿羊_United States_vmess_5443
  - 油管绵阿羊_None_vmess_5444
  - 油管绵阿羊_South Africa_vmess_5445
  - 油管绵阿羊_Costa Rica_vmess_5446
  - 油管绵阿羊_United States_vmess_5447
  - 油管绵阿羊_United States_vmess_5448
  - 油管绵阿羊_United States_vmess_5449
  - 油管绵阿羊_Kenya_vmess_5450
  - 油管绵阿羊_United States_vmess_5451
  - 油管绵阿羊_United States_vmess_5452
  - 油管绵阿羊_None_vmess_5453
  - 油管绵阿羊_Spain_vmess_5454
  - 油管绵阿羊_Costa Rica_vmess_5455
  - 油管绵阿羊_United States_vmess_5456
  - 油管绵阿羊_Germany_vmess_5457
  - 油管绵阿羊_United States_vmess_5458
  - 油管绵阿羊_None_vmess_5459
  - 油管绵阿羊_Costa Rica_vmess_5460
  - 油管绵阿羊_None_vmess_5461
  - 油管绵阿羊_Paraguay_vmess_5462
  - 油管绵阿羊_Australia_vmess_5463
  - 油管绵阿羊_United States_vmess_5464
  - 油管绵阿羊_South Africa_vmess_5465
  - 油管绵阿羊_None_vmess_5466
  - 油管绵阿羊_United States_vmess_5467
  - 油管绵阿羊_United States_vmess_5468
  - 油管绵阿羊_Spain_vmess_5469
  - 油管绵阿羊_United States_vmess_5470
  - 油管绵阿羊_United States_vmess_5471
  - 油管绵阿羊_None_vmess_5472
  - 油管绵阿羊_None_vmess_5473
  - 油管绵阿羊_None_vmess_5474
  - 油管绵阿羊_Germany_vmess_5475
  - 油管绵阿羊_India_vmess_5476
  - 油管绵阿羊_Costa Rica_vmess_5477
  - 油管绵阿羊_None_vmess_5478
  - 油管绵阿羊_Germany_vmess_5479
  - 油管绵阿羊_Netherlands_vmess_5480
  - 油管绵阿羊_United States_vmess_5481
  - 油管绵阿羊_United States_vmess_5482
  - 油管绵阿羊_Italy_vmess_5483
  - 油管绵阿羊_Australia_vmess_5484
  - 油管绵阿羊_United States_vmess_5485
  - 油管绵阿羊_None_vmess_5486
  - 油管绵阿羊_None_vmess_5487
  - 油管绵阿羊_United States_vmess_5488
  - 油管绵阿羊_United States_vmess_5489
  - 油管绵阿羊_Costa Rica_vmess_5490
  - 油管绵阿羊_None_vmess_5491
  - 油管绵阿羊_None_vmess_5492
  - 油管绵阿羊_Costa Rica_vmess_5493
  - 油管绵阿羊_United States_vmess_5494
  - 油管绵阿羊_United States_vmess_5495
  - 油管绵阿羊_United States_vmess_5496
  - 油管绵阿羊_Netherlands_vmess_5497
  - 油管绵阿羊_Japan_vmess_5498
  - 油管绵阿羊_Costa Rica_vmess_5499
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
  - 油管绵阿羊_None_vmess_51
  - 油管绵阿羊_United States_vmess_52
  - 油管绵阿羊_United States_vmess_53
  - 油管绵阿羊_Japan_vmess_54
  - 油管绵阿羊_Australia_vmess_55
  - 油管绵阿羊_United States_vmess_56
  - 油管绵阿羊_None_vmess_57
  - 油管绵阿羊_Brazil_vmess_58
  - 油管绵阿羊_United States_vmess_59
  - 油管绵阿羊_United States_vmess_510
  - 油管绵阿羊_None_vmess_511
  - 油管绵阿羊_United States_vmess_512
  - 油管绵阿羊_South Africa_vmess_513
  - 油管绵阿羊_Japan_vmess_514
  - 油管绵阿羊_United States_vmess_515
  - 油管绵阿羊_Italy_vmess_516
  - 油管绵阿羊_United States_vmess_517
  - 油管绵阿羊_United States_vmess_518
  - 油管绵阿羊_Singapore_vmess_519
  - 油管绵阿羊_None_vmess_520
  - 油管绵阿羊_Singapore_vmess_521
  - 油管绵阿羊_None_vmess_522
  - 油管绵阿羊_Costa Rica_vmess_523
  - 油管绵阿羊_Costa Rica_vmess_524
  - 油管绵阿羊_Japan_vmess_525
  - 油管绵阿羊_None_vmess_526
  - 油管绵阿羊_None_vmess_527
  - 油管绵阿羊_United States_vmess_528
  - 油管绵阿羊_United States_vmess_529
  - 油管绵阿羊_United States_vmess_530
  - 油管绵阿羊_None_vmess_531
  - 油管绵阿羊_South Africa_vmess_532
  - 油管绵阿羊_Costa Rica_vmess_533
  - 油管绵阿羊_Netherlands_vmess_534
  - 油管绵阿羊_Costa Rica_vmess_535
  - 油管绵阿羊_Costa Rica_vmess_536
  - 油管绵阿羊_United States_vmess_537
  - 油管绵阿羊_Spain_vmess_538
  - 油管绵阿羊_United States_vmess_539
  - 油管绵阿羊_United States_vmess_540
  - 油管绵阿羊_Costa Rica_vmess_541
  - 油管绵阿羊_Costa Rica_vmess_542
  - 油管绵阿羊_Netherlands_vmess_543
  - 油管绵阿羊_South Africa_vmess_544
  - 油管绵阿羊_Spain_vmess_545
  - 油管绵阿羊_None_vmess_546
  - 油管绵阿羊_None_vmess_547
  - 油管绵阿羊_None_vmess_548
  - 油管绵阿羊_United States_vmess_549
  - 油管绵阿羊_None_vmess_550
  - 油管绵阿羊_South Africa_vmess_551
  - 油管绵阿羊_None_vmess_552
  - 油管绵阿羊_United States_vmess_553
  - 油管绵阿羊_South Africa_vmess_554
  - 油管绵阿羊_Costa Rica_vmess_555
  - 油管绵阿羊_Costa Rica_vmess_556
  - 油管绵阿羊_Singapore_vmess_557
  - 油管绵阿羊_None_vmess_558
  - 油管绵阿羊_Italy_vmess_559
  - 油管绵阿羊_Rwanda_vmess_560
  - 油管绵阿羊_United States_vmess_561
  - 油管绵阿羊_United States_vmess_562
  - 油管绵阿羊_United States_vmess_563
  - 油管绵阿羊_United States_vmess_564
  - 油管绵阿羊_United States_vmess_565
  - 油管绵阿羊_United Arab Emirates_vmess_566
  - 油管绵阿羊_United States_vmess_567
  - 油管绵阿羊_None_vmess_568
  - 油管绵阿羊_Germany_vmess_569
  - 油管绵阿羊_United States_vmess_570
  - 油管绵阿羊_Spain_vmess_571
  - 油管绵阿羊_Costa Rica_vmess_572
  - 油管绵阿羊_None_vmess_573
  - 油管绵阿羊_Costa Rica_vmess_574
  - 油管绵阿羊_South Africa_vmess_575
  - 油管绵阿羊_None_vmess_576
  - 油管绵阿羊_None_vmess_577
  - 油管绵阿羊_Costa Rica_vmess_578
  - 油管绵阿羊_Japan_vmess_579
  - 油管绵阿羊_United States_vmess_580
  - 油管绵阿羊_Netherlands_vmess_581
  - 油管绵阿羊_United States_vmess_582
  - 油管绵阿羊_Singapore_vmess_583
  - 油管绵阿羊_None_vmess_584
  - 油管绵阿羊_South Africa_vmess_585
  - 油管绵阿羊_United States_vmess_586
  - 油管绵阿羊_Canada_vmess_587
  - 油管绵阿羊_None_vmess_588
  - 油管绵阿羊_Costa Rica_vmess_589
  - 油管绵阿羊_United States_vmess_590
  - 油管绵阿羊_South Africa_vmess_591
  - 油管绵阿羊_United States_vmess_592
  - 油管绵阿羊_United States_vmess_593
  - 油管绵阿羊_Costa Rica_vmess_594
  - 油管绵阿羊_United States_vmess_595
  - 油管绵阿羊_South Africa_vmess_596
  - 油管绵阿羊_United States_vmess_597
  - 油管绵阿羊_United States_vmess_598
  - 油管绵阿羊_Japan_vmess_599
  - 油管绵阿羊_United States_vmess_5100
  - 油管绵阿羊_Italy_vmess_5101
  - 油管绵阿羊_None_vmess_5102
  - 油管绵阿羊_Australia_vmess_5103
  - 油管绵阿羊_United States_vmess_5104
  - 油管绵阿羊_Spain_vmess_5105
  - 油管绵阿羊_India_vmess_5106
  - 油管绵阿羊_South Africa_vmess_5107
  - 油管绵阿羊_United States_vmess_5108
  - 油管绵阿羊_United States_vmess_5109
  - 油管绵阿羊_Netherlands_vmess_5110
  - 油管绵阿羊_United States_vmess_5111
  - 油管绵阿羊_United States_vmess_5112
  - 油管绵阿羊_United States_vmess_5113
  - 油管绵阿羊_None_vmess_5114
  - 油管绵阿羊_United States_vmess_5115
  - 油管绵阿羊_United States_vmess_5116
  - 油管绵阿羊_United States_vmess_5117
  - 油管绵阿羊_United States_vmess_5118
  - 油管绵阿羊_Costa Rica_vmess_5119
  - 油管绵阿羊_None_vmess_5120
  - 油管绵阿羊_United States_vmess_5121
  - 油管绵阿羊_None_vmess_5122
  - 油管绵阿羊_South Africa_vmess_5123
  - 油管绵阿羊_None_vmess_5124
  - 油管绵阿羊_South Africa_vmess_5125
  - 油管绵阿羊_United States_vmess_5126
  - 油管绵阿羊_None_vmess_5127
  - 油管绵阿羊_None_vmess_5128
  - 油管绵阿羊_United States_vmess_5129
  - 油管绵阿羊_South Africa_vmess_5130
  - 油管绵阿羊_United States_vmess_5131
  - 油管绵阿羊_Oman_vmess_5132
  - 油管绵阿羊_Netherlands_vmess_5133
  - 油管绵阿羊_None_vmess_5134
  - 油管绵阿羊_None_vmess_5135
  - 油管绵阿羊_Costa Rica_vmess_5136
  - 油管绵阿羊_United States_vmess_5137
  - 油管绵阿羊_None_vmess_5138
  - 油管绵阿羊_France_vmess_5139
  - 油管绵阿羊_United States_vmess_5140
  - 油管绵阿羊_None_vmess_5141
  - 油管绵阿羊_United States_vmess_5142
  - 油管绵阿羊_United States_vmess_5143
  - 油管绵阿羊_United States_vmess_5144
  - 油管绵阿羊_Japan_vmess_5145
  - 油管绵阿羊_South Africa_vmess_5146
  - 油管绵阿羊_Belgium_vmess_5147
  - 油管绵阿羊_None_vmess_5148
  - 油管绵阿羊_Australia_vmess_5149
  - 油管绵阿羊_Australia_vmess_5150
  - 油管绵阿羊_Australia_vmess_5151
  - 油管绵阿羊_Singapore_vmess_5152
  - 油管绵阿羊_United States_vmess_5153
  - 油管绵阿羊_Czechia_vmess_5154
  - 油管绵阿羊_Hong Kong_vmess_5155
  - 油管绵阿羊_United States_vmess_5156
  - 油管绵阿羊_United States_vmess_5157
  - 油管绵阿羊_South Africa_vmess_5158
  - 油管绵阿羊_None_vmess_5159
  - 油管绵阿羊_United States_vmess_5160
  - 油管绵阿羊_United States_vmess_5161
  - 油管绵阿羊_Costa Rica_vmess_5162
  - 油管绵阿羊_United States_vmess_5163
  - 油管绵阿羊_None_vmess_5164
  - 油管绵阿羊_United States_vmess_5165
  - 油管绵阿羊_None_vmess_5166
  - 油管绵阿羊_Costa Rica_vmess_5167
  - 油管绵阿羊_United States_vmess_5168
  - 油管绵阿羊_United States_vmess_5169
  - 油管绵阿羊_None_vmess_5170
  - 油管绵阿羊_United States_vmess_5171
  - 油管绵阿羊_None_vmess_5172
  - 油管绵阿羊_Japan_vmess_5173
  - 油管绵阿羊_None_vmess_5174
  - 油管绵阿羊_Costa Rica_vmess_5175
  - 油管绵阿羊_United States_vmess_5176
  - 油管绵阿羊_None_vmess_5177
  - 油管绵阿羊_None_vmess_5178
  - 油管绵阿羊_United States_vmess_5179
  - 油管绵阿羊_Spain_vmess_5180
  - 油管绵阿羊_Costa Rica_vmess_5181
  - 油管绵阿羊_Hong Kong_vmess_5182
  - 油管绵阿羊_United States_vmess_5183
  - 油管绵阿羊_None_vmess_5184
  - 油管绵阿羊_South Africa_vmess_5185
  - 油管绵阿羊_United States_vmess_5186
  - 油管绵阿羊_United States_vmess_5187
  - 油管绵阿羊_United States_vmess_5188
  - 油管绵阿羊_None_vmess_5189
  - 油管绵阿羊_United States_vmess_5190
  - 油管绵阿羊_Hong Kong_vmess_5191
  - 油管绵阿羊_United States_vmess_5192
  - 油管绵阿羊_None_vmess_5193
  - 油管绵阿羊_Japan_vmess_5194
  - 油管绵阿羊_None_vmess_5195
  - 油管绵阿羊_United States_vmess_5196
  - 油管绵阿羊_Costa Rica_vmess_5197
  - 油管绵阿羊_Costa Rica_vmess_5198
  - 油管绵阿羊_Spain_vmess_5199
  - 油管绵阿羊_Ecuador_vmess_5200
  - 油管绵阿羊_Netherlands_vmess_5201
  - 油管绵阿羊_Australia_vmess_5202
  - 油管绵阿羊_None_vmess_5203
  - 油管绵阿羊_Netherlands_vmess_5204
  - 油管绵阿羊_United States_vmess_5205
  - 油管绵阿羊_South Africa_vmess_5206
  - 油管绵阿羊_Spain_vmess_5207
  - 油管绵阿羊_None_vmess_5208
  - 油管绵阿羊_Italy_vmess_5209
  - 油管绵阿羊_Brazil_vmess_5210
  - 油管绵阿羊_United States_vmess_5211
  - 油管绵阿羊_United States_vmess_5212
  - 油管绵阿羊_Costa Rica_vmess_5213
  - 油管绵阿羊_South Africa_vmess_5214
  - 油管绵阿羊_United States_vmess_5215
  - 油管绵阿羊_None_vmess_5216
  - 油管绵阿羊_Costa Rica_vmess_5217
  - 油管绵阿羊_United States_vmess_5218
  - 油管绵阿羊_South Africa_vmess_5219
  - 油管绵阿羊_None_vmess_5220
  - 油管绵阿羊_United States_vmess_5221
  - 油管绵阿羊_Spain_vmess_5222
  - 油管绵阿羊_Japan_vmess_5223
  - 油管绵阿羊_South Africa_vmess_5224
  - 油管绵阿羊_South Africa_vmess_5225
  - 油管绵阿羊_Japan_vmess_5226
  - 油管绵阿羊_United States_vmess_5227
  - 油管绵阿羊_Japan_vmess_5228
  - 油管绵阿羊_United States_vmess_5229
  - 油管绵阿羊_South Africa_vmess_5230
  - 油管绵阿羊_United States_vmess_5231
  - 油管绵阿羊_None_vmess_5232
  - 油管绵阿羊_Italy_vmess_5233
  - 油管绵阿羊_United States_vmess_5234
  - 油管绵阿羊_United States_vmess_5235
  - 油管绵阿羊_United States_vmess_5236
  - 油管绵阿羊_None_vmess_5237
  - 油管绵阿羊_Costa Rica_vmess_5238
  - 油管绵阿羊_United States_vmess_5239
  - 油管绵阿羊_Costa Rica_vmess_5240
  - 油管绵阿羊_Costa Rica_vmess_5241
  - 油管绵阿羊_Japan_vmess_5242
  - 油管绵阿羊_United States_vmess_5243
  - 油管绵阿羊_None_vmess_5244
  - 油管绵阿羊_United States_vmess_5245
  - 油管绵阿羊_Spain_vmess_5246
  - 油管绵阿羊_United States_vmess_5247
  - 油管绵阿羊_Costa Rica_vmess_5248
  - 油管绵阿羊_Australia_vmess_5249
  - 油管绵阿羊_None_vmess_5250
  - 油管绵阿羊_United States_vmess_5251
  - 油管绵阿羊_Australia_vmess_5252
  - 油管绵阿羊_United States_vmess_5253
  - 油管绵阿羊_United States_vmess_5254
  - 油管绵阿羊_United States_vmess_5255
  - 油管绵阿羊_United States_vmess_5256
  - 油管绵阿羊_France_vmess_5257
  - 油管绵阿羊_United States_vmess_5258
  - 油管绵阿羊_United States_vmess_5259
  - 油管绵阿羊_United States_vmess_5260
  - 油管绵阿羊_United States_vmess_5261
  - 油管绵阿羊_United States_vmess_5262
  - 油管绵阿羊_United States_vmess_5263
  - 油管绵阿羊_United States_vmess_5264
  - 油管绵阿羊_Costa Rica_vmess_5265
  - 油管绵阿羊_Hong Kong_vmess_5266
  - 油管绵阿羊_Costa Rica_vmess_5267
  - 油管绵阿羊_None_vmess_5268
  - 油管绵阿羊_United States_vmess_5269
  - 油管绵阿羊_None_vmess_5270
  - 油管绵阿羊_United States_vmess_5271
  - 油管绵阿羊_Australia_vmess_5272
  - 油管绵阿羊_United States_vmess_5273
  - 油管绵阿羊_Brazil_vmess_5274
  - 油管绵阿羊_Japan_vmess_5275
  - 油管绵阿羊_United States_vmess_5276
  - 油管绵阿羊_Austria_vmess_5277
  - 油管绵阿羊_Costa Rica_vmess_5278
  - 油管绵阿羊_None_vmess_5279
  - 油管绵阿羊_None_vmess_5280
  - 油管绵阿羊_United States_vmess_5281
  - 油管绵阿羊_Costa Rica_vmess_5282
  - 油管绵阿羊_United States_vmess_5283
  - 油管绵阿羊_United States_vmess_5284
  - 油管绵阿羊_South Africa_vmess_5285
  - 油管绵阿羊_United States_vmess_5286
  - 油管绵阿羊_Japan_vmess_5287
  - 油管绵阿羊_United States_vmess_5288
  - 油管绵阿羊_None_vmess_5289
  - 油管绵阿羊_Spain_vmess_5290
  - 油管绵阿羊_Singapore_vmess_5291
  - 油管绵阿羊_United States_vmess_5292
  - 油管绵阿羊_Canada_vmess_5293
  - 油管绵阿羊_None_vmess_5294
  - 油管绵阿羊_None_vmess_5295
  - 油管绵阿羊_None_vmess_5296
  - 油管绵阿羊_United States_vmess_5297
  - 油管绵阿羊_Australia_vmess_5298
  - 油管绵阿羊_United States_vmess_5299
  - 油管绵阿羊_United States_vmess_5300
  - 油管绵阿羊_Costa Rica_vmess_5301
  - 油管绵阿羊_United States_vmess_5302
  - 油管绵阿羊_Costa Rica_vmess_5303
  - 油管绵阿羊_South Africa_vmess_5304
  - 油管绵阿羊_None_vmess_5305
  - 油管绵阿羊_Costa Rica_vmess_5306
  - 油管绵阿羊_Singapore_vmess_5307
  - 油管绵阿羊_None_vmess_5308
  - 油管绵阿羊_United States_vmess_5309
  - 油管绵阿羊_None_vmess_5310
  - 油管绵阿羊_United States_vmess_5311
  - 油管绵阿羊_None_vmess_5312
  - 油管绵阿羊_Italy_vmess_5313
  - 油管绵阿羊_South Africa_vmess_5314
  - 油管绵阿羊_Singapore_vmess_5315
  - 油管绵阿羊_Hong Kong_vmess_5316
  - 油管绵阿羊_None_vmess_5317
  - 油管绵阿羊_None_vmess_5318
  - 油管绵阿羊_None_vmess_5319
  - 油管绵阿羊_None_vmess_5320
  - 油管绵阿羊_United States_vmess_5321
  - 油管绵阿羊_United States_vmess_5322
  - 油管绵阿羊_Costa Rica_vmess_5323
  - 油管绵阿羊_United States_vmess_5324
  - 油管绵阿羊_Costa Rica_vmess_5325
  - 油管绵阿羊_None_vmess_5326
  - 油管绵阿羊_Japan_vmess_5327
  - 油管绵阿羊_None_vmess_5328
  - 油管绵阿羊_Spain_vmess_5329
  - 油管绵阿羊_None_vmess_5330
  - 油管绵阿羊_United States_vmess_5331
  - 油管绵阿羊_United States_vmess_5332
  - 油管绵阿羊_India_vmess_5333
  - 油管绵阿羊_United Kingdom_vmess_5334
  - 油管绵阿羊_Australia_vmess_5335
  - 油管绵阿羊_United States_vmess_5336
  - 油管绵阿羊_Hong Kong_vmess_5337
  - 油管绵阿羊_Costa Rica_vmess_5338
  - 油管绵阿羊_United States_vmess_5339
  - 油管绵阿羊_None_vmess_5340
  - 油管绵阿羊_United States_vmess_5341
  - 油管绵阿羊_United States_vmess_5342
  - 油管绵阿羊_Costa Rica_vmess_5343
  - 油管绵阿羊_Costa Rica_vmess_5344
  - 油管绵阿羊_None_vmess_5345
  - 油管绵阿羊_None_vmess_5346
  - 油管绵阿羊_None_vmess_5347
  - 油管绵阿羊_United States_vmess_5348
  - 油管绵阿羊_United States_vmess_5349
  - 油管绵阿羊_None_vmess_5350
  - 油管绵阿羊_United States_vmess_5351
  - 油管绵阿羊_United States_vmess_5352
  - 油管绵阿羊_Australia_vmess_5353
  - 油管绵阿羊_United States_vmess_5354
  - 油管绵阿羊_None_vmess_5355
  - 油管绵阿羊_United States_vmess_5356
  - 油管绵阿羊_South Africa_vmess_5357
  - 油管绵阿羊_None_vmess_5358
  - 油管绵阿羊_United States_vmess_5359
  - 油管绵阿羊_Czechia_vmess_5360
  - 油管绵阿羊_United States_vmess_5361
  - 油管绵阿羊_None_vmess_5362
  - 油管绵阿羊_None_vmess_5363
  - 油管绵阿羊_United States_vmess_5364
  - 油管绵阿羊_South Africa_vmess_5365
  - 油管绵阿羊_None_vmess_5366
  - 油管绵阿羊_None_vmess_5367
  - 油管绵阿羊_Costa Rica_vmess_5368
  - 油管绵阿羊_None_vmess_5369
  - 油管绵阿羊_Netherlands_vmess_5370
  - 油管绵阿羊_Australia_vmess_5371
  - 油管绵阿羊_South Africa_vmess_5372
  - 油管绵阿羊_Costa Rica_vmess_5373
  - 油管绵阿羊_United States_vmess_5374
  - 油管绵阿羊_Costa Rica_vmess_5375
  - 油管绵阿羊_United States_vmess_5376
  - 油管绵阿羊_Italy_vmess_5377
  - 油管绵阿羊_United Kingdom_vmess_5378
  - 油管绵阿羊_United States_vmess_5379
  - 油管绵阿羊_United States_vmess_5380
  - 油管绵阿羊_Costa Rica_vmess_5381
  - 油管绵阿羊_None_vmess_5382
  - 油管绵阿羊_South Africa_vmess_5383
  - 油管绵阿羊_United States_vmess_5384
  - 油管绵阿羊_None_vmess_5385
  - 油管绵阿羊_None_vmess_5386
  - 油管绵阿羊_United States_vmess_5387
  - 油管绵阿羊_Costa Rica_vmess_5388
  - 油管绵阿羊_United States_vmess_5389
  - 油管绵阿羊_Spain_vmess_5390
  - 油管绵阿羊_Costa Rica_vmess_5391
  - 油管绵阿羊_United States_vmess_5392
  - 油管绵阿羊_Japan_vmess_5393
  - 油管绵阿羊_United States_vmess_5394
  - 油管绵阿羊_Hong Kong_vmess_5395
  - 油管绵阿羊_United States_vmess_5396
  - 油管绵阿羊_United States_vmess_5397
  - 油管绵阿羊_United States_vmess_5398
  - 油管绵阿羊_United States_vmess_5399
  - 油管绵阿羊_Australia_vmess_5400
  - 油管绵阿羊_South Africa_vmess_5401
  - 油管绵阿羊_United States_vmess_5402
  - 油管绵阿羊_Costa Rica_vmess_5403
  - 油管绵阿羊_United States_vmess_5404
  - 油管绵阿羊_Australia_vmess_5405
  - 油管绵阿羊_United States_vmess_5406
  - 油管绵阿羊_United States_vmess_5407
  - 油管绵阿羊_Singapore_vmess_5408
  - 油管绵阿羊_United States_vmess_5409
  - 油管绵阿羊_None_vmess_5410
  - 油管绵阿羊_None_vmess_5411
  - 油管绵阿羊_Spain_vmess_5412
  - 油管绵阿羊_Hong Kong_vmess_5413
  - 油管绵阿羊_None_vmess_5414
  - 油管绵阿羊_United States_vmess_5415
  - 油管绵阿羊_United States_vmess_5416
  - 油管绵阿羊_United States_vmess_5417
  - 油管绵阿羊_United States_vmess_5418
  - 油管绵阿羊_Costa Rica_vmess_5419
  - 油管绵阿羊_Costa Rica_vmess_5420
  - 油管绵阿羊_United States_vmess_5421
  - 油管绵阿羊_Costa Rica_vmess_5422
  - 油管绵阿羊_Japan_vmess_5423
  - 油管绵阿羊_South Africa_vmess_5424
  - 油管绵阿羊_United States_vmess_5425
  - 油管绵阿羊_United States_vmess_5426
  - 油管绵阿羊_South Korea_vmess_5427
  - 油管绵阿羊_United States_vmess_5428
  - 油管绵阿羊_United States_vmess_5429
  - 油管绵阿羊_None_vmess_5430
  - 油管绵阿羊_None_vmess_5431
  - 油管绵阿羊_United States_vmess_5432
  - 油管绵阿羊_United States_vmess_5433
  - 油管绵阿羊_United States_vmess_5434
  - 油管绵阿羊_Japan_vmess_5435
  - 油管绵阿羊_Costa Rica_vmess_5436
  - 油管绵阿羊_United States_vmess_5437
  - 油管绵阿羊_United States_vmess_5438
  - 油管绵阿羊_United States_vmess_5439
  - 油管绵阿羊_United States_vmess_5440
  - 油管绵阿羊_None_vmess_5441
  - 油管绵阿羊_Netherlands_vmess_5442
  - 油管绵阿羊_United States_vmess_5443
  - 油管绵阿羊_None_vmess_5444
  - 油管绵阿羊_South Africa_vmess_5445
  - 油管绵阿羊_Costa Rica_vmess_5446
  - 油管绵阿羊_United States_vmess_5447
  - 油管绵阿羊_United States_vmess_5448
  - 油管绵阿羊_United States_vmess_5449
  - 油管绵阿羊_Kenya_vmess_5450
  - 油管绵阿羊_United States_vmess_5451
  - 油管绵阿羊_United States_vmess_5452
  - 油管绵阿羊_None_vmess_5453
  - 油管绵阿羊_Spain_vmess_5454
  - 油管绵阿羊_Costa Rica_vmess_5455
  - 油管绵阿羊_United States_vmess_5456
  - 油管绵阿羊_Germany_vmess_5457
  - 油管绵阿羊_United States_vmess_5458
  - 油管绵阿羊_None_vmess_5459
  - 油管绵阿羊_Costa Rica_vmess_5460
  - 油管绵阿羊_None_vmess_5461
  - 油管绵阿羊_Paraguay_vmess_5462
  - 油管绵阿羊_Australia_vmess_5463
  - 油管绵阿羊_United States_vmess_5464
  - 油管绵阿羊_South Africa_vmess_5465
  - 油管绵阿羊_None_vmess_5466
  - 油管绵阿羊_United States_vmess_5467
  - 油管绵阿羊_United States_vmess_5468
  - 油管绵阿羊_Spain_vmess_5469
  - 油管绵阿羊_United States_vmess_5470
  - 油管绵阿羊_United States_vmess_5471
  - 油管绵阿羊_None_vmess_5472
  - 油管绵阿羊_None_vmess_5473
  - 油管绵阿羊_None_vmess_5474
  - 油管绵阿羊_Germany_vmess_5475
  - 油管绵阿羊_India_vmess_5476
  - 油管绵阿羊_Costa Rica_vmess_5477
  - 油管绵阿羊_None_vmess_5478
  - 油管绵阿羊_Germany_vmess_5479
  - 油管绵阿羊_Netherlands_vmess_5480
  - 油管绵阿羊_United States_vmess_5481
  - 油管绵阿羊_United States_vmess_5482
  - 油管绵阿羊_Italy_vmess_5483
  - 油管绵阿羊_Australia_vmess_5484
  - 油管绵阿羊_United States_vmess_5485
  - 油管绵阿羊_None_vmess_5486
  - 油管绵阿羊_None_vmess_5487
  - 油管绵阿羊_United States_vmess_5488
  - 油管绵阿羊_United States_vmess_5489
  - 油管绵阿羊_Costa Rica_vmess_5490
  - 油管绵阿羊_None_vmess_5491
  - 油管绵阿羊_None_vmess_5492
  - 油管绵阿羊_Costa Rica_vmess_5493
  - 油管绵阿羊_United States_vmess_5494
  - 油管绵阿羊_United States_vmess_5495
  - 油管绵阿羊_United States_vmess_5496
  - 油管绵阿羊_Netherlands_vmess_5497
  - 油管绵阿羊_Japan_vmess_5498
  - 油管绵阿羊_Costa Rica_vmess_5499
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
  port: 18810
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
- name: 油管绵阿羊_None_vmess_51
  type: vmess
  server: 104.27.100.158
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_52
  type: vmess
  server: 172.71.191.55
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_53
  type: vmess
  server: 173.245.53.36
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_54
  type: vmess
  server: 103.22.201.156
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_55
  type: vmess
  server: 103.21.245.212
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_56
  type: vmess
  server: 103.21.246.99
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_57
  type: vmess
  server: 104.16.247.113
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Brazil_vmess_58
  type: vmess
  server: 172.70.101.28
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_59
  type: vmess
  server: 103.21.247.250
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_510
  type: vmess
  server: 173.245.56.169
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_511
  type: vmess
  server: 104.25.108.118
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_512
  type: vmess
  server: 108.162.235.211
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_513
  type: vmess
  server: 172.68.140.197
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_514
  type: vmess
  server: 103.22.202.12
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_515
  type: vmess
  server: 162.158.174.197
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Italy_vmess_516
  type: vmess
  server: 162.158.130.24
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_517
  type: vmess
  server: 108.162.205.223
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_518
  type: vmess
  server: 103.31.7.84
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Singapore_vmess_519
  type: vmess
  server: 103.22.200.144
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_520
  type: vmess
  server: 104.27.2.100
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Singapore_vmess_521
  type: vmess
  server: 103.22.200.178
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_522
  type: vmess
  server: 104.21.183.7
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_523
  type: vmess
  server: 190.93.251.226
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_524
  type: vmess
  server: 190.93.249.156
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_525
  type: vmess
  server: 103.22.201.147
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_526
  type: vmess
  server: 104.26.254.37
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_527
  type: vmess
  server: 104.19.224.51
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_528
  type: vmess
  server: 103.21.247.54
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_529
  type: vmess
  server: 198.41.132.133
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_530
  type: vmess
  server: 108.162.197.250
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_531
  type: vmess
  server: 162.159.148.101
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_532
  type: vmess
  server: 197.234.241.108
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_533
  type: vmess
  server: 131.0.72.103
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Netherlands_vmess_534
  type: vmess
  server: 188.114.99.214
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_535
  type: vmess
  server: 190.93.240.255
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_536
  type: vmess
  server: 190.93.248.186
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_537
  type: vmess
  server: 108.162.194.168
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_538
  type: vmess
  server: 188.114.111.9
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_539
  type: vmess
  server: 103.21.247.149
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_540
  type: vmess
  server: 172.65.50.58
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_541
  type: vmess
  server: 190.93.252.24
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_542
  type: vmess
  server: 190.93.243.54
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Netherlands_vmess_543
  type: vmess
  server: 188.114.97.10
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_544
  type: vmess
  server: 197.234.241.220
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_545
  type: vmess
  server: 188.114.109.114
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_546
  type: vmess
  server: 198.41.221.172
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_547
  type: vmess
  server: 104.20.34.65
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_548
  type: vmess
  server: 141.101.115.83
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_549
  type: vmess
  server: 103.31.4.142
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_550
  type: vmess
  server: 104.25.238.161
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_551
  type: vmess
  server: 197.234.243.213
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_552
  type: vmess
  server: 104.26.80.152
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_553
  type: vmess
  server: 141.101.103.145
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_554
  type: vmess
  server: 197.234.241.170
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_555
  type: vmess
  server: 131.0.75.123
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_556
  type: vmess
  server: 190.93.240.5
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Singapore_vmess_557
  type: vmess
  server: 103.22.200.14
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_558
  type: vmess
  server: 162.159.185.156
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Italy_vmess_559
  type: vmess
  server: 188.114.101.14
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Rwanda_vmess_560
  type: vmess
  server: 197.234.244.0
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_561
  type: vmess
  server: 173.245.60.72
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_562
  type: vmess
  server: 198.41.168.157
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_563
  type: vmess
  server: 141.101.81.8
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_564
  type: vmess
  server: 198.41.150.222
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_565
  type: vmess
  server: 173.245.63.169
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United Arab Emirates_vmess_566
  type: vmess
  server: 162.158.56.82
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_567
  type: vmess
  server: 103.31.7.104
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_568
  type: vmess
  server: 162.159.47.234
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Germany_vmess_569
  type: vmess
  server: 198.41.240.118
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_570
  type: vmess
  server: 173.245.62.53
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_571
  type: vmess
  server: 188.114.108.244
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_572
  type: vmess
  server: 131.0.72.55
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_573
  type: vmess
  server: 104.18.72.220
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_574
  type: vmess
  server: 131.0.75.75
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_575
  type: vmess
  server: 197.234.242.120
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_576
  type: vmess
  server: 104.17.202.31
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_577
  type: vmess
  server: 104.22.127.181
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_578
  type: vmess
  server: 190.93.246.52
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_579
  type: vmess
  server: 103.22.201.135
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_580
  type: vmess
  server: 103.31.6.42
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Netherlands_vmess_581
  type: vmess
  server: 188.114.96.176
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_582
  type: vmess
  server: 172.67.147.235
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Singapore_vmess_583
  type: vmess
  server: 103.22.200.20
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_584
  type: vmess
  server: 104.26.71.143
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_585
  type: vmess
  server: 197.234.243.175
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_586
  type: vmess
  server: 103.31.4.89
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Canada_vmess_587
  type: vmess
  server: 108.162.241.204
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_588
  type: vmess
  server: 198.41.213.177
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_589
  type: vmess
  server: 131.0.73.214
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_590
  type: vmess
  server: 162.158.62.179
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_591
  type: vmess
  server: 197.234.240.102
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_592
  type: vmess
  server: 103.21.247.104
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_593
  type: vmess
  server: 173.245.50.171
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_594
  type: vmess
  server: 190.93.242.13
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_595
  type: vmess
  server: 108.162.204.246
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_596
  type: vmess
  server: 197.234.241.141
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_597
  type: vmess
  server: 198.41.167.243
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_598
  type: vmess
  server: 198.41.149.172
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_599
  type: vmess
  server: 103.22.201.183
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5100
  type: vmess
  server: 173.245.48.104
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Italy_vmess_5101
  type: vmess
  server: 188.114.102.50
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5102
  type: vmess
  server: 104.16.179.215
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5103
  type: vmess
  server: 108.162.255.194
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5104
  type: vmess
  server: 103.21.246.136
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_5105
  type: vmess
  server: 188.114.110.12
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_India_vmess_5106
  type: vmess
  server: 198.41.245.136
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5107
  type: vmess
  server: 197.234.240.71
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5108
  type: vmess
  server: 141.101.72.166
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5109
  type: vmess
  server: 198.41.138.80
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Netherlands_vmess_5110
  type: vmess
  server: 141.101.64.90
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5111
  type: vmess
  server: 198.41.167.75
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5112
  type: vmess
  server: 172.69.115.24
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5113
  type: vmess
  server: 141.101.101.197
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5114
  type: vmess
  server: 104.23.144.174
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5115
  type: vmess
  server: 188.114.105.231
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5116
  type: vmess
  server: 108.162.208.228
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5117
  type: vmess
  server: 172.67.124.71
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5118
  type: vmess
  server: 103.31.4.12
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5119
  type: vmess
  server: 190.93.250.184
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5120
  type: vmess
  server: 104.26.134.119
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5121
  type: vmess
  server: 108.162.204.20
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5122
  type: vmess
  server: 162.159.127.42
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5123
  type: vmess
  server: 197.234.243.27
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5124
  type: vmess
  server: 104.25.39.131
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5125
  type: vmess
  server: 197.234.243.221
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5126
  type: vmess
  server: 188.114.104.26
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5127
  type: vmess
  server: 104.23.28.91
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5128
  type: vmess
  server: 104.25.127.175
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5129
  type: vmess
  server: 103.31.6.6
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5130
  type: vmess
  server: 197.234.240.17
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5131
  type: vmess
  server: 108.162.231.169
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Oman_vmess_5132
  type: vmess
  server: 162.158.30.253
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Netherlands_vmess_5133
  type: vmess
  server: 172.71.33.232
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5134
  type: vmess
  server: 141.101.117.0
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5135
  type: vmess
  server: 162.159.21.221
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5136
  type: vmess
  server: 131.0.75.157
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5137
  type: vmess
  server: 198.41.237.218
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5138
  type: vmess
  server: 141.101.115.108
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_France_vmess_5139
  type: vmess
  server: 141.101.69.145
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5140
  type: vmess
  server: 108.162.200.150
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5141
  type: vmess
  server: 104.26.124.107
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5142
  type: vmess
  server: 103.21.246.243
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5143
  type: vmess
  server: 173.245.60.253
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5144
  type: vmess
  server: 103.21.247.150
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5145
  type: vmess
  server: 103.22.202.166
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5146
  type: vmess
  server: 197.234.242.87
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Belgium_vmess_5147
  type: vmess
  server: 162.158.234.135
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5148
  type: vmess
  server: 104.26.67.200
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5149
  type: vmess
  server: 108.162.254.119
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5150
  type: vmess
  server: 108.162.247.50
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5151
  type: vmess
  server: 103.21.245.40
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Singapore_vmess_5152
  type: vmess
  server: 103.22.200.195
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5153
  type: vmess
  server: 108.162.230.241
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Czechia_vmess_5154
  type: vmess
  server: 141.101.94.232
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Hong Kong_vmess_5155
  type: vmess
  server: 103.22.203.206
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5156
  type: vmess
  server: 103.31.4.8
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5157
  type: vmess
  server: 103.31.4.183
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5158
  type: vmess
  server: 197.234.243.83
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5159
  type: vmess
  server: 162.159.174.65
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5160
  type: vmess
  server: 172.71.65.156
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5161
  type: vmess
  server: 172.65.47.50
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5162
  type: vmess
  server: 131.0.72.181
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5163
  type: vmess
  server: 103.31.6.183
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5164
  type: vmess
  server: 104.20.168.253
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5165
  type: vmess
  server: 172.71.169.103
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5166
  type: vmess
  server: 104.18.210.222
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5167
  type: vmess
  server: 131.0.72.107
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5168
  type: vmess
  server: 198.41.164.109
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5169
  type: vmess
  server: 103.21.247.211
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5170
  type: vmess
  server: 104.16.26.237
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5171
  type: vmess
  server: 108.162.211.129
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5172
  type: vmess
  server: 104.17.73.225
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5173
  type: vmess
  server: 103.22.201.121
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5174
  type: vmess
  server: 104.27.53.186
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5175
  type: vmess
  server: 162.158.81.180
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5176
  type: vmess
  server: 172.64.43.54
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5177
  type: vmess
  server: 141.101.126.126
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5178
  type: vmess
  server: 104.27.236.105
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5179
  type: vmess
  server: 103.31.5.56
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_5180
  type: vmess
  server: 188.114.111.22
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5181
  type: vmess
  server: 190.93.255.176
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Hong Kong_vmess_5182
  type: vmess
  server: 103.22.203.197
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5183
  type: vmess
  server: 108.162.193.186
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5184
  type: vmess
  server: 162.159.3.105
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5185
  type: vmess
  server: 197.234.243.209
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5186
  type: vmess
  server: 173.245.50.86
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5187
  type: vmess
  server: 173.245.51.74
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5188
  type: vmess
  server: 190.93.245.201
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5189
  type: vmess
  server: 141.101.113.233
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5190
  type: vmess
  server: 173.245.50.43
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Hong Kong_vmess_5191
  type: vmess
  server: 103.22.203.42
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5192
  type: vmess
  server: 103.31.7.68
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5193
  type: vmess
  server: 104.25.187.144
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5194
  type: vmess
  server: 103.22.201.219
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5195
  type: vmess
  server: 141.101.117.240
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5196
  type: vmess
  server: 108.162.216.2
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5197
  type: vmess
  server: 131.0.72.154
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5198
  type: vmess
  server: 190.93.248.59
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_5199
  type: vmess
  server: 188.114.107.39
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Ecuador_vmess_5200
  type: vmess
  server: 162.158.255.144
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Netherlands_vmess_5201
  type: vmess
  server: 188.114.97.79
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5202
  type: vmess
  server: 103.21.245.1
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5203
  type: vmess
  server: 104.25.53.152
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Netherlands_vmess_5204
  type: vmess
  server: 141.101.75.187
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5205
  type: vmess
  server: 188.114.105.9
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5206
  type: vmess
  server: 197.234.240.39
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_5207
  type: vmess
  server: 188.114.109.98
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5208
  type: vmess
  server: 198.41.192.45
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Italy_vmess_5209
  type: vmess
  server: 188.114.100.224
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Brazil_vmess_5210
  type: vmess
  server: 172.69.147.103
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5211
  type: vmess
  server: 198.41.178.32
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5212
  type: vmess
  server: 103.31.4.238
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5213
  type: vmess
  server: 131.0.72.30
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5214
  type: vmess
  server: 197.234.242.22
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5215
  type: vmess
  server: 172.64.50.224
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5216
  type: vmess
  server: 104.27.124.207
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5217
  type: vmess
  server: 190.93.242.26
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5218
  type: vmess
  server: 172.70.22.17
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5219
  type: vmess
  server: 197.234.240.106
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5220
  type: vmess
  server: 104.26.197.150
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5221
  type: vmess
  server: 173.245.51.137
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_5222
  type: vmess
  server: 188.114.110.115
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5223
  type: vmess
  server: 103.22.202.124
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5224
  type: vmess
  server: 197.234.242.202
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5225
  type: vmess
  server: 197.234.242.180
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5226
  type: vmess
  server: 103.22.202.43
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5227
  type: vmess
  server: 172.70.35.202
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5228
  type: vmess
  server: 103.22.201.182
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5229
  type: vmess
  server: 172.70.126.41
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5230
  type: vmess
  server: 197.234.240.113
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5231
  type: vmess
  server: 103.21.246.201
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5232
  type: vmess
  server: 141.101.116.197
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Italy_vmess_5233
  type: vmess
  server: 188.114.100.206
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5234
  type: vmess
  server: 173.245.60.225
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5235
  type: vmess
  server: 198.41.147.162
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5236
  type: vmess
  server: 141.101.103.244
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5237
  type: vmess
  server: 104.21.150.131
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5238
  type: vmess
  server: 131.0.75.189
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5239
  type: vmess
  server: 103.31.4.127
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5240
  type: vmess
  server: 190.93.251.106
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5241
  type: vmess
  server: 190.93.250.239
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5242
  type: vmess
  server: 103.22.201.155
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5243
  type: vmess
  server: 172.67.146.122
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5244
  type: vmess
  server: 104.25.70.12
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5245
  type: vmess
  server: 172.64.161.49
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_5246
  type: vmess
  server: 188.114.106.244
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5247
  type: vmess
  server: 172.64.20.161
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5248
  type: vmess
  server: 190.93.247.25
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5249
  type: vmess
  server: 103.21.245.53
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5250
  type: vmess
  server: 104.26.28.199
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5251
  type: vmess
  server: 198.41.144.73
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5252
  type: vmess
  server: 103.21.245.82
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5253
  type: vmess
  server: 108.162.213.55
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5254
  type: vmess
  server: 172.66.67.222
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5255
  type: vmess
  server: 173.245.51.243
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5256
  type: vmess
  server: 108.162.207.216
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_France_vmess_5257
  type: vmess
  server: 173.245.49.96
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5258
  type: vmess
  server: 141.101.72.37
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5259
  type: vmess
  server: 103.31.4.99
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5260
  type: vmess
  server: 108.162.198.160
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5261
  type: vmess
  server: 108.162.214.193
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5262
  type: vmess
  server: 173.245.56.255
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5263
  type: vmess
  server: 103.21.246.32
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5264
  type: vmess
  server: 188.114.104.209
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5265
  type: vmess
  server: 190.93.252.107
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Hong Kong_vmess_5266
  type: vmess
  server: 103.22.203.67
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5267
  type: vmess
  server: 190.93.248.126
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5268
  type: vmess
  server: 198.41.217.250
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5269
  type: vmess
  server: 103.21.244.162
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5270
  type: vmess
  server: 141.101.123.118
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5271
  type: vmess
  server: 173.245.52.216
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5272
  type: vmess
  server: 103.21.245.135
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5273
  type: vmess
  server: 198.41.151.2
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Brazil_vmess_5274
  type: vmess
  server: 172.71.2.250
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5275
  type: vmess
  server: 103.22.201.195
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5276
  type: vmess
  server: 162.158.187.78
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Austria_vmess_5277
  type: vmess
  server: 108.162.220.59
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5278
  type: vmess
  server: 190.93.249.193
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5279
  type: vmess
  server: 198.41.208.175
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5280
  type: vmess
  server: 104.27.111.75
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5281
  type: vmess
  server: 103.31.7.146
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5282
  type: vmess
  server: 131.0.72.149
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5283
  type: vmess
  server: 173.245.51.23
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5284
  type: vmess
  server: 103.21.246.130
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5285
  type: vmess
  server: 197.234.243.25
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5286
  type: vmess
  server: 173.245.48.139
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5287
  type: vmess
  server: 103.22.202.212
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5288
  type: vmess
  server: 141.101.80.108
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5289
  type: vmess
  server: 104.20.28.184
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_5290
  type: vmess
  server: 188.114.107.12
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Singapore_vmess_5291
  type: vmess
  server: 103.22.200.203
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5292
  type: vmess
  server: 108.162.209.41
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Canada_vmess_5293
  type: vmess
  server: 108.162.240.45
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5294
  type: vmess
  server: 104.18.216.212
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5295
  type: vmess
  server: 162.159.103.149
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5296
  type: vmess
  server: 104.25.148.207
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5297
  type: vmess
  server: 103.31.7.189
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5298
  type: vmess
  server: 108.162.251.114
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5299
  type: vmess
  server: 198.41.128.243
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5300
  type: vmess
  server: 103.31.5.233
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5301
  type: vmess
  server: 131.0.73.54
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5302
  type: vmess
  server: 103.31.4.19
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5303
  type: vmess
  server: 131.0.75.29
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5304
  type: vmess
  server: 197.234.240.142
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5305
  type: vmess
  server: 104.17.17.78
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5306
  type: vmess
  server: 190.93.250.199
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Singapore_vmess_5307
  type: vmess
  server: 162.158.171.93
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5308
  type: vmess
  server: 104.25.106.201
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5309
  type: vmess
  server: 162.158.177.127
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5310
  type: vmess
  server: 141.101.113.229
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5311
  type: vmess
  server: 103.31.5.205
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5312
  type: vmess
  server: 104.21.175.247
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Italy_vmess_5313
  type: vmess
  server: 162.158.131.177
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5314
  type: vmess
  server: 197.234.243.68
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Singapore_vmess_5315
  type: vmess
  server: 103.22.200.71
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Hong Kong_vmess_5316
  type: vmess
  server: 103.22.203.70
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5317
  type: vmess
  server: 104.25.149.63
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5318
  type: vmess
  server: 104.24.112.113
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5319
  type: vmess
  server: 104.25.81.142
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5320
  type: vmess
  server: 104.17.123.43
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5321
  type: vmess
  server: 173.245.48.208
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5322
  type: vmess
  server: 103.31.4.62
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5323
  type: vmess
  server: 131.0.72.121
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5324
  type: vmess
  server: 103.21.247.42
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5325
  type: vmess
  server: 131.0.74.255
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5326
  type: vmess
  server: 141.101.117.164
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5327
  type: vmess
  server: 103.22.201.133
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5328
  type: vmess
  server: 198.41.202.129
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_5329
  type: vmess
  server: 188.114.110.237
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5330
  type: vmess
  server: 162.159.71.101
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5331
  type: vmess
  server: 188.114.105.253
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5332
  type: vmess
  server: 172.67.126.180
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_India_vmess_5333
  type: vmess
  server: 172.69.118.194
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United Kingdom_vmess_5334
  type: vmess
  server: 141.101.70.231
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5335
  type: vmess
  server: 172.68.84.232
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5336
  type: vmess
  server: 103.21.244.255
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Hong Kong_vmess_5337
  type: vmess
  server: 103.22.203.245
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5338
  type: vmess
  server: 131.0.73.192
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5339
  type: vmess
  server: 103.31.4.214
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5340
  type: vmess
  server: 104.16.43.142
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5341
  type: vmess
  server: 141.101.109.248
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5342
  type: vmess
  server: 103.21.246.1
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5343
  type: vmess
  server: 190.93.242.178
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5344
  type: vmess
  server: 131.0.72.53
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5345
  type: vmess
  server: 104.19.217.124
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5346
  type: vmess
  server: 104.25.191.172
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5347
  type: vmess
  server: 198.41.217.201
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5348
  type: vmess
  server: 108.162.194.78
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5349
  type: vmess
  server: 172.64.156.232
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5350
  type: vmess
  server: 104.17.202.186
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5351
  type: vmess
  server: 172.71.189.182
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5352
  type: vmess
  server: 172.65.151.57
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5353
  type: vmess
  server: 103.21.245.208
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5354
  type: vmess
  server: 198.41.157.190
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5355
  type: vmess
  server: 162.159.64.132
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5356
  type: vmess
  server: 172.65.174.157
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5357
  type: vmess
  server: 197.234.241.241
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5358
  type: vmess
  server: 104.26.87.35
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5359
  type: vmess
  server: 173.245.58.249
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Czechia_vmess_5360
  type: vmess
  server: 141.101.96.43
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5361
  type: vmess
  server: 103.31.5.127
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5362
  type: vmess
  server: 104.22.169.204
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5363
  type: vmess
  server: 104.22.145.104
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5364
  type: vmess
  server: 173.245.56.143
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5365
  type: vmess
  server: 197.234.240.162
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5366
  type: vmess
  server: 104.23.61.193
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5367
  type: vmess
  server: 141.101.123.178
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5368
  type: vmess
  server: 190.93.241.223
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5369
  type: vmess
  server: 104.25.149.178
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Netherlands_vmess_5370
  type: vmess
  server: 188.114.99.31
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5371
  type: vmess
  server: 103.21.245.218
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5372
  type: vmess
  server: 197.234.242.7
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5373
  type: vmess
  server: 131.0.74.43
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5374
  type: vmess
  server: 190.93.244.172
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5375
  type: vmess
  server: 190.93.248.108
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5376
  type: vmess
  server: 173.245.53.60
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Italy_vmess_5377
  type: vmess
  server: 188.114.101.98
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United Kingdom_vmess_5378
  type: vmess
  server: 141.101.98.11
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5379
  type: vmess
  server: 103.21.246.7
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5380
  type: vmess
  server: 103.31.6.52
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5381
  type: vmess
  server: 131.0.73.202
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5382
  type: vmess
  server: 104.24.41.195
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5383
  type: vmess
  server: 197.234.240.205
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5384
  type: vmess
  server: 103.21.246.189
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5385
  type: vmess
  server: 141.101.114.179
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5386
  type: vmess
  server: 198.41.203.91
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5387
  type: vmess
  server: 198.41.161.104
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5388
  type: vmess
  server: 131.0.73.247
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5389
  type: vmess
  server: 198.41.165.178
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_5390
  type: vmess
  server: 188.114.106.136
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5391
  type: vmess
  server: 131.0.73.205
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5392
  type: vmess
  server: 108.162.230.132
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5393
  type: vmess
  server: 103.22.202.140
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5394
  type: vmess
  server: 103.21.246.254
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Hong Kong_vmess_5395
  type: vmess
  server: 103.22.203.105
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5396
  type: vmess
  server: 103.31.5.69
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5397
  type: vmess
  server: 198.41.156.253
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5398
  type: vmess
  server: 198.41.158.146
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5399
  type: vmess
  server: 198.41.171.79
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5400
  type: vmess
  server: 103.21.245.235
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5401
  type: vmess
  server: 197.234.242.179
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5402
  type: vmess
  server: 173.245.60.108
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5403
  type: vmess
  server: 131.0.73.244
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5404
  type: vmess
  server: 172.71.195.141
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5405
  type: vmess
  server: 103.21.245.210
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5406
  type: vmess
  server: 198.41.144.37
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5407
  type: vmess
  server: 103.21.247.184
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Singapore_vmess_5408
  type: vmess
  server: 172.70.141.93
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5409
  type: vmess
  server: 103.31.4.124
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5410
  type: vmess
  server: 104.27.3.220
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5411
  type: vmess
  server: 104.17.57.138
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_5412
  type: vmess
  server: 188.114.106.127
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Hong Kong_vmess_5413
  type: vmess
  server: 103.22.203.110
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5414
  type: vmess
  server: 141.101.119.56
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5415
  type: vmess
  server: 198.41.148.103
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5416
  type: vmess
  server: 103.21.247.93
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5417
  type: vmess
  server: 172.66.178.100
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5418
  type: vmess
  server: 188.114.105.48
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5419
  type: vmess
  server: 131.0.74.22
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5420
  type: vmess
  server: 131.0.72.23
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5421
  type: vmess
  server: 172.70.11.190
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5422
  type: vmess
  server: 190.93.252.191
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5423
  type: vmess
  server: 103.22.202.86
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5424
  type: vmess
  server: 197.234.243.94
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5425
  type: vmess
  server: 108.162.192.90
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5426
  type: vmess
  server: 103.31.4.235
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Korea_vmess_5427
  type: vmess
  server: 141.101.83.236
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5428
  type: vmess
  server: 141.101.73.233
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5429
  type: vmess
  server: 108.162.235.207
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5430
  type: vmess
  server: 104.23.46.116
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5431
  type: vmess
  server: 198.41.199.133
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5432
  type: vmess
  server: 173.245.59.231
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5433
  type: vmess
  server: 103.31.4.133
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5434
  type: vmess
  server: 141.101.107.227
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5435
  type: vmess
  server: 103.22.201.96
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5436
  type: vmess
  server: 131.0.72.187
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5437
  type: vmess
  server: 103.31.5.78
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5438
  type: vmess
  server: 108.162.205.155
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5439
  type: vmess
  server: 108.162.245.83
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5440
  type: vmess
  server: 173.245.61.105
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5441
  type: vmess
  server: 104.22.148.29
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Netherlands_vmess_5442
  type: vmess
  server: 141.101.64.153
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5443
  type: vmess
  server: 103.21.247.226
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5444
  type: vmess
  server: 104.24.46.240
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5445
  type: vmess
  server: 197.234.243.15
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5446
  type: vmess
  server: 131.0.72.135
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5447
  type: vmess
  server: 173.245.56.49
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5448
  type: vmess
  server: 103.31.4.162
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5449
  type: vmess
  server: 198.41.247.90
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Kenya_vmess_5450
  type: vmess
  server: 162.158.40.96
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5451
  type: vmess
  server: 173.245.50.11
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5452
  type: vmess
  server: 141.101.89.12
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5453
  type: vmess
  server: 104.19.250.206
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_5454
  type: vmess
  server: 188.114.109.168
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5455
  type: vmess
  server: 131.0.74.69
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5456
  type: vmess
  server: 173.245.51.60
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Germany_vmess_5457
  type: vmess
  server: 198.41.242.150
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5458
  type: vmess
  server: 108.162.244.5
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5459
  type: vmess
  server: 104.23.194.210
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5460
  type: vmess
  server: 190.93.242.203
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5461
  type: vmess
  server: 198.41.198.197
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Paraguay_vmess_5462
  type: vmess
  server: 162.158.147.180
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5463
  type: vmess
  server: 108.162.248.57
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5464
  type: vmess
  server: 103.21.246.158
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_South Africa_vmess_5465
  type: vmess
  server: 197.234.242.187
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5466
  type: vmess
  server: 162.159.144.195
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5467
  type: vmess
  server: 108.162.223.111
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5468
  type: vmess
  server: 103.31.5.225
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Spain_vmess_5469
  type: vmess
  server: 188.114.110.83
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5470
  type: vmess
  server: 108.162.232.20
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5471
  type: vmess
  server: 173.245.63.226
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5472
  type: vmess
  server: 198.41.218.111
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5473
  type: vmess
  server: 104.26.241.105
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5474
  type: vmess
  server: 104.25.132.70
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Germany_vmess_5475
  type: vmess
  server: 162.158.112.108
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_India_vmess_5476
  type: vmess
  server: 172.70.63.62
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5477
  type: vmess
  server: 131.0.73.5
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5478
  type: vmess
  server: 141.101.124.147
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Germany_vmess_5479
  type: vmess
  server: 162.158.87.59
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Netherlands_vmess_5480
  type: vmess
  server: 172.71.46.11
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5481
  type: vmess
  server: 108.162.233.73
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5482
  type: vmess
  server: 173.245.58.183
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Italy_vmess_5483
  type: vmess
  server: 188.114.102.26
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Australia_vmess_5484
  type: vmess
  server: 103.21.245.55
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5485
  type: vmess
  server: 172.65.226.175
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5486
  type: vmess
  server: 141.101.114.104
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5487
  type: vmess
  server: 162.159.244.158
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5488
  type: vmess
  server: 190.93.245.147
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5489
  type: vmess
  server: 198.41.189.192
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5490
  type: vmess
  server: 131.0.72.158
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5491
  type: vmess
  server: 104.21.16.29
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_None_vmess_5492
  type: vmess
  server: 104.22.174.180
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5493
  type: vmess
  server: 131.0.74.204
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5494
  type: vmess
  server: 108.162.246.49
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5495
  type: vmess
  server: 103.31.4.186
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_United States_vmess_5496
  type: vmess
  server: 141.101.79.187
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Netherlands_vmess_5497
  type: vmess
  server: 188.114.98.87
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Japan_vmess_5498
  type: vmess
  server: 103.22.201.107
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
- name: 油管绵阿羊_Costa Rica_vmess_5499
  type: vmess
  server: 131.0.74.245
  port: 8880
  cipher: auto
  uuid: 0dc3ae8c-43d4-4a19-97d3-e78ff2e2fdab
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: ''
  network: ws
  ws-opts:
    path: /OFR9SgW0/
    headers:
      host: cf5.freek1.xyz
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
  - 油管绵阿羊_None_vmess_51
  - 油管绵阿羊_United States_vmess_52
  - 油管绵阿羊_United States_vmess_53
  - 油管绵阿羊_Japan_vmess_54
  - 油管绵阿羊_Australia_vmess_55
  - 油管绵阿羊_United States_vmess_56
  - 油管绵阿羊_None_vmess_57
  - 油管绵阿羊_Brazil_vmess_58
  - 油管绵阿羊_United States_vmess_59
  - 油管绵阿羊_United States_vmess_510
  - 油管绵阿羊_None_vmess_511
  - 油管绵阿羊_United States_vmess_512
  - 油管绵阿羊_South Africa_vmess_513
  - 油管绵阿羊_Japan_vmess_514
  - 油管绵阿羊_United States_vmess_515
  - 油管绵阿羊_Italy_vmess_516
  - 油管绵阿羊_United States_vmess_517
  - 油管绵阿羊_United States_vmess_518
  - 油管绵阿羊_Singapore_vmess_519
  - 油管绵阿羊_None_vmess_520
  - 油管绵阿羊_Singapore_vmess_521
  - 油管绵阿羊_None_vmess_522
  - 油管绵阿羊_Costa Rica_vmess_523
  - 油管绵阿羊_Costa Rica_vmess_524
  - 油管绵阿羊_Japan_vmess_525
  - 油管绵阿羊_None_vmess_526
  - 油管绵阿羊_None_vmess_527
  - 油管绵阿羊_United States_vmess_528
  - 油管绵阿羊_United States_vmess_529
  - 油管绵阿羊_United States_vmess_530
  - 油管绵阿羊_None_vmess_531
  - 油管绵阿羊_South Africa_vmess_532
  - 油管绵阿羊_Costa Rica_vmess_533
  - 油管绵阿羊_Netherlands_vmess_534
  - 油管绵阿羊_Costa Rica_vmess_535
  - 油管绵阿羊_Costa Rica_vmess_536
  - 油管绵阿羊_United States_vmess_537
  - 油管绵阿羊_Spain_vmess_538
  - 油管绵阿羊_United States_vmess_539
  - 油管绵阿羊_United States_vmess_540
  - 油管绵阿羊_Costa Rica_vmess_541
  - 油管绵阿羊_Costa Rica_vmess_542
  - 油管绵阿羊_Netherlands_vmess_543
  - 油管绵阿羊_South Africa_vmess_544
  - 油管绵阿羊_Spain_vmess_545
  - 油管绵阿羊_None_vmess_546
  - 油管绵阿羊_None_vmess_547
  - 油管绵阿羊_None_vmess_548
  - 油管绵阿羊_United States_vmess_549
  - 油管绵阿羊_None_vmess_550
  - 油管绵阿羊_South Africa_vmess_551
  - 油管绵阿羊_None_vmess_552
  - 油管绵阿羊_United States_vmess_553
  - 油管绵阿羊_South Africa_vmess_554
  - 油管绵阿羊_Costa Rica_vmess_555
  - 油管绵阿羊_Costa Rica_vmess_556
  - 油管绵阿羊_Singapore_vmess_557
  - 油管绵阿羊_None_vmess_558
  - 油管绵阿羊_Italy_vmess_559
  - 油管绵阿羊_Rwanda_vmess_560
  - 油管绵阿羊_United States_vmess_561
  - 油管绵阿羊_United States_vmess_562
  - 油管绵阿羊_United States_vmess_563
  - 油管绵阿羊_United States_vmess_564
  - 油管绵阿羊_United States_vmess_565
  - 油管绵阿羊_United Arab Emirates_vmess_566
  - 油管绵阿羊_United States_vmess_567
  - 油管绵阿羊_None_vmess_568
  - 油管绵阿羊_Germany_vmess_569
  - 油管绵阿羊_United States_vmess_570
  - 油管绵阿羊_Spain_vmess_571
  - 油管绵阿羊_Costa Rica_vmess_572
  - 油管绵阿羊_None_vmess_573
  - 油管绵阿羊_Costa Rica_vmess_574
  - 油管绵阿羊_South Africa_vmess_575
  - 油管绵阿羊_None_vmess_576
  - 油管绵阿羊_None_vmess_577
  - 油管绵阿羊_Costa Rica_vmess_578
  - 油管绵阿羊_Japan_vmess_579
  - 油管绵阿羊_United States_vmess_580
  - 油管绵阿羊_Netherlands_vmess_581
  - 油管绵阿羊_United States_vmess_582
  - 油管绵阿羊_Singapore_vmess_583
  - 油管绵阿羊_None_vmess_584
  - 油管绵阿羊_South Africa_vmess_585
  - 油管绵阿羊_United States_vmess_586
  - 油管绵阿羊_Canada_vmess_587
  - 油管绵阿羊_None_vmess_588
  - 油管绵阿羊_Costa Rica_vmess_589
  - 油管绵阿羊_United States_vmess_590
  - 油管绵阿羊_South Africa_vmess_591
  - 油管绵阿羊_United States_vmess_592
  - 油管绵阿羊_United States_vmess_593
  - 油管绵阿羊_Costa Rica_vmess_594
  - 油管绵阿羊_United States_vmess_595
  - 油管绵阿羊_South Africa_vmess_596
  - 油管绵阿羊_United States_vmess_597
  - 油管绵阿羊_United States_vmess_598
  - 油管绵阿羊_Japan_vmess_599
  - 油管绵阿羊_United States_vmess_5100
  - 油管绵阿羊_Italy_vmess_5101
  - 油管绵阿羊_None_vmess_5102
  - 油管绵阿羊_Australia_vmess_5103
  - 油管绵阿羊_United States_vmess_5104
  - 油管绵阿羊_Spain_vmess_5105
  - 油管绵阿羊_India_vmess_5106
  - 油管绵阿羊_South Africa_vmess_5107
  - 油管绵阿羊_United States_vmess_5108
  - 油管绵阿羊_United States_vmess_5109
  - 油管绵阿羊_Netherlands_vmess_5110
  - 油管绵阿羊_United States_vmess_5111
  - 油管绵阿羊_United States_vmess_5112
  - 油管绵阿羊_United States_vmess_5113
  - 油管绵阿羊_None_vmess_5114
  - 油管绵阿羊_United States_vmess_5115
  - 油管绵阿羊_United States_vmess_5116
  - 油管绵阿羊_United States_vmess_5117
  - 油管绵阿羊_United States_vmess_5118
  - 油管绵阿羊_Costa Rica_vmess_5119
  - 油管绵阿羊_None_vmess_5120
  - 油管绵阿羊_United States_vmess_5121
  - 油管绵阿羊_None_vmess_5122
  - 油管绵阿羊_South Africa_vmess_5123
  - 油管绵阿羊_None_vmess_5124
  - 油管绵阿羊_South Africa_vmess_5125
  - 油管绵阿羊_United States_vmess_5126
  - 油管绵阿羊_None_vmess_5127
  - 油管绵阿羊_None_vmess_5128
  - 油管绵阿羊_United States_vmess_5129
  - 油管绵阿羊_South Africa_vmess_5130
  - 油管绵阿羊_United States_vmess_5131
  - 油管绵阿羊_Oman_vmess_5132
  - 油管绵阿羊_Netherlands_vmess_5133
  - 油管绵阿羊_None_vmess_5134
  - 油管绵阿羊_None_vmess_5135
  - 油管绵阿羊_Costa Rica_vmess_5136
  - 油管绵阿羊_United States_vmess_5137
  - 油管绵阿羊_None_vmess_5138
  - 油管绵阿羊_France_vmess_5139
  - 油管绵阿羊_United States_vmess_5140
  - 油管绵阿羊_None_vmess_5141
  - 油管绵阿羊_United States_vmess_5142
  - 油管绵阿羊_United States_vmess_5143
  - 油管绵阿羊_United States_vmess_5144
  - 油管绵阿羊_Japan_vmess_5145
  - 油管绵阿羊_South Africa_vmess_5146
  - 油管绵阿羊_Belgium_vmess_5147
  - 油管绵阿羊_None_vmess_5148
  - 油管绵阿羊_Australia_vmess_5149
  - 油管绵阿羊_Australia_vmess_5150
  - 油管绵阿羊_Australia_vmess_5151
  - 油管绵阿羊_Singapore_vmess_5152
  - 油管绵阿羊_United States_vmess_5153
  - 油管绵阿羊_Czechia_vmess_5154
  - 油管绵阿羊_Hong Kong_vmess_5155
  - 油管绵阿羊_United States_vmess_5156
  - 油管绵阿羊_United States_vmess_5157
  - 油管绵阿羊_South Africa_vmess_5158
  - 油管绵阿羊_None_vmess_5159
  - 油管绵阿羊_United States_vmess_5160
  - 油管绵阿羊_United States_vmess_5161
  - 油管绵阿羊_Costa Rica_vmess_5162
  - 油管绵阿羊_United States_vmess_5163
  - 油管绵阿羊_None_vmess_5164
  - 油管绵阿羊_United States_vmess_5165
  - 油管绵阿羊_None_vmess_5166
  - 油管绵阿羊_Costa Rica_vmess_5167
  - 油管绵阿羊_United States_vmess_5168
  - 油管绵阿羊_United States_vmess_5169
  - 油管绵阿羊_None_vmess_5170
  - 油管绵阿羊_United States_vmess_5171
  - 油管绵阿羊_None_vmess_5172
  - 油管绵阿羊_Japan_vmess_5173
  - 油管绵阿羊_None_vmess_5174
  - 油管绵阿羊_Costa Rica_vmess_5175
  - 油管绵阿羊_United States_vmess_5176
  - 油管绵阿羊_None_vmess_5177
  - 油管绵阿羊_None_vmess_5178
  - 油管绵阿羊_United States_vmess_5179
  - 油管绵阿羊_Spain_vmess_5180
  - 油管绵阿羊_Costa Rica_vmess_5181
  - 油管绵阿羊_Hong Kong_vmess_5182
  - 油管绵阿羊_United States_vmess_5183
  - 油管绵阿羊_None_vmess_5184
  - 油管绵阿羊_South Africa_vmess_5185
  - 油管绵阿羊_United States_vmess_5186
  - 油管绵阿羊_United States_vmess_5187
  - 油管绵阿羊_United States_vmess_5188
  - 油管绵阿羊_None_vmess_5189
  - 油管绵阿羊_United States_vmess_5190
  - 油管绵阿羊_Hong Kong_vmess_5191
  - 油管绵阿羊_United States_vmess_5192
  - 油管绵阿羊_None_vmess_5193
  - 油管绵阿羊_Japan_vmess_5194
  - 油管绵阿羊_None_vmess_5195
  - 油管绵阿羊_United States_vmess_5196
  - 油管绵阿羊_Costa Rica_vmess_5197
  - 油管绵阿羊_Costa Rica_vmess_5198
  - 油管绵阿羊_Spain_vmess_5199
  - 油管绵阿羊_Ecuador_vmess_5200
  - 油管绵阿羊_Netherlands_vmess_5201
  - 油管绵阿羊_Australia_vmess_5202
  - 油管绵阿羊_None_vmess_5203
  - 油管绵阿羊_Netherlands_vmess_5204
  - 油管绵阿羊_United States_vmess_5205
  - 油管绵阿羊_South Africa_vmess_5206
  - 油管绵阿羊_Spain_vmess_5207
  - 油管绵阿羊_None_vmess_5208
  - 油管绵阿羊_Italy_vmess_5209
  - 油管绵阿羊_Brazil_vmess_5210
  - 油管绵阿羊_United States_vmess_5211
  - 油管绵阿羊_United States_vmess_5212
  - 油管绵阿羊_Costa Rica_vmess_5213
  - 油管绵阿羊_South Africa_vmess_5214
  - 油管绵阿羊_United States_vmess_5215
  - 油管绵阿羊_None_vmess_5216
  - 油管绵阿羊_Costa Rica_vmess_5217
  - 油管绵阿羊_United States_vmess_5218
  - 油管绵阿羊_South Africa_vmess_5219
  - 油管绵阿羊_None_vmess_5220
  - 油管绵阿羊_United States_vmess_5221
  - 油管绵阿羊_Spain_vmess_5222
  - 油管绵阿羊_Japan_vmess_5223
  - 油管绵阿羊_South Africa_vmess_5224
  - 油管绵阿羊_South Africa_vmess_5225
  - 油管绵阿羊_Japan_vmess_5226
  - 油管绵阿羊_United States_vmess_5227
  - 油管绵阿羊_Japan_vmess_5228
  - 油管绵阿羊_United States_vmess_5229
  - 油管绵阿羊_South Africa_vmess_5230
  - 油管绵阿羊_United States_vmess_5231
  - 油管绵阿羊_None_vmess_5232
  - 油管绵阿羊_Italy_vmess_5233
  - 油管绵阿羊_United States_vmess_5234
  - 油管绵阿羊_United States_vmess_5235
  - 油管绵阿羊_United States_vmess_5236
  - 油管绵阿羊_None_vmess_5237
  - 油管绵阿羊_Costa Rica_vmess_5238
  - 油管绵阿羊_United States_vmess_5239
  - 油管绵阿羊_Costa Rica_vmess_5240
  - 油管绵阿羊_Costa Rica_vmess_5241
  - 油管绵阿羊_Japan_vmess_5242
  - 油管绵阿羊_United States_vmess_5243
  - 油管绵阿羊_None_vmess_5244
  - 油管绵阿羊_United States_vmess_5245
  - 油管绵阿羊_Spain_vmess_5246
  - 油管绵阿羊_United States_vmess_5247
  - 油管绵阿羊_Costa Rica_vmess_5248
  - 油管绵阿羊_Australia_vmess_5249
  - 油管绵阿羊_None_vmess_5250
  - 油管绵阿羊_United States_vmess_5251
  - 油管绵阿羊_Australia_vmess_5252
  - 油管绵阿羊_United States_vmess_5253
  - 油管绵阿羊_United States_vmess_5254
  - 油管绵阿羊_United States_vmess_5255
  - 油管绵阿羊_United States_vmess_5256
  - 油管绵阿羊_France_vmess_5257
  - 油管绵阿羊_United States_vmess_5258
  - 油管绵阿羊_United States_vmess_5259
  - 油管绵阿羊_United States_vmess_5260
  - 油管绵阿羊_United States_vmess_5261
  - 油管绵阿羊_United States_vmess_5262
  - 油管绵阿羊_United States_vmess_5263
  - 油管绵阿羊_United States_vmess_5264
  - 油管绵阿羊_Costa Rica_vmess_5265
  - 油管绵阿羊_Hong Kong_vmess_5266
  - 油管绵阿羊_Costa Rica_vmess_5267
  - 油管绵阿羊_None_vmess_5268
  - 油管绵阿羊_United States_vmess_5269
  - 油管绵阿羊_None_vmess_5270
  - 油管绵阿羊_United States_vmess_5271
  - 油管绵阿羊_Australia_vmess_5272
  - 油管绵阿羊_United States_vmess_5273
  - 油管绵阿羊_Brazil_vmess_5274
  - 油管绵阿羊_Japan_vmess_5275
  - 油管绵阿羊_United States_vmess_5276
  - 油管绵阿羊_Austria_vmess_5277
  - 油管绵阿羊_Costa Rica_vmess_5278
  - 油管绵阿羊_None_vmess_5279
  - 油管绵阿羊_None_vmess_5280
  - 油管绵阿羊_United States_vmess_5281
  - 油管绵阿羊_Costa Rica_vmess_5282
  - 油管绵阿羊_United States_vmess_5283
  - 油管绵阿羊_United States_vmess_5284
  - 油管绵阿羊_South Africa_vmess_5285
  - 油管绵阿羊_United States_vmess_5286
  - 油管绵阿羊_Japan_vmess_5287
  - 油管绵阿羊_United States_vmess_5288
  - 油管绵阿羊_None_vmess_5289
  - 油管绵阿羊_Spain_vmess_5290
  - 油管绵阿羊_Singapore_vmess_5291
  - 油管绵阿羊_United States_vmess_5292
  - 油管绵阿羊_Canada_vmess_5293
  - 油管绵阿羊_None_vmess_5294
  - 油管绵阿羊_None_vmess_5295
  - 油管绵阿羊_None_vmess_5296
  - 油管绵阿羊_United States_vmess_5297
  - 油管绵阿羊_Australia_vmess_5298
  - 油管绵阿羊_United States_vmess_5299
  - 油管绵阿羊_United States_vmess_5300
  - 油管绵阿羊_Costa Rica_vmess_5301
  - 油管绵阿羊_United States_vmess_5302
  - 油管绵阿羊_Costa Rica_vmess_5303
  - 油管绵阿羊_South Africa_vmess_5304
  - 油管绵阿羊_None_vmess_5305
  - 油管绵阿羊_Costa Rica_vmess_5306
  - 油管绵阿羊_Singapore_vmess_5307
  - 油管绵阿羊_None_vmess_5308
  - 油管绵阿羊_United States_vmess_5309
  - 油管绵阿羊_None_vmess_5310
  - 油管绵阿羊_United States_vmess_5311
  - 油管绵阿羊_None_vmess_5312
  - 油管绵阿羊_Italy_vmess_5313
  - 油管绵阿羊_South Africa_vmess_5314
  - 油管绵阿羊_Singapore_vmess_5315
  - 油管绵阿羊_Hong Kong_vmess_5316
  - 油管绵阿羊_None_vmess_5317
  - 油管绵阿羊_None_vmess_5318
  - 油管绵阿羊_None_vmess_5319
  - 油管绵阿羊_None_vmess_5320
  - 油管绵阿羊_United States_vmess_5321
  - 油管绵阿羊_United States_vmess_5322
  - 油管绵阿羊_Costa Rica_vmess_5323
  - 油管绵阿羊_United States_vmess_5324
  - 油管绵阿羊_Costa Rica_vmess_5325
  - 油管绵阿羊_None_vmess_5326
  - 油管绵阿羊_Japan_vmess_5327
  - 油管绵阿羊_None_vmess_5328
  - 油管绵阿羊_Spain_vmess_5329
  - 油管绵阿羊_None_vmess_5330
  - 油管绵阿羊_United States_vmess_5331
  - 油管绵阿羊_United States_vmess_5332
  - 油管绵阿羊_India_vmess_5333
  - 油管绵阿羊_United Kingdom_vmess_5334
  - 油管绵阿羊_Australia_vmess_5335
  - 油管绵阿羊_United States_vmess_5336
  - 油管绵阿羊_Hong Kong_vmess_5337
  - 油管绵阿羊_Costa Rica_vmess_5338
  - 油管绵阿羊_United States_vmess_5339
  - 油管绵阿羊_None_vmess_5340
  - 油管绵阿羊_United States_vmess_5341
  - 油管绵阿羊_United States_vmess_5342
  - 油管绵阿羊_Costa Rica_vmess_5343
  - 油管绵阿羊_Costa Rica_vmess_5344
  - 油管绵阿羊_None_vmess_5345
  - 油管绵阿羊_None_vmess_5346
  - 油管绵阿羊_None_vmess_5347
  - 油管绵阿羊_United States_vmess_5348
  - 油管绵阿羊_United States_vmess_5349
  - 油管绵阿羊_None_vmess_5350
  - 油管绵阿羊_United States_vmess_5351
  - 油管绵阿羊_United States_vmess_5352
  - 油管绵阿羊_Australia_vmess_5353
  - 油管绵阿羊_United States_vmess_5354
  - 油管绵阿羊_None_vmess_5355
  - 油管绵阿羊_United States_vmess_5356
  - 油管绵阿羊_South Africa_vmess_5357
  - 油管绵阿羊_None_vmess_5358
  - 油管绵阿羊_United States_vmess_5359
  - 油管绵阿羊_Czechia_vmess_5360
  - 油管绵阿羊_United States_vmess_5361
  - 油管绵阿羊_None_vmess_5362
  - 油管绵阿羊_None_vmess_5363
  - 油管绵阿羊_United States_vmess_5364
  - 油管绵阿羊_South Africa_vmess_5365
  - 油管绵阿羊_None_vmess_5366
  - 油管绵阿羊_None_vmess_5367
  - 油管绵阿羊_Costa Rica_vmess_5368
  - 油管绵阿羊_None_vmess_5369
  - 油管绵阿羊_Netherlands_vmess_5370
  - 油管绵阿羊_Australia_vmess_5371
  - 油管绵阿羊_South Africa_vmess_5372
  - 油管绵阿羊_Costa Rica_vmess_5373
  - 油管绵阿羊_United States_vmess_5374
  - 油管绵阿羊_Costa Rica_vmess_5375
  - 油管绵阿羊_United States_vmess_5376
  - 油管绵阿羊_Italy_vmess_5377
  - 油管绵阿羊_United Kingdom_vmess_5378
  - 油管绵阿羊_United States_vmess_5379
  - 油管绵阿羊_United States_vmess_5380
  - 油管绵阿羊_Costa Rica_vmess_5381
  - 油管绵阿羊_None_vmess_5382
  - 油管绵阿羊_South Africa_vmess_5383
  - 油管绵阿羊_United States_vmess_5384
  - 油管绵阿羊_None_vmess_5385
  - 油管绵阿羊_None_vmess_5386
  - 油管绵阿羊_United States_vmess_5387
  - 油管绵阿羊_Costa Rica_vmess_5388
  - 油管绵阿羊_United States_vmess_5389
  - 油管绵阿羊_Spain_vmess_5390
  - 油管绵阿羊_Costa Rica_vmess_5391
  - 油管绵阿羊_United States_vmess_5392
  - 油管绵阿羊_Japan_vmess_5393
  - 油管绵阿羊_United States_vmess_5394
  - 油管绵阿羊_Hong Kong_vmess_5395
  - 油管绵阿羊_United States_vmess_5396
  - 油管绵阿羊_United States_vmess_5397
  - 油管绵阿羊_United States_vmess_5398
  - 油管绵阿羊_United States_vmess_5399
  - 油管绵阿羊_Australia_vmess_5400
  - 油管绵阿羊_South Africa_vmess_5401
  - 油管绵阿羊_United States_vmess_5402
  - 油管绵阿羊_Costa Rica_vmess_5403
  - 油管绵阿羊_United States_vmess_5404
  - 油管绵阿羊_Australia_vmess_5405
  - 油管绵阿羊_United States_vmess_5406
  - 油管绵阿羊_United States_vmess_5407
  - 油管绵阿羊_Singapore_vmess_5408
  - 油管绵阿羊_United States_vmess_5409
  - 油管绵阿羊_None_vmess_5410
  - 油管绵阿羊_None_vmess_5411
  - 油管绵阿羊_Spain_vmess_5412
  - 油管绵阿羊_Hong Kong_vmess_5413
  - 油管绵阿羊_None_vmess_5414
  - 油管绵阿羊_United States_vmess_5415
  - 油管绵阿羊_United States_vmess_5416
  - 油管绵阿羊_United States_vmess_5417
  - 油管绵阿羊_United States_vmess_5418
  - 油管绵阿羊_Costa Rica_vmess_5419
  - 油管绵阿羊_Costa Rica_vmess_5420
  - 油管绵阿羊_United States_vmess_5421
  - 油管绵阿羊_Costa Rica_vmess_5422
  - 油管绵阿羊_Japan_vmess_5423
  - 油管绵阿羊_South Africa_vmess_5424
  - 油管绵阿羊_United States_vmess_5425
  - 油管绵阿羊_United States_vmess_5426
  - 油管绵阿羊_South Korea_vmess_5427
  - 油管绵阿羊_United States_vmess_5428
  - 油管绵阿羊_United States_vmess_5429
  - 油管绵阿羊_None_vmess_5430
  - 油管绵阿羊_None_vmess_5431
  - 油管绵阿羊_United States_vmess_5432
  - 油管绵阿羊_United States_vmess_5433
  - 油管绵阿羊_United States_vmess_5434
  - 油管绵阿羊_Japan_vmess_5435
  - 油管绵阿羊_Costa Rica_vmess_5436
  - 油管绵阿羊_United States_vmess_5437
  - 油管绵阿羊_United States_vmess_5438
  - 油管绵阿羊_United States_vmess_5439
  - 油管绵阿羊_United States_vmess_5440
  - 油管绵阿羊_None_vmess_5441
  - 油管绵阿羊_Netherlands_vmess_5442
  - 油管绵阿羊_United States_vmess_5443
  - 油管绵阿羊_None_vmess_5444
  - 油管绵阿羊_South Africa_vmess_5445
  - 油管绵阿羊_Costa Rica_vmess_5446
  - 油管绵阿羊_United States_vmess_5447
  - 油管绵阿羊_United States_vmess_5448
  - 油管绵阿羊_United States_vmess_5449
  - 油管绵阿羊_Kenya_vmess_5450
  - 油管绵阿羊_United States_vmess_5451
  - 油管绵阿羊_United States_vmess_5452
  - 油管绵阿羊_None_vmess_5453
  - 油管绵阿羊_Spain_vmess_5454
  - 油管绵阿羊_Costa Rica_vmess_5455
  - 油管绵阿羊_United States_vmess_5456
  - 油管绵阿羊_Germany_vmess_5457
  - 油管绵阿羊_United States_vmess_5458
  - 油管绵阿羊_None_vmess_5459
  - 油管绵阿羊_Costa Rica_vmess_5460
  - 油管绵阿羊_None_vmess_5461
  - 油管绵阿羊_Paraguay_vmess_5462
  - 油管绵阿羊_Australia_vmess_5463
  - 油管绵阿羊_United States_vmess_5464
  - 油管绵阿羊_South Africa_vmess_5465
  - 油管绵阿羊_None_vmess_5466
  - 油管绵阿羊_United States_vmess_5467
  - 油管绵阿羊_United States_vmess_5468
  - 油管绵阿羊_Spain_vmess_5469
  - 油管绵阿羊_United States_vmess_5470
  - 油管绵阿羊_United States_vmess_5471
  - 油管绵阿羊_None_vmess_5472
  - 油管绵阿羊_None_vmess_5473
  - 油管绵阿羊_None_vmess_5474
  - 油管绵阿羊_Germany_vmess_5475
  - 油管绵阿羊_India_vmess_5476
  - 油管绵阿羊_Costa Rica_vmess_5477
  - 油管绵阿羊_None_vmess_5478
  - 油管绵阿羊_Germany_vmess_5479
  - 油管绵阿羊_Netherlands_vmess_5480
  - 油管绵阿羊_United States_vmess_5481
  - 油管绵阿羊_United States_vmess_5482
  - 油管绵阿羊_Italy_vmess_5483
  - 油管绵阿羊_Australia_vmess_5484
  - 油管绵阿羊_United States_vmess_5485
  - 油管绵阿羊_None_vmess_5486
  - 油管绵阿羊_None_vmess_5487
  - 油管绵阿羊_United States_vmess_5488
  - 油管绵阿羊_United States_vmess_5489
  - 油管绵阿羊_Costa Rica_vmess_5490
  - 油管绵阿羊_None_vmess_5491
  - 油管绵阿羊_None_vmess_5492
  - 油管绵阿羊_Costa Rica_vmess_5493
  - 油管绵阿羊_United States_vmess_5494
  - 油管绵阿羊_United States_vmess_5495
  - 油管绵阿羊_United States_vmess_5496
  - 油管绵阿羊_Netherlands_vmess_5497
  - 油管绵阿羊_Japan_vmess_5498
  - 油管绵阿羊_Costa Rica_vmess_5499
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
  - 油管绵阿羊_None_vmess_51
  - 油管绵阿羊_United States_vmess_52
  - 油管绵阿羊_United States_vmess_53
  - 油管绵阿羊_Japan_vmess_54
  - 油管绵阿羊_Australia_vmess_55
  - 油管绵阿羊_United States_vmess_56
  - 油管绵阿羊_None_vmess_57
  - 油管绵阿羊_Brazil_vmess_58
  - 油管绵阿羊_United States_vmess_59
  - 油管绵阿羊_United States_vmess_510
  - 油管绵阿羊_None_vmess_511
  - 油管绵阿羊_United States_vmess_512
  - 油管绵阿羊_South Africa_vmess_513
  - 油管绵阿羊_Japan_vmess_514
  - 油管绵阿羊_United States_vmess_515
  - 油管绵阿羊_Italy_vmess_516
  - 油管绵阿羊_United States_vmess_517
  - 油管绵阿羊_United States_vmess_518
  - 油管绵阿羊_Singapore_vmess_519
  - 油管绵阿羊_None_vmess_520
  - 油管绵阿羊_Singapore_vmess_521
  - 油管绵阿羊_None_vmess_522
  - 油管绵阿羊_Costa Rica_vmess_523
  - 油管绵阿羊_Costa Rica_vmess_524
  - 油管绵阿羊_Japan_vmess_525
  - 油管绵阿羊_None_vmess_526
  - 油管绵阿羊_None_vmess_527
  - 油管绵阿羊_United States_vmess_528
  - 油管绵阿羊_United States_vmess_529
  - 油管绵阿羊_United States_vmess_530
  - 油管绵阿羊_None_vmess_531
  - 油管绵阿羊_South Africa_vmess_532
  - 油管绵阿羊_Costa Rica_vmess_533
  - 油管绵阿羊_Netherlands_vmess_534
  - 油管绵阿羊_Costa Rica_vmess_535
  - 油管绵阿羊_Costa Rica_vmess_536
  - 油管绵阿羊_United States_vmess_537
  - 油管绵阿羊_Spain_vmess_538
  - 油管绵阿羊_United States_vmess_539
  - 油管绵阿羊_United States_vmess_540
  - 油管绵阿羊_Costa Rica_vmess_541
  - 油管绵阿羊_Costa Rica_vmess_542
  - 油管绵阿羊_Netherlands_vmess_543
  - 油管绵阿羊_South Africa_vmess_544
  - 油管绵阿羊_Spain_vmess_545
  - 油管绵阿羊_None_vmess_546
  - 油管绵阿羊_None_vmess_547
  - 油管绵阿羊_None_vmess_548
  - 油管绵阿羊_United States_vmess_549
  - 油管绵阿羊_None_vmess_550
  - 油管绵阿羊_South Africa_vmess_551
  - 油管绵阿羊_None_vmess_552
  - 油管绵阿羊_United States_vmess_553
  - 油管绵阿羊_South Africa_vmess_554
  - 油管绵阿羊_Costa Rica_vmess_555
  - 油管绵阿羊_Costa Rica_vmess_556
  - 油管绵阿羊_Singapore_vmess_557
  - 油管绵阿羊_None_vmess_558
  - 油管绵阿羊_Italy_vmess_559
  - 油管绵阿羊_Rwanda_vmess_560
  - 油管绵阿羊_United States_vmess_561
  - 油管绵阿羊_United States_vmess_562
  - 油管绵阿羊_United States_vmess_563
  - 油管绵阿羊_United States_vmess_564
  - 油管绵阿羊_United States_vmess_565
  - 油管绵阿羊_United Arab Emirates_vmess_566
  - 油管绵阿羊_United States_vmess_567
  - 油管绵阿羊_None_vmess_568
  - 油管绵阿羊_Germany_vmess_569
  - 油管绵阿羊_United States_vmess_570
  - 油管绵阿羊_Spain_vmess_571
  - 油管绵阿羊_Costa Rica_vmess_572
  - 油管绵阿羊_None_vmess_573
  - 油管绵阿羊_Costa Rica_vmess_574
  - 油管绵阿羊_South Africa_vmess_575
  - 油管绵阿羊_None_vmess_576
  - 油管绵阿羊_None_vmess_577
  - 油管绵阿羊_Costa Rica_vmess_578
  - 油管绵阿羊_Japan_vmess_579
  - 油管绵阿羊_United States_vmess_580
  - 油管绵阿羊_Netherlands_vmess_581
  - 油管绵阿羊_United States_vmess_582
  - 油管绵阿羊_Singapore_vmess_583
  - 油管绵阿羊_None_vmess_584
  - 油管绵阿羊_South Africa_vmess_585
  - 油管绵阿羊_United States_vmess_586
  - 油管绵阿羊_Canada_vmess_587
  - 油管绵阿羊_None_vmess_588
  - 油管绵阿羊_Costa Rica_vmess_589
  - 油管绵阿羊_United States_vmess_590
  - 油管绵阿羊_South Africa_vmess_591
  - 油管绵阿羊_United States_vmess_592
  - 油管绵阿羊_United States_vmess_593
  - 油管绵阿羊_Costa Rica_vmess_594
  - 油管绵阿羊_United States_vmess_595
  - 油管绵阿羊_South Africa_vmess_596
  - 油管绵阿羊_United States_vmess_597
  - 油管绵阿羊_United States_vmess_598
  - 油管绵阿羊_Japan_vmess_599
  - 油管绵阿羊_United States_vmess_5100
  - 油管绵阿羊_Italy_vmess_5101
  - 油管绵阿羊_None_vmess_5102
  - 油管绵阿羊_Australia_vmess_5103
  - 油管绵阿羊_United States_vmess_5104
  - 油管绵阿羊_Spain_vmess_5105
  - 油管绵阿羊_India_vmess_5106
  - 油管绵阿羊_South Africa_vmess_5107
  - 油管绵阿羊_United States_vmess_5108
  - 油管绵阿羊_United States_vmess_5109
  - 油管绵阿羊_Netherlands_vmess_5110
  - 油管绵阿羊_United States_vmess_5111
  - 油管绵阿羊_United States_vmess_5112
  - 油管绵阿羊_United States_vmess_5113
  - 油管绵阿羊_None_vmess_5114
  - 油管绵阿羊_United States_vmess_5115
  - 油管绵阿羊_United States_vmess_5116
  - 油管绵阿羊_United States_vmess_5117
  - 油管绵阿羊_United States_vmess_5118
  - 油管绵阿羊_Costa Rica_vmess_5119
  - 油管绵阿羊_None_vmess_5120
  - 油管绵阿羊_United States_vmess_5121
  - 油管绵阿羊_None_vmess_5122
  - 油管绵阿羊_South Africa_vmess_5123
  - 油管绵阿羊_None_vmess_5124
  - 油管绵阿羊_South Africa_vmess_5125
  - 油管绵阿羊_United States_vmess_5126
  - 油管绵阿羊_None_vmess_5127
  - 油管绵阿羊_None_vmess_5128
  - 油管绵阿羊_United States_vmess_5129
  - 油管绵阿羊_South Africa_vmess_5130
  - 油管绵阿羊_United States_vmess_5131
  - 油管绵阿羊_Oman_vmess_5132
  - 油管绵阿羊_Netherlands_vmess_5133
  - 油管绵阿羊_None_vmess_5134
  - 油管绵阿羊_None_vmess_5135
  - 油管绵阿羊_Costa Rica_vmess_5136
  - 油管绵阿羊_United States_vmess_5137
  - 油管绵阿羊_None_vmess_5138
  - 油管绵阿羊_France_vmess_5139
  - 油管绵阿羊_United States_vmess_5140
  - 油管绵阿羊_None_vmess_5141
  - 油管绵阿羊_United States_vmess_5142
  - 油管绵阿羊_United States_vmess_5143
  - 油管绵阿羊_United States_vmess_5144
  - 油管绵阿羊_Japan_vmess_5145
  - 油管绵阿羊_South Africa_vmess_5146
  - 油管绵阿羊_Belgium_vmess_5147
  - 油管绵阿羊_None_vmess_5148
  - 油管绵阿羊_Australia_vmess_5149
  - 油管绵阿羊_Australia_vmess_5150
  - 油管绵阿羊_Australia_vmess_5151
  - 油管绵阿羊_Singapore_vmess_5152
  - 油管绵阿羊_United States_vmess_5153
  - 油管绵阿羊_Czechia_vmess_5154
  - 油管绵阿羊_Hong Kong_vmess_5155
  - 油管绵阿羊_United States_vmess_5156
  - 油管绵阿羊_United States_vmess_5157
  - 油管绵阿羊_South Africa_vmess_5158
  - 油管绵阿羊_None_vmess_5159
  - 油管绵阿羊_United States_vmess_5160
  - 油管绵阿羊_United States_vmess_5161
  - 油管绵阿羊_Costa Rica_vmess_5162
  - 油管绵阿羊_United States_vmess_5163
  - 油管绵阿羊_None_vmess_5164
  - 油管绵阿羊_United States_vmess_5165
  - 油管绵阿羊_None_vmess_5166
  - 油管绵阿羊_Costa Rica_vmess_5167
  - 油管绵阿羊_United States_vmess_5168
  - 油管绵阿羊_United States_vmess_5169
  - 油管绵阿羊_None_vmess_5170
  - 油管绵阿羊_United States_vmess_5171
  - 油管绵阿羊_None_vmess_5172
  - 油管绵阿羊_Japan_vmess_5173
  - 油管绵阿羊_None_vmess_5174
  - 油管绵阿羊_Costa Rica_vmess_5175
  - 油管绵阿羊_United States_vmess_5176
  - 油管绵阿羊_None_vmess_5177
  - 油管绵阿羊_None_vmess_5178
  - 油管绵阿羊_United States_vmess_5179
  - 油管绵阿羊_Spain_vmess_5180
  - 油管绵阿羊_Costa Rica_vmess_5181
  - 油管绵阿羊_Hong Kong_vmess_5182
  - 油管绵阿羊_United States_vmess_5183
  - 油管绵阿羊_None_vmess_5184
  - 油管绵阿羊_South Africa_vmess_5185
  - 油管绵阿羊_United States_vmess_5186
  - 油管绵阿羊_United States_vmess_5187
  - 油管绵阿羊_United States_vmess_5188
  - 油管绵阿羊_None_vmess_5189
  - 油管绵阿羊_United States_vmess_5190
  - 油管绵阿羊_Hong Kong_vmess_5191
  - 油管绵阿羊_United States_vmess_5192
  - 油管绵阿羊_None_vmess_5193
  - 油管绵阿羊_Japan_vmess_5194
  - 油管绵阿羊_None_vmess_5195
  - 油管绵阿羊_United States_vmess_5196
  - 油管绵阿羊_Costa Rica_vmess_5197
  - 油管绵阿羊_Costa Rica_vmess_5198
  - 油管绵阿羊_Spain_vmess_5199
  - 油管绵阿羊_Ecuador_vmess_5200
  - 油管绵阿羊_Netherlands_vmess_5201
  - 油管绵阿羊_Australia_vmess_5202
  - 油管绵阿羊_None_vmess_5203
  - 油管绵阿羊_Netherlands_vmess_5204
  - 油管绵阿羊_United States_vmess_5205
  - 油管绵阿羊_South Africa_vmess_5206
  - 油管绵阿羊_Spain_vmess_5207
  - 油管绵阿羊_None_vmess_5208
  - 油管绵阿羊_Italy_vmess_5209
  - 油管绵阿羊_Brazil_vmess_5210
  - 油管绵阿羊_United States_vmess_5211
  - 油管绵阿羊_United States_vmess_5212
  - 油管绵阿羊_Costa Rica_vmess_5213
  - 油管绵阿羊_South Africa_vmess_5214
  - 油管绵阿羊_United States_vmess_5215
  - 油管绵阿羊_None_vmess_5216
  - 油管绵阿羊_Costa Rica_vmess_5217
  - 油管绵阿羊_United States_vmess_5218
  - 油管绵阿羊_South Africa_vmess_5219
  - 油管绵阿羊_None_vmess_5220
  - 油管绵阿羊_United States_vmess_5221
  - 油管绵阿羊_Spain_vmess_5222
  - 油管绵阿羊_Japan_vmess_5223
  - 油管绵阿羊_South Africa_vmess_5224
  - 油管绵阿羊_South Africa_vmess_5225
  - 油管绵阿羊_Japan_vmess_5226
  - 油管绵阿羊_United States_vmess_5227
  - 油管绵阿羊_Japan_vmess_5228
  - 油管绵阿羊_United States_vmess_5229
  - 油管绵阿羊_South Africa_vmess_5230
  - 油管绵阿羊_United States_vmess_5231
  - 油管绵阿羊_None_vmess_5232
  - 油管绵阿羊_Italy_vmess_5233
  - 油管绵阿羊_United States_vmess_5234
  - 油管绵阿羊_United States_vmess_5235
  - 油管绵阿羊_United States_vmess_5236
  - 油管绵阿羊_None_vmess_5237
  - 油管绵阿羊_Costa Rica_vmess_5238
  - 油管绵阿羊_United States_vmess_5239
  - 油管绵阿羊_Costa Rica_vmess_5240
  - 油管绵阿羊_Costa Rica_vmess_5241
  - 油管绵阿羊_Japan_vmess_5242
  - 油管绵阿羊_United States_vmess_5243
  - 油管绵阿羊_None_vmess_5244
  - 油管绵阿羊_United States_vmess_5245
  - 油管绵阿羊_Spain_vmess_5246
  - 油管绵阿羊_United States_vmess_5247
  - 油管绵阿羊_Costa Rica_vmess_5248
  - 油管绵阿羊_Australia_vmess_5249
  - 油管绵阿羊_None_vmess_5250
  - 油管绵阿羊_United States_vmess_5251
  - 油管绵阿羊_Australia_vmess_5252
  - 油管绵阿羊_United States_vmess_5253
  - 油管绵阿羊_United States_vmess_5254
  - 油管绵阿羊_United States_vmess_5255
  - 油管绵阿羊_United States_vmess_5256
  - 油管绵阿羊_France_vmess_5257
  - 油管绵阿羊_United States_vmess_5258
  - 油管绵阿羊_United States_vmess_5259
  - 油管绵阿羊_United States_vmess_5260
  - 油管绵阿羊_United States_vmess_5261
  - 油管绵阿羊_United States_vmess_5262
  - 油管绵阿羊_United States_vmess_5263
  - 油管绵阿羊_United States_vmess_5264
  - 油管绵阿羊_Costa Rica_vmess_5265
  - 油管绵阿羊_Hong Kong_vmess_5266
  - 油管绵阿羊_Costa Rica_vmess_5267
  - 油管绵阿羊_None_vmess_5268
  - 油管绵阿羊_United States_vmess_5269
  - 油管绵阿羊_None_vmess_5270
  - 油管绵阿羊_United States_vmess_5271
  - 油管绵阿羊_Australia_vmess_5272
  - 油管绵阿羊_United States_vmess_5273
  - 油管绵阿羊_Brazil_vmess_5274
  - 油管绵阿羊_Japan_vmess_5275
  - 油管绵阿羊_United States_vmess_5276
  - 油管绵阿羊_Austria_vmess_5277
  - 油管绵阿羊_Costa Rica_vmess_5278
  - 油管绵阿羊_None_vmess_5279
  - 油管绵阿羊_None_vmess_5280
  - 油管绵阿羊_United States_vmess_5281
  - 油管绵阿羊_Costa Rica_vmess_5282
  - 油管绵阿羊_United States_vmess_5283
  - 油管绵阿羊_United States_vmess_5284
  - 油管绵阿羊_South Africa_vmess_5285
  - 油管绵阿羊_United States_vmess_5286
  - 油管绵阿羊_Japan_vmess_5287
  - 油管绵阿羊_United States_vmess_5288
  - 油管绵阿羊_None_vmess_5289
  - 油管绵阿羊_Spain_vmess_5290
  - 油管绵阿羊_Singapore_vmess_5291
  - 油管绵阿羊_United States_vmess_5292
  - 油管绵阿羊_Canada_vmess_5293
  - 油管绵阿羊_None_vmess_5294
  - 油管绵阿羊_None_vmess_5295
  - 油管绵阿羊_None_vmess_5296
  - 油管绵阿羊_United States_vmess_5297
  - 油管绵阿羊_Australia_vmess_5298
  - 油管绵阿羊_United States_vmess_5299
  - 油管绵阿羊_United States_vmess_5300
  - 油管绵阿羊_Costa Rica_vmess_5301
  - 油管绵阿羊_United States_vmess_5302
  - 油管绵阿羊_Costa Rica_vmess_5303
  - 油管绵阿羊_South Africa_vmess_5304
  - 油管绵阿羊_None_vmess_5305
  - 油管绵阿羊_Costa Rica_vmess_5306
  - 油管绵阿羊_Singapore_vmess_5307
  - 油管绵阿羊_None_vmess_5308
  - 油管绵阿羊_United States_vmess_5309
  - 油管绵阿羊_None_vmess_5310
  - 油管绵阿羊_United States_vmess_5311
  - 油管绵阿羊_None_vmess_5312
  - 油管绵阿羊_Italy_vmess_5313
  - 油管绵阿羊_South Africa_vmess_5314
  - 油管绵阿羊_Singapore_vmess_5315
  - 油管绵阿羊_Hong Kong_vmess_5316
  - 油管绵阿羊_None_vmess_5317
  - 油管绵阿羊_None_vmess_5318
  - 油管绵阿羊_None_vmess_5319
  - 油管绵阿羊_None_vmess_5320
  - 油管绵阿羊_United States_vmess_5321
  - 油管绵阿羊_United States_vmess_5322
  - 油管绵阿羊_Costa Rica_vmess_5323
  - 油管绵阿羊_United States_vmess_5324
  - 油管绵阿羊_Costa Rica_vmess_5325
  - 油管绵阿羊_None_vmess_5326
  - 油管绵阿羊_Japan_vmess_5327
  - 油管绵阿羊_None_vmess_5328
  - 油管绵阿羊_Spain_vmess_5329
  - 油管绵阿羊_None_vmess_5330
  - 油管绵阿羊_United States_vmess_5331
  - 油管绵阿羊_United States_vmess_5332
  - 油管绵阿羊_India_vmess_5333
  - 油管绵阿羊_United Kingdom_vmess_5334
  - 油管绵阿羊_Australia_vmess_5335
  - 油管绵阿羊_United States_vmess_5336
  - 油管绵阿羊_Hong Kong_vmess_5337
  - 油管绵阿羊_Costa Rica_vmess_5338
  - 油管绵阿羊_United States_vmess_5339
  - 油管绵阿羊_None_vmess_5340
  - 油管绵阿羊_United States_vmess_5341
  - 油管绵阿羊_United States_vmess_5342
  - 油管绵阿羊_Costa Rica_vmess_5343
  - 油管绵阿羊_Costa Rica_vmess_5344
  - 油管绵阿羊_None_vmess_5345
  - 油管绵阿羊_None_vmess_5346
  - 油管绵阿羊_None_vmess_5347
  - 油管绵阿羊_United States_vmess_5348
  - 油管绵阿羊_United States_vmess_5349
  - 油管绵阿羊_None_vmess_5350
  - 油管绵阿羊_United States_vmess_5351
  - 油管绵阿羊_United States_vmess_5352
  - 油管绵阿羊_Australia_vmess_5353
  - 油管绵阿羊_United States_vmess_5354
  - 油管绵阿羊_None_vmess_5355
  - 油管绵阿羊_United States_vmess_5356
  - 油管绵阿羊_South Africa_vmess_5357
  - 油管绵阿羊_None_vmess_5358
  - 油管绵阿羊_United States_vmess_5359
  - 油管绵阿羊_Czechia_vmess_5360
  - 油管绵阿羊_United States_vmess_5361
  - 油管绵阿羊_None_vmess_5362
  - 油管绵阿羊_None_vmess_5363
  - 油管绵阿羊_United States_vmess_5364
  - 油管绵阿羊_South Africa_vmess_5365
  - 油管绵阿羊_None_vmess_5366
  - 油管绵阿羊_None_vmess_5367
  - 油管绵阿羊_Costa Rica_vmess_5368
  - 油管绵阿羊_None_vmess_5369
  - 油管绵阿羊_Netherlands_vmess_5370
  - 油管绵阿羊_Australia_vmess_5371
  - 油管绵阿羊_South Africa_vmess_5372
  - 油管绵阿羊_Costa Rica_vmess_5373
  - 油管绵阿羊_United States_vmess_5374
  - 油管绵阿羊_Costa Rica_vmess_5375
  - 油管绵阿羊_United States_vmess_5376
  - 油管绵阿羊_Italy_vmess_5377
  - 油管绵阿羊_United Kingdom_vmess_5378
  - 油管绵阿羊_United States_vmess_5379
  - 油管绵阿羊_United States_vmess_5380
  - 油管绵阿羊_Costa Rica_vmess_5381
  - 油管绵阿羊_None_vmess_5382
  - 油管绵阿羊_South Africa_vmess_5383
  - 油管绵阿羊_United States_vmess_5384
  - 油管绵阿羊_None_vmess_5385
  - 油管绵阿羊_None_vmess_5386
  - 油管绵阿羊_United States_vmess_5387
  - 油管绵阿羊_Costa Rica_vmess_5388
  - 油管绵阿羊_United States_vmess_5389
  - 油管绵阿羊_Spain_vmess_5390
  - 油管绵阿羊_Costa Rica_vmess_5391
  - 油管绵阿羊_United States_vmess_5392
  - 油管绵阿羊_Japan_vmess_5393
  - 油管绵阿羊_United States_vmess_5394
  - 油管绵阿羊_Hong Kong_vmess_5395
  - 油管绵阿羊_United States_vmess_5396
  - 油管绵阿羊_United States_vmess_5397
  - 油管绵阿羊_United States_vmess_5398
  - 油管绵阿羊_United States_vmess_5399
  - 油管绵阿羊_Australia_vmess_5400
  - 油管绵阿羊_South Africa_vmess_5401
  - 油管绵阿羊_United States_vmess_5402
  - 油管绵阿羊_Costa Rica_vmess_5403
  - 油管绵阿羊_United States_vmess_5404
  - 油管绵阿羊_Australia_vmess_5405
  - 油管绵阿羊_United States_vmess_5406
  - 油管绵阿羊_United States_vmess_5407
  - 油管绵阿羊_Singapore_vmess_5408
  - 油管绵阿羊_United States_vmess_5409
  - 油管绵阿羊_None_vmess_5410
  - 油管绵阿羊_None_vmess_5411
  - 油管绵阿羊_Spain_vmess_5412
  - 油管绵阿羊_Hong Kong_vmess_5413
  - 油管绵阿羊_None_vmess_5414
  - 油管绵阿羊_United States_vmess_5415
  - 油管绵阿羊_United States_vmess_5416
  - 油管绵阿羊_United States_vmess_5417
  - 油管绵阿羊_United States_vmess_5418
  - 油管绵阿羊_Costa Rica_vmess_5419
  - 油管绵阿羊_Costa Rica_vmess_5420
  - 油管绵阿羊_United States_vmess_5421
  - 油管绵阿羊_Costa Rica_vmess_5422
  - 油管绵阿羊_Japan_vmess_5423
  - 油管绵阿羊_South Africa_vmess_5424
  - 油管绵阿羊_United States_vmess_5425
  - 油管绵阿羊_United States_vmess_5426
  - 油管绵阿羊_South Korea_vmess_5427
  - 油管绵阿羊_United States_vmess_5428
  - 油管绵阿羊_United States_vmess_5429
  - 油管绵阿羊_None_vmess_5430
  - 油管绵阿羊_None_vmess_5431
  - 油管绵阿羊_United States_vmess_5432
  - 油管绵阿羊_United States_vmess_5433
  - 油管绵阿羊_United States_vmess_5434
  - 油管绵阿羊_Japan_vmess_5435
  - 油管绵阿羊_Costa Rica_vmess_5436
  - 油管绵阿羊_United States_vmess_5437
  - 油管绵阿羊_United States_vmess_5438
  - 油管绵阿羊_United States_vmess_5439
  - 油管绵阿羊_United States_vmess_5440
  - 油管绵阿羊_None_vmess_5441
  - 油管绵阿羊_Netherlands_vmess_5442
  - 油管绵阿羊_United States_vmess_5443
  - 油管绵阿羊_None_vmess_5444
  - 油管绵阿羊_South Africa_vmess_5445
  - 油管绵阿羊_Costa Rica_vmess_5446
  - 油管绵阿羊_United States_vmess_5447
  - 油管绵阿羊_United States_vmess_5448
  - 油管绵阿羊_United States_vmess_5449
  - 油管绵阿羊_Kenya_vmess_5450
  - 油管绵阿羊_United States_vmess_5451
  - 油管绵阿羊_United States_vmess_5452
  - 油管绵阿羊_None_vmess_5453
  - 油管绵阿羊_Spain_vmess_5454
  - 油管绵阿羊_Costa Rica_vmess_5455
  - 油管绵阿羊_United States_vmess_5456
  - 油管绵阿羊_Germany_vmess_5457
  - 油管绵阿羊_United States_vmess_5458
  - 油管绵阿羊_None_vmess_5459
  - 油管绵阿羊_Costa Rica_vmess_5460
  - 油管绵阿羊_None_vmess_5461
  - 油管绵阿羊_Paraguay_vmess_5462
  - 油管绵阿羊_Australia_vmess_5463
  - 油管绵阿羊_United States_vmess_5464
  - 油管绵阿羊_South Africa_vmess_5465
  - 油管绵阿羊_None_vmess_5466
  - 油管绵阿羊_United States_vmess_5467
  - 油管绵阿羊_United States_vmess_5468
  - 油管绵阿羊_Spain_vmess_5469
  - 油管绵阿羊_United States_vmess_5470
  - 油管绵阿羊_United States_vmess_5471
  - 油管绵阿羊_None_vmess_5472
  - 油管绵阿羊_None_vmess_5473
  - 油管绵阿羊_None_vmess_5474
  - 油管绵阿羊_Germany_vmess_5475
  - 油管绵阿羊_India_vmess_5476
  - 油管绵阿羊_Costa Rica_vmess_5477
  - 油管绵阿羊_None_vmess_5478
  - 油管绵阿羊_Germany_vmess_5479
  - 油管绵阿羊_Netherlands_vmess_5480
  - 油管绵阿羊_United States_vmess_5481
  - 油管绵阿羊_United States_vmess_5482
  - 油管绵阿羊_Italy_vmess_5483
  - 油管绵阿羊_Australia_vmess_5484
  - 油管绵阿羊_United States_vmess_5485
  - 油管绵阿羊_None_vmess_5486
  - 油管绵阿羊_None_vmess_5487
  - 油管绵阿羊_United States_vmess_5488
  - 油管绵阿羊_United States_vmess_5489
  - 油管绵阿羊_Costa Rica_vmess_5490
  - 油管绵阿羊_None_vmess_5491
  - 油管绵阿羊_None_vmess_5492
  - 油管绵阿羊_Costa Rica_vmess_5493
  - 油管绵阿羊_United States_vmess_5494
  - 油管绵阿羊_United States_vmess_5495
  - 油管绵阿羊_United States_vmess_5496
  - 油管绵阿羊_Netherlands_vmess_5497
  - 油管绵阿羊_Japan_vmess_5498
  - 油管绵阿羊_Costa Rica_vmess_5499
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
  - 油管绵阿羊_None_vmess_51
  - 油管绵阿羊_United States_vmess_52
  - 油管绵阿羊_United States_vmess_53
  - 油管绵阿羊_Japan_vmess_54
  - 油管绵阿羊_Australia_vmess_55
  - 油管绵阿羊_United States_vmess_56
  - 油管绵阿羊_None_vmess_57
  - 油管绵阿羊_Brazil_vmess_58
  - 油管绵阿羊_United States_vmess_59
  - 油管绵阿羊_United States_vmess_510
  - 油管绵阿羊_None_vmess_511
  - 油管绵阿羊_United States_vmess_512
  - 油管绵阿羊_South Africa_vmess_513
  - 油管绵阿羊_Japan_vmess_514
  - 油管绵阿羊_United States_vmess_515
  - 油管绵阿羊_Italy_vmess_516
  - 油管绵阿羊_United States_vmess_517
  - 油管绵阿羊_United States_vmess_518
  - 油管绵阿羊_Singapore_vmess_519
  - 油管绵阿羊_None_vmess_520
  - 油管绵阿羊_Singapore_vmess_521
  - 油管绵阿羊_None_vmess_522
  - 油管绵阿羊_Costa Rica_vmess_523
  - 油管绵阿羊_Costa Rica_vmess_524
  - 油管绵阿羊_Japan_vmess_525
  - 油管绵阿羊_None_vmess_526
  - 油管绵阿羊_None_vmess_527
  - 油管绵阿羊_United States_vmess_528
  - 油管绵阿羊_United States_vmess_529
  - 油管绵阿羊_United States_vmess_530
  - 油管绵阿羊_None_vmess_531
  - 油管绵阿羊_South Africa_vmess_532
  - 油管绵阿羊_Costa Rica_vmess_533
  - 油管绵阿羊_Netherlands_vmess_534
  - 油管绵阿羊_Costa Rica_vmess_535
  - 油管绵阿羊_Costa Rica_vmess_536
  - 油管绵阿羊_United States_vmess_537
  - 油管绵阿羊_Spain_vmess_538
  - 油管绵阿羊_United States_vmess_539
  - 油管绵阿羊_United States_vmess_540
  - 油管绵阿羊_Costa Rica_vmess_541
  - 油管绵阿羊_Costa Rica_vmess_542
  - 油管绵阿羊_Netherlands_vmess_543
  - 油管绵阿羊_South Africa_vmess_544
  - 油管绵阿羊_Spain_vmess_545
  - 油管绵阿羊_None_vmess_546
  - 油管绵阿羊_None_vmess_547
  - 油管绵阿羊_None_vmess_548
  - 油管绵阿羊_United States_vmess_549
  - 油管绵阿羊_None_vmess_550
  - 油管绵阿羊_South Africa_vmess_551
  - 油管绵阿羊_None_vmess_552
  - 油管绵阿羊_United States_vmess_553
  - 油管绵阿羊_South Africa_vmess_554
  - 油管绵阿羊_Costa Rica_vmess_555
  - 油管绵阿羊_Costa Rica_vmess_556
  - 油管绵阿羊_Singapore_vmess_557
  - 油管绵阿羊_None_vmess_558
  - 油管绵阿羊_Italy_vmess_559
  - 油管绵阿羊_Rwanda_vmess_560
  - 油管绵阿羊_United States_vmess_561
  - 油管绵阿羊_United States_vmess_562
  - 油管绵阿羊_United States_vmess_563
  - 油管绵阿羊_United States_vmess_564
  - 油管绵阿羊_United States_vmess_565
  - 油管绵阿羊_United Arab Emirates_vmess_566
  - 油管绵阿羊_United States_vmess_567
  - 油管绵阿羊_None_vmess_568
  - 油管绵阿羊_Germany_vmess_569
  - 油管绵阿羊_United States_vmess_570
  - 油管绵阿羊_Spain_vmess_571
  - 油管绵阿羊_Costa Rica_vmess_572
  - 油管绵阿羊_None_vmess_573
  - 油管绵阿羊_Costa Rica_vmess_574
  - 油管绵阿羊_South Africa_vmess_575
  - 油管绵阿羊_None_vmess_576
  - 油管绵阿羊_None_vmess_577
  - 油管绵阿羊_Costa Rica_vmess_578
  - 油管绵阿羊_Japan_vmess_579
  - 油管绵阿羊_United States_vmess_580
  - 油管绵阿羊_Netherlands_vmess_581
  - 油管绵阿羊_United States_vmess_582
  - 油管绵阿羊_Singapore_vmess_583
  - 油管绵阿羊_None_vmess_584
  - 油管绵阿羊_South Africa_vmess_585
  - 油管绵阿羊_United States_vmess_586
  - 油管绵阿羊_Canada_vmess_587
  - 油管绵阿羊_None_vmess_588
  - 油管绵阿羊_Costa Rica_vmess_589
  - 油管绵阿羊_United States_vmess_590
  - 油管绵阿羊_South Africa_vmess_591
  - 油管绵阿羊_United States_vmess_592
  - 油管绵阿羊_United States_vmess_593
  - 油管绵阿羊_Costa Rica_vmess_594
  - 油管绵阿羊_United States_vmess_595
  - 油管绵阿羊_South Africa_vmess_596
  - 油管绵阿羊_United States_vmess_597
  - 油管绵阿羊_United States_vmess_598
  - 油管绵阿羊_Japan_vmess_599
  - 油管绵阿羊_United States_vmess_5100
  - 油管绵阿羊_Italy_vmess_5101
  - 油管绵阿羊_None_vmess_5102
  - 油管绵阿羊_Australia_vmess_5103
  - 油管绵阿羊_United States_vmess_5104
  - 油管绵阿羊_Spain_vmess_5105
  - 油管绵阿羊_India_vmess_5106
  - 油管绵阿羊_South Africa_vmess_5107
  - 油管绵阿羊_United States_vmess_5108
  - 油管绵阿羊_United States_vmess_5109
  - 油管绵阿羊_Netherlands_vmess_5110
  - 油管绵阿羊_United States_vmess_5111
  - 油管绵阿羊_United States_vmess_5112
  - 油管绵阿羊_United States_vmess_5113
  - 油管绵阿羊_None_vmess_5114
  - 油管绵阿羊_United States_vmess_5115
  - 油管绵阿羊_United States_vmess_5116
  - 油管绵阿羊_United States_vmess_5117
  - 油管绵阿羊_United States_vmess_5118
  - 油管绵阿羊_Costa Rica_vmess_5119
  - 油管绵阿羊_None_vmess_5120
  - 油管绵阿羊_United States_vmess_5121
  - 油管绵阿羊_None_vmess_5122
  - 油管绵阿羊_South Africa_vmess_5123
  - 油管绵阿羊_None_vmess_5124
  - 油管绵阿羊_South Africa_vmess_5125
  - 油管绵阿羊_United States_vmess_5126
  - 油管绵阿羊_None_vmess_5127
  - 油管绵阿羊_None_vmess_5128
  - 油管绵阿羊_United States_vmess_5129
  - 油管绵阿羊_South Africa_vmess_5130
  - 油管绵阿羊_United States_vmess_5131
  - 油管绵阿羊_Oman_vmess_5132
  - 油管绵阿羊_Netherlands_vmess_5133
  - 油管绵阿羊_None_vmess_5134
  - 油管绵阿羊_None_vmess_5135
  - 油管绵阿羊_Costa Rica_vmess_5136
  - 油管绵阿羊_United States_vmess_5137
  - 油管绵阿羊_None_vmess_5138
  - 油管绵阿羊_France_vmess_5139
  - 油管绵阿羊_United States_vmess_5140
  - 油管绵阿羊_None_vmess_5141
  - 油管绵阿羊_United States_vmess_5142
  - 油管绵阿羊_United States_vmess_5143
  - 油管绵阿羊_United States_vmess_5144
  - 油管绵阿羊_Japan_vmess_5145
  - 油管绵阿羊_South Africa_vmess_5146
  - 油管绵阿羊_Belgium_vmess_5147
  - 油管绵阿羊_None_vmess_5148
  - 油管绵阿羊_Australia_vmess_5149
  - 油管绵阿羊_Australia_vmess_5150
  - 油管绵阿羊_Australia_vmess_5151
  - 油管绵阿羊_Singapore_vmess_5152
  - 油管绵阿羊_United States_vmess_5153
  - 油管绵阿羊_Czechia_vmess_5154
  - 油管绵阿羊_Hong Kong_vmess_5155
  - 油管绵阿羊_United States_vmess_5156
  - 油管绵阿羊_United States_vmess_5157
  - 油管绵阿羊_South Africa_vmess_5158
  - 油管绵阿羊_None_vmess_5159
  - 油管绵阿羊_United States_vmess_5160
  - 油管绵阿羊_United States_vmess_5161
  - 油管绵阿羊_Costa Rica_vmess_5162
  - 油管绵阿羊_United States_vmess_5163
  - 油管绵阿羊_None_vmess_5164
  - 油管绵阿羊_United States_vmess_5165
  - 油管绵阿羊_None_vmess_5166
  - 油管绵阿羊_Costa Rica_vmess_5167
  - 油管绵阿羊_United States_vmess_5168
  - 油管绵阿羊_United States_vmess_5169
  - 油管绵阿羊_None_vmess_5170
  - 油管绵阿羊_United States_vmess_5171
  - 油管绵阿羊_None_vmess_5172
  - 油管绵阿羊_Japan_vmess_5173
  - 油管绵阿羊_None_vmess_5174
  - 油管绵阿羊_Costa Rica_vmess_5175
  - 油管绵阿羊_United States_vmess_5176
  - 油管绵阿羊_None_vmess_5177
  - 油管绵阿羊_None_vmess_5178
  - 油管绵阿羊_United States_vmess_5179
  - 油管绵阿羊_Spain_vmess_5180
  - 油管绵阿羊_Costa Rica_vmess_5181
  - 油管绵阿羊_Hong Kong_vmess_5182
  - 油管绵阿羊_United States_vmess_5183
  - 油管绵阿羊_None_vmess_5184
  - 油管绵阿羊_South Africa_vmess_5185
  - 油管绵阿羊_United States_vmess_5186
  - 油管绵阿羊_United States_vmess_5187
  - 油管绵阿羊_United States_vmess_5188
  - 油管绵阿羊_None_vmess_5189
  - 油管绵阿羊_United States_vmess_5190
  - 油管绵阿羊_Hong Kong_vmess_5191
  - 油管绵阿羊_United States_vmess_5192
  - 油管绵阿羊_None_vmess_5193
  - 油管绵阿羊_Japan_vmess_5194
  - 油管绵阿羊_None_vmess_5195
  - 油管绵阿羊_United States_vmess_5196
  - 油管绵阿羊_Costa Rica_vmess_5197
  - 油管绵阿羊_Costa Rica_vmess_5198
  - 油管绵阿羊_Spain_vmess_5199
  - 油管绵阿羊_Ecuador_vmess_5200
  - 油管绵阿羊_Netherlands_vmess_5201
  - 油管绵阿羊_Australia_vmess_5202
  - 油管绵阿羊_None_vmess_5203
  - 油管绵阿羊_Netherlands_vmess_5204
  - 油管绵阿羊_United States_vmess_5205
  - 油管绵阿羊_South Africa_vmess_5206
  - 油管绵阿羊_Spain_vmess_5207
  - 油管绵阿羊_None_vmess_5208
  - 油管绵阿羊_Italy_vmess_5209
  - 油管绵阿羊_Brazil_vmess_5210
  - 油管绵阿羊_United States_vmess_5211
  - 油管绵阿羊_United States_vmess_5212
  - 油管绵阿羊_Costa Rica_vmess_5213
  - 油管绵阿羊_South Africa_vmess_5214
  - 油管绵阿羊_United States_vmess_5215
  - 油管绵阿羊_None_vmess_5216
  - 油管绵阿羊_Costa Rica_vmess_5217
  - 油管绵阿羊_United States_vmess_5218
  - 油管绵阿羊_South Africa_vmess_5219
  - 油管绵阿羊_None_vmess_5220
  - 油管绵阿羊_United States_vmess_5221
  - 油管绵阿羊_Spain_vmess_5222
  - 油管绵阿羊_Japan_vmess_5223
  - 油管绵阿羊_South Africa_vmess_5224
  - 油管绵阿羊_South Africa_vmess_5225
  - 油管绵阿羊_Japan_vmess_5226
  - 油管绵阿羊_United States_vmess_5227
  - 油管绵阿羊_Japan_vmess_5228
  - 油管绵阿羊_United States_vmess_5229
  - 油管绵阿羊_South Africa_vmess_5230
  - 油管绵阿羊_United States_vmess_5231
  - 油管绵阿羊_None_vmess_5232
  - 油管绵阿羊_Italy_vmess_5233
  - 油管绵阿羊_United States_vmess_5234
  - 油管绵阿羊_United States_vmess_5235
  - 油管绵阿羊_United States_vmess_5236
  - 油管绵阿羊_None_vmess_5237
  - 油管绵阿羊_Costa Rica_vmess_5238
  - 油管绵阿羊_United States_vmess_5239
  - 油管绵阿羊_Costa Rica_vmess_5240
  - 油管绵阿羊_Costa Rica_vmess_5241
  - 油管绵阿羊_Japan_vmess_5242
  - 油管绵阿羊_United States_vmess_5243
  - 油管绵阿羊_None_vmess_5244
  - 油管绵阿羊_United States_vmess_5245
  - 油管绵阿羊_Spain_vmess_5246
  - 油管绵阿羊_United States_vmess_5247
  - 油管绵阿羊_Costa Rica_vmess_5248
  - 油管绵阿羊_Australia_vmess_5249
  - 油管绵阿羊_None_vmess_5250
  - 油管绵阿羊_United States_vmess_5251
  - 油管绵阿羊_Australia_vmess_5252
  - 油管绵阿羊_United States_vmess_5253
  - 油管绵阿羊_United States_vmess_5254
  - 油管绵阿羊_United States_vmess_5255
  - 油管绵阿羊_United States_vmess_5256
  - 油管绵阿羊_France_vmess_5257
  - 油管绵阿羊_United States_vmess_5258
  - 油管绵阿羊_United States_vmess_5259
  - 油管绵阿羊_United States_vmess_5260
  - 油管绵阿羊_United States_vmess_5261
  - 油管绵阿羊_United States_vmess_5262
  - 油管绵阿羊_United States_vmess_5263
  - 油管绵阿羊_United States_vmess_5264
  - 油管绵阿羊_Costa Rica_vmess_5265
  - 油管绵阿羊_Hong Kong_vmess_5266
  - 油管绵阿羊_Costa Rica_vmess_5267
  - 油管绵阿羊_None_vmess_5268
  - 油管绵阿羊_United States_vmess_5269
  - 油管绵阿羊_None_vmess_5270
  - 油管绵阿羊_United States_vmess_5271
  - 油管绵阿羊_Australia_vmess_5272
  - 油管绵阿羊_United States_vmess_5273
  - 油管绵阿羊_Brazil_vmess_5274
  - 油管绵阿羊_Japan_vmess_5275
  - 油管绵阿羊_United States_vmess_5276
  - 油管绵阿羊_Austria_vmess_5277
  - 油管绵阿羊_Costa Rica_vmess_5278
  - 油管绵阿羊_None_vmess_5279
  - 油管绵阿羊_None_vmess_5280
  - 油管绵阿羊_United States_vmess_5281
  - 油管绵阿羊_Costa Rica_vmess_5282
  - 油管绵阿羊_United States_vmess_5283
  - 油管绵阿羊_United States_vmess_5284
  - 油管绵阿羊_South Africa_vmess_5285
  - 油管绵阿羊_United States_vmess_5286
  - 油管绵阿羊_Japan_vmess_5287
  - 油管绵阿羊_United States_vmess_5288
  - 油管绵阿羊_None_vmess_5289
  - 油管绵阿羊_Spain_vmess_5290
  - 油管绵阿羊_Singapore_vmess_5291
  - 油管绵阿羊_United States_vmess_5292
  - 油管绵阿羊_Canada_vmess_5293
  - 油管绵阿羊_None_vmess_5294
  - 油管绵阿羊_None_vmess_5295
  - 油管绵阿羊_None_vmess_5296
  - 油管绵阿羊_United States_vmess_5297
  - 油管绵阿羊_Australia_vmess_5298
  - 油管绵阿羊_United States_vmess_5299
  - 油管绵阿羊_United States_vmess_5300
  - 油管绵阿羊_Costa Rica_vmess_5301
  - 油管绵阿羊_United States_vmess_5302
  - 油管绵阿羊_Costa Rica_vmess_5303
  - 油管绵阿羊_South Africa_vmess_5304
  - 油管绵阿羊_None_vmess_5305
  - 油管绵阿羊_Costa Rica_vmess_5306
  - 油管绵阿羊_Singapore_vmess_5307
  - 油管绵阿羊_None_vmess_5308
  - 油管绵阿羊_United States_vmess_5309
  - 油管绵阿羊_None_vmess_5310
  - 油管绵阿羊_United States_vmess_5311
  - 油管绵阿羊_None_vmess_5312
  - 油管绵阿羊_Italy_vmess_5313
  - 油管绵阿羊_South Africa_vmess_5314
  - 油管绵阿羊_Singapore_vmess_5315
  - 油管绵阿羊_Hong Kong_vmess_5316
  - 油管绵阿羊_None_vmess_5317
  - 油管绵阿羊_None_vmess_5318
  - 油管绵阿羊_None_vmess_5319
  - 油管绵阿羊_None_vmess_5320
  - 油管绵阿羊_United States_vmess_5321
  - 油管绵阿羊_United States_vmess_5322
  - 油管绵阿羊_Costa Rica_vmess_5323
  - 油管绵阿羊_United States_vmess_5324
  - 油管绵阿羊_Costa Rica_vmess_5325
  - 油管绵阿羊_None_vmess_5326
  - 油管绵阿羊_Japan_vmess_5327
  - 油管绵阿羊_None_vmess_5328
  - 油管绵阿羊_Spain_vmess_5329
  - 油管绵阿羊_None_vmess_5330
  - 油管绵阿羊_United States_vmess_5331
  - 油管绵阿羊_United States_vmess_5332
  - 油管绵阿羊_India_vmess_5333
  - 油管绵阿羊_United Kingdom_vmess_5334
  - 油管绵阿羊_Australia_vmess_5335
  - 油管绵阿羊_United States_vmess_5336
  - 油管绵阿羊_Hong Kong_vmess_5337
  - 油管绵阿羊_Costa Rica_vmess_5338
  - 油管绵阿羊_United States_vmess_5339
  - 油管绵阿羊_None_vmess_5340
  - 油管绵阿羊_United States_vmess_5341
  - 油管绵阿羊_United States_vmess_5342
  - 油管绵阿羊_Costa Rica_vmess_5343
  - 油管绵阿羊_Costa Rica_vmess_5344
  - 油管绵阿羊_None_vmess_5345
  - 油管绵阿羊_None_vmess_5346
  - 油管绵阿羊_None_vmess_5347
  - 油管绵阿羊_United States_vmess_5348
  - 油管绵阿羊_United States_vmess_5349
  - 油管绵阿羊_None_vmess_5350
  - 油管绵阿羊_United States_vmess_5351
  - 油管绵阿羊_United States_vmess_5352
  - 油管绵阿羊_Australia_vmess_5353
  - 油管绵阿羊_United States_vmess_5354
  - 油管绵阿羊_None_vmess_5355
  - 油管绵阿羊_United States_vmess_5356
  - 油管绵阿羊_South Africa_vmess_5357
  - 油管绵阿羊_None_vmess_5358
  - 油管绵阿羊_United States_vmess_5359
  - 油管绵阿羊_Czechia_vmess_5360
  - 油管绵阿羊_United States_vmess_5361
  - 油管绵阿羊_None_vmess_5362
  - 油管绵阿羊_None_vmess_5363
  - 油管绵阿羊_United States_vmess_5364
  - 油管绵阿羊_South Africa_vmess_5365
  - 油管绵阿羊_None_vmess_5366
  - 油管绵阿羊_None_vmess_5367
  - 油管绵阿羊_Costa Rica_vmess_5368
  - 油管绵阿羊_None_vmess_5369
  - 油管绵阿羊_Netherlands_vmess_5370
  - 油管绵阿羊_Australia_vmess_5371
  - 油管绵阿羊_South Africa_vmess_5372
  - 油管绵阿羊_Costa Rica_vmess_5373
  - 油管绵阿羊_United States_vmess_5374
  - 油管绵阿羊_Costa Rica_vmess_5375
  - 油管绵阿羊_United States_vmess_5376
  - 油管绵阿羊_Italy_vmess_5377
  - 油管绵阿羊_United Kingdom_vmess_5378
  - 油管绵阿羊_United States_vmess_5379
  - 油管绵阿羊_United States_vmess_5380
  - 油管绵阿羊_Costa Rica_vmess_5381
  - 油管绵阿羊_None_vmess_5382
  - 油管绵阿羊_South Africa_vmess_5383
  - 油管绵阿羊_United States_vmess_5384
  - 油管绵阿羊_None_vmess_5385
  - 油管绵阿羊_None_vmess_5386
  - 油管绵阿羊_United States_vmess_5387
  - 油管绵阿羊_Costa Rica_vmess_5388
  - 油管绵阿羊_United States_vmess_5389
  - 油管绵阿羊_Spain_vmess_5390
  - 油管绵阿羊_Costa Rica_vmess_5391
  - 油管绵阿羊_United States_vmess_5392
  - 油管绵阿羊_Japan_vmess_5393
  - 油管绵阿羊_United States_vmess_5394
  - 油管绵阿羊_Hong Kong_vmess_5395
  - 油管绵阿羊_United States_vmess_5396
  - 油管绵阿羊_United States_vmess_5397
  - 油管绵阿羊_United States_vmess_5398
  - 油管绵阿羊_United States_vmess_5399
  - 油管绵阿羊_Australia_vmess_5400
  - 油管绵阿羊_South Africa_vmess_5401
  - 油管绵阿羊_United States_vmess_5402
  - 油管绵阿羊_Costa Rica_vmess_5403
  - 油管绵阿羊_United States_vmess_5404
  - 油管绵阿羊_Australia_vmess_5405
  - 油管绵阿羊_United States_vmess_5406
  - 油管绵阿羊_United States_vmess_5407
  - 油管绵阿羊_Singapore_vmess_5408
  - 油管绵阿羊_United States_vmess_5409
  - 油管绵阿羊_None_vmess_5410
  - 油管绵阿羊_None_vmess_5411
  - 油管绵阿羊_Spain_vmess_5412
  - 油管绵阿羊_Hong Kong_vmess_5413
  - 油管绵阿羊_None_vmess_5414
  - 油管绵阿羊_United States_vmess_5415
  - 油管绵阿羊_United States_vmess_5416
  - 油管绵阿羊_United States_vmess_5417
  - 油管绵阿羊_United States_vmess_5418
  - 油管绵阿羊_Costa Rica_vmess_5419
  - 油管绵阿羊_Costa Rica_vmess_5420
  - 油管绵阿羊_United States_vmess_5421
  - 油管绵阿羊_Costa Rica_vmess_5422
  - 油管绵阿羊_Japan_vmess_5423
  - 油管绵阿羊_South Africa_vmess_5424
  - 油管绵阿羊_United States_vmess_5425
  - 油管绵阿羊_United States_vmess_5426
  - 油管绵阿羊_South Korea_vmess_5427
  - 油管绵阿羊_United States_vmess_5428
  - 油管绵阿羊_United States_vmess_5429
  - 油管绵阿羊_None_vmess_5430
  - 油管绵阿羊_None_vmess_5431
  - 油管绵阿羊_United States_vmess_5432
  - 油管绵阿羊_United States_vmess_5433
  - 油管绵阿羊_United States_vmess_5434
  - 油管绵阿羊_Japan_vmess_5435
  - 油管绵阿羊_Costa Rica_vmess_5436
  - 油管绵阿羊_United States_vmess_5437
  - 油管绵阿羊_United States_vmess_5438
  - 油管绵阿羊_United States_vmess_5439
  - 油管绵阿羊_United States_vmess_5440
  - 油管绵阿羊_None_vmess_5441
  - 油管绵阿羊_Netherlands_vmess_5442
  - 油管绵阿羊_United States_vmess_5443
  - 油管绵阿羊_None_vmess_5444
  - 油管绵阿羊_South Africa_vmess_5445
  - 油管绵阿羊_Costa Rica_vmess_5446
  - 油管绵阿羊_United States_vmess_5447
  - 油管绵阿羊_United States_vmess_5448
  - 油管绵阿羊_United States_vmess_5449
  - 油管绵阿羊_Kenya_vmess_5450
  - 油管绵阿羊_United States_vmess_5451
  - 油管绵阿羊_United States_vmess_5452
  - 油管绵阿羊_None_vmess_5453
  - 油管绵阿羊_Spain_vmess_5454
  - 油管绵阿羊_Costa Rica_vmess_5455
  - 油管绵阿羊_United States_vmess_5456
  - 油管绵阿羊_Germany_vmess_5457
  - 油管绵阿羊_United States_vmess_5458
  - 油管绵阿羊_None_vmess_5459
  - 油管绵阿羊_Costa Rica_vmess_5460
  - 油管绵阿羊_None_vmess_5461
  - 油管绵阿羊_Paraguay_vmess_5462
  - 油管绵阿羊_Australia_vmess_5463
  - 油管绵阿羊_United States_vmess_5464
  - 油管绵阿羊_South Africa_vmess_5465
  - 油管绵阿羊_None_vmess_5466
  - 油管绵阿羊_United States_vmess_5467
  - 油管绵阿羊_United States_vmess_5468
  - 油管绵阿羊_Spain_vmess_5469
  - 油管绵阿羊_United States_vmess_5470
  - 油管绵阿羊_United States_vmess_5471
  - 油管绵阿羊_None_vmess_5472
  - 油管绵阿羊_None_vmess_5473
  - 油管绵阿羊_None_vmess_5474
  - 油管绵阿羊_Germany_vmess_5475
  - 油管绵阿羊_India_vmess_5476
  - 油管绵阿羊_Costa Rica_vmess_5477
  - 油管绵阿羊_None_vmess_5478
  - 油管绵阿羊_Germany_vmess_5479
  - 油管绵阿羊_Netherlands_vmess_5480
  - 油管绵阿羊_United States_vmess_5481
  - 油管绵阿羊_United States_vmess_5482
  - 油管绵阿羊_Italy_vmess_5483
  - 油管绵阿羊_Australia_vmess_5484
  - 油管绵阿羊_United States_vmess_5485
  - 油管绵阿羊_None_vmess_5486
  - 油管绵阿羊_None_vmess_5487
  - 油管绵阿羊_United States_vmess_5488
  - 油管绵阿羊_United States_vmess_5489
  - 油管绵阿羊_Costa Rica_vmess_5490
  - 油管绵阿羊_None_vmess_5491
  - 油管绵阿羊_None_vmess_5492
  - 油管绵阿羊_Costa Rica_vmess_5493
  - 油管绵阿羊_United States_vmess_5494
  - 油管绵阿羊_United States_vmess_5495
  - 油管绵阿羊_United States_vmess_5496
  - 油管绵阿羊_Netherlands_vmess_5497
  - 油管绵阿羊_Japan_vmess_5498
  - 油管绵阿羊_Costa Rica_vmess_5499
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
aHlzdGVyaWEyOi8vZG9uZ3RhaXdhbmcuY29tQDY0LjMxLjU1LjMwOjIwMDExP2luc2VjdXJlPTEmc25pPWJpbmcuY29tJm9iZnM9Jm9iZnMtcGFzc3dvcmQ9I1VuaXRlZCBTdGF0ZXNfaHkyXzAKdHVpYzovLzdiZGEwNmZkLWU0YWYtNDExNS04YWEzLWYwMjE4MzJjZmE3ODpkb25ndGFpd2FuZy5jb21AMTA5LjEwNC4xNTIuMTQ0OjQ0NDExP3NuaT0mY29uZ2VzdGlvbl9jb250cm9sPWJiciZ1ZHBfcmVsYXlfbW9kZT1uYXRpdmUmYWxwbj1oMyZhbGxvd19pbnNlY3VyZT0wI1VuaXRlZCBTdGF0ZXNfdHVpY18xCmh5c3RlcmlhOi8vMTA5LjEwNC4xNTIuMTAxOjMyMjAwP3BlZXI9YmluZy5jb20mYXV0aD0maW5zZWN1cmU9MSZ1cG1icHM9NTAmZG93bm1icHM9ODAmYWxwbj1oMyZtcG9ydD0zMjIwMCZvYmZzPSZwcm90b2NvbD11ZHAmZmFzdG9wZW49MSNVbml0ZWQgU3RhdGVzX2h5XzIKdHVpYzovLzdiZGEwNmZkLWU0YWYtNDExNS04YWEzLWYwMjE4MzJjZmE3ODpkb25ndGFpd2FuZy5jb21AMTA5LjEwNC4xNTIuMTAxOjIyMjg4P3NuaT0mY29uZ2VzdGlvbl9jb250cm9sPWJiciZ1ZHBfcmVsYXlfbW9kZT1uYXRpdmUmYWxwbj1oMyZhbGxvd19pbnNlY3VyZT0wI1VuaXRlZCBTdGF0ZXNfdHVpY18zCnZsZXNzOi8vOWNjMzk0NzctMGQ4NS00NDE5LTg0ZDQtZmI3ZmM3NzY2OGIzQDEwOS4xMDQuMTUyLjEwMToxMTExMT9zZWN1cml0eT1yZWFsaXR5JmFsbG93SW5zZWN1cmUwJmZsb3c9eHRscy1ycHJ4LXZpc2lvbiZ0eXBlPXRjcCZmcD1jaHJvbWUmcGJrPXlLWG1MVG1YQWktQkhCZzNKcEN6LU5XVW1WY0tsZm03aU1tVm9xN1lReDAmc2lkPTZiYTg1MTc5ZTMwZDRmYzImc25pPW0ubWVkaWEtYW1hem9uLmNvbSZzZXJ2aWNlTmFtZT0mcGF0aD0maG9zdD0jVW5pdGVkIFN0YXRlc192bGVzc180Cmh5c3RlcmlhOi8vd3d3Mi5kdGt1NDgueHl6OjIyMzM0P3BlZXI9JmF1dGg9ZG9uZ3RhaXdhbmcuY29tJmluc2VjdXJlPTEmdXBtYnBzPTUwJmRvd25tYnBzPTgwJmFscG49aDMmbXBvcnQ9MjIzMzQmb2Jmcz0mcHJvdG9jb2w9dWRwJmZhc3RvcGVuPTEjVGFpd2FuX2h5XzYKaHlzdGVyaWEyOi8vZG9uZ3RhaXdhbmcuY29tQDUxLjE1OC41NC40Njo0NDU1MD9pbnNlY3VyZT0xJnNuaT1iaW5nLmNvbSZvYmZzPSZvYmZzLXBhc3N3b3JkPSNGcmFuY2VfaHkyXzcKaHlzdGVyaWEyOi8vZDAxN2UzMTYtODJjYi00NDFjLThlZWEtN2I1ZTlkZTY0YTIwQDQ1LjE1MC4xNjUuODQ6ODg4MT9pbnNlY3VyZT0xJnNuaT0mb2Jmcz1zYWxhbWFuZGVyJm9iZnMtcGFzc3dvcmQ9ZDAxN2UzMTYtODJjYi00NDFjLThlZWEtN2I1ZTlkZTY0YTIwI1VuaXRlZCBTdGF0ZXNfaHkyXzgKaHlzdGVyaWE6Ly93d3cuZHRrdTUwLnh5ejoxODQ3MD9wZWVyPXd3dy5hbWF6b24uY24mYXV0aD0maW5zZWN1cmU9MSZ1cG1icHM9NTAmZG93bm1icHM9ODAmYWxwbj1oMyZtcG9ydD0xODQ3MCZvYmZzPSZwcm90b2NvbD11ZHAmZmFzdG9wZW49MSNUYWl3YW5faHlfOQphSFIwY0hNNkx5OWtiMjVuZEdGcGQyRnVaeTVqYjIwNlpHOXVaM1JoYVhkaGJtY3VZMjl0UUc1aGFYWmxNVGt1WTJaalpHNHpMbmg1ZWpvME5ETT0KYUhSMGNITTZMeTlrYjI1bmRHRnBkMkZ1Wnk1amIyMDZaRzl1WjNSaGFYZGhibWN1WTI5dFFIZDNkeTVrZEd0MU5UQXVlSGw2T2pRME13PT0KaHlzdGVyaWE6Ly81MS4xNTguNTQuNDY6NTUzOTY/cGVlcj15b3VrdS5jb20mYXV0aD1kb25ndGFpd2FuZy5jb20maW5zZWN1cmU9MSZ1cG1icHM9MTEmZG93bm1icHM9NTUmYWxwbj1oMyZvYmZzPSZwcm90b2NvbD11ZHAmZmFzdG9wZW49MSNGcmFuY2VfaHlzdGVyaWFfMApoeXN0ZXJpYTovLzE3My4yMzQuMjUuNTI6NDg5MTk/cGVlcj1iaW5nLmNvbSZhdXRoPWRvbmd0YWl3YW5nLmNvbSZpbnNlY3VyZT0xJnVwbWJwcz0xMSZkb3dubWJwcz01NSZhbHBuPWgzJm9iZnM9JnByb3RvY29sPXVkcCZmYXN0b3Blbj0xI1VuaXRlZCBTdGF0ZXNfaHlzdGVyaWFfMQpoeXN0ZXJpYTovL3d3dy5kdGt1NDAueHl6OjE4NDkwP3BlZXI9YmluZy5jb20mYXV0aD1kb25ndGFpd2FuZy5jb20maW5zZWN1cmU9MSZ1cG1icHM9MTEmZG93bm1icHM9NTUmYWxwbj1oMyZvYmZzPSZwcm90b2NvbD11ZHAmZmFzdG9wZW49MSNUYWl3YW5faHlzdGVyaWFfMgpoeXN0ZXJpYTovLzE2Ny4xNjAuOTEuMTE1OjQxMTg5P3BlZXI9d3d3LmFtYXpvbi5jbiZhdXRoPWJXQXdJcUlObzdYRG0xZlVsWFFHQmlmVklYb1lzMXlsZ1ZLcVdGS3pLMVh5REt1d05GJmluc2VjdXJlPTEmdXBtYnBzPTExJmRvd25tYnBzPTU1JmFscG49aDMmb2Jmcz0mcHJvdG9jb2w9dWRwJmZhc3RvcGVuPTEjVW5pdGVkIFN0YXRlc19oeXN0ZXJpYV8zCmh5c3RlcmlhMjovL2Rvbmd0YWl3YW5nLmNvbUA2Mi4yMTAuMTAzLjA6MjI0ODM/aW5zZWN1cmU9MSZzbmk9d3d3LmJpbmcuY29tI0ZyYW5jZV9oeXN0ZXJpYTJfMApoeXN0ZXJpYTI6Ly9kb25ndGFpd2FuZy5jb21ANjQuMTEwLjI1LjExOjMzMzM3P2luc2VjdXJlPTEmc25pPXd3dy5iaW5nLmNvbSNVbml0ZWQgU3RhdGVzX2h5c3RlcmlhMl8xCmh5c3RlcmlhMjovL2Rvbmd0YWl3YW5nLmNvbUA2Mi4yMTAuMTAzLjA6MjI0ODM/aW5zZWN1cmU9MSZzbmk9d3d3LmJpbmcuY29tI0ZyYW5jZV9oeXN0ZXJpYTJfMgpoeXN0ZXJpYTI6Ly9kb25ndGFpd2FuZy5jb21ANTEuMTU5Ljc3LjE5ODoyOTI3Nz9pbnNlY3VyZT0xJnNuaT13d3cuYmluZy5jb20jRnJhbmNlX2h5c3RlcmlhMl8zCnZsZXNzOi8vZTY1OTY2MWQtODQzOS00NmUwLWIxYWItZDc1Y2VhZjczNDA0QDYyLjIxMC4xMDEuMDoxODcwMD9zZWN1cml0eT1yZWFsaXR5JmFsbG93SW5zZWN1cmU9MCZmbG93PXh0bHMtcnByeC12aXNpb24mdHlwZT10Y3AmZnA9Y2hyb21lJnBiaz1QQlJjMnY5U1NYcEc0ampRUllOYS1rZ3M4dzlWNFUzTU5MdW5jZDJkMGh3JnNpZD02YmE4NTE3OWUzMGQ0ZmMyJnNuaT11cGRhdGUubWljcm9zb2Z0JnNlcnZpY2VOYW1lPSZwYXRoPSZob3N0PSNGcmFuY2Vfdmxlc3NfMgp2bGVzczovL2U2NTk2NjFkLTg0MzktNDZlMC1iMWFiLWQ3NWNlYWY3MzQwNEA2Mi4yMTAuMTAxLjA6MTg3MDA/c2VjdXJpdHk9cmVhbGl0eSZhbGxvd0luc2VjdXJlPTAmZmxvdz14dGxzLXJwcngtdmlzaW9uJnR5cGU9dGNwJmZwPWNocm9tZSZwYms9UEJSYzJ2OVNTWHBHNGpqUVJZTmEta2dzOHc5VjRVM01OTHVuY2QyZDBodyZzaWQ9NmJhODUxNzllMzBkNGZjMiZzbmk9dXBkYXRlLm1pY3Jvc29mdCZzZXJ2aWNlTmFtZT0mcGF0aD0maG9zdD0jRnJhbmNlX3ZsZXNzXzM=
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
        "🇺🇸 United States_hy_2",
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
        "🇺🇸 United States_hy_2",
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
        "🇺🇸 United States_hy_2",
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
      "tag": "🇺🇸 United States_hy_2",
      "type": "hysteria",
      "server": "109.104.152.101",
      "server_port": 32200,
      "up_mbps": 50,
      "down_mbps": 80,
      "auth_str": "",
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


