import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter);

const questions = () => import('@/views/Questions');
const question = () => import('@/views/Question');

const routes = [
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