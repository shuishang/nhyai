<template>
	<div id="yellow">
		<Navigation></Navigation>
		<div class="top_contain">
			<el-row>
				<el-col :xs={span:24} :sm={span:11,offset:1} :md={span:10,offset:2} :lg={span:7,offset:4,pull:1} :xl={span:6,offset:5,pull:1}>
					<div class="show_title_outer">
						<h2>色情识别</h2>
						<p class="top_describe">依托腾讯领先的DeepEye图片鉴黄技术，准确快速输出每张目标图片属于“正常”、“性感”、
							“色情”的概率，有效帮助用户鉴别色情图片。该技术大幅提升了色情内容的打击覆盖面和打击效率，成倍地解放审核人力，
							助力网络环境更健康。
						</p>
					</div>
				</el-col>
				<el-col :xs={span:20,offset:2} :sm={span:8,offset:2} :md={span:7,offset:3} :lg={span:5,offset:4} :xl={span:4,offset:4}>
					<div >
						<img class="top_image" src="../assets/image/yellow/yellow_top.png" alt="">
					</div>
				</el-col>
			</el-row>
		</div>
		<div class="functional_experience">
			<h2 class="title">功能体验</h2>
			<div class="handwrite">
				<el-row>
					<el-col :xs={span:24} :sm={span:22,offset:1} :md={span:20,offset:2} :lg={span:18,offset:3} :xl={span:16,offset:4}>
						<div class="top_nav_image_outer">
							<a class="show_sm_image" href="javascript:void(0);" @click="clickImage(1)"><img src="../assets/image/yellow/y-1-sm.jpg" alt="" :class="{'active':currentImage===1}" ></a>
							<a class="show_sm_image" href="javascript:void(0);" @click="clickImage(2)"><img src="../assets/image/yellow/y-2-sm.jpg" alt="" :class="{'active':currentImage===2}"></a>
							<a class="show_sm_image" href="javascript:void(0);" @click="clickImage(3)"><img src="../assets/image/yellow/y-3-sm.jpg" alt="" :class="{'active':currentImage===3}"></a>
							<a class="show_sm_image" href="javascript:void(0);" @click="clickImage(4)"><img src="../assets/image/yellow/y-4-sm.jpg" alt="" :class="{'active':currentImage===4}"></a>
							<a class="show_sm_image" href="javascript:void(0);" @click="clickImage(5)"><img src="../assets/image/yellow/y-5-sm.jpg" alt="" :class="{'active':currentImage===5}"></a>
							<a class="show_sm_image" href="javascript:void(0);" @click="clickImage(6)"><img src="../assets/image/yellow/y-6-sm.jpg" alt="" :class="{'active':currentImage===6}"></a>
							<a class="show_sm_image" href="javascript:void(0);" @click="clickImage(7)"><img src="../assets/image/yellow/y-7-sm.jpg" alt="" :class="{'active':currentImage===1}" ></a>
							<a class="show_sm_image" href="javascript:void(0);" @click="clickImage(8)"><img src="../assets/image/yellow/y-8-sm.jpg" alt="" :class="{'active':currentImage===2}"></a>
							<a class="show_sm_image" href="javascript:void(0);" @click="clickImage(9)"><img src="../assets/image/yellow/y-9-sm.jpg" alt="" :class="{'active':currentImage===3}"></a>
							<a class="show_sm_image" href="javascript:void(0);" @click="clickImage(10)"><img src="../assets/image/yellow/y-10-sm.jpg" alt="" :class="{'active':currentImage===4}"></a>
							<a class="show_sm_image" href="javascript:void(0);" @click="clickImage(11)"><img src="../assets/image/yellow/y-11-sm.jpg" alt="" :class="{'active':currentImage===5}"></a>
							<a class="show_sm_image" href="javascript:void(0);" @click="clickImage(12)"><img src="../assets/image/yellow/y-12-sm.jpg" alt="" :class="{'active':currentImage===5}"></a>
						</div>
					</el-col>
				</el-row>
				<el-row>
					<el-col :xs={span:24} :sm={span:11,offset:1} :md={span:10,offset:2} :lg={span:9,offset:3} :xl={span:8,offset:4}>
						<div class="show_add_image_outer">
							<div class="outer_add">
								<img class="show_add_image" :src="dialogImageUrl">
								<div class="show_result_outer">
									<div class="show_result" v-if="isForce">
										<i class="show_word danger_result_back">恐暴</i>
										<p class="probability_number">{{showPercent}}</p>
									</div>
									<div class="show_result" v-else>
										<i class="show_word normal_result_back">正常</i>
										<p class="probability_number">{{showPercent}}</p>
									</div>
								</div>
							</div>
							<form action="http://10.10.43.114:8000/api/uploads/"
								  method="post"
								  enctype="multipart/form-data">
								<input id="datafile" name="datafile" type="file" class="inputfile" @change="changeImage($event)" v-if="!isLoading">
								<input class="inputfile" v-else>
								<div class="clearfix">
									<label for="datafile" class='choose_style fl' :disabled="!isLoading">上传图片</label>
									<input type="submit" class='choose_style fr' v-model="buttonWord" v-if="imageRight" >
									<input type="button" class='choose_style_no fr' v-model="buttonWord" v-else>
								</div>
								<p type="text" class="show_url" v-show="imageName"><i class="show_left_aerrow">√</i>{{imageName}}</p>
							</form>
							<p class="suggest">提示：图片大小不超过1M，请保证需要识别部分为图片主体部分 <span v-show="imageIsBig" style="color: red;margin-left: 10px;display: inline-block;">！该图片大小超过1M</span></p>
						</div>
					</el-col>
					<el-col :xs={span:24} :sm={span:11} :md="10" :lg="9" :xl="8">
						<div class="show_json_outer" v-loading="isLoading" element-loading-text="加载中..." >
							<div id="show_json"></div>
						</div>
					</el-col>
				</el-row>
			</div>

		</div>
		<div class="advantage_product">
			<h2 class="title">产品优势</h2>
			<el-row>
				<el-col :xs={span:24} :sm={span:22,offset:1} :md={span:20,offset:2} :lg={span:18,offset:3} :xl={span:16,offset:4}>
					<el-row align="left">
						<el-col :xs={span:24} :sm={span:12} :md={span:8} :lg={span:8} :xl={span:8} align="center" style="min-height: 250px;">
							<i class="title_image"></i>
							<div style="padding: 14px;">
								<span>及时高效</span>
								<div class="describe_outer">
									<time class="good_describe">能够主动发现潜在的涉黄图片，打击精度高，覆盖广，响应快，第一时间遏制涉黄图片的传播</time>
								</div>
							</div>
						</el-col>
						<el-col :xs={span:24} :sm={span:12} :md={span:8} :lg={span:8} :xl={span:8} align="center" style="min-height: 250px;">
							<i class="title_image_two"></i>
							<div style="padding: 14px;">
								<span>准确率高</span>
								<div class="describe_outer">
									<time class="good_describe">准确率可达99.9%以上，并通过不断学习错判样例，让模型更智能</time>
								</div>
							</div>
						</el-col>
						<el-col :xs={span:24} :sm={span:12} :md={span:8} :lg={span:8} :xl={span:8} align="center" style="min-height: 250px;">
							<i class="title_image_three"></i>
							<div style="padding: 14px;">
								<span>灵活定制</span>
								<div class="describe_outer">
									<time class="good_describe">
										基于系统输出的图片色情概率判断及其它用户信息，叠加使用定义的审核策略，灵活定制鉴黄方案</time>
								</div>
							</div>
						</el-col>
						<el-col :xs={span:24} :sm={span:12} :md={span:8} :lg={span:8} :xl={span:8} align="center" style="min-height: 250px;">
							<i class="title_image_four"></i>
							<div style="padding: 14px;">
								<span>节约成本</span>
								<div class="describe_outer">
									<time class="good_describe">

										24小时不间断服务，日审核图片过千万，可有效降低90%以上的人工审核成本</time>
								</div>
							</div>
						</el-col>
					</el-row>
				</el-col>
			</el-row>
		</div>

		<div class="recommended_scenario">
			<h2 class="title">推荐场景</h2>
			<el-row>
				<el-col :xs={span:24} :sm={span:22,offset:1} :md={span:20,offset:2} :lg={span:18,offset:3} :xl={span:16,offset:4}>
					<el-row align="left">
						<el-col :xs={span:24} :sm={span:12} :md={span:8} :lg={span:8} :xl={span:8} align="center">
							<div class="clearfix show_scenario_outer">
								<div class="fl left_image_con clearfix">
									<i class="recommended_image_one"></i>
								</div>
								<div class="fl right_word_con">
									<span>广告过滤</span>
									<div class="scenario_describe_outer">
										<span class="good_describe">
											利用机器自动滤除有色情风险的广告，大大节省网站运营人力
										</span>
									</div>
								</div>
							</div>
						</el-col>
						<el-col :xs={span:24} :sm={span:12} :md={span:8} :lg={span:8} :xl={span:8} align="center">
							<div class="clearfix show_scenario_outer">
								<div class="fl left_image_con clearfix">
									<i class="recommended_image_two"></i>
								</div>
								<div class="fl right_word_con">
									<span>视频鉴黄</span>
									<div class="scenario_describe_outer">
										<span class="good_describe">在直播平台、视频网站等实时检测视频流，自动处理掉大多数色情风险，保障平台健康</span>
									</div>
								</div>
							</div>
						</el-col>
						<el-col :xs={span:24} :sm={span:12} :md={span:8} :lg={span:8} :xl={span:8} align="center">
							<div class="clearfix show_scenario_outer">
								<div class="fl left_image_con clearfix">
									<i class="recommended_image_three"></i>
								</div>
								<div class="fl right_word_con">
									<span>图片审核</span>
									<div class="scenario_describe_outer">
										<span class="good_describe">在海量UGC图片中准确迅速定位不良内容，告别传统人工审核时代</span>
									</div>
								</div>
							</div>
						</el-col>
					</el-row>
				</el-col>
			</el-row>
		</div>

	</div>

</template>

<script>
	import Navigation from "../components/navigation.vue"
    export default {
        data() {
			return{
                dialogImageUrl: require("../assets/image/yellow/y-1.jpg"),
                dialogVisible: false,
                jsonDemo:'{"ret":0,"msg":"ok","data":{"tag_list":[{"tag_name":"protest","probability":0.3087675468623638},{"tag_name":"violence","probability":0.017580988407135},{"tag_name":"sign","probability":0.795149803161621},{"tag_name":"photo","probability":0.0147841582074761},{"tag_name":"fire","probability":0.0184208210557699},{"tag_name":"police","probability":0.0153429144993424},{"tag_name":"children","probability":0.00931504089385271},{"tag_name":"group_20","probability":0.683478415012359},{"tag_name":"group_100","probability":0.207240253686904},{"tag_name":"flag","probability":0.122076518833637},{"tag_name":"night","probability":0.212110564112663},{"tag_name":"shouting","probability":0.0291868895292282}]}}',
                buttonWord:"开始检测",
                imageName:"",
                showPercent:"概率：1.75%",
                isForce:false,
                imageRight:false,
                imageIsBig:false,
                activeName: 'first',
                showJson :{},
                options:{background:"rgba(0, 0, 0, 0.3)",fullscreen:false,target:document.querySelector(".show_json_outer")},
                currentImage:1,
                isLoading:false,
                clickFirst:0
			}
        },
        mounted:function () {
            var that = this;
            this.loadDate();
            var jdata = JSON.stringify(JSON.parse(this.jsonDemo), null, 4);
            $("#show_json").html("<pre>"+jdata+"</pre>");//这时数据展示正确
            $('form').submit(function(e) {
                that.imageRight = false;
                var formData = new FormData($(this));
                formData.append('datafile', $('#datafile')[0].files[0]);
                $.ajax({
                    url: $(this).attr('action'),
                    type: $(this).attr('method'),
                    data: formData,
                    cache: false,
                    contentType: false,
                    processData: false,
                    success:(response)=>{
                        var result = response.result;
                        console.log( result.data.tag_list[1].probability,"hhhhhhhhhhhh") ;
                        var jdata = JSON.stringify(result, null, 4);
                        $("#show_json").html("<pre>"+jdata+"</pre>");//这时数据展示正确
                        var forcePercent = result.data.tag_list[1].probability.toString();
                        forcePercent = forcePercent.substring(0,forcePercent.indexOf(".")+5)*100;
                        console.log(forcePercent);
                        that.showPercent =`概率：${forcePercent}%`;
                        if(forcePercent>80){
                            that.isForce = true;
                        }
                    },
                });
                e.preventDefault();
            });
        },
        methods: {
            uploadInfo(response){
                var result = response.result;
                console.log( result.data.tag_list[1].probability,"hhhhhhhhhhhh") ;
                var jdata = JSON.stringify(result, null, 4);
                $("#show_json").html("<pre>"+jdata+"</pre>");//这时数据展示正确
                var forcePercent = result.data.tag_list[1].probability.toString();
                forcePercent = forcePercent.substring(0,forcePercent.indexOf(".")+5)*100;
                console.log(forcePercent);
                this.showPercent =`概率：${forcePercent}%`;

                if(forcePercent>80){
                    this.isForce = true;
                }
            },
            changeImage(e){

                this.imageIsBig = false;
                this.imageRight = false;
                var file = e.target.files[0]
                var reader = new FileReader()
                var that = this
                reader.readAsDataURL(file);
                this.imageName = file.name;
                reader.onload = function(e) {
                    that.dialogImageUrl = this.result
                }
                let size=file.size;//文件的大小，判断图片的大小
                debugger;
                if(size>1048576){
                    this.imageIsBig = true;
                }else {
                    this.imageRight = true;
                }
            },
            clickImage(index){
                if(index!=this.currentImage){
                    this.currentImage =index;
                    this.dialogImageUrl = require(`../assets/image/yellow//y-${index}.jpg`);
                    if(this.clickFirst===0){
                        this.loadDate();
                    }
                }
            },
            loadDate() {
                this.isLoading = true;
                $(".show_sm_image").attr("disabled",true).css("pointer-events","none");
                console.log(this.clickFirst)
                if(this.clickFirst===0){
                    this.isLoading = true;
                    this.clickFirst+=1;
                    $("#show_json").html("");//这时数据展示正确
                    var intervalid1 = setTimeout(() => {
                        var jdata = JSON.stringify(JSON.parse(this.jsonDemo), null, 4);
                        $("#show_json").html("<pre>"+jdata+"</pre>");//这时数据展示正确
                        clearInterval(intervalid1);
                        this.isLoading = false;
                        $(".show_sm_image").attr("disabled",false).css("pointer-events","auto");
                        this.clickFirst = 0;
                    }, 4000)
                }

            }
        },
		components:{
            Navigation
		},

    }

</script>

<style scoped>
	.top_contain{background-color: #237EE6 ;min-height: 300px;margin-top: 110px;}
	.top_contain :after{content: '';width: 100%;height: 50px;background-image: url("../assets/image/top_back.png");background-position: 0 0;}
	.top_image{display: block;margin-top: 10px;}
	.show_title_outer{padding: 40px 20px 40px;color: white;}
	.show_title_outer h1{}
	.top_describe{font-size: 16px;margin-top: 20px;line-height: 30px;}

	.functional_experience{margin: 50px 0;}
	.functional_experience .title{text-align: center;color: #333333;margin: 40px 0;}

	.show_add_image_outer{min-height: 400px;}
	.top_nav_image_outer{margin-bottom: 15px;display: flex;}
	.top_nav_image_outer a{flex: 1;float: left;}
	.top_nav_image_outer a img{width: 100%;opacity: 0.6;cursor:pointer;}
	.top_nav_image_outer a .active{opacity: 1}
	.show_add_image{height: 100%;margin: 0 auto;display: block;}
	.show_url{height: 33px; line-height: 33px;min-width: 100px;padding: 0 8px;}
	.show_left_aerrow{height: 15px;  width: 14px;  line-height: 15px;  color: rgb(255, 255, 255);  background-color: rgb(103, 194, 58);  border-radius: 50%;  display: inline-block;  padding: 3px;  margin-right: 5px;}
	.outer_add{width: 98%;height:350px;position: relative;overflow: hidden;border: 1px solid #dddddd;}
	.choose_style{display:block;height: 35px; line-height: 35px;width: 40%;font-size: 15px;color: white;background-color: #237EE6;text-align: center;margin-right: 2.5%;cursor: pointer;border-radius: 5px;}
	.choose_style_no{display:block;height: 35px; line-height: 35px;width: 40%;font-size: 15px;color: #999999;background-color: #dddddd;text-align: center;margin-right: 2.5%;border-radius: 5px;}
	.show_json_outer{height: 400px;overflow-y:scroll;border: 1px solid #dddddd;}
	#show_json{margin: 50px auto;padding: 10px 30px;}
	#show_json p{height: 30px;line-height: 30px;}
	.inputfile{z-index: -11111;width: 0px;height:1px;opacity: 0;}
	.suggest{color: #b2b2b2;font-size: 14px;min-height: 30px;margin:8px 0;}
	.show_result_outer{width: 100%;height: 100%;position: absolute;top: 0;z-index: 1;text-align: center; background-color: rgba(0,0,0,.4);}
	.show_result_outer:before{content: '';position: absolute;left: 0;top: 0;width: 100%;height: 100%;}
	.show_result{ z-index: 3;display: inline-block;vertical-align: middle;margin-top: 15%}


	.advantage_product{padding: 65px 0;overflow: hidden;background-color: #f2f2f5;}
	.advantage_product .title{text-align: center;color: #333333;margin: 50px 0;}
	.advantage_product span{display: inline-block;padding: 10px;}
	.show_word{width: 192px;height: 148px;  display: inline-block;  text-align: center;  font-size: 22px;  font-style: normal;  color: #fff;  box-sizing: border-box;  padding-top: 58px;}
	.normal_result_back{background-image: url("../assets/image/2.png"); background-position: 0 0;}
	.danger_result_back{background-image: url("../assets/image/2.png"); background-position: -196px 0;}
	.probability_number{height: 30px;line-height: 30px;text-align: center;color: #fff;font-size: 16px;margin-top: 10px;}
	.title_image{width: 80px; height: 80px;background-image: url("../assets/image/yellow/product.yellow.png");background-position: -84px -408px;display: inline-block;margin-top: 50px;}
	.title_image_two{width: 80px;  height: 80px;background-image: url("../assets/image/yellow/product.yellow.png");background-position: 0 -408px;;display: inline-block;margin-top: 50px;}
	.title_image_three{width: 80px;  height: 80px;  background-image: url("../assets/image/yellow/product.yellow.png");  background-position: -453px -304px;display: inline-block;margin-top: 50px;}
	.title_image_four{width: 80px;  height: 80px;  background-image: url("../assets/image/yellow/product.yellow.png");  background-position: -392px -208px;display: inline-block;margin-top: 50px;}
	.good_describe{font-size: 14px;color: gray;}
	.describe_outer{width: 80%;margin: 0 auto;text-align: left}


	.recommended_scenario{padding: 65px 0;overflow: hidden;background-color: #fff;}
	.recommended_scenario .title{text-align: center;color: #333333;margin: 50px 0;}
	.recommended_scenario span{display: inline-block;padding: 10px;}
	.show_scenario_outer{margin-top: 15%;}
	.left_image_con{width: 30%;margin: auto 0;}
	.right_word_con{width: 70%;margin: auto 0;}
	.recommended_image_one{width: 56px;height: 56px;background-image: url("../assets/image/yellow/product.yellow.png");background-position: -476px -208px;display: inline-block;margin-top: 20px;margin-left: 35%;}
	.recommended_image_two{width: 50px;height: 51px;background-image: url("../assets/image/yellow/product.yellow.png");background-position: -257px -408px;display: inline-block;margin-top: 20px;margin-left: 35%;}
	.recommended_image_three{width: 56px;height: 56px;background-image: url("../assets/image/yellow/product.yellow.png");background-position: -311px -408px;display: inline-block;margin-top: 20px;margin-left: 35%;}
	.recommended_image_four{width: 56px;height: 56px;background-image: url("../assets/image/yellow/product.yellow.png");background-position: -302px -228px;display: inline-block;margin-top: 20px;margin-left: 35%;}
	.recommended_image_five{width: 56px;height: 56px;background-image: url("../assets/image/yellow/product.yellow.png");background-position: -302px -168px;display: inline-block;margin-top: 20px;margin-left: 35%;}
	.scenario_describe_outer{margin: 0 5px;text-align: left}
</style>