
---
title: VPN合集
date: 2024-03-06 14:27:56
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

> Last Update Time: 2024-03-06 14:27:56
---
# vless_node
```bash

None

```

# CloudFlare优质IP
```bash

电信141.101.120.144
电信172.64.192.97
电信172.64.135.219

联通172.67.78.221
联通162.159.134.96
联通162.159.134.96

移动172.67.40.230
移动172.67.219.229
移动172.67.214.138


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
140.82.113.25                 alive.github.com
140.82.113.6                  api.github.com
185.199.109.153               assets-cdn.github.com
185.199.111.133               avatars.githubusercontent.com
185.199.108.133               avatars0.githubusercontent.com
185.199.111.133               avatars1.githubusercontent.com
185.199.111.133               avatars2.githubusercontent.com
185.199.111.133               avatars3.githubusercontent.com
185.199.111.133               avatars4.githubusercontent.com
185.199.111.133               avatars5.githubusercontent.com
185.199.108.133               camo.githubusercontent.com
140.82.113.21                 central.github.com
185.199.111.133               cloud.githubusercontent.com
140.82.114.10                 codeload.github.com
140.82.114.22                 collector.github.com
185.199.111.133               desktop.githubusercontent.com
185.199.108.133               favicons.githubusercontent.com
140.82.112.3                  gist.github.com
52.216.109.59                 github-cloud.s3.amazonaws.com
3.5.20.16                     github-com.s3.amazonaws.com
54.231.161.153                github-production-release-asset-2e65be.s3.amazonaws.com
52.217.232.161                github-production-repository-file-5c1aeb.s3.amazonaws.com
52.216.38.233                 github-production-user-asset-6210df.s3.amazonaws.com
192.0.66.2                    github.blog
140.82.112.3                  github.com
140.82.114.17                 github.community
185.199.110.154               github.githubassets.com
151.101.129.194               github.global.ssl.fastly.net
185.199.109.153               github.io
185.199.111.133               github.map.fastly.net
185.199.109.153               githubstatus.com
140.82.114.25                 live.github.com
185.199.111.133               media.githubusercontent.com
185.199.111.133               objects.githubusercontent.com
13.107.42.16                  pipelines.actions.githubusercontent.com
185.199.111.133               raw.githubusercontent.com
185.199.111.133               user-images.githubusercontent.com
13.107.253.40                 vscode.dev
140.82.114.21                 education.github.com


# Update time: 2024-03-06T22:04:49+08:00
# Update url: https://raw.hellogithub.com/hosts
# Star me: https://github.com/521xueweihan/GitHub520
# GitHub520 Host End

```

该内容会自动定时更新， 数据更新时间：2024-03-06T22:04:49+08:00

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
- name: 油管绵阿羊_Canada_vmess_01
  type: vmess
  server: 23.227.38.23
  port: 8080
  cipher: auto
  uuid: 1a855748-ec07-408a-a3a2-7e1099a30616
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: uh-lawyers-instruments-kernel.trycloudflare.com
  network: ws
  ws-opts:
    path: 1a855748-ec07-408a-a3a2-7e1099a30616-vm
    headers:
      host: uh-lawyers-instruments-kernel.trycloudflare.com
- name: 油管绵阿羊_Canada_vmess_02
  type: vmess
  server: 23.227.38.44
  port: 8080
  cipher: auto
  uuid: 33eb512b-8f3a-459b-b823-3cccb6e82049
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: widescreen-instruction-breakdown-postage.trycloudflare.com
  network: ws
  ws-opts:
    path: 33eb512b-8f3a-459b-b823-3cccb6e82049-vm
    headers:
      host: widescreen-instruction-breakdown-postage.trycloudflare.com
- name: 油管绵阿羊_Canada_vmess_03
  type: vmess
  server: 23.227.38.22
  port: 8080
  cipher: auto
  uuid: e9d23b60-6e44-45a2-b24f-c8521c04c310
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: per-essex-patterns-bowling.trycloudflare.com
  network: ws
  ws-opts:
    path: e9d23b60-6e44-45a2-b24f-c8521c04c310-vm
    headers:
      host: per-essex-patterns-bowling.trycloudflare.com
- name: 油管绵阿羊_Canada_vmess_04
  type: vmess
  server: 23.227.38.11
  port: 8080
  cipher: auto
  uuid: 4a5ae806-ee72-473a-83b2-531808f454d5
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: championship-bidding-oxygen-brochure.trycloudflare.com
  network: ws
  ws-opts:
    path: 4a5ae806-ee72-473a-83b2-531808f454d5-vm
    headers:
      host: championship-bidding-oxygen-brochure.trycloudflare.com
- name: 油管绵阿羊_None_vmess_05
  type: vmess
  server: 162.159.153.11
  port: 8080
  cipher: auto
  uuid: 1a855748-ec07-408a-a3a2-7e1099a30616
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: uh-lawyers-instruments-kernel.trycloudflare.com
  network: ws
  ws-opts:
    path: 5f7934bf-a228-49a7-9572-5ce4377c34d5-vm
    headers:
      host: uh-lawyers-instruments-kernel.trycloudflare.com
- name: 油管绵阿羊_None_vmess_06
  type: vmess
  server: 162.159.134.23
  port: 8080
  cipher: auto
  uuid: 4a5ae806-ee72-473a-83b2-531808f454d5
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: championship-bidding-oxygen-brochure.trycloudflare.com
  network: ws
  ws-opts:
    path: 4a5ae806-ee72-473a-83b2-531808f454d5-vm
    headers:
      host: championship-bidding-oxygen-brochure.trycloudflare.com
- name: 油管绵阿羊_None_vmess_07
  type: vmess
  server: 162.159.137.31
  port: 8080
  cipher: auto
  uuid: e9d23b60-6e44-45a2-b24f-c8521c04c310
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: per-essex-patterns-bowling.trycloudflare.com
  network: ws
  ws-opts:
    path: 1a855748-ec07-408a-a3a2-7e1099a30616-vm
    headers:
      host: per-essex-patterns-bowling.trycloudflare.com
- name: 油管绵阿羊_None_vmess_08
  type: vmess
  server: 162.159.130.208
  port: 8080
  cipher: auto
  uuid: 33eb512b-8f3a-459b-b823-3cccb6e82049
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: widescreen-instruction-breakdown-postage.trycloudflare.com
  network: ws
  ws-opts:
    path: 33eb512b-8f3a-459b-b823-3cccb6e82049-vm
    headers:
      host: widescreen-instruction-breakdown-postage.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_09
  type: vmess
  server: yh1.dtku41.xyz
  port: 8080
  cipher: auto
  uuid: 1a855748-ec07-408a-a3a2-7e1099a30616
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: uh-lawyers-instruments-kernel.trycloudflare.com
  network: ws
  ws-opts:
    path: 1a855748-ec07-408a-a3a2-7e1099a30616-vm
    headers:
      host: uh-lawyers-instruments-kernel.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_010
  type: vmess
  server: yh1.dtku41.xyz
  port: 8080
  cipher: auto
  uuid: 4a5ae806-ee72-473a-83b2-531808f454d5
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: championship-bidding-oxygen-brochure.trycloudflare.com
  network: ws
  ws-opts:
    path: 4a5ae806-ee72-473a-83b2-531808f454d5-vm
    headers:
      host: championship-bidding-oxygen-brochure.trycloudflare.com
- name: 油管绵阿羊_None_vmess_011
  type: vmess
  server: yh1.dtku41.xyz
  port: 8080
  cipher: auto
  uuid: e9d23b60-6e44-45a2-b24f-c8521c04c310
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: per-essex-patterns-bowling.trycloudflare.com
  network: ws
  ws-opts:
    path: e9d23b60-6e44-45a2-b24f-c8521c04c310-vm
    headers:
      host: per-essex-patterns-bowling.trycloudflare.com
- name: 油管绵阿羊_None_vmess_012
  type: vmess
  server: yh1.dtku41.xyz
  port: 8080
  cipher: auto
  uuid: 33eb512b-8f3a-459b-b823-3cccb6e82049
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: widescreen-instruction-breakdown-postage.trycloudflare.com
  network: ws
  ws-opts:
    path: 33eb512b-8f3a-459b-b823-3cccb6e82049-vm
    headers:
      host: widescreen-instruction-breakdown-postage.trycloudflare.com
- name: 油管绵阿羊_None_vmess_013
  type: vmess
  server: yh2.dtku41.xyz
  port: 8080
  cipher: auto
  uuid: 1a855748-ec07-408a-a3a2-7e1099a30616
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: uh-lawyers-instruments-kernel.trycloudflare.com
  network: ws
  ws-opts:
    path: 1a855748-ec07-408a-a3a2-7e1099a30616-vm
    headers:
      host: uh-lawyers-instruments-kernel.trycloudflare.com
- name: 油管绵阿羊_None_vmess_014
  type: vmess
  server: yh2.dtku41.xyz
  port: 8080
  cipher: auto
  uuid: 4a5ae806-ee72-473a-83b2-531808f454d5
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: championship-bidding-oxygen-brochure.trycloudflare.com
  network: ws
  ws-opts:
    path: 4a5ae806-ee72-473a-83b2-531808f454d5-vm
    headers:
      host: championship-bidding-oxygen-brochure.trycloudflare.com
- name: 油管绵阿羊_None_vmess_015
  type: vmess
  server: yh2.dtku41.xyz
  port: 8080
  cipher: auto
  uuid: e9d23b60-6e44-45a2-b24f-c8521c04c310
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: per-essex-patterns-bowling.trycloudflare.com
  network: ws
  ws-opts:
    path: e9d23b60-6e44-45a2-b24f-c8521c04c310-vm
    headers:
      host: per-essex-patterns-bowling.trycloudflare.com
- name: 油管绵阿羊_None_vmess_016
  type: vmess
  server: yh2.dtku41.xyz
  port: 8080
  cipher: auto
  uuid: 33eb512b-8f3a-459b-b823-3cccb6e82049
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: widescreen-instruction-breakdown-postage.trycloudflare.com
  network: ws
  ws-opts:
    path: 33eb512b-8f3a-459b-b823-3cccb6e82049-vm
    headers:
      host: widescreen-instruction-breakdown-postage.trycloudflare.com
- name: 油管绵阿羊_None_vmess_11
  type: vmess
  server: fbi.gov
  port: 8080
  cipher: auto
  uuid: 0a5903c5-0ff3-4d79-9420-2a966873f787
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: pcs-referenced-camera-concerns.trycloudflare.com
  network: ws
  ws-opts:
    path: 0a5903c5-0ff3-4d79-9420-2a966873f787-vm
    headers:
      host: pcs-referenced-camera-concerns.trycloudflare.com
- name: 油管绵阿羊_None_vmess_12
  type: vmess
  server: fbi.gov
  port: 8080
  cipher: auto
  uuid: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: bibliographic-sword-sequence-advertisers.trycloudflare.com
  network: ws
  ws-opts:
    path: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876-vm
    headers:
      host: bibliographic-sword-sequence-advertisers.trycloudflare.com
- name: 油管绵阿羊_None_vmess_13
  type: vmess
  server: fbi.gov
  port: 8080
  cipher: auto
  uuid: b1e5c55d-e59b-42c4-aeb9-393e18525cca
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: nest-emily-healing-h.trycloudflare.com
  network: ws
  ws-opts:
    path: b1e5c55d-e59b-42c4-aeb9-393e18525cca-vm
    headers:
      host: nest-emily-healing-h.trycloudflare.com
- name: 油管绵阿羊_None_vmess_14
  type: vmess
  server: fbi.gov
  port: 8080
  cipher: auto
  uuid: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: larger-marketing-amounts-skin.trycloudflare.com
  network: ws
  ws-opts:
    path: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1-vm
    headers:
      host: larger-marketing-amounts-skin.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_21
  type: vmess
  server: yh1.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 0a5903c5-0ff3-4d79-9420-2a966873f787
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: pcs-referenced-camera-concerns.trycloudflare.com
  network: ws
  ws-opts:
    path: 0a5903c5-0ff3-4d79-9420-2a966873f787-vm
    headers:
      host: pcs-referenced-camera-concerns.trycloudflare.com
- name: 油管绵阿羊_None_vmess_22
  type: vmess
  server: yh1.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: bibliographic-sword-sequence-advertisers.trycloudflare.com
  network: ws
  ws-opts:
    path: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876-vm
    headers:
      host: bibliographic-sword-sequence-advertisers.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_23
  type: vmess
  server: yh1.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: b1e5c55d-e59b-42c4-aeb9-393e18525cca
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: nest-emily-healing-h.trycloudflare.com
  network: ws
  ws-opts:
    path: b1e5c55d-e59b-42c4-aeb9-393e18525cca-vm
    headers:
      host: nest-emily-healing-h.trycloudflare.com
- name: 油管绵阿羊_None_vmess_24
  type: vmess
  server: yh1.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: larger-marketing-amounts-skin.trycloudflare.com
  network: ws
  ws-opts:
    path: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1-vm
    headers:
      host: larger-marketing-amounts-skin.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_25
  type: vmess
  server: yh2.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: bibliographic-sword-sequence-advertisers.trycloudflare.com
  network: ws
  ws-opts:
    path: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876-vm
    headers:
      host: bibliographic-sword-sequence-advertisers.trycloudflare.com
- name: 油管绵阿羊_None_vmess_26
  type: vmess
  server: yh2.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: b1e5c55d-e59b-42c4-aeb9-393e18525cca
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: nest-emily-healing-h.trycloudflare.com
  network: ws
  ws-opts:
    path: b1e5c55d-e59b-42c4-aeb9-393e18525cca-vm
    headers:
      host: nest-emily-healing-h.trycloudflare.com
- name: 油管绵阿羊_None_vmess_27
  type: vmess
  server: yh2.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 0a5903c5-0ff3-4d79-9420-2a966873f787
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: pcs-referenced-camera-concerns.trycloudflare.com
  network: ws
  ws-opts:
    path: 0a5903c5-0ff3-4d79-9420-2a966873f787-vm
    headers:
      host: pcs-referenced-camera-concerns.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_28
  type: vmess
  server: yh3.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: larger-marketing-amounts-skin.trycloudflare.com
  network: ws
  ws-opts:
    path: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1-vm
    headers:
      host: larger-marketing-amounts-skin.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_29
  type: vmess
  server: yh3.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: bibliographic-sword-sequence-advertisers.trycloudflare.com
  network: ws
  ws-opts:
    path: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876-vm
    headers:
      host: bibliographic-sword-sequence-advertisers.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_210
  type: vmess
  server: yh3.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: b1e5c55d-e59b-42c4-aeb9-393e18525cca
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: nest-emily-healing-h.trycloudflare.com
  network: ws
  ws-opts:
    path: b1e5c55d-e59b-42c4-aeb9-393e18525cca-vm
    headers:
      host: nest-emily-healing-h.trycloudflare.com
- name: 油管绵阿羊_None_vmess_211
  type: vmess
  server: yh3.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 0a5903c5-0ff3-4d79-9420-2a966873f787
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: pcs-referenced-camera-concerns.trycloudflare.com
  network: ws
  ws-opts:
    path: 0a5903c5-0ff3-4d79-9420-2a966873f787-vm
    headers:
      host: pcs-referenced-camera-concerns.trycloudflare.com
- name: 油管绵阿羊_None_vmess_212
  type: vmess
  server: yh3.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: larger-marketing-amounts-skin.trycloudflare.com
  network: ws
  ws-opts:
    path: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1-vm
    headers:
      host: larger-marketing-amounts-skin.trycloudflare.com
- name: 油管绵阿羊_None_vmess_31
  type: vmess
  server: yh1.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 1a855748-ec07-408a-a3a2-7e1099a30616
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: uh-lawyers-instruments-kernel.trycloudflare.com
  network: ws
  ws-opts:
    path: 1a855748-ec07-408a-a3a2-7e1099a30616-vm
    headers:
      host: uh-lawyers-instruments-kernel.trycloudflare.com
- name: 油管绵阿羊_None_vmess_32
  type: vmess
  server: yh1.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: e9d23b60-6e44-45a2-b24f-c8521c04c310
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: per-essex-patterns-bowling.trycloudflare.com
  network: ws
  ws-opts:
    path: e9d23b60-6e44-45a2-b24f-c8521c04c310-vm
    headers:
      host: per-essex-patterns-bowling.trycloudflare.com
- name: 油管绵阿羊_None_vmess_33
  type: vmess
  server: yh1.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 4a5ae806-ee72-473a-83b2-531808f454d5
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: championship-bidding-oxygen-brochure.trycloudflare.com
  network: ws
  ws-opts:
    path: 4a5ae806-ee72-473a-83b2-531808f454d5-vm
    headers:
      host: championship-bidding-oxygen-brochure.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_34
  type: vmess
  server: yh1.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 33eb512b-8f3a-459b-b823-3cccb6e82049
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: widescreen-instruction-breakdown-postage.trycloudflare.com
  network: ws
  ws-opts:
    path: 33eb512b-8f3a-459b-b823-3cccb6e82049-vm
    headers:
      host: widescreen-instruction-breakdown-postage.trycloudflare.com
- name: 油管绵阿羊_Canada_vmess_41
  type: vmess
  server: 23.227.39.12
  port: 8080
  cipher: auto
  uuid: 1a855748-ec07-408a-a3a2-7e1099a30616
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: uh-lawyers-instruments-kernel.trycloudflare.com
  network: ws
  ws-opts:
    path: 1a855748-ec07-408a-a3a2-7e1099a30616-vm
    headers:
      host: uh-lawyers-instruments-kernel.trycloudflare.com
- name: 油管绵阿羊_Canada_vmess_42
  type: vmess
  server: 23.227.39.24
  port: 8080
  cipher: auto
  uuid: e9d23b60-6e44-45a2-b24f-c8521c04c310
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: per-essex-patterns-bowling.trycloudflare.com
  network: ws
  ws-opts:
    path: e9d23b60-6e44-45a2-b24f-c8521c04c310-vm
    headers:
      host: per-essex-patterns-bowling.trycloudflare.com
- name: 油管绵阿羊_Canada_vmess_43
  type: vmess
  server: 23.227.39.23
  port: 8080
  cipher: auto
  uuid: 4a5ae806-ee72-473a-83b2-531808f454d5
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: championship-bidding-oxygen-brochure.trycloudflare.com
  network: ws
  ws-opts:
    path: 4a5ae806-ee72-473a-83b2-531808f454d5-vm
    headers:
      host: championship-bidding-oxygen-brochure.trycloudflare.com
- name: 油管绵阿羊_Canada_vmess_44
  type: vmess
  server: 23.227.39.45
  port: 8080
  cipher: auto
  uuid: 33eb512b-8f3a-459b-b823-3cccb6e82049
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: widescreen-instruction-breakdown-postage.trycloudflare.com
  network: ws
  ws-opts:
    path: 33eb512b-8f3a-459b-b823-3cccb6e82049-vm
    headers:
      host: widescreen-instruction-breakdown-postage.trycloudflare.com
- name: 油管绵阿羊_None_vmess_51
  type: vmess
  server: fbi.gov
  port: 8080
  cipher: auto
  uuid: 0a5903c5-0ff3-4d79-9420-2a966873f787
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: pcs-referenced-camera-concerns.trycloudflare.com
  network: ws
  ws-opts:
    path: 0a5903c5-0ff3-4d79-9420-2a966873f787-vm
    headers:
      host: pcs-referenced-camera-concerns.trycloudflare.com
- name: 油管绵阿羊_None_vmess_52
  type: vmess
  server: fbi.gov
  port: 8080
  cipher: auto
  uuid: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: bibliographic-sword-sequence-advertisers.trycloudflare.com
  network: ws
  ws-opts:
    path: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876-vm
    headers:
      host: bibliographic-sword-sequence-advertisers.trycloudflare.com
- name: 油管绵阿羊_None_vmess_53
  type: vmess
  server: fbi.gov
  port: 8080
  cipher: auto
  uuid: b1e5c55d-e59b-42c4-aeb9-393e18525cca
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: nest-emily-healing-h.trycloudflare.com
  network: ws
  ws-opts:
    path: b1e5c55d-e59b-42c4-aeb9-393e18525cca-vm
    headers:
      host: nest-emily-healing-h.trycloudflare.com
- name: 油管绵阿羊_None_vmess_54
  type: vmess
  server: fbi.gov
  port: 8080
  cipher: auto
  uuid: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: larger-marketing-amounts-skin.trycloudflare.com
  network: ws
  ws-opts:
    path: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1-vm
    headers:
      host: larger-marketing-amounts-skin.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_55
  type: vmess
  server: yh1.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: bibliographic-sword-sequence-advertisers.trycloudflare.com
  network: ws
  ws-opts:
    path: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876-vm
    headers:
      host: bibliographic-sword-sequence-advertisers.trycloudflare.com
- name: 油管绵阿羊_None_vmess_56
  type: vmess
  server: yh1.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: b1e5c55d-e59b-42c4-aeb9-393e18525cca
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: nest-emily-healing-h.trycloudflare.com
  network: ws
  ws-opts:
    path: b1e5c55d-e59b-42c4-aeb9-393e18525cca-vm
    headers:
      host: nest-emily-healing-h.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_57
  type: vmess
  server: yh1.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 0a5903c5-0ff3-4d79-9420-2a966873f787
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: pcs-referenced-camera-concerns.trycloudflare.com
  network: ws
  ws-opts:
    path: 0a5903c5-0ff3-4d79-9420-2a966873f787-vm
    headers:
      host: pcs-referenced-camera-concerns.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_58
  type: vmess
  server: yh1.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: larger-marketing-amounts-skin.trycloudflare.com
  network: ws
  ws-opts:
    path: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1-vm
    headers:
      host: larger-marketing-amounts-skin.trycloudflare.com
- name: 油管绵阿羊_None_vmess_59
  type: vmess
  server: yh2.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: bibliographic-sword-sequence-advertisers.trycloudflare.com
  network: ws
  ws-opts:
    path: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876-vm
    headers:
      host: bibliographic-sword-sequence-advertisers.trycloudflare.com
- name: 油管绵阿羊_None_vmess_510
  type: vmess
  server: yh2.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: b1e5c55d-e59b-42c4-aeb9-393e18525cca
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: nest-emily-healing-h.trycloudflare.com
  network: ws
  ws-opts:
    path: b1e5c55d-e59b-42c4-aeb9-393e18525cca-vm
    headers:
      host: nest-emily-healing-h.trycloudflare.com
- name: 油管绵阿羊_None_vmess_511
  type: vmess
  server: yh2.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 0a5903c5-0ff3-4d79-9420-2a966873f787
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: pcs-referenced-camera-concerns.trycloudflare.com
  network: ws
  ws-opts:
    path: 0a5903c5-0ff3-4d79-9420-2a966873f787-vm
    headers:
      host: pcs-referenced-camera-concerns.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_512
  type: vmess
  server: yh3.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: larger-marketing-amounts-skin.trycloudflare.com
  network: ws
  ws-opts:
    path: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1-vm
    headers:
      host: larger-marketing-amounts-skin.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_513
  type: vmess
  server: yh3.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: bibliographic-sword-sequence-advertisers.trycloudflare.com
  network: ws
  ws-opts:
    path: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876-vm
    headers:
      host: bibliographic-sword-sequence-advertisers.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_514
  type: vmess
  server: yh3.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: b1e5c55d-e59b-42c4-aeb9-393e18525cca
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: nest-emily-healing-h.trycloudflare.com
  network: ws
  ws-opts:
    path: b1e5c55d-e59b-42c4-aeb9-393e18525cca-vm
    headers:
      host: nest-emily-healing-h.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_515
  type: vmess
  server: yh3.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 0a5903c5-0ff3-4d79-9420-2a966873f787
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: pcs-referenced-camera-concerns.trycloudflare.com
  network: ws
  ws-opts:
    path: 0a5903c5-0ff3-4d79-9420-2a966873f787-vm
    headers:
      host: pcs-referenced-camera-concerns.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_516
  type: vmess
  server: yh3.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: larger-marketing-amounts-skin.trycloudflare.com
  network: ws
  ws-opts:
    path: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1-vm
    headers:
      host: larger-marketing-amounts-skin.trycloudflare.com
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
  server: 51.159.77.153
  port: 33390
  password: dongtaiwang.com
  alpn:
  - h3
  sni: bing.com
  skip-cert-verify: true
  up: 11 Mbps
  down: 55 Mbps
- name: 油管绵阿羊_United States_ss_81
  type: ss
  server: 62.204.54.81
  port: 44550
  cipher: 2022-blake3-chacha20-poly1305
  password: 5IH4rBauUuOT4VpAshgMPMSQ3Tf+oJjDY/jEDbIel2Q=
  plugin: shadow-tls
  plugin-opts:
    host: nijigen-works.jp
    password: FHDLxKgzbcDCPmijble8uT1gddgBmOxA1XXeDgyqgGc=
    version: 3
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
  port: 53967
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
  - 油管绵阿羊_Canada_vmess_01
  - 油管绵阿羊_Canada_vmess_02
  - 油管绵阿羊_Canada_vmess_03
  - 油管绵阿羊_Canada_vmess_04
  - 油管绵阿羊_None_vmess_05
  - 油管绵阿羊_None_vmess_06
  - 油管绵阿羊_None_vmess_07
  - 油管绵阿羊_None_vmess_08
  - 油管绵阿羊_United States_vmess_09
  - 油管绵阿羊_United States_vmess_010
  - 油管绵阿羊_None_vmess_011
  - 油管绵阿羊_None_vmess_012
  - 油管绵阿羊_None_vmess_013
  - 油管绵阿羊_None_vmess_014
  - 油管绵阿羊_None_vmess_015
  - 油管绵阿羊_None_vmess_016
  - 油管绵阿羊_None_vmess_11
  - 油管绵阿羊_None_vmess_12
  - 油管绵阿羊_None_vmess_13
  - 油管绵阿羊_None_vmess_14
  - 油管绵阿羊_United States_vmess_21
  - 油管绵阿羊_None_vmess_22
  - 油管绵阿羊_United States_vmess_23
  - 油管绵阿羊_None_vmess_24
  - 油管绵阿羊_United States_vmess_25
  - 油管绵阿羊_None_vmess_26
  - 油管绵阿羊_None_vmess_27
  - 油管绵阿羊_United States_vmess_28
  - 油管绵阿羊_United States_vmess_29
  - 油管绵阿羊_United States_vmess_210
  - 油管绵阿羊_None_vmess_211
  - 油管绵阿羊_None_vmess_212
  - 油管绵阿羊_None_vmess_31
  - 油管绵阿羊_None_vmess_32
  - 油管绵阿羊_None_vmess_33
  - 油管绵阿羊_United States_vmess_34
  - 油管绵阿羊_Canada_vmess_41
  - 油管绵阿羊_Canada_vmess_42
  - 油管绵阿羊_Canada_vmess_43
  - 油管绵阿羊_Canada_vmess_44
  - 油管绵阿羊_None_vmess_51
  - 油管绵阿羊_None_vmess_52
  - 油管绵阿羊_None_vmess_53
  - 油管绵阿羊_None_vmess_54
  - 油管绵阿羊_United States_vmess_55
  - 油管绵阿羊_None_vmess_56
  - 油管绵阿羊_United States_vmess_57
  - 油管绵阿羊_United States_vmess_58
  - 油管绵阿羊_None_vmess_59
  - 油管绵阿羊_None_vmess_510
  - 油管绵阿羊_None_vmess_511
  - 油管绵阿羊_United States_vmess_512
  - 油管绵阿羊_United States_vmess_513
  - 油管绵阿羊_United States_vmess_514
  - 油管绵阿羊_United States_vmess_515
  - 油管绵阿羊_United States_vmess_516
  - 油管绵阿羊_Taiwan_hysteria_61
  - 油管绵阿羊_France_hysteria2_71
  - 油管绵阿羊_United States_ss_81
  - 油管绵阿羊_Taiwan_hysteria_91
  - 油管绵阿羊_France_hy_0
  - 油管绵阿羊_United States_hy_1
  - 油管绵阿羊_Taiwan_hy_2
  - 油管绵阿羊_United States_hy_3
  - 油管绵阿羊_France_hy2_0
  - 油管绵阿羊_United States_hy2_1
  - 油管绵阿羊_France_hy2_2
  - 油管绵阿羊_France_hy2_3
- name: 自动选择
  type: url-test
  url: http://www.gstatic.com/generate_204
  interval: 300
  tolerance: 50
  proxies:
  - 油管绵阿羊_Canada_vmess_01
  - 油管绵阿羊_Canada_vmess_02
  - 油管绵阿羊_Canada_vmess_03
  - 油管绵阿羊_Canada_vmess_04
  - 油管绵阿羊_None_vmess_05
  - 油管绵阿羊_None_vmess_06
  - 油管绵阿羊_None_vmess_07
  - 油管绵阿羊_None_vmess_08
  - 油管绵阿羊_United States_vmess_09
  - 油管绵阿羊_United States_vmess_010
  - 油管绵阿羊_None_vmess_011
  - 油管绵阿羊_None_vmess_012
  - 油管绵阿羊_None_vmess_013
  - 油管绵阿羊_None_vmess_014
  - 油管绵阿羊_None_vmess_015
  - 油管绵阿羊_None_vmess_016
  - 油管绵阿羊_None_vmess_11
  - 油管绵阿羊_None_vmess_12
  - 油管绵阿羊_None_vmess_13
  - 油管绵阿羊_None_vmess_14
  - 油管绵阿羊_United States_vmess_21
  - 油管绵阿羊_None_vmess_22
  - 油管绵阿羊_United States_vmess_23
  - 油管绵阿羊_None_vmess_24
  - 油管绵阿羊_United States_vmess_25
  - 油管绵阿羊_None_vmess_26
  - 油管绵阿羊_None_vmess_27
  - 油管绵阿羊_United States_vmess_28
  - 油管绵阿羊_United States_vmess_29
  - 油管绵阿羊_United States_vmess_210
  - 油管绵阿羊_None_vmess_211
  - 油管绵阿羊_None_vmess_212
  - 油管绵阿羊_None_vmess_31
  - 油管绵阿羊_None_vmess_32
  - 油管绵阿羊_None_vmess_33
  - 油管绵阿羊_United States_vmess_34
  - 油管绵阿羊_Canada_vmess_41
  - 油管绵阿羊_Canada_vmess_42
  - 油管绵阿羊_Canada_vmess_43
  - 油管绵阿羊_Canada_vmess_44
  - 油管绵阿羊_None_vmess_51
  - 油管绵阿羊_None_vmess_52
  - 油管绵阿羊_None_vmess_53
  - 油管绵阿羊_None_vmess_54
  - 油管绵阿羊_United States_vmess_55
  - 油管绵阿羊_None_vmess_56
  - 油管绵阿羊_United States_vmess_57
  - 油管绵阿羊_United States_vmess_58
  - 油管绵阿羊_None_vmess_59
  - 油管绵阿羊_None_vmess_510
  - 油管绵阿羊_None_vmess_511
  - 油管绵阿羊_United States_vmess_512
  - 油管绵阿羊_United States_vmess_513
  - 油管绵阿羊_United States_vmess_514
  - 油管绵阿羊_United States_vmess_515
  - 油管绵阿羊_United States_vmess_516
  - 油管绵阿羊_Taiwan_hysteria_61
  - 油管绵阿羊_France_hysteria2_71
  - 油管绵阿羊_United States_ss_81
  - 油管绵阿羊_Taiwan_hysteria_91
  - 油管绵阿羊_France_hy_0
  - 油管绵阿羊_United States_hy_1
  - 油管绵阿羊_Taiwan_hy_2
  - 油管绵阿羊_United States_hy_3
  - 油管绵阿羊_France_hy2_0
  - 油管绵阿羊_United States_hy2_1
  - 油管绵阿羊_France_hy2_2
  - 油管绵阿羊_France_hy2_3
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
- name: 油管绵阿羊_Canada_vmess_01
  type: vmess
  server: 23.227.38.23
  port: 8080
  cipher: auto
  uuid: 1a855748-ec07-408a-a3a2-7e1099a30616
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: uh-lawyers-instruments-kernel.trycloudflare.com
  network: ws
  ws-opts:
    path: 1a855748-ec07-408a-a3a2-7e1099a30616-vm
    headers:
      host: uh-lawyers-instruments-kernel.trycloudflare.com
- name: 油管绵阿羊_Canada_vmess_02
  type: vmess
  server: 23.227.38.44
  port: 8080
  cipher: auto
  uuid: 33eb512b-8f3a-459b-b823-3cccb6e82049
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: widescreen-instruction-breakdown-postage.trycloudflare.com
  network: ws
  ws-opts:
    path: 33eb512b-8f3a-459b-b823-3cccb6e82049-vm
    headers:
      host: widescreen-instruction-breakdown-postage.trycloudflare.com
- name: 油管绵阿羊_Canada_vmess_03
  type: vmess
  server: 23.227.38.22
  port: 8080
  cipher: auto
  uuid: e9d23b60-6e44-45a2-b24f-c8521c04c310
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: per-essex-patterns-bowling.trycloudflare.com
  network: ws
  ws-opts:
    path: e9d23b60-6e44-45a2-b24f-c8521c04c310-vm
    headers:
      host: per-essex-patterns-bowling.trycloudflare.com
- name: 油管绵阿羊_Canada_vmess_04
  type: vmess
  server: 23.227.38.11
  port: 8080
  cipher: auto
  uuid: 4a5ae806-ee72-473a-83b2-531808f454d5
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: championship-bidding-oxygen-brochure.trycloudflare.com
  network: ws
  ws-opts:
    path: 4a5ae806-ee72-473a-83b2-531808f454d5-vm
    headers:
      host: championship-bidding-oxygen-brochure.trycloudflare.com
- name: 油管绵阿羊_None_vmess_05
  type: vmess
  server: 162.159.153.11
  port: 8080
  cipher: auto
  uuid: 1a855748-ec07-408a-a3a2-7e1099a30616
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: uh-lawyers-instruments-kernel.trycloudflare.com
  network: ws
  ws-opts:
    path: 5f7934bf-a228-49a7-9572-5ce4377c34d5-vm
    headers:
      host: uh-lawyers-instruments-kernel.trycloudflare.com
- name: 油管绵阿羊_None_vmess_06
  type: vmess
  server: 162.159.134.23
  port: 8080
  cipher: auto
  uuid: 4a5ae806-ee72-473a-83b2-531808f454d5
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: championship-bidding-oxygen-brochure.trycloudflare.com
  network: ws
  ws-opts:
    path: 4a5ae806-ee72-473a-83b2-531808f454d5-vm
    headers:
      host: championship-bidding-oxygen-brochure.trycloudflare.com
- name: 油管绵阿羊_None_vmess_07
  type: vmess
  server: 162.159.137.31
  port: 8080
  cipher: auto
  uuid: e9d23b60-6e44-45a2-b24f-c8521c04c310
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: per-essex-patterns-bowling.trycloudflare.com
  network: ws
  ws-opts:
    path: 1a855748-ec07-408a-a3a2-7e1099a30616-vm
    headers:
      host: per-essex-patterns-bowling.trycloudflare.com
- name: 油管绵阿羊_None_vmess_08
  type: vmess
  server: 162.159.130.208
  port: 8080
  cipher: auto
  uuid: 33eb512b-8f3a-459b-b823-3cccb6e82049
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: widescreen-instruction-breakdown-postage.trycloudflare.com
  network: ws
  ws-opts:
    path: 33eb512b-8f3a-459b-b823-3cccb6e82049-vm
    headers:
      host: widescreen-instruction-breakdown-postage.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_09
  type: vmess
  server: yh1.dtku41.xyz
  port: 8080
  cipher: auto
  uuid: 1a855748-ec07-408a-a3a2-7e1099a30616
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: uh-lawyers-instruments-kernel.trycloudflare.com
  network: ws
  ws-opts:
    path: 1a855748-ec07-408a-a3a2-7e1099a30616-vm
    headers:
      host: uh-lawyers-instruments-kernel.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_010
  type: vmess
  server: yh1.dtku41.xyz
  port: 8080
  cipher: auto
  uuid: 4a5ae806-ee72-473a-83b2-531808f454d5
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: championship-bidding-oxygen-brochure.trycloudflare.com
  network: ws
  ws-opts:
    path: 4a5ae806-ee72-473a-83b2-531808f454d5-vm
    headers:
      host: championship-bidding-oxygen-brochure.trycloudflare.com
- name: 油管绵阿羊_None_vmess_011
  type: vmess
  server: yh1.dtku41.xyz
  port: 8080
  cipher: auto
  uuid: e9d23b60-6e44-45a2-b24f-c8521c04c310
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: per-essex-patterns-bowling.trycloudflare.com
  network: ws
  ws-opts:
    path: e9d23b60-6e44-45a2-b24f-c8521c04c310-vm
    headers:
      host: per-essex-patterns-bowling.trycloudflare.com
- name: 油管绵阿羊_None_vmess_012
  type: vmess
  server: yh1.dtku41.xyz
  port: 8080
  cipher: auto
  uuid: 33eb512b-8f3a-459b-b823-3cccb6e82049
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: widescreen-instruction-breakdown-postage.trycloudflare.com
  network: ws
  ws-opts:
    path: 33eb512b-8f3a-459b-b823-3cccb6e82049-vm
    headers:
      host: widescreen-instruction-breakdown-postage.trycloudflare.com
- name: 油管绵阿羊_None_vmess_013
  type: vmess
  server: yh2.dtku41.xyz
  port: 8080
  cipher: auto
  uuid: 1a855748-ec07-408a-a3a2-7e1099a30616
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: uh-lawyers-instruments-kernel.trycloudflare.com
  network: ws
  ws-opts:
    path: 1a855748-ec07-408a-a3a2-7e1099a30616-vm
    headers:
      host: uh-lawyers-instruments-kernel.trycloudflare.com
- name: 油管绵阿羊_None_vmess_014
  type: vmess
  server: yh2.dtku41.xyz
  port: 8080
  cipher: auto
  uuid: 4a5ae806-ee72-473a-83b2-531808f454d5
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: championship-bidding-oxygen-brochure.trycloudflare.com
  network: ws
  ws-opts:
    path: 4a5ae806-ee72-473a-83b2-531808f454d5-vm
    headers:
      host: championship-bidding-oxygen-brochure.trycloudflare.com
- name: 油管绵阿羊_None_vmess_015
  type: vmess
  server: yh2.dtku41.xyz
  port: 8080
  cipher: auto
  uuid: e9d23b60-6e44-45a2-b24f-c8521c04c310
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: per-essex-patterns-bowling.trycloudflare.com
  network: ws
  ws-opts:
    path: e9d23b60-6e44-45a2-b24f-c8521c04c310-vm
    headers:
      host: per-essex-patterns-bowling.trycloudflare.com
- name: 油管绵阿羊_None_vmess_016
  type: vmess
  server: yh2.dtku41.xyz
  port: 8080
  cipher: auto
  uuid: 33eb512b-8f3a-459b-b823-3cccb6e82049
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: widescreen-instruction-breakdown-postage.trycloudflare.com
  network: ws
  ws-opts:
    path: 33eb512b-8f3a-459b-b823-3cccb6e82049-vm
    headers:
      host: widescreen-instruction-breakdown-postage.trycloudflare.com
- name: 油管绵阿羊_None_vmess_11
  type: vmess
  server: fbi.gov
  port: 8080
  cipher: auto
  uuid: 0a5903c5-0ff3-4d79-9420-2a966873f787
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: pcs-referenced-camera-concerns.trycloudflare.com
  network: ws
  ws-opts:
    path: 0a5903c5-0ff3-4d79-9420-2a966873f787-vm
    headers:
      host: pcs-referenced-camera-concerns.trycloudflare.com
- name: 油管绵阿羊_None_vmess_12
  type: vmess
  server: fbi.gov
  port: 8080
  cipher: auto
  uuid: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: bibliographic-sword-sequence-advertisers.trycloudflare.com
  network: ws
  ws-opts:
    path: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876-vm
    headers:
      host: bibliographic-sword-sequence-advertisers.trycloudflare.com
- name: 油管绵阿羊_None_vmess_13
  type: vmess
  server: fbi.gov
  port: 8080
  cipher: auto
  uuid: b1e5c55d-e59b-42c4-aeb9-393e18525cca
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: nest-emily-healing-h.trycloudflare.com
  network: ws
  ws-opts:
    path: b1e5c55d-e59b-42c4-aeb9-393e18525cca-vm
    headers:
      host: nest-emily-healing-h.trycloudflare.com
- name: 油管绵阿羊_None_vmess_14
  type: vmess
  server: fbi.gov
  port: 8080
  cipher: auto
  uuid: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: larger-marketing-amounts-skin.trycloudflare.com
  network: ws
  ws-opts:
    path: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1-vm
    headers:
      host: larger-marketing-amounts-skin.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_21
  type: vmess
  server: yh1.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 0a5903c5-0ff3-4d79-9420-2a966873f787
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: pcs-referenced-camera-concerns.trycloudflare.com
  network: ws
  ws-opts:
    path: 0a5903c5-0ff3-4d79-9420-2a966873f787-vm
    headers:
      host: pcs-referenced-camera-concerns.trycloudflare.com
- name: 油管绵阿羊_None_vmess_22
  type: vmess
  server: yh1.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: bibliographic-sword-sequence-advertisers.trycloudflare.com
  network: ws
  ws-opts:
    path: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876-vm
    headers:
      host: bibliographic-sword-sequence-advertisers.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_23
  type: vmess
  server: yh1.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: b1e5c55d-e59b-42c4-aeb9-393e18525cca
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: nest-emily-healing-h.trycloudflare.com
  network: ws
  ws-opts:
    path: b1e5c55d-e59b-42c4-aeb9-393e18525cca-vm
    headers:
      host: nest-emily-healing-h.trycloudflare.com
- name: 油管绵阿羊_None_vmess_24
  type: vmess
  server: yh1.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: larger-marketing-amounts-skin.trycloudflare.com
  network: ws
  ws-opts:
    path: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1-vm
    headers:
      host: larger-marketing-amounts-skin.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_25
  type: vmess
  server: yh2.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: bibliographic-sword-sequence-advertisers.trycloudflare.com
  network: ws
  ws-opts:
    path: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876-vm
    headers:
      host: bibliographic-sword-sequence-advertisers.trycloudflare.com
- name: 油管绵阿羊_None_vmess_26
  type: vmess
  server: yh2.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: b1e5c55d-e59b-42c4-aeb9-393e18525cca
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: nest-emily-healing-h.trycloudflare.com
  network: ws
  ws-opts:
    path: b1e5c55d-e59b-42c4-aeb9-393e18525cca-vm
    headers:
      host: nest-emily-healing-h.trycloudflare.com
- name: 油管绵阿羊_None_vmess_27
  type: vmess
  server: yh2.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 0a5903c5-0ff3-4d79-9420-2a966873f787
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: pcs-referenced-camera-concerns.trycloudflare.com
  network: ws
  ws-opts:
    path: 0a5903c5-0ff3-4d79-9420-2a966873f787-vm
    headers:
      host: pcs-referenced-camera-concerns.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_28
  type: vmess
  server: yh3.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: larger-marketing-amounts-skin.trycloudflare.com
  network: ws
  ws-opts:
    path: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1-vm
    headers:
      host: larger-marketing-amounts-skin.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_29
  type: vmess
  server: yh3.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: bibliographic-sword-sequence-advertisers.trycloudflare.com
  network: ws
  ws-opts:
    path: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876-vm
    headers:
      host: bibliographic-sword-sequence-advertisers.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_210
  type: vmess
  server: yh3.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: b1e5c55d-e59b-42c4-aeb9-393e18525cca
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: nest-emily-healing-h.trycloudflare.com
  network: ws
  ws-opts:
    path: b1e5c55d-e59b-42c4-aeb9-393e18525cca-vm
    headers:
      host: nest-emily-healing-h.trycloudflare.com
- name: 油管绵阿羊_None_vmess_211
  type: vmess
  server: yh3.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 0a5903c5-0ff3-4d79-9420-2a966873f787
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: pcs-referenced-camera-concerns.trycloudflare.com
  network: ws
  ws-opts:
    path: 0a5903c5-0ff3-4d79-9420-2a966873f787-vm
    headers:
      host: pcs-referenced-camera-concerns.trycloudflare.com
- name: 油管绵阿羊_None_vmess_212
  type: vmess
  server: yh3.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: larger-marketing-amounts-skin.trycloudflare.com
  network: ws
  ws-opts:
    path: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1-vm
    headers:
      host: larger-marketing-amounts-skin.trycloudflare.com
- name: 油管绵阿羊_None_vmess_31
  type: vmess
  server: yh1.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 1a855748-ec07-408a-a3a2-7e1099a30616
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: uh-lawyers-instruments-kernel.trycloudflare.com
  network: ws
  ws-opts:
    path: 1a855748-ec07-408a-a3a2-7e1099a30616-vm
    headers:
      host: uh-lawyers-instruments-kernel.trycloudflare.com
- name: 油管绵阿羊_None_vmess_32
  type: vmess
  server: yh1.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: e9d23b60-6e44-45a2-b24f-c8521c04c310
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: per-essex-patterns-bowling.trycloudflare.com
  network: ws
  ws-opts:
    path: e9d23b60-6e44-45a2-b24f-c8521c04c310-vm
    headers:
      host: per-essex-patterns-bowling.trycloudflare.com
- name: 油管绵阿羊_None_vmess_33
  type: vmess
  server: yh1.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 4a5ae806-ee72-473a-83b2-531808f454d5
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: championship-bidding-oxygen-brochure.trycloudflare.com
  network: ws
  ws-opts:
    path: 4a5ae806-ee72-473a-83b2-531808f454d5-vm
    headers:
      host: championship-bidding-oxygen-brochure.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_34
  type: vmess
  server: yh1.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 33eb512b-8f3a-459b-b823-3cccb6e82049
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: widescreen-instruction-breakdown-postage.trycloudflare.com
  network: ws
  ws-opts:
    path: 33eb512b-8f3a-459b-b823-3cccb6e82049-vm
    headers:
      host: widescreen-instruction-breakdown-postage.trycloudflare.com
- name: 油管绵阿羊_Canada_vmess_41
  type: vmess
  server: 23.227.39.12
  port: 8080
  cipher: auto
  uuid: 1a855748-ec07-408a-a3a2-7e1099a30616
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: uh-lawyers-instruments-kernel.trycloudflare.com
  network: ws
  ws-opts:
    path: 1a855748-ec07-408a-a3a2-7e1099a30616-vm
    headers:
      host: uh-lawyers-instruments-kernel.trycloudflare.com
- name: 油管绵阿羊_Canada_vmess_42
  type: vmess
  server: 23.227.39.24
  port: 8080
  cipher: auto
  uuid: e9d23b60-6e44-45a2-b24f-c8521c04c310
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: per-essex-patterns-bowling.trycloudflare.com
  network: ws
  ws-opts:
    path: e9d23b60-6e44-45a2-b24f-c8521c04c310-vm
    headers:
      host: per-essex-patterns-bowling.trycloudflare.com
- name: 油管绵阿羊_Canada_vmess_43
  type: vmess
  server: 23.227.39.23
  port: 8080
  cipher: auto
  uuid: 4a5ae806-ee72-473a-83b2-531808f454d5
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: championship-bidding-oxygen-brochure.trycloudflare.com
  network: ws
  ws-opts:
    path: 4a5ae806-ee72-473a-83b2-531808f454d5-vm
    headers:
      host: championship-bidding-oxygen-brochure.trycloudflare.com
- name: 油管绵阿羊_Canada_vmess_44
  type: vmess
  server: 23.227.39.45
  port: 8080
  cipher: auto
  uuid: 33eb512b-8f3a-459b-b823-3cccb6e82049
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: widescreen-instruction-breakdown-postage.trycloudflare.com
  network: ws
  ws-opts:
    path: 33eb512b-8f3a-459b-b823-3cccb6e82049-vm
    headers:
      host: widescreen-instruction-breakdown-postage.trycloudflare.com
- name: 油管绵阿羊_None_vmess_51
  type: vmess
  server: fbi.gov
  port: 8080
  cipher: auto
  uuid: 0a5903c5-0ff3-4d79-9420-2a966873f787
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: pcs-referenced-camera-concerns.trycloudflare.com
  network: ws
  ws-opts:
    path: 0a5903c5-0ff3-4d79-9420-2a966873f787-vm
    headers:
      host: pcs-referenced-camera-concerns.trycloudflare.com
- name: 油管绵阿羊_None_vmess_52
  type: vmess
  server: fbi.gov
  port: 8080
  cipher: auto
  uuid: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: bibliographic-sword-sequence-advertisers.trycloudflare.com
  network: ws
  ws-opts:
    path: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876-vm
    headers:
      host: bibliographic-sword-sequence-advertisers.trycloudflare.com
- name: 油管绵阿羊_None_vmess_53
  type: vmess
  server: fbi.gov
  port: 8080
  cipher: auto
  uuid: b1e5c55d-e59b-42c4-aeb9-393e18525cca
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: nest-emily-healing-h.trycloudflare.com
  network: ws
  ws-opts:
    path: b1e5c55d-e59b-42c4-aeb9-393e18525cca-vm
    headers:
      host: nest-emily-healing-h.trycloudflare.com
- name: 油管绵阿羊_None_vmess_54
  type: vmess
  server: fbi.gov
  port: 8080
  cipher: auto
  uuid: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: larger-marketing-amounts-skin.trycloudflare.com
  network: ws
  ws-opts:
    path: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1-vm
    headers:
      host: larger-marketing-amounts-skin.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_55
  type: vmess
  server: yh1.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: bibliographic-sword-sequence-advertisers.trycloudflare.com
  network: ws
  ws-opts:
    path: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876-vm
    headers:
      host: bibliographic-sword-sequence-advertisers.trycloudflare.com
- name: 油管绵阿羊_None_vmess_56
  type: vmess
  server: yh1.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: b1e5c55d-e59b-42c4-aeb9-393e18525cca
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: nest-emily-healing-h.trycloudflare.com
  network: ws
  ws-opts:
    path: b1e5c55d-e59b-42c4-aeb9-393e18525cca-vm
    headers:
      host: nest-emily-healing-h.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_57
  type: vmess
  server: yh1.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 0a5903c5-0ff3-4d79-9420-2a966873f787
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: pcs-referenced-camera-concerns.trycloudflare.com
  network: ws
  ws-opts:
    path: 0a5903c5-0ff3-4d79-9420-2a966873f787-vm
    headers:
      host: pcs-referenced-camera-concerns.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_58
  type: vmess
  server: yh1.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: larger-marketing-amounts-skin.trycloudflare.com
  network: ws
  ws-opts:
    path: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1-vm
    headers:
      host: larger-marketing-amounts-skin.trycloudflare.com
- name: 油管绵阿羊_None_vmess_59
  type: vmess
  server: yh2.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: bibliographic-sword-sequence-advertisers.trycloudflare.com
  network: ws
  ws-opts:
    path: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876-vm
    headers:
      host: bibliographic-sword-sequence-advertisers.trycloudflare.com
- name: 油管绵阿羊_None_vmess_510
  type: vmess
  server: yh2.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: b1e5c55d-e59b-42c4-aeb9-393e18525cca
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: nest-emily-healing-h.trycloudflare.com
  network: ws
  ws-opts:
    path: b1e5c55d-e59b-42c4-aeb9-393e18525cca-vm
    headers:
      host: nest-emily-healing-h.trycloudflare.com
- name: 油管绵阿羊_None_vmess_511
  type: vmess
  server: yh2.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 0a5903c5-0ff3-4d79-9420-2a966873f787
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: pcs-referenced-camera-concerns.trycloudflare.com
  network: ws
  ws-opts:
    path: 0a5903c5-0ff3-4d79-9420-2a966873f787-vm
    headers:
      host: pcs-referenced-camera-concerns.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_512
  type: vmess
  server: yh3.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: larger-marketing-amounts-skin.trycloudflare.com
  network: ws
  ws-opts:
    path: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1-vm
    headers:
      host: larger-marketing-amounts-skin.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_513
  type: vmess
  server: yh3.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: bibliographic-sword-sequence-advertisers.trycloudflare.com
  network: ws
  ws-opts:
    path: 6f7e94e7-4a60-4aa4-9369-4f44ec2ae876-vm
    headers:
      host: bibliographic-sword-sequence-advertisers.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_514
  type: vmess
  server: yh3.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: b1e5c55d-e59b-42c4-aeb9-393e18525cca
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: nest-emily-healing-h.trycloudflare.com
  network: ws
  ws-opts:
    path: b1e5c55d-e59b-42c4-aeb9-393e18525cca-vm
    headers:
      host: nest-emily-healing-h.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_515
  type: vmess
  server: yh3.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 0a5903c5-0ff3-4d79-9420-2a966873f787
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: pcs-referenced-camera-concerns.trycloudflare.com
  network: ws
  ws-opts:
    path: 0a5903c5-0ff3-4d79-9420-2a966873f787-vm
    headers:
      host: pcs-referenced-camera-concerns.trycloudflare.com
- name: 油管绵阿羊_United States_vmess_516
  type: vmess
  server: yh3.freeh1.xyz
  port: 8080
  cipher: auto
  uuid: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1
  alterId: 0
  tls: false
  skip-cert-verify: true
  servername: larger-marketing-amounts-skin.trycloudflare.com
  network: ws
  ws-opts:
    path: 6d34f7f8-eb93-44ea-b5df-4f2f203524a1-vm
    headers:
      host: larger-marketing-amounts-skin.trycloudflare.com
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
  server: 51.159.77.153
  port: 33390
  password: dongtaiwang.com
  alpn:
  - h3
  sni: bing.com
  skip-cert-verify: true
  up: 11 Mbps
  down: 55 Mbps
- name: 油管绵阿羊_United States_ss_81
  type: ss
  server: 62.204.54.81
  port: 44550
  cipher: 2022-blake3-chacha20-poly1305
  password: 5IH4rBauUuOT4VpAshgMPMSQ3Tf+oJjDY/jEDbIel2Q=
  plugin: shadow-tls
  plugin-opts:
    host: nijigen-works.jp
    password: FHDLxKgzbcDCPmijble8uT1gddgBmOxA1XXeDgyqgGc=
    version: 3
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
  port: 53967
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
  - 油管绵阿羊_Canada_vmess_01
  - 油管绵阿羊_Canada_vmess_02
  - 油管绵阿羊_Canada_vmess_03
  - 油管绵阿羊_Canada_vmess_04
  - 油管绵阿羊_None_vmess_05
  - 油管绵阿羊_None_vmess_06
  - 油管绵阿羊_None_vmess_07
  - 油管绵阿羊_None_vmess_08
  - 油管绵阿羊_United States_vmess_09
  - 油管绵阿羊_United States_vmess_010
  - 油管绵阿羊_None_vmess_011
  - 油管绵阿羊_None_vmess_012
  - 油管绵阿羊_None_vmess_013
  - 油管绵阿羊_None_vmess_014
  - 油管绵阿羊_None_vmess_015
  - 油管绵阿羊_None_vmess_016
  - 油管绵阿羊_None_vmess_11
  - 油管绵阿羊_None_vmess_12
  - 油管绵阿羊_None_vmess_13
  - 油管绵阿羊_None_vmess_14
  - 油管绵阿羊_United States_vmess_21
  - 油管绵阿羊_None_vmess_22
  - 油管绵阿羊_United States_vmess_23
  - 油管绵阿羊_None_vmess_24
  - 油管绵阿羊_United States_vmess_25
  - 油管绵阿羊_None_vmess_26
  - 油管绵阿羊_None_vmess_27
  - 油管绵阿羊_United States_vmess_28
  - 油管绵阿羊_United States_vmess_29
  - 油管绵阿羊_United States_vmess_210
  - 油管绵阿羊_None_vmess_211
  - 油管绵阿羊_None_vmess_212
  - 油管绵阿羊_None_vmess_31
  - 油管绵阿羊_None_vmess_32
  - 油管绵阿羊_None_vmess_33
  - 油管绵阿羊_United States_vmess_34
  - 油管绵阿羊_Canada_vmess_41
  - 油管绵阿羊_Canada_vmess_42
  - 油管绵阿羊_Canada_vmess_43
  - 油管绵阿羊_Canada_vmess_44
  - 油管绵阿羊_None_vmess_51
  - 油管绵阿羊_None_vmess_52
  - 油管绵阿羊_None_vmess_53
  - 油管绵阿羊_None_vmess_54
  - 油管绵阿羊_United States_vmess_55
  - 油管绵阿羊_None_vmess_56
  - 油管绵阿羊_United States_vmess_57
  - 油管绵阿羊_United States_vmess_58
  - 油管绵阿羊_None_vmess_59
  - 油管绵阿羊_None_vmess_510
  - 油管绵阿羊_None_vmess_511
  - 油管绵阿羊_United States_vmess_512
  - 油管绵阿羊_United States_vmess_513
  - 油管绵阿羊_United States_vmess_514
  - 油管绵阿羊_United States_vmess_515
  - 油管绵阿羊_United States_vmess_516
  - 油管绵阿羊_Taiwan_hysteria_61
  - 油管绵阿羊_France_hysteria2_71
  - 油管绵阿羊_United States_ss_81
  - 油管绵阿羊_Taiwan_hysteria_91
  - 油管绵阿羊_France_hy_0
  - 油管绵阿羊_United States_hy_1
  - 油管绵阿羊_Taiwan_hy_2
  - 油管绵阿羊_United States_hy_3
  - 油管绵阿羊_France_hy2_0
  - 油管绵阿羊_United States_hy2_1
  - 油管绵阿羊_France_hy2_2
  - 油管绵阿羊_France_hy2_3
- name: 手动选择
  type: select
  proxies:
  - 油管绵阿羊_Canada_vmess_01
  - 油管绵阿羊_Canada_vmess_02
  - 油管绵阿羊_Canada_vmess_03
  - 油管绵阿羊_Canada_vmess_04
  - 油管绵阿羊_None_vmess_05
  - 油管绵阿羊_None_vmess_06
  - 油管绵阿羊_None_vmess_07
  - 油管绵阿羊_None_vmess_08
  - 油管绵阿羊_United States_vmess_09
  - 油管绵阿羊_United States_vmess_010
  - 油管绵阿羊_None_vmess_011
  - 油管绵阿羊_None_vmess_012
  - 油管绵阿羊_None_vmess_013
  - 油管绵阿羊_None_vmess_014
  - 油管绵阿羊_None_vmess_015
  - 油管绵阿羊_None_vmess_016
  - 油管绵阿羊_None_vmess_11
  - 油管绵阿羊_None_vmess_12
  - 油管绵阿羊_None_vmess_13
  - 油管绵阿羊_None_vmess_14
  - 油管绵阿羊_United States_vmess_21
  - 油管绵阿羊_None_vmess_22
  - 油管绵阿羊_United States_vmess_23
  - 油管绵阿羊_None_vmess_24
  - 油管绵阿羊_United States_vmess_25
  - 油管绵阿羊_None_vmess_26
  - 油管绵阿羊_None_vmess_27
  - 油管绵阿羊_United States_vmess_28
  - 油管绵阿羊_United States_vmess_29
  - 油管绵阿羊_United States_vmess_210
  - 油管绵阿羊_None_vmess_211
  - 油管绵阿羊_None_vmess_212
  - 油管绵阿羊_None_vmess_31
  - 油管绵阿羊_None_vmess_32
  - 油管绵阿羊_None_vmess_33
  - 油管绵阿羊_United States_vmess_34
  - 油管绵阿羊_Canada_vmess_41
  - 油管绵阿羊_Canada_vmess_42
  - 油管绵阿羊_Canada_vmess_43
  - 油管绵阿羊_Canada_vmess_44
  - 油管绵阿羊_None_vmess_51
  - 油管绵阿羊_None_vmess_52
  - 油管绵阿羊_None_vmess_53
  - 油管绵阿羊_None_vmess_54
  - 油管绵阿羊_United States_vmess_55
  - 油管绵阿羊_None_vmess_56
  - 油管绵阿羊_United States_vmess_57
  - 油管绵阿羊_United States_vmess_58
  - 油管绵阿羊_None_vmess_59
  - 油管绵阿羊_None_vmess_510
  - 油管绵阿羊_None_vmess_511
  - 油管绵阿羊_United States_vmess_512
  - 油管绵阿羊_United States_vmess_513
  - 油管绵阿羊_United States_vmess_514
  - 油管绵阿羊_United States_vmess_515
  - 油管绵阿羊_United States_vmess_516
  - 油管绵阿羊_Taiwan_hysteria_61
  - 油管绵阿羊_France_hysteria2_71
  - 油管绵阿羊_United States_ss_81
  - 油管绵阿羊_Taiwan_hysteria_91
  - 油管绵阿羊_France_hy_0
  - 油管绵阿羊_United States_hy_1
  - 油管绵阿羊_Taiwan_hy_2
  - 油管绵阿羊_United States_hy_3
  - 油管绵阿羊_France_hy2_0
  - 油管绵阿羊_United States_hy2_1
  - 油管绵阿羊_France_hy2_2
  - 油管绵阿羊_France_hy2_3
- name: 负载均衡
  type: load-balance
  proxies:
  - 油管绵阿羊_Canada_vmess_01
  - 油管绵阿羊_Canada_vmess_02
  - 油管绵阿羊_Canada_vmess_03
  - 油管绵阿羊_Canada_vmess_04
  - 油管绵阿羊_None_vmess_05
  - 油管绵阿羊_None_vmess_06
  - 油管绵阿羊_None_vmess_07
  - 油管绵阿羊_None_vmess_08
  - 油管绵阿羊_United States_vmess_09
  - 油管绵阿羊_United States_vmess_010
  - 油管绵阿羊_None_vmess_011
  - 油管绵阿羊_None_vmess_012
  - 油管绵阿羊_None_vmess_013
  - 油管绵阿羊_None_vmess_014
  - 油管绵阿羊_None_vmess_015
  - 油管绵阿羊_None_vmess_016
  - 油管绵阿羊_None_vmess_11
  - 油管绵阿羊_None_vmess_12
  - 油管绵阿羊_None_vmess_13
  - 油管绵阿羊_None_vmess_14
  - 油管绵阿羊_United States_vmess_21
  - 油管绵阿羊_None_vmess_22
  - 油管绵阿羊_United States_vmess_23
  - 油管绵阿羊_None_vmess_24
  - 油管绵阿羊_United States_vmess_25
  - 油管绵阿羊_None_vmess_26
  - 油管绵阿羊_None_vmess_27
  - 油管绵阿羊_United States_vmess_28
  - 油管绵阿羊_United States_vmess_29
  - 油管绵阿羊_United States_vmess_210
  - 油管绵阿羊_None_vmess_211
  - 油管绵阿羊_None_vmess_212
  - 油管绵阿羊_None_vmess_31
  - 油管绵阿羊_None_vmess_32
  - 油管绵阿羊_None_vmess_33
  - 油管绵阿羊_United States_vmess_34
  - 油管绵阿羊_Canada_vmess_41
  - 油管绵阿羊_Canada_vmess_42
  - 油管绵阿羊_Canada_vmess_43
  - 油管绵阿羊_Canada_vmess_44
  - 油管绵阿羊_None_vmess_51
  - 油管绵阿羊_None_vmess_52
  - 油管绵阿羊_None_vmess_53
  - 油管绵阿羊_None_vmess_54
  - 油管绵阿羊_United States_vmess_55
  - 油管绵阿羊_None_vmess_56
  - 油管绵阿羊_United States_vmess_57
  - 油管绵阿羊_United States_vmess_58
  - 油管绵阿羊_None_vmess_59
  - 油管绵阿羊_None_vmess_510
  - 油管绵阿羊_None_vmess_511
  - 油管绵阿羊_United States_vmess_512
  - 油管绵阿羊_United States_vmess_513
  - 油管绵阿羊_United States_vmess_514
  - 油管绵阿羊_United States_vmess_515
  - 油管绵阿羊_United States_vmess_516
  - 油管绵阿羊_Taiwan_hysteria_61
  - 油管绵阿羊_France_hysteria2_71
  - 油管绵阿羊_United States_ss_81
  - 油管绵阿羊_Taiwan_hysteria_91
  - 油管绵阿羊_France_hy_0
  - 油管绵阿羊_United States_hy_1
  - 油管绵阿羊_Taiwan_hy_2
  - 油管绵阿羊_United States_hy_3
  - 油管绵阿羊_France_hy2_0
  - 油管绵阿羊_United States_hy2_1
  - 油管绵阿羊_France_hy2_2
  - 油管绵阿羊_France_hy2_3
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
aHlzdGVyaWE6Ly93d3cyLmR0a3U0OC54eXo6MjIzMzQ/cGVlcj0mYXV0aD1kb25ndGFpd2FuZy5jb20maW5zZWN1cmU9MSZ1cG1icHM9NTAmZG93bm1icHM9ODAmYWxwbj1oMyZtcG9ydD0yMjMzNCZvYmZzPSZwcm90b2NvbD11ZHAmZmFzdG9wZW49MSNUYWl3YW5faHlfNgpoeXN0ZXJpYTI6Ly9kb25ndGFpd2FuZy5jb21ANTEuMTU5Ljc3LjE1MzozMzM5MD9pbnNlY3VyZT0xJnNuaT1iaW5nLmNvbSZvYmZzPSZvYmZzLXBhc3N3b3JkPSNGcmFuY2VfaHkyXzcKaHlzdGVyaWE6Ly93d3cuZHRrdTUwLnh5ejoxODQ3MD9wZWVyPXd3dy5hbWF6b24uY24mYXV0aD0maW5zZWN1cmU9MSZ1cG1icHM9NTAmZG93bm1icHM9ODAmYWxwbj1oMyZtcG9ydD0xODQ3MCZvYmZzPSZwcm90b2NvbD11ZHAmZmFzdG9wZW49MSNUYWl3YW5faHlfOQphSFIwY0hNNkx5OWtiMjVuZEdGcGQyRnVaeTVqYjIwNlpHOXVaM1JoYVhkaGJtY3VZMjl0UUc1aGFYWmxNVGt1WTJaalpHNHpMbmg1ZWpvME5ETT0KYUhSMGNITTZMeTlrYjI1bmRHRnBkMkZ1Wnk1amIyMDZaRzl1WjNSaGFYZGhibWN1WTI5dFFIZDNkeTVrZEd0MU5UQXVlSGw2T2pRME13PT0KaHlzdGVyaWE6Ly81MS4xNTguNTQuNDY6NTUzOTY/cGVlcj15b3VrdS5jb20mYXV0aD1kb25ndGFpd2FuZy5jb20maW5zZWN1cmU9MSZ1cG1icHM9MTEmZG93bm1icHM9NTUmYWxwbj1oMyZvYmZzPSZwcm90b2NvbD11ZHAmZmFzdG9wZW49MSNGcmFuY2VfaHlzdGVyaWFfMApoeXN0ZXJpYTovLzE3My4yMzQuMjUuNTI6NDg5MTk/cGVlcj1iaW5nLmNvbSZhdXRoPWRvbmd0YWl3YW5nLmNvbSZpbnNlY3VyZT0xJnVwbWJwcz0xMSZkb3dubWJwcz01NSZhbHBuPWgzJm9iZnM9JnByb3RvY29sPXVkcCZmYXN0b3Blbj0xI1VuaXRlZCBTdGF0ZXNfaHlzdGVyaWFfMQpoeXN0ZXJpYTovL3d3dy5kdGt1NDAueHl6OjE4NDkwP3BlZXI9YmluZy5jb20mYXV0aD1kb25ndGFpd2FuZy5jb20maW5zZWN1cmU9MSZ1cG1icHM9MTEmZG93bm1icHM9NTUmYWxwbj1oMyZvYmZzPSZwcm90b2NvbD11ZHAmZmFzdG9wZW49MSNUYWl3YW5faHlzdGVyaWFfMgpoeXN0ZXJpYTovLzE2Ny4xNjAuOTEuMTE1OjQxMTg5P3BlZXI9d3d3LmFtYXpvbi5jbiZhdXRoPWJXQXdJcUlObzdYRG0xZlVsWFFHQmlmVklYb1lzMXlsZ1ZLcVdGS3pLMVh5REt1d05GJmluc2VjdXJlPTEmdXBtYnBzPTExJmRvd25tYnBzPTU1JmFscG49aDMmb2Jmcz0mcHJvdG9jb2w9dWRwJmZhc3RvcGVuPTEjVW5pdGVkIFN0YXRlc19oeXN0ZXJpYV8zCmh5c3RlcmlhMjovL2Rvbmd0YWl3YW5nLmNvbUA2Mi4yMTAuMTAzLjA6MjI0ODM/aW5zZWN1cmU9MSZzbmk9d3d3LmJpbmcuY29tI0ZyYW5jZV9oeXN0ZXJpYTJfMApoeXN0ZXJpYTI6Ly9kb25ndGFpd2FuZy5jb21ANjQuMTEwLjI1LjExOjMzMzM3P2luc2VjdXJlPTEmc25pPXd3dy5iaW5nLmNvbSNVbml0ZWQgU3RhdGVzX2h5c3RlcmlhMl8xCmh5c3RlcmlhMjovL2Rvbmd0YWl3YW5nLmNvbUA2Mi4yMTAuMTAzLjA6MjI0ODM/aW5zZWN1cmU9MSZzbmk9d3d3LmJpbmcuY29tI0ZyYW5jZV9oeXN0ZXJpYTJfMgpoeXN0ZXJpYTI6Ly9kb25ndGFpd2FuZy5jb21ANTEuMTU5Ljc3LjE5ODo1Mzk2Nz9pbnNlY3VyZT0xJnNuaT13d3cuYmluZy5jb20jRnJhbmNlX2h5c3RlcmlhMl8zCnZsZXNzOi8vZWJmZGNjYjYtNzQxNi00YjZlLTg2MGQtOTg1ODczNDRkNTAwQHloMS5kdGt1NDEueHl6OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZT0wJmZsb3c9JnR5cGU9d3MmZnA9Y2hyb21lJnBiaz0mc2lkPSZzbmk9bGcxLmZyZWVzc3IyLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0veHlha3dzJmhvc3Q9bGcxLmZyZWVzc3IyLnh5eiNOb25lX3ZsZXNzXzEKdmxlc3M6Ly9lYmZkY2NiNi03NDE2LTRiNmUtODYwZC05ODU4NzM0NGQ1MDBAeWg2LmR0a3U0MS54eXo6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlPTAmZmxvdz0mdHlwZT13cyZmcD1jaHJvbWUmcGJrPSZzaWQ9JnNuaT1sZzEuZnJlZXNzcjIueHl6JnNlcnZpY2VOYW1lPSZwYXRoPS94eWFrd3MmaG9zdD1sZzEuZnJlZXNzcjIueHl6I1VuaXRlZCBTdGF0ZXNfdmxlc3NfMgp2bGVzczovL2ViZmRjY2I2LTc0MTYtNGI2ZS04NjBkLTk4NTg3MzQ0ZDUwMEBmYmkuZ292OjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZT0wJmZsb3c9JnR5cGU9d3MmZnA9Y2hyb21lJnBiaz0mc2lkPSZzbmk9bGcxLmZyZWVzc3IyLnh5eiZzZXJ2aWNlTmFtZT0mcGF0aD0veHlha3dzJmhvc3Q9bGcxLmZyZWVzc3IyLnh5eiNOb25lX3ZsZXNzXzM=
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
        "🇹🇼 Taiwan_hy_6",
        "🇫🇷 France_hy2_7",
        "🇺🇸 United States_vless_8",
        "🇹🇼 Taiwan_hy_9",
        "🇫🇷 France_hysteria_0",
        "🇺🇸 United States_hysteria_1",
        "🇹🇼 Taiwan_hysteria_2",
        "🇺🇸 United States_hysteria_3",
        "🇫🇷 France_hysteria2_0",
        "🇺🇸 United States_hysteria2_1",
        "🇫🇷 France_hysteria2_2",
        "🇫🇷 France_hysteria2_3",
        "None_vless_1",
        "🇫🇷 France_vless_2",
        "🇫🇷 France_vless_3"
      ]
    },
    {
      "tag": "🤖 OpenAI",
      "type": "selector",
      "outbounds": [
        "🇹🇼 台湾节点",
        "🇸🇬 狮城节点",
        "🇯🇵 日本节点",
        "🇺🇸 美国节点",
        "✈️ 其他节点"
      ],
      "default": "🇺🇸 美国节点"
    },
    {
      "tag": "🌌 Google",
      "type": "selector",
      "outbounds": [
        "🇭🇰 香港节点",
        "🇹🇼 台湾节点",
        "🇸🇬 狮城节点",
        "🇯🇵 日本节点",
        "🇺🇸 美国节点",
        "✈️ 其他节点"
      ]
    },
    {
      "tag": "📟 Telegram",
      "type": "selector",
      "outbounds": [
        "🇭🇰 香港节点",
        "🇹🇼 台湾节点",
        "🇸🇬 狮城节点",
        "🇯🇵 日本节点",
        "🇺🇸 美国节点",
        "✈️ 其他节点"
      ]
    },
    {
      "tag": "🐦 Twitter",
      "type": "selector",
      "outbounds": [
        "🇭🇰 香港节点",
        "🇹🇼 台湾节点",
        "🇸🇬 狮城节点",
        "🇯🇵 日本节点",
        "🇺🇸 美国节点",
        "✈️ 其他节点"
      ]
    },
    {
      "tag": "👤 Facebook",
      "type": "selector",
      "outbounds": [
        "🇭🇰 香港节点",
        "🇹🇼 台湾节点",
        "🇸🇬 狮城节点",
        "🇯🇵 日本节点",
        "🇺🇸 美国节点",
        "✈️ 其他节点"
      ]
    },
    {
      "tag": "🛍️ Amazon",
      "type": "selector",
      "outbounds": [
        "direct",
        "🇭🇰 香港节点",
        "🇹🇼 台湾节点",
        "🇸🇬 狮城节点",
        "🇯🇵 日本节点",
        "🇺🇸 美国节点",
        "✈️ 其他节点"
      ]
    },
    {
      "tag": "🍎 Apple",
      "type": "selector",
      "outbounds": [
        "direct",
        "🇭🇰 香港节点",
        "🇹🇼 台湾节点",
        "🇸🇬 狮城节点",
        "🇯🇵 日本节点",
        "🇺🇸 美国节点",
        "✈️ 其他节点"
      ]
    },
    {
      "tag": "🧩 Microsoft",
      "type": "selector",
      "outbounds": [
        "direct",
        "🇭🇰 香港节点",
        "🇹🇼 台湾节点",
        "🇸🇬 狮城节点",
        "🇯🇵 日本节点",
        "🇺🇸 美国节点",
        "✈️ 其他节点"
      ]
    },
    {
      "tag": "🎮 Game",
      "type": "selector",
      "outbounds": [
        "direct",
        "🇭🇰 香港节点",
        "🇹🇼 台湾节点",
        "🇸🇬 狮城节点",
        "🇯🇵 日本节点",
        "🇺🇸 美国节点",
        "✈️ 其他节点"
      ]
    },
    {
      "tag": "📺 Bilibili",
      "type": "selector",
      "outbounds": [
        "direct",
        "🇭🇰 香港节点",
        "🇹🇼 台湾节点"
      ]
    },
    {
      "tag": "🎬 MediaVideo",
      "type": "selector",
      "outbounds": [
        "🇭🇰 香港节点",
        "🇹🇼 台湾节点",
        "🇸🇬 狮城节点",
        "🇯🇵 日本节点",
        "🇺🇸 美国节点",
        "✈️ 其他节点"
      ]
    },
    {
      "tag": "🌏 !cn",
      "type": "selector",
      "outbounds": [
        "🇭🇰 香港节点",
        "🇹🇼 台湾节点",
        "🇸🇬 狮城节点",
        "🇯🇵 日本节点",
        "🇺🇸 美国节点",
        "✈️ 其他节点",
        "direct"
      ]
    },
    {
      "tag": "🇭🇰 香港节点",
      "type": "selector",
      "outbounds": [
        "proxy"
      ]
    },
    {
      "tag": "🇹🇼 台湾节点",
      "type": "selector",
      "outbounds": [
        "🇹🇼 Taiwan_hy_6",
        "🇹🇼 Taiwan_hy_9",
        "🇹🇼 Taiwan_hysteria_2",
        "proxy"
      ]
    },
    {
      "tag": "🇸🇬 狮城节点",
      "type": "selector",
      "outbounds": [
        "proxy"
      ]
    },
    {
      "tag": "🇯🇵 日本节点",
      "type": "selector",
      "outbounds": [
        "proxy"
      ]
    },
    {
      "tag": "🇺🇸 美国节点",
      "type": "selector",
      "outbounds": [
        "🇺🇸 United States_vless_8",
        "🇺🇸 United States_hysteria_1",
        "🇺🇸 United States_hysteria_3",
        "🇺🇸 United States_hysteria2_1",
        "proxy"
      ]
    },
    {
      "tag": "✈️ 其他节点",
      "type": "selector",
      "outbounds": [
        "🇫🇷 France_hy2_7",
        "🇫🇷 France_hysteria_0",
        "🇫🇷 France_hysteria2_0",
        "🇫🇷 France_hysteria2_2",
        "🇫🇷 France_hysteria2_3",
        "None_vless_1",
        "🇫🇷 France_vless_2",
        "🇫🇷 France_vless_3",
        "proxy"
      ]
    },
    {
      "tag": "🌏 cn",
      "type": "selector",
      "outbounds": [
        "direct",
        "proxy"
      ]
    },
    {
      "tag": "🛑 AdBlock",
      "type": "selector",
      "outbounds": [
        "block",
        "direct"
      ]
    },
    {
      "tag": "auto",
      "type": "urltest",
      "outbounds": [
        "🇹🇼 Taiwan_hy_6",
        "🇫🇷 France_hy2_7",
        "🇺🇸 United States_vless_8",
        "🇹🇼 Taiwan_hy_9",
        "🇫🇷 France_hysteria_0",
        "🇺🇸 United States_hysteria_1",
        "🇹🇼 Taiwan_hysteria_2",
        "🇺🇸 United States_hysteria_3",
        "🇫🇷 France_hysteria2_0",
        "🇺🇸 United States_hysteria2_1",
        "🇫🇷 France_hysteria2_2",
        "🇫🇷 France_hysteria2_3",
        "None_vless_1",
        "🇫🇷 France_vless_2",
        "🇫🇷 France_vless_3"
      ],
      "url": "http://www.gstatic.com/generate_204",
      "interval": "5m",
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
      "server": "51.159.77.153",
      "server_port": 33390,
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
      "tag": "🇺🇸 United States_vless_8",
      "type": "vless",
      "server": "45.145.72.212",
      "server_port": 11223,
      "uuid": "34d7aac1-fac7-4e17-b41e-5be028d286cd",
      "packet_encoding": "xudp",
      "flow": "xtls-rprx-vision",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "addons.mozilla.org",
        "utls": {
          "enabled": true,
          "fingerprint": "chrome"
        },
        "reality": {
          "enabled": true,
          "public_key": "u24pYS0RqtYk8NBqtg4NIHUZIA0HmwuYw2RBIyt0T0c"
        }
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
      "server_port": 53967,
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
      "tag": "None_vless_1",
      "type": "vless",
      "server": "yh1.dtku41.xyz",
      "server_port": 443,
      "uuid": "ebfdccb6-7416-4b6e-860d-98587344d500",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": false,
        "server_name": "lg1.freessr2.xyz",
        "utls": {
          "enabled": true,
          "fingerprint": "chrome"
        }
      },
      "transport": {
        "type": "ws",
        "path": "/xyakws",
        "headers": {
          "Host": "lg1.freessr2.xyz"
        }
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
        "network": "udp",
        "port": 443,
        "outbound": "block"
      },
      {
        "rule_set": "geosite-category-ads-all",
        "outbound": "🛑 AdBlock"
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
        "outbound": "🤖 OpenAI"
      },
      {
        "rule_set": "geosite-youtube",
        "outbound": "🌌 Google"
      },
      {
        "rule_set": "geoip-google",
        "outbound": "🌌 Google"
      },
      {
        "rule_set": [
          "geosite-google",
          "geosite-github"
        ],
        "outbound": "🌌 Google"
      },
      {
        "rule_set": "geoip-telegram",
        "outbound": "📟 Telegram"
      },
      {
        "rule_set": "geosite-telegram",
        "outbound": "📟 Telegram"
      },
      {
        "rule_set": "geoip-twitter",
        "outbound": "🐦 Twitter"
      },
      {
        "rule_set": "geosite-twitter",
        "outbound": "🐦 Twitter"
      },
      {
        "rule_set": "geoip-facebook",
        "outbound": "👤 Facebook"
      },
      {
        "rule_set": [
          "geosite-facebook",
          "geosite-instagram"
        ],
        "outbound": "👤 Facebook"
      },
      {
        "rule_set": "geosite-amazon",
        "outbound": "🛍️ Amazon"
      },
      {
        "rule_set": "geosite-apple",
        "outbound": "🍎 Apple"
      },
      {
        "rule_set": "geosite-microsoft",
        "outbound": "🧩 Microsoft"
      },
      {
        "rule_set": "geosite-category-games",
        "outbound": "🎮 Game"
      },
      {
        "rule_set": "geosite-bilibili",
        "outbound": "📺 Bilibili"
      },
      {
        "rule_set": "geoip-netflix",
        "outbound": "🎬 MediaVideo"
      },
      {
        "rule_set": [
          "geosite-tiktok",
          "geosite-netflix",
          "geosite-hbo",
          "geosite-disney",
          "geosite-primevideo"
        ],
        "outbound": "🎬 MediaVideo"
      },
      {
        "rule_set": "geosite-geolocation-!cn",
        "outbound": "🌏 !cn"
      },
      {
        "ip_is_private": true,
        "outbound": "🌏 cn"
      },
      {
        "rule_set": "geoip-cn",
        "outbound": "🌏 cn"
      },
      {
        "rule_set": "geosite-cn",
        "outbound": "🌏 cn"
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
        "tag": "geoip-cn",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geoip/cn.srs",
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
        "tag": "geosite-amazon",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/amazon.srs",
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
        "tag": "geosite-bilibili",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/bilibili.srs",
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
        "tag": "geosite-hbo",
        "type": "remote",
        "format": "binary",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/hbo.srs",
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


