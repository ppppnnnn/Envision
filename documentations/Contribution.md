<h1 align=center>Envision Contribution Guide</h1>
<p align=center>
<img src="https://img.shields.io/badge/version-1.0.0a-red.svg"> <img src="https://img.shields.io/badge/founder-Owen%20Tsai-orange.svg"> <img src="https://img.shields.io/badge/%E5%9B%9B%E5%B7%9D%E8%BD%BB%E5%8C%96%E5%B7%A5-AAIT-brightgreen.svg"> <img src="https://img.shields.io/badge/status-ReBuild%20in%20Progress-blue.svg">
</p>
  
<p align=center><b> - 任何参与 Envision 开发的贡献者均应参考本手册 - </b></p>
<br>

**通过阅读本文档，你将会：**
- 对项目做出贡献的方式；
- 在本地开发机器上完成项目开发环境的部署，并运行开发版项目；
- 了解客户端和服务端的代码编写规范；
- 向我们提交你的代码。

## 1 如何向 Envision 做出贡献

> 在这一部分你将会了解到所有能够对维护团队开发和维护 Envision 做出积极贡献的途径。大致浏览这一部分的内容，你可以很快地知道自己可以**怎样**为 Envision 贡献力量。

### 1.1 技术贡献

Envision 客户端采用 [**vue.js**](https://cn.vuejs.org/index.html) 作为框架，采用 [**Vuetify**](https://vuetifyjs.com/zh-Hans/) 作为UI组件库。如果你熟悉或者想要使用`vue.js`进行Web应用的开发，你可以考虑参与到 Envision 前端的开发进程中。查看 [【2.1 前端开发】](#2.1-前端开发)以了解前端开发代码规范和开发环境的部署。

Envision 服务端采用基于 Python 的轻量级框架 [**Django**](https://www.djangoproject.com/)，同时基于[**Django REST framework**](https://www.django-rest-framework.org/) 构建API。如果你使用Python编程，并且熟悉或者想要使用`Django`框架进行前后端分离的Web应用开发，那么你可以考虑参与到 Envision 后端的开发进程中。查看 [【2.2 后端开发】](#2.2-后端开发)以了解后端开发代码规范和开发环境的部署。

如果你没有任何编程基础，但是想要参与到 Envision 的开发中，现在还为时未晚。点击上面的链接对我们采用的技术栈进行了解与学习，你将会很快地掌握一定的Web开发技能，并应用于实际项目的开发中。

### 1.2 反馈与报告

除了技术贡献外，你可以向我们提出 [Issue](https://github.com/AAIT-SUSE/Envision/issues) 。你可以使用 Issue 请求一项你想要加入到Envision中的功能、反馈一项有待改善的功能，或者反馈一项亟需解决的BUG。

查看[【3 Issue Tracker的使用规范】](#3-issue-tracker-的使用规范)以了解关于如何使用Issue的说明。

### 1.3 小额赞助

如果愿意，你也可以通过在 Envision 中的礼品店对 Envision 进行赞助。所有对 Envision 的赞助将由专人负责管理，并确保其不会被用于除了维护 Envision 和购置服务器之外的其他任何途径。

## 2 技术贡献规范

> 通过阅读这一部分内容，贡献者可以了解到如何在本地机器上安装和部署开发环境，并且运行 Envision 的开发版本。同时，这一部分也包含了我们对代码规范的要求。遵照**代码规范**书写代码有助于保证 Envision 项目的简洁和易读。

### 2.1 前端开发

#### 2.1.1 开发环境部署

Envision 客户端采用 [**vue.js**](https://cn.vuejs.org/index.html) 作为框架，采用 [**Vuetify**](https://vuetifyjs.com/zh-Hans/) 作为UI组件库。一个快速安装所有项目的方式是通过[**npm**](https://www.npmjs.com/)。npm是[**node.js**](https://nodejs.org/zh-cn/)的包管理工具。你可以点击前面的链接来了解node.js和npm。

安装node.js和npm到本地开发机器上后，你可以通过Git Clone克隆或者手动下载 Envision 的`dev`分支——即最新的开发分支——到你的本地机器中。

项目的`client`目录即是前端开发根目录。如果你熟悉或者使用过`npm`，你可以打开`client`目录下的`package.json`文件，查看 Envision 前端所使用的所有依赖包(Dependencies)。并且，你可以在此目录下运行

```bash
npm install
```

命令来安装它们。

一旦你的所有依赖全部安装完毕，你就可以尝试在此目录下运行

```bash
npm run serve
```

命令来在本地的开发环境中编译和运行 Envision 的开发版本。

#### 2.1.2 前端代码规范

**注意，任何参与客户端开发的贡献者所提交的代码片段均应当遵守此代码规范**。任何不符合此代码规范的 pull requests 将不会被接受。

- 所有的Vue组件，即`.vue`文件的命名不可以使用单个英文单词，且每个英文单词的首字母均应当大写。
- 在Vue组件中引入其他的组件时，标签名称采用英文小写，单词之间使用短横线`-`（Dash）隔开。
- Vue组件中`prop`的定义必须使用标注详细的数据类型。
- 不要将`v-for`和`v-if`用在同一个元素上。
- 为组件的样式`<style>`设置作用域（scope）
- 在每个页面上只使用一次的组件，即只拥有单个活跃实例的组件应当使用`The`作为命名前缀，以显示其唯一性。单例组件不接受任何`prop`。
- 组件命中的单词应当使用具有一般性描述的单词开头作为前缀，且与父组件耦合密切的子组件应当使用父组件的名字作为命名前缀。比如：

错误的例子

```bash
components/
|- TodoList.vue
|- TodoItem.vue
|- TodoButton.vue
|- ButtonSearchBar
|- InputSearchBar
```

正确的例子

```bash
components/
|- TodoList.vue
|- TodoListItem.vue
|- TodoListButton.vue
|- SearchBarButton
|- SearchBarInput
```

- 现代的编辑器和IDE都具有自动补全功能，书写长名词的代价非常低，因此禁止意义不明确的缩写。
- 更多的关于Vue的代码规范，请参看Vue官方的[风格指南](https://cn.vuejs.org/v2/style-guide/index.html)

### 2.2 后端开发

#### 2.2.1 开发环境搭建

Envision 的服务端采用 Python 语言。基于 Python 的 [**Django**](https://www.djangoproject.com/) 框架允许我们快速稳定地开发服务端程序。Envision 采用前后端分离的架构，后端的任务是提供API。借助 Django 的第三方扩展包 [**REST Framework**](https://www.django-rest-framework.org/) 可以很轻松地实现这一需求。

一个安装后端开发环境最简单的方法就是通过 Python 的包管理工具 [**pip**](https://pypi.org/project/pip/)进行安装。安装好pip后，启动控制台，运行下面的命令来安装后端的依赖环境：

```bash
pip install Django #安装 Django
pip install djangorestframework #安装 Django-Rest-Framework
```

一旦开发环境安装完成，你可以你可以通过Git Clone克隆或者手动下载 Envision 的`dev`分支——即最新的开发分支——到你的本地机器中。切换到`server`文件夹下，你就可以查看所有的服务器端文件了。你可以在`manage.py`同级目录下通过命令控制台运行命令：

```bash
python manage.py runserver
```

来在本地环境下编译和运行服务器端程序，并在本地查看效果。

#### 2.2.2 后端代码规范

- Python 类与类之间空 2 行。
- Python 文件结尾空 1 行。
- ...[*邓总补充* ]

### 3 Issue Tracker 的使用规范

[**Issue Tracker**](https://github.com/AAIT-SUSE/Envision/issues) 的用途在于提出 BUG 反馈、请求功能、提出建议等等。当你在使用 Issue Tracker 向我们提出一个 Issue 的时候，请务必遵守下面的规范：

- 请不要使用 Issue Tracker 提出关于 Envision 使用过程中出现的个人的问题，比如“发帖的时候如何改变标题颜色”等问题不适合在 Issue Tracker 中提出。此类问题请直接在 Envision 中发帖询问或者使用站内私信询问管理员。
- 在提出一个 Issue 前，请先使用 Issue Tracker 的搜索功能进行搜索，看看是不是已经有人提出了相同的问题。
- 当你想要提出 Issue 时，请在标题中大致描述问题。形如“求救！”，“看一下这里是不是有BUG”之类的标题不符合我们的规范，我们将保留删除 Issue 的权利。
- 不要在一个 Issue 中提出两个不相关的话题。相反，开启两个不同的 Issue 分别阐述两个话题会更好。
- 在同一个话题内的讨论不应当偏移到另外一个话题。当你在讨论中想要指代或引用另外一个 Issue 的时候，你可以使用 Github 的引用功能。
- 单纯的类似于“赞”，“+1”之类的回复将会被删除。请不姚发送这些回复。你可以使用 Github 的表情回应功能进行点赞或者点踩等操作。

