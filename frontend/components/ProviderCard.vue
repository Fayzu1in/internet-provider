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
         



    
    

</template>
<script>
// import axios from 'axios'
export default {
  data() {
    return {
      plans: [],
      flink: [],
    }
  },
  async fetch() {
    const ip = await this.$axios.$get('http://127.0.0.1:8000/api/v1/plans')
    this.plans = ip
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
  },
}

// let freelink = this.plans.filter(function(index){
//     return index.provider === 'freelink'
//    })
</script>
<style lang="scss" scoped>
.Providers {
  background-color: #00000096;
  padding: 15px 10px;
  display: flex;
  border-radius: 5px;
  display: flex;
  flex-direction: column;

  .provider {
    margin-left: 15px;
    margin-bottom: 30px;
    &__title {
      font-size: 32px;
      padding-bottom: 30px;
      text-align: center;
      font-weight: bold;
    }
  }
}
</style>
