import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter);

const group = () => import('@/views/Group');
const newArticle =() => import('@/views/NewArticle');
const newPost = () => import('@/views/NewPost');
const newQuestion = () => import('@/views/NewQuestion');
const question = () => import('@/views/Question');
const questions = () => import('@/views/Questions');


const routes = [
  {
    path: '/',
    component: group,
    children: [
      {
        path: ''
      }
    ]
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
  }
];

const router = new VueRouter({
  routes: routes
});

export default router;