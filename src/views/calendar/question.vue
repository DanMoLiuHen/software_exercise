<template>
  <div style="height: 420px">
    <span style="font-size: 24px"><b>&nbsp;万年历问题</b></span>
    <p>本问题输入为年月日，输出为输入年月日的下一天，输出格式为xxxx-xx-xx.</p>
    <p>如果年份越界，输出“Year Exceed”。</p>
    <p>如果月份越界，输出“Month Exceed”。</p>
    <p>如果日期越界，输出“Day Exceed”。</p>
    <p>若三者都越界，则输出“Illegal Case”</p>
    <p>如果输出的日期不符合月份要求，则输出“day is out of range for month”。</p>
    <p>我们规定 1<= Month <=12，1<=Day<=31，对于年份的范围，规定2000<= Year <=2100。</p>
  </div>
</template>

<script>
export default {
  name: "CalendarQuestion",
  components: {},
  props: {},
  data() {
    return {
    };
  },
  computed: {},
  watch: {},
  created() {},
  mounted() {},
  methods: {},
};
</script>

<style scoped lang="less">
</style>