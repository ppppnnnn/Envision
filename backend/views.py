from django.shortcuts              import       render
from django.http                   import       JsonResponse
from django.views.generic          import       View
from django_filters                import       rest_framework
from django.contrib.auth.hashers   import       hashlib
from django_filters.rest_framework import       DjangoFilterBackend
#----------------------------------------------------------------------------------------
from rest_framework                import       filters
from rest_framework.views          import       APIView
from rest_framework.response       import       Response
from rest_framework.decorators     import       api_view
from rest_framework                import       permissions,viewsets,renderers,generics,status,exceptions
#-----------------------------------------------------------------------------------------
import random
#导入序列化器
from .serializers import ArticleSerializer,ArticleCommentSerializer,ArticleCommentReplySerializer,AffairSerializer
from .serializers import SectionSerializer,PostSerializer,PostCommentSerializer,PostCommentReplySerializer
from .serializers import PostCommentReplySerializer,DirectAnswerSerializer,DirectAnswerAnswerSerializer,GroupSerializer
from .serializers import GroupActivitySerializer,GroupAnnouncementSerializer,LearningTaskSerializer,UserRegisterSerializer
from .serializers import UserLoginSerializer,ChangePasswordSerializer,ForgetPasswordSerializer,ResetPasswordSerializer
from .serializers import AdministratorsSerializer,AnnouncementSerializer,UserSerializer,UserAccountSerializer
from .serializers import GroupLearningTaskSerializer,GroupLearningTaskSubmitSerializer,GroupLearningMaterialsSerializer
#导入模型
from .models import Article,ArticleComment,ArticleCommentReply,Announcement,Section,Post,PostComment,PostCommentReply
from .models import Group,GroupActivity,GroupAnnouncement,DirectAnswer,DirectAnswerAnswer,User,UserAccount,UserToken
from .models import LearningTask,Administrators,GroupLearningTask,GroupLearningTaskSubmit,GroupLearningMaterials,Affair

#导入过权限组
from .permissions import IsAdminUser,IsOwnerOrReadOnly,IsGroupAdminUser

class AdministratorsViewSet(viewsets.ModelViewSet):
    queryset           =   Administrators.objects.all()
    serializer_class   =   AdministratorsSerializer
    permission_classes =   (IsAdminUser,)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset           =   Article.objects.all()
    serializer_class   =   ArticleSerializer
#   permission_classes =   (IsOwnerOrReadOnly,IsAdminUser,)
    filter_backends    =   (DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    filter_fields      =   ('author_id','author_name',)
    ordering_fields    =   ('create_time',)
    search_fields      =   ('^tag',)



class ArticleCommentViewSet(viewsets.ModelViewSet):
    queryset           =   ArticleComment.objects.all()
    serializer_class   =   ArticleCommentSerializer
#   permission_classes =   (IsOwnerOrReadOnly,IsAdminUser,)
    filter_backends    =   (DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields      =   ('article_id','author_id','author_name',)
    ordering_fields    =   ('create_time',)


class ArticleCommentReplyViewSet(viewsets.ModelViewSet):
    queryset           =   ArticleCommentReply.objects.all()
    serializer_class   =   ArticleCommentReplySerializer
#   permission_classes =   (IsOwnerOrReadOnly,IsAdminUser,)
    filter_backends    =   (DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields      =   ('article_id','comment_id','author_id','author_name',)
    ordering_fields    =   ('create_time',)


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset           =   Announcement.objects.all()
    serializer_class   =   AnnouncementSerializer
#   permission_classes =   (IsAdminUser,)
    filter_backends    =   (filters.OrderingFilter,)
    ordering_fields    =   ('create_time',)


class SectionViewSet(viewsets.ModelViewSet):
    queryset           =   Section.objects.all()
    serializer_class   =   SectionSerializer
#   permission_classes =   (IsAdminUser,)


class PostVieweSet(viewsets.ModelViewSet):
    queryset           =   Post.objects.all()
    serializer_class   =   PostSerializer
#   permission_classes =   (IsOwnerOrReadOnly,IsAdminUser,)
    filter_backends    =   (DjangoFilterBackend,filters.OrderingFilter,)   
    filter_fields      =   ('author_id','author_name','section_id',)
    ordering_fields    =   ('create_time',)


class PostCommentViewSet(viewsets.ModelViewSet):
    queryset           =   PostComment.objects.all()
    serializer_class   =   PostCommentSerializer
#   permission_classes =   (IsOwnerOrReadOnly,IsAdminUser,)
    filter_backends    =   (DjangoFilterBackend,filters.OrderingFilter,)  
    filter_fields      =   ('author_id','author_name','post_id',)
    ordering_fields    =   ('create_time',)


class PostCommentReplyViewSet(viewsets.ModelViewSet):
    queryset           =   PostCommentReply.objects.all()
    serializer_class   =   PostCommentReplySerializer
#   permission_classes =   (IsOwnerOrReadOnly,IsAdminUser,)
    filter_backends    =   (DjangoFilterBackend,filters.OrderingFilter,)   
    filter_fields      =   ('comment_id','post_id','author_id','author_name',)
    ordering_fields    =   ('create_time',)


class DirectAnswerViewSet(viewsets.ModelViewSet):
    queryset           =   DirectAnswer.objects.all()
    serializer_class   =   DirectAnswerSerializer
#   permission_classes =   (IsOwnerOrReadOnly,IsAdminUser,)
    filter_backends    =   (DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter,)   
    filter_fields      =   ('author_id','author_name',)
    ordering_fields    =   ('create_time',)
    search_fields      =   ('^tag',)


class DirectAnswerAnswerViewSet(viewsets.ModelViewSet):
    queryset           =   DirectAnswerAnswer.objects.all()
    serializer_class   =   DirectAnswerAnswerSerializer
#   permission_classes =   (IsOwnerOrReadOnly,IsAdminUser,)
    filter_backends    =   (DjangoFilterBackend,filters.OrderingFilter,)   
    filter_fields      =   ('direct_answer_id','author_id','author_name',)
    ordering_fields    =   ('create_time',)


class GroupViewSet(viewsets.ModelViewSet):
    queryset           =   Group.objects.all()
    serializer_class   =   GroupSerializer
#   permission_classes =   (IsAdminUser,)
    filter_backends    =   (filters.OrderingFilter,filters.SearchFilter,)
    ordering_fields    =   ('degree_of_activity',)
    search_fields      =   ('group_name',)   



class GroupActivityViewSet(viewsets.ModelViewSet):
    queryset           =   GroupActivity.objects.all()
    serializer_class   =   GroupActivitySerializer
#   permission_classes =   (IsAdminUser,)
    filter_backends    =   (DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter,)   
    filter_fields      =   ('group_id',)
    ordering_fields    =   ('start_time',)
    search_fields      =   ('topic',)


class GroupAnnouncementViewSet(viewsets.ModelViewSet):
    queryset           =   GroupAnnouncement.objects.all()
    serializer_class   =   GroupAnnouncementSerializer
#   permission_classes =   (IsAdminUser,)
    filter_backends    =   (DjangoFilterBackend,filters.OrderingFilter,)   
    filter_fields      =   ('group_id',)
    ordering_fields    =   ('create_time',)


class GroupLearningTaskViewSet(viewsets.ModelViewSet):
    queryset           =   GroupLearningTask.objects.all()
    serializer_class   =   GroupLearningTaskSerializer
#   permission_classes =   (IsGroupAdminUser,IsAdminUser,)
    filter_backends    =   (DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter,)
    filter_fields      =   ('group_id',)
    ordering_fields    =   ('start_time',)
    search_fields      =   ('topic',)


class GroupLearningTaskSubmitViewSet(viewsets.ModelViewSet):
    queryset           =   GroupLearningTaskSubmit.objects.all()
    serializer_class   =   GroupLearningTaskSubmitSerializer
#   permission_classes =   (IsAdminUser,IsGroupAdminUser,)
    filter_backends    =   (DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields      =   ('task_id','group_id',)
    ordering_fields    =   ('score',)


class GroupLearningMaterialsViewSet(viewsets.ModelViewSet):
    queryset           =   GroupLearningMaterials.objects.all()
    serializer_class   =   GroupLearningMaterialsSerializer
 #  permission_classes =   (IsOwnerOrReadOnly)
    filter_backends    =   (DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields      =   ('author_id','author_name','group_id',)
    ordering_fields    =   ('create_time',)


class LearningTaskViewSet(viewsets.ModelViewSet):
    queryset           =   LearningTask.objects.all()
    serializer_class   =   LearningTaskSerializer
#   permission_classes =   (IsOwnerOrReadOnly,IsAdminUser,)
    filter_backends    =   (DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter,)   
    filter_fields      =   ('author_id','author_name',)
    ordering_fields    =   ('start_time',)
    search_fields      =   ('^tag',)


class AffairViewSet(viewsets.ModelViewSet):
    queryset           =   Affair.objects.all()
    serializer_class   =   AffairSerializer
    filter_backends    =   (DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter,)
    filter_fields      =   ('goods_name','goods_owner','borrower','is_return',)
    ordering_fields    =   ('register_time',)
    search_fields      =   ('^goods_name',)


class UserViewSet(viewsets.ModelViewSet):
    queryset           =   User.objects.all()
    serializer_class   =   UserSerializer
    filter_backends    =   (DjangoFilterBackend,filters.OrderingFilter,) 
    filter_fields      =   ('username','real_name','major','e_class','dept','identity',)


class UserAccountViewSet(viewsets.ModelViewSet):
    queryset           =   UserAccount.objects.all()
    serializer_class   =   UserAccountSerializer
    filter_backends    =   (DjangoFilterBackend,) 
    filter_fields      =   ('uid',)


class UserRegisterAPIView(APIView):
    queryset           =   User.objects.all()
    serializer_class   =   UserRegisterSerializer

    # 重载GET方法
    def get(self,request,format=None):
        serializer    =   UserRegisterSerializer()
        return Response(serializer.data)

    #重载POST方法
    def post(self,request,format=None):
        data          =   request.data
        if User.objects.filter(e_mail=data.get('e_mail')):
            return Response('该邮箱已被注册',status=status.HTTP_400_BAD_REQUEST)
        elif User.objects.filter(username=data.get('username')):
            return Response('用户名已存在',status=status.HTTP_400_BAD_REQUEST)
        serializer    =   UserRegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            uid = User.objects.get(username=data.get('username')).uid
            context   =   {'msg':'Succeeded','id':uid}
            return JsonResponse(context)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    #---------------登录成功时为用户设置Token,返回并保存---------------
    queryset          =   User.objects.all()
    serializer_class  =   UserLoginSerializer

    #重载GET方法
    def get(self,request,format=None):
        serializer    =   UserLoginSerializer()
        return Response(serializer.data)

    #重载POST方法
    def post(self,request,format=None):
        data          =   request.data
        user          =   None
        try:
            try:
                user = User.objects.get(e_mail=data.get('email_or_username'))
            except:
                user = User.objects.get(username=data.get('email_or_username'))
            password = data.get('password')
            for i in range(2):
                password = hashlib.md5(password.encode('utf-8') + user.salt.encode('utf-8')).hexdigest()
            if password  == user.password:
                random_list = 'abdjcniejknmdkjdj'
                ch = ''
                for i in range(10):
                    ch += (list(random_list)[random.randint(0,16)])
                token = hashlib.md5(user.e_mail.encode('utf-8') + ch.encode('utf-8')).hexdigest()
                uid   = user.uid
                UserToken.objects.update_or_create(owner=user,defaults={'token':token})
                context = {'msg':'Succeeded','Token':token,'id':uid}
                return JsonResponse(context)
        except:
            return Response({'msg':'ERROR Incorrect username or password'},status=status.HTTP_400_BAD_REQUEST)



class ChangePasswordAPIView(APIView):
    #---------------An endpoint for changing password.-------------
    queryset          =   User.objects.all()
    serializer_class  =   ChangePasswordSerializer

    #获取请求对象
    def get_object(self,queryset=None):
        return self.request.user

    #重载GET方法
    def get(self,request,format=None):
        serializer    =   ChangePasswordSerializer()
        return Response(serializer.data)

    #重载POST方法
    def post(self,request,*args,**kwargs):
        self.object   =   self.get_object()
        serializer    =   ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({'msg':'Old password error'},status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            return Response({'msg':'Successful password modification'},status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



        
