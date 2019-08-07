<template>
	<div id="sindex">
		<Navigation></Navigation>
		<div class="top_contain">
			<el-row>
				<el-row>
					<el-col :xl={span:24}>
						<img src="../assets/image/image_banner.png" alt="">
					</el-col>
				</el-row>
			</el-row>
		</div>
		<div class="functional_experience">
			<p class="title">功能体验</p>

			<el-row style="min-width: 800px;">
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
					<p class="top_suggest">支持图片格式：PNG、JPG、JPEG，大小限制<2M。支持视频格式：mkv 、mp4 、avi 、mov，大小限制<50M；</p>
				</el-col>
			</el-row>

			<!--图片评审-->
			<ImageCheck v-show="checkType ===1"></ImageCheck>

			<!--视频评审-->
			<VideoCheck :stopVideo="stopVideo" v-show="checkType ===2"></VideoCheck>

			<!--音频评审-->
			<AudioCheck :stopAudio="stopAudio" v-show="checkType ===3"></AudioCheck>

		</div>
		<div class="functional_experience">
			<p class="title">历史记录</p>
			<el-row style="min-width: 800px;">
				<el-col :md={span:20,offset:2} :lg={span:20,offset:2} :xl={span:16,offset:4}>
					<div class="show_search_con">
						<span>上传时间</span>
						<el-date-picker
							v-model="beginDate"
							type="date"
							placeholder="起始日期">
						</el-date-picker>
						<span>-</span>
						<el-date-picker
							v-model="endDate"
							type="date"
							placeholder="截止日期">
						</el-date-picker>
						<input type="text" class="search_input">
						<span class="search_btn">查询</span>
					</div>
					<table border="0" width="100%">
						<tr class="show_history_title">
							<th>文件名</th>
							<th>审查结果</th>
							<th>敏感类型</th>
							<th>敏感系数</th>
							<th>文本</th>
							<th>上传时间</th>
							<th>预览</th>
						</tr>
						<tr class="show_history_con">
							<td class="ell">imadef.jpg</td>
							<td class="red_color">违规</td>
							<td class="ell">暴恐识别、色情识别、其他识别</td>
							<td >92.243%</td>
							<td class="ell">文本内容占位字符...</td>
							<td class="ell">2019-03-04 20:29:33</td>
							<td  @click="centerDialogVisible = true">预览</td>
						</tr>
						<tr class="show_history_con">
							<td class="ell">imadef.jpg</td>
							<td class="orange_color">疑似违规</td>
							<td class="ell">暴恐识别、色情识别、其他识别</td>
							<td >92.243%</td>
							<td class="ell">文本内容占位字符...</td>
							<td class="ell">2019-03-04 20:29:33</td>
							<td  @click="centerDialogVisible = true">预览</td>
						</tr>
						<tr class="show_history_con">
							<td class="ell">imadef.jpg</td>
							<td class="green_color">合规</td>
							<td class="ell">暴恐识别、色情识别、其他识别</td>
							<td >92.243%</td>
							<td class="ell">文本内容占位字符...</td>
							<td class="ell">2019-03-04 20:29:33</td>
							<td  @click="centerDialogVisible = true">预览</td>
						</tr>
					</table>
					<div class="show_pagination">
						<el-pagination
							background
							:prev-text="prevText"
							:next-text="nextText"
							layout="prev, pager, next"
							:total="1000">
						</el-pagination>
					</div>
					<el-dialog
						:visible.sync="centerDialogVisible"
						width="60%"
						center>
						<div class="image_con">
							<img src="../assets/image/prelook_image.png">
						</div>
						<div class="pre_result_con">
							<table width="100%" cellspacing="0" cellpadding="0">
								<tr class="pre_item">
									<td class="pre_item_common">文件名称</td>
									<td>imadef.jpg</td>
								</tr>
								<tr class="pre_item">
									<td class="pre_item_common">上传时间</td>
									<td>2019/09/09    09:20:22</td>
								</tr>
								<tr class="pre_item">
									<td class="pre_result_item">审查结果</td>
									<td>
										<div class="clearfix">
											<div class="result_outer result_outer_notop fl">
												<p>暴恐识别</p>
												<p class="green_style_name">合规</p>
												<p class="green_style_number">12.35%</p>
											</div>
											<div class="result_outer result_outer_notop left_50 fl">
												<p>政治敏感识别</p>
												<p class="green_style_name">合规</p>
												<p class="green_style_number">12.56%</p>
											</div>
										</div>
										<div class="clearfix">
											<div class="result_outer fl">
												<p class="ell">色情识别</p>
												<p class="orange_style_name">疑似违规</p>
												<p class="orange_style_number">60.35%</p>
											</div>
											<div class="result_outer left_50 fl" >
												<p>公众人物识别</p>
												<p class="red_style_name">违规</p>
												<p class="red_style_number">90.35%</p>
											</div>
										</div>
										<div class="clearfix">
											<div class="result_outer fl">
												<p>广告检测</p>
												<p class="red_style_name">违规</p>
												<p class="red_style_number">90.16%</p>
											</div>
										</div>


									</td>
								</tr>
								<tr class="pre_item">
									<td class="pre_word_item">文本识别</td>
									<td>合规</td>
								</tr>
							</table>
						</div>

					</el-dialog>
				</el-col>
			</el-row>
		</div>
		<FooterIndex></FooterIndex>
	</div>

</template>

<script>
	import Navigation from "../components/navigation.vue"
	import FooterIndex from "../components/footerIndex.vue"
	import ImageCheck from '../views/AICheck/imageCheck.vue'
	import AudioCheck from '../views/AICheck/AudioCheck.vue'
	import VideoCheck from '../views/AICheck/videoCheck.vue'
    export default {
        data() {
            return {
                dialogImageUrl: require("../assets/image/sample_image.png"),
                dialogVisible: false,
				jsonDemo:'{"ret":0,"msg":"ok","data":{"tag_list":[{"tag_name":"protest","probability":0.3087675468623638},{"tag_name":"violence","probability":0.017580988407135},{"tag_name":"sign","probability":0.795149803161621},{"tag_name":"photo","probability":0.0147841582074761},{"tag_name":"fire","probability":0.0184208210557699},{"tag_name":"police","probability":0.0153429144993424},{"tag_name":"children","probability":0.00931504089385271},{"tag_name":"group_20","probability":0.683478415012359},{"tag_name":"group_100","probability":0.207240253686904},{"tag_name":"flag","probability":0.122076518833637},{"tag_name":"night","probability":0.212110564112663},{"tag_name":"shouting","probability":0.0291868895292282}]}}',
				buttonWord:"开始检测",
                showPercent:"概率：1.75%",
				isForce:false,
                imageRight:false,
                imageIsBig:false,
                options:{background:"rgba(0, 0, 0, 0.3)"},
				beginDate:'',
				endDate:'',
                prevText:'上一页',
                nextText:'下一页',
				checkType:1,
                stopVideo:false,
                stopAudio:false,
                centerDialogVisible: false
            };
        },
		components:{
            Navigation,
            FooterIndex,
            ImageCheck,
            AudioCheck,
            VideoCheck
		},
		watch:{

		},
		mounted:function () {

        },
        methods: {
            uploadImage(e){
                this.loading = this.$loading(this.options);
                this.imageRight = false;
                var formData = new FormData($(this));
                formData.append('datafile1', $('#datafile')[0].files[0]);
                $.ajax({
//                    url: "http://172.31.11.171:8000/api/uploads/",
                    url: "http://172.31.4.7:8000/api/violence_object/",
                    type: "post",
                    data: formData,
//                    headers: {'Authorization': 'Token mytoken'},
                    cache: false,
                    contentType: false,
                    processData: false,
                    success:(response)=>{
                        this.$loading().close();
//                        this.uploadInfo(response);
                        console.log(this)
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
                });
                e.preventDefault();
			},
            uploadInfo(response){
                var result = response.result;
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
                const file = e.target.files[0];
                const reader = new FileReader();
                const that = this;
                reader.readAsDataURL(file);
                reader.onload = function() {
                    that.dialogImageUrl = this.result;
                    const fileType = file.type;
                    if(fileType.substr(0, 5) === "image"){
                        that.checkType = 1;
                        that.stopVideo = true;
                        that.stopAudio = true;
                    }else if(fileType.substr(0, 5) === "audio"){
                        that.checkType = 3;
                        that.stopVideo = true;
                        that.stopAudio = false;
					}else if(fileType.substr(0, 5) === "video"){
                        that.checkType = 2;
                        that.stopVideo = false;
                        that.stopAudio = true;
					}

                };
                let size=file.size;//文件的大小，判断图片的大小
                if(size>1048576){
                    this.imageIsBig = true;
                }else {
                    this.imageRight = true;
                    this.uploadImage(e);
				}
			},
        }
    }

</script>

<style scoped>
	@import "../assets/css/audio.css";
	.top_contain img{width: 100%;}
	.functional_experience{margin: 50px 0;}
	.functional_experience .title{text-align: center;color: #333333;margin: 40px 0;font-size: 36px;}



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


	.show_search_con{height: 34px;line-height: 34px;padding-left: 20px;letter-spacing:0;font-size:0px;margin-bottom: 10px;}
	.show_search_con >span:first-child{color: #000000;font-size: 14px;padding: 10px;}
	.show_search_con >span:nth-of-type(2){color: #000000;font-size: 14px;padding: 10px;}
	.search_input{height: 32px;width:315px;line-height: 32px;border: 1px solid #E2ECFC;font-size: 15px;padding-left: 10px;margin-left: 20px;}
	.search_input:hover{border: 1px solid #C0C4CC;}
	.search_input:focus{border: 1px solid #409EFF;}
	.search_btn{display:inline-block;height: 32px;line-height: 32px;font-size: 14px;background-color: #316DFF;color:white;border: 1px solid #316DFF;width: 80px;text-align: center;cursor: pointer;}
	.search_btn:hover{background-color: white;color: #316DFF}

	.show_history_title{height: 50px;line-height: 50px;color: #333333;font-size: 16px;background-color: #ebeff8;width: 100%;display: flex;font-weight: 100;border: 1px solid #ebeff8;}
	.show_history_title th{flex: 1;text-align: left;padding-left: 10px;font-weight: 100;}
	.show_history_title th:last-child{flex: 1;text-align: center}
	.show_history_title th:first-child{padding-left: 20px;flex: 2;}
	.show_history_title th:nth-of-type(3){flex: 2.5;}
	.show_history_title th:nth-of-type(6){flex: 2;}
	.show_history_title th:nth-of-type(5){flex: 2.5;}
	.show_history_con{height: 50px;line-height: 50px;color: #333333;font-size: 14px;background-color: #fff;width: 100%;display: flex;border: 1px solid #e3e8f3;border-top: none;}
	.show_history_con td{flex: 1;text-align: left;padding-left: 10px;}
	.show_history_con td:last-child{flex: 1;text-align: center;color: #85afff;cursor: pointer;}
	.show_history_con td:first-child{padding-left: 20px;flex: 2;}
	.show_history_con td:nth-of-type(3){flex: 2.5;}
	.show_history_con td:nth-of-type(6){flex: 2;}
	.show_history_con td:nth-of-type(5){flex: 2.5;}
	.orange_color{color: #ffac09;}
	.red_color{color: #ff524a;}
	.green_color{color: #54cd62;}

	/*预览begin*/
	.image_con{text-align: center;}
	.image_con img{width: 100%;}
	.pre_result_con{padding: 30px 30px 40px;}
	.pre_result_con td{border: 1px solid #e3e8f3;height: 46px;}
	.pre_item{width: 100%;}
	.pre_item td:last-child{padding-left: 20px;}
	.pre_item td:first-child{width: 140px;text-align: center;background-color: #eaf1f6;}
	.pre_item_common{height: 46px;line-height: 46px;}
	.pre_result_item{height: 175px;line-height: 175px;}
	.pre_word_item {height: 150px;line-height: 150px;}
	.result_outer{margin: 25px 20px 0 0;display: flex;color: #000000;height: 25px;line-height: 25px;width: 35%;}
	.result_outer_notop{margin-top: 0;}
	.result_outer div:first-child{margin-top: 0;}
	.result_outer p:nth-of-type(1){font-size: 14px;margin:0 15px 0 0;}
	.result_outer p:nth-of-type(2){font-size: 14px;flex: 3;text-align: center;line-height: 23px;height: 23px;}
	.result_outer p:nth-of-type(3){font-size: 14px;flex: 4;text-align: center}
	.result_outer .green_style_name{background-color: #54cd62;border: 1px solid #54cd62;color: #fff}
	.result_outer .green_style_number{border: 1px solid #54cd62;color: #54cd62}
	.result_outer .orange_style_name{background-color: #ffac09;border: 1px solid #ffac09;color: #fff}
	.result_outer .orange_style_number{border: 1px solid #ffac09;color: #ffac09}
	.result_outer .red_style_name{background-color: #ff524a;border: 1px solid #ff524a;color: #fff}
	.result_outer .red_style_number{border: 1px solid #ff524a;color: #ff524a}
	.left_50{margin-left: 50px;}


	.show_pagination{text-align: center;margin-top: 30px;}
</style>