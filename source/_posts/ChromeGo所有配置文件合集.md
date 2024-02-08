
---
title: ChromeGo所有配置文件合集 
date: 2024-02-08 04:43:43
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

> Last Update Time: 2024-02-08 04:43:43
---

## Quick-ip_1.yaml
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
  - name: ip1 
    type: hysteria2
    server: 51.158.54.46
    port: 44550
    password: dongtaiwang.com
    sni: bing.com
    skip-cert-verify: true 
proxy-groups:
  - name: 🚀 节点选择
    type: select
    proxies:
      - ♻️ 自动选择
      - DIRECT
      - ip1
  - name: ♻️ 自动选择
    type: url-test
    url: https://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    proxies:
      - ip1
  - name: 🌍 国外媒体
    type: select
    proxies:
      - 🚀 节点选择
      - ♻️ 自动选择
      - 🎯 全球直连
      - ip1
  - name: 📲 电报信息
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - ip1
  - name: Ⓜ️ 微软服务
    type: select
    proxies:
      - 🎯 全球直连
      - 🚀 节点选择
      - ip1
  - name: 🍎 苹果服务
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - ip1
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
      - ip1

rules:
  - MATCH,🚀 节点选择

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

## Quick-ip_3.yaml
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
  - {"name":"quick_ip3","type":"hysteria","server":"www.dtku50.xyz","port":18470,"sni":"www.amazon.cn","skip-cert-verify":true,"alpn":["h3"],"protocol":"udp","auth_str":"dongtaiwang.com","up":2,"down":10}
proxy-groups:
  - name: 🚀 节点选择
    type: select
    proxies:
      - ♻️ 自动选择
      - DIRECT
      - quick_ip3
  - name: ♻️ 自动选择
    type: url-test
    url: https://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    proxies:
      - quick_ip3
  - name: 🌍 国外媒体
    type: select
    proxies:
      - 🚀 节点选择
      - ♻️ 自动选择
      - 🎯 全球直连
      - quick_ip3
  - name: 📲 电报信息
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - quick_ip3
  - name: Ⓜ️ 微软服务
    type: select
    proxies:
      - 🎯 全球直连
      - 🚀 节点选择
      - quick_ip3
  - name: 🍎 苹果服务
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - quick_ip3
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
      - quick_ip3

rules:
  - MATCH,🚀 节点选择


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
      "protocol": "shadowsocks",
      "settings": {
        "servers": [
          {
            "address": "www.dtku44.xyz",
            "method": "2022-blake3-aes-256-gcm",
            "ota": false,
            "password": "oats+7vdaSOb4NsxWwCBQll4qTwPu/dhpegiIGnqd9c=",
            "port": 22335,
            "level": 1
          }
        ]
      },
      "streamSettings": {
        "network": "tcp"
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
            "address": "108.181.22.213",
            "port": 28945,
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
  - {"name":"dongtaiwang.com_1","type":"hysteria","server":"51.159.103.141","port":18044,10000-13000,"sni":"bing.com","skip-cert-verify":true,"alpn":["h3"],"protocol":"udp","auth_str":"dongtaiwang.com","up":11,"down":55,"hop_interval":190}
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
  - {"name":"dongtaiwang.com_1","type":"tuic","server":"74.63.249.229","port":443,"udp":true,"uuid":"9a6140f4-abd8-4ece-aa0e-4f14556de56b","password":dongtaiwang.com,"alpn":["h3"],"disable-sni":true,"reduce-rtt":true,"udp-relay-mode":native,"congestion-controller":"bbr"}
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
  - {"name":"dongtaiwang.com_1","type":"tuic","server":"www2.dtku45.xyz","port":33098,"udp":true,"uuid":"fef3d3c2-ab3e-4134-a2f3-0c2d83e0a76d","password":dongtaiwang.com,"alpn":["h3"],"disable-sni":true,"reduce-rtt":true,"udp-relay-mode":native,"congestion-controller":"bbr"}
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
  - {"name":"dongtaiwang.com_1","type":"tuic","server":"195.137.220.189","port":33445,"udp":true,"uuid":"983a85bd-8fae-45d2-a702-5d00a383763e","password":dongtaiwang.com,"alpn":["h3"],"disable-sni":true,"reduce-rtt":true,"udp-relay-mode":native,"congestion-controller":"bbr"}
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

## clash.meta-ip_5.yaml
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
  - {"name":"dongtaiwang.com_1","type":"vless","server":"92.118.205.66","port":10081,"udp":true,"uuid":"7c009b14-ceb0-4373-9504-ab2a9ca2354a","tls":true,"servername":"images-na.ssl-images-amazon.com","network":"grpc","grpc-opts":{"grpc-service-name":"grpc"},"reality-opts":{"public-key":"JMHogufiGO132mtTq26O34ssU8rjCkUcFC98PSeMF3A","short-id":"6ba85179e30d4fc2"},"client-fingerprint":"chrome"}
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
  - {"name":"dongtaiwang.com_1","type":"vless","server":"92.118.205.66","port":10081,"udp":true,"uuid":"7c009b14-ceb0-4373-9504-ab2a9ca2354a","tls":true,"servername":"images-na.ssl-images-amazon.com","network":"grpc","grpc-opts":{"grpc-service-name":"grpc"},"reality-opts":{"public-key":"JMHogufiGO132mtTq26O34ssU8rjCkUcFC98PSeMF3A","short-id":"6ba85179e30d4fc2"},"client-fingerprint":"chrome"}
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

## hysteria-ip_1.json
```bash

{
"server": "51.158.54.46:55396",
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
"auth_str": "dongtaiwang.com",
"alpn": "h3",
"server_name": "youku.com",
"insecure": true,
"recv_window_conn": 115343360,
"recv_window": 461373440,
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
{
"server": "173.234.25.52:30072",
"protocol": "udp",
"up_mbps": 11,
"down_mbps": 55,
"http": {
"listen": "127.0.0.1:1081",
"timeout" : 300,
"disable_udp": false
},
"socks5": {
"listen": "127.0.0.1:1080",
"timeout": 300,
"disable_udp": false
},
"obfs": "",
"auth_str": "dongtaiwang.com",
"alpn": "h3",
"server_name": "bing.com",
"insecure": true,
"recv_window_conn": 115343360,
"recv_window": 461373440,
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

## hysteria-ip_4.json
```bash
{
"server": "108.181.22.239:39967",
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
"auth_str": "dongtaiwang.com",
"alpn": "h3",
"server_name": "bing.com",
"insecure": true,
"recv_window_conn": 115343360,
"recv_window": 461373440,
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
{
  "server": "64.110.25.11:33337",
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
{
  "server": "108.181.24.77:43656",
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
{
  "listen": "socks://127.0.0.1:1080",
  "proxy": "https://dongtaiwang.com:dongtaiwang.com@naive19.cfcdn3.xyz:443"
}

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
      "server": "www2.dtku48.xyz", 
      "server_port": 22334,
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
