
---
title: VPN合集
date: 2024-02-09 05:34:41
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

> Last Update Time: 2024-02-09 05:34:41
---
# vless_node
```bash

None

```

# CloudFlare优质IP
```bash

电信162.159.240.32
电信172.64.140.35
电信172.64.206.227

联通172.64.92.255
联通162.159.249.207
联通172.64.168.50

移动172.67.162.30
移动173.245.49.187
移动172.67.199.90


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
140.82.112.9                  codeload.github.com
140.82.113.22                 collector.github.com
185.199.109.133               desktop.githubusercontent.com
185.199.109.133               favicons.githubusercontent.com
140.82.113.4                  gist.github.com
52.216.9.35                   github-cloud.s3.amazonaws.com
3.5.20.16                     github-com.s3.amazonaws.com
54.231.161.153                github-production-release-asset-2e65be.s3.amazonaws.com
52.217.232.161                github-production-repository-file-5c1aeb.s3.amazonaws.com
52.216.38.233                 github-production-user-asset-6210df.s3.amazonaws.com
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


# Update time: 2024-02-09T12:05:22+08:00
# Update url: https://raw.hellogithub.com/hosts
# Star me: https://github.com/521xueweihan/GitHub520
# GitHub520 Host End

```

该内容会自动定时更新， 数据更新时间：2024-02-09T12:05:22+08:00

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
- name: 油管绵阿羊_None_vless_01
  type: vless
  server: 198.41.220.176
  port: 2083
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_South Korea_vless_02
  type: vless
  server: hk03.nttkk.com
  port: 443
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_03
  type: vless
  server: 104.17.208.177
  port: 2096
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_04
  type: vless
  server: 104.17.213.5
  port: 2083
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_05
  type: vless
  server: 104.17.223.161
  port: 2083
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_06
  type: vless
  server: 104.19.155.105
  port: 2083
  uuid: ffffffff-17ad-45e7-aaa1-f2baaa08e930
  tls: true
  servername: watashi.free.jppublic.moh539.link
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: watashi.free.jppublic.moh539.link
- name: 油管绵阿羊_None_vless_07
  type: vless
  server: 104.17.210.131
  port: 2087
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_08
  type: vless
  server: 104.17.212.239
  port: 8443
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_Japan_vless_09
  type: vless
  server: 43.153.181.217
  port: 443
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_010
  type: vless
  server: 104.16.96.82
  port: 8443
  uuid: ffffffff-17ad-45e7-aaa1-f2baaa08e930
  tls: true
  servername: watashi.free.jppublic.moh539.link
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: watashi.free.jppublic.moh539.link
- name: 油管绵阿羊_Singapore_vless_011
  type: vless
  server: 35.247.175.120
  port: 48597
  uuid: d342d11e-d424-4583-b36e-524ab1f0afa4
  tls: true
  servername: baipiao343.stunning-bassoon.pages.dev
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: baipiao343.stunning-bassoon.pages.dev
- name: 油管绵阿羊_None_vless_012
  type: vless
  server: 104.17.215.241
  port: 8443
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_013
  type: vless
  server: 104.17.214.39
  port: 8443
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_014
  type: vless
  server: 198.41.220.158
  port: 2087
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_015
  type: vless
  server: 104.17.210.128
  port: 2083
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_016
  type: vless
  server: 104.21.30.178
  port: 2087
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_017
  type: vless
  server: 104.17.210.138
  port: 2096
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_018
  type: vless
  server: 198.41.221.80
  port: 2083
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_019
  type: vless
  server: 198.41.221.237
  port: 443
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_020
  type: vless
  server: 104.21.17.151
  port: 443
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_021
  type: vless
  server: 104.17.221.226
  port: 2096
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_022
  type: vless
  server: 104.21.0.236
  port: 8443
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_023
  type: vless
  server: 104.17.219.35
  port: 2096
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_United States_vless_024
  type: vless
  server: jgw.wshyx.pp.ua
  port: 2087
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_025
  type: vless
  server: 198.41.221.12
  port: 2096
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_026
  type: vless
  server: 104.21.28.147
  port: 2083
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_027
  type: vless
  server: 198.41.209.150
  port: 8443
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_028
  type: vless
  server: 104.19.155.11
  port: 8443
  uuid: ffffffff-17ad-45e7-aaa1-f2baaa08e930
  tls: true
  servername: watashi.free.jppublic.moh539.link
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: watashi.free.jppublic.moh539.link
- name: 油管绵阿羊_None_vless_029
  type: vless
  server: 104.21.4.246
  port: 2083
  uuid: d342d11e-d424-4583-b36e-524ab1f0afa4
  tls: true
  servername: edgood.king361.cf
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: edgood.king361.cf
- name: 油管绵阿羊_None_vless_030
  type: vless
  server: 104.16.96.218
  port: 2087
  uuid: ffffffff-17ad-45e7-aaa1-f2baaa08e930
  tls: true
  servername: watashi.free.jppublic.moh539.link
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: watashi.free.jppublic.moh539.link
- name: 油管绵阿羊_United States_vless_031
  type: vless
  server: lilijuly.pp.ua
  port: 8443
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_032
  type: vless
  server: 104.17.208.174
  port: 8443
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_033
  type: vless
  server: 104.21.5.7
  port: 8443
  uuid: 73b6dbd5-a27a-4c76-9ad1-42a82380dddb
  tls: true
  servername: ed.ariesver.online
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: ed.ariesver.online
- name: 油管绵阿羊_None_vless_034
  type: vless
  server: 104.17.210.9
  port: 2083
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_035
  type: vless
  server: 104.21.2.0
  port: 8443
  uuid: 7fd7c15d-95cd-4f5c-bf59-f21e5eb27580
  tls: true
  servername: 3k.dabee.top
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: 3k.dabee.top
- name: 油管绵阿羊_None_vless_036
  type: vless
  server: 104.21.5.33
  port: 2083
  uuid: 73b6dbd5-a27a-4c76-9ad1-42a82380dddb
  tls: true
  servername: ed.ariesver.online
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: ed.ariesver.online
- name: 油管绵阿羊_None_vless_037
  type: vless
  server: 104.21.12.151
  port: 2087
  uuid: 7fd7c15d-95cd-4f5c-bf59-f21e5eb27580
  tls: true
  servername: 3k.dabee.top
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: 3k.dabee.top
- name: 油管绵阿羊_None_vless_038
  type: vless
  server: 104.21.12.84
  port: 443
  uuid: 7fd7c15d-95cd-4f5c-bf59-f21e5eb27580
  tls: true
  servername: 3k.dabee.top
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: 3k.dabee.top
- name: 油管绵阿羊_None_vless_039
  type: vless
  server: 104.17.219.151
  port: 8443
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_040
  type: vless
  server: 104.21.15.243
  port: 2096
  uuid: 73b6dbd5-a27a-4c76-9ad1-42a82380dddb
  tls: true
  servername: ed.ariesver.online
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: ed.ariesver.online
- name: 油管绵阿羊_United States_vless_041
  type: vless
  server: xwm-us-v6-a.mouboss.pp.ua
  port: 2083
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_United States_vless_042
  type: vless
  server: dvorda.pp.ua
  port: 2096
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_043
  type: vless
  server: 104.21.30.176
  port: 2096
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_044
  type: vless
  server: smi.pp.ua
  port: 8443
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_045
  type: vless
  server: 104.21.28.29
  port: 2053
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_046
  type: vless
  server: 104.16.96.197
  port: 2087
  uuid: ffffffff-17ad-45e7-aaa1-f2baaa08e930
  tls: true
  servername: watashi.free.jppublic.moh539.link
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: watashi.free.jppublic.moh539.link
- name: 油管绵阿羊_None_vless_047
  type: vless
  server: 104.16.96.54
  port: 8443
  uuid: ffffffff-17ad-45e7-aaa1-f2baaa08e930
  tls: true
  servername: watashi.free.jppublic.moh539.link
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: watashi.free.jppublic.moh539.link
- name: 油管绵阿羊_None_vless_048
  type: vless
  server: 198.41.221.195
  port: 2096
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_United States_vless_049
  type: vless
  server: jp7.vlessx.us
  port: 8443
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_050
  type: vless
  server: 104.21.17.152
  port: 2083
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_051
  type: vless
  server: 104.21.0.169
  port: 443
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_052
  type: vless
  server: 104.21.2.68
  port: 2087
  uuid: 7fd7c15d-95cd-4f5c-bf59-f21e5eb27580
  tls: true
  servername: 3k.dabee.top
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: 3k.dabee.top
- name: 油管绵阿羊_None_vless_053
  type: vless
  server: smi.pp.ua
  port: 2083
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_054
  type: vless
  server: 104.21.4.87
  port: 2083
  uuid: d342d11e-d424-4583-b36e-524ab1f0afa4
  tls: true
  servername: edgood.king361.cf
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: edgood.king361.cf
- name: 油管绵阿羊_None_vless_055
  type: vless
  server: 104.21.5.172
  port: 2053
  uuid: 73b6dbd5-a27a-4c76-9ad1-42a82380dddb
  tls: true
  servername: ed.ariesver.online
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: ed.ariesver.online
- name: 油管绵阿羊_None_vless_056
  type: vless
  server: 104.21.4.183
  port: 2087
  uuid: d342d11e-d424-4583-b36e-524ab1f0afa4
  tls: true
  servername: edgood.king361.cf
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: edgood.king361.cf
- name: 油管绵阿羊_United States_vless_057
  type: vless
  server: smi.pp.ua
  port: 443
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_058
  type: vless
  server: 104.21.1.138
  port: 2087
  uuid: ffffffff-17ad-45e7-aaa1-f2baaa08e930
  tls: true
  servername: watashi.free.jppublic.moh539.link
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: watashi.free.jppublic.moh539.link
- name: 油管绵阿羊_None_vless_059
  type: vless
  server: 104.18.190.52
  port: 443
  uuid: a4faf5d8-b9a8-433e-9518-2d2e21d76f78
  tls: true
  servername: nginx.nirevil.ir
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: nginx.nirevil.ir
- name: 油管绵阿羊_None_vless_060
  type: vless
  server: 198.41.208.156
  port: 2087
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_061
  type: vless
  server: 104.21.0.152
  port: 2053
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_United States_vless_062
  type: vless
  server: a.noonokorean.pp.ua
  port: 2096
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_063
  type: vless
  server: 104.21.16.238
  port: 443
  uuid: ffffffff-17ad-45e7-aaa1-f2baaa08e930
  tls: true
  servername: watashi.free.jppublic.moh539.link
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: watashi.free.jppublic.moh539.link
- name: 油管绵阿羊_None_vless_064
  type: vless
  server: 104.21.1.250
  port: 8443
  uuid: ffffffff-17ad-45e7-aaa1-f2baaa08e930
  tls: true
  servername: watashi.free.jppublic.moh539.link
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: watashi.free.jppublic.moh539.link
- name: 油管绵阿羊_None_vless_065
  type: vless
  server: 104.21.26.225
  port: 2083
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_066
  type: vless
  server: 104.17.209.149
  port: 2083
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_067
  type: vless
  server: us10.vlessx.us
  port: 8443
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_068
  type: vless
  server: 104.21.26.230
  port: 8443
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_069
  type: vless
  server: 104.21.28.62
  port: 443
  uuid: b9ad895b-12ac-40fc-a5ac-a5b2a1285001
  tls: true
  servername: 3k.pureboy.eu.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: 3k.pureboy.eu.org
- name: 油管绵阿羊_None_vless_070
  type: vless
  server: 104.21.2.96
  port: 2087
  uuid: 7fd7c15d-95cd-4f5c-bf59-f21e5eb27580
  tls: true
  servername: 3k.dabee.top
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: 3k.dabee.top
- name: 油管绵阿羊_None_vless_071
  type: vless
  server: 104.21.14.245
  port: 2087
  uuid: d342d11e-d424-4583-b36e-524ab1f0afa4
  tls: true
  servername: edgood.king361.cf
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: edgood.king361.cf
- name: 油管绵阿羊_None_vless_072
  type: vless
  server: 104.21.15.55
  port: 2083
  uuid: 73b6dbd5-a27a-4c76-9ad1-42a82380dddb
  tls: true
  servername: ed.ariesver.online
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: ed.ariesver.online
- name: 油管绵阿羊_None_vless_073
  type: vless
  server: 198.41.221.173
  port: 2087
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_074
  type: vless
  server: 104.21.15.226
  port: 2087
  uuid: 73b6dbd5-a27a-4c76-9ad1-42a82380dddb
  tls: true
  servername: ed.ariesver.online
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: ed.ariesver.online
- name: 油管绵阿羊_None_vless_075
  type: vless
  server: 104.21.2.173
  port: 2096
  uuid: 7fd7c15d-95cd-4f5c-bf59-f21e5eb27580
  tls: true
  servername: 3k.dabee.top
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: 3k.dabee.top
- name: 油管绵阿羊_United States_vless_076
  type: vless
  server: ctwct.arvancode.eu.org
  port: 2096
  uuid: f4cec6cc-6177-423c-90f8-2ad9f0dd996b
  tls: true
  servername: vpnct.arvancode.eu.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: vpnct.arvancode.eu.org
- name: 油管绵阿羊_None_vless_077
  type: vless
  server: 104.21.0.177
  port: 2053
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_United States_vless_078
  type: vless
  server: jgw.wshyx.pp.ua
  port: 2083
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_079
  type: vless
  server: 104.21.24.7
  port: 8443
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_080
  type: vless
  server: 104.21.2.219
  port: 2096
  uuid: 7fd7c15d-95cd-4f5c-bf59-f21e5eb27580
  tls: true
  servername: 3k.dabee.top
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: 3k.dabee.top
- name: 油管绵阿羊_None_vless_081
  type: vless
  server: 104.21.15.243
  port: 2053
  uuid: 73b6dbd5-a27a-4c76-9ad1-42a82380dddb
  tls: true
  servername: ed.ariesver.online
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: ed.ariesver.online
- name: 油管绵阿羊_None_vless_082
  type: vless
  server: 104.21.1.147
  port: 2053
  uuid: ffffffff-17ad-45e7-aaa1-f2baaa08e930
  tls: true
  servername: watashi.free.jppublic.moh539.link
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: watashi.free.jppublic.moh539.link
- name: 油管绵阿羊_None_vless_083
  type: vless
  server: 104.21.12.140
  port: 2053
  uuid: 7fd7c15d-95cd-4f5c-bf59-f21e5eb27580
  tls: true
  servername: 3k.dabee.top
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: 3k.dabee.top
- name: 油管绵阿羊_None_vless_084
  type: vless
  server: 198.41.209.180
  port: 2053
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_United States_vless_085
  type: vless
  server: tz.lilijuly.pp.ua
  port: 2083
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_United States_vless_086
  type: vless
  server: i.noonokorean.pp.ua
  port: 2096
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_United States_vless_087
  type: vless
  server: 88888.pp.ua
  port: 2087
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_088
  type: vless
  server: 104.21.1.179
  port: 2096
  uuid: ffffffff-17ad-45e7-aaa1-f2baaa08e930
  tls: true
  servername: watashi.free.jppublic.moh539.link
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: watashi.free.jppublic.moh539.link
- name: 油管绵阿羊_Taiwan_tuic_11
  type: tuic
  server: 111.243.97.2
  port: 33098
  udp: true
  uuid: fef3d3c2-ab3e-4134-a2f3-0c2d83e0a76d
  password: dongtaiwang.com
  alpn:
  - h3
  disable-sni: true
  reduce-rtt: true
  udp-relay-mode: native
  congestion-controller: bbr
- name: 油管绵阿羊_None_vmess_21
  type: vmess
  server: www.darkroom.lol
  port: 8080
  cipher: auto
  uuid: 22826b44-5c1a-4b4b-dbaa-83a2e8bd95f0
  alterId: 0
  tls: false
  skip-cert-verify: true
  network: ws
  ws-opts:
    path: /
    headers:
      host: www.darkroom.lol
- name: 油管绵阿羊_China_vmess_22
  type: vmess
  server: data-us-v1.shwjfkw.cn
  port: 20401
  cipher: auto
  uuid: b1478e24-4916-3abe-8f17-15931012ecbe
  alterId: 0
  tls: false
  skip-cert-verify: true
  network: ws
  ws-opts:
    path: /debian
    headers:
      host: data-us-v1.shwjfkw.cn
- name: 油管绵阿羊_China_ss_23
  type: ss
  server: service.ouluyun9803.com
  port: 20003
  password: d6105bbd-be0d-45b2-82ad-31fd1071c1d2
  cipher: chacha20-ietf-poly1305
- name: 油管绵阿羊_None_vmess_24
  type: vmess
  server: 104.21.82.183
  port: 8880
  cipher: auto
  uuid: 5a7021e0-26b4-45d6-b175-fe551601ca97
  alterId: 0
  tls: false
  skip-cert-verify: true
  network: ws
  ws-opts:
    path: /
    headers:
      host: server26.beheshtbaneh.com
- name: 油管绵阿羊_China_ss_25
  type: ss
  server: service.ouluyun9803.com
  port: 20005
  password: d6105bbd-be0d-45b2-82ad-31fd1071c1d2
  cipher: chacha20-ietf-poly1305
- name: 油管绵阿羊_United States_vmess_31
  type: vmess
  server: www.darkroom.lol
  port: 8080
  cipher: auto
  uuid: 22826b44-5c1a-4b4b-dbaa-83a2e8bd95f0
  alterId: 0
  tls: false
  skip-cert-verify: true
  network: ws
  ws-opts:
    path: /
    headers:
      host: www.darkroom.lol
- name: 油管绵阿羊_China_vmess_32
  type: vmess
  server: data-us-v1.shwjfkw.cn
  port: 20401
  cipher: auto
  uuid: b1478e24-4916-3abe-8f17-15931012ecbe
  alterId: 0
  tls: false
  skip-cert-verify: true
  network: ws
  ws-opts:
    path: /debian
    headers:
      host: data-us-v1.shwjfkw.cn
- name: 油管绵阿羊_China_ss_33
  type: ss
  server: service.ouluyun9803.com
  port: 20003
  password: d6105bbd-be0d-45b2-82ad-31fd1071c1d2
  cipher: chacha20-ietf-poly1305
- name: 油管绵阿羊_None_vmess_34
  type: vmess
  server: 104.21.82.183
  port: 8880
  cipher: auto
  uuid: 5a7021e0-26b4-45d6-b175-fe551601ca97
  alterId: 0
  tls: false
  skip-cert-verify: true
  network: ws
  ws-opts:
    path: /
    headers:
      host: server26.beheshtbaneh.com
- name: 油管绵阿羊_China_ss_35
  type: ss
  server: service.ouluyun9803.com
  port: 20005
  password: d6105bbd-be0d-45b2-82ad-31fd1071c1d2
  cipher: chacha20-ietf-poly1305
- name: 油管绵阿羊_United States_vmess_41
  type: vmess
  server: www.darkroom.lol
  port: 8080
  cipher: auto
  uuid: 22826b44-5c1a-4b4b-dbaa-83a2e8bd95f0
  alterId: 0
  tls: false
  skip-cert-verify: true
  network: ws
  ws-opts:
    path: /
    headers:
      host: www.darkroom.lol
- name: 油管绵阿羊_China_vmess_42
  type: vmess
  server: data-us-v1.shwjfkw.cn
  port: 20401
  cipher: auto
  uuid: b1478e24-4916-3abe-8f17-15931012ecbe
  alterId: 0
  tls: false
  skip-cert-verify: true
  network: ws
  ws-opts:
    path: /debian
    headers:
      host: data-us-v1.shwjfkw.cn
- name: 油管绵阿羊_China_ss_43
  type: ss
  server: service.ouluyun9803.com
  port: 20003
  password: d6105bbd-be0d-45b2-82ad-31fd1071c1d2
  cipher: chacha20-ietf-poly1305
- name: 油管绵阿羊_None_vmess_44
  type: vmess
  server: 104.21.82.183
  port: 8880
  cipher: auto
  uuid: 5a7021e0-26b4-45d6-b175-fe551601ca97
  alterId: 0
  tls: false
  skip-cert-verify: true
  network: ws
  ws-opts:
    path: /
    headers:
      host: server26.beheshtbaneh.com
- name: 油管绵阿羊_China_ss_45
  type: ss
  server: service.ouluyun9803.com
  port: 20005
  password: d6105bbd-be0d-45b2-82ad-31fd1071c1d2
  cipher: chacha20-ietf-poly1305
- name: 油管绵阿羊_United States_vmess_51
  type: vmess
  server: www.darkroom.lol
  port: 8080
  cipher: auto
  uuid: 22826b44-5c1a-4b4b-dbaa-83a2e8bd95f0
  alterId: 0
  tls: false
  skip-cert-verify: true
  network: ws
  ws-opts:
    path: /
    headers:
      host: www.darkroom.lol
- name: 油管绵阿羊_China_vmess_52
  type: vmess
  server: data-us-v1.shwjfkw.cn
  port: 20401
  cipher: auto
  uuid: b1478e24-4916-3abe-8f17-15931012ecbe
  alterId: 0
  tls: false
  skip-cert-verify: true
  network: ws
  ws-opts:
    path: /debian
    headers:
      host: data-us-v1.shwjfkw.cn
- name: 油管绵阿羊_China_ss_53
  type: ss
  server: service.ouluyun9803.com
  port: 20003
  password: d6105bbd-be0d-45b2-82ad-31fd1071c1d2
  cipher: chacha20-ietf-poly1305
- name: 油管绵阿羊_None_vmess_54
  type: vmess
  server: 104.21.82.183
  port: 8880
  cipher: auto
  uuid: 5a7021e0-26b4-45d6-b175-fe551601ca97
  alterId: 0
  tls: false
  skip-cert-verify: true
  network: ws
  ws-opts:
    path: /
    headers:
      host: server26.beheshtbaneh.com
- name: 油管绵阿羊_China_ss_55
  type: ss
  server: service.ouluyun9803.com
  port: 20005
  password: d6105bbd-be0d-45b2-82ad-31fd1071c1d2
  cipher: chacha20-ietf-poly1305
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
- name: 油管绵阿羊_Taiwan_hysteria_81
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
- name: 油管绵阿羊_United States_hy_2
  type: hysteria
  server: 108.181.22.239
  port: 39967
  ports: 39967
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
- name: 油管绵阿羊_United States_hy2_3
  type: hysteria2
  server: 108.181.24.77
  port: 43656
  password: dongtaiwang.com
  fast-open: true
  sni: www.bing.com
  skip-cert-verify: true
- name: 油管绵阿羊_United States_reality_1
  type: vless
  server: 108.181.22.213
  port: 28945
  uuid: 9cc39477-0d85-4419-84d4-fb7fc77668b3
  network: tcp
  tls: true
  udp: true
  flow: xtls-rprx-vision
  client-fingerprint: chrome
  servername: m.media-amazon.com
  reality-opts:
    public-key: yKXmLTmXAi-BHBg3JpCz-NWUmVcKlfm7iMmVoq7YQx0
    short-id: 6ba85179e30d4fc2
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
  - 油管绵阿羊_None_vless_01
  - 油管绵阿羊_South Korea_vless_02
  - 油管绵阿羊_None_vless_03
  - 油管绵阿羊_None_vless_04
  - 油管绵阿羊_None_vless_05
  - 油管绵阿羊_None_vless_06
  - 油管绵阿羊_None_vless_07
  - 油管绵阿羊_None_vless_08
  - 油管绵阿羊_Japan_vless_09
  - 油管绵阿羊_None_vless_010
  - 油管绵阿羊_Singapore_vless_011
  - 油管绵阿羊_None_vless_012
  - 油管绵阿羊_None_vless_013
  - 油管绵阿羊_None_vless_014
  - 油管绵阿羊_None_vless_015
  - 油管绵阿羊_None_vless_016
  - 油管绵阿羊_None_vless_017
  - 油管绵阿羊_None_vless_018
  - 油管绵阿羊_None_vless_019
  - 油管绵阿羊_None_vless_020
  - 油管绵阿羊_None_vless_021
  - 油管绵阿羊_None_vless_022
  - 油管绵阿羊_None_vless_023
  - 油管绵阿羊_United States_vless_024
  - 油管绵阿羊_None_vless_025
  - 油管绵阿羊_None_vless_026
  - 油管绵阿羊_None_vless_027
  - 油管绵阿羊_None_vless_028
  - 油管绵阿羊_None_vless_029
  - 油管绵阿羊_None_vless_030
  - 油管绵阿羊_United States_vless_031
  - 油管绵阿羊_None_vless_032
  - 油管绵阿羊_None_vless_033
  - 油管绵阿羊_None_vless_034
  - 油管绵阿羊_None_vless_035
  - 油管绵阿羊_None_vless_036
  - 油管绵阿羊_None_vless_037
  - 油管绵阿羊_None_vless_038
  - 油管绵阿羊_None_vless_039
  - 油管绵阿羊_None_vless_040
  - 油管绵阿羊_United States_vless_041
  - 油管绵阿羊_United States_vless_042
  - 油管绵阿羊_None_vless_043
  - 油管绵阿羊_None_vless_044
  - 油管绵阿羊_None_vless_045
  - 油管绵阿羊_None_vless_046
  - 油管绵阿羊_None_vless_047
  - 油管绵阿羊_None_vless_048
  - 油管绵阿羊_United States_vless_049
  - 油管绵阿羊_None_vless_050
  - 油管绵阿羊_None_vless_051
  - 油管绵阿羊_None_vless_052
  - 油管绵阿羊_None_vless_053
  - 油管绵阿羊_None_vless_054
  - 油管绵阿羊_None_vless_055
  - 油管绵阿羊_None_vless_056
  - 油管绵阿羊_United States_vless_057
  - 油管绵阿羊_None_vless_058
  - 油管绵阿羊_None_vless_059
  - 油管绵阿羊_None_vless_060
  - 油管绵阿羊_None_vless_061
  - 油管绵阿羊_United States_vless_062
  - 油管绵阿羊_None_vless_063
  - 油管绵阿羊_None_vless_064
  - 油管绵阿羊_None_vless_065
  - 油管绵阿羊_None_vless_066
  - 油管绵阿羊_None_vless_067
  - 油管绵阿羊_None_vless_068
  - 油管绵阿羊_None_vless_069
  - 油管绵阿羊_None_vless_070
  - 油管绵阿羊_None_vless_071
  - 油管绵阿羊_None_vless_072
  - 油管绵阿羊_None_vless_073
  - 油管绵阿羊_None_vless_074
  - 油管绵阿羊_None_vless_075
  - 油管绵阿羊_United States_vless_076
  - 油管绵阿羊_None_vless_077
  - 油管绵阿羊_United States_vless_078
  - 油管绵阿羊_None_vless_079
  - 油管绵阿羊_None_vless_080
  - 油管绵阿羊_None_vless_081
  - 油管绵阿羊_None_vless_082
  - 油管绵阿羊_None_vless_083
  - 油管绵阿羊_None_vless_084
  - 油管绵阿羊_United States_vless_085
  - 油管绵阿羊_United States_vless_086
  - 油管绵阿羊_United States_vless_087
  - 油管绵阿羊_None_vless_088
  - 油管绵阿羊_Taiwan_tuic_11
  - 油管绵阿羊_None_vmess_21
  - 油管绵阿羊_China_vmess_22
  - 油管绵阿羊_China_ss_23
  - 油管绵阿羊_None_vmess_24
  - 油管绵阿羊_China_ss_25
  - 油管绵阿羊_United States_vmess_31
  - 油管绵阿羊_China_vmess_32
  - 油管绵阿羊_China_ss_33
  - 油管绵阿羊_None_vmess_34
  - 油管绵阿羊_China_ss_35
  - 油管绵阿羊_United States_vmess_41
  - 油管绵阿羊_China_vmess_42
  - 油管绵阿羊_China_ss_43
  - 油管绵阿羊_None_vmess_44
  - 油管绵阿羊_China_ss_45
  - 油管绵阿羊_United States_vmess_51
  - 油管绵阿羊_China_vmess_52
  - 油管绵阿羊_China_ss_53
  - 油管绵阿羊_None_vmess_54
  - 油管绵阿羊_China_ss_55
  - 油管绵阿羊_Taiwan_hysteria_61
  - 油管绵阿羊_France_hysteria2_71
  - 油管绵阿羊_Taiwan_hysteria_81
  - 油管绵阿羊_Taiwan_hysteria_91
  - 油管绵阿羊_France_hy_0
  - 油管绵阿羊_United States_hy_1
  - 油管绵阿羊_United States_hy_2
  - 油管绵阿羊_United States_hy_3
  - 油管绵阿羊_France_hy2_0
  - 油管绵阿羊_United States_hy2_1
  - 油管绵阿羊_France_hy2_2
  - 油管绵阿羊_United States_hy2_3
  - 油管绵阿羊_United States_reality_1
  - 油管绵阿羊_France_reality_2
  - 油管绵阿羊_France_reality_3
- name: 自动选择
  type: url-test
  url: http://www.gstatic.com/generate_204
  interval: 300
  tolerance: 50
  proxies:
  - 油管绵阿羊_None_vless_01
  - 油管绵阿羊_South Korea_vless_02
  - 油管绵阿羊_None_vless_03
  - 油管绵阿羊_None_vless_04
  - 油管绵阿羊_None_vless_05
  - 油管绵阿羊_None_vless_06
  - 油管绵阿羊_None_vless_07
  - 油管绵阿羊_None_vless_08
  - 油管绵阿羊_Japan_vless_09
  - 油管绵阿羊_None_vless_010
  - 油管绵阿羊_Singapore_vless_011
  - 油管绵阿羊_None_vless_012
  - 油管绵阿羊_None_vless_013
  - 油管绵阿羊_None_vless_014
  - 油管绵阿羊_None_vless_015
  - 油管绵阿羊_None_vless_016
  - 油管绵阿羊_None_vless_017
  - 油管绵阿羊_None_vless_018
  - 油管绵阿羊_None_vless_019
  - 油管绵阿羊_None_vless_020
  - 油管绵阿羊_None_vless_021
  - 油管绵阿羊_None_vless_022
  - 油管绵阿羊_None_vless_023
  - 油管绵阿羊_United States_vless_024
  - 油管绵阿羊_None_vless_025
  - 油管绵阿羊_None_vless_026
  - 油管绵阿羊_None_vless_027
  - 油管绵阿羊_None_vless_028
  - 油管绵阿羊_None_vless_029
  - 油管绵阿羊_None_vless_030
  - 油管绵阿羊_United States_vless_031
  - 油管绵阿羊_None_vless_032
  - 油管绵阿羊_None_vless_033
  - 油管绵阿羊_None_vless_034
  - 油管绵阿羊_None_vless_035
  - 油管绵阿羊_None_vless_036
  - 油管绵阿羊_None_vless_037
  - 油管绵阿羊_None_vless_038
  - 油管绵阿羊_None_vless_039
  - 油管绵阿羊_None_vless_040
  - 油管绵阿羊_United States_vless_041
  - 油管绵阿羊_United States_vless_042
  - 油管绵阿羊_None_vless_043
  - 油管绵阿羊_None_vless_044
  - 油管绵阿羊_None_vless_045
  - 油管绵阿羊_None_vless_046
  - 油管绵阿羊_None_vless_047
  - 油管绵阿羊_None_vless_048
  - 油管绵阿羊_United States_vless_049
  - 油管绵阿羊_None_vless_050
  - 油管绵阿羊_None_vless_051
  - 油管绵阿羊_None_vless_052
  - 油管绵阿羊_None_vless_053
  - 油管绵阿羊_None_vless_054
  - 油管绵阿羊_None_vless_055
  - 油管绵阿羊_None_vless_056
  - 油管绵阿羊_United States_vless_057
  - 油管绵阿羊_None_vless_058
  - 油管绵阿羊_None_vless_059
  - 油管绵阿羊_None_vless_060
  - 油管绵阿羊_None_vless_061
  - 油管绵阿羊_United States_vless_062
  - 油管绵阿羊_None_vless_063
  - 油管绵阿羊_None_vless_064
  - 油管绵阿羊_None_vless_065
  - 油管绵阿羊_None_vless_066
  - 油管绵阿羊_None_vless_067
  - 油管绵阿羊_None_vless_068
  - 油管绵阿羊_None_vless_069
  - 油管绵阿羊_None_vless_070
  - 油管绵阿羊_None_vless_071
  - 油管绵阿羊_None_vless_072
  - 油管绵阿羊_None_vless_073
  - 油管绵阿羊_None_vless_074
  - 油管绵阿羊_None_vless_075
  - 油管绵阿羊_United States_vless_076
  - 油管绵阿羊_None_vless_077
  - 油管绵阿羊_United States_vless_078
  - 油管绵阿羊_None_vless_079
  - 油管绵阿羊_None_vless_080
  - 油管绵阿羊_None_vless_081
  - 油管绵阿羊_None_vless_082
  - 油管绵阿羊_None_vless_083
  - 油管绵阿羊_None_vless_084
  - 油管绵阿羊_United States_vless_085
  - 油管绵阿羊_United States_vless_086
  - 油管绵阿羊_United States_vless_087
  - 油管绵阿羊_None_vless_088
  - 油管绵阿羊_Taiwan_tuic_11
  - 油管绵阿羊_None_vmess_21
  - 油管绵阿羊_China_vmess_22
  - 油管绵阿羊_China_ss_23
  - 油管绵阿羊_None_vmess_24
  - 油管绵阿羊_China_ss_25
  - 油管绵阿羊_United States_vmess_31
  - 油管绵阿羊_China_vmess_32
  - 油管绵阿羊_China_ss_33
  - 油管绵阿羊_None_vmess_34
  - 油管绵阿羊_China_ss_35
  - 油管绵阿羊_United States_vmess_41
  - 油管绵阿羊_China_vmess_42
  - 油管绵阿羊_China_ss_43
  - 油管绵阿羊_None_vmess_44
  - 油管绵阿羊_China_ss_45
  - 油管绵阿羊_United States_vmess_51
  - 油管绵阿羊_China_vmess_52
  - 油管绵阿羊_China_ss_53
  - 油管绵阿羊_None_vmess_54
  - 油管绵阿羊_China_ss_55
  - 油管绵阿羊_Taiwan_hysteria_61
  - 油管绵阿羊_France_hysteria2_71
  - 油管绵阿羊_Taiwan_hysteria_81
  - 油管绵阿羊_Taiwan_hysteria_91
  - 油管绵阿羊_France_hy_0
  - 油管绵阿羊_United States_hy_1
  - 油管绵阿羊_United States_hy_2
  - 油管绵阿羊_United States_hy_3
  - 油管绵阿羊_France_hy2_0
  - 油管绵阿羊_United States_hy2_1
  - 油管绵阿羊_France_hy2_2
  - 油管绵阿羊_United States_hy2_3
  - 油管绵阿羊_United States_reality_1
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
- name: 油管绵阿羊_None_vless_01
  type: vless
  server: 198.41.220.176
  port: 2083
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_South Korea_vless_02
  type: vless
  server: hk03.nttkk.com
  port: 443
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_03
  type: vless
  server: 104.17.208.177
  port: 2096
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_04
  type: vless
  server: 104.17.213.5
  port: 2083
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_05
  type: vless
  server: 104.17.223.161
  port: 2083
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_06
  type: vless
  server: 104.19.155.105
  port: 2083
  uuid: ffffffff-17ad-45e7-aaa1-f2baaa08e930
  tls: true
  servername: watashi.free.jppublic.moh539.link
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: watashi.free.jppublic.moh539.link
- name: 油管绵阿羊_None_vless_07
  type: vless
  server: 104.17.210.131
  port: 2087
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_08
  type: vless
  server: 104.17.212.239
  port: 8443
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_Japan_vless_09
  type: vless
  server: 43.153.181.217
  port: 443
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_010
  type: vless
  server: 104.16.96.82
  port: 8443
  uuid: ffffffff-17ad-45e7-aaa1-f2baaa08e930
  tls: true
  servername: watashi.free.jppublic.moh539.link
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: watashi.free.jppublic.moh539.link
- name: 油管绵阿羊_Singapore_vless_011
  type: vless
  server: 35.247.175.120
  port: 48597
  uuid: d342d11e-d424-4583-b36e-524ab1f0afa4
  tls: true
  servername: baipiao343.stunning-bassoon.pages.dev
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: baipiao343.stunning-bassoon.pages.dev
- name: 油管绵阿羊_None_vless_012
  type: vless
  server: 104.17.215.241
  port: 8443
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_013
  type: vless
  server: 104.17.214.39
  port: 8443
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_014
  type: vless
  server: 198.41.220.158
  port: 2087
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_015
  type: vless
  server: 104.17.210.128
  port: 2083
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_016
  type: vless
  server: 104.21.30.178
  port: 2087
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_017
  type: vless
  server: 104.17.210.138
  port: 2096
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_018
  type: vless
  server: 198.41.221.80
  port: 2083
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_019
  type: vless
  server: 198.41.221.237
  port: 443
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_020
  type: vless
  server: 104.21.17.151
  port: 443
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_021
  type: vless
  server: 104.17.221.226
  port: 2096
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_022
  type: vless
  server: 104.21.0.236
  port: 8443
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_023
  type: vless
  server: 104.17.219.35
  port: 2096
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_United States_vless_024
  type: vless
  server: jgw.wshyx.pp.ua
  port: 2087
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_025
  type: vless
  server: 198.41.221.12
  port: 2096
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_026
  type: vless
  server: 104.21.28.147
  port: 2083
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_027
  type: vless
  server: 198.41.209.150
  port: 8443
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_028
  type: vless
  server: 104.19.155.11
  port: 8443
  uuid: ffffffff-17ad-45e7-aaa1-f2baaa08e930
  tls: true
  servername: watashi.free.jppublic.moh539.link
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: watashi.free.jppublic.moh539.link
- name: 油管绵阿羊_None_vless_029
  type: vless
  server: 104.21.4.246
  port: 2083
  uuid: d342d11e-d424-4583-b36e-524ab1f0afa4
  tls: true
  servername: edgood.king361.cf
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: edgood.king361.cf
- name: 油管绵阿羊_None_vless_030
  type: vless
  server: 104.16.96.218
  port: 2087
  uuid: ffffffff-17ad-45e7-aaa1-f2baaa08e930
  tls: true
  servername: watashi.free.jppublic.moh539.link
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: watashi.free.jppublic.moh539.link
- name: 油管绵阿羊_United States_vless_031
  type: vless
  server: lilijuly.pp.ua
  port: 8443
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_032
  type: vless
  server: 104.17.208.174
  port: 8443
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_033
  type: vless
  server: 104.21.5.7
  port: 8443
  uuid: 73b6dbd5-a27a-4c76-9ad1-42a82380dddb
  tls: true
  servername: ed.ariesver.online
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: ed.ariesver.online
- name: 油管绵阿羊_None_vless_034
  type: vless
  server: 104.17.210.9
  port: 2083
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_035
  type: vless
  server: 104.21.2.0
  port: 8443
  uuid: 7fd7c15d-95cd-4f5c-bf59-f21e5eb27580
  tls: true
  servername: 3k.dabee.top
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: 3k.dabee.top
- name: 油管绵阿羊_None_vless_036
  type: vless
  server: 104.21.5.33
  port: 2083
  uuid: 73b6dbd5-a27a-4c76-9ad1-42a82380dddb
  tls: true
  servername: ed.ariesver.online
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: ed.ariesver.online
- name: 油管绵阿羊_None_vless_037
  type: vless
  server: 104.21.12.151
  port: 2087
  uuid: 7fd7c15d-95cd-4f5c-bf59-f21e5eb27580
  tls: true
  servername: 3k.dabee.top
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: 3k.dabee.top
- name: 油管绵阿羊_None_vless_038
  type: vless
  server: 104.21.12.84
  port: 443
  uuid: 7fd7c15d-95cd-4f5c-bf59-f21e5eb27580
  tls: true
  servername: 3k.dabee.top
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: 3k.dabee.top
- name: 油管绵阿羊_None_vless_039
  type: vless
  server: 104.17.219.151
  port: 8443
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_040
  type: vless
  server: 104.21.15.243
  port: 2096
  uuid: 73b6dbd5-a27a-4c76-9ad1-42a82380dddb
  tls: true
  servername: ed.ariesver.online
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: ed.ariesver.online
- name: 油管绵阿羊_United States_vless_041
  type: vless
  server: xwm-us-v6-a.mouboss.pp.ua
  port: 2083
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_United States_vless_042
  type: vless
  server: dvorda.pp.ua
  port: 2096
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_043
  type: vless
  server: 104.21.30.176
  port: 2096
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_044
  type: vless
  server: smi.pp.ua
  port: 8443
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_045
  type: vless
  server: 104.21.28.29
  port: 2053
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_046
  type: vless
  server: 104.16.96.197
  port: 2087
  uuid: ffffffff-17ad-45e7-aaa1-f2baaa08e930
  tls: true
  servername: watashi.free.jppublic.moh539.link
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: watashi.free.jppublic.moh539.link
- name: 油管绵阿羊_None_vless_047
  type: vless
  server: 104.16.96.54
  port: 8443
  uuid: ffffffff-17ad-45e7-aaa1-f2baaa08e930
  tls: true
  servername: watashi.free.jppublic.moh539.link
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: watashi.free.jppublic.moh539.link
- name: 油管绵阿羊_None_vless_048
  type: vless
  server: 198.41.221.195
  port: 2096
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_United States_vless_049
  type: vless
  server: jp7.vlessx.us
  port: 8443
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_050
  type: vless
  server: 104.21.17.152
  port: 2083
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_051
  type: vless
  server: 104.21.0.169
  port: 443
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_052
  type: vless
  server: 104.21.2.68
  port: 2087
  uuid: 7fd7c15d-95cd-4f5c-bf59-f21e5eb27580
  tls: true
  servername: 3k.dabee.top
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: 3k.dabee.top
- name: 油管绵阿羊_None_vless_053
  type: vless
  server: smi.pp.ua
  port: 2083
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_054
  type: vless
  server: 104.21.4.87
  port: 2083
  uuid: d342d11e-d424-4583-b36e-524ab1f0afa4
  tls: true
  servername: edgood.king361.cf
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: edgood.king361.cf
- name: 油管绵阿羊_None_vless_055
  type: vless
  server: 104.21.5.172
  port: 2053
  uuid: 73b6dbd5-a27a-4c76-9ad1-42a82380dddb
  tls: true
  servername: ed.ariesver.online
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: ed.ariesver.online
- name: 油管绵阿羊_None_vless_056
  type: vless
  server: 104.21.4.183
  port: 2087
  uuid: d342d11e-d424-4583-b36e-524ab1f0afa4
  tls: true
  servername: edgood.king361.cf
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: edgood.king361.cf
- name: 油管绵阿羊_United States_vless_057
  type: vless
  server: smi.pp.ua
  port: 443
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_058
  type: vless
  server: 104.21.1.138
  port: 2087
  uuid: ffffffff-17ad-45e7-aaa1-f2baaa08e930
  tls: true
  servername: watashi.free.jppublic.moh539.link
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: watashi.free.jppublic.moh539.link
- name: 油管绵阿羊_None_vless_059
  type: vless
  server: 104.18.190.52
  port: 443
  uuid: a4faf5d8-b9a8-433e-9518-2d2e21d76f78
  tls: true
  servername: nginx.nirevil.ir
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: nginx.nirevil.ir
- name: 油管绵阿羊_None_vless_060
  type: vless
  server: 198.41.208.156
  port: 2087
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_061
  type: vless
  server: 104.21.0.152
  port: 2053
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_United States_vless_062
  type: vless
  server: a.noonokorean.pp.ua
  port: 2096
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_063
  type: vless
  server: 104.21.16.238
  port: 443
  uuid: ffffffff-17ad-45e7-aaa1-f2baaa08e930
  tls: true
  servername: watashi.free.jppublic.moh539.link
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: watashi.free.jppublic.moh539.link
- name: 油管绵阿羊_None_vless_064
  type: vless
  server: 104.21.1.250
  port: 8443
  uuid: ffffffff-17ad-45e7-aaa1-f2baaa08e930
  tls: true
  servername: watashi.free.jppublic.moh539.link
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: watashi.free.jppublic.moh539.link
- name: 油管绵阿羊_None_vless_065
  type: vless
  server: 104.21.26.225
  port: 2083
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_066
  type: vless
  server: 104.17.209.149
  port: 2083
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_067
  type: vless
  server: us10.vlessx.us
  port: 8443
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_068
  type: vless
  server: 104.21.26.230
  port: 8443
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_069
  type: vless
  server: 104.21.28.62
  port: 443
  uuid: b9ad895b-12ac-40fc-a5ac-a5b2a1285001
  tls: true
  servername: 3k.pureboy.eu.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: 3k.pureboy.eu.org
- name: 油管绵阿羊_None_vless_070
  type: vless
  server: 104.21.2.96
  port: 2087
  uuid: 7fd7c15d-95cd-4f5c-bf59-f21e5eb27580
  tls: true
  servername: 3k.dabee.top
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: 3k.dabee.top
- name: 油管绵阿羊_None_vless_071
  type: vless
  server: 104.21.14.245
  port: 2087
  uuid: d342d11e-d424-4583-b36e-524ab1f0afa4
  tls: true
  servername: edgood.king361.cf
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: edgood.king361.cf
- name: 油管绵阿羊_None_vless_072
  type: vless
  server: 104.21.15.55
  port: 2083
  uuid: 73b6dbd5-a27a-4c76-9ad1-42a82380dddb
  tls: true
  servername: ed.ariesver.online
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: ed.ariesver.online
- name: 油管绵阿羊_None_vless_073
  type: vless
  server: 198.41.221.173
  port: 2087
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_074
  type: vless
  server: 104.21.15.226
  port: 2087
  uuid: 73b6dbd5-a27a-4c76-9ad1-42a82380dddb
  tls: true
  servername: ed.ariesver.online
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: ed.ariesver.online
- name: 油管绵阿羊_None_vless_075
  type: vless
  server: 104.21.2.173
  port: 2096
  uuid: 7fd7c15d-95cd-4f5c-bf59-f21e5eb27580
  tls: true
  servername: 3k.dabee.top
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: 3k.dabee.top
- name: 油管绵阿羊_United States_vless_076
  type: vless
  server: ctwct.arvancode.eu.org
  port: 2096
  uuid: f4cec6cc-6177-423c-90f8-2ad9f0dd996b
  tls: true
  servername: vpnct.arvancode.eu.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: vpnct.arvancode.eu.org
- name: 油管绵阿羊_None_vless_077
  type: vless
  server: 104.21.0.177
  port: 2053
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_United States_vless_078
  type: vless
  server: jgw.wshyx.pp.ua
  port: 2083
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_079
  type: vless
  server: 104.21.24.7
  port: 8443
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_None_vless_080
  type: vless
  server: 104.21.2.219
  port: 2096
  uuid: 7fd7c15d-95cd-4f5c-bf59-f21e5eb27580
  tls: true
  servername: 3k.dabee.top
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: 3k.dabee.top
- name: 油管绵阿羊_None_vless_081
  type: vless
  server: 104.21.15.243
  port: 2053
  uuid: 73b6dbd5-a27a-4c76-9ad1-42a82380dddb
  tls: true
  servername: ed.ariesver.online
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: ed.ariesver.online
- name: 油管绵阿羊_None_vless_082
  type: vless
  server: 104.21.1.147
  port: 2053
  uuid: ffffffff-17ad-45e7-aaa1-f2baaa08e930
  tls: true
  servername: watashi.free.jppublic.moh539.link
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: watashi.free.jppublic.moh539.link
- name: 油管绵阿羊_None_vless_083
  type: vless
  server: 104.21.12.140
  port: 2053
  uuid: 7fd7c15d-95cd-4f5c-bf59-f21e5eb27580
  tls: true
  servername: 3k.dabee.top
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: 3k.dabee.top
- name: 油管绵阿羊_None_vless_084
  type: vless
  server: 198.41.209.180
  port: 2053
  uuid: 875e0c54-2690-4bfb-a4e5-d44bcf9d2a31
  tls: true
  servername: kyd.cloudns.org
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: kyd.cloudns.org
- name: 油管绵阿羊_United States_vless_085
  type: vless
  server: tz.lilijuly.pp.ua
  port: 2083
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_United States_vless_086
  type: vless
  server: i.noonokorean.pp.ua
  port: 2096
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_United States_vless_087
  type: vless
  server: 88888.pp.ua
  port: 2087
  uuid: 60813b9d-aa0e-4a5c-88b8-ed231058e82a
  tls: true
  servername: pages.20230619.love
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: pages.20230619.love
- name: 油管绵阿羊_None_vless_088
  type: vless
  server: 104.21.1.179
  port: 2096
  uuid: ffffffff-17ad-45e7-aaa1-f2baaa08e930
  tls: true
  servername: watashi.free.jppublic.moh539.link
  network: ws
  ws-opts:
    path: Twitter苏小柠
    headers:
      host: watashi.free.jppublic.moh539.link
- name: 油管绵阿羊_Taiwan_tuic_11
  type: tuic
  server: 111.243.97.2
  port: 33098
  udp: true
  uuid: fef3d3c2-ab3e-4134-a2f3-0c2d83e0a76d
  password: dongtaiwang.com
  alpn:
  - h3
  disable-sni: true
  reduce-rtt: true
  udp-relay-mode: native
  congestion-controller: bbr
- name: 油管绵阿羊_None_vmess_21
  type: vmess
  server: www.darkroom.lol
  port: 8080
  cipher: auto
  uuid: 22826b44-5c1a-4b4b-dbaa-83a2e8bd95f0
  alterId: 0
  tls: false
  skip-cert-verify: true
  network: ws
  ws-opts:
    path: /
    headers:
      host: www.darkroom.lol
- name: 油管绵阿羊_China_vmess_22
  type: vmess
  server: data-us-v1.shwjfkw.cn
  port: 20401
  cipher: auto
  uuid: b1478e24-4916-3abe-8f17-15931012ecbe
  alterId: 0
  tls: false
  skip-cert-verify: true
  network: ws
  ws-opts:
    path: /debian
    headers:
      host: data-us-v1.shwjfkw.cn
- name: 油管绵阿羊_China_ss_23
  type: ss
  server: service.ouluyun9803.com
  port: 20003
  password: d6105bbd-be0d-45b2-82ad-31fd1071c1d2
  cipher: chacha20-ietf-poly1305
- name: 油管绵阿羊_None_vmess_24
  type: vmess
  server: 104.21.82.183
  port: 8880
  cipher: auto
  uuid: 5a7021e0-26b4-45d6-b175-fe551601ca97
  alterId: 0
  tls: false
  skip-cert-verify: true
  network: ws
  ws-opts:
    path: /
    headers:
      host: server26.beheshtbaneh.com
- name: 油管绵阿羊_China_ss_25
  type: ss
  server: service.ouluyun9803.com
  port: 20005
  password: d6105bbd-be0d-45b2-82ad-31fd1071c1d2
  cipher: chacha20-ietf-poly1305
- name: 油管绵阿羊_United States_vmess_31
  type: vmess
  server: www.darkroom.lol
  port: 8080
  cipher: auto
  uuid: 22826b44-5c1a-4b4b-dbaa-83a2e8bd95f0
  alterId: 0
  tls: false
  skip-cert-verify: true
  network: ws
  ws-opts:
    path: /
    headers:
      host: www.darkroom.lol
- name: 油管绵阿羊_China_vmess_32
  type: vmess
  server: data-us-v1.shwjfkw.cn
  port: 20401
  cipher: auto
  uuid: b1478e24-4916-3abe-8f17-15931012ecbe
  alterId: 0
  tls: false
  skip-cert-verify: true
  network: ws
  ws-opts:
    path: /debian
    headers:
      host: data-us-v1.shwjfkw.cn
- name: 油管绵阿羊_China_ss_33
  type: ss
  server: service.ouluyun9803.com
  port: 20003
  password: d6105bbd-be0d-45b2-82ad-31fd1071c1d2
  cipher: chacha20-ietf-poly1305
- name: 油管绵阿羊_None_vmess_34
  type: vmess
  server: 104.21.82.183
  port: 8880
  cipher: auto
  uuid: 5a7021e0-26b4-45d6-b175-fe551601ca97
  alterId: 0
  tls: false
  skip-cert-verify: true
  network: ws
  ws-opts:
    path: /
    headers:
      host: server26.beheshtbaneh.com
- name: 油管绵阿羊_China_ss_35
  type: ss
  server: service.ouluyun9803.com
  port: 20005
  password: d6105bbd-be0d-45b2-82ad-31fd1071c1d2
  cipher: chacha20-ietf-poly1305
- name: 油管绵阿羊_United States_vmess_41
  type: vmess
  server: www.darkroom.lol
  port: 8080
  cipher: auto
  uuid: 22826b44-5c1a-4b4b-dbaa-83a2e8bd95f0
  alterId: 0
  tls: false
  skip-cert-verify: true
  network: ws
  ws-opts:
    path: /
    headers:
      host: www.darkroom.lol
- name: 油管绵阿羊_China_vmess_42
  type: vmess
  server: data-us-v1.shwjfkw.cn
  port: 20401
  cipher: auto
  uuid: b1478e24-4916-3abe-8f17-15931012ecbe
  alterId: 0
  tls: false
  skip-cert-verify: true
  network: ws
  ws-opts:
    path: /debian
    headers:
      host: data-us-v1.shwjfkw.cn
- name: 油管绵阿羊_China_ss_43
  type: ss
  server: service.ouluyun9803.com
  port: 20003
  password: d6105bbd-be0d-45b2-82ad-31fd1071c1d2
  cipher: chacha20-ietf-poly1305
- name: 油管绵阿羊_None_vmess_44
  type: vmess
  server: 104.21.82.183
  port: 8880
  cipher: auto
  uuid: 5a7021e0-26b4-45d6-b175-fe551601ca97
  alterId: 0
  tls: false
  skip-cert-verify: true
  network: ws
  ws-opts:
    path: /
    headers:
      host: server26.beheshtbaneh.com
- name: 油管绵阿羊_China_ss_45
  type: ss
  server: service.ouluyun9803.com
  port: 20005
  password: d6105bbd-be0d-45b2-82ad-31fd1071c1d2
  cipher: chacha20-ietf-poly1305
- name: 油管绵阿羊_United States_vmess_51
  type: vmess
  server: www.darkroom.lol
  port: 8080
  cipher: auto
  uuid: 22826b44-5c1a-4b4b-dbaa-83a2e8bd95f0
  alterId: 0
  tls: false
  skip-cert-verify: true
  network: ws
  ws-opts:
    path: /
    headers:
      host: www.darkroom.lol
- name: 油管绵阿羊_China_vmess_52
  type: vmess
  server: data-us-v1.shwjfkw.cn
  port: 20401
  cipher: auto
  uuid: b1478e24-4916-3abe-8f17-15931012ecbe
  alterId: 0
  tls: false
  skip-cert-verify: true
  network: ws
  ws-opts:
    path: /debian
    headers:
      host: data-us-v1.shwjfkw.cn
- name: 油管绵阿羊_China_ss_53
  type: ss
  server: service.ouluyun9803.com
  port: 20003
  password: d6105bbd-be0d-45b2-82ad-31fd1071c1d2
  cipher: chacha20-ietf-poly1305
- name: 油管绵阿羊_None_vmess_54
  type: vmess
  server: 104.21.82.183
  port: 8880
  cipher: auto
  uuid: 5a7021e0-26b4-45d6-b175-fe551601ca97
  alterId: 0
  tls: false
  skip-cert-verify: true
  network: ws
  ws-opts:
    path: /
    headers:
      host: server26.beheshtbaneh.com
- name: 油管绵阿羊_China_ss_55
  type: ss
  server: service.ouluyun9803.com
  port: 20005
  password: d6105bbd-be0d-45b2-82ad-31fd1071c1d2
  cipher: chacha20-ietf-poly1305
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
- name: 油管绵阿羊_Taiwan_hysteria_81
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
- name: 油管绵阿羊_United States_hy_2
  type: hysteria
  server: 108.181.22.239
  port: 39967
  ports: 39967
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
- name: 油管绵阿羊_United States_hy2_3
  type: hysteria2
  server: 108.181.24.77
  port: 43656
  password: dongtaiwang.com
  fast-open: true
  sni: www.bing.com
  skip-cert-verify: true
- name: 油管绵阿羊_United States_reality_1
  type: vless
  server: 108.181.22.213
  port: 28945
  uuid: 9cc39477-0d85-4419-84d4-fb7fc77668b3
  network: tcp
  tls: true
  udp: true
  flow: xtls-rprx-vision
  client-fingerprint: chrome
  servername: m.media-amazon.com
  reality-opts:
    public-key: yKXmLTmXAi-BHBg3JpCz-NWUmVcKlfm7iMmVoq7YQx0
    short-id: 6ba85179e30d4fc2
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
  - 油管绵阿羊_None_vless_01
  - 油管绵阿羊_South Korea_vless_02
  - 油管绵阿羊_None_vless_03
  - 油管绵阿羊_None_vless_04
  - 油管绵阿羊_None_vless_05
  - 油管绵阿羊_None_vless_06
  - 油管绵阿羊_None_vless_07
  - 油管绵阿羊_None_vless_08
  - 油管绵阿羊_Japan_vless_09
  - 油管绵阿羊_None_vless_010
  - 油管绵阿羊_Singapore_vless_011
  - 油管绵阿羊_None_vless_012
  - 油管绵阿羊_None_vless_013
  - 油管绵阿羊_None_vless_014
  - 油管绵阿羊_None_vless_015
  - 油管绵阿羊_None_vless_016
  - 油管绵阿羊_None_vless_017
  - 油管绵阿羊_None_vless_018
  - 油管绵阿羊_None_vless_019
  - 油管绵阿羊_None_vless_020
  - 油管绵阿羊_None_vless_021
  - 油管绵阿羊_None_vless_022
  - 油管绵阿羊_None_vless_023
  - 油管绵阿羊_United States_vless_024
  - 油管绵阿羊_None_vless_025
  - 油管绵阿羊_None_vless_026
  - 油管绵阿羊_None_vless_027
  - 油管绵阿羊_None_vless_028
  - 油管绵阿羊_None_vless_029
  - 油管绵阿羊_None_vless_030
  - 油管绵阿羊_United States_vless_031
  - 油管绵阿羊_None_vless_032
  - 油管绵阿羊_None_vless_033
  - 油管绵阿羊_None_vless_034
  - 油管绵阿羊_None_vless_035
  - 油管绵阿羊_None_vless_036
  - 油管绵阿羊_None_vless_037
  - 油管绵阿羊_None_vless_038
  - 油管绵阿羊_None_vless_039
  - 油管绵阿羊_None_vless_040
  - 油管绵阿羊_United States_vless_041
  - 油管绵阿羊_United States_vless_042
  - 油管绵阿羊_None_vless_043
  - 油管绵阿羊_None_vless_044
  - 油管绵阿羊_None_vless_045
  - 油管绵阿羊_None_vless_046
  - 油管绵阿羊_None_vless_047
  - 油管绵阿羊_None_vless_048
  - 油管绵阿羊_United States_vless_049
  - 油管绵阿羊_None_vless_050
  - 油管绵阿羊_None_vless_051
  - 油管绵阿羊_None_vless_052
  - 油管绵阿羊_None_vless_053
  - 油管绵阿羊_None_vless_054
  - 油管绵阿羊_None_vless_055
  - 油管绵阿羊_None_vless_056
  - 油管绵阿羊_United States_vless_057
  - 油管绵阿羊_None_vless_058
  - 油管绵阿羊_None_vless_059
  - 油管绵阿羊_None_vless_060
  - 油管绵阿羊_None_vless_061
  - 油管绵阿羊_United States_vless_062
  - 油管绵阿羊_None_vless_063
  - 油管绵阿羊_None_vless_064
  - 油管绵阿羊_None_vless_065
  - 油管绵阿羊_None_vless_066
  - 油管绵阿羊_None_vless_067
  - 油管绵阿羊_None_vless_068
  - 油管绵阿羊_None_vless_069
  - 油管绵阿羊_None_vless_070
  - 油管绵阿羊_None_vless_071
  - 油管绵阿羊_None_vless_072
  - 油管绵阿羊_None_vless_073
  - 油管绵阿羊_None_vless_074
  - 油管绵阿羊_None_vless_075
  - 油管绵阿羊_United States_vless_076
  - 油管绵阿羊_None_vless_077
  - 油管绵阿羊_United States_vless_078
  - 油管绵阿羊_None_vless_079
  - 油管绵阿羊_None_vless_080
  - 油管绵阿羊_None_vless_081
  - 油管绵阿羊_None_vless_082
  - 油管绵阿羊_None_vless_083
  - 油管绵阿羊_None_vless_084
  - 油管绵阿羊_United States_vless_085
  - 油管绵阿羊_United States_vless_086
  - 油管绵阿羊_United States_vless_087
  - 油管绵阿羊_None_vless_088
  - 油管绵阿羊_Taiwan_tuic_11
  - 油管绵阿羊_None_vmess_21
  - 油管绵阿羊_China_vmess_22
  - 油管绵阿羊_China_ss_23
  - 油管绵阿羊_None_vmess_24
  - 油管绵阿羊_China_ss_25
  - 油管绵阿羊_United States_vmess_31
  - 油管绵阿羊_China_vmess_32
  - 油管绵阿羊_China_ss_33
  - 油管绵阿羊_None_vmess_34
  - 油管绵阿羊_China_ss_35
  - 油管绵阿羊_United States_vmess_41
  - 油管绵阿羊_China_vmess_42
  - 油管绵阿羊_China_ss_43
  - 油管绵阿羊_None_vmess_44
  - 油管绵阿羊_China_ss_45
  - 油管绵阿羊_United States_vmess_51
  - 油管绵阿羊_China_vmess_52
  - 油管绵阿羊_China_ss_53
  - 油管绵阿羊_None_vmess_54
  - 油管绵阿羊_China_ss_55
  - 油管绵阿羊_Taiwan_hysteria_61
  - 油管绵阿羊_France_hysteria2_71
  - 油管绵阿羊_Taiwan_hysteria_81
  - 油管绵阿羊_Taiwan_hysteria_91
  - 油管绵阿羊_France_hy_0
  - 油管绵阿羊_United States_hy_1
  - 油管绵阿羊_United States_hy_2
  - 油管绵阿羊_United States_hy_3
  - 油管绵阿羊_France_hy2_0
  - 油管绵阿羊_United States_hy2_1
  - 油管绵阿羊_France_hy2_2
  - 油管绵阿羊_United States_hy2_3
  - 油管绵阿羊_United States_reality_1
  - 油管绵阿羊_France_reality_2
  - 油管绵阿羊_France_reality_3
- name: 手动选择
  type: select
  proxies:
  - 油管绵阿羊_None_vless_01
  - 油管绵阿羊_South Korea_vless_02
  - 油管绵阿羊_None_vless_03
  - 油管绵阿羊_None_vless_04
  - 油管绵阿羊_None_vless_05
  - 油管绵阿羊_None_vless_06
  - 油管绵阿羊_None_vless_07
  - 油管绵阿羊_None_vless_08
  - 油管绵阿羊_Japan_vless_09
  - 油管绵阿羊_None_vless_010
  - 油管绵阿羊_Singapore_vless_011
  - 油管绵阿羊_None_vless_012
  - 油管绵阿羊_None_vless_013
  - 油管绵阿羊_None_vless_014
  - 油管绵阿羊_None_vless_015
  - 油管绵阿羊_None_vless_016
  - 油管绵阿羊_None_vless_017
  - 油管绵阿羊_None_vless_018
  - 油管绵阿羊_None_vless_019
  - 油管绵阿羊_None_vless_020
  - 油管绵阿羊_None_vless_021
  - 油管绵阿羊_None_vless_022
  - 油管绵阿羊_None_vless_023
  - 油管绵阿羊_United States_vless_024
  - 油管绵阿羊_None_vless_025
  - 油管绵阿羊_None_vless_026
  - 油管绵阿羊_None_vless_027
  - 油管绵阿羊_None_vless_028
  - 油管绵阿羊_None_vless_029
  - 油管绵阿羊_None_vless_030
  - 油管绵阿羊_United States_vless_031
  - 油管绵阿羊_None_vless_032
  - 油管绵阿羊_None_vless_033
  - 油管绵阿羊_None_vless_034
  - 油管绵阿羊_None_vless_035
  - 油管绵阿羊_None_vless_036
  - 油管绵阿羊_None_vless_037
  - 油管绵阿羊_None_vless_038
  - 油管绵阿羊_None_vless_039
  - 油管绵阿羊_None_vless_040
  - 油管绵阿羊_United States_vless_041
  - 油管绵阿羊_United States_vless_042
  - 油管绵阿羊_None_vless_043
  - 油管绵阿羊_None_vless_044
  - 油管绵阿羊_None_vless_045
  - 油管绵阿羊_None_vless_046
  - 油管绵阿羊_None_vless_047
  - 油管绵阿羊_None_vless_048
  - 油管绵阿羊_United States_vless_049
  - 油管绵阿羊_None_vless_050
  - 油管绵阿羊_None_vless_051
  - 油管绵阿羊_None_vless_052
  - 油管绵阿羊_None_vless_053
  - 油管绵阿羊_None_vless_054
  - 油管绵阿羊_None_vless_055
  - 油管绵阿羊_None_vless_056
  - 油管绵阿羊_United States_vless_057
  - 油管绵阿羊_None_vless_058
  - 油管绵阿羊_None_vless_059
  - 油管绵阿羊_None_vless_060
  - 油管绵阿羊_None_vless_061
  - 油管绵阿羊_United States_vless_062
  - 油管绵阿羊_None_vless_063
  - 油管绵阿羊_None_vless_064
  - 油管绵阿羊_None_vless_065
  - 油管绵阿羊_None_vless_066
  - 油管绵阿羊_None_vless_067
  - 油管绵阿羊_None_vless_068
  - 油管绵阿羊_None_vless_069
  - 油管绵阿羊_None_vless_070
  - 油管绵阿羊_None_vless_071
  - 油管绵阿羊_None_vless_072
  - 油管绵阿羊_None_vless_073
  - 油管绵阿羊_None_vless_074
  - 油管绵阿羊_None_vless_075
  - 油管绵阿羊_United States_vless_076
  - 油管绵阿羊_None_vless_077
  - 油管绵阿羊_United States_vless_078
  - 油管绵阿羊_None_vless_079
  - 油管绵阿羊_None_vless_080
  - 油管绵阿羊_None_vless_081
  - 油管绵阿羊_None_vless_082
  - 油管绵阿羊_None_vless_083
  - 油管绵阿羊_None_vless_084
  - 油管绵阿羊_United States_vless_085
  - 油管绵阿羊_United States_vless_086
  - 油管绵阿羊_United States_vless_087
  - 油管绵阿羊_None_vless_088
  - 油管绵阿羊_Taiwan_tuic_11
  - 油管绵阿羊_None_vmess_21
  - 油管绵阿羊_China_vmess_22
  - 油管绵阿羊_China_ss_23
  - 油管绵阿羊_None_vmess_24
  - 油管绵阿羊_China_ss_25
  - 油管绵阿羊_United States_vmess_31
  - 油管绵阿羊_China_vmess_32
  - 油管绵阿羊_China_ss_33
  - 油管绵阿羊_None_vmess_34
  - 油管绵阿羊_China_ss_35
  - 油管绵阿羊_United States_vmess_41
  - 油管绵阿羊_China_vmess_42
  - 油管绵阿羊_China_ss_43
  - 油管绵阿羊_None_vmess_44
  - 油管绵阿羊_China_ss_45
  - 油管绵阿羊_United States_vmess_51
  - 油管绵阿羊_China_vmess_52
  - 油管绵阿羊_China_ss_53
  - 油管绵阿羊_None_vmess_54
  - 油管绵阿羊_China_ss_55
  - 油管绵阿羊_Taiwan_hysteria_61
  - 油管绵阿羊_France_hysteria2_71
  - 油管绵阿羊_Taiwan_hysteria_81
  - 油管绵阿羊_Taiwan_hysteria_91
  - 油管绵阿羊_France_hy_0
  - 油管绵阿羊_United States_hy_1
  - 油管绵阿羊_United States_hy_2
  - 油管绵阿羊_United States_hy_3
  - 油管绵阿羊_France_hy2_0
  - 油管绵阿羊_United States_hy2_1
  - 油管绵阿羊_France_hy2_2
  - 油管绵阿羊_United States_hy2_3
  - 油管绵阿羊_United States_reality_1
  - 油管绵阿羊_France_reality_2
  - 油管绵阿羊_France_reality_3
- name: 负载均衡
  type: load-balance
  proxies:
  - 油管绵阿羊_None_vless_01
  - 油管绵阿羊_South Korea_vless_02
  - 油管绵阿羊_None_vless_03
  - 油管绵阿羊_None_vless_04
  - 油管绵阿羊_None_vless_05
  - 油管绵阿羊_None_vless_06
  - 油管绵阿羊_None_vless_07
  - 油管绵阿羊_None_vless_08
  - 油管绵阿羊_Japan_vless_09
  - 油管绵阿羊_None_vless_010
  - 油管绵阿羊_Singapore_vless_011
  - 油管绵阿羊_None_vless_012
  - 油管绵阿羊_None_vless_013
  - 油管绵阿羊_None_vless_014
  - 油管绵阿羊_None_vless_015
  - 油管绵阿羊_None_vless_016
  - 油管绵阿羊_None_vless_017
  - 油管绵阿羊_None_vless_018
  - 油管绵阿羊_None_vless_019
  - 油管绵阿羊_None_vless_020
  - 油管绵阿羊_None_vless_021
  - 油管绵阿羊_None_vless_022
  - 油管绵阿羊_None_vless_023
  - 油管绵阿羊_United States_vless_024
  - 油管绵阿羊_None_vless_025
  - 油管绵阿羊_None_vless_026
  - 油管绵阿羊_None_vless_027
  - 油管绵阿羊_None_vless_028
  - 油管绵阿羊_None_vless_029
  - 油管绵阿羊_None_vless_030
  - 油管绵阿羊_United States_vless_031
  - 油管绵阿羊_None_vless_032
  - 油管绵阿羊_None_vless_033
  - 油管绵阿羊_None_vless_034
  - 油管绵阿羊_None_vless_035
  - 油管绵阿羊_None_vless_036
  - 油管绵阿羊_None_vless_037
  - 油管绵阿羊_None_vless_038
  - 油管绵阿羊_None_vless_039
  - 油管绵阿羊_None_vless_040
  - 油管绵阿羊_United States_vless_041
  - 油管绵阿羊_United States_vless_042
  - 油管绵阿羊_None_vless_043
  - 油管绵阿羊_None_vless_044
  - 油管绵阿羊_None_vless_045
  - 油管绵阿羊_None_vless_046
  - 油管绵阿羊_None_vless_047
  - 油管绵阿羊_None_vless_048
  - 油管绵阿羊_United States_vless_049
  - 油管绵阿羊_None_vless_050
  - 油管绵阿羊_None_vless_051
  - 油管绵阿羊_None_vless_052
  - 油管绵阿羊_None_vless_053
  - 油管绵阿羊_None_vless_054
  - 油管绵阿羊_None_vless_055
  - 油管绵阿羊_None_vless_056
  - 油管绵阿羊_United States_vless_057
  - 油管绵阿羊_None_vless_058
  - 油管绵阿羊_None_vless_059
  - 油管绵阿羊_None_vless_060
  - 油管绵阿羊_None_vless_061
  - 油管绵阿羊_United States_vless_062
  - 油管绵阿羊_None_vless_063
  - 油管绵阿羊_None_vless_064
  - 油管绵阿羊_None_vless_065
  - 油管绵阿羊_None_vless_066
  - 油管绵阿羊_None_vless_067
  - 油管绵阿羊_None_vless_068
  - 油管绵阿羊_None_vless_069
  - 油管绵阿羊_None_vless_070
  - 油管绵阿羊_None_vless_071
  - 油管绵阿羊_None_vless_072
  - 油管绵阿羊_None_vless_073
  - 油管绵阿羊_None_vless_074
  - 油管绵阿羊_None_vless_075
  - 油管绵阿羊_United States_vless_076
  - 油管绵阿羊_None_vless_077
  - 油管绵阿羊_United States_vless_078
  - 油管绵阿羊_None_vless_079
  - 油管绵阿羊_None_vless_080
  - 油管绵阿羊_None_vless_081
  - 油管绵阿羊_None_vless_082
  - 油管绵阿羊_None_vless_083
  - 油管绵阿羊_None_vless_084
  - 油管绵阿羊_United States_vless_085
  - 油管绵阿羊_United States_vless_086
  - 油管绵阿羊_United States_vless_087
  - 油管绵阿羊_None_vless_088
  - 油管绵阿羊_Taiwan_tuic_11
  - 油管绵阿羊_None_vmess_21
  - 油管绵阿羊_China_vmess_22
  - 油管绵阿羊_China_ss_23
  - 油管绵阿羊_None_vmess_24
  - 油管绵阿羊_China_ss_25
  - 油管绵阿羊_United States_vmess_31
  - 油管绵阿羊_China_vmess_32
  - 油管绵阿羊_China_ss_33
  - 油管绵阿羊_None_vmess_34
  - 油管绵阿羊_China_ss_35
  - 油管绵阿羊_United States_vmess_41
  - 油管绵阿羊_China_vmess_42
  - 油管绵阿羊_China_ss_43
  - 油管绵阿羊_None_vmess_44
  - 油管绵阿羊_China_ss_45
  - 油管绵阿羊_United States_vmess_51
  - 油管绵阿羊_China_vmess_52
  - 油管绵阿羊_China_ss_53
  - 油管绵阿羊_None_vmess_54
  - 油管绵阿羊_China_ss_55
  - 油管绵阿羊_Taiwan_hysteria_61
  - 油管绵阿羊_France_hysteria2_71
  - 油管绵阿羊_Taiwan_hysteria_81
  - 油管绵阿羊_Taiwan_hysteria_91
  - 油管绵阿羊_France_hy_0
  - 油管绵阿羊_United States_hy_1
  - 油管绵阿羊_United States_hy_2
  - 油管绵阿羊_United States_hy_3
  - 油管绵阿羊_France_hy2_0
  - 油管绵阿羊_United States_hy2_1
  - 油管绵阿羊_France_hy2_2
  - 油管绵阿羊_United States_hy2_3
  - 油管绵阿羊_United States_reality_1
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
dmxlc3M6Ly84NzVlMGM1NC0yNjkwLTRiZmItYTRlNS1kNDRiY2Y5ZDJhMzFAMTk4LjQxLjIyMC4xNzY6MjA4Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1reWQuY2xvdWRucy5vcmcmc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNOb25lX3ZsZXNzXzAKdmxlc3M6Ly82MDgxM2I5ZC1hYTBlLTRhNWMtODhiOC1lZDIzMTA1OGU4MmFAaGswMy5udHRray5jb206NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPXBhZ2VzLjIwMjMwNjE5LmxvdmUmc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNTb3V0aCBLb3JlYV92bGVzc18wCnZsZXNzOi8vODc1ZTBjNTQtMjY5MC00YmZiLWE0ZTUtZDQ0YmNmOWQyYTMxQDEwNC4xNy4yMDguMTc3OjIwOTY/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9a3lkLmNsb3VkbnMub3JnJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vODc1ZTBjNTQtMjY5MC00YmZiLWE0ZTUtZDQ0YmNmOWQyYTMxQDEwNC4xNy4yMTMuNToyMDgzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWt5ZC5jbG91ZG5zLm9yZyZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovLzg3NWUwYzU0LTI2OTAtNGJmYi1hNGU1LWQ0NGJjZjlkMmEzMUAxMDQuMTcuMjIzLjE2MToyMDgzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWt5ZC5jbG91ZG5zLm9yZyZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovL2ZmZmZmZmZmLTE3YWQtNDVlNy1hYWExLWYyYmFhYTA4ZTkzMEAxMDQuMTkuMTU1LjEwNToyMDgzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPXdhdGFzaGkuZnJlZS5qcHB1YmxpYy5tb2g1MzkubGluayZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovLzg3NWUwYzU0LTI2OTAtNGJmYi1hNGU1LWQ0NGJjZjlkMmEzMUAxMDQuMTcuMjEwLjEzMToyMDg3P3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWt5ZC5jbG91ZG5zLm9yZyZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovLzg3NWUwYzU0LTI2OTAtNGJmYi1hNGU1LWQ0NGJjZjlkMmEzMUAxMDQuMTcuMjEyLjIzOTo4NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWt5ZC5jbG91ZG5zLm9yZyZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovLzYwODEzYjlkLWFhMGUtNGE1Yy04OGI4LWVkMjMxMDU4ZTgyYUA0My4xNTMuMTgxLjIxNzo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9cGFnZXMuMjAyMzA2MTkubG92ZSZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I0phcGFuX3ZsZXNzXzAKdmxlc3M6Ly9mZmZmZmZmZi0xN2FkLTQ1ZTctYWFhMS1mMmJhYWEwOGU5MzBAMTA0LjE2Ljk2LjgyOjg0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9d2F0YXNoaS5mcmVlLmpwcHVibGljLm1vaDUzOS5saW5rJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vZDM0MmQxMWUtZDQyNC00NTgzLWIzNmUtNTI0YWIxZjBhZmE0QDM1LjI0Ny4xNzUuMTIwOjQ4NTk3P3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWJhaXBpYW8zNDMuc3R1bm5pbmctYmFzc29vbi5wYWdlcy5kZXYmc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNTaW5nYXBvcmVfdmxlc3NfMAp2bGVzczovLzg3NWUwYzU0LTI2OTAtNGJmYi1hNGU1LWQ0NGJjZjlkMmEzMUAxMDQuMTcuMjE1LjI0MTo4NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWt5ZC5jbG91ZG5zLm9yZyZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovLzg3NWUwYzU0LTI2OTAtNGJmYi1hNGU1LWQ0NGJjZjlkMmEzMUAxMDQuMTcuMjE0LjM5Ojg0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9a3lkLmNsb3VkbnMub3JnJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vODc1ZTBjNTQtMjY5MC00YmZiLWE0ZTUtZDQ0YmNmOWQyYTMxQDE5OC40MS4yMjAuMTU4OjIwODc/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9a3lkLmNsb3VkbnMub3JnJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vODc1ZTBjNTQtMjY5MC00YmZiLWE0ZTUtZDQ0YmNmOWQyYTMxQDEwNC4xNy4yMTAuMTI4OjIwODM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9a3lkLmNsb3VkbnMub3JnJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vODc1ZTBjNTQtMjY5MC00YmZiLWE0ZTUtZDQ0YmNmOWQyYTMxQDEwNC4yMS4zMC4xNzg6MjA4Nz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1reWQuY2xvdWRucy5vcmcmc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNOb25lX3ZsZXNzXzAKdmxlc3M6Ly84NzVlMGM1NC0yNjkwLTRiZmItYTRlNS1kNDRiY2Y5ZDJhMzFAMTA0LjE3LjIxMC4xMzg6MjA5Nj9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1reWQuY2xvdWRucy5vcmcmc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNOb25lX3ZsZXNzXzAKdmxlc3M6Ly84NzVlMGM1NC0yNjkwLTRiZmItYTRlNS1kNDRiY2Y5ZDJhMzFAMTk4LjQxLjIyMS44MDoyMDgzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWt5ZC5jbG91ZG5zLm9yZyZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovLzg3NWUwYzU0LTI2OTAtNGJmYi1hNGU1LWQ0NGJjZjlkMmEzMUAxOTguNDEuMjIxLjIzNzo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9a3lkLmNsb3VkbnMub3JnJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vNjA4MTNiOWQtYWEwZS00YTVjLTg4YjgtZWQyMzEwNThlODJhQDEwNC4yMS4xNy4xNTE6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPXBhZ2VzLjIwMjMwNjE5LmxvdmUmc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNOb25lX3ZsZXNzXzAKdmxlc3M6Ly84NzVlMGM1NC0yNjkwLTRiZmItYTRlNS1kNDRiY2Y5ZDJhMzFAMTA0LjE3LjIyMS4yMjY6MjA5Nj9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1reWQuY2xvdWRucy5vcmcmc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNOb25lX3ZsZXNzXzAKdmxlc3M6Ly82MDgxM2I5ZC1hYTBlLTRhNWMtODhiOC1lZDIzMTA1OGU4MmFAMTA0LjIxLjAuMjM2Ojg0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9cGFnZXMuMjAyMzA2MTkubG92ZSZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovLzg3NWUwYzU0LTI2OTAtNGJmYi1hNGU1LWQ0NGJjZjlkMmEzMUAxMDQuMTcuMjE5LjM1OjIwOTY/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9a3lkLmNsb3VkbnMub3JnJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vNjA4MTNiOWQtYWEwZS00YTVjLTg4YjgtZWQyMzEwNThlODJhQGpndy53c2h5eC5wcC51YToyMDg3P3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPXBhZ2VzLjIwMjMwNjE5LmxvdmUmc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNVbml0ZWQgU3RhdGVzX3ZsZXNzXzAKdmxlc3M6Ly84NzVlMGM1NC0yNjkwLTRiZmItYTRlNS1kNDRiY2Y5ZDJhMzFAMTk4LjQxLjIyMS4xMjoyMDk2P3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWt5ZC5jbG91ZG5zLm9yZyZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovLzg3NWUwYzU0LTI2OTAtNGJmYi1hNGU1LWQ0NGJjZjlkMmEzMUAxMDQuMjEuMjguMTQ3OjIwODM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9a3lkLmNsb3VkbnMub3JnJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vODc1ZTBjNTQtMjY5MC00YmZiLWE0ZTUtZDQ0YmNmOWQyYTMxQDE5OC40MS4yMDkuMTUwOjg0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9a3lkLmNsb3VkbnMub3JnJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vZmZmZmZmZmYtMTdhZC00NWU3LWFhYTEtZjJiYWFhMDhlOTMwQDEwNC4xOS4xNTUuMTE6ODQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT13YXRhc2hpLmZyZWUuanBwdWJsaWMubW9oNTM5Lmxpbmsmc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNOb25lX3ZsZXNzXzAKdmxlc3M6Ly9kMzQyZDExZS1kNDI0LTQ1ODMtYjM2ZS01MjRhYjFmMGFmYTRAMTA0LjIxLjQuMjQ2OjIwODM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9ZWRnb29kLmtpbmczNjEuY2Ymc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNOb25lX3ZsZXNzXzAKdmxlc3M6Ly9mZmZmZmZmZi0xN2FkLTQ1ZTctYWFhMS1mMmJhYWEwOGU5MzBAMTA0LjE2Ljk2LjIxODoyMDg3P3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPXdhdGFzaGkuZnJlZS5qcHB1YmxpYy5tb2g1MzkubGluayZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovLzYwODEzYjlkLWFhMGUtNGE1Yy04OGI4LWVkMjMxMDU4ZTgyYUBsaWxpanVseS5wcC51YTo4NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPXBhZ2VzLjIwMjMwNjE5LmxvdmUmc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNVbml0ZWQgU3RhdGVzX3ZsZXNzXzAKdmxlc3M6Ly84NzVlMGM1NC0yNjkwLTRiZmItYTRlNS1kNDRiY2Y5ZDJhMzFAMTA0LjE3LjIwOC4xNzQ6ODQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1reWQuY2xvdWRucy5vcmcmc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNOb25lX3ZsZXNzXzAKdmxlc3M6Ly83M2I2ZGJkNS1hMjdhLTRjNzYtOWFkMS00MmE4MjM4MGRkZGJAMTA0LjIxLjUuNzo4NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWVkLmFyaWVzdmVyLm9ubGluZSZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovLzg3NWUwYzU0LTI2OTAtNGJmYi1hNGU1LWQ0NGJjZjlkMmEzMUAxMDQuMTcuMjEwLjk6MjA4Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1reWQuY2xvdWRucy5vcmcmc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNOb25lX3ZsZXNzXzAKdmxlc3M6Ly83ZmQ3YzE1ZC05NWNkLTRmNWMtYmY1OS1mMjFlNWViMjc1ODBAMTA0LjIxLjIuMDo4NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPTNrLmRhYmVlLnRvcCZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovLzczYjZkYmQ1LWEyN2EtNGM3Ni05YWQxLTQyYTgyMzgwZGRkYkAxMDQuMjEuNS4zMzoyMDgzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWVkLmFyaWVzdmVyLm9ubGluZSZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovLzdmZDdjMTVkLTk1Y2QtNGY1Yy1iZjU5LWYyMWU1ZWIyNzU4MEAxMDQuMjEuMTIuMTUxOjIwODc/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9M2suZGFiZWUudG9wJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vN2ZkN2MxNWQtOTVjZC00ZjVjLWJmNTktZjIxZTVlYjI3NTgwQDEwNC4yMS4xMi44NDo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9M2suZGFiZWUudG9wJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vODc1ZTBjNTQtMjY5MC00YmZiLWE0ZTUtZDQ0YmNmOWQyYTMxQDEwNC4xNy4yMTkuMTUxOjg0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9a3lkLmNsb3VkbnMub3JnJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vNzNiNmRiZDUtYTI3YS00Yzc2LTlhZDEtNDJhODIzODBkZGRiQDEwNC4yMS4xNS4yNDM6MjA5Nj9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1lZC5hcmllc3Zlci5vbmxpbmUmc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNOb25lX3ZsZXNzXzAKdmxlc3M6Ly82MDgxM2I5ZC1hYTBlLTRhNWMtODhiOC1lZDIzMTA1OGU4MmFAeHdtLXVzLXY2LWEubW91Ym9zcy5wcC51YToyMDgzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPXBhZ2VzLjIwMjMwNjE5LmxvdmUmc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNOb25lX3ZsZXNzXzAKdmxlc3M6Ly82MDgxM2I5ZC1hYTBlLTRhNWMtODhiOC1lZDIzMTA1OGU4MmFAZHZvcmRhLnBwLnVhOjIwOTY/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9cGFnZXMuMjAyMzA2MTkubG92ZSZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I1VuaXRlZCBTdGF0ZXNfdmxlc3NfMAp2bGVzczovLzg3NWUwYzU0LTI2OTAtNGJmYi1hNGU1LWQ0NGJjZjlkMmEzMUAxMDQuMjEuMzAuMTc2OjIwOTY/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9a3lkLmNsb3VkbnMub3JnJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vNjA4MTNiOWQtYWEwZS00YTVjLTg4YjgtZWQyMzEwNThlODJhQHNtaS5wcC51YTo4NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPXBhZ2VzLjIwMjMwNjE5LmxvdmUmc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNOb25lX3ZsZXNzXzAKdmxlc3M6Ly84NzVlMGM1NC0yNjkwLTRiZmItYTRlNS1kNDRiY2Y5ZDJhMzFAMTA0LjIxLjI4LjI5OjIwNTM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9a3lkLmNsb3VkbnMub3JnJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vZmZmZmZmZmYtMTdhZC00NWU3LWFhYTEtZjJiYWFhMDhlOTMwQDEwNC4xNi45Ni4xOTc6MjA4Nz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT13YXRhc2hpLmZyZWUuanBwdWJsaWMubW9oNTM5Lmxpbmsmc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNOb25lX3ZsZXNzXzAKdmxlc3M6Ly9mZmZmZmZmZi0xN2FkLTQ1ZTctYWFhMS1mMmJhYWEwOGU5MzBAMTA0LjE2Ljk2LjU0Ojg0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9d2F0YXNoaS5mcmVlLmpwcHVibGljLm1vaDUzOS5saW5rJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vODc1ZTBjNTQtMjY5MC00YmZiLWE0ZTUtZDQ0YmNmOWQyYTMxQDE5OC40MS4yMjEuMTk1OjIwOTY/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9a3lkLmNsb3VkbnMub3JnJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vNjA4MTNiOWQtYWEwZS00YTVjLTg4YjgtZWQyMzEwNThlODJhQGpwNy52bGVzc3gudXM6ODQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1wYWdlcy4yMDIzMDYxOS5sb3ZlJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jVW5pdGVkIFN0YXRlc192bGVzc18wCnZsZXNzOi8vNjA4MTNiOWQtYWEwZS00YTVjLTg4YjgtZWQyMzEwNThlODJhQDEwNC4yMS4xNy4xNTI6MjA4Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1wYWdlcy4yMDIzMDYxOS5sb3ZlJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vNjA4MTNiOWQtYWEwZS00YTVjLTg4YjgtZWQyMzEwNThlODJhQDEwNC4yMS4wLjE2OTo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9cGFnZXMuMjAyMzA2MTkubG92ZSZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovLzdmZDdjMTVkLTk1Y2QtNGY1Yy1iZjU5LWYyMWU1ZWIyNzU4MEAxMDQuMjEuMi42ODoyMDg3P3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPTNrLmRhYmVlLnRvcCZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovLzYwODEzYjlkLWFhMGUtNGE1Yy04OGI4LWVkMjMxMDU4ZTgyYUBzbWkucHAudWE6MjA4Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1wYWdlcy4yMDIzMDYxOS5sb3ZlJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jVW5pdGVkIFN0YXRlc192bGVzc18wCnZsZXNzOi8vZDM0MmQxMWUtZDQyNC00NTgzLWIzNmUtNTI0YWIxZjBhZmE0QDEwNC4yMS40Ljg3OjIwODM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9ZWRnb29kLmtpbmczNjEuY2Ymc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNOb25lX3ZsZXNzXzAKdmxlc3M6Ly83M2I2ZGJkNS1hMjdhLTRjNzYtOWFkMS00MmE4MjM4MGRkZGJAMTA0LjIxLjUuMTcyOjIwNTM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9ZWQuYXJpZXN2ZXIub25saW5lJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vZDM0MmQxMWUtZDQyNC00NTgzLWIzNmUtNTI0YWIxZjBhZmE0QDEwNC4yMS40LjE4MzoyMDg3P3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWVkZ29vZC5raW5nMzYxLmNmJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vNjA4MTNiOWQtYWEwZS00YTVjLTg4YjgtZWQyMzEwNThlODJhQHNtaS5wcC51YTo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9cGFnZXMuMjAyMzA2MTkubG92ZSZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovL2ZmZmZmZmZmLTE3YWQtNDVlNy1hYWExLWYyYmFhYTA4ZTkzMEAxMDQuMjEuMS4xMzg6MjA4Nz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT13YXRhc2hpLmZyZWUuanBwdWJsaWMubW9oNTM5Lmxpbmsmc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNOb25lX3ZsZXNzXzAKdmxlc3M6Ly9hNGZhZjVkOC1iOWE4LTQzM2UtOTUxOC0yZDJlMjFkNzZmNzhAMTA0LjE4LjE5MC41Mjo0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9bmdpbngubmlyZXZpbC5pciZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovLzg3NWUwYzU0LTI2OTAtNGJmYi1hNGU1LWQ0NGJjZjlkMmEzMUAxOTguNDEuMjA4LjE1NjoyMDg3P3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWt5ZC5jbG91ZG5zLm9yZyZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovLzYwODEzYjlkLWFhMGUtNGE1Yy04OGI4LWVkMjMxMDU4ZTgyYUAxMDQuMjEuMC4xNTI6MjA1Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1wYWdlcy4yMDIzMDYxOS5sb3ZlJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vNjA4MTNiOWQtYWEwZS00YTVjLTg4YjgtZWQyMzEwNThlODJhQGEubm9vbm9rb3JlYW4ucHAudWE6MjA5Nj9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1wYWdlcy4yMDIzMDYxOS5sb3ZlJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jVW5pdGVkIFN0YXRlc192bGVzc18wCnZsZXNzOi8vZmZmZmZmZmYtMTdhZC00NWU3LWFhYTEtZjJiYWFhMDhlOTMwQDEwNC4yMS4xNi4yMzg6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPXdhdGFzaGkuZnJlZS5qcHB1YmxpYy5tb2g1MzkubGluayZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovL2ZmZmZmZmZmLTE3YWQtNDVlNy1hYWExLWYyYmFhYTA4ZTkzMEAxMDQuMjEuMS4yNTA6ODQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT13YXRhc2hpLmZyZWUuanBwdWJsaWMubW9oNTM5Lmxpbmsmc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNOb25lX3ZsZXNzXzAKdmxlc3M6Ly84NzVlMGM1NC0yNjkwLTRiZmItYTRlNS1kNDRiY2Y5ZDJhMzFAMTA0LjIxLjI2LjIyNToyMDgzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWt5ZC5jbG91ZG5zLm9yZyZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovLzg3NWUwYzU0LTI2OTAtNGJmYi1hNGU1LWQ0NGJjZjlkMmEzMUAxMDQuMTcuMjA5LjE0OToyMDgzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWt5ZC5jbG91ZG5zLm9yZyZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovLzYwODEzYjlkLWFhMGUtNGE1Yy04OGI4LWVkMjMxMDU4ZTgyYUB1czEwLnZsZXNzeC51czo4NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPXBhZ2VzLjIwMjMwNjE5LmxvdmUmc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNVbml0ZWQgU3RhdGVzX3ZsZXNzXzAKdmxlc3M6Ly84NzVlMGM1NC0yNjkwLTRiZmItYTRlNS1kNDRiY2Y5ZDJhMzFAMTA0LjIxLjI2LjIzMDo4NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWt5ZC5jbG91ZG5zLm9yZyZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovL2I5YWQ4OTViLTEyYWMtNDBmYy1hNWFjLWE1YjJhMTI4NTAwMUAxMDQuMjEuMjguNjI6NDQzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPTNrLnB1cmVib3kuZXUub3JnJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vN2ZkN2MxNWQtOTVjZC00ZjVjLWJmNTktZjIxZTVlYjI3NTgwQDEwNC4yMS4yLjk2OjIwODc/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9M2suZGFiZWUudG9wJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vZDM0MmQxMWUtZDQyNC00NTgzLWIzNmUtNTI0YWIxZjBhZmE0QDEwNC4yMS4xNC4yNDU6MjA4Nz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1lZGdvb2Qua2luZzM2MS5jZiZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovLzczYjZkYmQ1LWEyN2EtNGM3Ni05YWQxLTQyYTgyMzgwZGRkYkAxMDQuMjEuMTUuNTU6MjA4Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1lZC5hcmllc3Zlci5vbmxpbmUmc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNOb25lX3ZsZXNzXzAKdmxlc3M6Ly84NzVlMGM1NC0yNjkwLTRiZmItYTRlNS1kNDRiY2Y5ZDJhMzFAMTk4LjQxLjIyMS4xNzM6MjA4Nz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1reWQuY2xvdWRucy5vcmcmc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNOb25lX3ZsZXNzXzAKdmxlc3M6Ly83M2I2ZGJkNS1hMjdhLTRjNzYtOWFkMS00MmE4MjM4MGRkZGJAMTA0LjIxLjE1LjIyNjoyMDg3P3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPWVkLmFyaWVzdmVyLm9ubGluZSZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovLzdmZDdjMTVkLTk1Y2QtNGY1Yy1iZjU5LWYyMWU1ZWIyNzU4MEAxMDQuMjEuMi4xNzM6MjA5Nj9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT0zay5kYWJlZS50b3Amc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNOb25lX3ZsZXNzXzAKdmxlc3M6Ly9mNGNlYzZjYy02MTc3LTQyM2MtOTBmOC0yYWQ5ZjBkZDk5NmJAY3R3Y3QuYXJ2YW5jb2RlLmV1Lm9yZzoyMDk2P3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPXZwbmN0LmFydmFuY29kZS5ldS5vcmcmc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNVbml0ZWQgU3RhdGVzX3ZsZXNzXzAKdmxlc3M6Ly82MDgxM2I5ZC1hYTBlLTRhNWMtODhiOC1lZDIzMTA1OGU4MmFAMTA0LjIxLjAuMTc3OjIwNTM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9cGFnZXMuMjAyMzA2MTkubG92ZSZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovLzYwODEzYjlkLWFhMGUtNGE1Yy04OGI4LWVkMjMxMDU4ZTgyYUBqZ3cud3NoeXgucHAudWE6MjA4Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZTAmZmxvdz0mdHlwZT13cyZmcD0mcGJrPSZzaWQ9JnNuaT1wYWdlcy4yMDIzMDYxOS5sb3ZlJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jVW5pdGVkIFN0YXRlc192bGVzc18wCnZsZXNzOi8vODc1ZTBjNTQtMjY5MC00YmZiLWE0ZTUtZDQ0YmNmOWQyYTMxQDEwNC4yMS4yNC43Ojg0NDM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9a3lkLmNsb3VkbnMub3JnJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vN2ZkN2MxNWQtOTVjZC00ZjVjLWJmNTktZjIxZTVlYjI3NTgwQDEwNC4yMS4yLjIxOToyMDk2P3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPTNrLmRhYmVlLnRvcCZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovLzczYjZkYmQ1LWEyN2EtNGM3Ni05YWQxLTQyYTgyMzgwZGRkYkAxMDQuMjEuMTUuMjQzOjIwNTM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9ZWQuYXJpZXN2ZXIub25saW5lJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vZmZmZmZmZmYtMTdhZC00NWU3LWFhYTEtZjJiYWFhMDhlOTMwQDEwNC4yMS4xLjE0NzoyMDUzP3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPXdhdGFzaGkuZnJlZS5qcHB1YmxpYy5tb2g1MzkubGluayZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovLzdmZDdjMTVkLTk1Y2QtNGY1Yy1iZjU5LWYyMWU1ZWIyNzU4MEAxMDQuMjEuMTIuMTQwOjIwNTM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9M2suZGFiZWUudG9wJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vODc1ZTBjNTQtMjY5MC00YmZiLWE0ZTUtZDQ0YmNmOWQyYTMxQDE5OC40MS4yMDkuMTgwOjIwNTM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9a3lkLmNsb3VkbnMub3JnJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnZsZXNzOi8vNjA4MTNiOWQtYWEwZS00YTVjLTg4YjgtZWQyMzEwNThlODJhQHR6LmxpbGlqdWx5LnBwLnVhOjIwODM/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9cGFnZXMuMjAyMzA2MTkubG92ZSZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I05vbmVfdmxlc3NfMAp2bGVzczovLzYwODEzYjlkLWFhMGUtNGE1Yy04OGI4LWVkMjMxMDU4ZTgyYUBpLm5vb25va29yZWFuLnBwLnVhOjIwOTY/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9cGFnZXMuMjAyMzA2MTkubG92ZSZzZXJ2aWNlTmFtZT0mcGF0aD1Ud2l0dGVy6IuP5bCP5p+gJmhvc3Q9I1VuaXRlZCBTdGF0ZXNfdmxlc3NfMAp2bGVzczovLzYwODEzYjlkLWFhMGUtNGE1Yy04OGI4LWVkMjMxMDU4ZTgyYUA4ODg4OC5wcC51YToyMDg3P3NlY3VyaXR5PXRscyZhbGxvd0luc2VjdXJlMCZmbG93PSZ0eXBlPXdzJmZwPSZwYms9JnNpZD0mc25pPXBhZ2VzLjIwMjMwNjE5LmxvdmUmc2VydmljZU5hbWU9JnBhdGg9VHdpdHRlcuiLj+Wwj+afoCZob3N0PSNVbml0ZWQgU3RhdGVzX3ZsZXNzXzAKdmxlc3M6Ly9mZmZmZmZmZi0xN2FkLTQ1ZTctYWFhMS1mMmJhYWEwOGU5MzBAMTA0LjIxLjEuMTc5OjIwOTY/c2VjdXJpdHk9dGxzJmFsbG93SW5zZWN1cmUwJmZsb3c9JnR5cGU9d3MmZnA9JnBiaz0mc2lkPSZzbmk9d2F0YXNoaS5mcmVlLmpwcHVibGljLm1vaDUzOS5saW5rJnNlcnZpY2VOYW1lPSZwYXRoPVR3aXR0ZXLoi4/lsI/mn6AmaG9zdD0jTm9uZV92bGVzc18wCnR1aWM6Ly9mZWYzZDNjMi1hYjNlLTQxMzQtYTJmMy0wYzJkODNlMGE3NmQ6ZG9uZ3RhaXdhbmcuY29tQDExMS4yNDMuOTcuMjozMzA5OD9zbmk9JmNvbmdlc3Rpb25fY29udHJvbD1iYnImdWRwX3JlbGF5X21vZGU9bmF0aXZlJmFscG49aDMmYWxsb3dfaW5zZWN1cmU9MCNUYWl3YW5fdHVpY18xCmh5c3RlcmlhOi8vd3d3Mi5kdGt1NDgueHl6OjIyMzM0P3BlZXI9JmF1dGg9ZG9uZ3RhaXdhbmcuY29tJmluc2VjdXJlPTEmdXBtYnBzPTUwJmRvd25tYnBzPTgwJmFscG49aDMmbXBvcnQ9MjIzMzQmb2Jmcz0mcHJvdG9jb2w9dWRwJmZhc3RvcGVuPTEjVGFpd2FuX2h5XzYKaHlzdGVyaWEyOi8vZG9uZ3RhaXdhbmcuY29tQDUxLjE1OC41NC40Njo0NDU1MD9pbnNlY3VyZT0xJnNuaT1iaW5nLmNvbSZvYmZzPSZvYmZzLXBhc3N3b3JkPSNGcmFuY2VfaHkyXzcKaHlzdGVyaWE6Ly93d3cyLmR0a3U0OC54eXo6MjIzMzQ/cGVlcj0mYXV0aD1kb25ndGFpd2FuZy5jb20maW5zZWN1cmU9MSZ1cG1icHM9NTAmZG93bm1icHM9ODAmYWxwbj1oMyZtcG9ydD0yMjMzNCZvYmZzPSZwcm90b2NvbD11ZHAmZmFzdG9wZW49MSNUYWl3YW5faHlfOApoeXN0ZXJpYTovL3d3dy5kdGt1NTAueHl6OjE4NDcwP3BlZXI9d3d3LmFtYXpvbi5jbiZhdXRoPSZpbnNlY3VyZT0xJnVwbWJwcz01MCZkb3dubWJwcz04MCZhbHBuPWgzJm1wb3J0PTE4NDcwJm9iZnM9JnByb3RvY29sPXVkcCZmYXN0b3Blbj0xI1RhaXdhbl9oeV85CmFIUjBjSE02THk5a2IyNW5kR0ZwZDJGdVp5NWpiMjA2Wkc5dVozUmhhWGRoYm1jdVkyOXRRRzVoYVhabE1Ua3VZMlpqWkc0ekxuaDVlam8wTkRNPQphSFIwY0hNNkx5OWtiMjVuZEdGcGQyRnVaeTVqYjIwNlpHOXVaM1JoYVhkaGJtY3VZMjl0UUhkM2R5NWtkR3QxTlRBdWVIbDZPalEwTXc9PQpoeXN0ZXJpYTovLzUxLjE1OC41NC40Njo1NTM5Nj9wZWVyPXlvdWt1LmNvbSZhdXRoPWRvbmd0YWl3YW5nLmNvbSZpbnNlY3VyZT0xJnVwbWJwcz0xMSZkb3dubWJwcz01NSZhbHBuPWgzJm9iZnM9JnByb3RvY29sPXVkcCZmYXN0b3Blbj0xI0ZyYW5jZV9oeXN0ZXJpYV8wCmh5c3RlcmlhOi8vMTczLjIzNC4yNS41Mjo0ODkxOT9wZWVyPWJpbmcuY29tJmF1dGg9ZG9uZ3RhaXdhbmcuY29tJmluc2VjdXJlPTEmdXBtYnBzPTExJmRvd25tYnBzPTU1JmFscG49aDMmb2Jmcz0mcHJvdG9jb2w9dWRwJmZhc3RvcGVuPTEjVW5pdGVkIFN0YXRlc19oeXN0ZXJpYV8xCmh5c3RlcmlhOi8vMTA4LjE4MS4yMi4yMzk6Mzk5Njc/cGVlcj1iaW5nLmNvbSZhdXRoPWRvbmd0YWl3YW5nLmNvbSZpbnNlY3VyZT0xJnVwbWJwcz0xMSZkb3dubWJwcz01NSZhbHBuPWgzJm9iZnM9JnByb3RvY29sPXVkcCZmYXN0b3Blbj0xI1VuaXRlZCBTdGF0ZXNfaHlzdGVyaWFfMgpoeXN0ZXJpYTovLzE2Ny4xNjAuOTEuMTE1OjQxMTg5P3BlZXI9d3d3LmFtYXpvbi5jbiZhdXRoPWJXQXdJcUlObzdYRG0xZlVsWFFHQmlmVklYb1lzMXlsZ1ZLcVdGS3pLMVh5REt1d05GJmluc2VjdXJlPTEmdXBtYnBzPTExJmRvd25tYnBzPTU1JmFscG49aDMmb2Jmcz0mcHJvdG9jb2w9dWRwJmZhc3RvcGVuPTEjVW5pdGVkIFN0YXRlc19oeXN0ZXJpYV8zCmh5c3RlcmlhMjovL2Rvbmd0YWl3YW5nLmNvbUA2Mi4yMTAuMTAzLjA6MjI0ODM/aW5zZWN1cmU9MSZzbmk9d3d3LmJpbmcuY29tI0ZyYW5jZV9oeXN0ZXJpYTJfMApoeXN0ZXJpYTI6Ly9kb25ndGFpd2FuZy5jb21ANjQuMTEwLjI1LjExOjMzMzM3P2luc2VjdXJlPTEmc25pPXd3dy5iaW5nLmNvbSNVbml0ZWQgU3RhdGVzX2h5c3RlcmlhMl8xCmh5c3RlcmlhMjovL2Rvbmd0YWl3YW5nLmNvbUA2Mi4yMTAuMTAzLjA6MjI0ODM/aW5zZWN1cmU9MSZzbmk9d3d3LmJpbmcuY29tI0ZyYW5jZV9oeXN0ZXJpYTJfMgpoeXN0ZXJpYTI6Ly9kb25ndGFpd2FuZy5jb21AMTA4LjE4MS4yNC43Nzo0MzY1Nj9pbnNlY3VyZT0xJnNuaT13d3cuYmluZy5jb20jVW5pdGVkIFN0YXRlc19oeXN0ZXJpYTJfMwp2bGVzczovLzljYzM5NDc3LTBkODUtNDQxOS04NGQ0LWZiN2ZjNzc2NjhiM0AxMDguMTgxLjIyLjIxMzoyODk0NT9zZWN1cml0eT1yZWFsaXR5JmFsbG93SW5zZWN1cmU9MCZmbG93PXh0bHMtcnByeC12aXNpb24mdHlwZT10Y3AmZnA9Y2hyb21lJnBiaz15S1htTFRtWEFpLUJIQmczSnBDei1OV1VtVmNLbGZtN2lNbVZvcTdZUXgwJnNpZD02YmE4NTE3OWUzMGQ0ZmMyJnNuaT1tLm1lZGlhLWFtYXpvbi5jb20mc2VydmljZU5hbWU9JnBhdGg9Jmhvc3Q9I1VuaXRlZCBTdGF0ZXNfdmxlc3NfMQp2bGVzczovL2U2NTk2NjFkLTg0MzktNDZlMC1iMWFiLWQ3NWNlYWY3MzQwNEA2Mi4yMTAuMTAxLjA6MTg3MDA/c2VjdXJpdHk9cmVhbGl0eSZhbGxvd0luc2VjdXJlPTAmZmxvdz14dGxzLXJwcngtdmlzaW9uJnR5cGU9dGNwJmZwPWNocm9tZSZwYms9UEJSYzJ2OVNTWHBHNGpqUVJZTmEta2dzOHc5VjRVM01OTHVuY2QyZDBodyZzaWQ9NmJhODUxNzllMzBkNGZjMiZzbmk9dXBkYXRlLm1pY3Jvc29mdCZzZXJ2aWNlTmFtZT0mcGF0aD0maG9zdD0jRnJhbmNlX3ZsZXNzXzIKdmxlc3M6Ly9lNjU5NjYxZC04NDM5LTQ2ZTAtYjFhYi1kNzVjZWFmNzM0MDRANjIuMjEwLjEwMS4wOjE4NzAwP3NlY3VyaXR5PXJlYWxpdHkmYWxsb3dJbnNlY3VyZT0wJmZsb3c9eHRscy1ycHJ4LXZpc2lvbiZ0eXBlPXRjcCZmcD1jaHJvbWUmcGJrPVBCUmMydjlTU1hwRzRqalFSWU5hLWtnczh3OVY0VTNNTkx1bmNkMmQwaHcmc2lkPTZiYTg1MTc5ZTMwZDRmYzImc25pPXVwZGF0ZS5taWNyb3NvZnQmc2VydmljZU5hbWU9JnBhdGg9Jmhvc3Q9I0ZyYW5jZV92bGVzc18z
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
        "None_vless_0",
        "🇹🇼 Taiwan_tuic_1",
        "🇨🇦 Canada_vless_2",
        "🇺🇸 United States_tuic_3",
        "🇺🇸 United States_tuic_4",
        "🇺🇸 United States_tuic_5",
        "🇹🇼 Taiwan_hy_6",
        "🇫🇷 France_hy2_7",
        "🇹🇼 Taiwan_hy_8",
        "🇹🇼 Taiwan_hy_9",
        "🇫🇷 France_hysteria_0",
        "🇺🇸 United States_hysteria_1",
        "🇺🇸 United States_hysteria_2",
        "🇺🇸 United States_hysteria_3",
        "🇫🇷 France_hysteria2_0",
        "🇺🇸 United States_hysteria2_1",
        "🇫🇷 France_hysteria2_2",
        "🇺🇸 United States_hysteria2_3",
        "🇺🇸 United States_vless_1",
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
        "🇹🇼 Taiwan_tuic_1",
        "🇹🇼 Taiwan_hy_6",
        "🇹🇼 Taiwan_hy_8",
        "🇹🇼 Taiwan_hy_9",
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
        "🇺🇸 United States_tuic_3",
        "🇺🇸 United States_tuic_4",
        "🇺🇸 United States_tuic_5",
        "🇺🇸 United States_hysteria_1",
        "🇺🇸 United States_hysteria_2",
        "🇺🇸 United States_hysteria_3",
        "🇺🇸 United States_hysteria2_1",
        "🇺🇸 United States_hysteria2_3",
        "🇺🇸 United States_vless_1",
        "proxy"
      ]
    },
    {
      "tag": "Others",
      "type": "selector",
      "outbounds": [
        "None_vless_0",
        "🇨🇦 Canada_vless_2",
        "🇫🇷 France_hy2_7",
        "🇫🇷 France_hysteria_0",
        "🇫🇷 France_hysteria2_0",
        "🇫🇷 France_hysteria2_2",
        "🇫🇷 France_vless_2",
        "🇫🇷 France_vless_3",
        "proxy"
      ]
    },
    {
      "tag": "auto",
      "type": "urltest",
      "outbounds": [
        "None_vless_0",
        "🇹🇼 Taiwan_tuic_1",
        "🇨🇦 Canada_vless_2",
        "🇺🇸 United States_tuic_3",
        "🇺🇸 United States_tuic_4",
        "🇺🇸 United States_tuic_5",
        "🇹🇼 Taiwan_hy_6",
        "🇫🇷 France_hy2_7",
        "🇹🇼 Taiwan_hy_8",
        "🇹🇼 Taiwan_hy_9",
        "🇫🇷 France_hysteria_0",
        "🇺🇸 United States_hysteria_1",
        "🇺🇸 United States_hysteria_2",
        "🇺🇸 United States_hysteria_3",
        "🇫🇷 France_hysteria2_0",
        "🇺🇸 United States_hysteria2_1",
        "🇫🇷 France_hysteria2_2",
        "🇺🇸 United States_hysteria2_3",
        "🇺🇸 United States_vless_1",
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
      "tag": "None_vless_0",
      "type": "vless",
      "server": "cloudflare.cfgo.cc",
      "server_port": 2053,
      "uuid": "627016c6-a565-47f9-93cf-df937b38bbb7",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "4.dtku43.xyz",
        "utls": {
          "enabled": true,
          "fingerprint": "chrome"
        }
      },
      "transport": {
        "type": "ws",
        "path": "/hcxiws",
        "headers": {
          "Host": "4.dtku43.xyz"
        }
      }
    },
    {
      "tag": "🇹🇼 Taiwan_tuic_1",
      "type": "tuic",
      "server": "1.162.156.206",
      "server_port": 33098,
      "uuid": "fef3d3c2-ab3e-4134-a2f3-0c2d83e0a76d",
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
      "tag": "🇨🇦 Canada_vless_2",
      "type": "vless",
      "server": "23.227.38.54",
      "server_port": 2096,
      "uuid": "e80e0204-ddf1-4f59-8e75-44ea502aabae",
      "packet_encoding": "xudp",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "2.dtku43.xyz",
        "utls": {
          "enabled": true,
          "fingerprint": "chrome"
        }
      },
      "transport": {
        "type": "ws",
        "path": "/mjyrws",
        "headers": {
          "Host": "2.dtku43.xyz"
        }
      }
    },
    {
      "tag": "🇺🇸 United States_tuic_3",
      "type": "tuic",
      "server": "64.31.55.124",
      "server_port": 44556,
      "uuid": "a72c47f7-5d2d-4029-a5ca-997ac2d1c956",
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
      "tag": "🇺🇸 United States_tuic_4",
      "type": "tuic",
      "server": "64.31.55.124",
      "server_port": 44556,
      "uuid": "a72c47f7-5d2d-4029-a5ca-997ac2d1c956",
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
      "tag": "🇺🇸 United States_tuic_5",
      "type": "tuic",
      "server": "64.31.55.124",
      "server_port": 44556,
      "uuid": "a72c47f7-5d2d-4029-a5ca-997ac2d1c956",
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
      "tag": "🇹🇼 Taiwan_hy_8",
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
      "tag": "🇺🇸 United States_hysteria_2",
      "type": "hysteria",
      "server": "108.181.22.239",
      "server_port": 39967,
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
      "tag": "🇺🇸 United States_hysteria2_3",
      "type": "hysteria2",
      "server": "108.181.24.77",
      "server_port": 43656,
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
      "tag": "🇺🇸 United States_vless_1",
      "type": "vless",
      "server": "108.181.22.213",
      "server_port": 28945,
      "uuid": "9cc39477-0d85-4419-84d4-fb7fc77668b3",
      "packet_encoding": "xudp",
      "flow": "xtls-rprx-vision",
      "tls": {
        "enabled": true,
        "insecure": false,
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


