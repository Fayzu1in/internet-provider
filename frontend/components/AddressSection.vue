<template lang="pug">
section.address
  .container-fluid
  .address__top {{ $t('InternetprovidersofUzbekistan') }}
  .address__middle {{ $t('enterAddressSubtitle') }}
  .address__bottom
    AddressForm
</template>
<script>
export default {}
</script>
<style lang="scss" scoped>
// tetstatsaas
.address {
  padding-top: 100px;

  @media only screen and (max-width: 420px) {
    padding-top: 70px;
  }

  &__top {
    font-size: 32px;
    font-weight: 600;
    text-align: center;
    @media only screen and (max-width: 420px) {
      font-size: 24px;
      // text-align: left;
    }
  }
  &__middle {
    margin: 0 auto;
    text-align: center;
    max-width: 800px;
    width: 100%;
    color: #ffffff;
    padding-top: 15px;
    font-size: 18px;
    @media only screen and (max-width: 420px) {
      font-size: 16px;
      // text-align: left;
      padding-top: 10px;
    }
  }
}
</style>
