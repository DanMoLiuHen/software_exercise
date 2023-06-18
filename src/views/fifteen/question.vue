<template>
  <div>
    <span style="font-size:24px;"><b>&nbsp;ATM</b></span>
    <div style="font-size:16px;">

      <p>分析或查阅得到正确的ATM的系统状态图，再基于state transition testing分析出transition tree，最后设计出逻辑测试用例。</p>
      <div>
        <p> 主要状态为</p>
        <img src="./seven.png" />
      </div>
      <div>
        <p>主要行为为</p>
        <img src="./eight.png" />
        <img src="./nine.png" />
      </div>
      <div>
        <p>根据状态图转状态树的算法</p>
        <p>（1）状态树的节点描述状态图的状态，状态树的枝干描述状态图的事件。</p>
        <p>（2）转换树的根节点为状态图的初始状态，转换树的终节点为叶节点。</p>
        <p>（3）转换树的每个节点，在状态图中如有直接后续状态，则添加一个枝干和节点（不同的事件应 有不同的枝干和节点），直到出现从根节点到新添加的节点的路径上已经出现过相同状态的情 况，可将此节点作为叶节点： </p>
        <img src="./ten.png" />
      </div>
      <div>
        <p>基于状态树构建测试用例</p>
        <img src="./eleven.png" />
        <img src="./twelve.png" />
        <img src="./13.png" />
      </div>



    </div>






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
        minute: "0",
        times: 0,
        level: "3",
        amount: "Middle"
      }, {
        minute: "0",
        times: 3,
        level: "3",
        amount: "Middle"
      }, {
        minute: "0",
        times: 10,
        level: "3",
        amount: "Middle"
      }, {
        minute: "0",
        times: 18,
        level: "3",
        amount: "Middle"
      }, {
        minute: "0",
        times: 20,
        level: "3",
        amount: "Middle"
      }, {
        minute: "0",
        times: 22,
        level: "3",
        amount: "Middle"
      },
      {
        minute: "0",
        times: 10,
        level: "1",
        amount: "Middle"
      },
      {
        minute: "0",
        times: 10,
        level: "2",
        amount: "Middle"
      },
      {
        minute: "0",
        times: 10,
        level: "3",
        amount: "Middle"
      },
      {
        minute: "0",
        times: 10,
        level: "4",
        amount: "Middle"
      },
      {
        minute: "0",
        times: 10,
        level: "5",
        amount: "Middle"
      },
      {
        minute: "0",
        times: 10,
        level: "3",
        amount: "Min-"
      },
      {
        minute: "0",
        times: 10,
        level: "3",
        amount: "Min"
      },
      {
        minute: "0",
        times: 10,
        level: "3",
        amount: "Little"
      },
      {
        minute: "0",
        times: 10,
        level: "3",
        amount: "Middle"
      },
      {
        minute: "0",
        times: 10,
        level: "3",
        amount: "Large"
      },
      {
        minute: "0",
        times: 10,
        level: "3",
        amount: "Max"
      },
      {
        minute: "0",
        times: 10,
        level: "3",
        amount: "Max+"
      },
      {
        minute: "27",
        times: 0,
        level: "3",
        amount: "Middle"
      },
      {
        minute: "27",
        times: 3,
        level: "3",
        amount: "Middle"
      },
      {
        minute: "27",
        times: 10,
        level: "3",
        amount: "Middle"
      },
      {
        minute: "27",
        times: 18,
        level: "3",
        amount: "Middle"
      },
      {
        minute: "27",
        times: 20,
        level: "3",
        amount: "Middle"
      },
      {
        minute: "27",
        times: 22,
        level: "3",
        amount: "Middle"
      },
      {
        minute: "27",
        times: 10,
        level: "1",
        amount: "Middle"
      },
      {
        minute: "27",
        times: 10,
        level: "2",
        amount: "Middle"
      },
      {
        minute: "27",
        times: 10,
        level: "3",
        amount: "Middle"
      },
      {
        minute: "27",
        times: 10,
        level: "4",
        amount: "Middle"
      },
      {
        minute: "27",
        times: 10,
        level: "5",
        amount: "Middle"
      },
      {
        minute: "27",
        times: 10,
        level: "3",
        amount: "Min-"
      },
      {
        minute: "27",
        times: 10,
        level: "3",
        amount: "Min"
      },
      {
        minute: "27",
        times: 10,
        level: "3",
        amount: "Little"
      },
      {
        minute: "27",
        times: 10,
        level: "3",
        amount: "Middle"
      },
      {
        minute: "27",
        times: 10,
        level: "3",
        amount: "Large"
      },
      {
        minute: "27",
        times: 10,
        level: "3",
        amount: "Max"
      },
      {
        minute: "27",
        times: 10,
        level: "3",
        amount: "Max+"
      },
      ],
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