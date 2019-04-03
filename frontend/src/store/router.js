
import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter);

//实现懒加载
const forceIndex=resolve=>require(['../views/force_index'],resolve);
const imageRecognition=resolve=>require(['../views/image_recognition'],resolve);

Vue.config.productionTip = false

//路由配置
const router = new VueRouter({
    mode: 'history',
    base: process.env.NODE_ENV === 'production'? '/force-project': '',
    linkActiveClass:'active',

    routes: [
        {path:'/forceIndex',meta:{title:'暴力识别',keepAlive:true},component:forceIndex},
        {path:'/imageRecognition',meta:{title:'暴力识别',keepAlive:true},component:imageRecognition},
        {path:'/',redirect:'/forceIndex'}
    ],

});

router.beforeEach((to, from, next) => {
    next();
    document.title=to.meta.title;
});

export default router;
