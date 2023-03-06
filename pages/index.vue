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
      SplideCard

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
  padding-bottom: 50px;
  h1 {
    font-size: 48px;
    line-height: 0;
  }
}
.tariffCards {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  margin-top: 60px;
}
</style>
