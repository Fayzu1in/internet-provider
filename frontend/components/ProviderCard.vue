<template lang="pug">
section.Providers.container-fluid
      .provider
        .provider__title Freelink
        div(v-for='link in freelink' :key='link.id' )
          TariffCard(:tariffName='link.title', :cost='link.price', :speed='link.speed' traffic='Безлимит', :plan='link.id')
        .provider__title Uzonline 
        div(v-for='line in uzonline' :key='line.id' )
          TariffCard(:tariffName='line.title', :cost='line.price', :speed='line.speed' traffic='Безлимит', :plan='line.id')
        .provider__title Comnet 
        div(v-for='net in comnet' :key='net.id' )
          TariffCard(:tariffName='net.title', :cost='net.price', :speed='net.speed' traffic='Безлимит', :plan='net.id')
        .provider__title TPS 
        div(v-for='ps in tps' :key='ps.id' )
          TariffCard(:tariffName='ps.title', :cost='ps.price', :speed='ps.speed' traffic='Безлимит', :plan='ps.id')
        .provider__title ISTV 
        div(v-for='link in istv' :key='link.id' )
          TariffCard(:tariffName='link.title', :cost='link.price', :speed='link.speed' traffic='Безлимит', :plan='link.id')

         

</template>
<script>
export default {
  data() {
    return {
      plans: [],
      // flink: [],
    }
  },
  async fetch() {
    this.plans = await this.$axios.$get('http://internetbor.uz/api/v1/plans/')
    console.log(this.plans)
  },
  computed: {
    freelink() {
      return this.plans.filter((index) => {
        return index.provider === 'freelink'
      })
    },
    uzonline() {
      return this.plans.filter((index) => {
        return index.provider === 'uzonline'
      })
    },
    comnet() {
      return this.plans.filter((index) => {
        return index.provider === 'comnet'
      })
    },
    tps() {
      return this.plans.filter((index) => {
        return index.provider === 'tps'
      })
    },
    istv() {
      return this.plans.filter((index) => {
        return index.provider === 'istv'
      })
    },
  },
}
</script>
<style lang="scss" scoped>
.Providers {
  background-color: #00000096;
  box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;

  padding: 15px 10px;
  display: flex;
  border-radius: 5px;
  display: flex;
  flex-direction: column;

  .provider {
    margin-left: 15px;
    // margin-bottom: 30px;
    &__title {
      font-size: 32px;
      padding-bottom: 30px;
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
</style>
