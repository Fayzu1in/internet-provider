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
<style lang="scss">
.address {
  padding-top: 100px;
  &__top {
    font-size: 52px;
    font-weight: 600;
    text-align: center;
  }
  &__middle {
    margin: 0 auto;
    text-align: center;
    max-width: 800px;
    width: 100%;
    color: #ffffff;
    padding-top: 20px;
    font-size: 20px;
  }
}
</style>
