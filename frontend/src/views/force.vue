<template>
	<div id="force">
		<Navigation></Navigation>
		<div class="yellow_top_contain">
			<el-row>
				<el-row>
					<el-col :xl={span:24}>
						<img src="../assets/image/force/force_banner.png" alt="">
					</el-col>
				</el-row>
			</el-row>
		</div>
		<div class="functional_experience">
			<h2 class="title">功能介绍</h2>
			<div class="handwrite">
				<el-row>
					<el-col :xs={span:24} :sm={span:22,offset:1} :md={span:20,offset:2} :lg={span:18,offset:3} :xl={span:16,offset:4}>
						<p class="title_describe">智能识别含有宣扬恐怖主义、极端主义、血腥、政治游行等画面的暴恐及反动内容。暴恐识别模型更为严格，对涉嫌暴恐信息零容忍，为您的产品保驾护航，远离涉暴涉恐风险。</p>
						<div class="top_nav_image_outer">
							<img src="../assets/image/force/force_sample.png" alt="">
						</div>
					</el-col>
				</el-row>
			</div>
		</div>
		<div class="functional_experience">
			<h2 class="title">功能体验</h2>
			<el-row style="min-width: 800px;margin-top: 40px;">
				<el-col :xs={span:14} :sm={span:16} :md={span:14,offset:2} :lg={span:13,offset:2} :xl={span:11,offset:4}>
					<div class="show_input_outer">
						<input type="text" class="init_url_style">
						<p class="check_style">检测</p>
					</div>
				</el-col>
				<el-col :xs="10" :sm="8" :md="6" :lg="6" :xl="5">
					<div class="local_upload">
						<!--<p>本地上传</p>-->
						<input id="datafile" name="datafile" type="file" class="inputfile" @change="changeImage($event)">
						<label for="datafile">本地上传</label>
					</div>
				</el-col>
			</el-row>
			<el-row style="min-width: 800px;">
				<el-col :md={span:20,offset:2} :lg={span:20,offset:2} :xl={span:16,offset:4}>
					<p class="top_suggest">图片文件类型支持PNG、JPG、JPEG、BMP，图片大小不超过2M。</p>
					<div class="choose_image" v-show="!isImage">
						<div class="add_before">
							<!--<img src="../assets/image/yellow/image_upload.png" alt="">-->
							<!--<input id="imagefile" name="imagefile" type="file"  class="inputfile" @change="addImage($event)">
							<label for="imagefile"></label>-->
							<!--<el-upload
								action="https://jsonplaceholder.typicode.com/posts/"
								list-type="picture-card"
								:auto-upload="false"
								:on-preview="handlePictureCardPreview"
								:file-list="fileList"
								:on-change="onImageChange"
								:on-remove="handleRemove">
								<i class="el-icon-plus"></i>
							</el-upload>-->
							<el-upload
								class="avatar-uploader"
								action="https://jsonplaceholder.typicode.com/posts/"
								:auto-upload="false"
								:on-change="onImageChange">
								<i class="el-icon-plus avatar-uploader-icon"></i>
							</el-upload>
						</div>
						<p class="choose_suggest">支持图片多张上传，一次检测十张</p>
					</div>
					<div class="choose_image" v-show="isImage">
						<el-upload
							action="https://jsonplaceholder.typicode.com/posts/"
							list-type="picture-card"
							:auto-upload="false"
							:on-preview="handlePictureCardPreview"
							:file-list="fileList"
							:limit="10"
							:on-change="onImageChange"
							:on-remove="handleRemove">
							<i class="el-icon-plus"></i>
						</el-upload>
						<el-dialog :visible.sync="dialogVisible">
							<img width="100%" :src="dialogImageUrl" alt="">
						</el-dialog>
						<p class="begin_check">开始检测</p>
					</div>
				</el-col>
			</el-row>
		</div>
		<div class="recommended_scenario">
			<h2 class="title">应用场景</h2>
			<el-row>
				<el-col :xs={span:24} :sm={span:22,offset:1} :md={span:20,offset:2} :lg={span:18,offset:3} :xl={span:16,offset:4}>
					<div style="width: 70%;margin: 0 auto;">
						<el-carousel  type="card" height="250px"  trigger="click"><!--:interval="4000"-->
							<el-carousel-item v-for="(item,index) in recommendedList" :key="index">
								<img :src="item.imgUrl" alt="">
								<h3 class="medium">{{ item.imgUrl }}</h3>
							</el-carousel-item>
						</el-carousel>
					</div>

				</el-col>
			</el-row>
		</div>
		<div class="advantage_product">
			<h2 class="title">技术优势</h2>
			<el-row>
				<el-col :xs={span:24} :sm={span:22,offset:1} :md={span:20,offset:2} :lg={span:18,offset:3} :xl={span:16,offset:4}>
					<el-row align="left">
						<el-col :xs={span:24} :sm={span:12} :md={span:8} :lg={span:8} :xl={span:8} align="center" style="min-height: 250px;">
							<i class="title_image title_image_common"></i>
							<div class="show_advantage_describe">
								<span>准确率高</span>
								<div class="describe_outer">
									<p class="good_describe">目前准确率可达90%以上，基于智能的深度学习算法，准确度还将不断提高。</p>
								</div>
							</div>
						</el-col>
						<el-col :xs={span:24} :sm={span:12} :md={span:8} :lg={span:8} :xl={span:8} align="center" style="min-height: 250px;">
							<i class="title_image_two title_image_common"></i>
							<div class="show_advantage_describe">
								<span>及时高效</span>
								<div class="describe_outer">
									<p class="good_describe">能够对用户上传的图片自动审核，主动发现潜在的暴恐图片，打击精度高，覆盖广，响应快。</p>
								</div>
							</div>
						</el-col>
						<el-col :xs={span:24} :sm={span:12} :md={span:8} :lg={span:8} :xl={span:8} align="center" style="min-height: 250px;">
							<i class="title_image_three title_image_common"></i>
							<div class="show_advantage_describe">
								<span>灵活性定制</span>
								<div class="describe_outer">
									<p class="good_describe">根据用户审核平台需求，深度定制产品策略与解决方案。</p>
								</div>
							</div>
						</el-col>
					</el-row>
				</el-col>
			</el-row>
		</div>
		<FooterIndex></FooterIndex>
	</div>

</template>

<script>
	import Navigation from "../components/navigation.vue"
    import FooterIndex from "../components/footerIndex.vue"
    export default {
        data() {
			return{
                dialogImageUrl: "",
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
                clickFirst:0,
                fileList: [],
				isImage:false,
                imgUrl1:require('../../static/imgs/usage_image1.png'),
                imgUrl2:require('../../static/imgs/usage_image2.png'),
                imgUrl3:require('../../static/imgs/usage_image03.png'),
                recommendedList:[{'imgUrl':"../../static/imgs/usage_image1.png"},{'imgUrl':'../../static/imgs/usage_image2.png'},{'imgUrl':'../../static/imgs/usage_image03.png'}]
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
            console.log(this.recommendedList)
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
            onImageChange(file, fileList){
               this.fileList.push(file);
               console.log(file);
               if(!file.url){
                   file.url = URL.createObjectURL(file.raw);
			   }
               this.isImage = true;
			},
            addImage(e){
                var file = e.target.files[0];
                file.url = 'blob:http://localhost:8080/64f6d0fb-dfe1-45d9-bac6-9f8fe1758084'
                this.fileList.push(file);
                console.log(file)
                this.isImage = true;
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

            },
            handleRemove(file, fileList) {
                console.log(file, fileList);
            },
            handlePictureCardPreview(file) {
                this.dialogImageUrl = file.url;
                this.dialogVisible = true;
            }
        },
		components:{
            Navigation,
            FooterIndex
		},

    }

</script>

<style scoped>
	.yellow_top_contain{font-size: 0;line-height: 0;}
	.yellow_top_contain img{width: 100%;}
	.show_title_outer h1{}

	.functional_experience{margin: 50px 0;}
	.functional_experience .title{text-align: center;color: #000;margin: 40px 0 15px;font-size: 36px;}
	.functional_experience .title_describe{text-align: center;color: #000;font-size: 14px;width: 70%;margin: 0 auto 30px;}

	.top_nav_image_outer{margin-bottom: 15px;text-align: center;;}
	.top_nav_image_outer a{flex: 1;float: left;}
	.top_nav_image_outer a img{width: 100%;opacity: 0.6;cursor:pointer;}
	.top_nav_image_outer a .active{opacity: 1}

	.top_suggest{color: #999999;font-size: 14px;line-height: 40px;height: 30px;}
	.init_url_style{flex: 1;height: 35px;line-height: 35px;border: 1px solid #E2ECFC;font-size: 15px;padding-left: 10px;}
	.init_url_style:hover{border: 1px solid #C0C4CC;border-right: none;}
	.init_url_style:focus{border: 1px solid #409EFF;border-right: none;}
	.check_style{display:inline-block;height: 33px;line-height: 33px;font-size: 16px;color: #316DFF;border: 2px solid #316DFF;width: 100px;text-align: center;cursor:pointer;}
	.check_style:hover{background-color: #316DFF;color: white;}
	.local_upload{height: 33px;line-height: 33px;font-size: 16px;}
	.local_upload:before{content: "或";margin: 0 25px;}
	.inputfile{z-index: -11111;width: 0px;height:1px;opacity: 0;position: absolute;}
	.local_upload label{display:inline-block;height: 33px;line-height: 33px;font-size: 16px;background-color: #316DFF;color:white;border: 2px solid #316DFF;width: 100px;text-align: center;cursor: pointer;}
	.local_upload label:hover{background-color: white;color: #316DFF}
	.show_input_outer{display: flex;}
	.choose_image{border: 2px dashed #acc3ff;padding: 40px 0 40px 40px;position: relative;margin-top: 15px;min-height: 330px;}
	.add_before{width: 160px;height: 160px;margin: 50px auto 15px;}
	.add_before label{background: url("../assets/image/yellow/image_upload.png") no-repeat ;display: inline-block;height: 100px;width: 100px;background-size: 100px 100px;}
	.choose_suggest{text-align: center;font-size: 14px;color: #333;}
	.begin_check{width: 160px;height: 45px;line-height: 45px;background-color: #316dff;color: #ffffff;font-size: 16px;margin: 50px auto 0;text-align: center;}

	.advantage_product{padding: 65px 0 30px ;overflow: hidden;background-color: #f2f2f5;}
	.advantage_product .title{text-align: center;color: #000000;margin: 10px 0;font-size: 36px;}
	.advantage_product span{display: inline-block;padding: 10px;}
	.title_image_common{width: 70px; height: 70px;display: inline-block;margin-top: 50px;background-size: 70px 70px;}
	.title_image{background-image: url("../assets/image/yellow/yellow_advantage1.png");}
	.title_image_two{background-image: url("../assets/image/yellow/yellow_advantage2.png");}
	.title_image_three{background-image: url("../assets/image/yellow/yellow_advantage3.png");}
	.good_describe{font-size: 16px;color: #666666;line-height: 25px;text-align: center;}
	.describe_outer{width: 90%;margin: 0 auto;text-align: left}
	.show_advantage_describe{padding: 14px;}
	.show_advantage_describe span{font-size: 24px;color: #333333;}


	.recommended_scenario{padding: 50px 0 ;overflow: hidden;background-color: #fff;}
	.recommended_scenario .title{text-align: center;color: #000000;margin: 50px 0;font-size: 36px;}
	.recommended_scenario span{display: inline-block;padding: 10px;}
	.recommended_scenario img{width: 100%;height: 100%;}


</style>