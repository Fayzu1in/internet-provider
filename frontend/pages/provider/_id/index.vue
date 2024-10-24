<template lang="pug">
section.container-fluid.tariffWrapperr
  .tariff
    .providersText {{ $t('providers') }}
    .tariff__title {{ providerName }}
    .tariff__cards
    VueGlide(v-if="data && data.length" :options='options')
      VueGlideSlide(v-for='tariff in data' :key='tariff.id' )
        NuxtLink.tariffLink(:to='localePath(`/request/${tariff.id}` )')
          BetterofferCard.card(:router='tariff.router' :hot='tariff.is_hot' :image='tariff.provider_picture' :name='tariff.title' :nSpeed='tariff.night' :tech='tariff.tech' :speed='tariff.speed' :price='tariff.price' :message='tariff.id')
      template(slot='control' )
        button.glide__arrow.glide__arrow--left(data-glide-dir='<') 
          MaterialIcon(:icon='mdiChevronLeft' )
        button.glide__arrow.glide__arrow--right(data-glide-dir='>') 
          MaterialIcon(:icon='mdiChevronRight')
</template>
<script>
import { mdiChevronRight, mdiChevronLeft } from '@mdi/js'

export default {
  data() {
    return {
      providerID: this.$route.params.id,
      providerName: this.topProviders,
      data: null,
      mdiChevronRight,
      mdiChevronLeft,
    }
  },

  async fetch() {
    this.data = await this.$axios.$get(
      `https://internetbor.uz/api/v1/plans/?provider=${this.providerID}`
    )
    this.providerName = this.data[0].provider_name
  },
}
</script>
<style lang="scss" scoped>
* {
  width: auto;
}
.tariffWrapperr {
  display: flex;
  justify-content: center;
}
.tariff {
  display: flex;
  flex-direction: column;
  margin: 0 auto;
  margin-top: 120px;
  .providersText {
    width: fit-content;
    font-size: 11px;
    color: #2e363e;
    padding: 10px 18px;
    background-color: #fff;
    border-radius: 5px;
    margin-left: 30px;
    margin-top: 50px;
  }
  &__title {
    font-size: 32px;
    margin-left: 30px;
    margin-bottom: -20px;
    padding-top: 0;
    text-align: left;
    font-weight: bold;
    padding-top: 25px;
    padding-bottom: 55px;
  }
  &__cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;
    @media only screen and (max-width: 431px) {
      justify-content: center;
    }
    .card {
      margin-right: 10px;
      margin-left: 10px;
      margin-top: 10px;
    }
  }
  .tariffLink {
    text-decoration: none;
  }
}
:deep(div[data-glide-el='controls']) {
  position: absolute;
  left: 0;
  right: 0;
  top: 40%;
}

.glide__arrow--left,
.glide__arrow--right {
  position: absolute;
  border: 0;
  outline: 0;
  padding: 10px;
  border-radius: 3px;
  background: #56c1ff;
  opacity: 0.7;
  color: #fff;
  cursor: pointer;
  transition: opacity, 0.3s;
}
.glide__arrow--left {
  /* // :deep(button[data-glide-dir='<']) {
  // } */

  left: -35px;

  &:hover {
    opacity: 1;
  }
}
.glide__arrow--right {
  right: -35px;

  &:hover {
    opacity: 1;
  }
}
.glide__slide {
  width: 350px !important;
  padding-top: 20px;
}
:deep(.glide__slides) {
  display: flex !important;
  width: 100% !important;
  justify-content: space-around !important;
}
</style>
