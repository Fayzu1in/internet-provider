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
  section.allplaySection
    a(href='https://allplay.uz/profile/subscription' target='_blank').allplay
      img.allplay__logo(src='/allplay.png')
      img.allplay__bckg(src='/foreign-xl.png')
      .allplay__title АКЦИЯ
      .allplay__subtitle Приобрети первую подписку всего за 199 сум

</template>

<script>
export default {}
</script>
<style lang="scss" scoped>
.allplaySection {
  padding-top: 30px;
  @media only screen and (max-width: 431px) {
    padding-top: 15px;
  }
  .allplay {
    max-width: fit-content;
    width: 100%;
    // height: 250px;
    border: 1px solid grey;
    margin: 0 auto;
    border-radius: 5px;
    display: flex;
    // justify-content: center;
    align-items: center;
    overflow: hidden;
    flex-direction: column;
    color: #fff;
    text-decoration: none;
    &__logo {
      height: 60px;
      margin-top: 15px;
      @media only screen and (max-width: 431px) {
        height: 40px;
      }
    }
    &__bckg {
      height: 60px;
      margin-top: 15px;
      margin-bottom: 15px;
      @media only screen and (max-width: 431px) {
        // display: none;
        width: 100%;
        height: unset;
      }
    }
    &__title {
      font-size: 28px;
      padding-bottom: 5px;
      @media only screen and (max-width: 431px) {
        font-size: 22px;
      }
    }
    &__subtitle {
      font-size: 20px;
      padding-bottom: 15px;
      color: grey;
      @media only screen and (max-width: 431px) {
        text-align: center;
        font-size: 18px;
        padding: 0 10px;
        padding-bottom: 10px;
      }
    }
  }
}
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
  @media only screen and (max-width: 431px) {
    margin-top: 20px;
  }
}
</style>
