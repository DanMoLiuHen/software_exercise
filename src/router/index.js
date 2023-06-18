import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '@/views/login/'
import Home from '@/views/home/'
import Layout from '@/views/layout/'

// 判断三角形
import Triangle from '@/views/triangle'
// 万年历
import Calendar from '@/views/calendar'
// 电脑销售系统
import Sales from '@/views/sales/'
// 电信收费
import Cash from '@/views/cash/'
// 15.ATM
import Fifteen from '@/views/fifteen/'
// 16.构建程序图
import Sixteen from '@/views/sixteen/'
// 17.销售系统
import Seventeen from '@/views/seventeen/'


Vue.use(VueRouter)

const routes = [
  {
    path:'/login',
    name:'login',
    component:Login
  },
  {
    path:'/',
    component:Layout,
    children:[
      {
        path:'',
        name:'home',
        component:Home
      },
      {
        path:'/cash',
        name:'cash',
        component:Cash
      },{
        path:'/triangle',
        name:'triangle',
        component:Triangle
      },
      {
        path:'/calendar',
        name:'calendar',
        component:Calendar
      },
      {
        path:'/sales',
        name:'sales',
        component:Sales
      },
      {
        path:'/fifteen',
        name:'fifteen',
        component:Fifteen
      },
      {
        path:'/sixteen',
        name:'sixteen',
        component:Sixteen
      },
      {
        path:'/seventeen',
        name:'seventeen',
        component:Seventeen
      }
    ]
  }
]

const router = new VueRouter({
  routes
})

const user = JSON.parse(window.localStorage.getItem('user'));
//导航守卫
// router.beforeEach((to,_,next) =>{
//   //校验非登录页面的登录状态
//   if(to.path !== '/login'){
//     if(user){
//       next();
//     }else{
//       next('./login');
//     }
//   }else{
//     //登录页面正常允许通过
//     next()
//   }
// })

export default router
