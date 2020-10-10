<template>
  <el-row :gutter="20" style="height: 100%;padding: 20px;background: #07184E;">
    <el-col :span="8">
      <div class="platformContainer" style="min-height: 300px;">
        <div class="platformTitle">环境参数</div>
        <el-row>
          <el-col :span="12">
            <p class="marginBottom">室外温度：<span class="text-size-20 color-orange">35℃</span></p>
          </el-col>
          <el-col :span="12">
            <p class="marginBottom">人流数：<span class="text-size-20 color-darkblue">1112</span></p>
          </el-col>
          <el-col :span="12">
            <p class="marginBottom">站厅温度：<span class="text-size-20 color-success">26℃</span></p>
          </el-col>
          <el-col :span="12">
            <p class="marginBottom">站厅湿度：<span class="text-size-20 color-success">56％RH</span></p>
          </el-col>
          <el-col :span="12">
            <p class="marginBottom">站台温度：<span class="text-size-20 color-success">26℃</span></p>
          </el-col>
          <el-col :span="12">
            <p class="marginBottom">站台湿度：<span class="text-size-20 color-success">56％RH</span></p>
          </el-col>
        </el-row>
      </div>
    </el-col>
    <el-col :span="8">
      <div class="platformContainer" style="min-height: 300px;">
        <div class="platformTitle">便携导航</div>
        <el-row>
          <el-col :span="24" style="text-align: center;">
            <el-button type="success" class="marginBottom marginTop"><a href="http://192.168.8.109:9900/#/SystemMonitor">进入智慧环控系统</a></el-button>
            <el-button type="primary">进入智慧环控设备管理</el-button>
          </el-col>
        </el-row>
      </div>
    </el-col>
    <el-col :span="8">
      <div class="platformContainer" style="min-height: 300px;">
        <div class="platformTitle">电耗统计</div>
      </div>
    </el-col>
    <el-col :span="16">
      <div class="platformContainer" style="min-height: 300px;">

      </div>
    </el-col>
    <el-col :span="8">
      <div class="platformContainer" style="min-height: 300px;">

      </div>
    </el-col>
  </el-row>
</template>

<script>
  export default {
    name: "board"
  }
</script>

<style scoped>
  .platformTitle{
    display: inline-block;
    margin-left: -15px;
    margin-top: -15px;
    padding: 10px 15px;
    border-right: 3px solid #07184E;
    border-bottom: 3px solid #07184E;
    background: linear-gradient(270deg, #0D4A8E 0%, #072D69 23%, #093574 73%, #0D4A8E 100%);
    clear: both;
    overflow: hidden;
  }
</style>
