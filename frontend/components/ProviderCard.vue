<template lang="pug">
section.Providers
  .provider 
    template(v-for='provider in groups')
      //- .providersText {{ $t('providers') }}
      .provider__title {{ provider.provider_name }}
      VueGlide.desktopSlide(v-if="provider.plans?.length" :options='options')
        VueGlideSlide(v-for='link in provider.plans' :key='link.id')
          NuxtLink.providerLink(:to='localePath(`/request/${link.id}` )')
            BetterofferCard(:router='link.router' :hot='link.is_hot' :image='link.provider_picture' :name='link.title' :tech='link.tech' :nSpeed='link.night' :speed='link.speed' :price='link.price' :message='link.id')
        template(slot='control' )
          button.glide__arrow.glide__arrow--left(data-glide-dir='<') 
            MaterialIcon(:icon='mdiChevronLeft' )
          button.glide__arrow.glide__arrow--right(data-glide-dir='>') 
            MaterialIcon(:icon='mdiChevronRight')
      .mobileSlide
        div(v-for='link in provider.plans' :key='link.id')
          NuxtLink.providerLink(:to='localePath(`/request/${link.id}` )')
            BetterofferCard(:router='link.router' :hot='link.is_hot' :image='link.provider_picture' :name='link.title' :tech='link.tech' :nSpeed='link.night' :speed='link.speed' :price='link.price' :message='link.id')
</template>
<script>
import { mdiChevronRight, mdiChevronLeft } from '@mdi/js'
export default {
  data() {
    return {
      mdiChevronRight,
      mdiChevronLeft,
      plans: [],
      options: {
        perView: 3,
        keyboard: false,
        bound: true,
        breakpoints: {
          800: {
            perView: 2,
          },
          550: {
            perView: 1,
          },
        },
      },
    }
  },
  async fetch() {
    try {
      const res = await this.$api.getPlans()
      this.plans = res
    } catch (error) {
      console.error('Failed to fetch plans:', error)
    }
  },
  computed: {
    groups() {
      return this.plans.reduce((acc, cur) => {
        const provider = acc.find((c) => c.provider_id === cur.provider_id)

        if (provider) {
          provider.plans.push(cur)
        } else {
          acc.push({
            provider_id: cur.provider_id,
            provider_name: cur.provider_name,
            plans: [cur],
          })
        }

        return acc
      }, [])
    },
  },
}
</script>
<style lang="scss" scoped>
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
  justify-content: space-around !important;
}

.Providers {
  display: flex;
  flex-direction: column;
  max-width: 1250px;
  width: 100%;
  margin: 0 auto;
  @media only screen and (max-width: 431px) {
    padding-left: 20px;
    padding-right: 20px;
    padding-bottom: 60px;
  }
  /* @media only screen and (max-width: 431px) {
  } */

  .provider {
    .providersText {
      width: fit-content;
      font-size: 11px;
      color: #2e363e;
      padding: 10px 18px;
      background-color: #fff;
      border-radius: 5px;
      margin-left: 30px;
      margin-top: 50px;
      @media only screen and (max-width: 531px) {
        margin-left: 0;
        margin-top: 0;
        margin-bottom: 15px;
      }
    }
    &__title {
      font-size: 32px;
      margin-left: 30px;
      margin-bottom: -20px;
      padding-top: 0;
      text-align: left;
      font-weight: bold;
      padding-top: 25px;
      padding-bottom: 20px;

      @media only screen and (max-width: 431px) {
        font-size: 24px;
        padding-bottom: 0px;
        margin: 0;
        padding-top: 0;
      }
    }
    .providerLink {
      text-decoration: none;
      /* color: #000; */
    }
  }
}
.desktopSlide {
  @media only screen and (max-width: 531px) {
    display: none;
  }
}
.mobileSlide {
  display: none;
  @media only screen and (max-width: 531px) {
    display: flex;
    overflow: auto;
  }
  &::-webkit-scrollbar {
    display: none;
  }
}
/* .card {
  width: 300px;
  height: 300px;
  background-color: #fff;
} */
</style>
