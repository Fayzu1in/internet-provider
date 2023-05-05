<template lang="pug">
main
  AddressSection
  section.topProvider
    .Title 
      p.Title__top {{ $t('topProviders') }}

    .topProviders__card
  section.betterOffer
    TopProviders
    .Title 
      p.Title__top  {{ $t('bestTariffOfMonth') }}
      p.Title__bottom {{ $t('accordingTo') }}

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
  @media only screen and (max-width: 431px) {
    padding-top: 0px;
  }

  .Title {
    text-align: center;
    &__top {
      padding-top: 30px;
      font-size: 32px;
      margin: 0;
      font-weight: bold;
      text-transform: uppercase;
      @media only screen and (max-width: 431px) {
        padding-bottom: 20px;
      }
    }
    &__bottom {
      font-size: 18px;
      margin: 0;
      padding-top: 10px;
    }

    .fireImg {
      height: 35px;
      padding-left: 10px;
      @media only screen and (max-width: 431px) {
        height: 25px;
      }
    }
    @media only screen and (max-width: 431px) {
      text-align: center;
      font-size: 22px;
    }
  }
}
.topProvider {
  padding-top: 0;
}
.tariffCards {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 30px;
  @media only screen and (max-width: 431px) {
    margin-top: 20px;
  }
}
</style>
