<template lang="pug">
section.carousel
  .tariffCards
    .content
      TariffCard(provider='Uzonline', title='Yangi', speed='1', price='109 000')
      TariffCard(provider='Comnet', title='Comfort+', speed='60', price='135 150')
      TariffCard(provider='Comnet', title='Yangi', speed='1', price='109000')
      TariffCard(provider='Name', title='Yangi', speed='1', price='109000')
      TariffCard(provider='Default', title='Yangi', speed='1', price='109000')
      TariffCard(provider='Uzonline', title='Yangi', speed='1', price='109 000')
      TariffCard(provider='Comnet', title='Comfort+', speed='60', price='135 150')
      TariffCard(provider='Comnet', title='Yangi', speed='1', price='109000')
      TariffCard(provider='Name', title='Yangi', speed='1', price='109000')
      TariffCard(provider='Default', title='Yangi', speed='1', price='109000')
      button.prevBtn(@click='prevBtn') Previous
      button.nextBtn(@click='nextBtn') Next
</template>
<script>
export default {
  data() {
    return {
      next: false,
      gap: 16,
    }
  },
  methods: {
    nextBtn() {},
  },
}
</script>
<style lang="scss" scoped>
.carousel {
  width: 100%;
  max-width: 964px;
  position: relative;

  .tariffCards {
    overflow: auto;
    scroll-behavior: smooth;
    scrollbar-width: none;
    .content {
      display: grid;
      grid-gap: 45px;
      grid-auto-flow: column;
      margin: auto;
      box-sizing: border-box;
    }
  }
  .prevBtn,
  .nextBtn {
    display: flex;
    justify-content: center;
    align-content: center;
    background: white;
    border: none;
    padding: 8px;
    border-radius: 50%;
    outline: 0;
    cursor: pointer;
    position: absolute;
  }
  .prevBtn {
    top: 50%;
    left: 0;
    transform: translate(50%, -50%);
    display: none;
  }
  .nextBtn {
    top: 50%;
    right: 0;
    transform: translate(-50%, -50%);
  }
}
</style>
