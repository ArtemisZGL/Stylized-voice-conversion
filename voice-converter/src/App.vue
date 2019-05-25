<template>
  <div id="app">
    <h1> 风格化语音合成</h1>
    <div id="selectTarget">
      <label>合成语音目标: </label>
      <br/>
      <input type="radio" name ="target" value="trump2" @click="target_change_callback">Trump
      <input type="radio" name ="target" value="obama" checked @click="target_change_callback">Obama
    </div>
    <audio-recorder id="recorder"
      format="wav"
      upload-url="http://222.200.180.107:5000/audios"
      filename="au"
      :headers="headers"
      :attempts="6"
      :time="2"
      :before-recording="callback"
      :pause-recording="callback"
      :after-recording="callback"
      :select-record="callback"
      :before-upload="callback"
      :successful-upload="success_upload_callback"
      :failed-upload="callback"
      :bit-rate="192"/>
    <div id="resultPart" v-if="showResultPart">
      <label  @click="player_click_callback"> 合成语音结果 <br/> </label>
      <audio-player id="player" :src="mp3Src"/>
    </div>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

var baseURL = 'http://222.200.180.107:5000/audios/'
var headers = {"target": "obama"};
var showResultPart = false;
var mp3Src = baseURL + '6d4e57c5-f6f7-4651-8d86-02a795ecae4f';

export default {
  name: 'app',
  components: {
    HelloWorld
  },
  data () {
    return {
      mp3Src: mp3Src,
      headers: headers,
      showResultPart: showResultPart
    }
  },
  methods: {
    callback (data) {
      // disable-next-line:no-console
      //console.debug(data)
    },
    success_upload_callback(data){
      this.showResultPart = true;
      // disable-next-line:no-console
      //console.debug('success upload');
      // disable-next-line:no-console
      //console.debug(data['data']);
      this.mp3Src = baseURL + data['data'];
      // disable-next-line:no-console
      console.debug(this.mp3Src);
    },
    target_change_callback(event){
      this.headers["target"] = event.target.value;
      // disable-next-line:no-console
      //console.debug(this.headers);
    },
    player_click_callback(){
      // disable-next-line:no-console
      //console.debug(this.mp3Src);
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 50px;
}

#recorder {
  margin:0 auto;
  margin-top: 20px;
  margin-bottom: 20px;
}

#player {
  margin:0 auto;
}

#resultPart{
  border-radius: 16px;
  background-color: #FAFAFA;
  box-shadow: 0 4px 18px 0 rgba(0,0,0,0.17);
  box-sizing: content-box;
  margin:0 auto;
  width: auto;
  display:inline-block;
  padding: 16px;
}
</style>
