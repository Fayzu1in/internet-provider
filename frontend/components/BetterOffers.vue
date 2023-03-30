<template lang="pug">
//- Splide(:options="options" aria-label="Vue Splide Example")
//-   SplideSlide
section.betterOffers
  div.betterOffers__card(v-for='offer in offers' :key="offers.id")
    NuxtLink.betterOffers__card-link(:to='(`/request/${offer.id}` )')
      BetterofferCard(:provider='offer.provider', :title='offer.name', :speed='offer.speed', :price='offer.price')



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
    this.bestOffers = await this.$axios.$get(
      'http://internetbor.uz/api/v1/offers'
    )
    console.log(this.bestOffers)
    this.bestOffers = this.bestOffers[0].plans
    const [first, second, third] = this.bestOffers
    // console.log(this.first)
    this.first = await this.$axios.$get(
      `http://internetbor.uz/api/v1/plans/${first}`
    )
    this.second = await this.$axios.$get(
      `http://internetbor.uz/api/v1/plans/${second}`
    )
    this.third = await this.$axios.$get(
      `http://internetbor.uz/api/v1/plans/${third}`
    )
    this.offers.push(this.first)
    this.offers.push(this.second)
    this.offers.push(this.third)

    // console.log(this.offers)
  },
}
</script>
<style lang="scss">
.betterOffers {
  display: flex;
  text-decoration: none;
  @media only screen and (max-width: 420px) {
    flex-direction: column;
  }
  &__card {
    margin-left: 30px;
    margin-right: 30px;
    @media only screen and (max-width: 420px) {
      margin-left: 0;
      margin-right: 0;
      margin-bottom: 15px;
    }
    &-link {
      text-decoration: none;
    }
  }
}
</style>
