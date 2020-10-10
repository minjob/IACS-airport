<template>
  <el-row>
    <el-col :span="24">
      <div class="page-title">
        <span style="margin-left: 10px;" class="text-size-normol">机组实时数据趋势图</span>
      </div>
      <el-form :inline="true" class="blackComponents">
        <el-form-item label="选择机组参数：">
          <el-select v-model="value" placeholder="选择机组参数" @change="selectTag">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="参数值：" v-if="tagValue">
          <span class="text-size-18 color-lightgreen">{{ tagValue }}</span>
        </el-form-item>
      </el-form>
      <div class="platformContainer">
        <ve-line :data="chartData" :extend="ChartExtend"></ve-line>
      </div>
    </el-col>
  </el-row>
</template>

<script>
  var moment = require('moment');
  export default {
    name: "realTimeLine",
    data(){
      return{
        ChartExtend:{
          grid:{
            left:'10px',
            right:'10px',
            bottom:'40px',
            top:'40px'
          },
          legend:{
            textStyle:{
              color:"#fff"
            }
          },
          xAxis:{
            axisLabel:{
              color:"#fff"
            }
          },
          yAxis:{
            axisLabel:{
              color:"#fff"
            }
          },
          series:{
            smooth: false,
          }
        },
        websock:null,
        websockVarData:"",
        value:"",
        options:[
          {label:"2号机组1号机头负载",value:"LS_2.LS2.DATA2"},
          {label:"2号机组2号机头负载",value:"LS_2.LS2.DATA3"},
          {label:"2号机组入水温度",value:"LS_2.LS2.DATA13"},
          {label:"2号机组出水温度",value:"LS_2.LS2.DATA14"},
          {label:"2号机组1号机头电流",value:"LS_2.LS2.DATA23"},
          {label:"2号机组2号机头电流",value:"LS_2.LS2.DATA24"},
        ],
        chartData:{
          columns: ['时间', '数值'],
          rows: []
        },
        tagValue:""
      }
    },
    created(){
      this.initWebSocket()
    },
    mounted(){

    },
    destroyed() {
      if(this.websock){
        this.websock.close() //离开路由之后断开websocket连接
      }
    },
    methods:{
      selectTag(){
        this.tagValue = ""
        this.chartData.rows = [
          { '时间': moment().subtract(40, 's').format("HH:mm:ss"), '数值': null},
          { '时间': moment().subtract(38, 's').format("HH:mm:ss"), '数值': null},
          { '时间': moment().subtract(36, 's').format("HH:mm:ss"), '数值': null},
          { '时间': moment().subtract(34, 's').format("HH:mm:ss"), '数值': null},
          { '时间': moment().subtract(32, 's').format("HH:mm:ss"), '数值': null},
          { '时间': moment().subtract(30, 's').format("HH:mm:ss"), '数值': null},
          { '时间': moment().subtract(28, 's').format("HH:mm:ss"), '数值': null},
          { '时间': moment().subtract(26, 's').format("HH:mm:ss"), '数值': null},
          { '时间': moment().subtract(24, 's').format("HH:mm:ss"), '数值': null},
          { '时间': moment().subtract(22, 's').format("HH:mm:ss"), '数值': null},
          { '时间': moment().subtract(20, 's').format("HH:mm:ss"), '数值': null},
          { '时间': moment().subtract(18, 's').format("HH:mm:ss"), '数值': null},
          { '时间': moment().subtract(16, 's').format("HH:mm:ss"), '数值': null},
          { '时间': moment().subtract(14, 's').format("HH:mm:ss"), '数值': null},
          { '时间': moment().subtract(12, 's').format("HH:mm:ss"), '数值': null},
          { '时间': moment().subtract(10, 's').format("HH:mm:ss"), '数值': null},
          { '时间': moment().subtract(8, 's').format("HH:mm:ss"), '数值': null},
          { '时间': moment().subtract(6, 's').format("HH:mm:ss"), '数值': null},
          { '时间': moment().subtract(4, 's').format("HH:mm:ss"), '数值': null},
          { '时间': moment().subtract(2, 's').format("HH:mm:ss"), '数值': null}
        ]
      },
      initWebSocket(){ //初始化weosocket
        this.websock = new WebSocket('ws://' + location.host + '/socket');
        // this.websock = new WebSocket('ws://127.0.0.1:5002/socket');
        this.websock.onmessage = this.websocketonmessage;
        this.websock.onopen = this.websocketonopen;
        this.websock.onerror = this.websocketonerror;
        this.websock.onclose = this.websocketclose;
      },
      websocketonopen(){ //连接建立之后执行send方法发送数据
        this.websocketsend();
      },
      websocketonerror(){//连接建立失败重连
        console.log("websocket连接失败")
      },
      websocketonmessage(e){ //数据接收
        this.websockVarData = JSON.parse(e.data)
        let that = this
        for(var key in that.websockVarData){//循环返回的对象，并获取想要的tag参数
          if(key === that.value){
            that.tagValue = that.websockVarData[key]
            that.chartData.rows.push({
              "时间": moment().format("HH:mm:ss"),
              "数值": that.websockVarData[key]
            })
            that.chartData.rows.shift()
          }
        }
      },
      websocketsend(Data){//数据发送
        this.websock.send(Data);
      },
      websocketclose(e){  //关闭
        console.log("websocket关闭")
      },
      closesocket(){
        this.websock.close()
      },
    }
  }
</script>

<style scoped>

</style>
