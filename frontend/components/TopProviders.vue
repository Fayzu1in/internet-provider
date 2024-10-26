<template lang="pug">
section.topProviders
  div.topCard(v-for="provider in topProviders" :key='provider.provider_id')
    NuxtLink.topProviders__card(:to='localePath(`/provider/${provider.provider_id}` )', :message='topProviders')
      img.topProviders__card-img(:src='provider.provider_picture')

      //- img.topProviders__card-img(:src="`/api${provider.provider_picture}`")
</template>
<script>
export default {
  data() {
    return {
      topProviders: [],
    }
  },
  async fetch() {
    this.topProviders = await this.$axios.$get(
      'https://internetbor.uz/api/v1/top-providers'
    )
    // console.log(this.topProviders)
  },
}
</script>
<style lang="scss" scoped>
.topProviders {
  display: flex;
  justify-content: center;
  align-items: center;
  // padding-bottom: 30px;
  // transition: all 0.6s;
  @media only screen and (max-width: 431px) {
    flex-direction: column;
    padding-bottom: 0;
  }
  .topCard {
    width: 250px;
    height: 125px;
    margin-left: 10px;
    margin-right: 10px;
    @media only screen and (max-width: 431px) {
      display: flex;
      justify-content: center;

      margin: 0 0;
      height: unset;
    }
  }
  &__card {
    &-img {
      background-color: #ffffff;
      height: 100%;
      width: 100%;
      object-fit: contain;
      margin-left: 30px;
      padding: 44px 13px;
      border-radius: 30px;
      transition: transform 0.3s;
      &:hover {
        transform: scale(1.1);
      }
      @media only screen and (max-width: 431px) {
        margin-left: 0;
        padding: 20px;
        height: 200px;
        width: 200px;
        margin-bottom: 15px;
      }
    }
  }
}
</style>
