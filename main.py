
import datetime

update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>UpdateTime: {update_time}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
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



