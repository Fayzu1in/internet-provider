<template lang="pug">
main 
  AddressField
  section.topProviders
    h1 Топ провайдеров 
    .topProviders__card
      ProvidersCard(src="././uzonline.png")
      ProvidersCard(src="././comnet.png")
      ProvidersCard(src="././freelink.png")
  section.topProviders
    h1 Выгодные предложения
    .tariffCards.container-fluid
      TariffcardCarousel

</template>

<script>
export default {}
</script>
<style lang="scss" scoped>
.topProviders {
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
  &__card {
    margin-top: 60px;
    display: flex;
    justify-content: center;
  }
}
.tariffCards {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  margin-top: 60px;
}
</style>
