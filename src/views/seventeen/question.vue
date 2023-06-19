<template>
  <div>
    <span style="font-size:24px;"><b>&nbsp;第十七题</b></span>
    <div style="font-size:16px;">
      <p>
        一销售系统，如果销售员的年销售额大于200万RMB且请假天数不超过10天的情况下，现金到帐大于等于60%，则佣金（提成）系数为7，即佣金值为销售额除以佣金系数；现金到帐小于60%，佣金不予计算。所有其他情况且现金到帐小于等于85%，则按佣金系数均为6计算佣金，现金到账大于85%，佣金系数按5处理。
      </p>
      <p> 根据题意设计流程图并设计测试用例实现白盒测试（White Box Test）的1）语句覆盖，2）判断覆盖，3）条件覆盖，4）判断—条件覆盖，5）条件组合覆盖（测试用例及覆盖表示要清晰）。</p>
    </div>
    <el-divider></el-divider>

    <el-row :gutter="10">
      <el-col :span="6">
        <h3>名词命名</h3>
        <p>年销售额：AnnualSales</p>
        <p>请假天数：LeaveDays</p>
        <p>现金到账率： CashtoAccountRate </p>
        <p>佣金系数： CommissionCoefficient</p>
        <p>佣金值： Commission</p>
      </el-col>
    </el-row>
    <h3>流程图</h3>
    <el-row :gutter="10">
      <el-col :span="1"></el-col>
      <el-col :span="22">
        <el-image :src="require('/src/views/seventeen/17.jpeg')"></el-image>
      </el-col>
      <el-col :span="1"></el-col>
    </el-row>
    <el-divider></el-divider>
    <h3>语句覆盖</h3>
    <el-table :data="tableSentence" border>
      <el-table-column prop="id" label="用例编号" align="center">
      </el-table-column>
      <el-table-column prop="AnnualSales" label="年销售额" align="center">
      </el-table-column>
      <el-table-column prop="LeaveDays" label="请假天数" align="center">
      </el-table-column>
      <el-table-column prop="CashtoAccountRate" label="现金到账率" align="center">
      </el-table-column>
      <el-table-column prop="expectation" label="预期输出" align="center">
      </el-table-column>
      <el-table-column prop="cover" label="覆盖路径" align="center">
      </el-table-column>
    </el-table>

    <el-divider></el-divider>
    <h3>判断覆盖</h3>
    <el-table :data="table2" border>
      <el-table-column prop="id" label="用例编号" align="center">
      </el-table-column>
      <el-table-column prop="AnnualSales" label="年销售额" align="center">
      </el-table-column>
      <el-table-column prop="LeaveDays" label="请假天数" align="center">
      </el-table-column>
      <el-table-column prop="CashtoAccountRate" label="现金到账率" align="center">
      </el-table-column>
      <el-table-column prop="expectation" label="预期输出" align="center">
      </el-table-column>
      <el-table-column prop="cover" label="覆盖路径" align="center">
      </el-table-column>
    </el-table>

    <el-divider></el-divider>
    <h3>条件覆盖</h3>
    <p>要使得每个判断中的每个条件的可能取值至少满足一次。</p>
    <el-table :data="questionData" border>
      <el-table-column prop="con" label="条件" align="center">
      </el-table-column>
      <el-table-column prop="t" label="真" align="center">
      </el-table-column>
      <el-table-column prop="f" label="假" align="center">
      </el-table-column>
    </el-table>
    <p>测试用例</p>
    <el-table :data="table3" border>
      <el-table-column prop="id" label="用例编号" align="center">
      </el-table-column>
      <el-table-column prop="AnnualSales" label="年销售额" align="center">
      </el-table-column>
      <el-table-column prop="LeaveDays" label="请假天数" align="center">
      </el-table-column>
      <el-table-column prop="CashtoAccountRate" label="现金到账率" align="center">
      </el-table-column>
      <el-table-column prop="expectation" label="预期输出" align="center">
      </el-table-column>
      <el-table-column prop="cover" label="覆盖条件" align="center">
      </el-table-column>
    </el-table>

    <el-divider></el-divider>
    <h3>条件判断覆盖</h3>
    <p>一个判定中的每个条件的所有可能结果至少执行一次，并且每个判断本身的所有可 能结果至少执行一次。</p>
    <el-table :data="table4" border>
      <el-table-column prop="id" label="用例编号" align="center">
      </el-table-column>
      <el-table-column prop="AnnualSales" label="年销售额" align="center">
      </el-table-column>
      <el-table-column prop="LeaveDays" label="请假天数" align="center">
      </el-table-column>
      <el-table-column prop="CashtoAccountRate" label="现金到账率" align="center">
      </el-table-column>
      <el-table-column prop="expectation" label="预期输出" align="center">
      </el-table-column>
      <el-table-column prop="cover_condition" label="覆盖条件" align="center">
      </el-table-column>
      <el-table-column prop="cover" label="覆盖路径" align="center">
      </el-table-column>
      <el-table-column prop="cover_branch" label="覆盖分支" align="center">
      </el-table-column>
    </el-table>

    <el-divider></el-divider>
    <h3>条件组合覆盖</h3>
    <p>一个判定中的每个条件的所有可能结果至少执行一次，并且每个判断本身的所有可能结果至少执行一次。</p>
    <el-table :data="questionData2" border>
      <el-table-column prop="con" label="条件" align="center">
      </el-table-column>
      <el-table-column prop="t" label="真" align="center">
      </el-table-column>
      <el-table-column prop="f" label="假" align="center">
      </el-table-column>
    </el-table>
    <br>
    <el-table :data="table5" border>
      <el-table-column prop="id" label="覆盖组合号" align="center">
      </el-table-column>
      <el-table-column prop="combination" label="组合" align="center">
      </el-table-column>
      <el-table-column prop="abbreviation" label="简记" align="center">
      </el-table-column>
    </el-table>
    测试用例
    <el-table :data="table6" border>
      <el-table-column prop="id" label="用例编号" align="center">
      </el-table-column>
      <el-table-column prop="AnnualSales" label="年销售额" align="center">
      </el-table-column>
      <el-table-column prop="LeaveDays" label="请假天数" align="center">
      </el-table-column>
      <el-table-column prop="CashtoAccountRate" label="现金到账率" align="center">
      </el-table-column>
      <el-table-column prop="id2" label="覆盖组合号" align="center">
      </el-table-column>
      <el-table-column prop="cover" label="所走路径" align="center">
      </el-table-column>
      <el-table-column prop="cover_condition" label="覆盖条件" align="center">
      </el-table-column>
    </el-table>
  </div>
</template>

<script>

export default {
  name: "SalesQuestion",
  components: {},
  props: {},
  data() {
    return {
      questionData: [{
        con: "AnnualSales>=0",
        t: "T1",
        f: "F1",
      }, {
        con: "LeaveDays>=0",
        t: "T2",
        f: "F2",
      },
      {
        con: "CashtoAccountRate>=0",
        t: "T3",
        f: "F3",
      },
      {
        con: "AnnualSales>200",
        t: "T4",
        f: "F4",
      },
      {
        con: "LeaveDays<=10",
        t: "T5",
        f: "F5",
      },
      {
        con: "CashtoAccountRate>0.85",
        t: "T6",
        f: "F6",
      },
      {
        con: "CashtoAccountRate<0.6",
        t: "T7",
        f: "F7",
      },],
      tableSentence:[{"id":"1","AnnualSales":"-1","CashtoAccountRate":"0","LeaveDays":"0","expectation":"-1","cover":"{CN}"},{"id":"2","AnnualSales":"700","CashtoAccountRate":"0.8","LeaveDays":"5","expectation":"100","cover":"{ABEHLM}"},{"id":"3","AnnualSales":"700","CashtoAccountRate":"0.1","LeaveDays":"5","expectation":"0","cover":"{ABEIM}"},{"id":"4","AnnualSales":"600","CashtoAccountRate":"0.7","LeaveDays":"15","expectation":"100","cover":"{ABDGLM}"},{"id":"5","AnnualSales":"500","CashtoAccountRate":"0.9","LeaveDays":"15","expectation":"100","cover":"{ABDFLM}"}],
      table2:[{"id":"1","AnnualSales":"-1","CashtoAccountRate":"0","LeaveDays":"0","expectation":"-1","cover":"{CN}"},{"id":"2","AnnualSales":"700","CashtoAccountRate":"0.8","LeaveDays":"5","expectation":"100","cover":"{ABEHLM}"},{"id":"3","AnnualSales":"700","CashtoAccountRate":"0.1","LeaveDays":"5","expectation":"0","cover":"{ABEIM}"},{"id":"4","AnnualSales":"600","CashtoAccountRate":"0.7","LeaveDays":"15","expectation":"100","cover":"{ABDGLM}"},{"id":"5","AnnualSales":"500","CashtoAccountRate":"0.9","LeaveDays":"15","expectation":"100","cover":"{ABDFLM}"}],
      table3:[{"id":"1","AnnualSales":"-1","LeaveDays":"-1","CashtoAccountRate":"-1","expectation":"-1","cover":"F1,F2,F3,F4,T5,F6,T7"},{"id":"2","AnnualSales":"700","LeaveDays":"5","CashtoAccountRate":"0.7","expectation":"100","cover":"T1,T2,T3,T4,T5,F7"},{"id":"3","AnnualSales":"600","LeaveDays":"7","CashtoAccountRate":"0.4","expectation":"-1","cover":"T1,T2,T3,T4,T5,F7"},{"id":"4","AnnualSales":"120","LeaveDays":"15","CashtoAccountRate":"0.8","expectation":"20","cover":"T1,F4,T2,F5,T3,F6,F7"},{"id":"5","AnnualSales":"100","LeaveDays":"15","CashtoAccountRate":"0.9","expectation":"20","cover":"T1,F4,T2,F5,T3,T6,F7"}],
      table4:[{"id":"1","AnnualSales":"-1","LeaveDays":"-1","CashtoAccountRate":"-1","expectation":"-1","cover_condition":"F1,F2,F3,F4,T5,F6,T7","cover":"AC","cover_branch":"C"},{"id":"2","AnnualSales":"700","LeaveDays":"5","CashtoAccountRate":"0.7","expectation":"100","cover_condition":"T1,T2,T3,T4,T5,F7","cover":"ABEHLM","cover_branch":"BEH"},{"id":"3","AnnualSales":"600","LeaveDays":"7","CashtoAccountRate":"0.4","expectation":"-1","cover_condition":"T1,T2,T3,T4,T5,F7","cover":"ABEIM","cover_branch":"BEI"},{"id":"4","AnnualSales":"120","LeaveDays":"15","CashtoAccountRate":"0.8","expectation":"20","cover_condition":"T1,F4,T2,F5,T3,F6,F7","cover":"ABDGLM","cover_branch":"BDG"},{"id":"5","AnnualSales":"100","LeaveDays":"15","CashtoAccountRate":"0.9","expectation":"20","cover_condition":"T1,F4,T2,F5,T3,T6,F7","cover":"ABDFLM","cover_branch":"BDF"}],
      questionData2:[{"con":"AnnualSales > 200","t":"T1","f":"F1"},{"con":"LeaveDays <= 10","t":"T2","f":"F2"},{"con":"CashtoAccountRate <= 0.85","t":"T3","f":"F3"},{"con":"AnnualSales < 0","t":"T4","f":"F4"},{"con":"LeaveDays < 0","t":"T5","f":"F5"},{"con":"CashtoAccountRate < 0","t":"T6","f":"F6"}],
      table5:[{"id":"1","combination":"AnnualSales > 200, LeaveDays <= 10","abbreviation":"T1, T2"},{"id":"2","combination":"AnnualSales > 200, LeaveDays > 10","abbreviation":"T1, F2"},{"id":"3","combination":"AnnualSales <= 200, LeaveDays <= 10","abbreviation":"F1, T2"},{"id":"4","combination":"AnnualSales <= 200, LeaveDays > 10","abbreviation":"F1, F2"},{"id":"5","combination":"CashtoAccountRate <= 0.85","abbreviation":"T3"},{"id":"6","combination":"CashtoAccountRate > 0.85","abbreviation":"F3"},{"id":"7","combination":"CashtoAccountRate >= 0.6","abbreviation":"T4"},{"id":"8","combination":"CashtoAccountRate < 0.6","abbreviation":"F4"},{"id":"9","combination":"AnnualSales < 0, LeaveDays < 0, CashtoAccountRate < 0","abbreviation":"T5, T6, T7"},{"id":"10","combination":"AnnualSales < 0, LeaveDays < 0, CashtoAccountRate >= 0","abbreviation":"T5, T6, F7"},{"id":"11","combination":"AnnualSales < 0, LeaveDays >= 0, CashtoAccountRate >= 0","abbreviation":"T5, F6, F7"},{"id":"12","combination":"AnnualSales < 0, LeaveDays >= 0, CashtoAccountRate < 0","abbreviation":"T5, F6, T7"},{"id":"13","combination":"AnnualSales >= 0, LeaveDays < 0, CashtoAccountRate < 0","abbreviation":"F5, T6, T7"},{"id":"14","combination":"AnnualSales >= 0, LeaveDays < 0, CashtoAccountRate >= 0","abbreviation":"F5, T6, F7"},{"id":"15","combination":"AnnualSales >= 0, LeaveDays >= 0, CashtoAccountRate >= 0","abbreviation":"F5, F6, F7"},{"id":"16","combination":"AnnualSales >= 0, LeaveDays >= 0, CashtoAccountRate < 0","abbreviation":"F5, F6, T7"}],
      table6:[{"id":"1","AnnualSales":"-1","LeaveDays":"-1","CashtoAccountRate":"-1","id2":"9","cover":"AC","cover_condition":"T5,T6,T7"},{"id":"2","AnnualSales":"-1","LeaveDays":"-1","CashtoAccountRate":"0","id2":"10","cover":"AC","cover_condition":"T5,T6,F7"},{"id":"3","AnnualSales":"-1","LeaveDays":"0","CashtoAccountRate":"0","id2":"11","cover":"AC","cover_condition":"T5,F6,F7"},{"id":"4","AnnualSales":"-1","LeaveDays":"0","CashtoAccountRate":"-1","id2":"12","cover":"AC","cover_condition":"T5, F6, T7"},{"id":"5","AnnualSales":"0","LeaveDays":"-1","CashtoAccountRate":"-1","id2":"13","cover":"AC","cover_condition":"F5, T6, T7"},{"id":"6","AnnualSales":"0","LeaveDays":"-1","CashtoAccountRate":"0","id2":"14","cover":"AC","cover_condition":"F5, T6, F7"},{"id":"7","AnnualSales":"100","LeaveDays":"5","CashtoAccountRate":"0.9","id2":"3,6,15","cover":"ABDFLM","cover_condition":"F1,T2,F3,F5,F6,F7"},{"id":"8","AnnualSales":"100","LeaveDays":"15","CashtoAccountRate":"0.8","id2":"4,5,15","cover":"ABDGLM","cover_condition":"F1,F2,T3,F5,F6,F7"},{"id":"9","AnnualSales":"500","LeaveDays":"5","CashtoAccountRate":"0.8","id2":"1,6,15","cover":"ABEHLM","cover_condition":"T1,T2,F3,F5,F6,F7"},{"id":"10","AnnualSales":"500","LeaveDays":"15","CashtoAccountRate":"0.8","id2":"2,5,15","cover":"ABDGLM","cover_condition":"T1,F2,T3,F5,F6,F7"},{"id":"11","AnnualSales":"600","LeaveDays":"5","CashtoAccountRate":"0.5","id2":"1,7,15","cover":"ABEILM","cover_condition":"T1,T2,T4,F5,F6,F7"},{"id":"12","AnnualSales":"400","LeaveDays":"6","CashtoAccountRate":"0.5","id2":"1,8,15","cover":"ABDGLM","cover_condition":"T1,T2,F4,F5,F6,F7"},{"id":"13","AnnualSales":"200","LeaveDays":"15","CashtoAccountRate":"-1","id2":"16","cover":"AC","cover_condition":"F5,F6,T7"}],
    }
  },
  computed: {},
  watch: {},
  created() { },
  mounted() { },
  methods: {

  },
};
</script>

<style scoped lang="less"></style>