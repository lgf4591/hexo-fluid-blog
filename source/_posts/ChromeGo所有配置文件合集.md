
---
title: ChromeGo所有配置文件合集 
date: 2024-02-25 18:10:33
index_img: https://fluid.s3.bitiful.net/hello-fluid/cover.png?w=480&fmt=webp
category: VPN
tags:
  - VPN
  - ChromeGo
  - Config
math: true
mermaid: true
sticky: 100
---

> Last Update Time: 2024-02-25 18:10:33
---

## Quick-ip_1.yaml
```bash
<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.20.1</center>
</body>
</html>
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->

```

## Quick-ip_2.yaml
```bash
secret: dongtaiwang.com
mixed-port: 7890
allow-lan: false
log-level: info
dns:
  enabled: true
  nameserver:
    - 119.29.29.29
    - 223.5.5.5
  fallback:
    - 8.8.8.8
    - 8.8.4.4
    - tls://1.0.0.1:853
    - tls://dns.google:853
proxies:
  - {"name":"ip","type":"vless","server":"45.145.72.212","port":11223,"udp":true,"uuid":"34d7aac1-fac7-4e17-b41e-5be028d286cd","tls":true,"servername":"addons.mozilla.org","flow":"xtls-rprx-vision","network":"tcp","reality-opts":{"public-key":"u24pYS0RqtYk8NBqtg4NIHUZIA0HmwuYw2RBIyt0T0c"},"client-fingerprint":"chrome"}
proxy-groups:
  - name: 🚀 节点选择
    type: select
    proxies:
      - ♻️ 自动选择
      - DIRECT
      - ip
  - name: ♻️ 自动选择
    type: url-test
    url: https://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    proxies:
      - ip
  - name: 🌍 国外媒体
    type: select
    proxies:
      - 🚀 节点选择
      - ♻️ 自动选择
      - 🎯 全球直连
      - ip
  - name: 📲 电报信息
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - ip
  - name: Ⓜ️ 微软服务
    type: select
    proxies:
      - 🎯 全球直连
      - 🚀 节点选择
      - ip
  - name: 🍎 苹果服务
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - ip
  - name: 🎯 全球直连
    type: select
    proxies:
      - DIRECT
      - 🚀 节点选择
      - ♻️ 自动选择
  - name: 🛑 全球拦截
    type: select
    proxies:
      - REJECT
      - DIRECT
  - name: 🍃 应用净化
    type: select
    proxies:
      - REJECT
      - DIRECT
  - name: 🐟 漏网之鱼
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - ♻️ 自动选择
      - ip

rules:
  - MATCH,🚀 节点选择

```

## Quick-ip_3.yaml
```bash
<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.20.1</center>
</body>
</html>
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->

```

## Quick-ip_4.yaml
```bash
secret: dongtaiwang.com
mixed-port: 7890
allow-lan: false
log-level: info
dns:
  enabled: true
  nameserver:
    - 119.29.29.29
    - 223.5.5.5
  fallback:
    - 8.8.8.8
    - 8.8.4.4
    - tls://1.0.0.1:853
    - tls://dns.google:853
proxies:
  - name: ip 
    type: hysteria
    server: www2.dtku48.xyz
    port: 22334
    auth-str: dongtaiwang.com
    alpn:
      - h3
    protocol: udp
    up: "11 Mbps"
    down: "55 Mbps"
    skip-cert-verify: true 
proxy-groups:
  - name: 🚀 节点选择
    type: select
    proxies:
      - ♻️ 自动选择
      - DIRECT
      - ip
  - name: ♻️ 自动选择
    type: url-test
    url: https://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    proxies:
      - ip
  - name: 🌍 国外媒体
    type: select
    proxies:
      - 🚀 节点选择
      - ♻️ 自动选择
      - 🎯 全球直连
      - ip
  - name: 📲 电报信息
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - ip
  - name: Ⓜ️ 微软服务
    type: select
    proxies:
      - 🎯 全球直连
      - 🚀 节点选择
      - ip
  - name: 🍎 苹果服务
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - ip
  - name: 🎯 全球直连
    type: select
    proxies:
      - DIRECT
      - 🚀 节点选择
      - ♻️ 自动选择
  - name: 🛑 全球拦截
    type: select
    proxies:
      - REJECT
      - DIRECT
  - name: 🍃 应用净化
    type: select
    proxies:
      - REJECT
      - DIRECT
  - name: 🐟 漏网之鱼
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - ♻️ 自动选择
      - ip

rules:
  - MATCH,🚀 节点选择

```

## Xray-ip_1.json
```bash
<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.20.1</center>
</body>
</html>
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->

```

## Xray-ip_2.json
```bash
{
  "log": {
    "access": "",
    "error": "",
    "loglevel": "warning"
  },
  "inbounds": [
    {
      "tag": "socks",
      "port": 1080,
      "listen": "127.0.0.1",
      "protocol": "socks",
      "sniffing": {
        "enabled": true,
        "destOverride": [
          "http",
          "tls"
        ],
        "routeOnly": false
      },
      "settings": {
        "auth": "noauth",
        "udp": true,
        "allowTransparent": false
      }
    },
    {
      "tag": "http",
      "port": 1081,
      "listen": "127.0.0.1",
      "protocol": "http",
      "sniffing": {
        "enabled": true,
        "destOverride": [
          "http",
          "tls"
        ],
        "routeOnly": false
      },
      "settings": {
        "auth": "noauth",
        "udp": true,
        "allowTransparent": false
      }
    }
  ],
  "outbounds": [
    {
      "tag": "proxy",
      "protocol": "vless",
      "settings": {
        "vnext": [
          {
            "address": "62.210.101.0",
            "port": 18700,
            "users": [
              {
                "id": "e659661d-8439-46e0-b1ab-d75ceaf73404",
                "alterId": 0,
                "email": "t@t.tt",
                "security": "auto",
                "encryption": "none",
                "flow": "xtls-rprx-vision"
              }
            ]
          }
        ]
      },
      "streamSettings": {
        "network": "tcp",
        "security": "reality",
        "realitySettings": {
          "serverName": "update.microsoft",
          "fingerprint": "chrome",
          "show": false,
          "publicKey": "PBRc2v9SSXpG4jjQRYNa-kgs8w9V4U3MNLuncd2d0hw",
          "shortId": "6ba85179e30d4fc2",
          "spiderX": ""
        }
      },
      "mux": {
        "enabled": false,
        "concurrency": -1
      }
    },
    {
      "tag": "direct",
      "protocol": "freedom",
      "settings": {}
    },
    {
      "tag": "block",
      "protocol": "blackhole",
      "settings": {
        "response": {
          "type": "http"
        }
      }
    }
  ],
  "routing": {
    "domainStrategy": "AsIs",
    "rules": [
      {
        "type": "field",
        "inboundTag": [
          "api"
        ],
        "outboundTag": "api",
        "enabled": true
      },
      {
        "id": "4903912855803990739",
        "type": "field",
        "outboundTag": "direct",
        "domain": [
          "domain:example-example.com",
          "domain:example-example2.com"
        ],
        "enabled": true
      },
      {
        "id": "5708028511442260423",
        "type": "field",
        "outboundTag": "block",
        "domain": [
          "geosite:category-ads-all"
        ],
        "enabled": true
      },
      {
        "id": "5285280340381945458",
        "type": "field",
        "outboundTag": "direct",
        "domain": [
          "geosite:cn"
        ],
        "enabled": true
      },
      {
        "id": "5063426339087196734",
        "type": "field",
        "outboundTag": "direct",
        "ip": [
          "geoip:private",
          "geoip:cn"
        ],
        "enabled": true
      },
      {
        "id": "4919950405029472934",
        "type": "field",
        "port": "0-65535",
        "outboundTag": "proxy",
        "enabled": true
      }
    ]
  }
}

```

## Xray-ip_3.json
```bash
<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.20.1</center>
</body>
</html>
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->

```

## Xray-ip_4.json
```bash
{
  "log": {
    "access": "",
    "error": "",
    "loglevel": "warning"
  },
  "inbounds": [
    {
      "tag": "socks",
      "port": 1080,
      "listen": "127.0.0.1",
      "protocol": "socks",
      "sniffing": {
        "enabled": true,
        "destOverride": [
          "http",
          "tls"
        ],
        "routeOnly": false
      },
      "settings": {
        "auth": "noauth",
        "udp": true,
        "allowTransparent": false
      }
    },
    {
      "tag": "http",
      "port": 1081,
      "listen": "127.0.0.1",
      "protocol": "http",
      "sniffing": {
        "enabled": true,
        "destOverride": [
          "http",
          "tls"
        ],
        "routeOnly": false
      },
      "settings": {
        "auth": "noauth",
        "udp": true,
        "allowTransparent": false
      }
    }
  ],
  "outbounds": [
    {
      "tag": "proxy",
      "protocol": "vmess",
      "settings": {
        "vnext": [
          {
            "address": "23.227.39.88",
            "port": 8080,
            "users": [
              {
                "id": "6dca5aed-9206-4496-9d1f-65c31c92f50b",
                "alterId": 0,
                "email": "t@t.tt",
                "security": "auto"
              }
            ]
          }
        ]
      },
      "streamSettings": {
        "network": "ws",
        "wsSettings": {
          "path": "6dca5aed-9206-4496-9d1f-65c31c92f50b-vm",
          "headers": {
            "Host": "proprietary-arc-durham-motorcycle.trycloudflare.com"
          }
        }
      },
      "mux": {
        "enabled": false,
        "concurrency": -1
      }
    },
    {
      "tag": "direct",
      "protocol": "freedom",
      "settings": {}
    },
    {
      "tag": "block",
      "protocol": "blackhole",
      "settings": {
        "response": {
          "type": "http"
        }
      }
    }
  ],
  "routing": {
    "domainStrategy": "AsIs",
    "rules": [
      {
        "type": "field",
        "inboundTag": [
          "api"
        ],
        "outboundTag": "api",
        "enabled": true
      },
      {
        "id": "4903912855803990739",
        "type": "field",
        "outboundTag": "direct",
        "domain": [
          "domain:example-example.com",
          "domain:example-example2.com"
        ],
        "enabled": true
      },
      {
        "id": "5708028511442260423",
        "type": "field",
        "outboundTag": "block",
        "domain": [
          "geosite:category-ads-all"
        ],
        "enabled": true
      },
      {
        "id": "5285280340381945458",
        "type": "field",
        "outboundTag": "direct",
        "domain": [
          "geosite:cn"
        ],
        "enabled": true
      },
      {
        "id": "5063426339087196734",
        "type": "field",
        "outboundTag": "direct",
        "ip": [
          "geoip:private",
          "geoip:cn"
        ],
        "enabled": true
      },
      {
        "id": "4919950405029472934",
        "type": "field",
        "port": "0-65535",
        "outboundTag": "proxy",
        "enabled": true
      }
    ]
  }
}

```

## clash.meta-ip_1.yaml
```bash
<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.20.1</center>
</body>
</html>
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->

```

## clash.meta-ip_2.yaml
```bash
secret: dongtaiwang.com
mixed-port: 7890
allow-lan: false
log-level: info
dns:
  enabled: true
  nameserver:
    - 119.29.29.29
    - 223.5.5.5
  fallback-filter:
    geoip: false
    ipcidr:
      - 240.0.0.0/4
      - 0.0.0.0/32
proxies:
  - {"name":"dongtaiwang.com_0","type":"vless","server":"64.31.55.42","port":23514,"udp":true,"uuid":"b17fa17d-13a0-4e8a-a398-8e549ea8b208","tls":true,"servername":"addons.mozilla.org","flow":"xtls-rprx-vision","network":"tcp","reality-opts":{"public-key":"ew6CB407JaI_WVD7QlD5QuvJTD7Pbv1oEbtis35-MRM"},"client-fingerprint":"chrome"}
  - {"name":"dongtaiwang.com_1","type":"vmess","server":"fbi.gov","port":8080,"cipher":"auto","uuid":"9084653a-ee34-4293-979e-7c2b50dffb84","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"configured-creek-relating-theater.trycloudflare.com","network":"ws","ws-opts":{"path":"9084653a-ee34-4293-979e-7c2b50dffb84-vm","headers":{"host":"configured-creek-relating-theater.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_2","type":"vmess","server":"fbi.gov","port":8080,"cipher":"auto","uuid":"ac750859-79e7-4507-ba93-e92584ac49e3","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"per-essex-patterns-bowling.trycloudflare.com","network":"ws","ws-opts":{"path":"ac750859-79e7-4507-ba93-e92584ac49e3-vm","headers":{"host":"per-essex-patterns-bowling.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_3","type":"vmess","server":"fbi.gov","port":8080,"cipher":"auto","uuid":"5f7934bf-a228-49a7-9572-5ce4377c34d5","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"uh-lawyers-instruments-kernel.trycloudflare.com","network":"ws","ws-opts":{"path":"5f7934bf-a228-49a7-9572-5ce4377c34d5-vm","headers":{"host":"uh-lawyers-instruments-kernel.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_4","type":"vmess","server":"fbi.gov","port":8080,"cipher":"auto","uuid":"0e5da13a-b148-4889-9d72-ad1d9d5aa9ad","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"widescreen-instruction-breakdown-postage.trycloudflare.com","network":"ws","ws-opts":{"path":"0e5da13a-b148-4889-9d72-ad1d9d5aa9ad-vm","headers":{"host":"widescreen-instruction-breakdown-postage.trycloudflare.com"}}}
proxy-groups:
  - name: 🚀 节点选择
    type: select
    proxies:
      - ♻️ 自动选择
      - DIRECT
      - dongtaiwang.com_0
      - dongtaiwang.com_1
      - dongtaiwang.com_2
      - dongtaiwang.com_3
      - dongtaiwang.com_4
  - name: ♻️ 自动选择
    type: url-test
    url: https://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    proxies:
      - dongtaiwang.com_0
      - dongtaiwang.com_1
      - dongtaiwang.com_2
      - dongtaiwang.com_3
      - dongtaiwang.com_4
  - name: 🌍 国外媒体
    type: select
    proxies:
      - 🚀 节点选择
      - ♻️ 自动选择
      - 🎯 全球直连
      - dongtaiwang.com_0
      - dongtaiwang.com_1
      - dongtaiwang.com_2
      - dongtaiwang.com_3
      - dongtaiwang.com_4
  - name: 📲 电报信息
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - dongtaiwang.com_0
      - dongtaiwang.com_1
      - dongtaiwang.com_2
      - dongtaiwang.com_3
      - dongtaiwang.com_4
  - name: Ⓜ️ 微软服务
    type: select
    proxies:
      - 🎯 全球直连
      - 🚀 节点选择
      - dongtaiwang.com_0
      - dongtaiwang.com_1
      - dongtaiwang.com_2
      - dongtaiwang.com_3
      - dongtaiwang.com_4
  - name: 🍎 苹果服务
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - dongtaiwang.com_0
      - dongtaiwang.com_1
      - dongtaiwang.com_2
      - dongtaiwang.com_3
      - dongtaiwang.com_4
  - name: 🎯 全球直连
    type: select
    proxies:
      - DIRECT
      - 🚀 节点选择
      - ♻️ 自动选择
  - name: 🛑 全球拦截
    type: select
    proxies:
      - REJECT
      - DIRECT
  - name: 🍃 应用净化
    type: select
    proxies:
      - REJECT
      - DIRECT
  - name: 🐟 漏网之鱼
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - ♻️ 自动选择
      - dongtaiwang.com_0
      - dongtaiwang.com_1
      - dongtaiwang.com_2
      - dongtaiwang.com_3
      - dongtaiwang.com_4
   

rules:
  - MATCH,🚀 节点选择

```

## clash.meta-ip_3.yaml
```bash
<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.20.1</center>
</body>
</html>
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->

```

## clash.meta-ip_4.yaml
```bash
secret: dongtaiwang.com
mixed-port: 7890
allow-lan: false
log-level: info
dns:
  enabled: true
  nameserver:
    - 119.29.29.29
    - 223.5.5.5
  fallback-filter:
    geoip: false
    ipcidr:
      - 240.0.0.0/4
      - 0.0.0.0/32
proxies:
  - {"name":"dongtaiwang.com_1","type":"vmess","server":"23.227.39.12","port":8080,"cipher":"auto","uuid":"9084653a-ee34-4293-979e-7c2b50dffb84","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"configured-creek-relating-theater.trycloudflare.com","network":"ws","ws-opts":{"path":"9084653a-ee34-4293-979e-7c2b50dffb84-vm","headers":{"host":"configured-creek-relating-theater.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_2","type":"vmess","server":"23.227.39.23","port":8080,"cipher":"auto","uuid":"ac750859-79e7-4507-ba93-e92584ac49e3","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"per-essex-patterns-bowling.trycloudflare.com","network":"ws","ws-opts":{"path":"ac750859-79e7-4507-ba93-e92584ac49e3-vm","headers":{"host":"per-essex-patterns-bowling.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_3","type":"vmess","server":"23.227.39.24","port":8080,"cipher":"auto","uuid":"5f7934bf-a228-49a7-9572-5ce4377c34d5","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"uh-lawyers-instruments-kernel.trycloudflare.com","network":"ws","ws-opts":{"path":"5f7934bf-a228-49a7-9572-5ce4377c34d5-vm","headers":{"host":"uh-lawyers-instruments-kernel.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_4","type":"vmess","server":"23.227.39.45","port":8080,"cipher":"auto","uuid":"0e5da13a-b148-4889-9d72-ad1d9d5aa9ad","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"widescreen-instruction-breakdown-postage.trycloudflare.com","network":"ws","ws-opts":{"path":"0e5da13a-b148-4889-9d72-ad1d9d5aa9ad-vm","headers":{"host":"widescreen-instruction-breakdown-postage.trycloudflare.com"}}}
proxy-groups:
  - name: 🚀 节点选择
    type: select
    proxies:
      - ♻️ 自动选择
      - DIRECT
      - dongtaiwang.com_1
      - dongtaiwang.com_2
      - dongtaiwang.com_3
      - dongtaiwang.com_4
  - name: ♻️ 自动选择
    type: url-test
    url: https://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    proxies:
      - dongtaiwang.com_1
      - dongtaiwang.com_2
      - dongtaiwang.com_3
      - dongtaiwang.com_4
  - name: 🌍 国外媒体
    type: select
    proxies:
      - 🚀 节点选择
      - ♻️ 自动选择
      - 🎯 全球直连
      - dongtaiwang.com_1
      - dongtaiwang.com_2
      - dongtaiwang.com_3
      - dongtaiwang.com_4
  - name: 📲 电报信息
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - dongtaiwang.com_1
      - dongtaiwang.com_2
      - dongtaiwang.com_3
      - dongtaiwang.com_4
  - name: Ⓜ️ 微软服务
    type: select
    proxies:
      - 🎯 全球直连
      - 🚀 节点选择
      - dongtaiwang.com_1
      - dongtaiwang.com_2
      - dongtaiwang.com_3
      - dongtaiwang.com_4
  - name: 🍎 苹果服务
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - dongtaiwang.com_1
      - dongtaiwang.com_2
      - dongtaiwang.com_3
      - dongtaiwang.com_4
  - name: 🎯 全球直连
    type: select
    proxies:
      - DIRECT
      - 🚀 节点选择
      - ♻️ 自动选择
  - name: 🛑 全球拦截
    type: select
    proxies:
      - REJECT
      - DIRECT
  - name: 🍃 应用净化
    type: select
    proxies:
      - REJECT
      - DIRECT
  - name: 🐟 漏网之鱼
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - ♻️ 自动选择
      - dongtaiwang.com_1
      - dongtaiwang.com_2
      - dongtaiwang.com_3
      - dongtaiwang.com_4
   

rules:
  - MATCH,🚀 节点选择


```

## clash.meta-ip_5.yaml
```bash
<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.20.1</center>
</body>
</html>
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->

```

## clash.meta-ip_6.yaml
```bash
secret: dongtaiwang.com
mixed-port: 7890
allow-lan: false
log-level: info
dns:
  enabled: true
  nameserver:
    - 119.29.29.29
    - 223.5.5.5
  fallback-filter:
    geoip: false
    ipcidr:
      - 240.0.0.0/4
      - 0.0.0.0/32
proxies:
  - {"name":"dongtaiwang.com_1","type":"vmess","server":"fbi.gov","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_2","type":"vmess","server":"fbi.gov","port":8080,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_3","type":"vmess","server":"fbi.gov","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_4","type":"vmess","server":"fbi.gov","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_5","type":"vmess","server":"yh1.freeh1.xyz","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_6","type":"vmess","server":"yh1.freeh1.xyz","port":8080,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_7","type":"vmess","server":"yh1.freeh1.xyz","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_8","type":"vmess","server":"yh1.freeh1.xyz","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_9","type":"vmess","server":"yh2.freeh1.xyz","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_10","type":"vmess","server":"yh2.freeh1.xyz","port":8080,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_11","type":"vmess","server":"yh2.freeh1.xyz","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_12","type":"vmess","server":"yh3.freeh1.xyz","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_13","type":"vmess","server":"yh3.freeh1.xyz","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_14","type":"vmess","server":"yh3.freeh1.xyz","port":8080,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_15","type":"vmess","server":"yh3.freeh1.xyz","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_16","type":"vmess","server":"yh3.freeh1.xyz","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}

proxy-groups:
  - name: 🚀 节点选择
    type: select
    proxies:
      - ♻️ 自动选择
      - DIRECT
      - dongtaiwang.com_1
      - dongtaiwang.com_2
      - dongtaiwang.com_3
      - dongtaiwang.com_4
      - dongtaiwang.com_5
      - dongtaiwang.com_6
      - dongtaiwang.com_7
      - dongtaiwang.com_8
      - dongtaiwang.com_9
      - dongtaiwang.com_10
      - dongtaiwang.com_11
      - dongtaiwang.com_12
      - dongtaiwang.com_13
      - dongtaiwang.com_14
      - dongtaiwang.com_15
      - dongtaiwang.com_16
  - name: ♻️ 自动选择
    type: url-test
    url: https://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    proxies:
      - dongtaiwang.com_1
      - dongtaiwang.com_2
      - dongtaiwang.com_3
      - dongtaiwang.com_4
      - dongtaiwang.com_5
      - dongtaiwang.com_6
      - dongtaiwang.com_7
      - dongtaiwang.com_8
      - dongtaiwang.com_9
      - dongtaiwang.com_10
      - dongtaiwang.com_11
      - dongtaiwang.com_12
      - dongtaiwang.com_13
      - dongtaiwang.com_14
      - dongtaiwang.com_15
      - dongtaiwang.com_16
  - name: 🌍 国外媒体
    type: select
    proxies:
      - 🚀 节点选择
      - ♻️ 自动选择
      - 🎯 全球直连
      - dongtaiwang.com_1
      - dongtaiwang.com_2
      - dongtaiwang.com_3
      - dongtaiwang.com_4
      - dongtaiwang.com_5
      - dongtaiwang.com_6
      - dongtaiwang.com_7
      - dongtaiwang.com_8
      - dongtaiwang.com_9
      - dongtaiwang.com_10
      - dongtaiwang.com_11
      - dongtaiwang.com_12
      - dongtaiwang.com_13
      - dongtaiwang.com_14
      - dongtaiwang.com_15
      - dongtaiwang.com_16
  - name: 📲 电报信息
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - dongtaiwang.com_1
      - dongtaiwang.com_2
      - dongtaiwang.com_3
      - dongtaiwang.com_4
      - dongtaiwang.com_5
      - dongtaiwang.com_6
      - dongtaiwang.com_7
      - dongtaiwang.com_8
      - dongtaiwang.com_9
      - dongtaiwang.com_10
      - dongtaiwang.com_11
      - dongtaiwang.com_12
      - dongtaiwang.com_13
      - dongtaiwang.com_14
      - dongtaiwang.com_15
      - dongtaiwang.com_16
  - name: Ⓜ️ 微软服务
    type: select
    proxies:
      - 🎯 全球直连
      - 🚀 节点选择
      - dongtaiwang.com_1
      - dongtaiwang.com_2
      - dongtaiwang.com_3
      - dongtaiwang.com_4
      - dongtaiwang.com_5
      - dongtaiwang.com_6
      - dongtaiwang.com_7
      - dongtaiwang.com_8
      - dongtaiwang.com_9
      - dongtaiwang.com_10
      - dongtaiwang.com_11
      - dongtaiwang.com_12
      - dongtaiwang.com_13
      - dongtaiwang.com_14
      - dongtaiwang.com_15
      - dongtaiwang.com_16
  - name: 🍎 苹果服务
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - dongtaiwang.com_1
      - dongtaiwang.com_2
      - dongtaiwang.com_3
      - dongtaiwang.com_4
      - dongtaiwang.com_5
      - dongtaiwang.com_6
      - dongtaiwang.com_7
      - dongtaiwang.com_8
      - dongtaiwang.com_9
      - dongtaiwang.com_10
      - dongtaiwang.com_11
      - dongtaiwang.com_12
      - dongtaiwang.com_13
      - dongtaiwang.com_14
      - dongtaiwang.com_15
      - dongtaiwang.com_16
  - name: 🎯 全球直连
    type: select
    proxies:
      - DIRECT
      - 🚀 节点选择
      - ♻️ 自动选择
  - name: 🛑 全球拦截
    type: select
    proxies:
      - REJECT
      - DIRECT
  - name: 🍃 应用净化
    type: select
    proxies:
      - REJECT
      - DIRECT
  - name: 🐟 漏网之鱼
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - ♻️ 自动选择
      - dongtaiwang.com_1
      - dongtaiwang.com_2
      - dongtaiwang.com_3
      - dongtaiwang.com_4
      - dongtaiwang.com_5
      - dongtaiwang.com_6
      - dongtaiwang.com_7
      - dongtaiwang.com_8
      - dongtaiwang.com_9
      - dongtaiwang.com_10
      - dongtaiwang.com_11
      - dongtaiwang.com_12
      - dongtaiwang.com_13
      - dongtaiwang.com_14
      - dongtaiwang.com_15
      - dongtaiwang.com_16
   

rules:
  - MATCH,🚀 节点选择


```

## hysteria-ip_1.json
```bash
<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.20.1</center>
</body>
</html>
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->

```

## hysteria-ip_2.json
```bash
{
"server": "167.160.91.115:41189",
"protocol": "udp",
"up_mbps": 11,
"down_mbps": 55,
"http": {
"listen": "127.0.0.1:1081",
"timeout" : 250,
"disable_udp": false
},
"socks5": {
"listen": "127.0.0.1:1080",
"timeout": 250,
"disable_udp": false
},
"obfs": "",
"auth_str": "bWAwIqINo7XDm1fUlXQGBifVIXoYs1ylgVKqWFKzK1XyDKuwNF",
"alpn": "h3",
"server_name": "www.amazon.cn",
"insecure": true,
"recv_window_conn": 5767168,
"recv_window": 23068672,
"disable_mtu_discovery": true,
"resolver": "https://223.5.5.5/dns-query",
"retry": 3,
"retry_interval": 3,
"quit_on_disconnect": false,
"handshake_timeout": 15,
"idle_timeout": 30,
"fast_open": true,
"hop_interval": 120
}

```

## hysteria-ip_3.json
```bash
<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.20.1</center>
</body>
</html>
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->

```

## hysteria-ip_4.json
```bash
{
"server": "www.dtku40.xyz:18490",
"protocol": "udp",
"up_mbps": 11,
"down_mbps": 55,
"http": {
"listen": "127.0.0.1:1081",
"timeout" : 150,
"disable_udp": false
},
"socks5": {
"listen": "127.0.0.1:1080",
"timeout": 150,
"disable_udp": false
},
"obfs": "",
"auth_str": "dongtaiwang.com",
"alpn": "h3",
"server_name": "bing.com",
"insecure": true,
"recv_window_conn": 69206016,
"recv_window": 276824064,
"disable_mtu_discovery": true,
"resolver": "https://223.5.5.5/dns-query",
"retry": 3,
"retry_interval": 3,
"quit_on_disconnect": false,
"handshake_timeout": 15,
"idle_timeout": 30,
"fast_open": true,
"hop_interval": 120
}

```

## hysteria2-ip_1.json
```bash
<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.20.1</center>
</body>
</html>
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->

```

## hysteria2-ip_2.json
```bash
{
  "server": "62.210.103.0:22483",
  "auth": "dongtaiwang.com",
  "tls": {
    "sni": "www.bing.com",
    "insecure": true
  },
  "quic": {
    "initStreamReceiveWindow": 16777216,
    "maxStreamReceiveWindow": 16777216,
    "initConnReceiveWindow": 33554432,
    "maxConnReceiveWindow": 33554432
  },
  "socks5": {
    "listen": "127.0.0.1:1080"
  },
  "transport": {
    "udp": {
      "hopInterval": "30s"
    }
  }
}

```

## hysteria2-ip_3.json
```bash
<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.20.1</center>
</body>
</html>
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->

```

## hysteria2-ip_4.json
```bash
{
  "server": "62.210.103.0:22483",
  "auth": "dongtaiwang.com",
  "tls": {
    "sni": "www.bing.com",
    "insecure": true
  },
  "quic": {
    "initStreamReceiveWindow": 16777216,
    "maxStreamReceiveWindow": 16777216,
    "initConnReceiveWindow": 33554432,
    "maxConnReceiveWindow": 33554432
  },
  "socks5": {
    "listen": "127.0.0.1:1080"
  },
  "transport": {
    "udp": {
      "hopInterval": "30s"
    }
  }
}

```

## naiveproxy-ip_1.json
```bash
<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.20.1</center>
</body>
</html>
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->

```

## naiveproxy-ip_2.json
```bash
{
  "listen": "socks://127.0.0.1:1080",
  "proxy": "https://dongtaiwang.com:dongtaiwang.com@www.dtku50.xyz:443"
}

```

## singbox-ip_1.json
```bash
<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.20.1</center>
</body>
</html>
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->

```

## singbox-ip_2.json
```bash
{
  "inbounds": [
    {
      "type": "mixed",
      "tag": "mixed-in",
      "listen": "::",
      "listen_port": 1080,
      "sniff": true,
      "set_system_proxy": false
    }
  ],
  "outbounds": [
    {
      "type": "hysteria",
      "tag": "dongtaiwang.com",
      "server": "www.dtku50.xyz", 
      "server_port": 11229,
      "up_mbps": 11, 
      "down_mbps": 55,
      "auth_str": "dongtaiwang.com",
      "tls": {
        "enabled": true,
        "insecure": true,
        "server_name": "bing.com", 
        "alpn": [
          "h3"
        ]

      }
    }
  ] 
	 
}


```
