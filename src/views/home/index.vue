<template>
    <div class="main-container">
      <el-image
        style="width: 800px; height: 600px"
        :src="require('/src/views/home/cat.jpg')"></el-image>
    </div>
</template>

<script>

export default {
  name: "HomeIndex",
  components: {},
  props: {},
  data() {
    return {}
  },
  computed: {},
  watch: {},
  created() {},
  mounted() {},
  methods: {

  },
};
</script>

<style scoped lang="less">
.main-container{
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

</style>