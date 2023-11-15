---
title: git submodule添加、更新和删除
date: 2020-04-22 22:22:22
index_img: https://fluid.s3.bitiful.net/hello-fluid/cover.png?w=480&fmt=webp
category: 编程
tags:
  - 编程
  - git
math: true
mermaid: true
sticky: 100
---

# git submodule添加、更新和删除

## 添加[#](https://www.cnblogs.com/jyroy/p/14367776.html#idx_0)

```
Copygit submodule add <url> <path>

```

-   url：替换为自己要引入的子模块仓库地址
-   path：要存放的本地路径

执行添加命令成功后，可以在当前路径中看到一个.gitsubmodule文件，里面的内容就是我们刚刚add的内容

如果在添加子模块的时候想要指定分支，可以利用 -b 参数

```
Copygit submodule add -b <branch> <url> <path>

```

## 例子[#](https://www.cnblogs.com/jyroy/p/14367776.html#idx_1)

### 未指定分支[#](https://www.cnblogs.com/jyroy/p/14367776.html#idx_2)

```
Copygit submodule add https://github.com/tensorflow/benchmarks.git 3rdparty/benchmarks

```

.gitsubmodule内容

```
Copy[submodule "3rdparty/benchmarks"]
path = 3rdparty/benchmarks
url = https://github.com/tensorflow/benchmarks.git

```

### 指定分支[#](https://www.cnblogs.com/jyroy/p/14367776.html#idx_3)

```
Copygit submodule add -b cnn_tf_v1.10_compatible https://github.com/tensorflow/benchmarks.git 3rdparty/benchmarks

```

.gitsubmodule内容

```
Copy[submodule "3rdparty/benchmarks"]
path = 3rdparty/benchmarks
url = https://github.com/tensorflow/benchmarks.git
branch = cnn_tf_v1.10_compatible

```

## 使用[#](https://www.cnblogs.com/jyroy/p/14367776.html#idx_4)

当我们add子模块之后，会发现文件夹下没有任何内容。这个时候我们需要再执行下面的指令添加源码。

```
Copygit submodule update --init --recursive

```

这个命令是下面两条命令的合并版本

```
Copygit submodule init
git submodule update

```

## 更新[#](https://www.cnblogs.com/jyroy/p/14367776.html#idx_5)

我们引入了别人的仓库之后，如果该仓库作者进行了更新，我们需要手动进行更新。即进入子模块后，执行

```
Copygit pull

```

进行更新。

## 删除[#](https://www.cnblogs.com/jyroy/p/14367776.html#idx_6)

1.  删除子模块目录及源码

```
Copyrm -rf 子模块目录

```

2.  删除.gitmodules中的对应子模块内容

```
Copyvi .gitmodules

```

3.  删除.git/config配置中的对应子模块内容

```
Copyvi .git/config

```

4.  删除.git/modules/下对应子模块目录

```
Copyrm -rf .git/modules/子模块目录

```

5.  删除git索引中的对应子模块

```
Copygit rm --cached 子模块目录

```