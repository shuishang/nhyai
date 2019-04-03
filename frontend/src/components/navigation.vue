<template>
	<div id="navigation" @mouseenter="mouseHover(this)" @mouseleave="mouseLeave(this)">
		<el-row>
			<el-col :xs={span:24} :sm={span:22,offset:1} :md={span:20,offset:2} :lg={span:18,offset:3} :xl={span:16,offset:4}>
				<div class="header_con clearfix">
					<a class="header_logo fl" href="www.rschn.com">
						<img :src="isNavHover?require('../assets/image/rsc_logo_white.png'):require('../assets/image/rsc_logo.png')">
					</a>
					<ul class="header_nav fl">
						<li><router-link to="/forceIndex"><span>暴恐识别</span></router-link></li>
						<li><router-link to="/imageRecognition"><span>OCR识别</span></router-link></li>
						<li><router-link to="/imageRecognition"><span>色情识别</span></router-link></li>
						<li><router-link to="/imageRecognition"><span>视频识别</span></router-link></li>

						<!--<li @mouseenter="headerNavHover($event)" @mouseleave="headerNavLeave">
							&lt;!&ndash; <a href="javascript:;"><span class="header_point">{{$t('title.city')}}</span></a> &ndash;&gt;
							<router-link to=""><span>新的开始</span></router-link>
							&lt;!&ndash;<ul class="header_nav_two">
								<li v-for="(item,index) in zhxcList">
									<router-link >{{item.title}}</router-link>
								</li>
							</ul>&ndash;&gt;
						</li>-->
					</ul>

				</div>
			</el-col>
		</el-row>

	</div>

</template>

<script>
	export default {
	    name:"navigation",
		data(){
	        return{
                activeIndex: '1',
				isNavHover:false
			}
		},
		methods:{
            handleSelect(key, keyPath) {
                console.log(key, keyPath);
            },
            //头部导航鼠标经过事件
            headerNavHover:function(event){
                $(".header_nav_two").hide();
                $(event.currentTarget).children(".header_nav_two").show();
            },
            headerNavLeave:function(){
                $(".header_nav_two").hide();
            },
            mouseHover(element){
                this.isNavHover = true;
			},
            mouseLeave(element){
                this.isNavHover = false;
			}
		}
	}

</script>

<style>
	#navigation{height:110px;position:fixed;top:0;width: 100%;z-index: 99;background-color: white;}
	#navigation :hover{background-color: #323232;}
	#navigation :hover .header_nav span{color: #fff;}
	#navigation :hover .header_logo img{/*display: inline-block;width: 133px;height: 58px;*/}

	/*头部样式*/
	/*.header_con{ width:1280px; height:110px;position:absolute;top:0;left:50%;margin-left:-640px;z-index:99;}*/
	.header_logo{ margin-top:26px;}
	.header_nav{ margin-left:88px;margin-right:30px;}
	.header_nav li{height:110px;line-height:110px;display:inline-block; /* display:table-cell;vertical-align:middle; */padding: 0 20px;position:relative;}
	.header_nav li a{display:block; /* display: table-cell;vertical-align: middle; */font-size:16px; color:#333;}
	.header_nav li a span{word-break:break-all;}
	/* .header_nav li a span.header_point{background:url(../assets/images/sindex/header_down_hover.png) no-repeat right center;padding-right:15px;} */
	/* .header_nav li a.active{height:107px;border-bottom: 3px solid #7fcd61;} */
	.header_nav li a:hover{height:107px;border-bottom: 3px solid #7fcd61!important;}
	/* .header_nav li:hover .header_nav_two{display:block;} */
	.header_nav_two{background-color:rgba(255, 255, 255, 0.9)!important;box-shadow:0px 6px 8px rgba(0,0,0,0.2); position:absolute;left:0;top:107px;border-top: 3px solid #7fcd61;display:none;}
	.header_nav_two li{height:46px;line-height: 46px;display:block;padding:0;}
	.header_nav_two li a{/* min-width:110px; */height:46px;line-height: 46px;display:block;font-size:14px;color:#555 !important;padding:0 30px;white-space:nowrap;text-align:center;}
	.header_nav_two li a:hover{height:46px;border-bottom:none;color: #fff !important;background-color:#7fcd61!important;}
	.header_nav_two li a.active{height:46px;border-bottom:none;}
	.header_link{height:110px;line-height:110px;padding-right:60px;position:relative;}
	.header_link p a{font-size:14px;color:#3488ea;}
	.header_link ul{height:36px;overflow:hidden;background:url("../assets/image/load_image_top.jpg") no-repeat 40px 17px;position:absolute;top:37px;right:0;z-index:99;cursor:pointer;border:1px solid transparent;}
	.header_link ul li{height:36px;line-height:36px;text-align:center;font-size:14px;color:#c8c8c8;padding-right:17px;padding-left:5px; }
	.header_link ul.active{height:auto;background:#fff url("../assets/image/load_image_top.jpg") no-repeat 40px 17px; border:1px solid #eee;}
	.header_link ul.active li{color:#333;}
	.header_fixed .header_nav li a{color:#fff;}
	/* .header_fixed .header_nav li a span.header_point{background:url(../assets/images/sindex/header_down_white.png) no-repeat right center;} */
	.header_fixed .header_link p a{color:#fff;}
	.header_nav li a .ru_menu_list{width:100%;height:0;line-height:50px;text-align:center;border-top:none; box-shadow: 0 13px 16px 0px rgba(0, 0, 0, 0.03);background-color:#fff; overflow:hidden; position:fixed;left:0;top:110px;z-index:99;transition:height 0.5s ease;}
	.header_nav li a .ru_menu_list a{font-size:16px; color:#333;margin:0 20px;display:inline-block;vertical-align: top;}
	.header_nav li a .ru_menu_list a:hover{color:#3488ea;height:auto;border-bottom:none;}
	.header_nav li a .ru_menu_list a.active{color:#3488ea;height:auto;border-bottom:none;}
	.ru_menu:hover .ru_menu_list{height:50px;border-top:1px solid #eaeaea;}

</style>