<template lang="pug">
section.betterOffers
  VueGlide(:options='options' v-if="bestOffers?.length")
    VueGlideSlide.betterOffers__card(v-for='offer in bestOffers' :key="bestOffers.plan_id")
      NuxtLink.betterOffers__card-link(:to='localePath(`/request/${offer.plan_id}` )')
        BetterofferCard.offerCard(:router='offer.router' :hot='offer.is_hot' :image='offer.provider_picture', :name='offer.title', :speed='offer.speed', :nSpeed='offer.night' :tech='offer.tech' :price='offer.price' :message='offer.plan_id')
    template(slot='control')
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
      bestOffers: [],
      offers: [],
      first: '',
      second: '',
      third: '',
      options: {
        perView: 3,
        keyboard: false,
        bound: true,
        breakpoints: {},
      },
      mdiChevronRight,
      mdiChevronLeft,
    }
  },
  async fetch() {
    this.offers = await this.$axios.$get('https://internetbor.uz/api/v1/offers')
    this.bestOffers = this.offers[0].plans
  },
}
</script>
<style lang="scss">
.betterOffers {
  display: flex;
  text-decoration: none;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 15px;

  @media only screen and (max-width: 431px) {
    flex-direction: column;
  }
  &__card {
    margin-left: 30px;
    margin-right: 30px;
    margin-top: 30px;
    width: fit-content;
    @media only screen and (max-width: 431px) {
      margin-left: 0;
      margin-right: 0;
      margin-bottom: 15px;
    }
    &-link {
      text-decoration: none !important;
    }
  }
  .offerCard {
    transition: all 0.3s;
    // &:hover {
    //   transform: scale(1.1);
    // }
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
  width: auto;
  position: absolute;
  border: 0;
  outline: 0;
  padding: 10px;
  border-radius: 50%;
  background: #3f62a7;
  opacity: 0.7;
  color: #fff;
  cursor: pointer;
  transition: opacity, 0.3s;
}
.glide__arrow--left {
  left: 44%;
}
.glide__arrow--right {
  right: 44%;
}
</style>
