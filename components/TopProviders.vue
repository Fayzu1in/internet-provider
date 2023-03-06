<template lang="pug">
section.topProviders
  div.topProviders__card(v-for="topProvider in topProviders")
    img.topProviders__card-img(:src="topProvider")
</template>
<script>
export default {
  // props: {
  //   src: {
  //     type: String,
  //     default: null,
  //   },
  // },
  data() {
    return {
      topProviders: ['././uzonline.png', '././freelink.png', '././comnet.png'],
    }
  },
}
</script>
<style lang="scss" scoped>
.topProviders {
  display: flex;
  justify-content: center;
  align-items: center;
  padding-bottom: 50px;
  &__card {
    &-img {
      background-color: #ffffff;
      height: 200px;
      width: 200px;
      padding: 30px;
      margin-left: 30px;
      border-radius: 3px;
      box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px,
        rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
    }
  }
}
</style>
