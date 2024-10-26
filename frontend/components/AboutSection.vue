<template lang="pug">
.container-fluid
  .AboutCompany
    .AboutCompany__top
      .AboutCompany__top-left
        .connect {{ $t('aboutUs') }}
        .title  {{ $t('bestService') }}
        .subtitle {{ $t('quickConvenientSearch') }}
      .AboutCompany__top-right
        img(src='/wiki.png')
    .AboutCompany__bottom
      .AboutCompany__bottom-top
        .aboutTextCard
          .aboutTextCard-top
            img(src='/gayka.png')
          .aboutTextCard-title {{ $t('convenientTools') }}
          .aboutTextCard-subtitle {{ $t('ourExperiencedTeam') }}
        .aboutTextCard
          .aboutTextCard-top
            img(src='/cart.png')
          .aboutTextCard-title {{ $t('profitableOffers') }}
          .aboutTextCard-subtitle {{ $t('optimalTariff') }}
      .AboutCompany__bottom-btm
        .aboutTextCard
          .aboutTextCard-top
            img(src='/location.png')
          .aboutTextCard-title {{ $t('searchByAddress') }}
          .aboutTextCard-subtitle {{ $t('filteredOffers') }}

        

      
</template>
<script>
export default {}
</script>
<style lang="scss">
.AboutCompany {
  padding-bottom: 45px;
  padding-top: 48px;
  @media only screen and (max-width: 576px) {
    padding-top: 0;
    padding-bottom: 0;
  }
  &__top {
    display: flex;
    padding-top: 65px;
    align-items: center;
    padding-bottom: 93px;
    @media only screen and (max-width: 576px) {
      flex-direction: column;
      padding-top: 0;

      display: none;
    }

    &-left {
      color: #fff;
      .connect {
        width: fit-content;
        font-size: 11px;
        color: #2e363e;
        padding: 10px 18px;
        background-color: #fff;
        border-radius: 5px;
        font-family: 'Montserrat', sans-serif;
      }
      .title {
        font-size: 45px;
        padding-top: 24px;
        font-weight: bold;
        line-height: 60px;
        padding-bottom: 14px;
        font-family: 'Raleway', sans-serif;
      }
      .subtitle {
        font-family: 'Montserrat', sans-serif;
        font-size: 20px;
        font-weight: 200;
      }
    }
    &-right {
      display: flex;
      justify-content: flex-end;
      img {
        height: 325px;
        width: 353px;
      }
    }
  }
  &__bottom {
    &-top {
      display: flex;
      justify-content: center;
      @media only screen and (max-width: 576px) {
        flex-direction: column;
        align-items: center;
        justify-content: center;
      }
    }
    &-btm {
      margin-top: 35px;
      display: flex;
      justify-content: center;
      @media only screen and (max-width: 576px) {
        margin-top: 0;
      }
    }
  }
}
.aboutTextCard {
  max-width: 380px;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #fff;
  border-radius: 30px;
  text-align: center;
  padding: 40px;
  margin-left: 10px;
  margin-right: 10px;
  @media only screen and (max-width: 576px) {
    margin-bottom: 20px;
    min-width: 375px;
  }
  &-top {
    width: auto;
    img {
      height: 40px;
      width: auto;
    }
  }
  &-title {
    color: #2e363e;
    font-size: 20px;
    font-weight: 500;
    padding-top: 24px;
    padding-bottom: 10px;
  }
  &-subtitle {
    color: #2e363e;
    font-size: 14px;
  }
}
</style>
