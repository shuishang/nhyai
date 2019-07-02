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
			<!--<el-row style="min-width: 800px;margin-top: 30px;display: none;">
				<el-col :md={span:14,offset:2} :lg={span:13,offset:2} :xl={span:11,offset:4}>
					<div class="show_add_image_outer">
						<div class="outer_add">
							<img class="show_add_image" :src="dialogImageUrl">
							<div class="show_result_outer">
								<div class="show_result" v-if="isForce">
									<i class="show_word danger_result_back"></i>
								</div>
								<div class="show_result" v-else>
									<i class="show_word normal_result_back"></i>
								</div>
							</div>
						</div>
						<p class="suggest"><span style="color: red">*</span> 提示: 敏感系数<50%为合规，50%～90%为疑似违规，>90%为违规<span v-show="imageIsBig" style="color: red;margin-left: 10px;display: inline-block;">！该图片大小超过1M</span></p>
					</div>
				</el-col>
				<el-col :md="6" :lg="7" :xl="5">
					<div class="show_json_outer">
						<p class="result_title">审查结果</p>
						<div class="result_outer">
							<p>暴恐识别</p>
							<p class="green_style_name">合规</p>
							<p class="green_style_number">12.35%</p>
						</div>
						<div class="result_outer">
							<p>色情识别</p>
							<p class="green_style_name">合规</p>
							<p class="green_style_number">12.56%</p>
						</div>
						<div class="result_outer">
							<p class="ell">政治敏感识别</p>
							<p class="orange_style_name">疑似违规</p>
							<p class="orange_style_number">60.35%</p>
						</div>
						<div class="result_outer">
							<p>公众人物识别</p>
							<p class="red_style_name">违规</p>
							<p class="red_style_number">90.35%</p>
						</div>
						<div class="result_outer">
							<p>广告检测</p>
							<p class="red_style_name">违规</p>
							<p class="red_style_number">90.16%</p>
						</div>
					</div>
				</el-col>
			</el-row>-->

			<!--视频评审-->
			<VideoCheck :stopVideo="stopVideo" v-show="checkType ===2"></VideoCheck>
			<!--<el-row style="min-width: 800px;margin-top: 30px;display: none;">
				<el-col :md={span:11,offset:2} :lg={span:11,offset:2} :xl={span:10,offset:4}>
					<div class="show_video_outer">
						<div class="show_video">
							<video src="../assets/video/dragen_wind.mp4" controls style="height: 100%;width: 100%;"></video>
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
			<el-row style="min-width: 800px;display: none;">
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
								<img src="../assets/image/force_image_example.png" alt="">
								<p>视频时间：00:10:25</p>
							</div>
							<div class="video_image_item fl">
								<div class="show_result_title">
									<div></div>
									<span class="video_result_red_title">违规</span>
									<span class="video_result_red_number">95.62%</span>
								</div>
								<img src="../assets/image/force_image_example.png" alt="">
								<p>视频时间：00:10:25</p>
							</div>
							<div class="video_image_item fl">
								<div class="show_result_title">
									<div></div>
									<span class="video_result_orange_title">疑似违规</span>
									<span class="video_result_orange_number">80.62%</span>
								</div>
								<img src="../assets/image/force_image_example.png" alt="">
								<p>视频时间：00:10:25</p>
							</div>
							<div class="video_image_item fl">
								<div class="show_result_title">
									<div></div>
									<span class="video_result_red_title">违规</span>
									<span class="video_result_red_number">95.62%</span>
								</div>
								<img src="../assets/image/force_image_example.png" alt="">
								<p>视频时间：00:10:25</p>
							</div>
							<div class="video_image_item fl">
								<div class="show_result_title">
									<div></div>
									<span class="video_result_orange_title">疑似违规</span>
									<span class="video_result_orange_number">80.62%</span>
								</div>
								<img src="../assets/image/force_image_example.png" alt="">
								<p>视频时间：00:10:25</p>
							</div>
							<div class="video_image_item fl">
								<div class="show_result_title">
									<div></div>
									<span class="video_result_red_title">违规</span>
									<span class="video_result_red_number">95.62%</span>
								</div>
								<img src="../assets/image/force_image_example.png" alt="">
								<p>视频时间：00:10:25</p>
							</div>
							<div class="video_image_item fl">
								<div class="show_result_title">
									<div></div>
									<span class="video_result_orange_title">疑似违规</span>
									<span class="video_result_orange_number">80.62%</span>
								</div>
								<img src="../assets/image/force_image_example.png" alt="">
								<p>视频时间：00:10:25</p>
							</div>
						</div>
						<p class="choose_again">重新选择</p>
					</div>
					<p class="suggest"><span style="color: red">*</span> 提示: 敏感系数<50%为合规，50%～90%为疑似违规，>90%为违规<span v-show="imageIsBig" style="color: red;margin-left: 10px;display: inline-block;">！该图片大小超过1M</span></p>

				</el-col>
			</el-row>-->

			<!--音频评审-->
			<AudioCheck :stopAudio="stopAudio" v-show="checkType ===3"></AudioCheck>
			<!--<el-row style="min-width: 800px;margin-top: 30px;">
				<el-col :md={span:14,offset:2} :lg={span:13,offset:2} :xl={span:11,offset:4}>
					<div class="show_voice_outer">
						<div class="outer_voice">
							<p class="voice_title">语音审查</p>
							<div class="voice_player_outer clearfix">
								<img src="../assets/image/voice_mark.png" class="fl icon_music" id="music_icon">
								<div class="audio_wrapper_outer">
									<div class="audio-wrapper">
										<audio size="#4.50MB" duration="#01:57" filename="#Launch_Kan R. Gao.mp3">
											<source src="../assets/audio/1.mp3" type="audio/mp3">
										</audio>
										<div class="audio-left">
											<img id="audioPlayer" src="../assets/image/audio/play.png">
										</div>
										<div class="audio-right">

											<div class="progress-bar-bg" id="progressBarBg">
												<span id="progressDot"></span>
												<div class="progress-bar" id="progressBar"></div>
											</div>
											<div class="audio-time">
												<span class="audio-length-current" id="audioCurTime">00:00</span>
												<span class="audio-length-total"></span>
											</div>
											<p style="max-width: 536px;">Launch_Kan R. Gao.mp3</p>
										</div>
									</div>
								</div>

							</div>
							<div class="voice_result_outer">
								<div class="show_voice_word">
									<span class="fl"> 1:05 - 1:06</span>
									<span class="fl ell"> 好，现在<span class="red_color">违禁词</span>到室当中呢，<span class="red_color">违禁词</span>了三十位</span>
								</div>
								<div class="show_voice_word">
									<span class="fl"> 1:05 - 1:06</span>
									<span class="fl ell"> 好，现在呢我们匆匆那年人机<span class="red_color">违禁词</span>交锋的第二轮，大家可以看到，违禁词 室当中呢，<span class="red_color">违禁词</span>了三十位</span>
								</div>
								<div class="show_voice_word">
									<span class="fl"> 1:05 - 1:06</span>
									<span class="fl ell"> 好，现在呢我们匆<span class="red_color">违禁词</span>匆那年人机交<span class="red_color">违禁词</span>室当中呢，了三十位</span>
								</div>
								<div class="show_voice_word">
									<span class="fl"> 1:05 - 1:06</span>
									<span class="fl ell"> 好<span class="red_color">违禁词</span>当中呢，<span class="red_color">违禁词</span>了三十位</span>
								</div>
							</div>
						</div>
						<p class="suggest"><span class="red_color">*</span> 提示: 敏感系数<50%为合规，50%～90%为疑似违规，>90%为违规<span v-show="imageIsBig" style="color: red;margin-left: 10px;display: inline-block;">！该图片大小超过1M</span></p>
					</div>
				</el-col>
				<el-col :md="6" :lg="7" :xl="5">
					<div class="show_json_outer">
						<p class="result_title">审查结果</p>
						<div class="result_outer">
							<p>暴恐识别</p>
							<p class="green_style_name">合规</p>
							<p class="green_style_number">12.35%</p>
						</div>
						<div class="result_outer">
							<p>色情识别</p>
							<p class="green_style_name">合规</p>
							<p class="green_style_number">12.56%</p>
						</div>
						<div class="result_outer">
							<p class="ell">政治敏感识别</p>
							<p class="orange_style_name">疑似违规</p>
							<p class="orange_style_number">60.35%</p>
						</div>
						<div class="result_outer">
							<p>公众人物识别</p>
							<p class="red_style_name">违规</p>
							<p class="red_style_number">90.35%</p>
						</div>
						<div class="result_outer">
							<p>广告检测</p>
							<p class="red_style_name">违规</p>
							<p class="red_style_number">90.16%</p>
						</div>
					</div>
				</el-col>
			</el-row>-->
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
							<td>预览</td>
						</tr>
						<tr class="show_history_con">
							<td class="ell">imadef.jpg</td>
							<td class="orange_color">疑似违规</td>
							<td class="ell">暴恐识别、色情识别、其他识别</td>
							<td >92.243%</td>
							<td class="ell">文本内容占位字符...</td>
							<td class="ell">2019-03-04 20:29:33</td>
							<td>预览</td>
						</tr>
						<tr class="show_history_con">
							<td class="ell">imadef.jpg</td>
							<td class="green_color">合规</td>
							<td class="ell">暴恐识别、色情识别、其他识别</td>
							<td >92.243%</td>
							<td class="ell">文本内容占位字符...</td>
							<td class="ell">2019-03-04 20:29:33</td>
							<td>预览</td>
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
                stopAudio:false

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
            /*document.addEventListener('DOMContentLoaded', ()=> {
                // 设置音频文件名显示宽度
                var element = document.querySelector('.audio-right');
                var maxWidth = window.getComputedStyle(element, null).width;
                document.querySelector('.audio-right p').style.maxWidth = maxWidth;

                // 初始化音频控制事件
                this.initAudioEvent();
            }, false);*/
//            this.initAudioEvent();
        },
        methods: {
            uploadImage(e){
                this.loading = this.$loading(this.options);
                this.imageRight = false;
                var formData = new FormData($(this));
                formData.append('datafile1', $('#datafile')[0].files[0]);
                $.ajax({
//                    url: "http://172.31.11.171:8000/api/uploads/",
                    url: "http://172.31.4.6:8000/api/imageTerrorismUploads/",
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


            /*initAudioEvent(){
				var audio = document.getElementsByTagName('audio')[0];
				var audioPlayer = document.getElementById('audioPlayer');
				var musicIcon = document.getElementById('music_icon');

				// // 添加音频自动播放功能
				// // PS：不完善，在chrome下会报错，原因看这里https://developers.google.com/web/updates/2017/09/autoplay-policy-changes
				// audio.addEventListener('canplaythrough', function (event) {
				//     var playPromise = audio.play();
				//     if (playPromise !== undefined) {
				//         playPromise.then(() => {
				//                 audioPlayer.src = './image/pause.png';
				//             })
				//             .catch(error => {
				//                 // Auto-play was prevented
				//                 // Show paused UI.
				//                 console.log(error.message)
				//             });
				//     }
				// });

				// 监听音频播放时间并更新进度条
				audio.addEventListener('timeupdate', ()=>{
					this.updateProgress(audio);
				}, false);

				// 监听播放完成事件
				audio.addEventListener('ended', ()=> {
					this.audioEnded();
				}, false);

				// 点击播放/暂停图片时，控制音乐的播放与暂停
				audioPlayer.addEventListener('click', ()=> {
					// 改变播放/暂停图片
					if (audio.paused) {
						// 开始播放当前点击的音频
						audio.play();
						audioPlayer.src =require('../assets/image/audio/pause.png') ;
                        musicIcon.src = require('../assets/image/audio/icon-music.gif');
					} else {
						audio.pause();
						audioPlayer.src =require( '../assets/image/audio/play.png');
                        musicIcon.src = require('../assets/image/voice_mark.png');
					}
				}, false);

				// 点击进度条跳到指定点播放
				// PS：此处不要用click，否则下面的拖动进度点事件有可能在此处触发，此时e.offsetX的值非常小，会导致进度条弹回开始处（简直不能忍！！）
				var progressBarBg = document.getElementById('progressBarBg');
				progressBarBg.addEventListener('mousedown', (event)=> {
					// 只有音乐开始播放后才可以调节，已经播放过但暂停了的也可以
					if (!audio.paused || audio.currentTime != 0) {
						var pgsWidth = parseFloat(window.getComputedStyle(progressBarBg, null).width.replace('px', ''));
						var rate = event.offsetX / pgsWidth;
						audio.currentTime = audio.duration * rate;
						this.updateProgress(audio);
					}
				}, false);

				// 拖动进度点调节进度
				this.dragProgressDotEvent(audio);
			},

			/!**
			 * 鼠标拖动进度点时可以调节进度
			 * @param {*} audio
			 *!/
			dragProgressDotEvent(audio) {
				var dot = document.getElementById('progressDot');

				var position = {
					oriOffestLeft: 0, // 移动开始时进度条的点距离进度条的偏移值
					oriX: 0, // 移动开始时的x坐标
					maxLeft: 0, // 向左最大可拖动距离
					maxRight: 0 // 向右最大可拖动距离
				};
				var flag = false; // 标记是否拖动开始

				// 鼠标按下时
				dot.addEventListener('mousedown', down, false);
				dot.addEventListener('touchstart', down, false);

				// 开始拖动
				document.addEventListener('mousemove', move, false);
				document.addEventListener('touchmove', move, false);

				// 拖动结束
				document.addEventListener('mouseup', end, false);
				document.addEventListener('touchend', end, false);

				function down(event) {
					if (!audio.paused || audio.currentTime != 0) { // 只有音乐开始播放后才可以调节，已经播放过但暂停了的也可以
						flag = true;

						position.oriOffestLeft = dot.offsetLeft;
						position.oriX = event.touches ? event.touches[0].clientX : event.clientX; // 要同时适配mousedown和touchstart事件
						position.maxLeft = position.oriOffestLeft; // 向左最大可拖动距离
						position.maxRight = document.getElementById('progressBarBg').offsetWidth - position.oriOffestLeft; // 向右最大可拖动距离

						// 禁止默认事件（避免鼠标拖拽进度点的时候选中文字）
						if (event && event.preventDefault) {
							event.preventDefault();
						} else {
							event.returnValue = false;
						}

						// 禁止事件冒泡
						if (event && event.stopPropagation) {
							event.stopPropagation();
						} else {
							window.event.cancelBubble = true;
						}
					}
				}

				function move(event) {
					if (flag) {
						var clientX = event.touches ? event.touches[0].clientX : event.clientX; // 要同时适配mousemove和touchmove事件
						var length = clientX - position.oriX;
						if (length > position.maxRight) {
							length = position.maxRight;
						} else if (length < -position.maxLeft) {
							length = -position.maxLeft;
						}
						var progressBarBg = document.getElementById('progressBarBg');
						var pgsWidth = parseFloat(window.getComputedStyle(progressBarBg, null).width.replace('px', ''));
						var rate = (position.oriOffestLeft + length) / pgsWidth;
						audio.currentTime = audio.duration * rate;
						this.updateProgress(audio);
					}
				}

				function end() {
					flag = false;
				}
			},

			/!**
			 * 更新进度条与当前播放时间
			 * @param {object} audio - audio对象
			 *!/
			updateProgress(audio) {
				var value = audio.currentTime / audio.duration;
				document.getElementById('progressBar').style.width = value * 100 + '%';
				document.getElementById('progressDot').style.left = value * 100 + '%';
				document.getElementById('audioCurTime').innerText = this.transTime(audio.currentTime);
				document.getElementsByClassName('audio-length-total')[0].innerText = this.transTime(audio.duration);
			},

			/!**
			 * 播放完成时把进度调回开始的位置
			 *!/
			audioEnded() {
				document.getElementById('progressBar').style.width = 0;
				document.getElementById('progressDot').style.left = 0;
				document.getElementById('audioCurTime').innerText = this.transTime(0);
				document.getElementById('audioPlayer').src =require( '../assets/image/audio/play.png');
				document.getElementById('music_icon').src =require( '../assets/image/voice_mark.png');
			},

			/!**
			 * 音频播放时间换算
			 * @param {number} value - 音频当前播放时间，单位秒
			 *!/
			transTime(value) {
				var time = "";
				var h = parseInt(value / 3600);
				value %= 3600;
				var m = parseInt(value / 60);
				var s = parseInt(value % 60);
				if (h > 0) {
					time = this.formatTime(h + ":" + m + ":" + s);
				} else {
					time = this.formatTime(m + ":" + s);
				}

				return time;
			},

			/!**
			 * 格式化时间显示，补零对齐
			 * eg：2:4  -->  02:04
			 * @param {string} value - 形如 h:m:s 的字符串
			 *!/
			formatTime(value) {
				var time = "";
				var s = value.split(':');
				var i = 0;
				for (; i < s.length - 1; i++) {
					time += s[i].length == 1 ? ("0" + s[i]) : s[i];
					time += ":";
				}
				time += s[i].length == 1 ? ("0" + s[i]) : s[i];

				return time;
			}*/

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

	/*image样式begin*/
	.show_add_image_outer{min-height: 400px}
	.show_word{width: 180px;height: 200px;  display: inline-block;  text-align: center;  font-size: 22px;  font-style: normal;  color: #fff;  box-sizing: border-box;  padding-top: 58px;}
	.normal_result_back{background-image: url("../assets/image/compliance_result.png");background-repeat: no-repeat;position: absolute;top: 50%;left: 50%;margin-left: -90px;margin-top: -100px;}
	.danger_result_back{background-image: url("../assets/image/2.png"); background-position: -196px 0;}
	.show_json_outer{height: 430px;z-index: 99;background-color: white;position: relative;left: -20px;top: 35px;box-shadow:5px 0 20px #c5cff1}
	.show_json_outer .result_title{font-size: 24px;color: #000000;text-align: center;height: 100px;padding-top: 30px;}
	.show_json_outer .result_title:before{content: "";background: url("../assets/image/result_top_image.png") no-repeat center center;height: 23px;display: block;margin-bottom: 10px;}
	.suggest{color: #b2b2b2;font-size: 14px;min-height: 30px;margin:8px 0;}
	.show_result_outer{width: 100%;height: 100%;position: absolute;top: 0;z-index: 1;text-align: center; background-color: rgba(0,0,0,.4);}
	.show_result_outer:before{content: '';position: absolute;left: 0;top: 0;width: 100%;height: 100%;}
	.show_result{ z-index: 3;display: inline-block;vertical-align: middle;margin-top: 15%}
	.result_outer{margin: 20px 30px;display: flex;color: #000000;height: 28px;line-height: 28px;}
	.result_outer p:nth-of-type(1){font-size: 16px;flex: 5;margin-left: 10px;}
	.result_outer p:nth-of-type(2){font-size: 16px;flex: 3;text-align: center}
	.result_outer p:nth-of-type(3){font-size: 16px;flex: 4;text-align: center}
	.result_outer .green_style_name{background-color: #54cd62;border: 1px solid #54cd62;color: #fff}
	.result_outer .green_style_number{border: 1px solid #54cd62;color: #54cd62}
	.result_outer .orange_style_name{background-color: #ffac09;border: 1px solid #ffac09;color: #fff}
	.result_outer .orange_style_number{border: 1px solid #ffac09;color: #ffac09}
	.result_outer .red_style_name{background-color: #ff524a;border: 1px solid #ff524a;color: #fff}
	.result_outer .red_style_number{border: 1px solid #ff524a;color: #ff524a}
	.show_add_image{height: 100%;margin: 0 auto;display: block;}
	.outer_add{height:500px;position: relative;overflow: hidden;}
	/*image样式end*/

	/*视频样式begin*/
	.show_video_outer{height: 400px}
	.show_video{height:440px;position: relative;overflow: hidden;}

	.video_result_outer{height: 440px;z-index: 99;background-color: white;box-shadow:5px 0 20px #c5cff1}
	.video_result_outer .result_title{font-size: 24px;color: #000000;text-align: center;height: 100px;padding-top: 30px;}
	.video_result_outer .result_title:before{content: "";background: url("../assets/image/result_top_image.png") no-repeat center center;height: 23px;display: block;margin-bottom: 10px;}
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

	/*音频样式begin*/
	.show_voice_outer{min-height: 440px}
	.outer_voice{height:500px;z-index: 1;text-align: center;background-color: #f4f5f7;padding-right: 20px;}
	.voice_title{height: 34px;line-height:34px;width: 135px;margin: 0 auto;background-color: #deecf9;color: #007bff;margin-bottom: 20px;}
	.voice_player_outer{height: 125px;width: 94%;margin: 10px auto;border-radius: 5px;background-color: white;}
	.voice_result_outer{height: 290px;background-color: white;width: 94%;margin: 10px auto;border-radius: 5px;overflow-y: scroll;overflow-x: hidden;}
	.voice_player{margin-top: 20px;}
	.audio_wrapper_outer{margin-left: 180px;margin-right: 120px;}
	.icon_music{margin: 25px 0 0 95px;}
	.show_voice_word{margin: 20px ;color: #010101;font-size: 14px;display: flex}
	.show_voice_word span{display: inline-block;text-align: left;}
	.show_voice_word span:nth-of-type(2){margin-left: 20px;flex: 1;}

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
	.show_history_con td:last-child{flex: 1;text-align: center;color: #85afff;}
	.show_history_con td:first-child{padding-left: 20px;flex: 2;}
	.show_history_con td:nth-of-type(3){flex: 2.5;}
	.show_history_con td:nth-of-type(6){flex: 2;}
	.show_history_con td:nth-of-type(5){flex: 2.5;}
	.orange_color{color: #ffac09;}
	.red_color{color: #ff524a;}
	.green_color{color: #54cd62;}

	.show_pagination{text-align: center;margin-top: 30px;}
</style>