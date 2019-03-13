import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter);


const activitynews = () => import('@/components/ActivityNews');
const activitynewsdetail = () => import('@/views/ActivityNewsDetail');
const announcementlist = () => import('@/components/AnnouncementList');
const announcementdetail = () => import('@/views/AnnouncementDetail');
const articleDetail = () => import('@/views/ArticleDetail');
const explore = () => import('@/views/Explore');
const exploreArticleList = () => import('@/components/ExploreArticleList');
const exploreDynamic = () => import('@/components/ExploreDynamic');
const exploreQuestionsList = () => import('@/views/Questions');
const forum = () => import('@/views/Forum');
const giftshop = () => import('@/views/GiftShop');
const group = () => import('@/views/Group');
const groupGeneralInfo = () => import('@/components/GroupGeneralInfo');
const groupMemberList = () => import('@/components/GroupMemberList');
const newArticle =() => import('@/views/NewArticle');
const newPost = () => import('@/views/NewPost');
const newQuestion = () => import('@/views/NewQuestion');
const person = () => import('@/views/Person');
const personArticleList = () => import('@/components/PersonArticleList');
const personAttention = () => import('@/components/PersonAttention');
// const personPostList = () => import('@/components/PersonPostList');
const personQuestions = () => import('@/components/PersonQuestions');
const personStudy = () => import('@/components/PersonStudy');
const postlist = () => import('@/views/PostList');
const postdetail = () => import('@/views/PostDetail');
const question = () => import('@/views/QuestionDetail');
const questions = () => import('@/views/Questions');
const shoppingdetail = () => import('@/views/ShoppingDetail');
const home = () => import('@/views/Home');

const routes = [
  {
    path: '/',
    component: home
  },
  {
    path: '/group',
    component: group,
    children: [
      {
        path: 'general',
        component: groupGeneralInfo
      },
      {
        path: 'members',
        component: groupMemberList
      },
    ]
  },
  {
    path: '/explore',
    component: explore,
    children: [
      {
        path: 'articlelist',
        component: exploreArticleList
      },
      {
        path: 'dynamic',
        component: exploreDynamic
      },
      {
        path: 'questionslist',
        component: exploreQuestionsList
      },
    ]
  },
  {
    path: '/article/:id',
    name: 'articleDetail',
    component: articleDetail
  },
  {
    path: '/articles/new',
    component: newArticle
  },
  {
    path: '/posts/new',
    component: newPost
  },
  {
    path: '/questions/new',
    component: newQuestion
  },
  {
    path: '/questions',
    name: 'questions',
    component: questions
  },
  {
    path: '/question/:id',
    name: 'questionDetail',
    component: question
  },
  {
    path: '/forum',
    component: forum
  },
  // {
  //   path: '/person',
  //   component: person,
  //   children: [
  //     {
  //       path: 'articlelist',
  //       component: personArticleList
  //     },
  //     {
  //       path: 'attention',
  //       component: personAttention
  //     },
  //     {
  //       path: 'postlist',
  //       component: personPostList
  //     },
  //     {
  //       path: 'questions',
  //       component: personQuestions
  //     },
  //     {
  //       path: 'study',
  //       component: personStudy
  //     }
  //   ]
  // },
  {
    path: '/announmentcelists',
    component: announcementlist
  },
  {
    path: '/activitynews',
    component: activitynews
  },
  {
    path: '/postlist/:id',
    component: postlist
  },
  {
    path: '/postdetail/:id',
    component: postdetail
  },
  {
    path: '/announcementdetail/:id',
    component: announcementdetail
  },
  {
    path: '/activitynewsdetail/:id',
    component: activitynewsdetail
  },
  {
    path: '/giftshop',
    component: giftshop
  },
  {
    path: '/shoppingdetail',
    component: shoppingdetail
  }
];

const router = new VueRouter({
  routes: routes
});

export default router;