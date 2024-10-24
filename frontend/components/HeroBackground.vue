<template lang="pug">
section.globalBackground
  .gradient 
</template>
<script>
export default {}
</script>
<style lang="scss">
.globalBackground {
  // background-image: url('/ib-backgroung-new-1.svg');

  position: fixed;
  top: -105px;
  left: 0;
  z-index: -999;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-repeat: no-repeat;
  .gradient {
    width: 100%;
    height: 100%;
    background: linear-gradient(to bottom, rgb(0, 0, 0, 20%) 50%, black 100%);
  }
}
</style>
