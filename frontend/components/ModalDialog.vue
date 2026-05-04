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
  inset: 0;
  width: 100%;
  height: 100%;
  z-index: 1000;

  display: flex;
  align-items: center;
  justify-content: center;

  padding: 20px;

  background: rgba(0, 0, 0, 0.55);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);

  overflow-y: auto;
  overscroll-behavior-y: none;
}
</style>
