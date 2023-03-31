<template lang="pug">
section.container-fluid
  .providers
    .provider
      .provider__title {{ providerName }}
      div(v-for='current in currentProvider' :key='current.id' )
        TariffCard(:tariffName='current.title', :cost='current.price', :speed='current.speed' traffic='Безлимит', :plan='current.id')

  

</template>
<script>
export default {
  data() {
    return {
      providerID: this.$route.params.id,
      providerName: this.topProviders,
      plans: [],
    }
  },

  async fetch() {
    this.topProviders = await this.$axios.$get(
      `https://internetbor.uz/api/v1/providers/${this.providerID}`
    )
    this.providerName = this.topProviders.name
    // console.log(this.providerName)

    this.plans = await this.$axios.$get('https://internetbor.uz/api/v1/plans/')
    // console.log(this.plans)
  },
  computed: {
    currentProvider() {
      return this.plans.filter((index) => {
        return index.provider === this.providerName.toLowerCase()
      })
    },
  },
}
</script>
<style lang="scss" scoped>
.providers {
  margin-top: 100px;
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
      @media only screen and (max-width: 420px) {
        font-size: 24px;
      }
    }
  }
}
</style>
