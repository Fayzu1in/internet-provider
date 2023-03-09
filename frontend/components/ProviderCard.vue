<template lang="pug">
section.Providers.container-fluid
      .provider
        .provider__title Freelink
        div(v-for='plan in plans' :key='plan.id' )
          TariffCard(:tariffName='plan.title', :cost='plan.price', :speed='plan.speed' traffic='Безлимит', :plan='plan.id')
       



    
    

</template>
<script>
// import axios from 'axios'
export default {
  data() {
    return {
      plans: null,
    }
  },

  async fetch() {
    const ip = await this.$axios.$get('http://127.0.0.1:8000/plans')
    this.plans = ip
    console.log(this.plans)
  },
  // mounted() {
  //   axios
  //     .get('http://127.0.0.1:8000/plans')
  //     .then((response) => (this.info = response))
  // },
}
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
