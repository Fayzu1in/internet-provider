<template lang="pug">
Splide(:options="options" aria-label="Vue Splide Example")
  SplideSlide
    TariffCard(provider='Uzonline', title='Yangi', speed='1', price='109 000')
  SplideSlide
    TariffCard(provider='Comnet', title='Comfort+', speed='60', price='135 150')
  SplideSlide
    TariffCard(provider='Comnet', title='Yangi', speed='1', price='109000')
  SplideSlide
    TariffCard(provider='Name', title='Yangi', speed='1', price='109000')
  SplideSlide
    TariffCard(provider='Default', title='Yangi', speed='1', price='109000')
  SplideSlide
    TariffCard(provider='Uzonline', title='Yangi', speed='1', price='109 000')
  SplideSlide
    TariffCard(provider='Comnet', title='Comfort+', speed='60', price='135 150')
  SplideSlide
    TariffCard(provider='Comnet', title='Yangi', speed='1', price='109000')
  SplideSlide
    TariffCard(provider='Name', title='Yangi', speed='1', price='109000')
  SplideSlide
    TariffCard(provider='Default', title='Yangi', speed='1', price='109000')


</template>
<script>
export default {
  props: {
    src: {
      type: String,
      default: null,
    },
  },
  data() {
    return {
      options: {
        rewind: true,
        width: 800,
        perPage: 3,
        gap: '0.5rem',
        perMove: 2,
        type: 'loop',
      },
    }
  },
}
</script>
<style lang="scss"></style>
