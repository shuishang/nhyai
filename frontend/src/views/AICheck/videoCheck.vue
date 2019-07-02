<template>
	<div class="videoCheck">
		<!--视频评审-->
		<el-row style="min-width: 800px;margin-top: 30px;">
			<el-col :md={span:11,offset:2} :lg={span:11,offset:2} :xl={span:10,offset:4}>
				<div class="show_video_outer">
					<div class="show_video">
						{% load static %}
						<video id="video" src="{% static "../../assets/video/dragen_wind.mp4" %}" controls style="height: 100%;width: 100%;background-color: #333333"></video>
					</div>
					<div>

					</div>

				</div>
			</el-col>
			<el-col :md="6" :lg="6" :xl="4">
				<div class="video_result_outer">
					<p class="result_title">审查结果</p>
					<div class="result_outer">
						<p>暴恐识别</p>
						<p class="green_style_name">合规</p>
					</div>
					<div class="result_outer">
						<p>色情识别</p>
						<p class="green_style_name">合规</p>
					</div>
					<div class="result_outer">
						<p class="ell">政治敏感识别</p>
						<p class="orange_style_name">疑似违规</p>
					</div>
					<div class="result_outer">
						<p>公众人物识别</p>
						<p class="red_style_name">违规</p>
					</div>
					<div class="result_outer">
						<p>广告检测</p>
						<p class="red_style_name">违规</p>
					</div>
				</div>
			</el-col>
		</el-row>
		<el-row style="min-width: 800px;">
			<el-col :md={span:17,offset:2} :lg={span:17,offset:2} :xl={span:14,offset:4}>
				<div class="video_image_outer">
					<p>证据信息</p>
					<div class="video_image_con clearfix">
						<div class="video_image_item fl">
							<div class="show_result_title">
								<div></div>
								<span class="video_result_red_title">违规</span>
								<span class="video_result_red_number">95.62%</span>
							</div>
							<img src="../../assets/image/force_image_example.png" alt="">
							<p>视频时间：00:10:25</p>
						</div>
						<div class="video_image_item fl">
							<div class="show_result_title">
								<div></div>
								<span class="video_result_red_title">违规</span>
								<span class="video_result_red_number">95.62%</span>
							</div>
							<img src="../../assets/image/force_image_example.png" alt="">
							<p>视频时间：00:10:25</p>
						</div>
						<div class="video_image_item fl">
							<div class="show_result_title">
								<div></div>
								<span class="video_result_orange_title">疑似违规</span>
								<span class="video_result_orange_number">80.62%</span>
							</div>
							<img src="../../assets/image/force_image_example.png" alt="">
							<p>视频时间：00:10:25</p>
						</div>
						<div class="video_image_item fl">
							<div class="show_result_title">
								<div></div>
								<span class="video_result_red_title">违规</span>
								<span class="video_result_red_number">95.62%</span>
							</div>
							<img src="../../assets/image/force_image_example.png" alt="">
							<p>视频时间：00:10:25</p>
						</div>
						<div class="video_image_item fl">
							<div class="show_result_title">
								<div></div>
								<span class="video_result_orange_title">疑似违规</span>
								<span class="video_result_orange_number">80.62%</span>
							</div>
							<img src="../../assets/image/force_image_example.png" alt="">
							<p>视频时间：00:10:25</p>
						</div>
						<div class="video_image_item fl">
							<div class="show_result_title">
								<div></div>
								<span class="video_result_red_title">违规</span>
								<span class="video_result_red_number">95.62%</span>
							</div>
							<img src="../../assets/image/force_image_example.png" alt="">
							<p>视频时间：00:10:25</p>
						</div>
						<div class="video_image_item fl">
							<div class="show_result_title">
								<div></div>
								<span class="video_result_orange_title">疑似违规</span>
								<span class="video_result_orange_number">80.62%</span>
							</div>
							<img src="../../assets/image/force_image_example.png" alt="">
							<p>视频时间：00:10:25</p>
						</div>
					</div>
					<p class="choose_again">重新选择</p>
				</div>
				<p class="suggest"><span style="color: red">*</span> 提示: 敏感系数<50%为合规，50%～90%为疑似违规，>90%为违规<span v-show="imageIsBig" style="color: red;margin-left: 10px;display: inline-block;">！该图片大小超过1M</span></p>

			</el-col>
		</el-row>
	</div>
</template>

<script>
	export default {
        props:['stopVideo'],
	    data(){
	        return{
                imageIsBig:false
			}
		},
		mounted(){

		},
        watch: {
            stopVideo:(newVal,oldVal) => {
                console.log(newVal);
                if(newVal){
                    var myVideo = document.getElementById("video")
                    if(!myVideo.paused){
                        myVideo.pause();
					}

                }
            }
        },

		methods:{

		}
	}
</script>

<style scoped>
	/*视频样式begin*/
	.show_video_outer{height: 400px}
	.show_video{height:440px;position: relative;overflow: hidden;}

	.video_result_outer{height: 440px;z-index: 99;background-color: white;box-shadow:5px 0 20px #c5cff1}
	.video_result_outer .result_title{font-size: 24px;color: #000000;text-align: center;height: 100px;padding-top: 30px;}
	.video_result_outer .result_title:before{content: "";background: url("../../assets/image/result_top_image.png") no-repeat center center;height: 23px;display: block;margin-bottom: 10px;}
	.video_image_outer{border: 1px solid #e2ecfc;min-height: 200px;margin-top: 20px;padding-left: 20px;}
	.video_image_outer:first-child{color: #010101;font-size: 16px;line-height: 50px;}
	.video_image_con{}
	.video_image_item{height: 150px;width: 160px;padding-right: 20px;margin-bottom: 20px;position: relative;}
	.video_image_con .video_image_item img{height: 120px;width: 100%;display: block}
	.video_image_con .video_image_item p{height: 30px;line-height:30px;font-size: 14px;text-align: center;border: 1px solid #e2ecfc;border-top: none;}
	.show_result_title{position: absolute;height: 20px;font-size: 0;line-height: 0}
	.show_result_title span{;font-size: 14px;line-height: 20px;display: inline-block;vertical-align: top;}
	.show_result_title span:nth-of-type(2){background-color: white;padding: 0 5px;}
	.show_result_title span:nth-of-type(1){line-height: 22px;padding: 0 10px;}
	.video_result_red_number{color: #ff524a;border: 1px solid #ff524a;}
	.video_result_red_title{background-color: #ff524a;color: white;}
	.video_result_orange_number{color: #ffac09;border: 1px solid #ffac09;}
	.video_result_orange_title{background-color: #ffac09;color: white;}
	.choose_again{color: #333333;font-size: 16px;height: 42px;width: 120px;line-height: 42px;margin: 40px auto;border: 1px solid #e1e3e7;text-align: center;background-color: #fafcfe;cursor: pointer;}


	.show_json_outer .result_title{font-size: 24px;color: #000000;text-align: center;height: 100px;padding-top: 30px;}
	.show_json_outer .result_title:before{content: "";background: url("../../assets/image/result_top_image.png") no-repeat center center;height: 23px;display: block;margin-bottom: 10px;}
	.suggest{color: #b2b2b2;font-size: 14px;min-height: 30px;margin:8px 0;}

	.result_outer{margin: 20px 30px;display: flex;color: #000000;height: 28px;line-height: 28px;}
	.result_outer p:nth-of-type(1){font-size: 16px;flex: 5;margin-left: 10px;}
	.result_outer p:nth-of-type(2){font-size: 16px;flex: 3;text-align: center}
	.result_outer p:nth-of-type(3){font-size: 16px;flex: 4;text-align: center}
	.result_outer .green_style_name{background-color: #54cd62;border: 1px solid #54cd62;color: #fff}
	.result_outer .orange_style_name{background-color: #ffac09;border: 1px solid #ffac09;color: #fff}
	.result_outer .red_style_name{background-color: #ff524a;border: 1px solid #ff524a;color: #fff}


</style>