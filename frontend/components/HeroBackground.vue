<template lang="pug">
section.globalBackground
  .gradient 
</template>
<script>
export default {}
</script>
<style lang="scss">
.globalBackground {
  background-image: url('./static/Tashkent-5.png');

  position: absolute;
  top: -5px;
  left: 0;
  z-index: -999;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-repeat: no-repeat;
  .gradient {
    width: 100%;
    height: 100%;
    background: linear-gradient(to bottom, transparent 70%, black 100%);
  }
}
</style>
