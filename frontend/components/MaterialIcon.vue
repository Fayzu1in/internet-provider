<template lang="pug">
svg.MaterialIcon(viewBox='0 0 24 24', :style='{ width: size, height: size }')
  path(:style='{ fill: color }', :d='icon')
</template>

<script>
export default {
  props: {
    icon: {
      type: String,
      default: null,
    },
    color: {
      type: String,
      default: null,
    },
    size: {
      type: String,
      default: null,
    },
  },
}
</script>

<style lang="scss" scoped>
.MaterialIcon {
  height: 2rem;
  width: 2rem;

  path {
    fill: #fff;
  }
}
</style>
