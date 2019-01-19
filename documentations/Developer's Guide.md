<h1 align=center>Envision v1.1.0a 开发手册</h1>
<p align=center>
<img src="https://img.shields.io/badge/version-1.1.0a-red.svg"> <img src="https://img.shields.io/badge/founder-Owen%20Tsai-orange.svg"> <img src="https://img.shields.io/badge/%E5%9B%9B%E5%B7%9D%E8%BD%BB%E5%8C%96%E5%B7%A5-AAIT-brightgreen.svg"> <img src="https://img.shields.io/badge/status-ReBuild%20in%20Progress-blue.svg">
</p>

> 本手册包含了 Envision v1.1.0a 版本的功能需求和开发时的约定与说明。请在开发开始之前阅读本手册。



<h3 align=center>- 目录 -</h3>
<p align=center>[名词约定](#名词约定)<br>[功能需求](#功能需求)<br>[字段用词规范](#字段用词规范)</p>

## 名词约定

- 视图（View）
视图指 Envision 的主要页面，包括主页、学习、论坛、发现、个人中心、系统设置等等。视图不是一个组件(component)，而是作为其他一些组件的容器。例如，论坛这个视图包含左侧的帖子列表组件，右侧的快捷按钮组件等等。

- 组件（Component）
组件指 Vue.js 中一般意义上的组件。一般情况下一个`.vue`文件就是一个组件。一个网页通常由很多个组件构成。

- 信息流（Feed）
信息流指的是 Envision 根据用户的喜好或者关注内容，在首页视图中推送给用户的内容。这些内容可能包括帖子（Post），文章（Article），直答（Direct Answer）或者公告（Announcement）等。

- 标签（Tag）
标签指的是用户根据自己喜好订阅的一个短语。例如用户订阅了“Web开发”这个标签，那么用户将会在 Envision 的推送上看到所有带有“Web开发”标签的内容。

- 帖子（Post）
帖子指的是 Envision 中论坛里发出的、归属于某一个论坛板块的、包含有标题与内容的UGC。帖子是完全由用户产生的，且允许其他用户对帖子进行回复和各种形式的讨论。

- 文章（Article）
文章指的是 Envision 中发出的、包含有标题与内容的UGC。文章也是完全由用户产生的内容，但是与帖子不同，文章没有特定的归属板块，但是含有一些标签用于区分文章主题。

- 直答（Direct Answer）
直答指的是 Envision 中由用户提出的、包含有问题和问题描述的UGC。直答是由用户提出的内容，且可以邀请指定的其他用户来回答该问题。直答没有特定的板块，但是提问者可以为每一个问题添加一些标签，用于区分问题的主题。

- 公告（Announcement）
公告指的是 Envision 中由管理员发出的、包含有标题和内容的UGC。公告将会出现在首页、群组页面或者用户的通知信息中。这取决于管理员对该公告的设置。

- 礼品店（Gift Shop）
即“商城”，用户可以使用积分在礼品店兑换礼物。

- *待添加 ...*

## 功能需求



- **注册与登录**。

 - 用户需要能够完成注册与登录功能，注册时不再需要填写个人身份信息。在注册完成后，个人身份信息可以在个人中心进行补全。**协会的干事干部则必须通过身份信息验证。**

 - 用户注册时可以从头像库随机 roll 头像。

 - 用户注册完成后自动登录系统。之后再次访问 Envision 时，除非用户手动注销账号活动，否则用户不需要再次登录即可访问系统。

 - 用户在注册的时候需要填写用户名，用户可以通过用户名或者邮箱进行登录。



- **论坛**。

 - 包含完整的论坛功能，用户可以浏览论坛中的任何帖子（Post），并在任何分区下发布帖子，或者在任何帖子下进行跟帖复。

 - 管理员可以对论坛进行管理。能够查找、删除帖子或论坛分区。

 - 在论坛的某个分区下，发布的帖子按照时间顺序倒序显示，即先显示最晚发布的帖子。



- **文章管理**。

 - 包含完整的文章管理功能。用户可以发表新文章，管理自己所发表的全部文章，并在任何文章下发表评论。

 - 管理员可以对文章进行管理。能够查找、删除文章和文章包含的评论。

 - 文章的作者可以对文章添加一系列标签，来指定文章的主题。例如作者可以为题目为《Vue.js 基础教程》的文章指定标签为“教程”，“vue.js”，“Web开发”，“Web前端开发”等等，方便对同一类文章感兴趣的用户可以更快看到该文章。

 - 管理员可以按照标签筛选和查找同一类别的所有文章。

 - 在文章视图，所有文章按照时间顺序倒序显示，即先显示最晚发布的文章。在探索视图，则根据用户订阅的标签显示符合筛选条件的文章。



- **直答。**

 - 包含提问与邀请回答功能。提问者提出问题，添加问题描述或者图片，为问题添加合适的标签标明主题之后，提问者还可以（也可以不）邀请其他 Envision 用户进行回答。被邀请的用户会收到通知。

 - 任何人都可以回答直答中列出的问题，但提问者邀请的回答者所给出的回答将会置顶显示在其他所有回答之上。

 - 如果提问者选择邀请其他用户回答自己提出的问题，且被邀请者做出了回答，那么提问者将会支付 20 积分给被邀请者。

 - 管理员可以查找、删除所有问题和问答。

 - 在直答视图，所有问题按照时间顺序倒序显示，即先显示最晚发布的问题。在探索视图，则根据用户订阅的标签显示符合筛选条件的问题。



- **公告管理。**

 - 包含发布公告的功能。公告只能由管理员发布，公告的标题将会显示在每个视图右侧的公告栏中。点击公告栏中某条公告的标题，将会弹出窗口显示改公告的详细内容。

 - 发布公告之后，管理员可以选择是否通过站内通知功能通知所有用户查看公告。

 - 公告的删除只能由 super-admin 进行。



- **信息流**。

 - 在首页视图中，信息流功能针对用户的兴趣和用户订阅的标签为用户筛选和显示合适的内容。

 - 在探索视图中，文章和直答将会根据用户订阅的标签为用户筛选和显示合适的内容。当用户点击“全部文章”或者“全部问题”按钮的时候，才展示全部的文章和问题。

 - 用户可以在设置中对自己订阅的标签进行管理，增加新的标签或者取消对某个标签的订阅。



- **设置**。

 - Envision (Web版) 左侧导航菜单中，默认的菜单项是“首页”、“学习”、“论坛”、“探索”、“个人中心”。完整的菜单项还有“创作”、“群组”、“礼品店”、“管理后台”、“社团事务”五项。用户可以在个人设置中对想要展示在左侧导航菜单中的菜单项进行设置，按照自己的喜好显示和隐藏部分菜单项。

 - 允许用户设置 Envision 的皮肤颜色（不重要功能）。

 - 允许用户管理自己订阅的标签，方便 Envision 对不同的用户进行个性化的内容推送。

 - 允许用户完善自己的个人身份信息。

 - 允许用户修改自己的账号信息。



- **学习视图**。

  - 包含 TODO List 的全部功能。可以添加一项任务、添加任务的详细描述、添加任务的截止日期、添加任务分类、完成、修改和删除任务等。

  - 可以添加学习目标，并查看他人的学习目标。

  - 可以开启“监督我”功能，将你的任务列表向全体 Envision 用户公开。



- **个人中心**。

 - 包含个人信息的展示，包括用户名、头像、身份、最近动态、学习目标等。

 - 包含快捷入口，比如修改信息、进入管理后台、查看、修改和删除自己发表的文章、帖子、直答等等。



- **群组**。

 - 群组视图中可以对全部群组进行浏览。管理员可以创建群组，并可以指定多个群组负责人。

 - 每一个群组拥有一个群组页面，所有群组成员可以在自己群组的页面看到群组公告、近期活动、学习资料、学习任务等，并且可以在线提交学习任务。

 - 群组的负责人可以在线浏览群组成员提交的学习任务，并进行评分。

 - 群组的负责人可以发布公告、发布近期活动、发布学习任务。

 - 任何群组成员均可上传学习资料。

 - 一个群组越活跃，则在群组视图中的排名就越高。



- ***待添加 ...***



## 字段用词规范



在前端和数据库中使用某些关键的字段时，请参照以下的名词表，以确保命名上的尽量统一，避免错误和不必要的麻烦。



username, 用户名, 即用户的昵称

password, 密码

password raw, 未加密的密码

salt, 加密使用的随机字符串

major, 专业

e class, 行政班级

dept, 协会部门

identity, 身份

admin, 管理员

avatar, 头像

real name, 真实姓名

user id 或者 uid，用户ID

email, 邮箱

author, 作者

last update time, 最近更新时间

forum, 论坛

section, 分区

group, 群组

content, 内容

topic, 标题

theme, 主题

tags, 标签(复数)



*待添加 ...*


