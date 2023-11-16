---
title: Github Actions + Cloudflare Pages 部署静态网站
date: 2020-04-22 22:22:22
index_img: https://fluid.s3.bitiful.net/hello-fluid/cover.png?w=480&fmt=webp
category: 编程
tags:
  - 编程
  - Cloudflare
  - GitHub Actions
  - Hexo
math: true
mermaid: true
sticky: 100
---

本文首发于：[玩转云服务（4）：Github Actions + Cloudflare Pages 部署静态网站](https://link.zhihu.com/?target=https%3A//blog.baldcoder.top/articles/deploying-a-static-website-with-github-action-and-cloudflare-pages/)

Github Pages 很好很强大，对于公有仓库来说几乎无用量限制。参见：[凉拖捞佬Pro：玩转云服务（3）：使用 Hugo + docsy + Github Actions + Github Pages 创建项目文档](https://zhuanlan.zhihu.com/p/654959051)

但是，有一个很致命的问题：只有个人主页、公司主页和为项目单独创立个账户，才能分配到独立的三级域名 `<project-name>.github.io` ，否则如果是个人账户下的其他仓库，分配到的是带路径的域名。比如说我的 Github 帐户名是 eterance，我有个仓库叫 web-toolbox，那么分配的 URL 是：`https://eterance.github.io/web-toolbox/` 。这就带来几个问题：

-   名字太长不好记，而且因为和账户名和仓库名绑定，没法改。
-   虽然可以绑定自定义域名，但是也只是 `https://eterance.github.io/web-toolbox/` → `https://tools.eterance.com/web-toolbox/`，而不是我需要的 `https://eterance.github.io/web-toolbox/` → `https://tools.eterance.com/`。也就是说，三级域名改称自己的了，但是后面还是有个仓库名的小尾巴。
-   URL带路径还有个问题，就是自己徒手撸的 HTML 文件里，所有 link、src 的 “/path/to/main.css” 这种从根目录算起的路径就不能用了，得改成 “/web-toolbox/path/to/main.css” ；但是本地改了在本地服务器上又不能用了。虽然可以靠 Github Actions 在部署时做字符串替换，但是还是不方便。

相比之下，Cloudflare Pages 就没这种问题，分配的 URL 都是没有小尾巴的三级域名 `<site-name>.pages.dev`，而且 `<site-name>` 还是能自己随意取的，不受仓库名限制；甚至还能很方便的绑自己的域名。

官方文档：[Use Direct Upload with continuous integration · Cloudflare Pages docs](https://link.zhihu.com/?target=https%3A//developers.cloudflare.com/pages/how-to/use-direct-upload-with-continuous-integration/)

## 先决条件

-   把你的网站项目上传到 Github。我的示例：[GitHub - Eterance/web-toolbox](https://link.zhihu.com/?target=https%3A//github.com/Eterance/web-toolbox)

## 配置 Cloudflare 帐户凭据

### 获取 Cloudflare API 令牌

1.  登录 Cloudflare 仪表板。
2.  点击在仪表板右上角的用户图标，下拉菜单中选择“我的个人资料”。
3.  选择左边导航栏的“API 令牌” > “创建令牌”。
4.  滚动到最底部，在“自定义令牌”下，选择“开始”。
5.  在“令牌名称”字段中起个名字。建议与项目有关联，一个项目用一个令牌，不要重复使用。
6.  在“权限”下，选择“账户”、“Cloudflare Pages” 和 “编辑”：
7.  选择“继续以显示摘要” > “创建令牌”。
8.  复制令牌待后面使用。

![](https://pic2.zhimg.com/v2-22a891fc9bb2fd5fde16908a7216e53d_b.jpg)

如果以后不用了，记得及时回来这里删掉令牌。

### 获取 Cloudflare 帐户 ID

随便点进去一个自己托管到 CF 的域名，拉到最下方右下角即可复制。

![](https://pic4.zhimg.com/v2-7567ec3523ebfff9af7e55d8f8f1e17b_b.jpg)

### 添加凭据到 Github

进入项目设置，分别添加令牌和ID。令牌的名字是 **`CLOUDFLARE_API_TOKEN`**，ID 的是 **`CLOUDFLARE_ACCOUNT_ID`**。

![](https://pic3.zhimg.com/v2-aa368c8e830964b630f5e9c1b78c07f2_b.jpg)

## 建立 Cloudflare Pages 项目

打开 CF pages 面板：[https://dash.cloudflare.com/sign-up/workers-and-pages](https://link.zhihu.com/?target=https%3A//dash.cloudflare.com/sign-up/workers-and-pages)

选择上传资产。

![](https://pic3.zhimg.com/v2-d5aa2ac76ef19f9cb56c6bf51047f242_b.jpg)

取个项目名字，同时也就是域名（如果域名被人取过了就会自动在后面添加随机字符，但是项目名字不变）。下载一个演示站点（不用解压），然后创建。

![](https://pic1.zhimg.com/v2-99f37623aeafdc48eec81fbbd05ebd48_b.jpg)

然后直接上传压缩包并且创建。成功后会给出项目网址：

![](https://pic4.zhimg.com/v2-294fac3bc685e6a59c7ef7421c1babc3_b.jpg)

## 设置 Github Actions

在项目根目录里新建文件 `.github/workflows/cf-pages.yml`。然后把我的 [cf-pages.yml](https://link.zhihu.com/?target=https%3A//github.com/Eterance/web-toolbox/blob/main/.github/workflows/cf-pages.yml) 内容粘贴进去。

官方原始文件：[https://github.com/cloudflare/pages-action](https://link.zhihu.com/?target=https%3A//github.com/cloudflare/pages-action)

这里只讲解最后一块：

```
- name: Publish to Cloudflare Pages
        uses: cloudflare/pages-action@v1
        with:
          apiToken: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          accountId: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}
          projectName: eterance-tools
          directory: ./
          # Optional: Enable this if you want to have GitHub Deployments triggered
          gitHubToken: ${{ secrets.GITHUB_TOKEN }}
          # Optional: Switch what branch you are publishing to.
          # By default this will be the branch which triggered this workflow
          branch: main
          # Optional: Change the working directory
          # All my website content is in the site folder
          workingDirectory: ./site
          # Optional: Change the Wrangler version, allows you to point to a specific version or a tag such as `beta`
          wranglerVersion: '3'
```

-   projectName：写 CF Pages 的项目名。即使你的域名因为重名，后面被加了随机字符，那也是原来那个。
-   workingDirectory：因为我的网站网址全放到 `site` 文件夹所以我写了 `./site`。如果你的网站文件是一整个根目录，或者使用 jekyll、hugo 之类的生成到 dist 文件夹，则要相应修改。

然后推送，Github Action 就会自动部署。

部署成功后就可以访问项目网址了。

## 绑定自定义域名（可选）

![](https://pic4.zhimg.com/v2-12fbdaeb8909e2114b17c0faf00d8f3b_b.jpg)

![](https://pic2.zhimg.com/v2-55b7a4e1bb5f72119b383e805513a8c9_b.jpg)

之后激活域。

接下来，如果你的域名托管在 CF 上，那么什么都不用做等十来分钟就行；否则，还要去域名的解析提供商做个 cname 解析。

![](https://pic2.zhimg.com/v2-80d66b90001addddc2015057c4ae00d1_b.jpg)
