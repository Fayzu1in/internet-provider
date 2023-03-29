<template lang="pug">
section.address
  .container-fluid
  .address__top Интернет провайдеры Ташкента
  .address__middle Укажите адрес проживания, чтобы мы определили доступные к подключению провайдеры по их зоне предоставления услуг.
  .address__bottom
    AddressForm
</template>
<script>
export default {}
</script>
<style lang="scss" scoped>
.address {
  padding-top: 100px;

  @media only screen and (max-width: 420px) {
    padding-top: 70px;
  }

  &__top {
    font-size: 52px;
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
    padding-top: 20px;
    font-size: 20px;
    @media only screen and (max-width: 420px) {
      font-size: 16px;
      // text-align: left;
      padding-top: 10px;
    }
  }
}
</style>
