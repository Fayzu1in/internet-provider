<template lang="pug">
//- Splide(:options="options" aria-label="Vue Splide Example")
//-   SplideSlide
section.betterOffers
  div.betterOffers__card(v-for='offer in bestOffers' :key="bestOffers.plan_id")
    NuxtLink.betterOffers__card-link(:to='(`/request/${offer.plan_id}` )')
      BetterofferCard.offerCard(:router='offer.router' :hot='offer.is_hot' :image='offer.provider_picture', :name='offer.title', :speed='offer.speed', :nSpeed='offer.night' :tech='offer.tech' :price='offer.price' :message='offer.plan_id')
      //- BetterofferCard.card(image='/freelink.png' :name='tariff.title' :nSpeed='tariff.night' :tech='tariff.tech' :speed='tariff.speed' :price='tariff.price' :message='tariff.id')




</template>
<script>
export default {
  props: {
    src: {
      type: String,
      default: null,
    },
  },
  data() {
    return {
      bestOffers: [],
      offers: [],
      first: '',
      second: '',
      third: '',
      options: {
        rewind: true,
        width: 800,
        perPage: 3,
        gap: '0.5rem',
        perMove: 2,
        type: 'loop',
      },
    }
  },
  async fetch() {
    this.offers = await this.$axios.$get('https://internetbor.uz/api/v1/offers')
    this.bestOffers = this.offers[0].plans
    console.log(this.bestOffers)

    // this.bestOffers = this.bestOffers[0].plans
    // const [first, second, third] = this.bestOffers
    // // console.log(this.first)
    // this.first = await this.$axios.$get(
    //   `https://internetbor.uz/api/v1/plans/${first}`
    // )
    // this.second = await this.$axios.$get(
    //   `https://internetbor.uz/api/v1/plans/${second}`
    // )
    // this.third = await this.$axios.$get(
    //   `https://internetbor.uz/api/v1/plans/${third}`
    // )
    // this.offers.push(this.first)
    // this.offers.push(this.second)
    // this.offers.push(this.third)

    // console.log(this.offers)
  },
}
</script>
<style lang="scss">
.betterOffers {
  display: flex;
  text-decoration: none;
  @media only screen and (max-width: 431px) {
    flex-direction: column;
  }
  &__card {
    margin-left: 30px;
    margin-right: 30px;
    @media only screen and (max-width: 431px) {
      margin-left: 0;
      margin-right: 0;
      margin-bottom: 15px;
    }
    &-link {
      text-decoration: none;
    }
  }
  .offerCard {
    transition: all 0.3s;
    &:hover {
      transform: scale(1.1);
    }
  }
}
</style>
