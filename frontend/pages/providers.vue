<template lang="pug">
section.providers 
  ScrollTop
  h1 {{ $t('internetProviders') }}
  ProviderCard
</template>
<script>
export default {}
</script>
<style lang="scss" scoped>
.providers {
  padding-top: 60px;
  h1 {
    text-align: center;
    font-size: 40px;
    @media only screen and (max-width: 431px) {
      font-size: 24px;
      margin: 0;
      padding-bottom: 20px;
    }
  }
}
</style>
