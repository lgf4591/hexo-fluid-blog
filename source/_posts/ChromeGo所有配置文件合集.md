
---
title: ChromeGo所有配置文件合集 
date: 2024-02-18 22:57:14
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

> Last Update Time: 2024-02-18 22:57:14
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
      "protocol": "vmess",
      "settings": {
        "vnext": [
          {
            "address": "23.227.39.88",
            "port": 443,
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
        "security": "tls",
        "tlsSettings": {
          "allowInsecure": false,
          "serverName": "proprietary-arc-durham-motorcycle.trycloudflare.com",
          "show": false
        },
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
  fallback:
    - 8.8.8.8
    - 8.8.4.4
    - tls://1.0.0.1:853
    - tls://dns.google:853
proxies:
  - {"name":"dongtaiwang.com_1","type":"vmess","server":"23.227.38.220","port":443,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_2","type":"vmess","server":"23.227.39.210","port":443,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"sequence-worse-councils-nest.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"sequence-worse-councils-nest.trycloudflare.com"}}}
proxy-groups:
  - name: 🚀 节点选择
    type: select
    proxies:
      - ♻️ 自动选择
      - DIRECT
      - dongtaiwang.com_1
      - dongtaiwang.com_2
  - name: ♻️ 自动选择
    type: url-test
    url: https://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    proxies:
      - dongtaiwang.com_1
      - dongtaiwang.com_2
  - name: 🌍 国外媒体
    type: select
    proxies:
      - 🚀 节点选择
      - ♻️ 自动选择
      - 🎯 全球直连
      - dongtaiwang.com_1
      - dongtaiwang.com_2
  - name: 📲 电报信息
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - dongtaiwang.com_1
      - dongtaiwang.com_2
  - name: Ⓜ️ 微软服务
    type: select
    proxies:
      - 🎯 全球直连
      - 🚀 节点选择
      - dongtaiwang.com_1
      - dongtaiwang.com_2
  - name: 🍎 苹果服务
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - dongtaiwang.com_1
      - dongtaiwang.com_2
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
  - {"name":"dongtaiwang.com_1","type":"vmess","server":"23.227.38.220","port":443,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_2","type":"vmess","server":"23.227.39.210","port":443,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"sequence-worse-councils-nest.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"sequence-worse-councils-nest.trycloudflare.com"}}}
proxy-groups:
  - name: 🚀 节点选择
    type: select
    proxies:
      - ♻️ 自动选择
      - DIRECT
      - dongtaiwang.com_1
      - dongtaiwang.com_2
  - name: ♻️ 自动选择
    type: url-test
    url: https://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    proxies:
      - dongtaiwang.com_1
      - dongtaiwang.com_2
  - name: 🌍 国外媒体
    type: select
    proxies:
      - 🚀 节点选择
      - ♻️ 自动选择
      - 🎯 全球直连
      - dongtaiwang.com_1
      - dongtaiwang.com_2
  - name: 📲 电报信息
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - dongtaiwang.com_1
      - dongtaiwang.com_2
  - name: Ⓜ️ 微软服务
    type: select
    proxies:
      - 🎯 全球直连
      - 🚀 节点选择
      - dongtaiwang.com_1
      - dongtaiwang.com_2
  - name: 🍎 苹果服务
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - dongtaiwang.com_1
      - dongtaiwang.com_2
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
  - {"name":"dongtaiwang.com_1","type":"vmess","server":"23.227.38.12","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_2","type":"vmess","server":"103.21.244.83","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_3","type":"vmess","server":"188.114.97.196","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_4","type":"vmess","server":"190.93.247.214","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_5","type":"vmess","server":"173.245.58.51","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_6","type":"vmess","server":"141.101.123.221","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_7","type":"vmess","server":"198.41.209.240","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_8","type":"vmess","server":"141.101.121.91","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_9","type":"vmess","server":"103.21.244.136","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_10","type":"vmess","server":"190.93.245.141","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_11","type":"vmess","server":"190.93.245.232","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_12","type":"vmess","server":"188.114.96.25","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_13","type":"vmess","server":"172.67.229.73","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_14","type":"vmess","server":"190.93.245.223","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_15","type":"vmess","server":"103.21.244.96","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_16","type":"vmess","server":"172.64.142.35","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_17","type":"vmess","server":"173.245.58.185","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_18","type":"vmess","server":"162.159.43.135","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_19","type":"vmess","server":"198.41.214.178","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_20","type":"vmess","server":"188.114.97.109","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_21","type":"vmess","server":"198.41.217.124","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_22","type":"vmess","server":"162.159.136.86","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_23","type":"vmess","server":"188.114.99.212","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_24","type":"vmess","server":"198.41.199.127","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_25","type":"vmess","server":"198.41.219.235","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_26","type":"vmess","server":"198.41.204.209","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_27","type":"vmess","server":"198.41.212.118","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_28","type":"vmess","server":"162.159.58.126","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_29","type":"vmess","server":"173.245.59.149","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_30","type":"vmess","server":"188.114.97.52","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_31","type":"vmess","server":"190.93.247.120","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_32","type":"vmess","server":"188.114.97.4","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_33","type":"vmess","server":"162.159.35.180","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_34","type":"vmess","server":"172.67.144.123","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_35","type":"vmess","server":"162.159.152.92","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_36","type":"vmess","server":"198.41.215.80","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_37","type":"vmess","server":"172.66.154.44","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_38","type":"vmess","server":"162.159.12.58","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_39","type":"vmess","server":"188.114.98.60","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_40","type":"vmess","server":"162.159.10.152","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_41","type":"vmess","server":"198.41.196.136","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_42","type":"vmess","server":"188.114.99.147","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_43","type":"vmess","server":"103.21.244.237","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_44","type":"vmess","server":"108.162.193.176","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_45","type":"vmess","server":"198.41.221.193","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_46","type":"vmess","server":"188.114.98.96","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_47","type":"vmess","server":"173.245.59.190","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_48","type":"vmess","server":"190.93.247.33","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_49","type":"vmess","server":"172.66.151.45","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_50","type":"vmess","server":"190.93.246.223","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_51","type":"vmess","server":"188.114.98.224","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_52","type":"vmess","server":"108.162.196.207","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_53","type":"vmess","server":"190.93.244.15","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_54","type":"vmess","server":"141.101.120.144","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_55","type":"vmess","server":"188.114.96.75","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_56","type":"vmess","server":"103.21.244.245","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_57","type":"vmess","server":"141.101.122.10","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_58","type":"vmess","server":"173.245.58.123","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_59","type":"vmess","server":"103.21.244.112","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_60","type":"vmess","server":"190.93.247.242","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_61","type":"vmess","server":"173.245.49.132","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_62","type":"vmess","server":"173.245.59.29","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_63","type":"vmess","server":"103.21.244.192","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_64","type":"vmess","server":"103.21.244.241","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_65","type":"vmess","server":"190.93.244.67","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_66","type":"vmess","server":"103.21.244.90","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_67","type":"vmess","server":"188.114.98.112","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_68","type":"vmess","server":"172.67.144.231","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_69","type":"vmess","server":"162.159.141.10","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_70","type":"vmess","server":"103.21.244.142","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_71","type":"vmess","server":"198.41.207.116","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_72","type":"vmess","server":"198.41.214.1","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_73","type":"vmess","server":"173.245.59.189","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_74","type":"vmess","server":"103.21.244.23","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_75","type":"vmess","server":"141.101.115.194","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_76","type":"vmess","server":"188.114.96.81","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_77","type":"vmess","server":"190.93.245.25","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_78","type":"vmess","server":"172.67.205.95","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_79","type":"vmess","server":"173.245.58.151","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_80","type":"vmess","server":"190.93.246.2","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_81","type":"vmess","server":"108.162.194.82","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_82","type":"vmess","server":"172.64.81.37","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_83","type":"vmess","server":"172.67.82.251","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_84","type":"vmess","server":"141.101.115.216","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_85","type":"vmess","server":"103.21.244.151","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_86","type":"vmess","server":"103.21.244.156","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_87","type":"vmess","server":"198.41.192.100","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_88","type":"vmess","server":"103.21.244.81","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_89","type":"vmess","server":"190.93.246.12","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_90","type":"vmess","server":"162.159.245.75","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_91","type":"vmess","server":"190.93.246.122","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_92","type":"vmess","server":"108.162.193.38","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_93","type":"vmess","server":"173.245.58.253","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_94","type":"vmess","server":"198.41.212.54","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_95","type":"vmess","server":"190.93.246.147","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_96","type":"vmess","server":"198.41.204.95","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_97","type":"vmess","server":"173.245.49.54","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_98","type":"vmess","server":"173.245.59.188","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_99","type":"vmess","server":"172.66.172.182","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_100","type":"vmess","server":"188.114.98.242","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_101","type":"vmess","server":"141.101.90.100","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_102","type":"vmess","server":"188.114.99.6","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_103","type":"vmess","server":"190.93.246.47","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_104","type":"vmess","server":"188.114.97.48","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_105","type":"vmess","server":"108.162.196.15","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_106","type":"vmess","server":"173.245.58.81","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_107","type":"vmess","server":"103.21.244.78","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_108","type":"vmess","server":"103.21.244.141","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_109","type":"vmess","server":"108.162.196.31","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_110","type":"vmess","server":"23.227.38.11","port":443,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":true,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
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
      - dongtaiwang.com_17
      - dongtaiwang.com_18
      - dongtaiwang.com_19
      - dongtaiwang.com_20
      - dongtaiwang.com_21
      - dongtaiwang.com_22
      - dongtaiwang.com_23
      - dongtaiwang.com_24
      - dongtaiwang.com_25
      - dongtaiwang.com_26
      - dongtaiwang.com_27
      - dongtaiwang.com_28
      - dongtaiwang.com_29
      - dongtaiwang.com_30
      - dongtaiwang.com_31
      - dongtaiwang.com_32
      - dongtaiwang.com_33
      - dongtaiwang.com_34
      - dongtaiwang.com_35
      - dongtaiwang.com_36
      - dongtaiwang.com_37
      - dongtaiwang.com_38
      - dongtaiwang.com_39
      - dongtaiwang.com_40
      - dongtaiwang.com_41
      - dongtaiwang.com_42
      - dongtaiwang.com_43
      - dongtaiwang.com_44
      - dongtaiwang.com_45
      - dongtaiwang.com_46
      - dongtaiwang.com_47
      - dongtaiwang.com_48
      - dongtaiwang.com_49
      - dongtaiwang.com_50
      - dongtaiwang.com_51
      - dongtaiwang.com_52
      - dongtaiwang.com_53
      - dongtaiwang.com_54
      - dongtaiwang.com_55
      - dongtaiwang.com_56
      - dongtaiwang.com_57
      - dongtaiwang.com_58
      - dongtaiwang.com_59
      - dongtaiwang.com_60
      - dongtaiwang.com_61
      - dongtaiwang.com_62
      - dongtaiwang.com_63
      - dongtaiwang.com_64
      - dongtaiwang.com_65
      - dongtaiwang.com_66
      - dongtaiwang.com_67
      - dongtaiwang.com_68
      - dongtaiwang.com_69
      - dongtaiwang.com_70
      - dongtaiwang.com_71
      - dongtaiwang.com_72
      - dongtaiwang.com_73
      - dongtaiwang.com_74
      - dongtaiwang.com_75
      - dongtaiwang.com_76
      - dongtaiwang.com_77
      - dongtaiwang.com_78
      - dongtaiwang.com_79
      - dongtaiwang.com_80
      - dongtaiwang.com_81
      - dongtaiwang.com_82
      - dongtaiwang.com_83
      - dongtaiwang.com_84
      - dongtaiwang.com_85
      - dongtaiwang.com_86
      - dongtaiwang.com_87
      - dongtaiwang.com_88
      - dongtaiwang.com_89
      - dongtaiwang.com_90
      - dongtaiwang.com_91
      - dongtaiwang.com_92
      - dongtaiwang.com_93
      - dongtaiwang.com_94
      - dongtaiwang.com_95
      - dongtaiwang.com_96
      - dongtaiwang.com_97
      - dongtaiwang.com_98
      - dongtaiwang.com_99
      - dongtaiwang.com_100
      - dongtaiwang.com_101
      - dongtaiwang.com_102
      - dongtaiwang.com_103
      - dongtaiwang.com_104
      - dongtaiwang.com_105
      - dongtaiwang.com_106
      - dongtaiwang.com_107
      - dongtaiwang.com_108
      - dongtaiwang.com_109
      - dongtaiwang.com_110
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
      - dongtaiwang.com_17
      - dongtaiwang.com_18
      - dongtaiwang.com_19
      - dongtaiwang.com_20
      - dongtaiwang.com_21
      - dongtaiwang.com_22
      - dongtaiwang.com_23
      - dongtaiwang.com_24
      - dongtaiwang.com_25
      - dongtaiwang.com_26
      - dongtaiwang.com_27
      - dongtaiwang.com_28
      - dongtaiwang.com_29
      - dongtaiwang.com_30
      - dongtaiwang.com_31
      - dongtaiwang.com_32
      - dongtaiwang.com_33
      - dongtaiwang.com_34
      - dongtaiwang.com_35
      - dongtaiwang.com_36
      - dongtaiwang.com_37
      - dongtaiwang.com_38
      - dongtaiwang.com_39
      - dongtaiwang.com_40
      - dongtaiwang.com_41
      - dongtaiwang.com_42
      - dongtaiwang.com_43
      - dongtaiwang.com_44
      - dongtaiwang.com_45
      - dongtaiwang.com_46
      - dongtaiwang.com_47
      - dongtaiwang.com_48
      - dongtaiwang.com_49
      - dongtaiwang.com_50
      - dongtaiwang.com_51
      - dongtaiwang.com_52
      - dongtaiwang.com_53
      - dongtaiwang.com_54
      - dongtaiwang.com_55
      - dongtaiwang.com_56
      - dongtaiwang.com_57
      - dongtaiwang.com_58
      - dongtaiwang.com_59
      - dongtaiwang.com_60
      - dongtaiwang.com_61
      - dongtaiwang.com_62
      - dongtaiwang.com_63
      - dongtaiwang.com_64
      - dongtaiwang.com_65
      - dongtaiwang.com_66
      - dongtaiwang.com_67
      - dongtaiwang.com_68
      - dongtaiwang.com_69
      - dongtaiwang.com_70
      - dongtaiwang.com_71
      - dongtaiwang.com_72
      - dongtaiwang.com_73
      - dongtaiwang.com_74
      - dongtaiwang.com_75
      - dongtaiwang.com_76
      - dongtaiwang.com_77
      - dongtaiwang.com_78
      - dongtaiwang.com_79
      - dongtaiwang.com_80
      - dongtaiwang.com_81
      - dongtaiwang.com_82
      - dongtaiwang.com_83
      - dongtaiwang.com_84
      - dongtaiwang.com_85
      - dongtaiwang.com_86
      - dongtaiwang.com_87
      - dongtaiwang.com_88
      - dongtaiwang.com_89
      - dongtaiwang.com_90
      - dongtaiwang.com_91
      - dongtaiwang.com_92
      - dongtaiwang.com_93
      - dongtaiwang.com_94
      - dongtaiwang.com_95
      - dongtaiwang.com_96
      - dongtaiwang.com_97
      - dongtaiwang.com_98
      - dongtaiwang.com_99
      - dongtaiwang.com_100
      - dongtaiwang.com_101
      - dongtaiwang.com_102
      - dongtaiwang.com_103
      - dongtaiwang.com_104
      - dongtaiwang.com_105
      - dongtaiwang.com_106
      - dongtaiwang.com_107
      - dongtaiwang.com_108
      - dongtaiwang.com_109
      - dongtaiwang.com_110
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
      - dongtaiwang.com_17
      - dongtaiwang.com_18
      - dongtaiwang.com_19
      - dongtaiwang.com_20
      - dongtaiwang.com_21
      - dongtaiwang.com_22
      - dongtaiwang.com_23
      - dongtaiwang.com_24
      - dongtaiwang.com_25
      - dongtaiwang.com_26
      - dongtaiwang.com_27
      - dongtaiwang.com_28
      - dongtaiwang.com_29
      - dongtaiwang.com_30
      - dongtaiwang.com_31
      - dongtaiwang.com_32
      - dongtaiwang.com_33
      - dongtaiwang.com_34
      - dongtaiwang.com_35
      - dongtaiwang.com_36
      - dongtaiwang.com_37
      - dongtaiwang.com_38
      - dongtaiwang.com_39
      - dongtaiwang.com_40
      - dongtaiwang.com_41
      - dongtaiwang.com_42
      - dongtaiwang.com_43
      - dongtaiwang.com_44
      - dongtaiwang.com_45
      - dongtaiwang.com_46
      - dongtaiwang.com_47
      - dongtaiwang.com_48
      - dongtaiwang.com_49
      - dongtaiwang.com_50
      - dongtaiwang.com_51
      - dongtaiwang.com_52
      - dongtaiwang.com_53
      - dongtaiwang.com_54
      - dongtaiwang.com_55
      - dongtaiwang.com_56
      - dongtaiwang.com_57
      - dongtaiwang.com_58
      - dongtaiwang.com_59
      - dongtaiwang.com_60
      - dongtaiwang.com_61
      - dongtaiwang.com_62
      - dongtaiwang.com_63
      - dongtaiwang.com_64
      - dongtaiwang.com_65
      - dongtaiwang.com_66
      - dongtaiwang.com_67
      - dongtaiwang.com_68
      - dongtaiwang.com_69
      - dongtaiwang.com_70
      - dongtaiwang.com_71
      - dongtaiwang.com_72
      - dongtaiwang.com_73
      - dongtaiwang.com_74
      - dongtaiwang.com_75
      - dongtaiwang.com_76
      - dongtaiwang.com_77
      - dongtaiwang.com_78
      - dongtaiwang.com_79
      - dongtaiwang.com_80
      - dongtaiwang.com_81
      - dongtaiwang.com_82
      - dongtaiwang.com_83
      - dongtaiwang.com_84
      - dongtaiwang.com_85
      - dongtaiwang.com_86
      - dongtaiwang.com_87
      - dongtaiwang.com_88
      - dongtaiwang.com_89
      - dongtaiwang.com_90
      - dongtaiwang.com_91
      - dongtaiwang.com_92
      - dongtaiwang.com_93
      - dongtaiwang.com_94
      - dongtaiwang.com_95
      - dongtaiwang.com_96
      - dongtaiwang.com_97
      - dongtaiwang.com_98
      - dongtaiwang.com_99
      - dongtaiwang.com_100
      - dongtaiwang.com_101
      - dongtaiwang.com_102
      - dongtaiwang.com_103
      - dongtaiwang.com_104
      - dongtaiwang.com_105
      - dongtaiwang.com_106
      - dongtaiwang.com_107
      - dongtaiwang.com_108
      - dongtaiwang.com_109
      - dongtaiwang.com_110
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
      - dongtaiwang.com_17
      - dongtaiwang.com_18
      - dongtaiwang.com_19
      - dongtaiwang.com_20
      - dongtaiwang.com_21
      - dongtaiwang.com_22
      - dongtaiwang.com_23
      - dongtaiwang.com_24
      - dongtaiwang.com_25
      - dongtaiwang.com_26
      - dongtaiwang.com_27
      - dongtaiwang.com_28
      - dongtaiwang.com_29
      - dongtaiwang.com_30
      - dongtaiwang.com_31
      - dongtaiwang.com_32
      - dongtaiwang.com_33
      - dongtaiwang.com_34
      - dongtaiwang.com_35
      - dongtaiwang.com_36
      - dongtaiwang.com_37
      - dongtaiwang.com_38
      - dongtaiwang.com_39
      - dongtaiwang.com_40
      - dongtaiwang.com_41
      - dongtaiwang.com_42
      - dongtaiwang.com_43
      - dongtaiwang.com_44
      - dongtaiwang.com_45
      - dongtaiwang.com_46
      - dongtaiwang.com_47
      - dongtaiwang.com_48
      - dongtaiwang.com_49
      - dongtaiwang.com_50
      - dongtaiwang.com_51
      - dongtaiwang.com_52
      - dongtaiwang.com_53
      - dongtaiwang.com_54
      - dongtaiwang.com_55
      - dongtaiwang.com_56
      - dongtaiwang.com_57
      - dongtaiwang.com_58
      - dongtaiwang.com_59
      - dongtaiwang.com_60
      - dongtaiwang.com_61
      - dongtaiwang.com_62
      - dongtaiwang.com_63
      - dongtaiwang.com_64
      - dongtaiwang.com_65
      - dongtaiwang.com_66
      - dongtaiwang.com_67
      - dongtaiwang.com_68
      - dongtaiwang.com_69
      - dongtaiwang.com_70
      - dongtaiwang.com_71
      - dongtaiwang.com_72
      - dongtaiwang.com_73
      - dongtaiwang.com_74
      - dongtaiwang.com_75
      - dongtaiwang.com_76
      - dongtaiwang.com_77
      - dongtaiwang.com_78
      - dongtaiwang.com_79
      - dongtaiwang.com_80
      - dongtaiwang.com_81
      - dongtaiwang.com_82
      - dongtaiwang.com_83
      - dongtaiwang.com_84
      - dongtaiwang.com_85
      - dongtaiwang.com_86
      - dongtaiwang.com_87
      - dongtaiwang.com_88
      - dongtaiwang.com_89
      - dongtaiwang.com_90
      - dongtaiwang.com_91
      - dongtaiwang.com_92
      - dongtaiwang.com_93
      - dongtaiwang.com_94
      - dongtaiwang.com_95
      - dongtaiwang.com_96
      - dongtaiwang.com_97
      - dongtaiwang.com_98
      - dongtaiwang.com_99
      - dongtaiwang.com_100
      - dongtaiwang.com_101
      - dongtaiwang.com_102
      - dongtaiwang.com_103
      - dongtaiwang.com_104
      - dongtaiwang.com_105
      - dongtaiwang.com_106
      - dongtaiwang.com_107
      - dongtaiwang.com_108
      - dongtaiwang.com_109
      - dongtaiwang.com_110
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
      - dongtaiwang.com_17
      - dongtaiwang.com_18
      - dongtaiwang.com_19
      - dongtaiwang.com_20
      - dongtaiwang.com_21
      - dongtaiwang.com_22
      - dongtaiwang.com_23
      - dongtaiwang.com_24
      - dongtaiwang.com_25
      - dongtaiwang.com_26
      - dongtaiwang.com_27
      - dongtaiwang.com_28
      - dongtaiwang.com_29
      - dongtaiwang.com_30
      - dongtaiwang.com_31
      - dongtaiwang.com_32
      - dongtaiwang.com_33
      - dongtaiwang.com_34
      - dongtaiwang.com_35
      - dongtaiwang.com_36
      - dongtaiwang.com_37
      - dongtaiwang.com_38
      - dongtaiwang.com_39
      - dongtaiwang.com_40
      - dongtaiwang.com_41
      - dongtaiwang.com_42
      - dongtaiwang.com_43
      - dongtaiwang.com_44
      - dongtaiwang.com_45
      - dongtaiwang.com_46
      - dongtaiwang.com_47
      - dongtaiwang.com_48
      - dongtaiwang.com_49
      - dongtaiwang.com_50
      - dongtaiwang.com_51
      - dongtaiwang.com_52
      - dongtaiwang.com_53
      - dongtaiwang.com_54
      - dongtaiwang.com_55
      - dongtaiwang.com_56
      - dongtaiwang.com_57
      - dongtaiwang.com_58
      - dongtaiwang.com_59
      - dongtaiwang.com_60
      - dongtaiwang.com_61
      - dongtaiwang.com_62
      - dongtaiwang.com_63
      - dongtaiwang.com_64
      - dongtaiwang.com_65
      - dongtaiwang.com_66
      - dongtaiwang.com_67
      - dongtaiwang.com_68
      - dongtaiwang.com_69
      - dongtaiwang.com_70
      - dongtaiwang.com_71
      - dongtaiwang.com_72
      - dongtaiwang.com_73
      - dongtaiwang.com_74
      - dongtaiwang.com_75
      - dongtaiwang.com_76
      - dongtaiwang.com_77
      - dongtaiwang.com_78
      - dongtaiwang.com_79
      - dongtaiwang.com_80
      - dongtaiwang.com_81
      - dongtaiwang.com_82
      - dongtaiwang.com_83
      - dongtaiwang.com_84
      - dongtaiwang.com_85
      - dongtaiwang.com_86
      - dongtaiwang.com_87
      - dongtaiwang.com_88
      - dongtaiwang.com_89
      - dongtaiwang.com_90
      - dongtaiwang.com_91
      - dongtaiwang.com_92
      - dongtaiwang.com_93
      - dongtaiwang.com_94
      - dongtaiwang.com_95
      - dongtaiwang.com_96
      - dongtaiwang.com_97
      - dongtaiwang.com_98
      - dongtaiwang.com_99
      - dongtaiwang.com_100
      - dongtaiwang.com_101
      - dongtaiwang.com_102
      - dongtaiwang.com_103
      - dongtaiwang.com_104
      - dongtaiwang.com_105
      - dongtaiwang.com_106
      - dongtaiwang.com_107
      - dongtaiwang.com_108
      - dongtaiwang.com_109
      - dongtaiwang.com_110
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
      - dongtaiwang.com_17
      - dongtaiwang.com_18
      - dongtaiwang.com_19
      - dongtaiwang.com_20
      - dongtaiwang.com_21
      - dongtaiwang.com_22
      - dongtaiwang.com_23
      - dongtaiwang.com_24
      - dongtaiwang.com_25
      - dongtaiwang.com_26
      - dongtaiwang.com_27
      - dongtaiwang.com_28
      - dongtaiwang.com_29
      - dongtaiwang.com_30
      - dongtaiwang.com_31
      - dongtaiwang.com_32
      - dongtaiwang.com_33
      - dongtaiwang.com_34
      - dongtaiwang.com_35
      - dongtaiwang.com_36
      - dongtaiwang.com_37
      - dongtaiwang.com_38
      - dongtaiwang.com_39
      - dongtaiwang.com_40
      - dongtaiwang.com_41
      - dongtaiwang.com_42
      - dongtaiwang.com_43
      - dongtaiwang.com_44
      - dongtaiwang.com_45
      - dongtaiwang.com_46
      - dongtaiwang.com_47
      - dongtaiwang.com_48
      - dongtaiwang.com_49
      - dongtaiwang.com_50
      - dongtaiwang.com_51
      - dongtaiwang.com_52
      - dongtaiwang.com_53
      - dongtaiwang.com_54
      - dongtaiwang.com_55
      - dongtaiwang.com_56
      - dongtaiwang.com_57
      - dongtaiwang.com_58
      - dongtaiwang.com_59
      - dongtaiwang.com_60
      - dongtaiwang.com_61
      - dongtaiwang.com_62
      - dongtaiwang.com_63
      - dongtaiwang.com_64
      - dongtaiwang.com_65
      - dongtaiwang.com_66
      - dongtaiwang.com_67
      - dongtaiwang.com_68
      - dongtaiwang.com_69
      - dongtaiwang.com_70
      - dongtaiwang.com_71
      - dongtaiwang.com_72
      - dongtaiwang.com_73
      - dongtaiwang.com_74
      - dongtaiwang.com_75
      - dongtaiwang.com_76
      - dongtaiwang.com_77
      - dongtaiwang.com_78
      - dongtaiwang.com_79
      - dongtaiwang.com_80
      - dongtaiwang.com_81
      - dongtaiwang.com_82
      - dongtaiwang.com_83
      - dongtaiwang.com_84
      - dongtaiwang.com_85
      - dongtaiwang.com_86
      - dongtaiwang.com_87
      - dongtaiwang.com_88
      - dongtaiwang.com_89
      - dongtaiwang.com_90
      - dongtaiwang.com_91
      - dongtaiwang.com_92
      - dongtaiwang.com_93
      - dongtaiwang.com_94
      - dongtaiwang.com_95
      - dongtaiwang.com_96
      - dongtaiwang.com_97
      - dongtaiwang.com_98
      - dongtaiwang.com_99
      - dongtaiwang.com_100
      - dongtaiwang.com_101
      - dongtaiwang.com_102
      - dongtaiwang.com_103
      - dongtaiwang.com_104
      - dongtaiwang.com_105
      - dongtaiwang.com_106
      - dongtaiwang.com_107
      - dongtaiwang.com_108
      - dongtaiwang.com_109
      - dongtaiwang.com_110
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
      - dongtaiwang.com_17
      - dongtaiwang.com_18
      - dongtaiwang.com_19
      - dongtaiwang.com_20
      - dongtaiwang.com_21
      - dongtaiwang.com_22
      - dongtaiwang.com_23
      - dongtaiwang.com_24
      - dongtaiwang.com_25
      - dongtaiwang.com_26
      - dongtaiwang.com_27
      - dongtaiwang.com_28
      - dongtaiwang.com_29
      - dongtaiwang.com_30
      - dongtaiwang.com_31
      - dongtaiwang.com_32
      - dongtaiwang.com_33
      - dongtaiwang.com_34
      - dongtaiwang.com_35
      - dongtaiwang.com_36
      - dongtaiwang.com_37
      - dongtaiwang.com_38
      - dongtaiwang.com_39
      - dongtaiwang.com_40
      - dongtaiwang.com_41
      - dongtaiwang.com_42
      - dongtaiwang.com_43
      - dongtaiwang.com_44
      - dongtaiwang.com_45
      - dongtaiwang.com_46
      - dongtaiwang.com_47
      - dongtaiwang.com_48
      - dongtaiwang.com_49
      - dongtaiwang.com_50
      - dongtaiwang.com_51
      - dongtaiwang.com_52
      - dongtaiwang.com_53
      - dongtaiwang.com_54
      - dongtaiwang.com_55
      - dongtaiwang.com_56
      - dongtaiwang.com_57
      - dongtaiwang.com_58
      - dongtaiwang.com_59
      - dongtaiwang.com_60
      - dongtaiwang.com_61
      - dongtaiwang.com_62
      - dongtaiwang.com_63
      - dongtaiwang.com_64
      - dongtaiwang.com_65
      - dongtaiwang.com_66
      - dongtaiwang.com_67
      - dongtaiwang.com_68
      - dongtaiwang.com_69
      - dongtaiwang.com_70
      - dongtaiwang.com_71
      - dongtaiwang.com_72
      - dongtaiwang.com_73
      - dongtaiwang.com_74
      - dongtaiwang.com_75
      - dongtaiwang.com_76
      - dongtaiwang.com_77
      - dongtaiwang.com_78
      - dongtaiwang.com_79
      - dongtaiwang.com_80
      - dongtaiwang.com_81
      - dongtaiwang.com_82
      - dongtaiwang.com_83
      - dongtaiwang.com_84
      - dongtaiwang.com_85
      - dongtaiwang.com_86
      - dongtaiwang.com_87
      - dongtaiwang.com_88
      - dongtaiwang.com_89
      - dongtaiwang.com_90
      - dongtaiwang.com_91
      - dongtaiwang.com_92
      - dongtaiwang.com_93
      - dongtaiwang.com_94
      - dongtaiwang.com_95
      - dongtaiwang.com_96
      - dongtaiwang.com_97
      - dongtaiwang.com_98
      - dongtaiwang.com_99
      - dongtaiwang.com_100
      - dongtaiwang.com_101
      - dongtaiwang.com_102
      - dongtaiwang.com_103
      - dongtaiwang.com_104
      - dongtaiwang.com_105
      - dongtaiwang.com_106
      - dongtaiwang.com_107
      - dongtaiwang.com_108
      - dongtaiwang.com_109
      - dongtaiwang.com_110

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
