<template lang="pug">
main
  AddressSection
  section.topProvider
    .Title 
      p.Title__top Топ провайдеров 
      //- img.fireImg(src='@/static/star.png')
    .topProviders__card
  section.betterOffer
    TopProviders
    .Title 
      p.Title__top  Лучшие тарифы месяца
      p.Title__bottom по версии портала INTERNETBOR
      //- img.fireImg(src='@/static/fire.png')
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
  padding-top: 30px;
  @media only screen and (max-width: 420px) {
    padding-top: 20px;
  }

  .Title {
    // display: flex;
    // align-items: center;
    text-align: center;
    &__top {
      padding-top: 30px;
      font-size: 32px;
      margin: 0;
      font-weight: bold;
      text-transform: uppercase;
    }
    &__bottom {
      font-size: 18px;
      margin: 0;
      padding-top: 10px;
    }

    .fireImg {
      height: 35px;
      padding-left: 10px;
      @media only screen and (max-width: 420px) {
        height: 25px;
      }
    }
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
  margin-top: 30px;
  @media only screen and (max-width: 420px) {
    margin-top: 20px;
  }
}
</style>
