---
title: 为 Python 项目编写 Makefile
date: 2020-04-22 22:22:22
index_img: https://fluid.s3.bitiful.net/hello-fluid/cover.png?w=480&fmt=webp
category: 编程
tags:
  - 编程
  - python
  - makefile
math: true
mermaid: true
sticky: 100
---

本文翻译自**Writing Makefiles for Python Projects**<sup>[1]</sup>。原作者：Bastian Venthur.

作为 `Makefiles`的粉丝，我几乎在每一个业余项目里面都使用它们。并且我也主张在工作项目中使用。

对开源项目来说，`Makefiles` 让代码贡献者知道怎么构建、测试、部署项目。并且，如果你正确使用了 `Makefiles`，他们可以大大简化你的CI/CD 流程脚本。因为你只需要简单地调用对应的 `make` 命令就可以了。最重要的是，`Makefiles` 可以简化你的开发工作。

对 Python 项目来说，我总是使用虚拟环境，因此我使用了两个不同的 `Makefiles` 策略：

1.  假设 make 命令是在虚拟环境里面执行的

2.  通过 make 命令来封装虚拟环境的命令

## 假设 make 命令是在虚拟环境中执行的

我们来看一个非常简单的 `Makefile` 文件，这个文件可以让你实现构建、测试和发布 Python 项目：

```
all: lint test
.PHONY: test
test:
    pytest
.PHONY: lint
lint:
    flake8
.PHONY: release
release:
    python3 setup.py sdist bdist_wheel upload
clean:
    find . -type f -name *.pyc -delete
    find . -type d -name __pycache__ -delete
```

这几段代码写的非常直接，所有潜在贡献者立刻就知道你项目的入口在哪里了。

假设已经有一个虚拟环境了，那么你需要首先激活它，然后再运行 make 命令：

```
$ . venv/bin/activate
$ make test
```

当然，不方便的地方在于，你的每一个 shell 窗口都必须手动激活虚拟环境。所以当你使用 tmux  激活一个新的终端窗口或者把 vim 放到后台上去运行的时候，就很麻烦。

在 make 命令里面激活虚拟环境看起来是很难做到的，因为每一段代码甚至每一个命令都会在它自己的 shell 里面运行。但是我们稍后看一个办法绕过这个限制，比如说使用`.ONESHELL`标志，但这无法解决新开新的代码片段运行在新 shell 的问题。

## 在 make 命令里面封装虚拟环境的调用命令

第二个方法基本上解决了在 make 命令里面激活虚拟环境的问题。这个办法是从**makefile.venv**<sup>[2]</sup>里面学到的，我简化了一下：

```
# system python interpreter. used only to create virtual environment
PY = python3
VENV = venv
BIN=$(VENV)/bin
# make it work on windows too
ifeq ($(OS), Windows_NT)
    BIN=$(VENV)/Scripts
    PY=python
endif
all: lint test
$(VENV): requirements.txt requirements-dev.txt setup.py
    $(PY) -m venv $(VENV)
    $(BIN)/pip install --upgrade -r requirements.txt
    $(BIN)/pip install --upgrade -r requirements-dev.txt
    $(BIN)/pip install -e .
    touch $(VENV)
.PHONY: test
test: $(VENV)
    $(BIN)/pytest
.PHONY: lint
lint: $(VENV)
    $(BIN)/flake8
.PHONY: release
release: $(VENV)
    $(BIN)/python setup.py sdist bdist_wheel upload
clean:
    rm -rf $(VENV)
    find . -type f -name *.pyc -delete
    find . -type d -name __pycache__ -delete
```

仅从功能上看，这个 Makefile 跟刚才的差不多，但是代码看起来更复杂了。所以我们现在一行一行来看看它是怎么实现的。

如果虚拟环境已经激活，或者`pytest`, `flake8`这些包已经安装到了系统 Python 环境里面，那么我们直接调用他们就可以了。但是现在，在新的 Makefile 文件中，我们显式地使用虚拟环境中的绝对路径来调用他们。为了确保虚拟环境存在，每一段代码都依赖于`$(VENV)`这一项。这一项确保了当前有一个最新的虚拟环境可用。

这种方案有效，是因为当我们执行`. venv/bin/activate`的时候，本来虚拟环境就是把它自己的绝对路径放到了环境变量里面。因此每一次调用 Python 或者其他包的时候，都是使用虚拟环境中安装的。

虽然 Makefile 文件变得有点复杂了，但是我们要测试代码的时候，还是仅仅需要简单地执行一下命令：

就可以了，我们不需要再去关心虚拟环境是不是已经安装了之类的问题。如果你不需要支持 Windows，甚至可以从 Makefile 里面移除Windows 相关的部分。这样一来，这个 Makefile 文件即使对于不怎么用的人来说也不难理解。

## 哪一种更好？

我觉得第二种方案更方便。虽然第一种方法我已经快乐地用了几年了，而第二种方法是最近才学到的。之前我确实没有注意到这种方法。但我注意到几乎所有使用 Makefile的 Python 项目都用的第一种方法，我也想知道为什么。

## Kingname 点评

我在Python 项目和Golang 项目里面经常使用Makefile，其中，Python 项目我主要用来删除`__pycache__`，而 Golang 项目中，由于我使用的是 VSCode 来开发，它的 lint 有点问题，所以代码写完以后，我会使用 Makefile 来执行一段`gofmt`命令，把所有`.go`文件都格式化。

但 Makefile 有一个非常智障的地方——它里面的缩进必须使用制表符，不能使用空格。所以要写Makefile 的时候，我还必须用 vim 来写。因为我的 PyCharm 已经调成把所有制表符换成空格的设置了。而如果在 Makefile 的缩进里面混入了空格，它就会报错。

### 参考资料

\[1\]

Writing Makefiles for Python Projects: _[https://venthur.de/2021-03-31-python-makefiles.html](https://venthur.de/2021-03-31-python-makefiles.html)_

\[2\]

makefile.venv: _[https://github.com/sio/Makefile.venv](https://github.com/sio/Makefile.venv)_

请关注微信公众号【未闻Code】获取更多精彩文章。