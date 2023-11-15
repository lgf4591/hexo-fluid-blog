
import datetime
import urllib.request



def curl(url):
    try:
        response = urllib.request.urlopen(url)
        if response.status == 200:
            # 响应状态码为200表示请求成功
            data = response.read().decode('utf-8')
            # json_data = json.loads(data)
            # print(json_data)
            return data
        else:
            print(f'Error: {response.status} {response.reason}')
    except urllib.error.URLError as e:
        print(f'Error: {e.reason}')

update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

vless_node = curl('https://vless-node.lgf4591.workers.dev/0d9163eb-b54f-4144-b7a2-96efda0f4ee7')
better_cf_ips = curl('https://raw.githubusercontent.com/Alvin9999/new-pac/master/CloudFlare%E4%BC%98%E8%B4%A8IP')
freefq_doc = curl('https://raw.githubusercontent.com/freefq/free/master/README.md')
github520_doc = curl('https://raw.githubusercontent.com/521xueweihan/GitHub520/main/README.md')
fetch_github_hosts_doc = curl('https://raw.githubusercontent.com/Licoy/fetch-github-hosts/main/README.md')


with open("python/chromego_merge/ReadMe.md","r", encoding="utf-8") as f:
    chromego_merge_readme = f.read()

with open("python/chromego_merge/sub/merged_proxies.yaml","r", encoding="utf-8") as f:
    chromego_merge_merged_proxies = f.read()

with open("python/chromego_merge/sub/merged_proxies_new.yaml","r", encoding="utf-8") as f:
    chromego_merge_merged_proxies_new = f.read()
    
with open("python/chromego_merge/sub/merged_warp_proxies.yaml","r", encoding="utf-8") as f:
    chromego_merge_merged_warp_proxies = f.read()
    
with open("python/chromego_merge/sub/merged_warp_proxies_new.yaml","r", encoding="utf-8") as f:
    chromego_merge_merged_warp_proxies_new = f.read()
    
with open("python/chromego_merge/sub/shadowrocket_base64.txt","r", encoding="utf-8") as f:
    chromego_merge_shadowrocket_base64 = f.read()


final_content = f"""
---
title: VPN合集 
date: {update_time}
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

> Last Update Time: {update_time}
---
# vless_node
```bash

{vless_node}

```

# CloudFlare优质IP
```bash

{better_cf_ips}

```

# Github hosts
## [Github520](https://github.com/521xueweihan/GitHub520)
{github520_doc}

## [Fetch GitHub Hosts](https://hosts.gitcdn.top/)
{fetch_github_hosts_doc}

# [freefq](https://github.com/freefq/free)
{freefq_doc}


# ChromeGo_Merge Readme Content
{chromego_merge_readme}

# ChromeGo_Merge Detail Content
## 不套warp版本（clashmeta）
**不含hysteria2节点** (https://mareep.netlify.app/sub/merged_proxies.yaml)
```yaml
{chromego_merge_merged_proxies}
```

**含hysteria2节点(节点最全）** (https://mareep.netlify.app/sub/merged_proxies_new.yaml)
```yaml
{chromego_merge_merged_proxies_new}
```

## 套warp版本（clashmeta)
**不含hysteria2节点** (https://mareep.netlify.app/sub/merged_warp_proxies.yaml)
```yaml
{chromego_merge_merged_warp_proxies}
```

**含hysteria2节点(节点最全）** (https://mareep.netlify.app/sub/merged_warp_proxies_new.yaml)
```yaml
{chromego_merge_merged_warp_proxies_new}
```

## 通用链接 （shadowrocket和nekoray）  (https://mareep.netlify.app/sub/shadowrocket_base64.txt)
```txt
{chromego_merge_shadowrocket_base64}
```

## sing-box订阅链接 (https://sing-box-subscribe.vercel.app/config/https:/mareep.netlify.app/sub/merged_proxies_new.yaml)
```yaml
None
```


"""

def main():
    print("hello, python")
    # print(final_content)
    with open("source/_posts/VPN合集.md", "w", encoding="utf-8") as f:
        f.write(final_content)
    

if __name__ == "__main__":
    main()



