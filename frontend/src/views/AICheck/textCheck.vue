<template>
	<div class="textCheck">
		<!--音频评审-->
		<el-row style="min-width: 800px;margin-top: 30px;">
			<el-col :md={span:14,offset:2} :lg={span:13,offset:2} :xl={span:11,offset:4}>
				<div class="show_voice_outer">
					<div class="outer_text">
						<p class="voice_title">文本审查</p>
						<div class="voice_result_outer">
							<div class="show_text_word">
								<!--<span class="fl"> 1:05 - 1:06</span>-->
								<!--<span class="fl ell"> 好，现在<span class="red_color">违禁词</span>到室当中呢，<span class="red_color">违禁词</span>了三十位</span>-->
							</div>
						</div>
					</div>
					<p class="suggest"><span class="red_color">*</span> 提示: 敏感系数<50%为合规，50%～90%为疑似违规，>90%为违规</p>
				</div>
			</el-col>
			<el-col :md="6" :lg="7" :xl="5">
				<div class="show_json_outer">
					<p class="result_title">审查结果</p>
					<div class="result_outer" v-for="item in resultType">
						<p>{{item.firstType}}</p>
						<p class="red_style_name">违规</p>
					</div>
					<div class="result_outer" v-show="resultType.length==0">
						<p class="green_style_name">合规</p>
					</div>
				</div>
			</el-col>
		</el-row>
	</div>
</template>

<script>
    export default {
	    props:['stopAudio'],
	    data(){
            return{
				resultType:[],
			}
        },
		mounted(){
		},
		watch:{

		},
		methods:{

            submitText(e,file){
                console.log(file);
                this.audioName = file.name;
                var loading = this.$loading({fullscreen:false,target:document.querySelector(".outer_text")});
                console.log("文本提交中。。。")
                var formData = new FormData($(this));
                formData.append('text', file);
                $.ajax({
                    url: this.api+"/api/v1/text/get_text_recognition_inspection/",
                    type: "post",
                    data: formData,
//                    headers: {'Authorization': 'Token mytoken'},
                    cache: false,
                    contentType: false,
                    processData: false,
                    success:(response)=>{
                        console.log(response);
                        window.setTimeout(()=>{
                            console.log(document.getElementsByClassName('show_text_word')[0]);
                            document.getElementsByClassName('show_text_word')[0].innerHTML= response.data.web_text;
                            loading.close();
                        },1000);
                        if(response.data.sensitive_list.length!=0){
                            this.resultType = response.data.sensitive_list;
                            this.isNone = false;

                            this.$parent.changeUploadState(false);
                        }else {
                            this.resultType=[];
                            this.isNone = true;
                            loading.close();
                        }
                    },
                    error:err=>{
                        loading.close();
                        console.log(err)
                        this.$parent.changeUploadState(false);
                    }
                });
                e.preventDefault();
            }
		}
	}
</script>

<style scoped>
	@import "../../assets/css/audio.css";
	/*音频样式begin*/
	.show_voice_outer{min-height: 440px}
	.outer_text{height:500px;z-index: 1;text-align: center;background-color: #f4f5f7;padding-right: 20px;}
	.voice_title{height: 34px;line-height:34px;width: 135px;margin: 0 auto;background-color: #deecf9;color: #007bff;margin-bottom: 20px;}
	.voice_player_outer{height: 125px;width: 94%;margin: 10px auto;border-radius: 5px;background-color: white;}
	.voice_result_outer{height: 430px;background-color: white;width: 94%;margin: 10px auto;border-radius: 5px;overflow-y: scroll;overflow-x: hidden;}
	.audio_wrapper_outer{margin-left: 180px;margin-right: 20%;}
	.icon_music{margin: 25px 0 0 95px;}
	.show_text_word{margin: 20px ;color: #333;font-size: 14px;text-align: left;}
	/*.show_voice_word span{display: inline-block;text-align: left;}
	.show_voice_word span:nth-of-type(2){margin-left: 20px;flex: 1;}*/

	.show_json_outer{height: 430px;z-index: 99;background-color: white;position: relative;left: -20px;top: 35px;box-shadow:5px 0 20px #c5cff1;overflow-y: scroll;}
	.show_json_outer .result_title{font-size: 24px;color: #000000;text-align: center;height: 100px;padding-top: 30px;}
	.show_json_outer .result_title:before{content: "";background: url("../../assets/image/result_top_image.png") no-repeat center center;height: 23px;display: block;margin-bottom: 10px;}
	.suggest{color: #b2b2b2;font-size: 14px;min-height: 30px;margin:8px 0;}
	.result_outer{margin: 20px 30px;display: flex;color: #000000;height: 28px;line-height: 28px;}
	.result_outer p:nth-of-type(1){font-size: 16px;flex: 5;margin-left: 10px;}
	.result_outer p:nth-of-type(2){font-size: 16px;flex: 3;text-align: center}
	.result_outer p:nth-of-type(3){font-size: 16px;flex: 4;text-align: center}
	.result_outer .green_style_name{background-color: #54cd62;border: 1px solid #54cd62;color: #fff;text-align: center;}
	.result_outer .green_style_number{border: 1px solid #54cd62;color: #54cd62}
	.result_outer .orange_style_name{background-color: #ffac09;border: 1px solid #ffac09;color: #fff}
	.result_outer .orange_style_number{border: 1px solid #ffac09;color: #ffac09}
	.result_outer .red_style_name{background-color: #ff524a;border: 1px solid #ff524a;color: #fff}
	.result_outer .red_style_number{border: 1px solid #ff524a;color: #ff524a}
	.orange_color{color: #ffac09;}
	.red_color{color: #ff524a;}
</style>