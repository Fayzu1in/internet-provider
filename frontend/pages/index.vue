<template lang="pug">
main
  AddressSection
  section.topProvider
    .Title 
      p Топ провайдеров 
      //- img.fireImg(src='@/static/star.png')
    .topProviders__card
  section.betterOffer
    TopProviders
    .Title 
      p  Выгодные предложения
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
  padding-top: 50px;
  @media only screen and (max-width: 420px) {
    padding-top: 20px;
  }

  .Title {
    font-size: 32px;
    margin: 0;
    display: flex;
    align-items: center;
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
  margin-top: 50px;
  @media only screen and (max-width: 420px) {
    margin-top: 20px;
  }
}
</style>
