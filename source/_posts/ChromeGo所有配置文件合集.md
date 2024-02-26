
---
title: ChromeGo所有配置文件合集 
date: 2024-02-26 04:29:06
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

> Last Update Time: 2024-02-26 04:29:06
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
  - name: dongtaiwang.com_0
    type: hysteria2
    server: 51.159.77.153
    port: 33390
    password: dongtaiwang.com
    alpn:
      - h3
    sni: bing.com
    skip-cert-verify: true
    up: "11 Mbps"
    down: "55 Mbps"
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
  - {"name":"dongtaiwang.com_1","type":"vmess","server":"23.227.38.11","port":8080,"cipher":"auto","uuid":"9084653a-ee34-4293-979e-7c2b50dffb84","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"configured-creek-relating-theater.trycloudflare.com","network":"ws","ws-opts":{"path":"9084653a-ee34-4293-979e-7c2b50dffb84-vm","headers":{"host":"configured-creek-relating-theater.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_2","type":"vmess","server":"23.227.38.22","port":8080,"cipher":"auto","uuid":"ac750859-79e7-4507-ba93-e92584ac49e3","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"per-essex-patterns-bowling.trycloudflare.com","network":"ws","ws-opts":{"path":"ac750859-79e7-4507-ba93-e92584ac49e3-vm","headers":{"host":"per-essex-patterns-bowling.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_3","type":"vmess","server":"23.227.38.23","port":8080,"cipher":"auto","uuid":"5f7934bf-a228-49a7-9572-5ce4377c34d5","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"uh-lawyers-instruments-kernel.trycloudflare.com","network":"ws","ws-opts":{"path":"5f7934bf-a228-49a7-9572-5ce4377c34d5-vm","headers":{"host":"uh-lawyers-instruments-kernel.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_4","type":"vmess","server":"23.227.38.44","port":8080,"cipher":"auto","uuid":"0e5da13a-b148-4889-9d72-ad1d9d5aa9ad","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"widescreen-instruction-breakdown-postage.trycloudflare.com","network":"ws","ws-opts":{"path":"0e5da13a-b148-4889-9d72-ad1d9d5aa9ad-vm","headers":{"host":"widescreen-instruction-breakdown-postage.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_5","type":"vmess","server":"162.159.134.23","port":8080,"cipher":"auto","uuid":"9084653a-ee34-4293-979e-7c2b50dffb84","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"configured-creek-relating-theater.trycloudflare.com","network":"ws","ws-opts":{"path":"9084653a-ee34-4293-979e-7c2b50dffb84-vm","headers":{"host":"configured-creek-relating-theater.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_6","type":"vmess","server":"162.159.137.31","port":8080,"cipher":"auto","uuid":"ac750859-79e7-4507-ba93-e92584ac49e3","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"per-essex-patterns-bowling.trycloudflare.com","network":"ws","ws-opts":{"path":"ac750859-79e7-4507-ba93-e92584ac49e3-vm","headers":{"host":"per-essex-patterns-bowling.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_7","type":"vmess","server":"162.159.153.11","port":8080,"cipher":"auto","uuid":"5f7934bf-a228-49a7-9572-5ce4377c34d5","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"uh-lawyers-instruments-kernel.trycloudflare.com","network":"ws","ws-opts":{"path":"5f7934bf-a228-49a7-9572-5ce4377c34d5-vm","headers":{"host":"uh-lawyers-instruments-kernel.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_8","type":"vmess","server":"162.159.130.208","port":8080,"cipher":"auto","uuid":"0e5da13a-b148-4889-9d72-ad1d9d5aa9ad","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"widescreen-instruction-breakdown-postage.trycloudflare.com","network":"ws","ws-opts":{"path":"0e5da13a-b148-4889-9d72-ad1d9d5aa9ad-vm","headers":{"host":"widescreen-instruction-breakdown-postage.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_9","type":"vmess","server":"yh1.dtku41.xyz","port":8080,"cipher":"auto","uuid":"9084653a-ee34-4293-979e-7c2b50dffb84","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"configured-creek-relating-theater.trycloudflare.com","network":"ws","ws-opts":{"path":"9084653a-ee34-4293-979e-7c2b50dffb84-vm","headers":{"host":"configured-creek-relating-theater.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_10","type":"vmess","server":"yh1.dtku41.xyz","port":8080,"cipher":"auto","uuid":"ac750859-79e7-4507-ba93-e92584ac49e3","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"per-essex-patterns-bowling.trycloudflare.com","network":"ws","ws-opts":{"path":"ac750859-79e7-4507-ba93-e92584ac49e3-vm","headers":{"host":"per-essex-patterns-bowling.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_11","type":"vmess","server":"yh1.dtku41.xyz","port":8080,"cipher":"auto","uuid":"5f7934bf-a228-49a7-9572-5ce4377c34d5","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"uh-lawyers-instruments-kernel.trycloudflare.com","network":"ws","ws-opts":{"path":"5f7934bf-a228-49a7-9572-5ce4377c34d5-vm","headers":{"host":"uh-lawyers-instruments-kernel.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_12","type":"vmess","server":"yh1.dtku41.xyz","port":8080,"cipher":"auto","uuid":"0e5da13a-b148-4889-9d72-ad1d9d5aa9ad","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"widescreen-instruction-breakdown-postage.trycloudflare.com","network":"ws","ws-opts":{"path":"0e5da13a-b148-4889-9d72-ad1d9d5aa9ad-vm","headers":{"host":"widescreen-instruction-breakdown-postage.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_13","type":"vmess","server":"yh2.dtku41.xyz","port":8080,"cipher":"auto","uuid":"9084653a-ee34-4293-979e-7c2b50dffb84","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"configured-creek-relating-theater.trycloudflare.com","network":"ws","ws-opts":{"path":"9084653a-ee34-4293-979e-7c2b50dffb84-vm","headers":{"host":"configured-creek-relating-theater.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_14","type":"vmess","server":"yh2.dtku41.xyz","port":8080,"cipher":"auto","uuid":"ac750859-79e7-4507-ba93-e92584ac49e3","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"per-essex-patterns-bowling.trycloudflare.com","network":"ws","ws-opts":{"path":"ac750859-79e7-4507-ba93-e92584ac49e3-vm","headers":{"host":"per-essex-patterns-bowling.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_15","type":"vmess","server":"yh2.dtku41.xyz","port":8080,"cipher":"auto","uuid":"5f7934bf-a228-49a7-9572-5ce4377c34d5","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"uh-lawyers-instruments-kernel.trycloudflare.com","network":"ws","ws-opts":{"path":"5f7934bf-a228-49a7-9572-5ce4377c34d5-vm","headers":{"host":"uh-lawyers-instruments-kernel.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_16","type":"vmess","server":"yh2.dtku41.xyz","port":8080,"cipher":"auto","uuid":"0e5da13a-b148-4889-9d72-ad1d9d5aa9ad","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"widescreen-instruction-breakdown-postage.trycloudflare.com","network":"ws","ws-opts":{"path":"0e5da13a-b148-4889-9d72-ad1d9d5aa9ad-vm","headers":{"host":"widescreen-instruction-breakdown-postage.trycloudflare.com"}}}

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
  - {"name":"dongtaiwang.com_1","type":"vmess","server":"fbi.gov","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_2","type":"vmess","server":"103.21.244.107","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_3","type":"vmess","server":"103.21.244.139","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_4","type":"vmess","server":"103.21.244.156","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_5","type":"vmess","server":"103.21.244.162","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_6","type":"vmess","server":"103.21.244.188","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_7","type":"vmess","server":"103.21.244.202","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_8","type":"vmess","server":"103.21.244.207","port":8080,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_9","type":"vmess","server":"103.21.244.21","port":8080,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_10","type":"vmess","server":"103.21.244.222","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_11","type":"vmess","server":"103.21.244.239","port":8080,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_12","type":"vmess","server":"103.21.244.43","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_13","type":"vmess","server":"103.21.244.48","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_14","type":"vmess","server":"103.21.244.48","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_15","type":"vmess","server":"103.21.244.61","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_16","type":"vmess","server":"103.21.244.76","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_17","type":"vmess","server":"103.21.244.90","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_18","type":"vmess","server":"103.21.244.92","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_19","type":"vmess","server":"103.21.244.95","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_20","type":"vmess","server":"108.162.192.50","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_21","type":"vmess","server":"108.162.193.200","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_22","type":"vmess","server":"108.162.193.241","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_23","type":"vmess","server":"108.162.194.192","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_24","type":"vmess","server":"108.162.194.215","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_25","type":"vmess","server":"108.162.195.102","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_26","type":"vmess","server":"108.162.195.142","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_27","type":"vmess","server":"108.162.195.228","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_28","type":"vmess","server":"108.162.196.125","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_29","type":"vmess","server":"108.162.196.163","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_30","type":"vmess","server":"108.162.198.140","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_31","type":"vmess","server":"108.162.198.186","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_32","type":"vmess","server":"108.162.198.241","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_33","type":"vmess","server":"141.101.113.109","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_34","type":"vmess","server":"141.101.113.35","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_35","type":"vmess","server":"141.101.114.11","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_36","type":"vmess","server":"141.101.114.186","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_37","type":"vmess","server":"141.101.114.54","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_38","type":"vmess","server":"141.101.120.111","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_39","type":"vmess","server":"141.101.121.11","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_40","type":"vmess","server":"141.101.121.130","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_41","type":"vmess","server":"141.101.122.109","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_42","type":"vmess","server":"141.101.122.171","port":8080,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_43","type":"vmess","server":"141.101.122.49","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_44","type":"vmess","server":"162.159.13.39","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_45","type":"vmess","server":"162.159.137.23","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_46","type":"vmess","server":"162.159.15.70","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_47","type":"vmess","server":"162.159.22.71","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_48","type":"vmess","server":"162.159.24.165","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_49","type":"vmess","server":"162.159.24.7","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_50","type":"vmess","server":"162.159.243.190","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_51","type":"vmess","server":"162.159.249.242","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_52","type":"vmess","server":"162.159.3.99","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_53","type":"vmess","server":"162.159.33.161","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_54","type":"vmess","server":"162.159.45.230","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_55","type":"vmess","server":"162.159.46.22","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_56","type":"vmess","server":"162.159.48.234","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_57","type":"vmess","server":"162.159.61.113","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_58","type":"vmess","server":"162.159.61.64","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_59","type":"vmess","server":"172.64.231.191","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_60","type":"vmess","server":"172.64.231.230","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_61","type":"vmess","server":"172.64.27.234","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_62","type":"vmess","server":"172.64.33.252","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_63","type":"vmess","server":"172.66.128.78","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_64","type":"vmess","server":"172.66.165.149","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_65","type":"vmess","server":"172.66.173.72","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_66","type":"vmess","server":"172.67.101.196","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_67","type":"vmess","server":"172.67.105.98","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_68","type":"vmess","server":"172.67.120.192","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_69","type":"vmess","server":"172.67.132.97","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_70","type":"vmess","server":"172.67.186.4","port":8080,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_71","type":"vmess","server":"172.67.20.147","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_72","type":"vmess","server":"172.67.234.151","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_73","type":"vmess","server":"172.67.3.129","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_74","type":"vmess","server":"172.67.56.218","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_75","type":"vmess","server":"172.67.67.34","port":8080,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_76","type":"vmess","server":"172.67.72.146","port":8080,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_77","type":"vmess","server":"172.67.92.67","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_78","type":"vmess","server":"173.245.49.10","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_79","type":"vmess","server":"173.245.49.106","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_80","type":"vmess","server":"173.245.49.123","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_81","type":"vmess","server":"173.245.49.157","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_82","type":"vmess","server":"173.245.49.208","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_83","type":"vmess","server":"173.245.49.220","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_84","type":"vmess","server":"173.245.49.32","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_85","type":"vmess","server":"173.245.58.133","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_86","type":"vmess","server":"173.245.58.148","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_87","type":"vmess","server":"173.245.58.54","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_88","type":"vmess","server":"173.245.58.57","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_89","type":"vmess","server":"173.245.59.248","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_90","type":"vmess","server":"173.245.59.251","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_91","type":"vmess","server":"173.245.59.42","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_92","type":"vmess","server":"173.245.59.60","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_93","type":"vmess","server":"173.245.59.72","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_94","type":"vmess","server":"188.114.96.179","port":8080,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_95","type":"vmess","server":"188.114.96.31","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_96","type":"vmess","server":"188.114.96.69","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_97","type":"vmess","server":"188.114.96.71","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_98","type":"vmess","server":"188.114.96.8","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_99","type":"vmess","server":"188.114.97.24","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_100","type":"vmess","server":"188.114.97.32","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_101","type":"vmess","server":"188.114.97.49","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_102","type":"vmess","server":"188.114.98.123","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_103","type":"vmess","server":"188.114.98.128","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_104","type":"vmess","server":"188.114.98.162","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_105","type":"vmess","server":"188.114.98.193","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_106","type":"vmess","server":"188.114.98.201","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_107","type":"vmess","server":"188.114.98.208","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_108","type":"vmess","server":"188.114.98.33","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_109","type":"vmess","server":"188.114.98.66","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_110","type":"vmess","server":"188.114.98.67","port":8080,"cipher":"auto","uuid":"3069ecb6-dd75-4e24-a30d-ec55747d83a1","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"3069ecb6-dd75-4e24-a30d-ec55747d83a1-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_111","type":"vmess","server":"188.114.99.233","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_112","type":"vmess","server":"190.93.244.114","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_113","type":"vmess","server":"190.93.244.122","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_114","type":"vmess","server":"190.93.244.126","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_115","type":"vmess","server":"190.93.244.13","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_116","type":"vmess","server":"190.93.244.21","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_117","type":"vmess","server":"190.93.244.249","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_118","type":"vmess","server":"190.93.244.61","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_119","type":"vmess","server":"190.93.245.232","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_120","type":"vmess","server":"190.93.245.246","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_121","type":"vmess","server":"190.93.245.4","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_122","type":"vmess","server":"190.93.246.138","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_123","type":"vmess","server":"190.93.246.18","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_124","type":"vmess","server":"190.93.246.226","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_125","type":"vmess","server":"190.93.246.239","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_126","type":"vmess","server":"190.93.246.252","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_127","type":"vmess","server":"190.93.246.26","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_128","type":"vmess","server":"190.93.247.131","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_129","type":"vmess","server":"190.93.247.204","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_130","type":"vmess","server":"198.41.192.144","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_131","type":"vmess","server":"198.41.192.209","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_132","type":"vmess","server":"198.41.195.33","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_133","type":"vmess","server":"198.41.196.139","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_134","type":"vmess","server":"198.41.196.219","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_135","type":"vmess","server":"198.41.196.81","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_136","type":"vmess","server":"198.41.199.22","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_137","type":"vmess","server":"198.41.200.217","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_138","type":"vmess","server":"198.41.201.205","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_139","type":"vmess","server":"198.41.201.21","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_140","type":"vmess","server":"198.41.205.204","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_141","type":"vmess","server":"198.41.207.21","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_142","type":"vmess","server":"198.41.209.47","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_143","type":"vmess","server":"198.41.215.116","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_144","type":"vmess","server":"198.41.217.158","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_145","type":"vmess","server":"198.41.217.193","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_146","type":"vmess","server":"198.41.218.10","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_147","type":"vmess","server":"198.41.218.126","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_148","type":"vmess","server":"198.41.218.16","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_149","type":"vmess","server":"198.41.218.55","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_150","type":"vmess","server":"198.41.219.36","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_151","type":"vmess","server":"198.41.222.161","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_152","type":"vmess","server":"198.41.223.149","port":8080,"cipher":"auto","uuid":"d26363ff-8810-4591-8b77-d2f45e2b9f41","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"d26363ff-8810-4591-8b77-d2f45e2b9f41-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_153","type":"vmess","server":"198.41.223.157","port":8080,"cipher":"auto","uuid":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"e6b124d8-7a82-463d-b360-a3a3a19f7dc2-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_154","type":"vmess","server":"198.41.223.91","port":8080,"cipher":"auto","uuid":"41eeccfd-18e6-40b3-933d-c7000120ec2c","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"41eeccfd-18e6-40b3-933d-c7000120ec2c-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
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
      - dongtaiwang.com_111
      - dongtaiwang.com_112
      - dongtaiwang.com_113
      - dongtaiwang.com_114
      - dongtaiwang.com_115
      - dongtaiwang.com_116
      - dongtaiwang.com_117
      - dongtaiwang.com_118
      - dongtaiwang.com_119
      - dongtaiwang.com_120
      - dongtaiwang.com_121
      - dongtaiwang.com_122
      - dongtaiwang.com_123
      - dongtaiwang.com_124
      - dongtaiwang.com_125
      - dongtaiwang.com_126
      - dongtaiwang.com_127
      - dongtaiwang.com_128
      - dongtaiwang.com_129
      - dongtaiwang.com_130
      - dongtaiwang.com_131
      - dongtaiwang.com_132
      - dongtaiwang.com_133
      - dongtaiwang.com_134
      - dongtaiwang.com_135
      - dongtaiwang.com_136
      - dongtaiwang.com_137
      - dongtaiwang.com_138
      - dongtaiwang.com_139
      - dongtaiwang.com_140
      - dongtaiwang.com_141
      - dongtaiwang.com_142
      - dongtaiwang.com_143
      - dongtaiwang.com_144
      - dongtaiwang.com_145
      - dongtaiwang.com_146
      - dongtaiwang.com_147
      - dongtaiwang.com_148
      - dongtaiwang.com_149
      - dongtaiwang.com_150
      - dongtaiwang.com_151
      - dongtaiwang.com_152
      - dongtaiwang.com_153
      - dongtaiwang.com_154
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
      - dongtaiwang.com_111
      - dongtaiwang.com_112
      - dongtaiwang.com_113
      - dongtaiwang.com_114
      - dongtaiwang.com_115
      - dongtaiwang.com_116
      - dongtaiwang.com_117
      - dongtaiwang.com_118
      - dongtaiwang.com_119
      - dongtaiwang.com_120
      - dongtaiwang.com_121
      - dongtaiwang.com_122
      - dongtaiwang.com_123
      - dongtaiwang.com_124
      - dongtaiwang.com_125
      - dongtaiwang.com_126
      - dongtaiwang.com_127
      - dongtaiwang.com_128
      - dongtaiwang.com_129
      - dongtaiwang.com_130
      - dongtaiwang.com_131
      - dongtaiwang.com_132
      - dongtaiwang.com_133
      - dongtaiwang.com_134
      - dongtaiwang.com_135
      - dongtaiwang.com_136
      - dongtaiwang.com_137
      - dongtaiwang.com_138
      - dongtaiwang.com_139
      - dongtaiwang.com_140
      - dongtaiwang.com_141
      - dongtaiwang.com_142
      - dongtaiwang.com_143
      - dongtaiwang.com_144
      - dongtaiwang.com_145
      - dongtaiwang.com_146
      - dongtaiwang.com_147
      - dongtaiwang.com_148
      - dongtaiwang.com_149
      - dongtaiwang.com_150
      - dongtaiwang.com_151
      - dongtaiwang.com_152
      - dongtaiwang.com_153
      - dongtaiwang.com_154
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
      - dongtaiwang.com_111
      - dongtaiwang.com_112
      - dongtaiwang.com_113
      - dongtaiwang.com_114
      - dongtaiwang.com_115
      - dongtaiwang.com_116
      - dongtaiwang.com_117
      - dongtaiwang.com_118
      - dongtaiwang.com_119
      - dongtaiwang.com_120
      - dongtaiwang.com_121
      - dongtaiwang.com_122
      - dongtaiwang.com_123
      - dongtaiwang.com_124
      - dongtaiwang.com_125
      - dongtaiwang.com_126
      - dongtaiwang.com_127
      - dongtaiwang.com_128
      - dongtaiwang.com_129
      - dongtaiwang.com_130
      - dongtaiwang.com_131
      - dongtaiwang.com_132
      - dongtaiwang.com_133
      - dongtaiwang.com_134
      - dongtaiwang.com_135
      - dongtaiwang.com_136
      - dongtaiwang.com_137
      - dongtaiwang.com_138
      - dongtaiwang.com_139
      - dongtaiwang.com_140
      - dongtaiwang.com_141
      - dongtaiwang.com_142
      - dongtaiwang.com_143
      - dongtaiwang.com_144
      - dongtaiwang.com_145
      - dongtaiwang.com_146
      - dongtaiwang.com_147
      - dongtaiwang.com_148
      - dongtaiwang.com_149
      - dongtaiwang.com_150
      - dongtaiwang.com_151
      - dongtaiwang.com_152
      - dongtaiwang.com_153
      - dongtaiwang.com_154
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
      - dongtaiwang.com_111
      - dongtaiwang.com_112
      - dongtaiwang.com_113
      - dongtaiwang.com_114
      - dongtaiwang.com_115
      - dongtaiwang.com_116
      - dongtaiwang.com_117
      - dongtaiwang.com_118
      - dongtaiwang.com_119
      - dongtaiwang.com_120
      - dongtaiwang.com_121
      - dongtaiwang.com_122
      - dongtaiwang.com_123
      - dongtaiwang.com_124
      - dongtaiwang.com_125
      - dongtaiwang.com_126
      - dongtaiwang.com_127
      - dongtaiwang.com_128
      - dongtaiwang.com_129
      - dongtaiwang.com_130
      - dongtaiwang.com_131
      - dongtaiwang.com_132
      - dongtaiwang.com_133
      - dongtaiwang.com_134
      - dongtaiwang.com_135
      - dongtaiwang.com_136
      - dongtaiwang.com_137
      - dongtaiwang.com_138
      - dongtaiwang.com_139
      - dongtaiwang.com_140
      - dongtaiwang.com_141
      - dongtaiwang.com_142
      - dongtaiwang.com_143
      - dongtaiwang.com_144
      - dongtaiwang.com_145
      - dongtaiwang.com_146
      - dongtaiwang.com_147
      - dongtaiwang.com_148
      - dongtaiwang.com_149
      - dongtaiwang.com_150
      - dongtaiwang.com_151
      - dongtaiwang.com_152
      - dongtaiwang.com_153
      - dongtaiwang.com_154
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
      - dongtaiwang.com_111
      - dongtaiwang.com_112
      - dongtaiwang.com_113
      - dongtaiwang.com_114
      - dongtaiwang.com_115
      - dongtaiwang.com_116
      - dongtaiwang.com_117
      - dongtaiwang.com_118
      - dongtaiwang.com_119
      - dongtaiwang.com_120
      - dongtaiwang.com_121
      - dongtaiwang.com_122
      - dongtaiwang.com_123
      - dongtaiwang.com_124
      - dongtaiwang.com_125
      - dongtaiwang.com_126
      - dongtaiwang.com_127
      - dongtaiwang.com_128
      - dongtaiwang.com_129
      - dongtaiwang.com_130
      - dongtaiwang.com_131
      - dongtaiwang.com_132
      - dongtaiwang.com_133
      - dongtaiwang.com_134
      - dongtaiwang.com_135
      - dongtaiwang.com_136
      - dongtaiwang.com_137
      - dongtaiwang.com_138
      - dongtaiwang.com_139
      - dongtaiwang.com_140
      - dongtaiwang.com_141
      - dongtaiwang.com_142
      - dongtaiwang.com_143
      - dongtaiwang.com_144
      - dongtaiwang.com_145
      - dongtaiwang.com_146
      - dongtaiwang.com_147
      - dongtaiwang.com_148
      - dongtaiwang.com_149
      - dongtaiwang.com_150
      - dongtaiwang.com_151
      - dongtaiwang.com_152
      - dongtaiwang.com_153
      - dongtaiwang.com_154
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
      - dongtaiwang.com_111
      - dongtaiwang.com_112
      - dongtaiwang.com_113
      - dongtaiwang.com_114
      - dongtaiwang.com_115
      - dongtaiwang.com_116
      - dongtaiwang.com_117
      - dongtaiwang.com_118
      - dongtaiwang.com_119
      - dongtaiwang.com_120
      - dongtaiwang.com_121
      - dongtaiwang.com_122
      - dongtaiwang.com_123
      - dongtaiwang.com_124
      - dongtaiwang.com_125
      - dongtaiwang.com_126
      - dongtaiwang.com_127
      - dongtaiwang.com_128
      - dongtaiwang.com_129
      - dongtaiwang.com_130
      - dongtaiwang.com_131
      - dongtaiwang.com_132
      - dongtaiwang.com_133
      - dongtaiwang.com_134
      - dongtaiwang.com_135
      - dongtaiwang.com_136
      - dongtaiwang.com_137
      - dongtaiwang.com_138
      - dongtaiwang.com_139
      - dongtaiwang.com_140
      - dongtaiwang.com_141
      - dongtaiwang.com_142
      - dongtaiwang.com_143
      - dongtaiwang.com_144
      - dongtaiwang.com_145
      - dongtaiwang.com_146
      - dongtaiwang.com_147
      - dongtaiwang.com_148
      - dongtaiwang.com_149
      - dongtaiwang.com_150
      - dongtaiwang.com_151
      - dongtaiwang.com_152
      - dongtaiwang.com_153
      - dongtaiwang.com_154
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
      - dongtaiwang.com_111
      - dongtaiwang.com_112
      - dongtaiwang.com_113
      - dongtaiwang.com_114
      - dongtaiwang.com_115
      - dongtaiwang.com_116
      - dongtaiwang.com_117
      - dongtaiwang.com_118
      - dongtaiwang.com_119
      - dongtaiwang.com_120
      - dongtaiwang.com_121
      - dongtaiwang.com_122
      - dongtaiwang.com_123
      - dongtaiwang.com_124
      - dongtaiwang.com_125
      - dongtaiwang.com_126
      - dongtaiwang.com_127
      - dongtaiwang.com_128
      - dongtaiwang.com_129
      - dongtaiwang.com_130
      - dongtaiwang.com_131
      - dongtaiwang.com_132
      - dongtaiwang.com_133
      - dongtaiwang.com_134
      - dongtaiwang.com_135
      - dongtaiwang.com_136
      - dongtaiwang.com_137
      - dongtaiwang.com_138
      - dongtaiwang.com_139
      - dongtaiwang.com_140
      - dongtaiwang.com_141
      - dongtaiwang.com_142
      - dongtaiwang.com_143
      - dongtaiwang.com_144
      - dongtaiwang.com_145
      - dongtaiwang.com_146
      - dongtaiwang.com_147
      - dongtaiwang.com_148
      - dongtaiwang.com_149
      - dongtaiwang.com_150
      - dongtaiwang.com_151
      - dongtaiwang.com_152
      - dongtaiwang.com_153
      - dongtaiwang.com_154

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
  - {"name":"dongtaiwang.com_1","type":"vmess","server":"yh1.freeh1.xyz","port":8080,"cipher":"auto","uuid":"9084653a-ee34-4293-979e-7c2b50dffb84","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"configured-creek-relating-theater.trycloudflare.com","network":"ws","ws-opts":{"path":"9084653a-ee34-4293-979e-7c2b50dffb84-vm","headers":{"host":"configured-creek-relating-theater.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_2","type":"vmess","server":"yh1.freeh1.xyz","port":8080,"cipher":"auto","uuid":"ac750859-79e7-4507-ba93-e92584ac49e3","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"per-essex-patterns-bowling.trycloudflare.com","network":"ws","ws-opts":{"path":"ac750859-79e7-4507-ba93-e92584ac49e3-vm","headers":{"host":"per-essex-patterns-bowling.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_3","type":"vmess","server":"yh1.freeh1.xyz","port":8080,"cipher":"auto","uuid":"5f7934bf-a228-49a7-9572-5ce4377c34d5","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"uh-lawyers-instruments-kernel.trycloudflare.com","network":"ws","ws-opts":{"path":"5f7934bf-a228-49a7-9572-5ce4377c34d5-vm","headers":{"host":"uh-lawyers-instruments-kernel.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_4","type":"vmess","server":"yh1.freeh1.xyz","port":8080,"cipher":"auto","uuid":"0e5da13a-b148-4889-9d72-ad1d9d5aa9ad","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"widescreen-instruction-breakdown-postage.trycloudflare.com","network":"ws","ws-opts":{"path":"0e5da13a-b148-4889-9d72-ad1d9d5aa9ad-vm","headers":{"host":"widescreen-instruction-breakdown-postage.trycloudflare.com"}}}
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
  "server": "51.159.77.198:29277",
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
