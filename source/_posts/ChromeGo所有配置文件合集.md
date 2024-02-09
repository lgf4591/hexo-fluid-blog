
---
title: ChromeGo所有配置文件合集 
date: 2024-02-09 10:49:57
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

> Last Update Time: 2024-02-09 10:49:57
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
  - {"name":"freenode_1","type":"vless","server":"198.41.220.176","port":2083,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_2","type":"vless","server":"hk03.nttkk.com","port":443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_3","type":"vless","server":"104.17.208.177","port":2096,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_4","type":"vless","server":"104.17.213.5","port":2083,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_5","type":"vless","server":"104.17.223.161","port":2083,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_6","type":"vless","server":"104.19.155.105","port":2083,"uuid":"ffffffff-17ad-45e7-aaa1-f2baaa08e930","tls":true,"servername":"watashi.free.jppublic.moh539.link","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"watashi.free.jppublic.moh539.link"}}}
  - {"name":"freenode_7","type":"vless","server":"104.17.210.131","port":2087,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_8","type":"vless","server":"104.17.212.239","port":8443,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_9","type":"vless","server":"43.153.181.217","port":443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_10","type":"vless","server":"104.16.96.82","port":8443,"uuid":"ffffffff-17ad-45e7-aaa1-f2baaa08e930","tls":true,"servername":"watashi.free.jppublic.moh539.link","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"watashi.free.jppublic.moh539.link"}}}
  - {"name":"freenode_11","type":"vless","server":"104.17.215.241","port":8443,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_12","type":"vless","server":"104.17.214.39","port":8443,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_13","type":"vless","server":"198.41.220.158","port":2087,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_14","type":"vless","server":"104.17.210.128","port":2083,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_15","type":"vless","server":"104.21.30.178","port":2087,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_16","type":"vless","server":"104.17.210.138","port":2096,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_17","type":"vless","server":"198.41.221.80","port":2083,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_18","type":"vless","server":"198.41.221.237","port":443,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_19","type":"vless","server":"104.21.17.151","port":443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_20","type":"vless","server":"104.17.221.226","port":2096,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_21","type":"vless","server":"104.21.0.236","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_22","type":"vless","server":"104.17.219.35","port":2096,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_23","type":"vless","server":"jgw.wshyx.pp.ua","port":2087,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_24","type":"vless","server":"198.41.221.12","port":2096,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_25","type":"vless","server":"104.21.28.147","port":2083,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_26","type":"vless","server":"198.41.209.150","port":8443,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_27","type":"vless","server":"104.19.155.11","port":8443,"uuid":"ffffffff-17ad-45e7-aaa1-f2baaa08e930","tls":true,"servername":"watashi.free.jppublic.moh539.link","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"watashi.free.jppublic.moh539.link"}}}
  - {"name":"freenode_28","type":"vless","server":"104.21.4.246","port":2083,"uuid":"d342d11e-d424-4583-b36e-524ab1f0afa4","tls":true,"servername":"edgood.king361.cf","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"edgood.king361.cf"}}}
  - {"name":"freenode_29","type":"vless","server":"104.16.96.218","port":2087,"uuid":"ffffffff-17ad-45e7-aaa1-f2baaa08e930","tls":true,"servername":"watashi.free.jppublic.moh539.link","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"watashi.free.jppublic.moh539.link"}}}
  - {"name":"freenode_30","type":"vless","server":"lilijuly.pp.ua","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_31","type":"vless","server":"104.17.208.174","port":8443,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_32","type":"vless","server":"104.21.5.7","port":8443,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode_33","type":"vless","server":"104.17.210.9","port":2083,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_34","type":"vless","server":"104.21.2.0","port":8443,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode_35","type":"vless","server":"104.21.5.33","port":2083,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode_36","type":"vless","server":"104.21.12.151","port":2087,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode_37","type":"vless","server":"104.21.12.84","port":443,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode_38","type":"vless","server":"104.17.219.151","port":8443,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_39","type":"vless","server":"104.21.15.243","port":2096,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode_40","type":"vless","server":"xwm-us-v6-a.mouboss.pp.ua","port":2083,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_41","type":"vless","server":"dvorda.pp.ua","port":2096,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_42","type":"vless","server":"104.21.30.176","port":2096,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_43","type":"vless","server":"smi.pp.ua","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_44","type":"vless","server":"104.21.28.29","port":2053,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_45","type":"vless","server":"104.16.96.197","port":2087,"uuid":"ffffffff-17ad-45e7-aaa1-f2baaa08e930","tls":true,"servername":"watashi.free.jppublic.moh539.link","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"watashi.free.jppublic.moh539.link"}}}
  - {"name":"freenode_46","type":"vless","server":"104.16.96.54","port":8443,"uuid":"ffffffff-17ad-45e7-aaa1-f2baaa08e930","tls":true,"servername":"watashi.free.jppublic.moh539.link","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"watashi.free.jppublic.moh539.link"}}}
  - {"name":"freenode_47","type":"vless","server":"198.41.221.195","port":2096,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_48","type":"vless","server":"jp7.vlessx.us","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_49","type":"vless","server":"104.21.17.152","port":2083,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_50","type":"vless","server":"104.21.0.169","port":443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_51","type":"vless","server":"104.21.2.68","port":2087,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode_52","type":"vless","server":"smi.pp.ua","port":2083,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_53","type":"vless","server":"104.21.4.87","port":2083,"uuid":"d342d11e-d424-4583-b36e-524ab1f0afa4","tls":true,"servername":"edgood.king361.cf","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"edgood.king361.cf"}}}
  - {"name":"freenode_54","type":"vless","server":"104.21.5.172","port":2053,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode_55","type":"vless","server":"104.21.4.183","port":2087,"uuid":"d342d11e-d424-4583-b36e-524ab1f0afa4","tls":true,"servername":"edgood.king361.cf","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"edgood.king361.cf"}}}
  - {"name":"freenode_56","type":"vless","server":"smi.pp.ua","port":443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_57","type":"vless","server":"104.21.1.138","port":2087,"uuid":"ffffffff-17ad-45e7-aaa1-f2baaa08e930","tls":true,"servername":"watashi.free.jppublic.moh539.link","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"watashi.free.jppublic.moh539.link"}}}
  - {"name":"freenode_58","type":"vless","server":"104.18.190.52","port":443,"uuid":"a4faf5d8-b9a8-433e-9518-2d2e21d76f78","tls":true,"servername":"nginx.nirevil.ir","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"nginx.nirevil.ir"}}}
  - {"name":"freenode_59","type":"vless","server":"198.41.208.156","port":2087,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_60","type":"vless","server":"104.21.0.152","port":2053,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_61","type":"vless","server":"a.noonokorean.pp.ua","port":2096,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_62","type":"vless","server":"104.21.16.238","port":443,"uuid":"ffffffff-17ad-45e7-aaa1-f2baaa08e930","tls":true,"servername":"watashi.free.jppublic.moh539.link","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"watashi.free.jppublic.moh539.link"}}}
  - {"name":"freenode_63","type":"vless","server":"104.21.1.250","port":8443,"uuid":"ffffffff-17ad-45e7-aaa1-f2baaa08e930","tls":true,"servername":"watashi.free.jppublic.moh539.link","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"watashi.free.jppublic.moh539.link"}}}
  - {"name":"freenode_64","type":"vless","server":"104.21.26.225","port":2083,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_65","type":"vless","server":"104.17.209.149","port":2083,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_66","type":"vless","server":"us10.vlessx.us","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_67","type":"vless","server":"104.21.26.230","port":8443,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_68","type":"vless","server":"104.21.28.62","port":443,"uuid":"b9ad895b-12ac-40fc-a5ac-a5b2a1285001","tls":true,"servername":"3k.pureboy.eu.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.pureboy.eu.org"}}}
  - {"name":"freenode_69","type":"vless","server":"104.21.2.96","port":2087,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode_70","type":"vless","server":"104.21.14.245","port":2087,"uuid":"d342d11e-d424-4583-b36e-524ab1f0afa4","tls":true,"servername":"edgood.king361.cf","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"edgood.king361.cf"}}}
  - {"name":"freenode_71","type":"vless","server":"104.21.15.55","port":2083,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode_72","type":"vless","server":"198.41.221.173","port":2087,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_73","type":"vless","server":"104.21.15.226","port":2087,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode_74","type":"vless","server":"104.21.2.173","port":2096,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode_75","type":"vless","server":"ctwct.arvancode.eu.org","port":2096,"uuid":"f4cec6cc-6177-423c-90f8-2ad9f0dd996b","tls":true,"servername":"vpnct.arvancode.eu.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"vpnct.arvancode.eu.org"}}}
  - {"name":"freenode_76","type":"vless","server":"104.21.0.177","port":2053,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_77","type":"vless","server":"jgw.wshyx.pp.ua","port":2083,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_78","type":"vless","server":"104.21.24.7","port":8443,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_79","type":"vless","server":"104.21.2.219","port":2096,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode_80","type":"vless","server":"104.21.15.243","port":2053,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode_81","type":"vless","server":"104.21.1.147","port":2053,"uuid":"ffffffff-17ad-45e7-aaa1-f2baaa08e930","tls":true,"servername":"watashi.free.jppublic.moh539.link","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"watashi.free.jppublic.moh539.link"}}}
  - {"name":"freenode_82","type":"vless","server":"104.21.12.140","port":2053,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode_83","type":"vless","server":"198.41.209.180","port":2053,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_84","type":"vless","server":"tz.lilijuly.pp.ua","port":2083,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_85","type":"vless","server":"i.noonokorean.pp.ua","port":2096,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_86","type":"vless","server":"88888.pp.ua","port":2087,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_87","type":"vless","server":"104.21.1.179","port":2096,"uuid":"ffffffff-17ad-45e7-aaa1-f2baaa08e930","tls":true,"servername":"watashi.free.jppublic.moh539.link","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"watashi.free.jppublic.moh539.link"}}}
  - {"name":"freenode_88","type":"vless","server":"104.21.0.57","port":2083,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_89","type":"vless","server":"104.21.12.186","port":2087,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode_90","type":"vless","server":"104.21.4.98","port":2083,"uuid":"d342d11e-d424-4583-b36e-524ab1f0afa4","tls":true,"servername":"edgood.king361.cf","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"edgood.king361.cf"}}}
  - {"name":"freenode_91","type":"vless","server":"104.21.30.250","port":8443,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_92","type":"vless","server":"104.21.1.214","port":2053,"uuid":"ffffffff-17ad-45e7-aaa1-f2baaa08e930","tls":true,"servername":"watashi.free.jppublic.moh539.link","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"watashi.free.jppublic.moh539.link"}}}
  - {"name":"freenode_93","type":"vless","server":"104.21.2.235","port":2096,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode_94","type":"vless","server":"us21.vlessx.us","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_95","type":"vless","server":"104.21.24.179","port":2096,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_96","type":"vless","server":"nl26.vlessx.us","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_97","type":"vless","server":"sg2.vlessx.xyz","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_98","type":"vless","server":"nl2.vlessx.us","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_99","type":"vless","server":"104.21.2.68","port":8443,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode_100","type":"vless","server":"198.41.209.83","port":2087,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_101","type":"vless","server":"c.noonokorean.pp.ua","port":2096,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_102","type":"vless","server":"104.21.0.64","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_103","type":"vless","server":"104.21.5.54","port":2096,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode_104","type":"vless","server":"104.21.5.192","port":2087,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode_105","type":"vless","server":"104.21.2.35","port":443,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode_106","type":"vless","server":"sg18.vlessx.xyz","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_107","type":"vless","server":"104.21.26.150","port":2083,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_108","type":"vless","server":"nl35.vlessx.us","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_109","type":"vless","server":"104.21.30.247","port":2096,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_110","type":"vless","server":"smi.pp.ua","port":2053,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode_111","type":"vless","server":"www.butech.pp.ua","port":2083,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_112","type":"vless","server":"104.21.0.229","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_113","type":"vless","server":"104.21.2.223","port":2087,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode_114","type":"vless","server":"cao.pp.ua","port":2087,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_115","type":"vless","server":"104.17.215.14","port":8443,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_116","type":"vless","server":"104.17.221.174","port":2083,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_117","type":"vless","server":"104.21.2.151","port":2053,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode_118","type":"vless","server":"104.21.25.161","port":2083,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_119","type":"vless","server":"104.21.17.245","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_120","type":"vless","server":"www.ipget.net","port":2083,"uuid":"a13df940-020c-465f-bc89-ee5279b5cd6a","tls":true,"servername":"ss2.wang66.homes","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ss2.wang66.homes"}}}
  - {"name":"freenode_121","type":"vless","server":"8.222.212.255","port":443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_122","type":"vless","server":"de4.vlessx.xyz","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_123","type":"vless","server":"sg30.vlessx.xyz","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_124","type":"vless","server":"104.21.4.136","port":8443,"uuid":"d342d11e-d424-4583-b36e-524ab1f0afa4","tls":true,"servername":"edgood.king361.cf","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"edgood.king361.cf"}}}
  - {"name":"freenode_125","type":"vless","server":"sg22.vlessx.xyz","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_126","type":"vless","server":"104.21.5.77","port":2096,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode_127","type":"vless","server":"104.17.217.35","port":2053,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_128","type":"vless","server":"104.21.2.199","port":443,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode_129","type":"vless","server":"104.21.24.113","port":2083,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_130","type":"vless","server":"104.21.0.210","port":2096,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_131","type":"vless","server":"104.21.17.242","port":2096,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_132","type":"vless","server":"104.21.2.21","port":443,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode_133","type":"vless","server":"104.21.4.192","port":2083,"uuid":"d342d11e-d424-4583-b36e-524ab1f0afa4","tls":true,"servername":"edgood.king361.cf","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"edgood.king361.cf"}}}
  - {"name":"freenode_134","type":"vless","server":"104.21.29.156","port":2053,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_135","type":"vless","server":"104.17.209.81","port":2053,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_136","type":"vless","server":"104.21.0.124","port":2053,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_137","type":"vless","server":"cc.zxj.pp.ua","port":2087,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_138","type":"vless","server":"104.21.2.104","port":2083,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode_139","type":"vless","server":"104.21.17.101","port":2096,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_140","type":"vless","server":"104.21.17.244","port":443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_141","type":"vless","server":"104.21.14.35","port":2087,"uuid":"d342d11e-d424-4583-b36e-524ab1f0afa4","tls":true,"servername":"edgood.king361.cf","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"edgood.king361.cf"}}}
  - {"name":"freenode_142","type":"vless","server":"104.21.2.29","port":2096,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode_143","type":"vless","server":"104.17.213.167","port":2083,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_144","type":"vless","server":"104.21.0.74","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_145","type":"vless","server":"104.21.30.242","port":2087,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_146","type":"vless","server":"104.21.4.93","port":8443,"uuid":"d342d11e-d424-4583-b36e-524ab1f0afa4","tls":true,"servername":"edgood.king361.cf","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"edgood.king361.cf"}}}
  - {"name":"freenode_147","type":"vless","server":"104.21.2.5","port":2083,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode_148","type":"vless","server":"104.21.30.148","port":2053,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_149","type":"vless","server":"108.162.192.100","port":443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_150","type":"vless","server":"198.41.220.60","port":2096,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_151","type":"vless","server":"104.21.0.96","port":2096,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_152","type":"vless","server":"104.21.28.51","port":2053,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode_153","type":"vless","server":"nl62.vlessx.us","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode_154","type":"vless","server":"chat.opo.pp.ua","port":2096,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
proxy-groups:
  - name: 🚀 节点选择
    type: select
    proxies:
      - ♻️ 自动选择
      - DIRECT
      - freenode_1
      - freenode_2
      - freenode_3
      - freenode_4
      - freenode_5
      - freenode_6
      - freenode_7
      - freenode_8
      - freenode_9
      - freenode_10
      - freenode_11
      - freenode_12
      - freenode_13
      - freenode_14
      - freenode_15
      - freenode_16
      - freenode_17
      - freenode_18
      - freenode_19
      - freenode_20
      - freenode_21
      - freenode_22
      - freenode_23
      - freenode_24
      - freenode_25
      - freenode_26
      - freenode_27
      - freenode_28
      - freenode_29
      - freenode_30
      - freenode_31
      - freenode_32
      - freenode_33
      - freenode_34
      - freenode_35
      - freenode_36
      - freenode_37
      - freenode_38
      - freenode_39
      - freenode_40
      - freenode_41
      - freenode_42
      - freenode_43
      - freenode_44
      - freenode_45
      - freenode_46
      - freenode_47
      - freenode_48
      - freenode_49
      - freenode_50
      - freenode_51
      - freenode_52
      - freenode_53
      - freenode_54
      - freenode_55
      - freenode_56
      - freenode_57
      - freenode_58
      - freenode_59
      - freenode_60
      - freenode_61
      - freenode_62
      - freenode_63
      - freenode_64
      - freenode_65
      - freenode_66
      - freenode_67
      - freenode_68
      - freenode_69
      - freenode_70
      - freenode_71
      - freenode_72
      - freenode_73
      - freenode_74
      - freenode_75
      - freenode_76
      - freenode_77
      - freenode_78
      - freenode_79
      - freenode_80
      - freenode_81
      - freenode_82
      - freenode_83
      - freenode_84
      - freenode_85
      - freenode_86
      - freenode_87
      - freenode_88
      - freenode_89
      - freenode_90
      - freenode_91
      - freenode_92
      - freenode_93
      - freenode_94
      - freenode_95
      - freenode_96
      - freenode_97
      - freenode_98
      - freenode_99
      - freenode_100
      - freenode_101
      - freenode_102
      - freenode_103
      - freenode_104
      - freenode_105
      - freenode_106
      - freenode_107
      - freenode_108
      - freenode_109
      - freenode_110
      - freenode_111
      - freenode_112
      - freenode_113
      - freenode_114
      - freenode_115
      - freenode_116
      - freenode_117
      - freenode_118
      - freenode_119
      - freenode_120
      - freenode_121
      - freenode_122
      - freenode_123
      - freenode_124
      - freenode_125
      - freenode_126
      - freenode_127
      - freenode_128
      - freenode_129
      - freenode_130
      - freenode_131
      - freenode_132
      - freenode_133
      - freenode_134
      - freenode_135
      - freenode_136
      - freenode_137
      - freenode_138
      - freenode_139
      - freenode_140
      - freenode_141
      - freenode_142
      - freenode_143
      - freenode_144
      - freenode_145
      - freenode_146
      - freenode_147
      - freenode_148
      - freenode_149
      - freenode_150
      - freenode_151
      - freenode_152
      - freenode_153
      - freenode_154

  - name: ♻️ 自动选择
    type: url-test
    url: https://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    proxies:
      - freenode_1
      - freenode_2
      - freenode_3
      - freenode_4
      - freenode_5
      - freenode_6
      - freenode_7
      - freenode_8
      - freenode_9
      - freenode_10
      - freenode_11
      - freenode_12
      - freenode_13
      - freenode_14
      - freenode_15
      - freenode_16
      - freenode_17
      - freenode_18
      - freenode_19
      - freenode_20
      - freenode_21
      - freenode_22
      - freenode_23
      - freenode_24
      - freenode_25
      - freenode_26
      - freenode_27
      - freenode_28
      - freenode_29
      - freenode_30
      - freenode_31
      - freenode_32
      - freenode_33
      - freenode_34
      - freenode_35
      - freenode_36
      - freenode_37
      - freenode_38
      - freenode_39
      - freenode_40
      - freenode_41
      - freenode_42
      - freenode_43
      - freenode_44
      - freenode_45
      - freenode_46
      - freenode_47
      - freenode_48
      - freenode_49
      - freenode_50
      - freenode_51
      - freenode_52
      - freenode_53
      - freenode_54
      - freenode_55
      - freenode_56
      - freenode_57
      - freenode_58
      - freenode_59
      - freenode_60
      - freenode_61
      - freenode_62
      - freenode_63
      - freenode_64
      - freenode_65
      - freenode_66
      - freenode_67
      - freenode_68
      - freenode_69
      - freenode_70
      - freenode_71
      - freenode_72
      - freenode_73
      - freenode_74
      - freenode_75
      - freenode_76
      - freenode_77
      - freenode_78
      - freenode_79
      - freenode_80
      - freenode_81
      - freenode_82
      - freenode_83
      - freenode_84
      - freenode_85
      - freenode_86
      - freenode_87
      - freenode_88
      - freenode_89
      - freenode_90
      - freenode_91
      - freenode_92
      - freenode_93
      - freenode_94
      - freenode_95
      - freenode_96
      - freenode_97
      - freenode_98
      - freenode_99
      - freenode_100
      - freenode_101
      - freenode_102
      - freenode_103
      - freenode_104
      - freenode_105
      - freenode_106
      - freenode_107
      - freenode_108
      - freenode_109
      - freenode_110
      - freenode_111
      - freenode_112
      - freenode_113
      - freenode_114
      - freenode_115
      - freenode_116
      - freenode_117
      - freenode_118
      - freenode_119
      - freenode_120
      - freenode_121
      - freenode_122
      - freenode_123
      - freenode_124
      - freenode_125
      - freenode_126
      - freenode_127
      - freenode_128
      - freenode_129
      - freenode_130
      - freenode_131
      - freenode_132
      - freenode_133
      - freenode_134
      - freenode_135
      - freenode_136
      - freenode_137
      - freenode_138
      - freenode_139
      - freenode_140
      - freenode_141
      - freenode_142
      - freenode_143
      - freenode_144
      - freenode_145
      - freenode_146
      - freenode_147
      - freenode_148
      - freenode_149
      - freenode_150
      - freenode_151
      - freenode_152
      - freenode_153
      - freenode_154

  - name: 🌍 国外媒体
    type: select
    proxies:
      - 🚀 节点选择
      - ♻️ 自动选择
      - 🎯 全球直连
      - freenode_1
      - freenode_2
      - freenode_3
      - freenode_4
      - freenode_5
      - freenode_6
      - freenode_7
      - freenode_8
      - freenode_9
      - freenode_10
      - freenode_11
      - freenode_12
      - freenode_13
      - freenode_14
      - freenode_15
      - freenode_16
      - freenode_17
      - freenode_18
      - freenode_19
      - freenode_20
      - freenode_21
      - freenode_22
      - freenode_23
      - freenode_24
      - freenode_25
      - freenode_26
      - freenode_27
      - freenode_28
      - freenode_29
      - freenode_30
      - freenode_31
      - freenode_32
      - freenode_33
      - freenode_34
      - freenode_35
      - freenode_36
      - freenode_37
      - freenode_38
      - freenode_39
      - freenode_40
      - freenode_41
      - freenode_42
      - freenode_43
      - freenode_44
      - freenode_45
      - freenode_46
      - freenode_47
      - freenode_48
      - freenode_49
      - freenode_50
      - freenode_51
      - freenode_52
      - freenode_53
      - freenode_54
      - freenode_55
      - freenode_56
      - freenode_57
      - freenode_58
      - freenode_59
      - freenode_60
      - freenode_61
      - freenode_62
      - freenode_63
      - freenode_64
      - freenode_65
      - freenode_66
      - freenode_67
      - freenode_68
      - freenode_69
      - freenode_70
      - freenode_71
      - freenode_72
      - freenode_73
      - freenode_74
      - freenode_75
      - freenode_76
      - freenode_77
      - freenode_78
      - freenode_79
      - freenode_80
      - freenode_81
      - freenode_82
      - freenode_83
      - freenode_84
      - freenode_85
      - freenode_86
      - freenode_87
      - freenode_88
      - freenode_89
      - freenode_90
      - freenode_91
      - freenode_92
      - freenode_93
      - freenode_94
      - freenode_95
      - freenode_96
      - freenode_97
      - freenode_98
      - freenode_99
      - freenode_100
      - freenode_101
      - freenode_102
      - freenode_103
      - freenode_104
      - freenode_105
      - freenode_106
      - freenode_107
      - freenode_108
      - freenode_109
      - freenode_110
      - freenode_111
      - freenode_112
      - freenode_113
      - freenode_114
      - freenode_115
      - freenode_116
      - freenode_117
      - freenode_118
      - freenode_119
      - freenode_120
      - freenode_121
      - freenode_122
      - freenode_123
      - freenode_124
      - freenode_125
      - freenode_126
      - freenode_127
      - freenode_128
      - freenode_129
      - freenode_130
      - freenode_131
      - freenode_132
      - freenode_133
      - freenode_134
      - freenode_135
      - freenode_136
      - freenode_137
      - freenode_138
      - freenode_139
      - freenode_140
      - freenode_141
      - freenode_142
      - freenode_143
      - freenode_144
      - freenode_145
      - freenode_146
      - freenode_147
      - freenode_148
      - freenode_149
      - freenode_150
      - freenode_151
      - freenode_152
      - freenode_153
      - freenode_154
  - name: 📲 电报信息
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - freenode_1
      - freenode_2
      - freenode_3
      - freenode_4
      - freenode_5
      - freenode_6
      - freenode_7
      - freenode_8
      - freenode_9
      - freenode_10
      - freenode_11
      - freenode_12
      - freenode_13
      - freenode_14
      - freenode_15
      - freenode_16
      - freenode_17
      - freenode_18
      - freenode_19
      - freenode_20
      - freenode_21
      - freenode_22
      - freenode_23
      - freenode_24
      - freenode_25
      - freenode_26
      - freenode_27
      - freenode_28
      - freenode_29
      - freenode_30
      - freenode_31
      - freenode_32
      - freenode_33
      - freenode_34
      - freenode_35
      - freenode_36
      - freenode_37
      - freenode_38
      - freenode_39
      - freenode_40
      - freenode_41
      - freenode_42
      - freenode_43
      - freenode_44
      - freenode_45
      - freenode_46
      - freenode_47
      - freenode_48
      - freenode_49
      - freenode_50
      - freenode_51
      - freenode_52
      - freenode_53
      - freenode_54
      - freenode_55
      - freenode_56
      - freenode_57
      - freenode_58
      - freenode_59
      - freenode_60
      - freenode_61
      - freenode_62
      - freenode_63
      - freenode_64
      - freenode_65
      - freenode_66
      - freenode_67
      - freenode_68
      - freenode_69
      - freenode_70
      - freenode_71
      - freenode_72
      - freenode_73
      - freenode_74
      - freenode_75
      - freenode_76
      - freenode_77
      - freenode_78
      - freenode_79
      - freenode_80
      - freenode_81
      - freenode_82
      - freenode_83
      - freenode_84
      - freenode_85
      - freenode_86
      - freenode_87
      - freenode_88
      - freenode_89
      - freenode_90
      - freenode_91
      - freenode_92
      - freenode_93
      - freenode_94
      - freenode_95
      - freenode_96
      - freenode_97
      - freenode_98
      - freenode_99
      - freenode_100
      - freenode_101
      - freenode_102
      - freenode_103
      - freenode_104
      - freenode_105
      - freenode_106
      - freenode_107
      - freenode_108
      - freenode_109
      - freenode_110
      - freenode_111
      - freenode_112
      - freenode_113
      - freenode_114
      - freenode_115
      - freenode_116
      - freenode_117
      - freenode_118
      - freenode_119
      - freenode_120
      - freenode_121
      - freenode_122
      - freenode_123
      - freenode_124
      - freenode_125
      - freenode_126
      - freenode_127
      - freenode_128
      - freenode_129
      - freenode_130
      - freenode_131
      - freenode_132
      - freenode_133
      - freenode_134
      - freenode_135
      - freenode_136
      - freenode_137
      - freenode_138
      - freenode_139
      - freenode_140
      - freenode_141
      - freenode_142
      - freenode_143
      - freenode_144
      - freenode_145
      - freenode_146
      - freenode_147
      - freenode_148
      - freenode_149
      - freenode_150
      - freenode_151
      - freenode_152
      - freenode_153
      - freenode_154
  - name: Ⓜ️ 微软服务
    type: select
    proxies:
      - 🎯 全球直连
      - 🚀 节点选择
      - freenode_1
      - freenode_2
      - freenode_3
      - freenode_4
      - freenode_5
      - freenode_6
      - freenode_7
      - freenode_8
      - freenode_9
      - freenode_10
      - freenode_11
      - freenode_12
      - freenode_13
      - freenode_14
      - freenode_15
      - freenode_16
      - freenode_17
      - freenode_18
      - freenode_19
      - freenode_20
      - freenode_21
      - freenode_22
      - freenode_23
      - freenode_24
      - freenode_25
      - freenode_26
      - freenode_27
      - freenode_28
      - freenode_29
      - freenode_30
      - freenode_31
      - freenode_32
      - freenode_33
      - freenode_34
      - freenode_35
      - freenode_36
      - freenode_37
      - freenode_38
      - freenode_39
      - freenode_40
      - freenode_41
      - freenode_42
      - freenode_43
      - freenode_44
      - freenode_45
      - freenode_46
      - freenode_47
      - freenode_48
      - freenode_49
      - freenode_50
      - freenode_51
      - freenode_52
      - freenode_53
      - freenode_54
      - freenode_55
      - freenode_56
      - freenode_57
      - freenode_58
      - freenode_59
      - freenode_60
      - freenode_61
      - freenode_62
      - freenode_63
      - freenode_64
      - freenode_65
      - freenode_66
      - freenode_67
      - freenode_68
      - freenode_69
      - freenode_70
      - freenode_71
      - freenode_72
      - freenode_73
      - freenode_74
      - freenode_75
      - freenode_76
      - freenode_77
      - freenode_78
      - freenode_79
      - freenode_80
      - freenode_81
      - freenode_82
      - freenode_83
      - freenode_84
      - freenode_85
      - freenode_86
      - freenode_87
      - freenode_88
      - freenode_89
      - freenode_90
      - freenode_91
      - freenode_92
      - freenode_93
      - freenode_94
      - freenode_95
      - freenode_96
      - freenode_97
      - freenode_98
      - freenode_99
      - freenode_100
      - freenode_101
      - freenode_102
      - freenode_103
      - freenode_104
      - freenode_105
      - freenode_106
      - freenode_107
      - freenode_108
      - freenode_109
      - freenode_110
      - freenode_111
      - freenode_112
      - freenode_113
      - freenode_114
      - freenode_115
      - freenode_116
      - freenode_117
      - freenode_118
      - freenode_119
      - freenode_120
      - freenode_121
      - freenode_122
      - freenode_123
      - freenode_124
      - freenode_125
      - freenode_126
      - freenode_127
      - freenode_128
      - freenode_129
      - freenode_130
      - freenode_131
      - freenode_132
      - freenode_133
      - freenode_134
      - freenode_135
      - freenode_136
      - freenode_137
      - freenode_138
      - freenode_139
      - freenode_140
      - freenode_141
      - freenode_142
      - freenode_143
      - freenode_144
      - freenode_145
      - freenode_146
      - freenode_147
      - freenode_148
      - freenode_149
      - freenode_150
      - freenode_151
      - freenode_152
      - freenode_153
      - freenode_154
  - name: 🍎 苹果服务
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - freenode_1
      - freenode_2
      - freenode_3
      - freenode_4
      - freenode_5
      - freenode_6
      - freenode_7
      - freenode_8
      - freenode_9
      - freenode_10
      - freenode_11
      - freenode_12
      - freenode_13
      - freenode_14
      - freenode_15
      - freenode_16
      - freenode_17
      - freenode_18
      - freenode_19
      - freenode_20
      - freenode_21
      - freenode_22
      - freenode_23
      - freenode_24
      - freenode_25
      - freenode_26
      - freenode_27
      - freenode_28
      - freenode_29
      - freenode_30
      - freenode_31
      - freenode_32
      - freenode_33
      - freenode_34
      - freenode_35
      - freenode_36
      - freenode_37
      - freenode_38
      - freenode_39
      - freenode_40
      - freenode_41
      - freenode_42
      - freenode_43
      - freenode_44
      - freenode_45
      - freenode_46
      - freenode_47
      - freenode_48
      - freenode_49
      - freenode_50
      - freenode_51
      - freenode_52
      - freenode_53
      - freenode_54
      - freenode_55
      - freenode_56
      - freenode_57
      - freenode_58
      - freenode_59
      - freenode_60
      - freenode_61
      - freenode_62
      - freenode_63
      - freenode_64
      - freenode_65
      - freenode_66
      - freenode_67
      - freenode_68
      - freenode_69
      - freenode_70
      - freenode_71
      - freenode_72
      - freenode_73
      - freenode_74
      - freenode_75
      - freenode_76
      - freenode_77
      - freenode_78
      - freenode_79
      - freenode_80
      - freenode_81
      - freenode_82
      - freenode_83
      - freenode_84
      - freenode_85
      - freenode_86
      - freenode_87
      - freenode_88
      - freenode_89
      - freenode_90
      - freenode_91
      - freenode_92
      - freenode_93
      - freenode_94
      - freenode_95
      - freenode_96
      - freenode_97
      - freenode_98
      - freenode_99
      - freenode_100
      - freenode_101
      - freenode_102
      - freenode_103
      - freenode_104
      - freenode_105
      - freenode_106
      - freenode_107
      - freenode_108
      - freenode_109
      - freenode_110
      - freenode_111
      - freenode_112
      - freenode_113
      - freenode_114
      - freenode_115
      - freenode_116
      - freenode_117
      - freenode_118
      - freenode_119
      - freenode_120
      - freenode_121
      - freenode_122
      - freenode_123
      - freenode_124
      - freenode_125
      - freenode_126
      - freenode_127
      - freenode_128
      - freenode_129
      - freenode_130
      - freenode_131
      - freenode_132
      - freenode_133
      - freenode_134
      - freenode_135
      - freenode_136
      - freenode_137
      - freenode_138
      - freenode_139
      - freenode_140
      - freenode_141
      - freenode_142
      - freenode_143
      - freenode_144
      - freenode_145
      - freenode_146
      - freenode_147
      - freenode_148
      - freenode_149
      - freenode_150
      - freenode_151
      - freenode_152
      - freenode_153
      - freenode_154
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
      - freenode_1
      - freenode_2
      - freenode_3
      - freenode_4
      - freenode_5
      - freenode_6
      - freenode_7
      - freenode_8
      - freenode_9
      - freenode_10
      - freenode_11
      - freenode_12
      - freenode_13
      - freenode_14
      - freenode_15
      - freenode_16
      - freenode_17
      - freenode_18
      - freenode_19
      - freenode_20
      - freenode_21
      - freenode_22
      - freenode_23
      - freenode_24
      - freenode_25
      - freenode_26
      - freenode_27
      - freenode_28
      - freenode_29
      - freenode_30
      - freenode_31
      - freenode_32
      - freenode_33
      - freenode_34
      - freenode_35
      - freenode_36
      - freenode_37
      - freenode_38
      - freenode_39
      - freenode_40
      - freenode_41
      - freenode_42
      - freenode_43
      - freenode_44
      - freenode_45
      - freenode_46
      - freenode_47
      - freenode_48
      - freenode_49
      - freenode_50
      - freenode_51
      - freenode_52
      - freenode_53
      - freenode_54
      - freenode_55
      - freenode_56
      - freenode_57
      - freenode_58
      - freenode_59
      - freenode_60
      - freenode_61
      - freenode_62
      - freenode_63
      - freenode_64
      - freenode_65
      - freenode_66
      - freenode_67
      - freenode_68
      - freenode_69
      - freenode_70
      - freenode_71
      - freenode_72
      - freenode_73
      - freenode_74
      - freenode_75
      - freenode_76
      - freenode_77
      - freenode_78
      - freenode_79
      - freenode_80
      - freenode_81
      - freenode_82
      - freenode_83
      - freenode_84
      - freenode_85
      - freenode_86
      - freenode_87
      - freenode_88
      - freenode_89
      - freenode_90
      - freenode_91
      - freenode_92
      - freenode_93
      - freenode_94
      - freenode_95
      - freenode_96
      - freenode_97
      - freenode_98
      - freenode_99
      - freenode_100
      - freenode_101
      - freenode_102
      - freenode_103
      - freenode_104
      - freenode_105
      - freenode_106
      - freenode_107
      - freenode_108
      - freenode_109
      - freenode_110
      - freenode_111
      - freenode_112
      - freenode_113
      - freenode_114
      - freenode_115
      - freenode_116
      - freenode_117
      - freenode_118
      - freenode_119
      - freenode_120
      - freenode_121
      - freenode_122
      - freenode_123
      - freenode_124
      - freenode_125
      - freenode_126
      - freenode_127
      - freenode_128
      - freenode_129
      - freenode_130
      - freenode_131
      - freenode_132
      - freenode_133
      - freenode_134
      - freenode_135
      - freenode_136
      - freenode_137
      - freenode_138
      - freenode_139
      - freenode_140
      - freenode_141
      - freenode_142
      - freenode_143
      - freenode_144
      - freenode_145
      - freenode_146
      - freenode_147
      - freenode_148
      - freenode_149
      - freenode_150
      - freenode_151
      - freenode_152
      - freenode_153
      - freenode_154

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
  - {"name":"freenode2_1","type":"vless","server":"104.21.2.65","port":2053,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_2","type":"vless","server":"104.21.2.194","port":2096,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_3","type":"vless","server":"dytyna.pp.ua","port":2083,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_4","type":"vless","server":"104.21.5.24","port":2087,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_5","type":"vless","server":"104.19.174.72","port":443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_6","type":"vless","server":"104.21.2.139","port":2087,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_7","type":"vless","server":"104.21.0.224","port":2083,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_8","type":"vless","server":"gb1.vlessx.xyz","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_9","type":"vless","server":"104.21.5.238","port":443,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_10","type":"vless","server":"104.21.4.245","port":2053,"uuid":"d342d11e-d424-4583-b36e-524ab1f0afa4","tls":true,"servername":"edgood.king361.cf","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"edgood.king361.cf"}}}
  - {"name":"freenode2_11","type":"vless","server":"104.16.96.55","port":2087,"uuid":"ffffffff-17ad-45e7-aaa1-f2baaa08e930","tls":true,"servername":"watashi.free.jppublic.moh539.link","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"watashi.free.jppublic.moh539.link"}}}
  - {"name":"freenode2_12","type":"vless","server":"104.21.12.37","port":8443,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_13","type":"vless","server":"104.21.15.147","port":2096,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_14","type":"vless","server":"jp11.vlessx.xyz","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_15","type":"vless","server":"104.21.15.241","port":443,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_16","type":"vless","server":"104.21.2.250","port":2087,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_17","type":"vless","server":"198.41.221.213","port":2087,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode2_18","type":"vless","server":"104.21.2.119","port":2083,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_19","type":"vless","server":"104.21.28.133","port":8443,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode2_20","type":"vless","server":"104.21.5.103","port":2096,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_21","type":"vless","server":"104.21.30.245","port":2083,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode2_22","type":"vless","server":"198.41.208.160","port":8443,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode2_23","type":"vless","server":"de5.vlessx.xyz","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_24","type":"vless","server":"nl54.vlessx.us","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_25","type":"vless","server":"104.21.12.54","port":2083,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_26","type":"vless","server":"www.ipget.net","port":2087,"uuid":"a13df940-020c-465f-bc89-ee5279b5cd6a","tls":true,"servername":"ss2.wang66.homes","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ss2.wang66.homes"}}}
  - {"name":"freenode2_27","type":"vless","server":"172.64.89.170","port":443,"uuid":"b9ad895b-12ac-40fc-a5ac-a5b2a1285001","tls":true,"servername":"3k.pureboy.eu.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.pureboy.eu.org"}}}
  - {"name":"freenode2_28","type":"vless","server":"104.21.4.130","port":2087,"uuid":"d342d11e-d424-4583-b36e-524ab1f0afa4","tls":true,"servername":"edgood.king361.cf","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"edgood.king361.cf"}}}
  - {"name":"freenode2_29","type":"vless","server":"104.21.0.199","port":2053,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_30","type":"vless","server":"ipv6.yuhe9555proton.pp.ua","port":2087,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_31","type":"vless","server":"104.21.4.179","port":2087,"uuid":"d342d11e-d424-4583-b36e-524ab1f0afa4","tls":true,"servername":"edgood.king361.cf","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"edgood.king361.cf"}}}
  - {"name":"freenode2_32","type":"vless","server":"smi.pp.ua","port":2096,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_33","type":"vless","server":"104.21.5.70","port":443,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_34","type":"vless","server":"104.21.5.236","port":8443,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_35","type":"vless","server":"104.21.1.57","port":2087,"uuid":"ffffffff-17ad-45e7-aaa1-f2baaa08e930","tls":true,"servername":"watashi.free.jppublic.moh539.link","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"watashi.free.jppublic.moh539.link"}}}
  - {"name":"freenode2_36","type":"vless","server":"www.butech.pp.ua","port":2087,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_37","type":"vless","server":"104.21.15.177","port":8443,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_38","type":"vless","server":"104.21.15.36","port":8443,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_39","type":"vless","server":"104.21.5.200","port":2083,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_40","type":"vless","server":"104.21.4.164","port":2083,"uuid":"d342d11e-d424-4583-b36e-524ab1f0afa4","tls":true,"servername":"edgood.king361.cf","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"edgood.king361.cf"}}}
  - {"name":"freenode2_41","type":"vless","server":"104.21.4.248","port":2087,"uuid":"d342d11e-d424-4583-b36e-524ab1f0afa4","tls":true,"servername":"edgood.king361.cf","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"edgood.king361.cf"}}}
  - {"name":"freenode2_42","type":"vless","server":"104.21.2.189","port":2087,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_43","type":"vless","server":"104.21.30.234","port":8443,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode2_44","type":"vless","server":"104.21.2.83","port":2087,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_45","type":"vless","server":"104.21.5.253","port":2083,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_46","type":"vless","server":"nl46.vlessx.us","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_47","type":"vless","server":"104.21.15.241","port":2087,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_48","type":"vless","server":"104.21.4.134","port":2053,"uuid":"d342d11e-d424-4583-b36e-524ab1f0afa4","tls":true,"servername":"edgood.king361.cf","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"edgood.king361.cf"}}}
  - {"name":"freenode2_49","type":"vless","server":"104.21.0.48","port":2053,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_50","type":"vless","server":"104.21.5.154","port":8443,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_51","type":"vless","server":"104.21.26.237","port":2083,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode2_52","type":"vless","server":"104.21.24.70","port":2096,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode2_53","type":"vless","server":"104.21.28.9","port":2053,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode2_54","type":"vless","server":"104.21.2.60","port":443,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_55","type":"vless","server":"104.21.0.248","port":2096,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_56","type":"vless","server":"104.21.5.66","port":2096,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_57","type":"vless","server":"104.16.32.40","port":443,"uuid":"d342d11e-d424-4583-b36e-524ab1f0afa4","tls":true,"servername":"baipiao406.stunning-bassoon.pages.dev","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"baipiao406.stunning-bassoon.pages.dev"}}}
  - {"name":"freenode2_58","type":"vless","server":"104.21.0.222","port":443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_59","type":"vless","server":"198.41.208.243","port":8443,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode2_60","type":"vless","server":"104.21.2.242","port":2087,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_61","type":"vless","server":"104.21.24.40","port":443,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode2_62","type":"vless","server":"kr2.vlessx.xyz","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_63","type":"vless","server":"104.21.2.155","port":2083,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_64","type":"vless","server":"104.21.59.125","port":443,"uuid":"b9ad895b-12ac-40fc-a5ac-a5b2a1285001","tls":true,"servername":"3k.pureboy.eu.org","network":"ws","ws-opts":{"path":"shabi","headers":{"host":"3k.pureboy.eu.org"}}}
  - {"name":"freenode2_65","type":"vless","server":"104.21.43.16","port":443,"uuid":"b9ad895b-12ac-40fc-a5ac-a5b2a1285001","tls":true,"servername":"3k.pureboy.eu.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.pureboy.eu.org"}}}
  - {"name":"freenode2_66","type":"vless","server":"ipv6.yuhe9555proton.pp.ua","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_67","type":"vless","server":"104.21.2.1","port":2083,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_68","type":"vless","server":"104.16.97.212","port":2083,"uuid":"ffffffff-17ad-45e7-aaa1-f2baaa08e930","tls":true,"servername":"watashi.free.jppublic.moh539.link","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"watashi.free.jppublic.moh539.link"}}}
  - {"name":"freenode2_69","type":"vless","server":"104.21.2.74","port":8443,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_70","type":"vless","server":"104.21.5.78","port":2083,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_71","type":"vless","server":"104.21.2.159","port":8443,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_72","type":"vless","server":"104.21.5.109","port":2053,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_73","type":"vless","server":"198.41.209.254","port":443,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode2_74","type":"vless","server":"www.microfix.pp.ua","port":2083,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_75","type":"vless","server":"104.21.17.178","port":2083,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_76","type":"vless","server":"104.21.2.115","port":443,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_77","type":"vless","server":"104.21.5.209","port":2053,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
proxy-groups:
  - name: 🚀 节点选择
    type: select
    proxies:
      - ♻️ 自动选择
      - DIRECT
      - freenode2_1
      - freenode2_2
      - freenode2_3
      - freenode2_4
      - freenode2_5
      - freenode2_6
      - freenode2_7
      - freenode2_8
      - freenode2_9
      - freenode2_10
      - freenode2_11
      - freenode2_12
      - freenode2_13
      - freenode2_14
      - freenode2_15
      - freenode2_16
      - freenode2_17
      - freenode2_18
      - freenode2_19
      - freenode2_20
      - freenode2_21
      - freenode2_22
      - freenode2_23
      - freenode2_24
      - freenode2_25
      - freenode2_26
      - freenode2_27
      - freenode2_28
      - freenode2_29
      - freenode2_30
      - freenode2_31
      - freenode2_32
      - freenode2_33
      - freenode2_34
      - freenode2_35
      - freenode2_36
      - freenode2_37
      - freenode2_38
      - freenode2_39
      - freenode2_40
      - freenode2_41
      - freenode2_42
      - freenode2_43
      - freenode2_44
      - freenode2_45
      - freenode2_46
      - freenode2_47
      - freenode2_48
      - freenode2_49
      - freenode2_50
      - freenode2_51
      - freenode2_52
      - freenode2_53
      - freenode2_54
      - freenode2_55
      - freenode2_56
      - freenode2_57
      - freenode2_58
      - freenode2_59
      - freenode2_60
      - freenode2_61
      - freenode2_62
      - freenode2_63
      - freenode2_64
      - freenode2_65
      - freenode2_66
      - freenode2_67
      - freenode2_68
      - freenode2_69
      - freenode2_70
      - freenode2_71
      - freenode2_72
      - freenode2_73
      - freenode2_74
      - freenode2_75
      - freenode2_76
      - freenode2_77
  - name: ♻️ 自动选择
    type: url-test
    url: https://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    proxies:
      - freenode2_1
      - freenode2_2
      - freenode2_3
      - freenode2_4
      - freenode2_5
      - freenode2_6
      - freenode2_7
      - freenode2_8
      - freenode2_9
      - freenode2_10
      - freenode2_11
      - freenode2_12
      - freenode2_13
      - freenode2_14
      - freenode2_15
      - freenode2_16
      - freenode2_17
      - freenode2_18
      - freenode2_19
      - freenode2_20
      - freenode2_21
      - freenode2_22
      - freenode2_23
      - freenode2_24
      - freenode2_25
      - freenode2_26
      - freenode2_27
      - freenode2_28
      - freenode2_29
      - freenode2_30
      - freenode2_31
      - freenode2_32
      - freenode2_33
      - freenode2_34
      - freenode2_35
      - freenode2_36
      - freenode2_37
      - freenode2_38
      - freenode2_39
      - freenode2_40
      - freenode2_41
      - freenode2_42
      - freenode2_43
      - freenode2_44
      - freenode2_45
      - freenode2_46
      - freenode2_47
      - freenode2_48
      - freenode2_49
      - freenode2_50
      - freenode2_51
      - freenode2_52
      - freenode2_53
      - freenode2_54
      - freenode2_55
      - freenode2_56
      - freenode2_57
      - freenode2_58
      - freenode2_59
      - freenode2_60
      - freenode2_61
      - freenode2_62
      - freenode2_63
      - freenode2_64
      - freenode2_65
      - freenode2_66
      - freenode2_67
      - freenode2_68
      - freenode2_69
      - freenode2_70
      - freenode2_71
      - freenode2_72
      - freenode2_73
      - freenode2_74
      - freenode2_75
      - freenode2_76
      - freenode2_77
  - name: 🌍 国外媒体
    type: select
    proxies:
      - 🚀 节点选择
      - ♻️ 自动选择
      - 🎯 全球直连
      - freenode2_1
      - freenode2_2
      - freenode2_3
      - freenode2_4
      - freenode2_5
      - freenode2_6
      - freenode2_7
      - freenode2_8
      - freenode2_9
      - freenode2_10
      - freenode2_11
      - freenode2_12
      - freenode2_13
      - freenode2_14
      - freenode2_15
      - freenode2_16
      - freenode2_17
      - freenode2_18
      - freenode2_19
      - freenode2_20
      - freenode2_21
      - freenode2_22
      - freenode2_23
      - freenode2_24
      - freenode2_25
      - freenode2_26
      - freenode2_27
      - freenode2_28
      - freenode2_29
      - freenode2_30
      - freenode2_31
      - freenode2_32
      - freenode2_33
      - freenode2_34
      - freenode2_35
      - freenode2_36
      - freenode2_37
      - freenode2_38
      - freenode2_39
      - freenode2_40
      - freenode2_41
      - freenode2_42
      - freenode2_43
      - freenode2_44
      - freenode2_45
      - freenode2_46
      - freenode2_47
      - freenode2_48
      - freenode2_49
      - freenode2_50
      - freenode2_51
      - freenode2_52
      - freenode2_53
      - freenode2_54
      - freenode2_55
      - freenode2_56
      - freenode2_57
      - freenode2_58
      - freenode2_59
      - freenode2_60
      - freenode2_61
      - freenode2_62
      - freenode2_63
      - freenode2_64
      - freenode2_65
      - freenode2_66
      - freenode2_67
      - freenode2_68
      - freenode2_69
      - freenode2_70
      - freenode2_71
      - freenode2_72
      - freenode2_73
      - freenode2_74
      - freenode2_75
      - freenode2_76
      - freenode2_77
  - name: 📲 电报信息
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - freenode2_1
      - freenode2_2
      - freenode2_3
      - freenode2_4
      - freenode2_5
      - freenode2_6
      - freenode2_7
      - freenode2_8
      - freenode2_9
      - freenode2_10
      - freenode2_11
      - freenode2_12
      - freenode2_13
      - freenode2_14
      - freenode2_15
      - freenode2_16
      - freenode2_17
      - freenode2_18
      - freenode2_19
      - freenode2_20
      - freenode2_21
      - freenode2_22
      - freenode2_23
      - freenode2_24
      - freenode2_25
      - freenode2_26
      - freenode2_27
      - freenode2_28
      - freenode2_29
      - freenode2_30
      - freenode2_31
      - freenode2_32
      - freenode2_33
      - freenode2_34
      - freenode2_35
      - freenode2_36
      - freenode2_37
      - freenode2_38
      - freenode2_39
      - freenode2_40
      - freenode2_41
      - freenode2_42
      - freenode2_43
      - freenode2_44
      - freenode2_45
      - freenode2_46
      - freenode2_47
      - freenode2_48
      - freenode2_49
      - freenode2_50
      - freenode2_51
      - freenode2_52
      - freenode2_53
      - freenode2_54
      - freenode2_55
      - freenode2_56
      - freenode2_57
      - freenode2_58
      - freenode2_59
      - freenode2_60
      - freenode2_61
      - freenode2_62
      - freenode2_63
      - freenode2_64
      - freenode2_65
      - freenode2_66
      - freenode2_67
      - freenode2_68
      - freenode2_69
      - freenode2_70
      - freenode2_71
      - freenode2_72
      - freenode2_73
      - freenode2_74
      - freenode2_75
      - freenode2_76
      - freenode2_77
  - name: Ⓜ️ 微软服务
    type: select
    proxies:
      - 🎯 全球直连
      - 🚀 节点选择
      - freenode2_1
      - freenode2_2
      - freenode2_3
      - freenode2_4
      - freenode2_5
      - freenode2_6
      - freenode2_7
      - freenode2_8
      - freenode2_9
      - freenode2_10
      - freenode2_11
      - freenode2_12
      - freenode2_13
      - freenode2_14
      - freenode2_15
      - freenode2_16
      - freenode2_17
      - freenode2_18
      - freenode2_19
      - freenode2_20
      - freenode2_21
      - freenode2_22
      - freenode2_23
      - freenode2_24
      - freenode2_25
      - freenode2_26
      - freenode2_27
      - freenode2_28
      - freenode2_29
      - freenode2_30
      - freenode2_31
      - freenode2_32
      - freenode2_33
      - freenode2_34
      - freenode2_35
      - freenode2_36
      - freenode2_37
      - freenode2_38
      - freenode2_39
      - freenode2_40
      - freenode2_41
      - freenode2_42
      - freenode2_43
      - freenode2_44
      - freenode2_45
      - freenode2_46
      - freenode2_47
      - freenode2_48
      - freenode2_49
      - freenode2_50
      - freenode2_51
      - freenode2_52
      - freenode2_53
      - freenode2_54
      - freenode2_55
      - freenode2_56
      - freenode2_57
      - freenode2_58
      - freenode2_59
      - freenode2_60
      - freenode2_61
      - freenode2_62
      - freenode2_63
      - freenode2_64
      - freenode2_65
      - freenode2_66
      - freenode2_67
      - freenode2_68
      - freenode2_69
      - freenode2_70
      - freenode2_71
      - freenode2_72
      - freenode2_73
      - freenode2_74
      - freenode2_75
      - freenode2_76
      - freenode2_77
  - name: 🍎 苹果服务
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - freenode2_1
      - freenode2_2
      - freenode2_3
      - freenode2_4
      - freenode2_5
      - freenode2_6
      - freenode2_7
      - freenode2_8
      - freenode2_9
      - freenode2_10
      - freenode2_11
      - freenode2_12
      - freenode2_13
      - freenode2_14
      - freenode2_15
      - freenode2_16
      - freenode2_17
      - freenode2_18
      - freenode2_19
      - freenode2_20
      - freenode2_21
      - freenode2_22
      - freenode2_23
      - freenode2_24
      - freenode2_25
      - freenode2_26
      - freenode2_27
      - freenode2_28
      - freenode2_29
      - freenode2_30
      - freenode2_31
      - freenode2_32
      - freenode2_33
      - freenode2_34
      - freenode2_35
      - freenode2_36
      - freenode2_37
      - freenode2_38
      - freenode2_39
      - freenode2_40
      - freenode2_41
      - freenode2_42
      - freenode2_43
      - freenode2_44
      - freenode2_45
      - freenode2_46
      - freenode2_47
      - freenode2_48
      - freenode2_49
      - freenode2_50
      - freenode2_51
      - freenode2_52
      - freenode2_53
      - freenode2_54
      - freenode2_55
      - freenode2_56
      - freenode2_57
      - freenode2_58
      - freenode2_59
      - freenode2_60
      - freenode2_61
      - freenode2_62
      - freenode2_63
      - freenode2_64
      - freenode2_65
      - freenode2_66
      - freenode2_67
      - freenode2_68
      - freenode2_69
      - freenode2_70
      - freenode2_71
      - freenode2_72
      - freenode2_73
      - freenode2_74
      - freenode2_75
      - freenode2_76
      - freenode2_77
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
      - freenode2_1
      - freenode2_2
      - freenode2_3
      - freenode2_4
      - freenode2_5
      - freenode2_6
      - freenode2_7
      - freenode2_8
      - freenode2_9
      - freenode2_10
      - freenode2_11
      - freenode2_12
      - freenode2_13
      - freenode2_14
      - freenode2_15
      - freenode2_16
      - freenode2_17
      - freenode2_18
      - freenode2_19
      - freenode2_20
      - freenode2_21
      - freenode2_22
      - freenode2_23
      - freenode2_24
      - freenode2_25
      - freenode2_26
      - freenode2_27
      - freenode2_28
      - freenode2_29
      - freenode2_30
      - freenode2_31
      - freenode2_32
      - freenode2_33
      - freenode2_34
      - freenode2_35
      - freenode2_36
      - freenode2_37
      - freenode2_38
      - freenode2_39
      - freenode2_40
      - freenode2_41
      - freenode2_42
      - freenode2_43
      - freenode2_44
      - freenode2_45
      - freenode2_46
      - freenode2_47
      - freenode2_48
      - freenode2_49
      - freenode2_50
      - freenode2_51
      - freenode2_52
      - freenode2_53
      - freenode2_54
      - freenode2_55
      - freenode2_56
      - freenode2_57
      - freenode2_58
      - freenode2_59
      - freenode2_60
      - freenode2_61
      - freenode2_62
      - freenode2_63
      - freenode2_64
      - freenode2_65
      - freenode2_66
      - freenode2_67
      - freenode2_68
      - freenode2_69
      - freenode2_70
      - freenode2_71
      - freenode2_72
      - freenode2_73
      - freenode2_74
      - freenode2_75
      - freenode2_76
      - freenode2_77

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
  - {"name":"dongtaiwang.com_1","type":"vmess","server":"www.darkroom.lol","port":8080,"cipher":"auto","uuid":"22826b44-5c1a-4b4b-dbaa-83a2e8bd95f0","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"","network":"ws","ws-opts":{"path":"/","headers":{"host":"www.darkroom.lol"}}}
  - {"name":"dongtaiwang.com_2","type":"vmess","server":"data-us-v1.shwjfkw.cn","port":20401,"cipher":"auto","uuid":"b1478e24-4916-3abe-8f17-15931012ecbe","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"","network":"ws","ws-opts":{"path":"/debian","headers":{"host":"data-us-v1.shwjfkw.cn"}}}
  - {"name":"dongtaiwang.com_3","type":"ss","server":"service.ouluyun9803.com","port":20003,"password":"d6105bbd-be0d-45b2-82ad-31fd1071c1d2","cipher":"chacha20-ietf-poly1305"}
  - {"name":"dongtaiwang.com_4","type":"vmess","server":"104.21.82.183","port":8880,"cipher":"auto","uuid":"5a7021e0-26b4-45d6-b175-fe551601ca97","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"","network":"ws","ws-opts":{"path":"/","headers":{"host":"server26.beheshtbaneh.com"}}}
  - {"name":"dongtaiwang.com_5","type":"ss","server":"service.ouluyun9803.com","port":20005,"password":"d6105bbd-be0d-45b2-82ad-31fd1071c1d2","cipher":"chacha20-ietf-poly1305"}
  - {"name":"dongtaiwang.com_6","type":"ss","server":"109.104.152.161","port":12345,"password":"dongtaiwang.com","cipher":"chacha20-ietf-poly1305"}
  - {"name":"dongtaiwang.com_7","type":"ss","server":"109.104.152.33","port":12345,"password":"dongtaiwang.com","cipher":"chacha20-ietf-poly1305"}
  - {"name":"dongtaiwang.com_8","type":"ss","server":"64.31.55.124","port":12345,"password":"dongtaiwang.com","cipher":"chacha20-ietf-poly1305"}
  - {"name":"dongtaiwang.com_9","type":"ss","server":"111.243.98.243","port":12345,"password":"dongtaiwang.com","cipher":"chacha20-ietf-poly1305"}
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
  - {"name":"dongtaiwang.com_0","type":"vmess","server":"167.82.19.72","port":80,"cipher":"auto","uuid":"eff57453-31bc-4b6a-968a-17687dacc13f","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"","network":"ws","ws-opts":{"path":"/z4l0eJX1/","headers":{"host":"freedom1.com"}}}
  - {"name":"dongtaiwang.com_1","type":"vmess","server":"146.75.116.107","port":80,"cipher":"auto","uuid":"eff57453-31bc-4b6a-968a-17687dacc13f","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"","network":"ws","ws-opts":{"path":"/z4l0eJX1/","headers":{"host":"freedom1.com"}}}
proxy-groups:
  - name: 🚀 节点选择
    type: select
    proxies:
      - ♻️ 自动选择
      - DIRECT
      - dongtaiwang.com_0
      - dongtaiwang.com_1
  - name: ♻️ 自动选择
    type: url-test
    url: https://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    proxies:
      - dongtaiwang.com_0
      - dongtaiwang.com_1
  - name: 🌍 国外媒体
    type: select
    proxies:
      - 🚀 节点选择
      - ♻️ 自动选择
      - 🎯 全球直连
      - dongtaiwang.com_0
      - dongtaiwang.com_1
  - name: 📲 电报信息
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - dongtaiwang.com_0
      - dongtaiwang.com_1
  - name: Ⓜ️ 微软服务
    type: select
    proxies:
      - 🎯 全球直连
      - 🚀 节点选择
      - dongtaiwang.com_0
      - dongtaiwang.com_1
  - name: 🍎 苹果服务
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - dongtaiwang.com_0
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
      - dongtaiwang.com_0
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
  - {"name":"dongtaiwang.com_1","type":"vmess","server":"www.darkroom.lol","port":8080,"cipher":"auto","uuid":"22826b44-5c1a-4b4b-dbaa-83a2e8bd95f0","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"","network":"ws","ws-opts":{"path":"/","headers":{"host":"www.darkroom.lol"}}}
  - {"name":"dongtaiwang.com_2","type":"vmess","server":"data-us-v1.shwjfkw.cn","port":20401,"cipher":"auto","uuid":"b1478e24-4916-3abe-8f17-15931012ecbe","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"","network":"ws","ws-opts":{"path":"/debian","headers":{"host":"data-us-v1.shwjfkw.cn"}}}
  - {"name":"dongtaiwang.com_3","type":"ss","server":"service.ouluyun9803.com","port":20003,"password":"d6105bbd-be0d-45b2-82ad-31fd1071c1d2","cipher":"chacha20-ietf-poly1305"}
  - {"name":"dongtaiwang.com_4","type":"vmess","server":"104.21.82.183","port":8880,"cipher":"auto","uuid":"5a7021e0-26b4-45d6-b175-fe551601ca97","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"","network":"ws","ws-opts":{"path":"/","headers":{"host":"server26.beheshtbaneh.com"}}}
  - {"name":"dongtaiwang.com_5","type":"ss","server":"service.ouluyun9803.com","port":20005,"password":"d6105bbd-be0d-45b2-82ad-31fd1071c1d2","cipher":"chacha20-ietf-poly1305"}
  - {"name":"dongtaiwang.com_6","type":"ss","server":"109.104.152.161","port":12345,"password":"dongtaiwang.com","cipher":"chacha20-ietf-poly1305"}
  - {"name":"dongtaiwang.com_7","type":"ss","server":"109.104.152.33","port":12345,"password":"dongtaiwang.com","cipher":"chacha20-ietf-poly1305"}
  - {"name":"dongtaiwang.com_8","type":"ss","server":"64.31.55.124","port":12345,"password":"dongtaiwang.com","cipher":"chacha20-ietf-poly1305"}
  - {"name":"dongtaiwang.com_9","type":"ss","server":"111.243.98.243","port":12345,"password":"dongtaiwang.com","cipher":"chacha20-ietf-poly1305"}
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
  - {"name":"freenode2_1","type":"vless","server":"104.21.2.65","port":2053,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_2","type":"vless","server":"104.21.2.194","port":2096,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_3","type":"vless","server":"dytyna.pp.ua","port":2083,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_4","type":"vless","server":"104.21.5.24","port":2087,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_5","type":"vless","server":"104.19.174.72","port":443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_6","type":"vless","server":"104.21.2.139","port":2087,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_7","type":"vless","server":"104.21.0.224","port":2083,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_8","type":"vless","server":"gb1.vlessx.xyz","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_9","type":"vless","server":"104.21.5.238","port":443,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_10","type":"vless","server":"104.21.4.245","port":2053,"uuid":"d342d11e-d424-4583-b36e-524ab1f0afa4","tls":true,"servername":"edgood.king361.cf","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"edgood.king361.cf"}}}
  - {"name":"freenode2_11","type":"vless","server":"104.16.96.55","port":2087,"uuid":"ffffffff-17ad-45e7-aaa1-f2baaa08e930","tls":true,"servername":"watashi.free.jppublic.moh539.link","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"watashi.free.jppublic.moh539.link"}}}
  - {"name":"freenode2_12","type":"vless","server":"104.21.12.37","port":8443,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_13","type":"vless","server":"104.21.15.147","port":2096,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_14","type":"vless","server":"jp11.vlessx.xyz","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_15","type":"vless","server":"104.21.15.241","port":443,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_16","type":"vless","server":"104.21.2.250","port":2087,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_17","type":"vless","server":"198.41.221.213","port":2087,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode2_18","type":"vless","server":"104.21.2.119","port":2083,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_19","type":"vless","server":"104.21.28.133","port":8443,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode2_20","type":"vless","server":"104.21.5.103","port":2096,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_21","type":"vless","server":"104.21.30.245","port":2083,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode2_22","type":"vless","server":"198.41.208.160","port":8443,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode2_23","type":"vless","server":"de5.vlessx.xyz","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_24","type":"vless","server":"nl54.vlessx.us","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_25","type":"vless","server":"104.21.12.54","port":2083,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_26","type":"vless","server":"www.ipget.net","port":2087,"uuid":"a13df940-020c-465f-bc89-ee5279b5cd6a","tls":true,"servername":"ss2.wang66.homes","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ss2.wang66.homes"}}}
  - {"name":"freenode2_27","type":"vless","server":"172.64.89.170","port":443,"uuid":"b9ad895b-12ac-40fc-a5ac-a5b2a1285001","tls":true,"servername":"3k.pureboy.eu.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.pureboy.eu.org"}}}
  - {"name":"freenode2_28","type":"vless","server":"104.21.4.130","port":2087,"uuid":"d342d11e-d424-4583-b36e-524ab1f0afa4","tls":true,"servername":"edgood.king361.cf","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"edgood.king361.cf"}}}
  - {"name":"freenode2_29","type":"vless","server":"104.21.0.199","port":2053,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_30","type":"vless","server":"ipv6.yuhe9555proton.pp.ua","port":2087,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_31","type":"vless","server":"104.21.4.179","port":2087,"uuid":"d342d11e-d424-4583-b36e-524ab1f0afa4","tls":true,"servername":"edgood.king361.cf","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"edgood.king361.cf"}}}
  - {"name":"freenode2_32","type":"vless","server":"smi.pp.ua","port":2096,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_33","type":"vless","server":"104.21.5.70","port":443,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_34","type":"vless","server":"104.21.5.236","port":8443,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_35","type":"vless","server":"104.21.1.57","port":2087,"uuid":"ffffffff-17ad-45e7-aaa1-f2baaa08e930","tls":true,"servername":"watashi.free.jppublic.moh539.link","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"watashi.free.jppublic.moh539.link"}}}
  - {"name":"freenode2_36","type":"vless","server":"www.butech.pp.ua","port":2087,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_37","type":"vless","server":"104.21.15.177","port":8443,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_38","type":"vless","server":"104.21.15.36","port":8443,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_39","type":"vless","server":"104.21.5.200","port":2083,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_40","type":"vless","server":"104.21.4.164","port":2083,"uuid":"d342d11e-d424-4583-b36e-524ab1f0afa4","tls":true,"servername":"edgood.king361.cf","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"edgood.king361.cf"}}}
  - {"name":"freenode2_41","type":"vless","server":"104.21.4.248","port":2087,"uuid":"d342d11e-d424-4583-b36e-524ab1f0afa4","tls":true,"servername":"edgood.king361.cf","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"edgood.king361.cf"}}}
  - {"name":"freenode2_42","type":"vless","server":"104.21.2.189","port":2087,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_43","type":"vless","server":"104.21.30.234","port":8443,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode2_44","type":"vless","server":"104.21.2.83","port":2087,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_45","type":"vless","server":"104.21.5.253","port":2083,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_46","type":"vless","server":"nl46.vlessx.us","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_47","type":"vless","server":"104.21.15.241","port":2087,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_48","type":"vless","server":"104.21.4.134","port":2053,"uuid":"d342d11e-d424-4583-b36e-524ab1f0afa4","tls":true,"servername":"edgood.king361.cf","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"edgood.king361.cf"}}}
  - {"name":"freenode2_49","type":"vless","server":"104.21.0.48","port":2053,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_50","type":"vless","server":"104.21.5.154","port":8443,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_51","type":"vless","server":"104.21.26.237","port":2083,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode2_52","type":"vless","server":"104.21.24.70","port":2096,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode2_53","type":"vless","server":"104.21.28.9","port":2053,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode2_54","type":"vless","server":"104.21.2.60","port":443,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_55","type":"vless","server":"104.21.0.248","port":2096,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_56","type":"vless","server":"104.21.5.66","port":2096,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_57","type":"vless","server":"104.16.32.40","port":443,"uuid":"d342d11e-d424-4583-b36e-524ab1f0afa4","tls":true,"servername":"baipiao406.stunning-bassoon.pages.dev","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"baipiao406.stunning-bassoon.pages.dev"}}}
  - {"name":"freenode2_58","type":"vless","server":"104.21.0.222","port":443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_59","type":"vless","server":"198.41.208.243","port":8443,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode2_60","type":"vless","server":"104.21.2.242","port":2087,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_61","type":"vless","server":"104.21.24.40","port":443,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode2_62","type":"vless","server":"kr2.vlessx.xyz","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_63","type":"vless","server":"104.21.2.155","port":2083,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_64","type":"vless","server":"104.21.59.125","port":443,"uuid":"b9ad895b-12ac-40fc-a5ac-a5b2a1285001","tls":true,"servername":"3k.pureboy.eu.org","network":"ws","ws-opts":{"path":"shabi","headers":{"host":"3k.pureboy.eu.org"}}}
  - {"name":"freenode2_65","type":"vless","server":"104.21.43.16","port":443,"uuid":"b9ad895b-12ac-40fc-a5ac-a5b2a1285001","tls":true,"servername":"3k.pureboy.eu.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.pureboy.eu.org"}}}
  - {"name":"freenode2_66","type":"vless","server":"ipv6.yuhe9555proton.pp.ua","port":8443,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_67","type":"vless","server":"104.21.2.1","port":2083,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_68","type":"vless","server":"104.16.97.212","port":2083,"uuid":"ffffffff-17ad-45e7-aaa1-f2baaa08e930","tls":true,"servername":"watashi.free.jppublic.moh539.link","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"watashi.free.jppublic.moh539.link"}}}
  - {"name":"freenode2_69","type":"vless","server":"104.21.2.74","port":8443,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_70","type":"vless","server":"104.21.5.78","port":2083,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_71","type":"vless","server":"104.21.2.159","port":8443,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_72","type":"vless","server":"104.21.5.109","port":2053,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
  - {"name":"freenode2_73","type":"vless","server":"198.41.209.254","port":443,"uuid":"875e0c54-2690-4bfb-a4e5-d44bcf9d2a31","tls":true,"servername":"kyd.cloudns.org","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"kyd.cloudns.org"}}}
  - {"name":"freenode2_74","type":"vless","server":"www.microfix.pp.ua","port":2083,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_75","type":"vless","server":"104.21.17.178","port":2083,"uuid":"60813b9d-aa0e-4a5c-88b8-ed231058e82a","tls":true,"servername":"pages.20230619.love","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"pages.20230619.love"}}}
  - {"name":"freenode2_76","type":"vless","server":"104.21.2.115","port":443,"uuid":"7fd7c15d-95cd-4f5c-bf59-f21e5eb27580","tls":true,"servername":"3k.dabee.top","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"3k.dabee.top"}}}
  - {"name":"freenode2_77","type":"vless","server":"104.21.5.209","port":2053,"uuid":"73b6dbd5-a27a-4c76-9ad1-42a82380dddb","tls":true,"servername":"ed.ariesver.online","network":"ws","ws-opts":{"path":"Twitter苏小柠","headers":{"host":"ed.ariesver.online"}}}
proxy-groups:
  - name: 🚀 节点选择
    type: select
    proxies:
      - ♻️ 自动选择
      - DIRECT
      - freenode2_1
      - freenode2_2
      - freenode2_3
      - freenode2_4
      - freenode2_5
      - freenode2_6
      - freenode2_7
      - freenode2_8
      - freenode2_9
      - freenode2_10
      - freenode2_11
      - freenode2_12
      - freenode2_13
      - freenode2_14
      - freenode2_15
      - freenode2_16
      - freenode2_17
      - freenode2_18
      - freenode2_19
      - freenode2_20
      - freenode2_21
      - freenode2_22
      - freenode2_23
      - freenode2_24
      - freenode2_25
      - freenode2_26
      - freenode2_27
      - freenode2_28
      - freenode2_29
      - freenode2_30
      - freenode2_31
      - freenode2_32
      - freenode2_33
      - freenode2_34
      - freenode2_35
      - freenode2_36
      - freenode2_37
      - freenode2_38
      - freenode2_39
      - freenode2_40
      - freenode2_41
      - freenode2_42
      - freenode2_43
      - freenode2_44
      - freenode2_45
      - freenode2_46
      - freenode2_47
      - freenode2_48
      - freenode2_49
      - freenode2_50
      - freenode2_51
      - freenode2_52
      - freenode2_53
      - freenode2_54
      - freenode2_55
      - freenode2_56
      - freenode2_57
      - freenode2_58
      - freenode2_59
      - freenode2_60
      - freenode2_61
      - freenode2_62
      - freenode2_63
      - freenode2_64
      - freenode2_65
      - freenode2_66
      - freenode2_67
      - freenode2_68
      - freenode2_69
      - freenode2_70
      - freenode2_71
      - freenode2_72
      - freenode2_73
      - freenode2_74
      - freenode2_75
      - freenode2_76
      - freenode2_77
  - name: ♻️ 自动选择
    type: url-test
    url: https://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    proxies:
      - freenode2_1
      - freenode2_2
      - freenode2_3
      - freenode2_4
      - freenode2_5
      - freenode2_6
      - freenode2_7
      - freenode2_8
      - freenode2_9
      - freenode2_10
      - freenode2_11
      - freenode2_12
      - freenode2_13
      - freenode2_14
      - freenode2_15
      - freenode2_16
      - freenode2_17
      - freenode2_18
      - freenode2_19
      - freenode2_20
      - freenode2_21
      - freenode2_22
      - freenode2_23
      - freenode2_24
      - freenode2_25
      - freenode2_26
      - freenode2_27
      - freenode2_28
      - freenode2_29
      - freenode2_30
      - freenode2_31
      - freenode2_32
      - freenode2_33
      - freenode2_34
      - freenode2_35
      - freenode2_36
      - freenode2_37
      - freenode2_38
      - freenode2_39
      - freenode2_40
      - freenode2_41
      - freenode2_42
      - freenode2_43
      - freenode2_44
      - freenode2_45
      - freenode2_46
      - freenode2_47
      - freenode2_48
      - freenode2_49
      - freenode2_50
      - freenode2_51
      - freenode2_52
      - freenode2_53
      - freenode2_54
      - freenode2_55
      - freenode2_56
      - freenode2_57
      - freenode2_58
      - freenode2_59
      - freenode2_60
      - freenode2_61
      - freenode2_62
      - freenode2_63
      - freenode2_64
      - freenode2_65
      - freenode2_66
      - freenode2_67
      - freenode2_68
      - freenode2_69
      - freenode2_70
      - freenode2_71
      - freenode2_72
      - freenode2_73
      - freenode2_74
      - freenode2_75
      - freenode2_76
      - freenode2_77
  - name: 🌍 国外媒体
    type: select
    proxies:
      - 🚀 节点选择
      - ♻️ 自动选择
      - 🎯 全球直连
      - freenode2_1
      - freenode2_2
      - freenode2_3
      - freenode2_4
      - freenode2_5
      - freenode2_6
      - freenode2_7
      - freenode2_8
      - freenode2_9
      - freenode2_10
      - freenode2_11
      - freenode2_12
      - freenode2_13
      - freenode2_14
      - freenode2_15
      - freenode2_16
      - freenode2_17
      - freenode2_18
      - freenode2_19
      - freenode2_20
      - freenode2_21
      - freenode2_22
      - freenode2_23
      - freenode2_24
      - freenode2_25
      - freenode2_26
      - freenode2_27
      - freenode2_28
      - freenode2_29
      - freenode2_30
      - freenode2_31
      - freenode2_32
      - freenode2_33
      - freenode2_34
      - freenode2_35
      - freenode2_36
      - freenode2_37
      - freenode2_38
      - freenode2_39
      - freenode2_40
      - freenode2_41
      - freenode2_42
      - freenode2_43
      - freenode2_44
      - freenode2_45
      - freenode2_46
      - freenode2_47
      - freenode2_48
      - freenode2_49
      - freenode2_50
      - freenode2_51
      - freenode2_52
      - freenode2_53
      - freenode2_54
      - freenode2_55
      - freenode2_56
      - freenode2_57
      - freenode2_58
      - freenode2_59
      - freenode2_60
      - freenode2_61
      - freenode2_62
      - freenode2_63
      - freenode2_64
      - freenode2_65
      - freenode2_66
      - freenode2_67
      - freenode2_68
      - freenode2_69
      - freenode2_70
      - freenode2_71
      - freenode2_72
      - freenode2_73
      - freenode2_74
      - freenode2_75
      - freenode2_76
      - freenode2_77
  - name: 📲 电报信息
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - freenode2_1
      - freenode2_2
      - freenode2_3
      - freenode2_4
      - freenode2_5
      - freenode2_6
      - freenode2_7
      - freenode2_8
      - freenode2_9
      - freenode2_10
      - freenode2_11
      - freenode2_12
      - freenode2_13
      - freenode2_14
      - freenode2_15
      - freenode2_16
      - freenode2_17
      - freenode2_18
      - freenode2_19
      - freenode2_20
      - freenode2_21
      - freenode2_22
      - freenode2_23
      - freenode2_24
      - freenode2_25
      - freenode2_26
      - freenode2_27
      - freenode2_28
      - freenode2_29
      - freenode2_30
      - freenode2_31
      - freenode2_32
      - freenode2_33
      - freenode2_34
      - freenode2_35
      - freenode2_36
      - freenode2_37
      - freenode2_38
      - freenode2_39
      - freenode2_40
      - freenode2_41
      - freenode2_42
      - freenode2_43
      - freenode2_44
      - freenode2_45
      - freenode2_46
      - freenode2_47
      - freenode2_48
      - freenode2_49
      - freenode2_50
      - freenode2_51
      - freenode2_52
      - freenode2_53
      - freenode2_54
      - freenode2_55
      - freenode2_56
      - freenode2_57
      - freenode2_58
      - freenode2_59
      - freenode2_60
      - freenode2_61
      - freenode2_62
      - freenode2_63
      - freenode2_64
      - freenode2_65
      - freenode2_66
      - freenode2_67
      - freenode2_68
      - freenode2_69
      - freenode2_70
      - freenode2_71
      - freenode2_72
      - freenode2_73
      - freenode2_74
      - freenode2_75
      - freenode2_76
      - freenode2_77
  - name: Ⓜ️ 微软服务
    type: select
    proxies:
      - 🎯 全球直连
      - 🚀 节点选择
      - freenode2_1
      - freenode2_2
      - freenode2_3
      - freenode2_4
      - freenode2_5
      - freenode2_6
      - freenode2_7
      - freenode2_8
      - freenode2_9
      - freenode2_10
      - freenode2_11
      - freenode2_12
      - freenode2_13
      - freenode2_14
      - freenode2_15
      - freenode2_16
      - freenode2_17
      - freenode2_18
      - freenode2_19
      - freenode2_20
      - freenode2_21
      - freenode2_22
      - freenode2_23
      - freenode2_24
      - freenode2_25
      - freenode2_26
      - freenode2_27
      - freenode2_28
      - freenode2_29
      - freenode2_30
      - freenode2_31
      - freenode2_32
      - freenode2_33
      - freenode2_34
      - freenode2_35
      - freenode2_36
      - freenode2_37
      - freenode2_38
      - freenode2_39
      - freenode2_40
      - freenode2_41
      - freenode2_42
      - freenode2_43
      - freenode2_44
      - freenode2_45
      - freenode2_46
      - freenode2_47
      - freenode2_48
      - freenode2_49
      - freenode2_50
      - freenode2_51
      - freenode2_52
      - freenode2_53
      - freenode2_54
      - freenode2_55
      - freenode2_56
      - freenode2_57
      - freenode2_58
      - freenode2_59
      - freenode2_60
      - freenode2_61
      - freenode2_62
      - freenode2_63
      - freenode2_64
      - freenode2_65
      - freenode2_66
      - freenode2_67
      - freenode2_68
      - freenode2_69
      - freenode2_70
      - freenode2_71
      - freenode2_72
      - freenode2_73
      - freenode2_74
      - freenode2_75
      - freenode2_76
      - freenode2_77
  - name: 🍎 苹果服务
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - freenode2_1
      - freenode2_2
      - freenode2_3
      - freenode2_4
      - freenode2_5
      - freenode2_6
      - freenode2_7
      - freenode2_8
      - freenode2_9
      - freenode2_10
      - freenode2_11
      - freenode2_12
      - freenode2_13
      - freenode2_14
      - freenode2_15
      - freenode2_16
      - freenode2_17
      - freenode2_18
      - freenode2_19
      - freenode2_20
      - freenode2_21
      - freenode2_22
      - freenode2_23
      - freenode2_24
      - freenode2_25
      - freenode2_26
      - freenode2_27
      - freenode2_28
      - freenode2_29
      - freenode2_30
      - freenode2_31
      - freenode2_32
      - freenode2_33
      - freenode2_34
      - freenode2_35
      - freenode2_36
      - freenode2_37
      - freenode2_38
      - freenode2_39
      - freenode2_40
      - freenode2_41
      - freenode2_42
      - freenode2_43
      - freenode2_44
      - freenode2_45
      - freenode2_46
      - freenode2_47
      - freenode2_48
      - freenode2_49
      - freenode2_50
      - freenode2_51
      - freenode2_52
      - freenode2_53
      - freenode2_54
      - freenode2_55
      - freenode2_56
      - freenode2_57
      - freenode2_58
      - freenode2_59
      - freenode2_60
      - freenode2_61
      - freenode2_62
      - freenode2_63
      - freenode2_64
      - freenode2_65
      - freenode2_66
      - freenode2_67
      - freenode2_68
      - freenode2_69
      - freenode2_70
      - freenode2_71
      - freenode2_72
      - freenode2_73
      - freenode2_74
      - freenode2_75
      - freenode2_76
      - freenode2_77
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
      - freenode2_1
      - freenode2_2
      - freenode2_3
      - freenode2_4
      - freenode2_5
      - freenode2_6
      - freenode2_7
      - freenode2_8
      - freenode2_9
      - freenode2_10
      - freenode2_11
      - freenode2_12
      - freenode2_13
      - freenode2_14
      - freenode2_15
      - freenode2_16
      - freenode2_17
      - freenode2_18
      - freenode2_19
      - freenode2_20
      - freenode2_21
      - freenode2_22
      - freenode2_23
      - freenode2_24
      - freenode2_25
      - freenode2_26
      - freenode2_27
      - freenode2_28
      - freenode2_29
      - freenode2_30
      - freenode2_31
      - freenode2_32
      - freenode2_33
      - freenode2_34
      - freenode2_35
      - freenode2_36
      - freenode2_37
      - freenode2_38
      - freenode2_39
      - freenode2_40
      - freenode2_41
      - freenode2_42
      - freenode2_43
      - freenode2_44
      - freenode2_45
      - freenode2_46
      - freenode2_47
      - freenode2_48
      - freenode2_49
      - freenode2_50
      - freenode2_51
      - freenode2_52
      - freenode2_53
      - freenode2_54
      - freenode2_55
      - freenode2_56
      - freenode2_57
      - freenode2_58
      - freenode2_59
      - freenode2_60
      - freenode2_61
      - freenode2_62
      - freenode2_63
      - freenode2_64
      - freenode2_65
      - freenode2_66
      - freenode2_67
      - freenode2_68
      - freenode2_69
      - freenode2_70
      - freenode2_71
      - freenode2_72
      - freenode2_73
      - freenode2_74
      - freenode2_75
      - freenode2_76
      - freenode2_77

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
"server": "173.234.25.52:48919",
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
