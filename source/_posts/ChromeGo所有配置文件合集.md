
---
title: ChromeGo所有配置文件合集 
date: 2024-02-12 09:14:40
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

> Last Update Time: 2024-02-12 09:14:40
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
  - {name: "ip", type: hysteria2, server: 45.150.165.84, port: 8881, password: d017e316-82cb-441c-8eea-7b5e9de64a20, obfs: salamander, obfs-password: d017e316-82cb-441c-8eea-7b5e9de64a20, skip-cert-verify: true, up: "2 Mbps", down: "10 Mbps"}
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
      "protocol": "vless",
      "settings": {
        "vnext": [
          {
            "address": "51.159.77.153",
            "port": 11111,
            "users": [
              {
                "id": "9cc39477-0d85-4419-84d4-fb7fc77668b3",
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
          "serverName": "m.media-amazon.com",
          "fingerprint": "chrome",
          "show": false,
          "publicKey": "yKXmLTmXAi-BHBg3JpCz-NWUmVcKlfm7iMmVoq7YQx0",
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
  fallback:
    - 8.8.8.8
    - 8.8.4.4
    - tls://1.0.0.1:853
    - tls://dns.google:853
proxies:
  - {"name":"dongtaiwang.com_1","type":"tuic","server":"109.104.152.144","port":44411,"udp":true,"uuid":"7bda06fd-e4af-4115-8aa3-f021832cfa78","password":dongtaiwang.com,"alpn":["h3"],"disable-sni":true,"reduce-rtt":true,"udp-relay-mode":native,"congestion-controller":"bbr"}
proxy-groups:
  - name: 🚀 节点选择
    type: select
    proxies:
      - ♻️ 自动选择
      - DIRECT
      - dongtaiwang.com_1
  - name: ♻️ 自动选择
    type: url-test
    url: https://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    proxies:
      - dongtaiwang.com_1
  - name: 🌍 国外媒体
    type: select
    proxies:
      - 🚀 节点选择
      - ♻️ 自动选择
      - 🎯 全球直连
      - dongtaiwang.com_1
  - name: 📲 电报信息
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - dongtaiwang.com_1
  - name: Ⓜ️ 微软服务
    type: select
    proxies:
      - 🎯 全球直连
      - 🚀 节点选择
      - dongtaiwang.com_1
  - name: 🍎 苹果服务
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - dongtaiwang.com_1
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
  fallback:
    - 8.8.8.8
    - 8.8.4.4
    - tls://1.0.0.1:853
    - tls://dns.google:853
proxies:
  - {"name":"dongtaiwang.com_0","type":"vless","server":"109.104.152.101","port":11111,"udp":true,"uuid":"9cc39477-0d85-4419-84d4-fb7fc77668b3","tls":true,"servername":"m.media-amazon.com","flow":"xtls-rprx-vision","network":"tcp","reality-opts":{"public-key":"yKXmLTmXAi-BHBg3JpCz-NWUmVcKlfm7iMmVoq7YQx0","short-id":"6ba85179e30d4fc2"},"client-fingerprint":"chrome"}
proxy-groups:
  - name: 🚀 节点选择
    type: select
    proxies:
      - ♻️ 自动选择
      - DIRECT
      - dongtaiwang.com_0
  - name: ♻️ 自动选择
    type: url-test
    url: https://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    proxies:
      - dongtaiwang.com_0
  - name: 🌍 国外媒体
    type: select
    proxies:
      - 🚀 节点选择
      - ♻️ 自动选择
      - 🎯 全球直连
      - dongtaiwang.com_0
  - name: 📲 电报信息
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - dongtaiwang.com_0
  - name: Ⓜ️ 微软服务
    type: select
    proxies:
      - 🎯 全球直连
      - 🚀 节点选择
      - dongtaiwang.com_0
  - name: 🍎 苹果服务
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - dongtaiwang.com_0
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
  fallback:
    - 8.8.8.8
    - 8.8.4.4
    - tls://1.0.0.1:853
    - tls://dns.google:853
proxies:
  - {"name":"95878aa5-VLESS_WS_1","type":"vless","server":"198.41.193.226","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_2","type":"vless","server":"104.27.97.91","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_3","type":"vless","server":"108.162.196.107","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_4","type":"vless","server":"104.22.46.253","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_5","type":"vless","server":"173.245.49.56","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_6","type":"vless","server":"198.41.195.168","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_7","type":"vless","server":"103.21.244.189","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_8","type":"vless","server":"104.21.35.228","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_9","type":"vless","server":"162.159.38.71","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_10","type":"vless","server":"104.19.7.150","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_11","type":"vless","server":"108.162.196.74","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_12","type":"vless","server":"104.18.9.181","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_13","type":"vless","server":"190.93.245.188","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_14","type":"vless","server":"198.41.218.199","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_15","type":"vless","server":"104.18.110.163","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_16","type":"vless","server":"190.93.246.114","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_17","type":"vless","server":"103.21.244.236","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_18","type":"vless","server":"162.159.24.166","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_19","type":"vless","server":"104.25.69.69","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_20","type":"vless","server":"104.16.196.143","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_21","type":"vless","server":"103.21.244.162","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_22","type":"vless","server":"172.66.138.14","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_23","type":"vless","server":"172.64.49.33","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_24","type":"vless","server":"104.25.113.186","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_25","type":"vless","server":"104.20.5.9","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_26","type":"vless","server":"104.25.211.145","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_27","type":"vless","server":"172.67.209.51","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_28","type":"vless","server":"104.18.141.86","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_29","type":"vless","server":"188.114.97.19","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_30","type":"vless","server":"104.27.16.75","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_31","type":"vless","server":"104.18.95.234","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_32","type":"vless","server":"198.41.202.98","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_33","type":"vless","server":"162.159.24.244","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_34","type":"vless","server":"104.24.132.228","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_35","type":"vless","server":"198.41.209.249","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_36","type":"vless","server":"104.24.88.199","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_37","type":"vless","server":"103.21.244.248","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_38","type":"vless","server":"104.20.253.93","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_39","type":"vless","server":"173.245.58.18","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_40","type":"vless","server":"104.17.11.252","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_41","type":"vless","server":"104.24.18.7","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_42","type":"vless","server":"104.16.38.162","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_43","type":"vless","server":"108.162.194.144","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_44","type":"vless","server":"190.93.244.218","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_45","type":"vless","server":"104.19.45.11","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_46","type":"vless","server":"188.114.96.211","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_47","type":"vless","server":"172.67.152.22","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_48","type":"vless","server":"104.16.75.128","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_49","type":"vless","server":"198.41.202.169","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_50","type":"vless","server":"104.24.57.248","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_51","type":"vless","server":"173.245.49.207","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_52","type":"vless","server":"104.24.226.143","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_53","type":"vless","server":"173.245.59.17","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_54","type":"vless","server":"104.17.2.38","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_55","type":"vless","server":"162.159.6.199","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_56","type":"vless","server":"141.101.113.239","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_57","type":"vless","server":"172.64.173.200","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_58","type":"vless","server":"104.21.235.122","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_59","type":"vless","server":"190.93.246.107","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_60","type":"vless","server":"188.114.97.27","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_61","type":"vless","server":"190.93.244.47","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_62","type":"vless","server":"173.245.58.237","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_63","type":"vless","server":"172.67.166.72","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_64","type":"vless","server":"190.93.245.106","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_65","type":"vless","server":"104.27.107.221","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_66","type":"vless","server":"103.21.244.137","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_67","type":"vless","server":"104.22.71.28","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_68","type":"vless","server":"104.17.123.53","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_69","type":"vless","server":"104.21.25.95","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_70","type":"vless","server":"104.24.190.226","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_71","type":"vless","server":"104.27.61.67","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_72","type":"vless","server":"104.24.171.195","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_73","type":"vless","server":"173.245.49.195","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_74","type":"vless","server":"190.93.247.5","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_75","type":"vless","server":"108.162.192.179","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_76","type":"vless","server":"198.41.216.62","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_77","type":"vless","server":"104.17.6.218","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_78","type":"vless","server":"103.21.244.219","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_79","type":"vless","server":"141.101.121.69","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_80","type":"vless","server":"104.25.12.88","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_81","type":"vless","server":"104.24.74.248","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_82","type":"vless","server":"104.18.9.239","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_83","type":"vless","server":"104.16.247.95","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_84","type":"vless","server":"104.25.19.37","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_85","type":"vless","server":"104.18.238.119","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_86","type":"vless","server":"104.24.214.188","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_87","type":"vless","server":"172.66.142.115","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_88","type":"vless","server":"103.21.244.126","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_89","type":"vless","server":"103.21.244.74","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_90","type":"vless","server":"103.21.244.94","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_91","type":"vless","server":"104.20.87.76","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_92","type":"vless","server":"104.25.122.116","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_93","type":"vless","server":"190.93.245.66","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_94","type":"vless","server":"104.18.23.136","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_95","type":"vless","server":"104.25.254.11","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_96","type":"vless","server":"104.25.94.175","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_97","type":"vless","server":"141.101.121.18","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_98","type":"vless","server":"162.159.133.78","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_99","type":"vless","server":"173.245.59.173","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_100","type":"vless","server":"190.93.247.107","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_101","type":"vless","server":"162.159.252.249","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_102","type":"vless","server":"104.17.12.96","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_103","type":"vless","server":"162.159.21.6","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_104","type":"vless","server":"103.21.244.125","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_105","type":"vless","server":"104.16.137.106","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_106","type":"vless","server":"172.64.149.192","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_107","type":"vless","server":"104.24.16.226","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_108","type":"vless","server":"172.67.103.221","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_109","type":"vless","server":"188.114.97.111","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_110","type":"vless","server":"172.67.109.53","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_111","type":"vless","server":"104.20.252.36","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_112","type":"vless","server":"104.20.125.193","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_113","type":"vless","server":"188.114.99.120","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_114","type":"vless","server":"108.162.193.37","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_115","type":"vless","server":"104.17.103.194","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_116","type":"vless","server":"198.41.200.139","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_117","type":"vless","server":"188.114.97.222","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_118","type":"vless","server":"190.93.247.68","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_119","type":"vless","server":"104.17.87.110","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_120","type":"vless","server":"172.67.155.77","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_121","type":"vless","server":"162.159.26.15","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_122","type":"vless","server":"198.41.217.152","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_123","type":"vless","server":"104.18.244.225","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_124","type":"vless","server":"190.93.245.73","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_125","type":"vless","server":"104.27.41.157","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_126","type":"vless","server":"141.101.121.106","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_127","type":"vless","server":"104.24.31.205","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_128","type":"vless","server":"198.41.220.53","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_129","type":"vless","server":"104.24.178.127","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_130","type":"vless","server":"162.159.240.167","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_131","type":"vless","server":"103.21.244.141","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_132","type":"vless","server":"172.67.19.224","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_133","type":"vless","server":"104.25.225.101","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_134","type":"vless","server":"188.114.96.162","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_135","type":"vless","server":"104.18.135.212","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_136","type":"vless","server":"104.19.246.22","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
  - {"name":"95878aa5-VLESS_WS_137","type":"vless","server":"172.64.164.162","port":443,"uuid":"95878aa5-a695-4b88-b502-55c05c998cf2","tls":true,"servername":"lg1.dtku41.xyz","network":"ws","ws-opts":{"path":"/ugrlws","headers":{"host":"lg1.dtku41.xyz"}}}
proxy-groups:
  - name: 🚀 节点选择
    type: select
    proxies:
      - ♻️ 自动选择
      - DIRECT
      - 95878aa5-VLESS_WS_1
      - 95878aa5-VLESS_WS_2
      - 95878aa5-VLESS_WS_3
      - 95878aa5-VLESS_WS_4
      - 95878aa5-VLESS_WS_5
      - 95878aa5-VLESS_WS_6
      - 95878aa5-VLESS_WS_7
      - 95878aa5-VLESS_WS_8
      - 95878aa5-VLESS_WS_9
      - 95878aa5-VLESS_WS_10
      - 95878aa5-VLESS_WS_11
      - 95878aa5-VLESS_WS_12
      - 95878aa5-VLESS_WS_13
      - 95878aa5-VLESS_WS_14
      - 95878aa5-VLESS_WS_15
      - 95878aa5-VLESS_WS_16
      - 95878aa5-VLESS_WS_17
      - 95878aa5-VLESS_WS_18
      - 95878aa5-VLESS_WS_19
      - 95878aa5-VLESS_WS_20
      - 95878aa5-VLESS_WS_21
      - 95878aa5-VLESS_WS_22
      - 95878aa5-VLESS_WS_23
      - 95878aa5-VLESS_WS_24
      - 95878aa5-VLESS_WS_25
      - 95878aa5-VLESS_WS_26
      - 95878aa5-VLESS_WS_27
      - 95878aa5-VLESS_WS_28
      - 95878aa5-VLESS_WS_29
      - 95878aa5-VLESS_WS_30
      - 95878aa5-VLESS_WS_31
      - 95878aa5-VLESS_WS_32
      - 95878aa5-VLESS_WS_33
      - 95878aa5-VLESS_WS_34
      - 95878aa5-VLESS_WS_35
      - 95878aa5-VLESS_WS_36
      - 95878aa5-VLESS_WS_37
      - 95878aa5-VLESS_WS_38
      - 95878aa5-VLESS_WS_39
      - 95878aa5-VLESS_WS_40
      - 95878aa5-VLESS_WS_41
      - 95878aa5-VLESS_WS_42
      - 95878aa5-VLESS_WS_43
      - 95878aa5-VLESS_WS_44
      - 95878aa5-VLESS_WS_45
      - 95878aa5-VLESS_WS_46
      - 95878aa5-VLESS_WS_47
      - 95878aa5-VLESS_WS_48
      - 95878aa5-VLESS_WS_49
      - 95878aa5-VLESS_WS_50
      - 95878aa5-VLESS_WS_51
      - 95878aa5-VLESS_WS_52
      - 95878aa5-VLESS_WS_53
      - 95878aa5-VLESS_WS_54
      - 95878aa5-VLESS_WS_55
      - 95878aa5-VLESS_WS_56
      - 95878aa5-VLESS_WS_57
      - 95878aa5-VLESS_WS_58
      - 95878aa5-VLESS_WS_59
      - 95878aa5-VLESS_WS_60
      - 95878aa5-VLESS_WS_61
      - 95878aa5-VLESS_WS_62
      - 95878aa5-VLESS_WS_63
      - 95878aa5-VLESS_WS_64
      - 95878aa5-VLESS_WS_65
      - 95878aa5-VLESS_WS_66
      - 95878aa5-VLESS_WS_67
      - 95878aa5-VLESS_WS_68
      - 95878aa5-VLESS_WS_69
      - 95878aa5-VLESS_WS_70
      - 95878aa5-VLESS_WS_71
      - 95878aa5-VLESS_WS_72
      - 95878aa5-VLESS_WS_73
      - 95878aa5-VLESS_WS_74
      - 95878aa5-VLESS_WS_75
      - 95878aa5-VLESS_WS_76
      - 95878aa5-VLESS_WS_77
      - 95878aa5-VLESS_WS_78
      - 95878aa5-VLESS_WS_79
      - 95878aa5-VLESS_WS_80
      - 95878aa5-VLESS_WS_81
      - 95878aa5-VLESS_WS_82
      - 95878aa5-VLESS_WS_83
      - 95878aa5-VLESS_WS_84
      - 95878aa5-VLESS_WS_85
      - 95878aa5-VLESS_WS_86
      - 95878aa5-VLESS_WS_87
      - 95878aa5-VLESS_WS_88
      - 95878aa5-VLESS_WS_89
      - 95878aa5-VLESS_WS_90
      - 95878aa5-VLESS_WS_91
      - 95878aa5-VLESS_WS_92
      - 95878aa5-VLESS_WS_93
      - 95878aa5-VLESS_WS_94
      - 95878aa5-VLESS_WS_95
      - 95878aa5-VLESS_WS_96
      - 95878aa5-VLESS_WS_97
      - 95878aa5-VLESS_WS_98
      - 95878aa5-VLESS_WS_99
      - 95878aa5-VLESS_WS_100
      - 95878aa5-VLESS_WS_101
      - 95878aa5-VLESS_WS_102
      - 95878aa5-VLESS_WS_103
      - 95878aa5-VLESS_WS_104
      - 95878aa5-VLESS_WS_105
      - 95878aa5-VLESS_WS_106
      - 95878aa5-VLESS_WS_107
      - 95878aa5-VLESS_WS_108
      - 95878aa5-VLESS_WS_109
      - 95878aa5-VLESS_WS_110
      - 95878aa5-VLESS_WS_111
      - 95878aa5-VLESS_WS_112
      - 95878aa5-VLESS_WS_113
      - 95878aa5-VLESS_WS_114
      - 95878aa5-VLESS_WS_115
      - 95878aa5-VLESS_WS_116
      - 95878aa5-VLESS_WS_117
      - 95878aa5-VLESS_WS_118
      - 95878aa5-VLESS_WS_119
      - 95878aa5-VLESS_WS_120
      - 95878aa5-VLESS_WS_121
      - 95878aa5-VLESS_WS_122
      - 95878aa5-VLESS_WS_123
      - 95878aa5-VLESS_WS_124
      - 95878aa5-VLESS_WS_125
      - 95878aa5-VLESS_WS_126
      - 95878aa5-VLESS_WS_127
      - 95878aa5-VLESS_WS_128
      - 95878aa5-VLESS_WS_129
      - 95878aa5-VLESS_WS_130
      - 95878aa5-VLESS_WS_131
      - 95878aa5-VLESS_WS_132
      - 95878aa5-VLESS_WS_133
      - 95878aa5-VLESS_WS_134
      - 95878aa5-VLESS_WS_135
      - 95878aa5-VLESS_WS_136
      - 95878aa5-VLESS_WS_137
  - name: ♻️ 自动选择
    type: url-test
    url: https://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    proxies:
      - 95878aa5-VLESS_WS_1
      - 95878aa5-VLESS_WS_2
      - 95878aa5-VLESS_WS_3
      - 95878aa5-VLESS_WS_4
      - 95878aa5-VLESS_WS_5
      - 95878aa5-VLESS_WS_6
      - 95878aa5-VLESS_WS_7
      - 95878aa5-VLESS_WS_8
      - 95878aa5-VLESS_WS_9
      - 95878aa5-VLESS_WS_10
      - 95878aa5-VLESS_WS_11
      - 95878aa5-VLESS_WS_12
      - 95878aa5-VLESS_WS_13
      - 95878aa5-VLESS_WS_14
      - 95878aa5-VLESS_WS_15
      - 95878aa5-VLESS_WS_16
      - 95878aa5-VLESS_WS_17
      - 95878aa5-VLESS_WS_18
      - 95878aa5-VLESS_WS_19
      - 95878aa5-VLESS_WS_20
      - 95878aa5-VLESS_WS_21
      - 95878aa5-VLESS_WS_22
      - 95878aa5-VLESS_WS_23
      - 95878aa5-VLESS_WS_24
      - 95878aa5-VLESS_WS_25
      - 95878aa5-VLESS_WS_26
      - 95878aa5-VLESS_WS_27
      - 95878aa5-VLESS_WS_28
      - 95878aa5-VLESS_WS_29
      - 95878aa5-VLESS_WS_30
      - 95878aa5-VLESS_WS_31
      - 95878aa5-VLESS_WS_32
      - 95878aa5-VLESS_WS_33
      - 95878aa5-VLESS_WS_34
      - 95878aa5-VLESS_WS_35
      - 95878aa5-VLESS_WS_36
      - 95878aa5-VLESS_WS_37
      - 95878aa5-VLESS_WS_38
      - 95878aa5-VLESS_WS_39
      - 95878aa5-VLESS_WS_40
      - 95878aa5-VLESS_WS_41
      - 95878aa5-VLESS_WS_42
      - 95878aa5-VLESS_WS_43
      - 95878aa5-VLESS_WS_44
      - 95878aa5-VLESS_WS_45
      - 95878aa5-VLESS_WS_46
      - 95878aa5-VLESS_WS_47
      - 95878aa5-VLESS_WS_48
      - 95878aa5-VLESS_WS_49
      - 95878aa5-VLESS_WS_50
      - 95878aa5-VLESS_WS_51
      - 95878aa5-VLESS_WS_52
      - 95878aa5-VLESS_WS_53
      - 95878aa5-VLESS_WS_54
      - 95878aa5-VLESS_WS_55
      - 95878aa5-VLESS_WS_56
      - 95878aa5-VLESS_WS_57
      - 95878aa5-VLESS_WS_58
      - 95878aa5-VLESS_WS_59
      - 95878aa5-VLESS_WS_60
      - 95878aa5-VLESS_WS_61
      - 95878aa5-VLESS_WS_62
      - 95878aa5-VLESS_WS_63
      - 95878aa5-VLESS_WS_64
      - 95878aa5-VLESS_WS_65
      - 95878aa5-VLESS_WS_66
      - 95878aa5-VLESS_WS_67
      - 95878aa5-VLESS_WS_68
      - 95878aa5-VLESS_WS_69
      - 95878aa5-VLESS_WS_70
      - 95878aa5-VLESS_WS_71
      - 95878aa5-VLESS_WS_72
      - 95878aa5-VLESS_WS_73
      - 95878aa5-VLESS_WS_74
      - 95878aa5-VLESS_WS_75
      - 95878aa5-VLESS_WS_76
      - 95878aa5-VLESS_WS_77
      - 95878aa5-VLESS_WS_78
      - 95878aa5-VLESS_WS_79
      - 95878aa5-VLESS_WS_80
      - 95878aa5-VLESS_WS_81
      - 95878aa5-VLESS_WS_82
      - 95878aa5-VLESS_WS_83
      - 95878aa5-VLESS_WS_84
      - 95878aa5-VLESS_WS_85
      - 95878aa5-VLESS_WS_86
      - 95878aa5-VLESS_WS_87
      - 95878aa5-VLESS_WS_88
      - 95878aa5-VLESS_WS_89
      - 95878aa5-VLESS_WS_90
      - 95878aa5-VLESS_WS_91
      - 95878aa5-VLESS_WS_92
      - 95878aa5-VLESS_WS_93
      - 95878aa5-VLESS_WS_94
      - 95878aa5-VLESS_WS_95
      - 95878aa5-VLESS_WS_96
      - 95878aa5-VLESS_WS_97
      - 95878aa5-VLESS_WS_98
      - 95878aa5-VLESS_WS_99
      - 95878aa5-VLESS_WS_100
      - 95878aa5-VLESS_WS_101
      - 95878aa5-VLESS_WS_102
      - 95878aa5-VLESS_WS_103
      - 95878aa5-VLESS_WS_104
      - 95878aa5-VLESS_WS_105
      - 95878aa5-VLESS_WS_106
      - 95878aa5-VLESS_WS_107
      - 95878aa5-VLESS_WS_108
      - 95878aa5-VLESS_WS_109
      - 95878aa5-VLESS_WS_110
      - 95878aa5-VLESS_WS_111
      - 95878aa5-VLESS_WS_112
      - 95878aa5-VLESS_WS_113
      - 95878aa5-VLESS_WS_114
      - 95878aa5-VLESS_WS_115
      - 95878aa5-VLESS_WS_116
      - 95878aa5-VLESS_WS_117
      - 95878aa5-VLESS_WS_118
      - 95878aa5-VLESS_WS_119
      - 95878aa5-VLESS_WS_120
      - 95878aa5-VLESS_WS_121
      - 95878aa5-VLESS_WS_122
      - 95878aa5-VLESS_WS_123
      - 95878aa5-VLESS_WS_124
      - 95878aa5-VLESS_WS_125
      - 95878aa5-VLESS_WS_126
      - 95878aa5-VLESS_WS_127
      - 95878aa5-VLESS_WS_128
      - 95878aa5-VLESS_WS_129
      - 95878aa5-VLESS_WS_130
      - 95878aa5-VLESS_WS_131
      - 95878aa5-VLESS_WS_132
      - 95878aa5-VLESS_WS_133
      - 95878aa5-VLESS_WS_134
      - 95878aa5-VLESS_WS_135
      - 95878aa5-VLESS_WS_136
      - 95878aa5-VLESS_WS_137
  - name: 🌍 国外媒体
    type: select
    proxies:
      - 🚀 节点选择
      - ♻️ 自动选择
      - 🎯 全球直连
      - 95878aa5-VLESS_WS_1
      - 95878aa5-VLESS_WS_2
      - 95878aa5-VLESS_WS_3
      - 95878aa5-VLESS_WS_4
      - 95878aa5-VLESS_WS_5
      - 95878aa5-VLESS_WS_6
      - 95878aa5-VLESS_WS_7
      - 95878aa5-VLESS_WS_8
      - 95878aa5-VLESS_WS_9
      - 95878aa5-VLESS_WS_10
      - 95878aa5-VLESS_WS_11
      - 95878aa5-VLESS_WS_12
      - 95878aa5-VLESS_WS_13
      - 95878aa5-VLESS_WS_14
      - 95878aa5-VLESS_WS_15
      - 95878aa5-VLESS_WS_16
      - 95878aa5-VLESS_WS_17
      - 95878aa5-VLESS_WS_18
      - 95878aa5-VLESS_WS_19
      - 95878aa5-VLESS_WS_20
      - 95878aa5-VLESS_WS_21
      - 95878aa5-VLESS_WS_22
      - 95878aa5-VLESS_WS_23
      - 95878aa5-VLESS_WS_24
      - 95878aa5-VLESS_WS_25
      - 95878aa5-VLESS_WS_26
      - 95878aa5-VLESS_WS_27
      - 95878aa5-VLESS_WS_28
      - 95878aa5-VLESS_WS_29
      - 95878aa5-VLESS_WS_30
      - 95878aa5-VLESS_WS_31
      - 95878aa5-VLESS_WS_32
      - 95878aa5-VLESS_WS_33
      - 95878aa5-VLESS_WS_34
      - 95878aa5-VLESS_WS_35
      - 95878aa5-VLESS_WS_36
      - 95878aa5-VLESS_WS_37
      - 95878aa5-VLESS_WS_38
      - 95878aa5-VLESS_WS_39
      - 95878aa5-VLESS_WS_40
      - 95878aa5-VLESS_WS_41
      - 95878aa5-VLESS_WS_42
      - 95878aa5-VLESS_WS_43
      - 95878aa5-VLESS_WS_44
      - 95878aa5-VLESS_WS_45
      - 95878aa5-VLESS_WS_46
      - 95878aa5-VLESS_WS_47
      - 95878aa5-VLESS_WS_48
      - 95878aa5-VLESS_WS_49
      - 95878aa5-VLESS_WS_50
      - 95878aa5-VLESS_WS_51
      - 95878aa5-VLESS_WS_52
      - 95878aa5-VLESS_WS_53
      - 95878aa5-VLESS_WS_54
      - 95878aa5-VLESS_WS_55
      - 95878aa5-VLESS_WS_56
      - 95878aa5-VLESS_WS_57
      - 95878aa5-VLESS_WS_58
      - 95878aa5-VLESS_WS_59
      - 95878aa5-VLESS_WS_60
      - 95878aa5-VLESS_WS_61
      - 95878aa5-VLESS_WS_62
      - 95878aa5-VLESS_WS_63
      - 95878aa5-VLESS_WS_64
      - 95878aa5-VLESS_WS_65
      - 95878aa5-VLESS_WS_66
      - 95878aa5-VLESS_WS_67
      - 95878aa5-VLESS_WS_68
      - 95878aa5-VLESS_WS_69
      - 95878aa5-VLESS_WS_70
      - 95878aa5-VLESS_WS_71
      - 95878aa5-VLESS_WS_72
      - 95878aa5-VLESS_WS_73
      - 95878aa5-VLESS_WS_74
      - 95878aa5-VLESS_WS_75
      - 95878aa5-VLESS_WS_76
      - 95878aa5-VLESS_WS_77
      - 95878aa5-VLESS_WS_78
      - 95878aa5-VLESS_WS_79
      - 95878aa5-VLESS_WS_80
      - 95878aa5-VLESS_WS_81
      - 95878aa5-VLESS_WS_82
      - 95878aa5-VLESS_WS_83
      - 95878aa5-VLESS_WS_84
      - 95878aa5-VLESS_WS_85
      - 95878aa5-VLESS_WS_86
      - 95878aa5-VLESS_WS_87
      - 95878aa5-VLESS_WS_88
      - 95878aa5-VLESS_WS_89
      - 95878aa5-VLESS_WS_90
      - 95878aa5-VLESS_WS_91
      - 95878aa5-VLESS_WS_92
      - 95878aa5-VLESS_WS_93
      - 95878aa5-VLESS_WS_94
      - 95878aa5-VLESS_WS_95
      - 95878aa5-VLESS_WS_96
      - 95878aa5-VLESS_WS_97
      - 95878aa5-VLESS_WS_98
      - 95878aa5-VLESS_WS_99
      - 95878aa5-VLESS_WS_100
      - 95878aa5-VLESS_WS_101
      - 95878aa5-VLESS_WS_102
      - 95878aa5-VLESS_WS_103
      - 95878aa5-VLESS_WS_104
      - 95878aa5-VLESS_WS_105
      - 95878aa5-VLESS_WS_106
      - 95878aa5-VLESS_WS_107
      - 95878aa5-VLESS_WS_108
      - 95878aa5-VLESS_WS_109
      - 95878aa5-VLESS_WS_110
      - 95878aa5-VLESS_WS_111
      - 95878aa5-VLESS_WS_112
      - 95878aa5-VLESS_WS_113
      - 95878aa5-VLESS_WS_114
      - 95878aa5-VLESS_WS_115
      - 95878aa5-VLESS_WS_116
      - 95878aa5-VLESS_WS_117
      - 95878aa5-VLESS_WS_118
      - 95878aa5-VLESS_WS_119
      - 95878aa5-VLESS_WS_120
      - 95878aa5-VLESS_WS_121
      - 95878aa5-VLESS_WS_122
      - 95878aa5-VLESS_WS_123
      - 95878aa5-VLESS_WS_124
      - 95878aa5-VLESS_WS_125
      - 95878aa5-VLESS_WS_126
      - 95878aa5-VLESS_WS_127
      - 95878aa5-VLESS_WS_128
      - 95878aa5-VLESS_WS_129
      - 95878aa5-VLESS_WS_130
      - 95878aa5-VLESS_WS_131
      - 95878aa5-VLESS_WS_132
      - 95878aa5-VLESS_WS_133
      - 95878aa5-VLESS_WS_134
      - 95878aa5-VLESS_WS_135
      - 95878aa5-VLESS_WS_136
      - 95878aa5-VLESS_WS_137
  - name: 📲 电报信息
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - 95878aa5-VLESS_WS_1
      - 95878aa5-VLESS_WS_2
      - 95878aa5-VLESS_WS_3
      - 95878aa5-VLESS_WS_4
      - 95878aa5-VLESS_WS_5
      - 95878aa5-VLESS_WS_6
      - 95878aa5-VLESS_WS_7
      - 95878aa5-VLESS_WS_8
      - 95878aa5-VLESS_WS_9
      - 95878aa5-VLESS_WS_10
      - 95878aa5-VLESS_WS_11
      - 95878aa5-VLESS_WS_12
      - 95878aa5-VLESS_WS_13
      - 95878aa5-VLESS_WS_14
      - 95878aa5-VLESS_WS_15
      - 95878aa5-VLESS_WS_16
      - 95878aa5-VLESS_WS_17
      - 95878aa5-VLESS_WS_18
      - 95878aa5-VLESS_WS_19
      - 95878aa5-VLESS_WS_20
      - 95878aa5-VLESS_WS_21
      - 95878aa5-VLESS_WS_22
      - 95878aa5-VLESS_WS_23
      - 95878aa5-VLESS_WS_24
      - 95878aa5-VLESS_WS_25
      - 95878aa5-VLESS_WS_26
      - 95878aa5-VLESS_WS_27
      - 95878aa5-VLESS_WS_28
      - 95878aa5-VLESS_WS_29
      - 95878aa5-VLESS_WS_30
      - 95878aa5-VLESS_WS_31
      - 95878aa5-VLESS_WS_32
      - 95878aa5-VLESS_WS_33
      - 95878aa5-VLESS_WS_34
      - 95878aa5-VLESS_WS_35
      - 95878aa5-VLESS_WS_36
      - 95878aa5-VLESS_WS_37
      - 95878aa5-VLESS_WS_38
      - 95878aa5-VLESS_WS_39
      - 95878aa5-VLESS_WS_40
      - 95878aa5-VLESS_WS_41
      - 95878aa5-VLESS_WS_42
      - 95878aa5-VLESS_WS_43
      - 95878aa5-VLESS_WS_44
      - 95878aa5-VLESS_WS_45
      - 95878aa5-VLESS_WS_46
      - 95878aa5-VLESS_WS_47
      - 95878aa5-VLESS_WS_48
      - 95878aa5-VLESS_WS_49
      - 95878aa5-VLESS_WS_50
      - 95878aa5-VLESS_WS_51
      - 95878aa5-VLESS_WS_52
      - 95878aa5-VLESS_WS_53
      - 95878aa5-VLESS_WS_54
      - 95878aa5-VLESS_WS_55
      - 95878aa5-VLESS_WS_56
      - 95878aa5-VLESS_WS_57
      - 95878aa5-VLESS_WS_58
      - 95878aa5-VLESS_WS_59
      - 95878aa5-VLESS_WS_60
      - 95878aa5-VLESS_WS_61
      - 95878aa5-VLESS_WS_62
      - 95878aa5-VLESS_WS_63
      - 95878aa5-VLESS_WS_64
      - 95878aa5-VLESS_WS_65
      - 95878aa5-VLESS_WS_66
      - 95878aa5-VLESS_WS_67
      - 95878aa5-VLESS_WS_68
      - 95878aa5-VLESS_WS_69
      - 95878aa5-VLESS_WS_70
      - 95878aa5-VLESS_WS_71
      - 95878aa5-VLESS_WS_72
      - 95878aa5-VLESS_WS_73
      - 95878aa5-VLESS_WS_74
      - 95878aa5-VLESS_WS_75
      - 95878aa5-VLESS_WS_76
      - 95878aa5-VLESS_WS_77
      - 95878aa5-VLESS_WS_78
      - 95878aa5-VLESS_WS_79
      - 95878aa5-VLESS_WS_80
      - 95878aa5-VLESS_WS_81
      - 95878aa5-VLESS_WS_82
      - 95878aa5-VLESS_WS_83
      - 95878aa5-VLESS_WS_84
      - 95878aa5-VLESS_WS_85
      - 95878aa5-VLESS_WS_86
      - 95878aa5-VLESS_WS_87
      - 95878aa5-VLESS_WS_88
      - 95878aa5-VLESS_WS_89
      - 95878aa5-VLESS_WS_90
      - 95878aa5-VLESS_WS_91
      - 95878aa5-VLESS_WS_92
      - 95878aa5-VLESS_WS_93
      - 95878aa5-VLESS_WS_94
      - 95878aa5-VLESS_WS_95
      - 95878aa5-VLESS_WS_96
      - 95878aa5-VLESS_WS_97
      - 95878aa5-VLESS_WS_98
      - 95878aa5-VLESS_WS_99
      - 95878aa5-VLESS_WS_100
      - 95878aa5-VLESS_WS_101
      - 95878aa5-VLESS_WS_102
      - 95878aa5-VLESS_WS_103
      - 95878aa5-VLESS_WS_104
      - 95878aa5-VLESS_WS_105
      - 95878aa5-VLESS_WS_106
      - 95878aa5-VLESS_WS_107
      - 95878aa5-VLESS_WS_108
      - 95878aa5-VLESS_WS_109
      - 95878aa5-VLESS_WS_110
      - 95878aa5-VLESS_WS_111
      - 95878aa5-VLESS_WS_112
      - 95878aa5-VLESS_WS_113
      - 95878aa5-VLESS_WS_114
      - 95878aa5-VLESS_WS_115
      - 95878aa5-VLESS_WS_116
      - 95878aa5-VLESS_WS_117
      - 95878aa5-VLESS_WS_118
      - 95878aa5-VLESS_WS_119
      - 95878aa5-VLESS_WS_120
      - 95878aa5-VLESS_WS_121
      - 95878aa5-VLESS_WS_122
      - 95878aa5-VLESS_WS_123
      - 95878aa5-VLESS_WS_124
      - 95878aa5-VLESS_WS_125
      - 95878aa5-VLESS_WS_126
      - 95878aa5-VLESS_WS_127
      - 95878aa5-VLESS_WS_128
      - 95878aa5-VLESS_WS_129
      - 95878aa5-VLESS_WS_130
      - 95878aa5-VLESS_WS_131
      - 95878aa5-VLESS_WS_132
      - 95878aa5-VLESS_WS_133
      - 95878aa5-VLESS_WS_134
      - 95878aa5-VLESS_WS_135
      - 95878aa5-VLESS_WS_136
      - 95878aa5-VLESS_WS_137
  - name: Ⓜ️ 微软服务
    type: select
    proxies:
      - 🎯 全球直连
      - 🚀 节点选择
      - 95878aa5-VLESS_WS_1
      - 95878aa5-VLESS_WS_2
      - 95878aa5-VLESS_WS_3
      - 95878aa5-VLESS_WS_4
      - 95878aa5-VLESS_WS_5
      - 95878aa5-VLESS_WS_6
      - 95878aa5-VLESS_WS_7
      - 95878aa5-VLESS_WS_8
      - 95878aa5-VLESS_WS_9
      - 95878aa5-VLESS_WS_10
      - 95878aa5-VLESS_WS_11
      - 95878aa5-VLESS_WS_12
      - 95878aa5-VLESS_WS_13
      - 95878aa5-VLESS_WS_14
      - 95878aa5-VLESS_WS_15
      - 95878aa5-VLESS_WS_16
      - 95878aa5-VLESS_WS_17
      - 95878aa5-VLESS_WS_18
      - 95878aa5-VLESS_WS_19
      - 95878aa5-VLESS_WS_20
      - 95878aa5-VLESS_WS_21
      - 95878aa5-VLESS_WS_22
      - 95878aa5-VLESS_WS_23
      - 95878aa5-VLESS_WS_24
      - 95878aa5-VLESS_WS_25
      - 95878aa5-VLESS_WS_26
      - 95878aa5-VLESS_WS_27
      - 95878aa5-VLESS_WS_28
      - 95878aa5-VLESS_WS_29
      - 95878aa5-VLESS_WS_30
      - 95878aa5-VLESS_WS_31
      - 95878aa5-VLESS_WS_32
      - 95878aa5-VLESS_WS_33
      - 95878aa5-VLESS_WS_34
      - 95878aa5-VLESS_WS_35
      - 95878aa5-VLESS_WS_36
      - 95878aa5-VLESS_WS_37
      - 95878aa5-VLESS_WS_38
      - 95878aa5-VLESS_WS_39
      - 95878aa5-VLESS_WS_40
      - 95878aa5-VLESS_WS_41
      - 95878aa5-VLESS_WS_42
      - 95878aa5-VLESS_WS_43
      - 95878aa5-VLESS_WS_44
      - 95878aa5-VLESS_WS_45
      - 95878aa5-VLESS_WS_46
      - 95878aa5-VLESS_WS_47
      - 95878aa5-VLESS_WS_48
      - 95878aa5-VLESS_WS_49
      - 95878aa5-VLESS_WS_50
      - 95878aa5-VLESS_WS_51
      - 95878aa5-VLESS_WS_52
      - 95878aa5-VLESS_WS_53
      - 95878aa5-VLESS_WS_54
      - 95878aa5-VLESS_WS_55
      - 95878aa5-VLESS_WS_56
      - 95878aa5-VLESS_WS_57
      - 95878aa5-VLESS_WS_58
      - 95878aa5-VLESS_WS_59
      - 95878aa5-VLESS_WS_60
      - 95878aa5-VLESS_WS_61
      - 95878aa5-VLESS_WS_62
      - 95878aa5-VLESS_WS_63
      - 95878aa5-VLESS_WS_64
      - 95878aa5-VLESS_WS_65
      - 95878aa5-VLESS_WS_66
      - 95878aa5-VLESS_WS_67
      - 95878aa5-VLESS_WS_68
      - 95878aa5-VLESS_WS_69
      - 95878aa5-VLESS_WS_70
      - 95878aa5-VLESS_WS_71
      - 95878aa5-VLESS_WS_72
      - 95878aa5-VLESS_WS_73
      - 95878aa5-VLESS_WS_74
      - 95878aa5-VLESS_WS_75
      - 95878aa5-VLESS_WS_76
      - 95878aa5-VLESS_WS_77
      - 95878aa5-VLESS_WS_78
      - 95878aa5-VLESS_WS_79
      - 95878aa5-VLESS_WS_80
      - 95878aa5-VLESS_WS_81
      - 95878aa5-VLESS_WS_82
      - 95878aa5-VLESS_WS_83
      - 95878aa5-VLESS_WS_84
      - 95878aa5-VLESS_WS_85
      - 95878aa5-VLESS_WS_86
      - 95878aa5-VLESS_WS_87
      - 95878aa5-VLESS_WS_88
      - 95878aa5-VLESS_WS_89
      - 95878aa5-VLESS_WS_90
      - 95878aa5-VLESS_WS_91
      - 95878aa5-VLESS_WS_92
      - 95878aa5-VLESS_WS_93
      - 95878aa5-VLESS_WS_94
      - 95878aa5-VLESS_WS_95
      - 95878aa5-VLESS_WS_96
      - 95878aa5-VLESS_WS_97
      - 95878aa5-VLESS_WS_98
      - 95878aa5-VLESS_WS_99
      - 95878aa5-VLESS_WS_100
      - 95878aa5-VLESS_WS_101
      - 95878aa5-VLESS_WS_102
      - 95878aa5-VLESS_WS_103
      - 95878aa5-VLESS_WS_104
      - 95878aa5-VLESS_WS_105
      - 95878aa5-VLESS_WS_106
      - 95878aa5-VLESS_WS_107
      - 95878aa5-VLESS_WS_108
      - 95878aa5-VLESS_WS_109
      - 95878aa5-VLESS_WS_110
      - 95878aa5-VLESS_WS_111
      - 95878aa5-VLESS_WS_112
      - 95878aa5-VLESS_WS_113
      - 95878aa5-VLESS_WS_114
      - 95878aa5-VLESS_WS_115
      - 95878aa5-VLESS_WS_116
      - 95878aa5-VLESS_WS_117
      - 95878aa5-VLESS_WS_118
      - 95878aa5-VLESS_WS_119
      - 95878aa5-VLESS_WS_120
      - 95878aa5-VLESS_WS_121
      - 95878aa5-VLESS_WS_122
      - 95878aa5-VLESS_WS_123
      - 95878aa5-VLESS_WS_124
      - 95878aa5-VLESS_WS_125
      - 95878aa5-VLESS_WS_126
      - 95878aa5-VLESS_WS_127
      - 95878aa5-VLESS_WS_128
      - 95878aa5-VLESS_WS_129
      - 95878aa5-VLESS_WS_130
      - 95878aa5-VLESS_WS_131
      - 95878aa5-VLESS_WS_132
      - 95878aa5-VLESS_WS_133
      - 95878aa5-VLESS_WS_134
      - 95878aa5-VLESS_WS_135
      - 95878aa5-VLESS_WS_136
      - 95878aa5-VLESS_WS_137
  - name: 🍎 苹果服务
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - 95878aa5-VLESS_WS_1
      - 95878aa5-VLESS_WS_2
      - 95878aa5-VLESS_WS_3
      - 95878aa5-VLESS_WS_4
      - 95878aa5-VLESS_WS_5
      - 95878aa5-VLESS_WS_6
      - 95878aa5-VLESS_WS_7
      - 95878aa5-VLESS_WS_8
      - 95878aa5-VLESS_WS_9
      - 95878aa5-VLESS_WS_10
      - 95878aa5-VLESS_WS_11
      - 95878aa5-VLESS_WS_12
      - 95878aa5-VLESS_WS_13
      - 95878aa5-VLESS_WS_14
      - 95878aa5-VLESS_WS_15
      - 95878aa5-VLESS_WS_16
      - 95878aa5-VLESS_WS_17
      - 95878aa5-VLESS_WS_18
      - 95878aa5-VLESS_WS_19
      - 95878aa5-VLESS_WS_20
      - 95878aa5-VLESS_WS_21
      - 95878aa5-VLESS_WS_22
      - 95878aa5-VLESS_WS_23
      - 95878aa5-VLESS_WS_24
      - 95878aa5-VLESS_WS_25
      - 95878aa5-VLESS_WS_26
      - 95878aa5-VLESS_WS_27
      - 95878aa5-VLESS_WS_28
      - 95878aa5-VLESS_WS_29
      - 95878aa5-VLESS_WS_30
      - 95878aa5-VLESS_WS_31
      - 95878aa5-VLESS_WS_32
      - 95878aa5-VLESS_WS_33
      - 95878aa5-VLESS_WS_34
      - 95878aa5-VLESS_WS_35
      - 95878aa5-VLESS_WS_36
      - 95878aa5-VLESS_WS_37
      - 95878aa5-VLESS_WS_38
      - 95878aa5-VLESS_WS_39
      - 95878aa5-VLESS_WS_40
      - 95878aa5-VLESS_WS_41
      - 95878aa5-VLESS_WS_42
      - 95878aa5-VLESS_WS_43
      - 95878aa5-VLESS_WS_44
      - 95878aa5-VLESS_WS_45
      - 95878aa5-VLESS_WS_46
      - 95878aa5-VLESS_WS_47
      - 95878aa5-VLESS_WS_48
      - 95878aa5-VLESS_WS_49
      - 95878aa5-VLESS_WS_50
      - 95878aa5-VLESS_WS_51
      - 95878aa5-VLESS_WS_52
      - 95878aa5-VLESS_WS_53
      - 95878aa5-VLESS_WS_54
      - 95878aa5-VLESS_WS_55
      - 95878aa5-VLESS_WS_56
      - 95878aa5-VLESS_WS_57
      - 95878aa5-VLESS_WS_58
      - 95878aa5-VLESS_WS_59
      - 95878aa5-VLESS_WS_60
      - 95878aa5-VLESS_WS_61
      - 95878aa5-VLESS_WS_62
      - 95878aa5-VLESS_WS_63
      - 95878aa5-VLESS_WS_64
      - 95878aa5-VLESS_WS_65
      - 95878aa5-VLESS_WS_66
      - 95878aa5-VLESS_WS_67
      - 95878aa5-VLESS_WS_68
      - 95878aa5-VLESS_WS_69
      - 95878aa5-VLESS_WS_70
      - 95878aa5-VLESS_WS_71
      - 95878aa5-VLESS_WS_72
      - 95878aa5-VLESS_WS_73
      - 95878aa5-VLESS_WS_74
      - 95878aa5-VLESS_WS_75
      - 95878aa5-VLESS_WS_76
      - 95878aa5-VLESS_WS_77
      - 95878aa5-VLESS_WS_78
      - 95878aa5-VLESS_WS_79
      - 95878aa5-VLESS_WS_80
      - 95878aa5-VLESS_WS_81
      - 95878aa5-VLESS_WS_82
      - 95878aa5-VLESS_WS_83
      - 95878aa5-VLESS_WS_84
      - 95878aa5-VLESS_WS_85
      - 95878aa5-VLESS_WS_86
      - 95878aa5-VLESS_WS_87
      - 95878aa5-VLESS_WS_88
      - 95878aa5-VLESS_WS_89
      - 95878aa5-VLESS_WS_90
      - 95878aa5-VLESS_WS_91
      - 95878aa5-VLESS_WS_92
      - 95878aa5-VLESS_WS_93
      - 95878aa5-VLESS_WS_94
      - 95878aa5-VLESS_WS_95
      - 95878aa5-VLESS_WS_96
      - 95878aa5-VLESS_WS_97
      - 95878aa5-VLESS_WS_98
      - 95878aa5-VLESS_WS_99
      - 95878aa5-VLESS_WS_100
      - 95878aa5-VLESS_WS_101
      - 95878aa5-VLESS_WS_102
      - 95878aa5-VLESS_WS_103
      - 95878aa5-VLESS_WS_104
      - 95878aa5-VLESS_WS_105
      - 95878aa5-VLESS_WS_106
      - 95878aa5-VLESS_WS_107
      - 95878aa5-VLESS_WS_108
      - 95878aa5-VLESS_WS_109
      - 95878aa5-VLESS_WS_110
      - 95878aa5-VLESS_WS_111
      - 95878aa5-VLESS_WS_112
      - 95878aa5-VLESS_WS_113
      - 95878aa5-VLESS_WS_114
      - 95878aa5-VLESS_WS_115
      - 95878aa5-VLESS_WS_116
      - 95878aa5-VLESS_WS_117
      - 95878aa5-VLESS_WS_118
      - 95878aa5-VLESS_WS_119
      - 95878aa5-VLESS_WS_120
      - 95878aa5-VLESS_WS_121
      - 95878aa5-VLESS_WS_122
      - 95878aa5-VLESS_WS_123
      - 95878aa5-VLESS_WS_124
      - 95878aa5-VLESS_WS_125
      - 95878aa5-VLESS_WS_126
      - 95878aa5-VLESS_WS_127
      - 95878aa5-VLESS_WS_128
      - 95878aa5-VLESS_WS_129
      - 95878aa5-VLESS_WS_130
      - 95878aa5-VLESS_WS_131
      - 95878aa5-VLESS_WS_132
      - 95878aa5-VLESS_WS_133
      - 95878aa5-VLESS_WS_134
      - 95878aa5-VLESS_WS_135
      - 95878aa5-VLESS_WS_136
      - 95878aa5-VLESS_WS_137
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
      - 95878aa5-VLESS_WS_1
      - 95878aa5-VLESS_WS_2
      - 95878aa5-VLESS_WS_3
      - 95878aa5-VLESS_WS_4
      - 95878aa5-VLESS_WS_5
      - 95878aa5-VLESS_WS_6
      - 95878aa5-VLESS_WS_7
      - 95878aa5-VLESS_WS_8
      - 95878aa5-VLESS_WS_9
      - 95878aa5-VLESS_WS_10
      - 95878aa5-VLESS_WS_11
      - 95878aa5-VLESS_WS_12
      - 95878aa5-VLESS_WS_13
      - 95878aa5-VLESS_WS_14
      - 95878aa5-VLESS_WS_15
      - 95878aa5-VLESS_WS_16
      - 95878aa5-VLESS_WS_17
      - 95878aa5-VLESS_WS_18
      - 95878aa5-VLESS_WS_19
      - 95878aa5-VLESS_WS_20
      - 95878aa5-VLESS_WS_21
      - 95878aa5-VLESS_WS_22
      - 95878aa5-VLESS_WS_23
      - 95878aa5-VLESS_WS_24
      - 95878aa5-VLESS_WS_25
      - 95878aa5-VLESS_WS_26
      - 95878aa5-VLESS_WS_27
      - 95878aa5-VLESS_WS_28
      - 95878aa5-VLESS_WS_29
      - 95878aa5-VLESS_WS_30
      - 95878aa5-VLESS_WS_31
      - 95878aa5-VLESS_WS_32
      - 95878aa5-VLESS_WS_33
      - 95878aa5-VLESS_WS_34
      - 95878aa5-VLESS_WS_35
      - 95878aa5-VLESS_WS_36
      - 95878aa5-VLESS_WS_37
      - 95878aa5-VLESS_WS_38
      - 95878aa5-VLESS_WS_39
      - 95878aa5-VLESS_WS_40
      - 95878aa5-VLESS_WS_41
      - 95878aa5-VLESS_WS_42
      - 95878aa5-VLESS_WS_43
      - 95878aa5-VLESS_WS_44
      - 95878aa5-VLESS_WS_45
      - 95878aa5-VLESS_WS_46
      - 95878aa5-VLESS_WS_47
      - 95878aa5-VLESS_WS_48
      - 95878aa5-VLESS_WS_49
      - 95878aa5-VLESS_WS_50
      - 95878aa5-VLESS_WS_51
      - 95878aa5-VLESS_WS_52
      - 95878aa5-VLESS_WS_53
      - 95878aa5-VLESS_WS_54
      - 95878aa5-VLESS_WS_55
      - 95878aa5-VLESS_WS_56
      - 95878aa5-VLESS_WS_57
      - 95878aa5-VLESS_WS_58
      - 95878aa5-VLESS_WS_59
      - 95878aa5-VLESS_WS_60
      - 95878aa5-VLESS_WS_61
      - 95878aa5-VLESS_WS_62
      - 95878aa5-VLESS_WS_63
      - 95878aa5-VLESS_WS_64
      - 95878aa5-VLESS_WS_65
      - 95878aa5-VLESS_WS_66
      - 95878aa5-VLESS_WS_67
      - 95878aa5-VLESS_WS_68
      - 95878aa5-VLESS_WS_69
      - 95878aa5-VLESS_WS_70
      - 95878aa5-VLESS_WS_71
      - 95878aa5-VLESS_WS_72
      - 95878aa5-VLESS_WS_73
      - 95878aa5-VLESS_WS_74
      - 95878aa5-VLESS_WS_75
      - 95878aa5-VLESS_WS_76
      - 95878aa5-VLESS_WS_77
      - 95878aa5-VLESS_WS_78
      - 95878aa5-VLESS_WS_79
      - 95878aa5-VLESS_WS_80
      - 95878aa5-VLESS_WS_81
      - 95878aa5-VLESS_WS_82
      - 95878aa5-VLESS_WS_83
      - 95878aa5-VLESS_WS_84
      - 95878aa5-VLESS_WS_85
      - 95878aa5-VLESS_WS_86
      - 95878aa5-VLESS_WS_87
      - 95878aa5-VLESS_WS_88
      - 95878aa5-VLESS_WS_89
      - 95878aa5-VLESS_WS_90
      - 95878aa5-VLESS_WS_91
      - 95878aa5-VLESS_WS_92
      - 95878aa5-VLESS_WS_93
      - 95878aa5-VLESS_WS_94
      - 95878aa5-VLESS_WS_95
      - 95878aa5-VLESS_WS_96
      - 95878aa5-VLESS_WS_97
      - 95878aa5-VLESS_WS_98
      - 95878aa5-VLESS_WS_99
      - 95878aa5-VLESS_WS_100
      - 95878aa5-VLESS_WS_101
      - 95878aa5-VLESS_WS_102
      - 95878aa5-VLESS_WS_103
      - 95878aa5-VLESS_WS_104
      - 95878aa5-VLESS_WS_105
      - 95878aa5-VLESS_WS_106
      - 95878aa5-VLESS_WS_107
      - 95878aa5-VLESS_WS_108
      - 95878aa5-VLESS_WS_109
      - 95878aa5-VLESS_WS_110
      - 95878aa5-VLESS_WS_111
      - 95878aa5-VLESS_WS_112
      - 95878aa5-VLESS_WS_113
      - 95878aa5-VLESS_WS_114
      - 95878aa5-VLESS_WS_115
      - 95878aa5-VLESS_WS_116
      - 95878aa5-VLESS_WS_117
      - 95878aa5-VLESS_WS_118
      - 95878aa5-VLESS_WS_119
      - 95878aa5-VLESS_WS_120
      - 95878aa5-VLESS_WS_121
      - 95878aa5-VLESS_WS_122
      - 95878aa5-VLESS_WS_123
      - 95878aa5-VLESS_WS_124
      - 95878aa5-VLESS_WS_125
      - 95878aa5-VLESS_WS_126
      - 95878aa5-VLESS_WS_127
      - 95878aa5-VLESS_WS_128
      - 95878aa5-VLESS_WS_129
      - 95878aa5-VLESS_WS_130
      - 95878aa5-VLESS_WS_131
      - 95878aa5-VLESS_WS_132
      - 95878aa5-VLESS_WS_133
      - 95878aa5-VLESS_WS_134
      - 95878aa5-VLESS_WS_135
      - 95878aa5-VLESS_WS_136
      - 95878aa5-VLESS_WS_137

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
