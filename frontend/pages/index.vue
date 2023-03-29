<template lang="pug">
main
  AddressSection
  section.topProvider
    h1 Топ провайдеров 
    .topProviders__card
  section.betterOffer
    TopProviders
    h1 Выгодные предложения
    .tariffCards.container-fluid
      BetterOffers

</template>

<script>
export default {}
</script>
<style lang="scss" scoped>
.topProvider,
.betterOffer {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  padding-top: 60px;
  @media only screen and (max-width: 420px) {
    padding-top: 20px;
  }

  h1 {
    font-size: 48px;
    line-height: 0;
    @media only screen and (max-width: 420px) {
      text-align: center;
      font-size: 22px;
    }
  }
}
.tariffCards {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 60px;
  @media only screen and (max-width: 420px) {
    margin-top: 20px;
  }
}
</style>
