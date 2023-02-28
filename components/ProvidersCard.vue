<template lang="pug">
section.ProvidersCard
  img.ProvidersCard__img(:src='src')
</template>
<script>
export default {
  props: {
    src: {
      type: String,
      default: null,
    },
  },
}
</script>
<style lang="scss" scoped>
.ProvidersCard {
  display: flex;
  justify-content: center;
  align-items: center;

  &__img {
    background-color: #ffffff;
    height: 110px;
    padding: 40px;
    margin-left: 30px;
    border-radius: 3px;
    box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px,
      rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
  }
}
</style>
