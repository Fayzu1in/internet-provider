<template lang="pug">
section.Providers.container-fluid
      .provider
        .provider__title Freelink
        Splide(:options='options' v-if="freelink?.length")
          splide-slide(v-for='link in freelink' :key='link.id')
            BetterofferCard(image='/freelink.png' :name='link.title' :nSpeed='link.night' :speed='link.speed' :price='link.price' :message='link.id')
        .provider__title Uzonline 
        Splide(:options='options' v-if="uzonline?.length")
          splide-slide(v-for='link in uzonline' :key='link.id')
            BetterofferCard(image='/uzonline.png' :name='link.title' :nSpeed='link.night' :tech='link.tech' :speed='link.speed' :price='link.price' :message='link.id')
        .provider__title Comnet 
        Splide(:options='options' v-if="comnet?.length")
          splide-slide(v-for='link in comnet' :key='link.id')
            BetterofferCard(image='/comnet.svg' :name='link.title' :nSpeed='link.night' :tech='link.tech' :speed='link.speed' :price='link.price' :message='link.id')
        .provider__title TPS 
        Splide(:options='options' v-if="tps?.length")
          splide-slide(v-for='link in tps' :key='link.id')
            BetterofferCard(image='/tps.png' :name='link.title' :nSpeed='link.night' :tech='link.tech' :speed='link.speed' :price='link.price' :message='link.id')
        .provider__title ISTV 
        Splide(:options='options' v-if="istv?.length")
          splide-slide(v-for='link in istv' :key='link.id')
            BetterofferCard(image='/istv.png' :name='link.title' :nSpeed='link.night' :tech='link.tech' :speed='link.speed' :price='link.price' :message='link.id')
</template>
<script>
export default {
  data() {
    return {
      plans: [],
      options: {
        type: 'loop',
        rewind: true,
        width: '100%',
        perPage: 4,
        padding: '20px',
        // arrows: true,
        gap: '30px',
      },
    }
  },
  async fetch() {
    this.plans = await this.$axios.$get('https://internetbor.uz/api/v1/plans/')
  },
  computed: {
    freelink() {
      return this.plans.filter((index) => {
        return index.provider_name === 'Freelink'
      })
    },
    uzonline() {
      return this.plans.filter((index) => {
        return index.provider_name === 'Uzonline'
      })
    },
    comnet() {
      return this.plans.filter((index) => {
        return index.provider_name === 'Comnet'
      })
    },
    tps() {
      return this.plans.filter((index) => {
        return index.provider_name === 'TPS'
      })
    },
    istv() {
      return this.plans.filter((index) => {
        return index.provider_name === 'ISTV'
      })
    },
  },
  mounted() {
    // Update splideOptions for mobile
    const mq = window.matchMedia('(max-width: 420px)')
    if (mq.matches) {
      this.options.perPage = 1
      // this.options.arrows = false
      this.options.width = '350px'
      this.options.gap = '30px'
      this.options.rewind = true
    }
    // // Add event listener to update options on window resize
    // window.addEventListener('resize', this.updateSplideOptions)
  },
}
</script>
<style lang="scss" scoped>
.Providers {
  background-color: #00000096;
  backdrop-filter: blur(10px);
  border-radius: 5px;
  border: 1px solid rgba(128, 128, 128, 0.417);
  padding: 15px 10px;
  padding-bottom: 30px;
  display: flex;
  border-radius: 5px;
  display: flex;
  flex-direction: column;

  .provider {
    &__title {
      font-size: 32px;
      padding-bottom: 30px;
      padding-top: 30px;
      text-align: center;
      font-weight: bold;

      @media only screen and (max-width: 420px) {
        font-size: 24px;
        padding-bottom: 15px;
        margin: 0;
      }
    }
  }
}
.card {
  width: 300px;
  height: 300px;
  background-color: #fff;
}
:deep(.splide__arrow) {
  border-radius: 10px;
  width: 3rem;
  height: 3rem;
  @media only screen and (max-width: 420px) {
    display: none;
  }
}
:deep(.splide__arrow--prev) {
  left: 0rem;
}
:deep(.splide__arrow--next) {
  right: 0rem;
}
:deep(.splide__pagination) {
  bottom: -1rem;
}
:deep(.splide__slide) {
  @media only screen and (max-width: 420px) {
    display: flex;
    justify-content: center;
  }
}
</style>
