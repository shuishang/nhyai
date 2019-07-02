<template>
	<div class="handwrite">
		<el-row class="loading_con">
			<el-col :xs={span:24} :sm={span:11,offset:1} :md={span:10,offset:2} :lg={span:9,offset:3} :xl={span:8,offset:4}>
				<div class="image_outer">
					<div class="outer_add">
						<span class="original_style">原始图片</span>
						<img class="show_add_image" :src="dialogImageUrl">

					</div>
					<div class="upload_outer">
						<div class="local_upload">
							<!--<p>本地上传</p>-->
							<input id="datafile" name="datafile" type="file" class="inputfile" @change="changeImage($event)">
							<label for="datafile">本地上传</label>
						</div>
						<div class="show_input_outer">
							<input type="text" class="init_url_style">
							<p class="check_style">检测</p>
						</div>
					</div>
					<p class="top_suggest">提示：图片大小不超过1M，请保证需要识别部分为图片主体部分</p>
				</div>
				<!--<div class="show_add_image_outer">
					<div class="top_nav_image_outer">
						<a class="show_sm_image" href="javascript:void(0);" @click="clickImage(1)"><img src="../../assets/image/ocr/handwrite/hd-1-sm.jpg" alt="" :class="{'active':currentImage===1}" ></a>
						<a class="show_sm_image" href="javascript:void(0);" @click="clickImage(2)"><img src="../../assets/image/ocr/handwrite/hd-2-sm.jpg" alt="" :class="{'active':currentImage===2}"></a>
						<a class="show_sm_image" href="javascript:void(0);" @click="clickImage(3)"><img src="../../assets/image/ocr/handwrite/hd-3-sm.jpg" alt="" :class="{'active':currentImage===3}"></a>
						<a class="show_sm_image" href="javascript:void(0);" @click="clickImage(4)"><img src="../../assets/image/ocr/handwrite/hd-4-sm.jpg" alt="" :class="{'active':currentImage===4}"></a>
						<a class="show_sm_image" href="javascript:void(0);" @click="clickImage(5)"><img src="../../assets/image/ocr/handwrite/hd-5-sm.jpg" alt="" :class="{'active':currentImage===5}"></a>
						<a class="show_sm_image" href="javascript:void(0);" @click="clickImage(6)"><img src="../../assets/image/ocr/handwrite/hd-6-sm.jpg" alt="" :class="{'active':currentImage===6}"></a>
					</div>
					<div class="outer_add">
						<img class="show_add_image" :src="dialogImageUrl">
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
				</div>-->
			</el-col>
			<el-col :xs={span:24} :sm={span:11} :md="10" :lg="9" :xl="8">
				<div class="show_json_outer" v-loading="isLoading" element-loading-text="加载中..." >
					<span class="original_style">识别结果</span>
					<div id="show_json" v-show="showJson.name">
						<p>姓名：{{showJson.name}}</p>
						<p>性别：{{showJson.sex}}</p>
						<p>民族：{{showJson.nation}}</p>
						<p>出生：{{showJson.birthday}}</p>
						<p>住址：{{showJson.address}}</p>
						<p>公民身份证号：{{showJson.idNumber}}</p>
					</div>
				</div>
			</el-col>
		</el-row>
	</div>

</template>

<script>
    export default {
        data() {
            return {
                dialogImageUrl: require("../../assets/image/hand_writer_sample.jpg"),
                dialogVisible: false,
                jsonDemo:'{"name":"艾米","sex":"女","nation":"汉","birthday":"1986年4月23日","address":"上海徐汇区田林路397号腾云大厦6F","idNumber":"310104198604230289"}',
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

            };
        },
        mounted:function () {
            var that = this;
            var jdata = JSON.stringify(JSON.parse(this.jsonDemo), null, 4);
            this.loadDate();

//            $("#show_json").html("<pre>"+jdata+"</pre>");//这时数据展示正确
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
            uploadImage(e){
                this.loading = this.$loading(this.options);
                this.imageRight = false;
                var formData = new FormData($(this));
                formData.append('datafile', $('#datafile')[0].files[0]);
                $.ajax({
                    url: "http://172.31.11.171:8000/api/uploads/",
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
            changeImage(e){
                this.imageIsBig = false;
                this.imageRight = false;
                const file = e.target.files[0];
                const reader = new FileReader();
                const that = this;
                reader.readAsDataURL(file);
                reader.onload = function() {
                    that.dialogImageUrl = this.result;
                };
                let size=file.size;//文件的大小，判断图片的大小
                if(size>1048576){
                    console.log("图片太大了")
                }else {
                    this.imageRight = true;
                    console.log('开始上传')
//                    this.uploadImage(e);
                }
            },
            clickImage(index){
                if(index!=this.currentImage){
                    this.currentImage =index;
                    this.dialogImageUrl = require(`../../assets/image/ocr/handwrite/hd-${index}-lg.jpg`);
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
                    this.showJson= {};
                    var intervalid1 = setTimeout(() => {
                        this.showJson = JSON.parse(this.jsonDemo);
                        clearInterval(intervalid1);
                        this.isLoading = false;
                        $(".show_sm_image").attr("disabled",false).css("pointer-events","auto");
                        this.clickFirst = 0;
                    }, 4000)
				}

            }
        }
    }
</script>

<style scoped>
	/*.nav_header{height: 40px;line-height: 40px;font-size: 16px;display: inline-block;padding: 0 10px;color: #999999;border: 1px solid #dddddd;}
	.show_json_outer{height: 520px;overflow-y:scroll;border: 1px solid #e2ecfc;}
	.top_nav_image_outer{width: 98%;margin-bottom: 15px;display: flex;}
	.top_nav_image_outer a{flex: 1;float: left;}
	.top_nav_image_outer a img{width: 100%;opacity: 0.6;cursor:pointer;}
	.top_nav_image_outer a .active{opacity: 1}
	.show_add_image{height: 100%;margin: 0 auto;display: block;}
	.show_url{height: 33px; line-height: 33px;min-width: 100px;padding: 0 8px;}
	.show_left_aerrow{height: 15px;  width: 14px;  line-height: 15px;  color: rgb(255, 255, 255);  background-color: rgb(103, 194, 58);  border-radius: 50%;  display: inline-block;  padding: 3px;  margin-right: 5px;}
	.outer_add{width: 98%;height:350px;position: relative;overflow: hidden;border: 1px solid #e2ecfc;}
	.choose_style{display:block;height: 35px; line-height: 35px;width: 40%;font-size: 15px;color: white;background-color: #237EE6;text-align: center;margin-right: 2.5%;cursor: pointer;border-radius: 5px;}
	.choose_style_no{display:block;height: 35px; line-height: 35px;width: 40%;font-size: 15px;color: #999999;background-color: #dddddd;text-align: center;margin-right: 2.5%;border-radius: 5px;}
	#show_json{margin: 50px auto;padding: 10px 30px;}
	#show_json p{height: 30px;line-height: 30px;}
	.inputfile{z-index: -11111;width: 0px;height:1px;opacity: 0;}
	.suggest{color: #b2b2b2;font-size: 14px;min-height: 30px;margin:8px 0;}
	.show_result_outer{width: 100%;height: 100%;position: absolute;top: 0;z-index: 1;text-align: center; background-color: rgba(0,0,0,.4);}
	.show_result_outer:before{content: '';position: absolute;left: 0;top: 0;width: 100%;height: 100%;}
	.show_result{ z-index: 3;display: inline-block;vertical-align: middle;margin-top: 15%}*/
	.show_json_outer{height: 350px;overflow-y:scroll;border: 1px solid #e2ecfc;}
	.show_add_image{height: 100%;margin: 0 auto;display: block;}
	.original_style{position: absolute;font-size: 14px;color: #316dff;height: 30px;line-height: 30px;background-color: #e3ecfb;display: inline-block;padding: 0 35px 0 25px;-webkit-clip-path: polygon(0% 0%, 100% 0%, 90% 100%, 0% 100%);}
	.image_outer{margin-right: 10px;}
	.outer_add{height:350px;position: relative;overflow: hidden;border: 1px solid #e2ecfc;}
	.upload_outer{display: flex;margin-top: 20px;}
	.top_suggest{color: #999999;font-size: 14px;line-height: 40px;height: 30px;}
	.init_url_style{flex: 1;height: 43px;line-height: 43px;border: 1px solid #E2ECFC;font-size: 15px;padding-left: 10px;background-color: #fafcfe;}
	.init_url_style:hover{border: 1px solid #C0C4CC;border-right: none;}
	.init_url_style:focus{border: 1px solid #409EFF;border-right: none;}
	.check_style{display:inline-block;height: 41px;line-height: 41px;font-size: 16px;color: #316dff;border: 2px solid #316dff;width: 100px;text-align: center;cursor:pointer;background-color: #fafcfe;}
	.check_style:hover{background-color: #316DFF;color: white;}
	.local_upload{height: 45px;line-height: 45px;font-size: 16px;}
	.local_upload:after{content: "或";margin: 0 15px;}
	.inputfile{z-index: -11111;width: 0px;height:1px;opacity: 0;position: absolute;}
	.local_upload label{display:inline-block;height: 43px;line-height: 43px;font-size: 16px;background-color: #316DFF;color:white;border: 1px solid #316DFF;padding: 0 15px;text-align: center;cursor: pointer;}
	.local_upload label:hover{background-color: white;color: #316DFF}
	.show_input_outer{display: flex;flex: 1;}
	#show_json{margin: 50px auto;padding: 10px 30px;}
	#show_json p{height: 30px;line-height: 30px;}

	.advantage_product span{display: inline-block;padding: 10px;}
	.show_word{width: 192px;height: 148px;  display: inline-block;  text-align: center;  font-size: 22px;  font-style: normal;  color: #fff;  box-sizing: border-box;  padding-top: 58px;}
	.normal_result_back{background-image: url("../../assets/image/2.png"); background-position: 0 0;}
	.danger_result_back{background-image: url("../../assets/image/2.png"); background-position: -196px 0;}
	.probability_number{height: 30px;line-height: 30px;text-align: center;color: #fff;font-size: 16px;margin-top: 10px;}
</style>