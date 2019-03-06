from django.contrib import admin
from .models import User,UserAccount,UserToken,Article,ArticleComment,ArticleCommentReply,GroupLearningTask
from .models import GroupAnnouncement,LearningTask,Section,Post,PostComment,PostCommentReply,GroupLearningTaskSubmit
from .models import Administrators,DirectAnswerAnswer,Announcement,Group,GroupActivity,DirectAnswer,GroupLearningMaterials
# Register your models here.

#-----------用户------------------------
admin.site.register(User)
admin.site.register(UserAccount)
admin.site.register(UserToken)

#-----------文章------------------------
admin.site.register(Article)
admin.site.register(ArticleComment)
admin.site.register(ArticleCommentReply)

#-----------群组------------------------
admin.site.register(Group)
admin.site.register(GroupLearningTask)
admin.site.register(GroupAnnouncement)
admin.site.register(GroupLearningTaskSubmit)
admin.site.register(GroupLearningMaterials)
admin.site.register(GroupActivity)

#-----------帖子------------------------
admin.site.register(Section)
admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(PostCommentReply)

#-----------直答-----------------------
admin.site.register(DirectAnswer)
admin.site.register(DirectAnswerAnswer)

#----------个人学习任务-----------------
admin.site.register(LearningTask)

#----------管理员---------------------
admin.site.register(Administrators)

#----------公告---------------------
admin.site.register(Announcement)


