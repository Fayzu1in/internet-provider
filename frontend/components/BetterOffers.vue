<template lang="pug">
Splide(:options="options" aria-label="Vue Splide Example")
  SplideSlide
    BetterofferCard(provider='Uzonline', title='Yangi', speed='1', price='109 000')
  SplideSlide
    BetterofferCard(provider='Comnet', title='Comfort+', speed='60', price='135 150')
  SplideSlide
    BetterofferCard(provider='Comnet', title='Yangi', speed='1', price='109000')
  SplideSlide
    BetterofferCard(provider='Name', title='Yangi', speed='1', price='109000')
  SplideSlide
    BetterofferCard(provider='Default', title='Yangi', speed='1', price='109000')
  SplideSlide
    BetterofferCard(provider='Uzonline', title='Yangi', speed='1', price='109 000')
  SplideSlide
    BetterofferCard(provider='Comnet', title='Comfort+', speed='60', price='135 150')
  SplideSlide
    BetterofferCard(provider='Comnet', title='Yangi', speed='1', price='109000')
  SplideSlide
    BetterofferCard(provider='Name', title='Yangi', speed='1', price='109000')
  SplideSlide
    BetterofferCard(provider='Default', title='Yangi', speed='1', price='109000')


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
