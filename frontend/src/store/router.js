
import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter);

//实现懒加载
const forceIndex=resolve=>require(['../views/force_index'],resolve);
const imageRecognition=resolve=>require(['../views/image_recognition'],resolve);
const idCard=resolve=>require(['../views/OCRRecognition/id_card'],resolve);
const drivingLicence=resolve=>require(['../views/OCRRecognition/driving_licence'],resolve);
const runningLicence=resolve=>require(['../views/OCRRecognition/running_licence'],resolve);
const commonUse=resolve=>require(['../views/OCRRecognition/common_use'],resolve);
const businessLicence=resolve=>require(['../views/OCRRecognition/business_licence'],resolve);
const bankCard=resolve=>require(['../views/OCRRecognition/bank_card'],resolve);
const handwriten=resolve=>require(['../views/OCRRecognition/handwriten'],resolve);
const carNumber=resolve=>require(['../views/OCRRecognition/car_number'],resolve);
const visitingCard=resolve=>require(['../views/OCRRecognition/visiting_card'],resolve);

Vue.config.productionTip = false

//路由配置
const router = new VueRouter({
    mode: 'history',
    base: process.env.NODE_ENV === 'production'? '': '',
    linkActiveClass:'active',

    routes: [
        {path:'/forceIndex',meta:{title:'暴力识别',keepAlive:true},component:forceIndex},
        {path:'/imageRecognition',meta:{title:'ORC识别'},component:imageRecognition,
            children:[
                {path:'idCard',meta:{title:'OCR识别'},component:idCard},
                {path:'drivingLicence',meta:{title:'OCR识别'},component:drivingLicence},
                {path:'runningLicence',meta:{title:'OCR识别'},component:runningLicence},
                {path:'commonUse',meta:{title:'OCR识别'},component:commonUse},
                {path:'businessLicence',meta:{title:'OCR识别'},component:businessLicence},//营业执照
                {path:'bankCard',meta:{title:'OCR识别'},component:bankCard},    //银行卡
                {path:'handwriten',meta:{title:'OCR识别'},component:handwriten},//手写体
                {path:'carNumber',meta:{title:'OCR识别'},component:carNumber},  //车牌
                {path:'visitingCard',meta:{title:'OCR识别'},component:visitingCard},  //名片
                {path:'/',redirect:'idCard'},
        ]},

        {path:'/',redirect:'/forceIndex'}
    ],

});

router.beforeEach((to, from, next) => {
    next();
    document.title=to.meta.title;
});

export default router;
