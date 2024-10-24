<template lang="pug">
.ModalDialog(@click.self='$emit("close")')
  .ModalContent
    slot
</template>

<script>
export default {
  methods: {},
}
</script>

<style lang="scss" scoped>
* {
  width: auto;
}
.ModalDialog {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  z-index: 1000;
  display: flex;
  backdrop-filter: blur(1.5rem);
  overflow-y: auto;
  overscroll-behavior-y: none;
}
</style>
