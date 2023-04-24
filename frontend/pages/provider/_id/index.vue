<template lang="pug">
section.container-fluid.tariffWrapperr
  .tariff
    .tariff__title
      p {{ providerName }}
    .tariff__cards
      div(v-for='tariff in data' :key='tariff.id' )
        BetterofferCard.card(:router='tariff.router' :hot='tariff.is_hot' :image='tariff.provider_picture' :name='tariff.title' :nSpeed='tariff.night' :tech='tariff.tech' :speed='tariff.speed' :price='tariff.price' :message='tariff.id')
      



  

</template>
<script>
export default {
  data() {
    return {
      providerID: this.$route.params.id,
      providerName: this.topProviders,
      // plans: [],
      data: null,
    }
  },

  async fetch() {
    this.data = await this.$axios.$get(
      // `https://internetbor.uz/api/v1/providers/${this.providerID}`
      `https://internetbor.uz/api/v1/plans/?provider=${this.providerID}`
    )
    // console.log(this.data)
    this.providerName = this.data[0].provider_name
    // console.log(this.providerName)

    // this.plans = await this.$axios.$get('https://internetbor.uz/api/v1/plans/')
    // console.log(this.plans)
  },
  computed: {
    // currentProvider() {
    //   return this.plans.filter((index) => {
    //     return index.provider === this.providerName.toLowerCase()
    //   })
    // },
  },
}
</script>
<style lang="scss" scoped>
.tariffWrapperr {
  display: flex;
  justify-content: center;
}
.tariff {
  max-width: 1120px;

  width: 100%;
  margin-top: 100px;
  background-color: #00000096;
  padding: 15px 20px;
  display: flex;
  border-radius: 5px;
  flex-wrap: wrap;
  backdrop-filter: blur(10px);

  flex-direction: column;
  &__title {
    font-size: 32px;

    text-align: center;
    font-weight: bold;
    @media only screen and (max-width: 431px) {
      font-size: 24px;
    }
  }
  &__cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;
    @media only screen and (max-width: 431px) {
      justify-content: center;
    }
    .card {
      margin-right: 10px;
      margin-left: 10px;
      margin-top: 10px;
    }
  }
}
</style>
