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
        
        
        


        //- div(v-for='line in uzonline' :key='line.id' )
        //-   TariffCard(:tariffName='line.title', :cost='line.price', :speed='line.speed' traffic='Безлимит', :plan='line.id')
        //- div(v-for='net in comnet' :key='net.id' )
        //-   TariffCard(:tariffName='net.title', :cost='net.price', :speed='net.speed' traffic='Безлимит', :plan='net.id')
        //- div(v-for='ps in tps' :key='ps.id' )
        //-   TariffCard(:tariffName='ps.title', :cost='ps.price', :speed='ps.speed' traffic='Безлимит', :plan='ps.id')
        //- div(v-for='link in istv' :key='link.id' )
        //-   TariffCard(:tariffName='link.title', :cost='link.price', :speed='link.speed' traffic='Безлимит', :plan='link.id')

         

</template>
<script>
export default {
  data() {
    return {
      plans: [],
      // flink: [],
      options: {
        type: 'loop',
        rewind: true,
        width: '100%',
        // gap: '25px',

        perPage: 4,
        padding: '20px',
      },
    }
  },
  async fetch() {
    this.plans = await this.$axios.$get('https://internetbor.uz/api/v1/plans/')
    // console.log(this.plans)
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
    // margin-left: 15px;
    // margin-bottom: 30px;
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
}
:deep(.splide__arrow--prev) {
  left: 0rem;
  // right: 0rem;
}
:deep(.splide__arrow--next) {
  right: 0rem;
  // right: 0rem;
}
:deep(.splide__pagination) {
  bottom: -1rem;
}
</style>
