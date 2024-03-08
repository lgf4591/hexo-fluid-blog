
---
title: ChromeGo所有配置文件合集 
date: 2024-03-08 13:50:20
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

> Last Update Time: 2024-03-08 13:50:20
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
  fallback-filter:
    geoip: false
    ipcidr:
      - 240.0.0.0/4
      - 0.0.0.0/32
proxies:
  - name: dongtaiwang.com_0
    type: ss
    server: 62.204.54.81
    port: 44550
    cipher: 2022-blake3-chacha20-poly1305
    password: "5IH4rBauUuOT4VpAshgMPMSQ3Tf+oJjDY/jEDbIel2Q="
    plugin: shadow-tls
    plugin-opts:
      host: "nijigen-works.jp"
      password: "FHDLxKgzbcDCPmijble8uT1gddgBmOxA1XXeDgyqgGc="
      version: 3
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
            "address": "fbi.gov",
            "port": 443,
            "users": [
              {
                "id": "ebfdccb6-7416-4b6e-860d-98587344d500",
                "alterId": 0,
                "email": "t@t.tt",
                "security": "auto",
                "encryption": "none",
                "flow": ""
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
          "serverName": "lg1.freessr2.xyz",
          "fingerprint": "chrome",
          "show": false
        },
        "wsSettings": {
          "path": "/xyakws",
          "headers": {
            "Host": "lg1.freessr2.xyz"
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
            "address": "yh6.dtku41.xyz",
            "port": 443,
            "users": [
              {
                "id": "ebfdccb6-7416-4b6e-860d-98587344d500",
                "alterId": 0,
                "email": "t@t.tt",
                "security": "auto",
                "encryption": "none",
                "flow": ""
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
          "serverName": "lg1.freessr2.xyz",
          "fingerprint": "chrome",
          "show": false
        },
        "wsSettings": {
          "path": "/xyakws",
          "headers": {
            "Host": "lg1.freessr2.xyz"
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
            "address": "yh1.dtku41.xyz",
            "port": 443,
            "users": [
              {
                "id": "ebfdccb6-7416-4b6e-860d-98587344d500",
                "alterId": 0,
                "email": "t@t.tt",
                "security": "auto",
                "encryption": "none",
                "flow": ""
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
          "serverName": "lg1.freessr2.xyz",
          "fingerprint": "chrome",
          "show": false
        },
        "wsSettings": {
          "path": "/xyakws",
          "headers": {
            "Host": "lg1.freessr2.xyz"
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
  - {"name":"dongtaiwang.com_1","type":"vmess","server":"23.227.38.23","port":8080,"cipher":"auto","uuid":"34c0bb5e-c120-432d-9c58-bd7d82c7397b","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"uh-lawyers-instruments-kernel.trycloudflare.com","network":"ws","ws-opts":{"path":"34c0bb5e-c120-432d-9c58-bd7d82c7397b-vm","headers":{"host":"uh-lawyers-instruments-kernel.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_2","type":"vmess","server":"23.227.38.44","port":8080,"cipher":"auto","uuid":"55021a7c-bd6c-418e-be95-ceac8ba27b45","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"widescreen-instruction-breakdown-postage.trycloudflare.com","network":"ws","ws-opts":{"path":"55021a7c-bd6c-418e-be95-ceac8ba27b45-vm","headers":{"host":"widescreen-instruction-breakdown-postage.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_3","type":"vmess","server":"23.227.38.22","port":8080,"cipher":"auto","uuid":"9258153a-dc97-4e39-9037-009abfc4fed0","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"per-essex-patterns-bowling.trycloudflare.com","network":"ws","ws-opts":{"path":"9258153a-dc97-4e39-9037-009abfc4fed0-vm","headers":{"host":"per-essex-patterns-bowling.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_4","type":"vmess","server":"23.227.38.11","port":8080,"cipher":"auto","uuid":"9b196b50-37f2-4f4b-b175-06273adc6207","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"championship-bidding-oxygen-brochure.trycloudflare.com","network":"ws","ws-opts":{"path":"9b196b50-37f2-4f4b-b175-06273adc6207-vm","headers":{"host":"championship-bidding-oxygen-brochure.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_5","type":"vmess","server":"162.159.153.11","port":8080,"cipher":"auto","uuid":"34c0bb5e-c120-432d-9c58-bd7d82c7397b","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"uh-lawyers-instruments-kernel.trycloudflare.com","network":"ws","ws-opts":{"path":"5f7934bf-a228-49a7-9572-5ce4377c34d5-vm","headers":{"host":"uh-lawyers-instruments-kernel.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_6","type":"vmess","server":"162.159.134.23","port":8080,"cipher":"auto","uuid":"9b196b50-37f2-4f4b-b175-06273adc6207","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"championship-bidding-oxygen-brochure.trycloudflare.com","network":"ws","ws-opts":{"path":"9b196b50-37f2-4f4b-b175-06273adc6207-vm","headers":{"host":"championship-bidding-oxygen-brochure.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_7","type":"vmess","server":"162.159.137.31","port":8080,"cipher":"auto","uuid":"9258153a-dc97-4e39-9037-009abfc4fed0","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"per-essex-patterns-bowling.trycloudflare.com","network":"ws","ws-opts":{"path":"34c0bb5e-c120-432d-9c58-bd7d82c7397b-vm","headers":{"host":"per-essex-patterns-bowling.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_8","type":"vmess","server":"162.159.130.208","port":8080,"cipher":"auto","uuid":"55021a7c-bd6c-418e-be95-ceac8ba27b45","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"widescreen-instruction-breakdown-postage.trycloudflare.com","network":"ws","ws-opts":{"path":"55021a7c-bd6c-418e-be95-ceac8ba27b45-vm","headers":{"host":"widescreen-instruction-breakdown-postage.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_9","type":"vmess","server":"yh1.dtku41.xyz","port":8080,"cipher":"auto","uuid":"34c0bb5e-c120-432d-9c58-bd7d82c7397b","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"uh-lawyers-instruments-kernel.trycloudflare.com","network":"ws","ws-opts":{"path":"34c0bb5e-c120-432d-9c58-bd7d82c7397b-vm","headers":{"host":"uh-lawyers-instruments-kernel.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_10","type":"vmess","server":"yh1.dtku41.xyz","port":8080,"cipher":"auto","uuid":"9b196b50-37f2-4f4b-b175-06273adc6207","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"championship-bidding-oxygen-brochure.trycloudflare.com","network":"ws","ws-opts":{"path":"9b196b50-37f2-4f4b-b175-06273adc6207-vm","headers":{"host":"championship-bidding-oxygen-brochure.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_11","type":"vmess","server":"yh1.dtku41.xyz","port":8080,"cipher":"auto","uuid":"9258153a-dc97-4e39-9037-009abfc4fed0","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"per-essex-patterns-bowling.trycloudflare.com","network":"ws","ws-opts":{"path":"9258153a-dc97-4e39-9037-009abfc4fed0-vm","headers":{"host":"per-essex-patterns-bowling.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_12","type":"vmess","server":"yh1.dtku41.xyz","port":8080,"cipher":"auto","uuid":"55021a7c-bd6c-418e-be95-ceac8ba27b45","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"widescreen-instruction-breakdown-postage.trycloudflare.com","network":"ws","ws-opts":{"path":"55021a7c-bd6c-418e-be95-ceac8ba27b45-vm","headers":{"host":"widescreen-instruction-breakdown-postage.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_13","type":"vmess","server":"yh2.dtku41.xyz","port":8080,"cipher":"auto","uuid":"34c0bb5e-c120-432d-9c58-bd7d82c7397b","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"uh-lawyers-instruments-kernel.trycloudflare.com","network":"ws","ws-opts":{"path":"34c0bb5e-c120-432d-9c58-bd7d82c7397b-vm","headers":{"host":"uh-lawyers-instruments-kernel.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_14","type":"vmess","server":"yh2.dtku41.xyz","port":8080,"cipher":"auto","uuid":"9b196b50-37f2-4f4b-b175-06273adc6207","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"championship-bidding-oxygen-brochure.trycloudflare.com","network":"ws","ws-opts":{"path":"9b196b50-37f2-4f4b-b175-06273adc6207-vm","headers":{"host":"championship-bidding-oxygen-brochure.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_15","type":"vmess","server":"yh2.dtku41.xyz","port":8080,"cipher":"auto","uuid":"9258153a-dc97-4e39-9037-009abfc4fed0","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"per-essex-patterns-bowling.trycloudflare.com","network":"ws","ws-opts":{"path":"9258153a-dc97-4e39-9037-009abfc4fed0-vm","headers":{"host":"per-essex-patterns-bowling.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_16","type":"vmess","server":"yh2.dtku41.xyz","port":8080,"cipher":"auto","uuid":"55021a7c-bd6c-418e-be95-ceac8ba27b45","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"widescreen-instruction-breakdown-postage.trycloudflare.com","network":"ws","ws-opts":{"path":"55021a7c-bd6c-418e-be95-ceac8ba27b45-vm","headers":{"host":"widescreen-instruction-breakdown-postage.trycloudflare.com"}}}

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
  - {"name":"dongtaiwang.com_1","type":"vmess","server":"fbi.gov","port":8080,"cipher":"auto","uuid":"d9c5ec6a-a8d8-4732-8447-56fbd2f93e96","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"d9c5ec6a-a8d8-4732-8447-56fbd2f93e96-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_2","type":"vmess","server":"fbi.gov","port":8080,"cipher":"auto","uuid":"ef8c954e-014f-4b36-8273-9b5086afab34","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"ef8c954e-014f-4b36-8273-9b5086afab34-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_3","type":"vmess","server":"fbi.gov","port":8080,"cipher":"auto","uuid":"028c8131-9e3e-4836-94ac-ea7f24d4d05a","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"028c8131-9e3e-4836-94ac-ea7f24d4d05a-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_4","type":"vmess","server":"fbi.gov","port":8080,"cipher":"auto","uuid":"82cb93a3-65a9-4dac-a2a7-d997b6c26d6a","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"82cb93a3-65a9-4dac-a2a7-d997b6c26d6a-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
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
  - name: dongtaiwang.com_0
    server: 64.31.55.18
    port: 11223
    type: tuic
    uuid: 1a0a455e-4207-44be-b5a0-062747671570
    password: dongtaiwang.com
    alpn: [h3]
    disable-sni: true
    reduce-rtt: true
    udp-relay-mode: native
    congestion-controller: bbr
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
  - {"name":"dongtaiwang.com_1","type":"vmess","server":"23.227.39.12","port":8080,"cipher":"auto","uuid":"34c0bb5e-c120-432d-9c58-bd7d82c7397b","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"uh-lawyers-instruments-kernel.trycloudflare.com","network":"ws","ws-opts":{"path":"34c0bb5e-c120-432d-9c58-bd7d82c7397b-vm","headers":{"host":"uh-lawyers-instruments-kernel.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_2","type":"vmess","server":"23.227.39.24","port":8080,"cipher":"auto","uuid":"9258153a-dc97-4e39-9037-009abfc4fed0","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"per-essex-patterns-bowling.trycloudflare.com","network":"ws","ws-opts":{"path":"9258153a-dc97-4e39-9037-009abfc4fed0-vm","headers":{"host":"per-essex-patterns-bowling.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_3","type":"vmess","server":"23.227.39.23","port":8080,"cipher":"auto","uuid":"9b196b50-37f2-4f4b-b175-06273adc6207","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"championship-bidding-oxygen-brochure.trycloudflare.com","network":"ws","ws-opts":{"path":"9b196b50-37f2-4f4b-b175-06273adc6207-vm","headers":{"host":"championship-bidding-oxygen-brochure.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_4","type":"vmess","server":"23.227.39.45","port":8080,"cipher":"auto","uuid":"55021a7c-bd6c-418e-be95-ceac8ba27b45","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"widescreen-instruction-breakdown-postage.trycloudflare.com","network":"ws","ws-opts":{"path":"55021a7c-bd6c-418e-be95-ceac8ba27b45-vm","headers":{"host":"widescreen-instruction-breakdown-postage.trycloudflare.com"}}}
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
  - {"name":"dongtaiwang.com_1","type":"vmess","server":"yh1.freeh1.xyz","port":8080,"cipher":"auto","uuid":"34c0bb5e-c120-432d-9c58-bd7d82c7397b","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"uh-lawyers-instruments-kernel.trycloudflare.com","network":"ws","ws-opts":{"path":"34c0bb5e-c120-432d-9c58-bd7d82c7397b-vm","headers":{"host":"uh-lawyers-instruments-kernel.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_2","type":"vmess","server":"yh1.freeh1.xyz","port":8080,"cipher":"auto","uuid":"9258153a-dc97-4e39-9037-009abfc4fed0","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"per-essex-patterns-bowling.trycloudflare.com","network":"ws","ws-opts":{"path":"9258153a-dc97-4e39-9037-009abfc4fed0-vm","headers":{"host":"per-essex-patterns-bowling.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_3","type":"vmess","server":"yh1.freeh1.xyz","port":8080,"cipher":"auto","uuid":"9b196b50-37f2-4f4b-b175-06273adc6207","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"championship-bidding-oxygen-brochure.trycloudflare.com","network":"ws","ws-opts":{"path":"9b196b50-37f2-4f4b-b175-06273adc6207-vm","headers":{"host":"championship-bidding-oxygen-brochure.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_4","type":"vmess","server":"yh1.freeh1.xyz","port":8080,"cipher":"auto","uuid":"55021a7c-bd6c-418e-be95-ceac8ba27b45","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"widescreen-instruction-breakdown-postage.trycloudflare.com","network":"ws","ws-opts":{"path":"55021a7c-bd6c-418e-be95-ceac8ba27b45-vm","headers":{"host":"widescreen-instruction-breakdown-postage.trycloudflare.com"}}}
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
  - {"name":"dongtaiwang.com_1","type":"vmess","server":"fbi.gov","port":8080,"cipher":"auto","uuid":"d9c5ec6a-a8d8-4732-8447-56fbd2f93e96","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"d9c5ec6a-a8d8-4732-8447-56fbd2f93e96-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_2","type":"vmess","server":"fbi.gov","port":8080,"cipher":"auto","uuid":"ef8c954e-014f-4b36-8273-9b5086afab34","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"ef8c954e-014f-4b36-8273-9b5086afab34-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_3","type":"vmess","server":"fbi.gov","port":8080,"cipher":"auto","uuid":"028c8131-9e3e-4836-94ac-ea7f24d4d05a","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"028c8131-9e3e-4836-94ac-ea7f24d4d05a-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_4","type":"vmess","server":"fbi.gov","port":8080,"cipher":"auto","uuid":"82cb93a3-65a9-4dac-a2a7-d997b6c26d6a","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"82cb93a3-65a9-4dac-a2a7-d997b6c26d6a-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_5","type":"vmess","server":"yh1.freeh1.xyz","port":8080,"cipher":"auto","uuid":"ef8c954e-014f-4b36-8273-9b5086afab34","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"ef8c954e-014f-4b36-8273-9b5086afab34-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_6","type":"vmess","server":"yh1.freeh1.xyz","port":8080,"cipher":"auto","uuid":"028c8131-9e3e-4836-94ac-ea7f24d4d05a","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"028c8131-9e3e-4836-94ac-ea7f24d4d05a-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_7","type":"vmess","server":"yh1.freeh1.xyz","port":8080,"cipher":"auto","uuid":"d9c5ec6a-a8d8-4732-8447-56fbd2f93e96","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"d9c5ec6a-a8d8-4732-8447-56fbd2f93e96-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_8","type":"vmess","server":"yh1.freeh1.xyz","port":8080,"cipher":"auto","uuid":"82cb93a3-65a9-4dac-a2a7-d997b6c26d6a","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"82cb93a3-65a9-4dac-a2a7-d997b6c26d6a-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_9","type":"vmess","server":"yh2.freeh1.xyz","port":8080,"cipher":"auto","uuid":"ef8c954e-014f-4b36-8273-9b5086afab34","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"ef8c954e-014f-4b36-8273-9b5086afab34-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_10","type":"vmess","server":"yh2.freeh1.xyz","port":8080,"cipher":"auto","uuid":"028c8131-9e3e-4836-94ac-ea7f24d4d05a","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"028c8131-9e3e-4836-94ac-ea7f24d4d05a-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_11","type":"vmess","server":"yh2.freeh1.xyz","port":8080,"cipher":"auto","uuid":"d9c5ec6a-a8d8-4732-8447-56fbd2f93e96","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"d9c5ec6a-a8d8-4732-8447-56fbd2f93e96-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_12","type":"vmess","server":"yh3.freeh1.xyz","port":8080,"cipher":"auto","uuid":"82cb93a3-65a9-4dac-a2a7-d997b6c26d6a","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"82cb93a3-65a9-4dac-a2a7-d997b6c26d6a-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_13","type":"vmess","server":"yh3.freeh1.xyz","port":8080,"cipher":"auto","uuid":"ef8c954e-014f-4b36-8273-9b5086afab34","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"bibliographic-sword-sequence-advertisers.trycloudflare.com","network":"ws","ws-opts":{"path":"ef8c954e-014f-4b36-8273-9b5086afab34-vm","headers":{"host":"bibliographic-sword-sequence-advertisers.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_14","type":"vmess","server":"yh3.freeh1.xyz","port":8080,"cipher":"auto","uuid":"028c8131-9e3e-4836-94ac-ea7f24d4d05a","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"nest-emily-healing-h.trycloudflare.com","network":"ws","ws-opts":{"path":"028c8131-9e3e-4836-94ac-ea7f24d4d05a-vm","headers":{"host":"nest-emily-healing-h.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_15","type":"vmess","server":"yh3.freeh1.xyz","port":8080,"cipher":"auto","uuid":"d9c5ec6a-a8d8-4732-8447-56fbd2f93e96","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"pcs-referenced-camera-concerns.trycloudflare.com","network":"ws","ws-opts":{"path":"d9c5ec6a-a8d8-4732-8447-56fbd2f93e96-vm","headers":{"host":"pcs-referenced-camera-concerns.trycloudflare.com"}}}
  - {"name":"dongtaiwang.com_16","type":"vmess","server":"yh3.freeh1.xyz","port":8080,"cipher":"auto","uuid":"82cb93a3-65a9-4dac-a2a7-d997b6c26d6a","alterId":0,"tls":false,"skip-cert-verify":true,"servername":"larger-marketing-amounts-skin.trycloudflare.com","network":"ws","ws-opts":{"path":"82cb93a3-65a9-4dac-a2a7-d997b6c26d6a-vm","headers":{"host":"larger-marketing-amounts-skin.trycloudflare.com"}}}

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
  "server": "51.159.77.198:53967",
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
      "type": "shadowsocks",
      "tag": "ss-6120",
      "method": "2022-blake3-chacha20-poly1305", 
      "password": "5IH4rBauUuOT4VpAshgMPMSQ3Tf+oJjDY/jEDbIel2Q=",
      "detour": "stl-6243",
      "multiplex": {
        "enabled": true,
        "protocol": "h2mux",
        "max_connections": 1,
        "min_streams": 4,
        "padding": false
      }
    },
    {
      "type": "shadowtls",
      "tag": "stl-6243",
      "server": "172.83.156.157", 
      "server_port": 44550,
      "version": 3, 
      "password": "FHDLxKgzbcDCPmijble8uT1gddgBmOxA1XXeDgyqgGc=", 
      "tls": {
        "enabled": true,
        "server_name": "nijigen-works.jp", 
        "utls": {
          "enabled": true,
          "fingerprint": "chrome" 
        }
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
