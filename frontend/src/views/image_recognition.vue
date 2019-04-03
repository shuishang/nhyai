<template>
	<div id="imageRecognition">
		<Navigation></Navigation>
		<div class="top_contain">
			<el-row>
				<el-col :xs={span:24} :sm={span:11,offset:1} :md={span:10,offset:2} :lg={span:7,offset:4,pull:1} :xl={span:6,offset:5,pull:1}>
					<div class="show_title_outer">
						<h2>图片识别</h2>
						<p class="top_describe">南海云暴恐图片识别基于南海云平台领先的深度学习引擎，对用户上传的图片进行自动审核，暴恐识别算法会返回“疑似暴
							恐”的字段，对血腥、暴力等图片进行自动打击，用AI捍卫互联网安全，助力建立安全、健康的互联网环境。</p>
					</div>
				</el-col>

				<el-col :xs={span:20,offset:2} :sm={span:11,offset:1} :md="10" :lg="8" :xl="6">
					<div >
						<img class="top_image" src="../assets/image/1.gif" alt="">
					</div>
				</el-col>
			</el-row>
		</div>
		<div class="functional_experience">
			<h2 class="title">功能体验</h2>
			<el-row>
				<el-col :xs={span:24} :sm={span:22,offset:1} :md={span:20,offset:2} :lg={span:18,offset:3} :xl={span:16,offset:4}>
					<img src="../assets/image/load_image_top.jpg" class="show_top_sample">
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
							<input id="datafile" name="datafile" type="file" class="inputfile" @change="changeImage($event)">
							<div class="clearfix">
								<label for="datafile" class='choose_style fl'>上传图片</label>

								<input type="submit" class='choose_style fr' v-model="buttonWord" v-if="imageRight">
								<input type="button" class='choose_style_no fr' v-model="buttonWord" v-else>
							</div>
							<p type="text" class="show_url" v-show="imageName"><i class="show_left_aerrow">√</i>{{imageName}}</p>
						</form>
						<!--<p class="suggest">提示：图片大小不超过1M，请保证需要识别部分为图片主体部分</p>-->
						<!--<form action="http://10.10.43.114:8000/api/uploads/"method="post" enctype="multipart/form-data">
							<input type="file" id="datafile" name="datafile" class="inputfile" accept="image/*" @change="changeImage($event)"/>
							<label for="datafile" class='choose_style'>上传图片</label>
						</form>-->
						<p class="suggest">提示：图片大小不超过1M，请保证需要识别部分为图片主体部分 <span v-show="imageIsBig" style="color: red;margin-left: 10px;display: inline-block;">！该图片大小超过1M</span></p>
					</div>
				</el-col>
				<el-col :xs={span:24} :sm={span:11} :md="10" :lg="9" :xl="8">
					<div class="show_json_outer">
						<div id="show_json"></div>
					</div>
				</el-col>
			</el-row>
		</div>
		<div class="advantage_product">
			<h2 class="title">产品优势</h2>
			<el-row>
				<el-col :xs={span:24} :sm={span:22,offset:1} :md={span:20,offset:2} :lg={span:18,offset:3} :xl={span:16,offset:4}>
					<el-row align="left">
						<el-col :xs={span:24} :sm={span:12} :md={span:8} :lg={span:8} :xl={span:8} align="center">
							<i class="title_image"></i>
							<div style="padding: 14px;">
								<span>及时高效</span>
								<div class="describe_outer">
									<time class="good_describe">能够对用户上传的图片自动审核，主动发现潜在的暴恐图片，打击精度高，覆盖广，响应快</time>
								</div>
							</div>
						</el-col>
						<el-col :xs={span:24} :sm={span:12} :md={span:8} :lg={span:8} :xl={span:8} align="center">
							<i class="title_image_two"></i>
							<div style="padding: 14px;">
								<span>准确率高</span>
								<div class="describe_outer">
									<time class="good_describe">准确率可达97%以上，并通过智能的深度学习算法，不断学习错判样例，让系统变得更智能，更精准</time>
								</div>
							</div>
						</el-col>
						<el-col :xs={span:24} :sm={span:12} :md={span:8} :lg={span:8} :xl={span:8} align="center">
							<i class="title_image_three"></i>
							<div style="padding: 14px;">
								<span>解决方案成熟灵活</span>
								<div class="describe_outer">
									<time class="good_describe">承载每天数十亿张南海云内部业务图片的自动审核任务，经历过各种业务场景的长期充分验证</time>
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
							<i class="recommended_image_one"></i>
							<div style="padding: 14px;">
								<span>广告过滤</span>
								<div class="describe_outer">
									<time class="good_describe">利用机器自动滤除有暴恐风险的广告，大大节省网站运营人力</time>
								</div>
							</div>
						</el-col>
						<el-col :xs={span:24} :sm={span:12} :md={span:8} :lg={span:8} :xl={span:8} align="center">
							<i class="recommended_image_two"></i>
							<div style="padding: 14px;">
								<span>视频暴恐识别</span>
								<div class="describe_outer">
									<time class="good_describe">在直播平台、视频网站等实时检测视频流，自动处理掉大多数暴恐风险，保障平台健康</time>
								</div>
							</div>
						</el-col>
						<el-col :xs={span:24} :sm={span:12} :md={span:8} :lg={span:8} :xl={span:8} align="center">
							<i class="recommended_image_three"></i>
							<div style="padding: 14px;">
								<span>图片自动审核</span>
								<div class="describe_outer">
									<time class="good_describe">在海量UGC图片中准确迅速定位暴恐内容，告别传统人工审核时代</time>
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
            return {
                dialogImageUrl: 'https://yyb.gtimg.com/ai/assets/ai-demo/large/terror-17-lg.jpg',
                dialogVisible: false,
				jsonDemo:'{"ret":0,"msg":"ok","data":{"tag_list":[{"tag_name":"protest","probability":0.3087675468623638},{"tag_name":"violence","probability":0.017580988407135},{"tag_name":"sign","probability":0.795149803161621},{"tag_name":"photo","probability":0.0147841582074761},{"tag_name":"fire","probability":0.0184208210557699},{"tag_name":"police","probability":0.0153429144993424},{"tag_name":"children","probability":0.00931504089385271},{"tag_name":"group_20","probability":0.683478415012359},{"tag_name":"group_100","probability":0.207240253686904},{"tag_name":"flag","probability":0.122076518833637},{"tag_name":"night","probability":0.212110564112663},{"tag_name":"shouting","probability":0.0291868895292282}]}}',
				buttonWord:"开始检测",
				imageName:"",
                showPercent:"概率：1.75%",
				isForce:false,
                imageRight:false,
                imageIsBig:false

            };
        },
		components:{
            Navigation
		},
		watch:{

		},
		mounted:function () {
            var self = this;
//            $('#show_json').html(this.syntaxHighlight(this.jsonDemo));
            var jdata = JSON.stringify(JSON.parse(this.jsonDemo), null, 4);
//            console.log(jdata);//这是在输出框的json数据确实被格式话了
            $("#show_json").html("<pre>"+jdata+"</pre>");//这时数据展示正确

            $('form').submit(function(e) {
                self.imageRight = false;
                var formData = new FormData($(this));
                formData.append('datafile', $('#datafile')[0].files[0]);


                $.ajax({
                    url: $(this).attr('action'),
                    type: $(this).attr('method'),
                    data: formData,
//                    headers: {'Authorization': 'Token mytoken'},
                    cache: false,
                    contentType: false,
                    processData: false,
					success:(response)=>{

//                        this.uploadInfo(response);
                        console.log(this)
                        var result = response.result;
                        console.log( result.data.tag_list[1].probability,"hhhhhhhhhhhh") ;
                        var jdata = JSON.stringify(result, null, 4);
                        $("#show_json").html("<pre>"+jdata+"</pre>");//这时数据展示正确
                        var forcePercent = result.data.tag_list[1].probability.toString();
                        forcePercent = forcePercent.substring(0,forcePercent.indexOf(".")+5)*100;
                        console.log(forcePercent);
                        self.showPercent =`概率：${forcePercent}%`;

                        if(forcePercent>80){
                            self.isForce = true;
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
            update(e){
                let file = e.target.files[0];
                let param = new FormData($(this)); //创建form对象
                param.append('file',file);//通过append向form对象添加数据
                console.log(param.get('file')); //FormData私有类对象，访问不到，可以通过get判断值是否传进去
                let config = {
                    headers:{'Content-Type':'multipart/form-data'}
                }; //添加请求头
                this.$http.post('http://127.0.0.1:8081/upload',param,config)
                    .then(response=>{
                        console.log(response.data);

                    })
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

            /*selectFileManually.addEventListener('change', function(event){
            event.stopPropagation();
            event.preventDefault();
            axios.put('http://127.0.0.1:8000/api/v1/fileupload/', {
                    file: this.files[0]
                },{headers:{
                    'Content-Disposition': 'attachment; filename=this.files[0].name'
                }
                },
            ).then(resp => console.log(resp.data)).catch(err => console.log(err.response.data))
        }
    }
    })*/

			uploadImage(event){
                let reader =new FileReader();
                let img1=event.target.files[0];
                let type=img1.type;//文件的类型，判断是否是图片
                let size=img1.size;//文件的大小，判断图片的大小
                /*if(this.imgData.accept.indexOf(type) == -1){
                    alert('请选择我们支持的图片格式！');
                    return false;
                }*/
                if(size>3145728){
                    alert('请选择3M以内的图片！');
                    return false;
                }
                var uri = ''
                let form = new FormData();
                form.append('file',img1);
                form.append("result","123")
                this.$post('http://10.10.43.114:8000/api/uploads/',form,{
                    headers:{'Content-Type':'multipart/form-data'}
                	}).then((response) => {
                        console.log(response)
                    })
			},
        }
    }

</script>

<style scoped>
	.top_contain{background-color: #237EE6 ;min-height: 300px;margin-top: 110px;}
	.top_contain :after{content: '';width: 100%;height: 50px;background-image: url("../assets/image/top_back.png");background-position: 0 0;}
	.top_image{width: 100%;display: block;}
	.show_title_outer{padding: 40px 20px 40px;color: white;}
	.show_title_outer h1{}
	.top_describe{font-size: 16px;margin-top: 20px;line-height: 30px;}

	.functional_experience{}
	.functional_experience .title{text-align: center;color: #333333;margin: 40px 0;}

	.show_add_image_outer{min-height: 400px;}
	.show_top_sample{width: 100%;margin-bottom: 15px;}
	.show_json_outer{height: 400px;overflow-y:scroll;border: 1px solid #dddddd;}
	.show_add_image{height: 100%;margin: 0 auto;display: block;}
	.show_url{height: 33px; line-height: 33px;min-width: 100px;padding: 0 8px;}
	.show_left_aerrow{height: 15px;  width: 14px;  line-height: 15px;  color: rgb(255, 255, 255);  background-color: rgb(103, 194, 58);  border-radius: 50%;  display: inline-block;  padding: 3px;  margin-right: 5px;}
	.outer_add{width: 98%;height:350px;position: relative;overflow: hidden;}
	.choose_style{display:block;height: 35px; line-height: 35px;width: 40%;font-size: 15px;color: white;background-color: #237EE6;text-align: center;margin-right: 2.5%;cursor: pointer;}
	.choose_style_no{display:block;height: 35px; line-height: 35px;width: 40%;font-size: 15px;color: #999999;background-color: #dddddd;text-align: center;margin-right: 2.5%;}
	#show_json{width: 95%;margin: 0 auto;padding: 10px 5px;}
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
	.title_image{width: 67px; height: 67px;background-image: url("../assets/image/2.png");background-position: -470px -104px;display: inline-block;margin-top: 50px;}
	.title_image_two{width: 78px;  height: 67px;  background-image: url("../assets/image/2.png");  background-position: -392px -254px;display: inline-block;margin-top: 50px;}
	.title_image_three{width: 68px;  height: 65px;  background-image: url("../assets/image/2.png");  background-position: -302px -152px;;display: inline-block;margin-top: 50px;}
	.good_describe{font-size: 14px;color: gray;}
	.describe_outer{width: 80%;margin: 0 auto;text-align: left}

	.recommended_scenario{padding: 65px 0;overflow: hidden;background-color: #fff;}
	.recommended_scenario .title{text-align: center;color: #333333;margin: 50px 0;}
	.recommended_scenario span{display: inline-block;padding: 10px;}
	.recommended_image_one{width: 54px;height: 51px;background-image: url("../assets/image/2.png");background-position: -481px -185px;display: inline-block;margin-top: 50px;}
	.recommended_image_two{width: 50px;height: 51px;background-image: url("../assets/image/2.png");background-position: -474px -254px;;display: inline-block;margin-top: 50px;}
	.recommended_image_three{width: 50px;height: 51px;background-image: url("../assets/image/2.png");background-position: -302px -256px;display: inline-block;margin-top: 50px;}

</style>