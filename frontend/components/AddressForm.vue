<template lang="pug">
section.addressFormSection
  .modalRequest.foundedProviders(v-if='switc' :class='{switc}')
    .closeModal(@click='switc = false')
      MaterialIcon(:icon='mdiCloseCircleOutline') 
    .modalRequest__top
      p.title {{ $t('congratulations') }} 
      p.subtitle {{ $t('availableProviders') }}
    .modalRequest__middle
      div.availableCard(v-for="available in availableProviders", v-if='available.provider_id !== 6') 
        NuxtLink.availableProvider(:to='localePath(`/provider/${available.provider_id}/`)') 
          img.providerLogo(:src="`${available.provider_picture}`")
    .modalRequest__bottom
      p.subtitle.subBottom {{ $t('favorableTariff') }}
      VueGlide(:options='options' v-if="bestOfAvailable?.length")
        VueGlideSlide(v-for="best in bestOfAvailable" :key="best.plan_id", v-if='best.provider_id !== 6')
          BetterofferCard(:router='best.router' :hot='best.is_hot' :image='best.provider_picture' :name='best.plan_name' :price='best.plan_price' :speed='best.plan_speed' :nSpeed='best.night' :tech='best.tech' :message='best.plan_id')
        template(slot='control')
          button.glide__arrow.glide__arrow--left(data-glide-dir='<') 
            MaterialIcon(:icon='mdiChevronLeft' )
          button.glide__arrow.glide__arrow--right(data-glide-dir='>') 
            MaterialIcon(:icon='mdiChevronRight')
      .help
        p {{$t('callUsForHelp')}}
        .help__phone(@click='callCatcher') 
          img(src='/phone.png')
          p {{ $t('call') }}
  .modalRequest(v-if="notFounded")
    .notFounded 
      .closeModal(@click="notFounded = false")
        MaterialIcon(:icon='mdiCloseCircleOutline')
      .notFounded__top 
        p.notFounded__top-title {{ $t('oops') }} :(
        p.notFounded__top-subtitle {{ $t('registered') }}
      .notFounded__middle 
        p.notFounded__middle-title {{ $t('leavePhone') }}
        form.notFoundedForm(action="" method="post", @submit.prevent="notFoundedForm")
          input.notFoundedForm__inputPhone( v-maska data-maska='+998 (##) ### ## ##' name='phone' v-model="phoneNumberOfNotFounded.phone" required)
          button.notFoundedForm__sendBtn {{$t('send')}}
      .notFounded__bottom(v-if="providersByStreet?.length")
        p.notFounded__bottom-title {{ $t('availableAtStreet') }}
        div.availableByStreets
          div.availableCard(v-for="provider in providersByStreet") 
            NuxtLink.availableProvider(:to='localePath(`/provider/${provider.provider_id}/`)') 
              img.providerLogo(:src="`${provider.provider_picture}`")        


  form.addressForm(action="" method="post", @submit.prevent="formSubmit")
    label.inputWrapper(for='city')
      input.addressForm__field(type='text' :placeholder=`$t('city')` required v-model="inputCity" @input="showCities = inputCity.length > 0" @click="showCities = !showCities, showDistrict = false, showStreets = false" )
      ul.suggestionList(v-if='showCities')
        div(v-if="$fetchState.pending")  
          loader.loader( object="#EBA026" size="3" speed="2" objectbg="#999793" opacity="80" disableScrolling="false" name="spinning")
        div(v-else) 
          li.suggestionItem(v-for="city in city" @click="selectCity(city.city)") {{ city.city }}

    label.inputWrapper(for='street')
      input.addressForm__field(type='text' :placeholder=`$t('district')` required v-model="inputDistrict" @input="showDistrict = inputDistrict.length > 0" @click='suggestion' :disabled="isSecondDisabled" )
      ul.suggestionList(v-if="showDistrict" )
        li.suggestionItem(v-for="district in district"  @click="selectDistrict(district.district)") {{ district.district }}

    label.inputWrapper(for='street')
      input.addressForm__field(type='text' :placeholder=`$t('street')` required v-model="inputStreets" @input="showStreets = inputStreets.length > 0" @click="showStreets = !showStreets, showCities = false, showHouses = false, showDistrict = false" :disabled="isThirdDisabled" )
      ul.suggestionList(v-if="showStreets")
        li.suggestionItem(v-for="str in street"  @click="selectStreet(str.street)") {{ str.street }}

    label.inputWrapper(for='house')
      input.addressForm__field(type='text' :placeholder=`$t('house')` required v-model="inputHouse" @click='showHouses = !showHouses, showStreets = false, showDistrict=false, showCities= false' :disabled="isForthDisabled")
      ul.suggestionList(v-if="showHouses")
        li.suggestionItem(v-for="house in this.housesByStreets" @click="selectHouse(house)" ) {{ house }}
    button.searchProviders {{ loading ? $t('searching') : $t('searchProviders') }}
  div
</template>
<script>
import axios from 'axios'
import {
  mdiCloseCircleOutline,
  mdiPhone,
  mdiChevronRight,
  mdiChevronLeft,
} from '@mdi/js'

export default {
  data() {
    return {
      mdiCloseCircleOutline,
      mdiPhone,
      mdiChevronRight,
      mdiChevronLeft,
      selectedCity: '',
      streets: [],
      inputCity: '',
      inputDistrict: '',
      inputStreets: '',
      inputHouse: '',
      showDistrict: false,
      showCities: false,
      showStreets: false,
      showHouses: false,
      loading: false,
      districtByCities: [],
      streetsByDistrict: [],
      housesByStreets: [],
      topProviders: null,
      providersByStreet: null,
      response: null,
      switc: false,
      modalHelp: false,
      availableProviders: null,
      bestOfAvailable: [],
      notFounded: false,
      center: false,
      phoneNumberOfNotFounded: {
        phone: '+998',
      },
      currentIndex: 0,
      // phoneNumber: '+998',
      modalBckg: false,
      options: {
        perView: 1,
        keyboard: false,
        bound: true,
        breakpoints: {},
      },
    }
  },
  async fetch() {
    this.streets = await this.$axios.$get(
      'https://internetbor.uz/api/v1/coverage-cities/'
    )
  },
  computed: {
    // filteredWords() {
    //   const uniqueWords = this.streets.reduce((acc, word) => {
    //     if (!acc[word.street]) {
    //       acc[word.street] = word
    //     }
    //     return acc
    //   }, {})
    //   return Object.values(uniqueWords).filter((word) => {
    //     return word.street
    //       .toLowerCase()
    //       .includes(this.inputDistrict.toLowerCase())
    //   })
    // },
    city() {
      const uniqueWords = this.streets.reduce((acc, cur) => {
        if (!acc[cur.city]) {
          acc[cur.city] = cur
        }
        return acc
      }, {})

      const cities = Object.values(uniqueWords)

      if (cities.some((c) => c.city === this.inputCity)) {
        return cities
      }

      return cities.filter((cur) => {
        return cur.city.toLowerCase().includes(this.inputCity.toLowerCase())
      })
    },
    district() {
      const uniqueWords = this.districtByCities.reduce((acc, cur) => {
        if (!acc[cur.district]) {
          acc[cur.district] = cur
        }
        return acc
      }, {})

      const districts = Object.values(uniqueWords)

      if (districts.some((d) => d.district === this.inputDistrict)) {
        return districts
      }

      return Object.values(uniqueWords).filter((cur) => {
        return cur.district
          .toLowerCase()
          .includes(this.inputDistrict.toLowerCase())
      })
    },
    street() {
      const uniqueWords = this.streetsByDistrict.reduce((acc, cur) => {
        if (!acc[cur.street]) {
          acc[cur.street] = cur
        }
        return acc
      }, {})
      return Object.values(uniqueWords).filter((cur) => {
        return cur.street
          .toLowerCase()
          .includes(this.inputStreets.toLowerCase())
      })
    },

    isSecondDisabled() {
      return !this.inputCity
    },
    isThirdDisabled() {
      return !this.inputDistrict
    },
    isForthDisabled() {
      return !this.inputStreets
    },
  },

  watch: {
    inputCity(newVal) {
      if (!newVal.length) {
        this.inputDistrict = ''
        this.inputStreets = ''
        this.inputHouse = ''
      }
    },
    inputDistrict(newVal) {
      if (!newVal.length) {
        this.inputStreets = ''
        this.inputHouse = ''
      }
    },
    inputStreets(newVal) {
      if (!newVal.length) {
        this.inputHouse = ''
      }
    },
  },

  mounted() {
    if (this.inputCity.length === 0) {
      this.inputStreets = ''
      this.inputDistrict = ''
      this.inputHouse = ''
    }
  },

  methods: {
    selectCity(word) {
      this.inputDistrict = ''
      this.inputStreets = ''
      this.inputHouse = ''
      this.districtByCities = this.streets.filter((obj) => obj.city === word)
      this.districtByCities = this.districtByCities.reduce((acc, obj) => {
        const foundIndex = acc.findIndex(
          (item) => item.district === obj.district
        )
        if (foundIndex === -1) {
          acc.push(obj)
        } else {
          acc[foundIndex] = obj
        }
        return acc
      }, [])
      this.selectedCity = word
      this.inputCity = word
      this.showCities = false
    },

    selectDistrict(word) {
      this.inputStreets = ''
      this.inputHouse = ''
      this.streetsByDistrict = this.streets.filter(
        (obj) => obj.district === word
      )
      this.streetsByDistrict = this.streetsByDistrict.reduce((acc, obj) => {
        const foundIndex = acc.findIndex((item) => item.street === obj.street)
        if (foundIndex === -1) {
          acc.push(obj)
        } else {
          acc[foundIndex] = obj
        }
        return acc
      }, [])
      // console.log(this.streetsByDistrict)
      this.inputDistrict = word
      this.SuggestionList = false
      this.showDistrict = false
    },
    selectStreet(word) {
      this.inputStreets = word
      this.showStreets = false
      this.housesByStreets = axios
        .get(
          `https://internetbor.uz/api/v1/coverage/?street=${word}&district=${this.inputDistrict}`
        )
        .then((response) => {
          this.housesByStreets = response.data[0].houses
          // console.log(this.housesByStreets)
        })
    },
    suggestion() {
      this.showDistrict = !this.showDistrict
      this.showCities = false
      this.showStreets = false
      this.showHouses = false
    },
    selectHouse(word) {
      this.inputHouse = word
      this.showHouses = false
    },
    // nextSlide() {
    //   this.currentIndex = Math.min(
    //     this.currentIndex + 1,
    //     this.cards.length - this.itemsToShow
    //   )
    // },
    // prevSlide() {
    //   this.currentIndex = Math.max(this.currentIndex - 1, 0)
    // },
    formSubmit() {
      this.loading = true
      axios
        .get(
          // `https://internetbor.uz/api/v1/coverage/?street=${this.inputStreets}`
          // `https://internetbor.uz/api/v1/coverage-check/?street=${this.inputStreets}&house=${this.inputHouse}`
          `https://internetbor.uz/api/v1/coverage-check/?district=${this.inputDistrict}&street=${this.inputStreets}&house=${this.inputHouse}`
        )
        .then((response) => {
          this.response = response.data
          console.dir(this.response)
          // console.log('response', this.response)
          this.inputCity = ''
          this.inputDistrict = ''
          this.inputStreets = ''
          this.inputHouse = ''
          if (this.response.providers !== null) {
            this.switc = true
            this.availableProviders = this.response.providers
            this.showHouses = false
            this.showCities = false
            this.showDistrict = false
            this.showStreets = false
            let result = []
            for (const obj of this.availableProviders) {
              result = result.concat(obj.provider_best)
              this.bestOfAvailable = result
            }
          }

          if (this.response.providers === null) {
            this.notFounded = true
          }
        })
        .catch((error) => {
          console.error('Error:', error)
        })
        .finally(() => {
          this.loading = false
        })
      axios
        .get(
          `https://internetbor.uz/api/v1/coverage/?street=${this.inputStreets}`
        )
        .then((data) => {
          this.providersByStreet = data.data[0].providers
        })
        .catch((error) => {
          console.error('Error:', error)
        })
        .finally(() => {
          this.loading = false
        })
    },
    notFoundedForm() {
      axios
        .post(
          'https://internetbor.uz/api/v1/noaddress-callback/',
          this.phoneNumberOfNotFounded
        )
        .then((response) => {
          // console.log(response)
          this.notFounded = false
        })
    },
    async callCatcher() {
      try {
        await this.$api.clickCatcher('phone call')
      } catch (error) {
        console.error('Error occured', error)
      } finally {
        const phoneNumber = '+998781137071'
        window.location.href = `tel:${phoneNumber}`
      }
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
  border-radius: 50%;
  background: #56c1ff;
  opacity: 0.7;
  color: #fff;
  cursor: pointer;
  transition: opacity, 0.3s;
  @media only screen and (max-width: 431px) {
    padding: 0;
    opacity: unset;
    .MaterialIcon {
      width: 3rem;
      height: 3rem;
      z-index: 1000;
    }
  }
}
.glide__arrow--left {
  /* // :deep(button[data-glide-dir='<']) {
  // } */

  left: 5px;
  @media only screen and (max-width: 431px) {
    left: -5px;
  }

  &:hover {
    opacity: 1;
    // border-radius: 10px;
  }
}
.glide__arrow--right {
  /* // :deep(button[data-glide-dir='>']) {
  // } */

  right: 5px;
  @media only screen and (max-width: 431px) {
    right: -5px;
  }

  &:hover {
    opacity: 1;
  }
}
:deep(.glide__slides) {
  display: flex !important;
  justify-content: space-around !important;
  margin-bottom: 0;
}
.glide__slide {
  padding-top: 11px;
  width: 270px !important;
}
.modalBckg {
  position: fixed;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  background: #0000005f;
}
.foundedProviders {
  transform: translate(30%, -50%);
  @media only screen and (max-width: 431px) {
    transform: translate(0%, 5%) !important;
  }
}

.modalRequest {
  border: 1px solid rgba(128, 128, 128, 0.417);
  position: fixed;
  max-width: 600px;
  width: 100%;
  border-radius: 15px;
  top: 52%;
  z-index: 1001;
  // background-color: #ffffffc3;
  backdrop-filter: blur(10px);
  padding: 10px 20px;
  text-align: center;
  max-height: 100%;
  // transform: translate(50%, -50%);
  color: #001b48;
  @media only screen and (max-width: 431px) {
    overflow: scroll;
    overscroll-behavior: contain;
    // bottom: 70px;
    top: 0px;
    max-height: 100vh;
    width: 90%;
    overflow: scroll;
    // transform: translateY(0);
    // transform: translate(0%, 15%);
  }
  .switc {
    @media only screen and (max-width: 431px) {
      // transform: translate(0%, 10%) !important;
    }
  }

  .closeModal {
    position: absolute;
    right: 10px;
    top: 10px;
    cursor: pointer;
  }

  .subtitle {
    margin: 0;
    padding-top: 5px;
    font-size: 18px;
    padding-bottom: 5px;
    // margin-bottom: 10px;
    @media only screen and (max-width: 431px) {
      font-size: 16px;
      padding-top: 10px;
      // padding-bottom: 10px;
      margin-bottom: 0;
    }
  }
  &__top {
    @media only screen and (max-width: 431px) {
      // padding-top: 30px;
    }
    .title {
      font-size: 32px;
      margin: 0;
      @media only screen and (max-width: 431px) {
        font-size: 24px;
      }
    }
  }
  &__middle {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    .availableCard {
      @media only screen and (max-width: 431px) {
        margin-left: 5px;
        margin-right: 5px;
      }
    }
    .availableProvider {
      border-radius: 5px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding: 3px;
      border: 1px solid rgba(128, 128, 128, 0.417);
      margin-left: 10px;
      margin-right: 10px;
      cursor: pointer;
      &:hover {
        border: 1px dashed #fff;
      }
      @media only screen and (max-width: 431px) {
        margin-left: 0;
        margin-right: 0;
        margin-bottom: 10px;
      }
      .providerLogo {
        object-fit: contain;
        height: 140px;
        background: #fff;
        width: 140px;
        border-radius: 5px;
        object-fit: contain;
      }
      .selectBtn {
        border: none;
        font-size: 18px;
        padding: 5px 0;
        color: #fff;
        background: #56c1ff;
      }
    }
  }
  &__bottom {
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    .splide {
      // margin-top: 20px;
      margin-bottom: 15px;
    }
    .subBottom {
      // margin-top: 0px;
      @media only screen and (max-width: 431px) {
        margin-bottom: -30;
        padding-top: 0;
      }
    }
  }
  &__help {
    display: flex;
    flex-direction: column;
    align-items: center;
    border-top: 1px solid grey;
    padding-top: 10px;
    padding-bottom: 10px;
    .helpLink {
      display: flex;
      align-items: center;
      justify-content: center;
      text-decoration: none;
      padding: 7px 15px;
      background: #008de5;
      color: #fff;
      border: none;
      border-radius: 25px;
      font-size: 22px;
      cursor: pointer;
      transition: all 0.3s;
      margin-bottom: 10px;
      margin-top: 10px;
      width: 200px;
      @media only screen and (max-width: 431px) {
        font-size: 18px;
      }

      p {
        margin: 0;
        margin-left: 5px;
        font-size: 22px;
        @media only screen and (max-width: 431px) {
          font-size: 20px;
          padding-right: 10px;
        }
      }
      img {
        height: 30px;
      }
    }
  }

  .help {
    display: flex;
    border-top: 1px solid grey;
    flex-direction: column;
    align-items: center;

    p {
      margin: 10px 0;
      margin-left: 10px;
      @media only screen and (max-width: 431px) {
        margin-left: 5px;
      }
    }
    &__phone {
      display: flex;
      align-items: center;
      justify-content: center;
      text-decoration: none;
      padding: 0 15px;
      background: #fff;
      color: #008de5;
      border: none;
      border-radius: 25px;
      font-size: 22px;
      cursor: pointer;
      transition: all 0.3s;

      @media only screen and (max-width: 431px) {
        font-size: 18px;
      }
      img {
        height: 30px;
      }
    }
  }
  &__bottomLogo {
    border-top: 1px solid grey;
    /* stylelint-disable-next-line no-descending-specificity */
    img {
      // margin-top: 20px;
      height: 100px;
    }
  }
  .notFounded {
    font-size: 18px;
    &__top {
      &-title {
        font-size: 32px;
        margin: 0;
      }
      &-subtitle {
        margin: 0;
        padding: 10px 0;
        border-bottom: 1px solid grey;
      }
    }

    &__bottom {
      .availableByStreets {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-evenly;
        .availableCard {
          .availableProvider {
            border-radius: 5px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding: 3px;
            border: 1px solid rgba(128, 128, 128, 0.417);
            margin-left: 10px;
            margin-right: 10px;
            cursor: pointer;
            &:hover {
              border: 1px dashed #fff;
            }
            @media only screen and (max-width: 431px) {
              margin-left: 0;
              margin-right: 0;
              margin-bottom: 10px;
            }
            .providerLogo {
              object-fit: contain;
              // object-fit
              height: 140px;
              background: #fff;
              width: 140px;
              border-radius: 5px;
            }
          }
        }
      }
    }
    .notFoundedForm {
      @media only screen and (max-width: 431px) {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
      }
      &__inputPhone {
        outline: none;
        border: 1px solid rgba(128, 128, 128, 0.417);
        background: #00000096;
        border-top-left-radius: 5px;
        border-bottom-left-radius: 5px;
        font-size: 22px;
        color: #fff;
        padding: 10px 15px;
        @media only screen and (max-width: 431px) {
          border-radius: 5px;
          font-size: 18px;
        }
      }
      &__sendBtn {
        border: none;
        font-size: 22px;
        cursor: pointer;
        text-decoration: none;
        color: #fff;
        background: linear-gradient(to right, #d1b88c 0%, #ec9f1b 100%);
        padding: 10px 20px;
        border-top-right-radius: 5px;
        border-bottom-right-radius: 5px;
        border: 1px solid rgba(128, 128, 128, 0.417);
        @media only screen and (max-width: 431px) {
          border-radius: 5px;
          margin-top: 20px;
          font-size: 18px;
        }
      }
    }
  }
}
.addressFormSection {
  display: flex;
  justify-content: space-around;
  flex-direction: column;
  align-items: center;
  @media only screen and (max-width: 431px) {
    padding-top: 0px;
  }
}
.inputWrapper {
  position: relative;
}

.addressForm {
  display: flex;
  align-items: center;
  background-color: #fff;
  border-radius: 30px;
  overflow: hidden;
  padding: 5px 14px;
  box-shadow: rgba(255, 255, 255, 0.1) 0px 1px 1px 0px inset,
    rgba(50, 50, 93, 0.25) 0px 50px 100px -20px,
    rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;

  @media only screen and (max-width: 431px) {
    flex-direction: column;
    align-items: center;
  }
  label {
    margin-bottom: 0;
  }
  &__field {
    padding: 30px 0;
    border: none;
    text-align: left;
    padding-left: 15px;
    padding-bottom: 25px;
    border-right: 1px solid #3f62a7;
    font-size: 1.125rem;

    &:disabled {
      cursor: not-allowed;
    }
    @media only screen and (max-width: 431px) {
      margin-left: 0;
      margin-bottom: 0px;
      width: 250px;
    }
  }

  .suggestionList {
    z-index: 999;
    position: absolute;
    font-size: 18px;
    top: 53px;
    left: 0px;
    width: 100%;
    max-height: 220px;
    overflow-y: auto;
    background-color: #fff;
    color: grey;
    // border: 1px solid #fdb931;
    border-top: none;
    border-radius: 15px;
    backdrop-filter: blur(10px);
    list-style: none;
    padding: 5px 10px;
    margin: 0;
    @media only screen and (max-width: 431px) {
      left: 0;
    }
    .suggestionItem {
      transition: all 0.2s;
      cursor: pointer;
      padding-top: 10px;
      padding-left: 15px;
      padding-bottom: 10px;
      // background-color: rgba(155, 155, 155, 0.317);
      border-radius: 15px;
      &:hover {
        // color: rgb(193, 191, 191);
        color: #fff;
        background-color: #56c1ff;
      }
    }
    .suggestionItem:not(:last-child) {
      border-bottom: 1px solid rgb(193, 191, 191);
      margin-bottom: 10px;
    }
    .loader {
      height: 170px;
    }
    :deep(.loader-spinner) {
      width: 40px;
      height: 40px;
    }
  }
}
.searchProviders {
  // padding: 0 20px;
  // height: 50px;
  background: #008de5;
  color: #fff;
  border: none;
  border-radius: 10px;
  width: 300px;
  margin-top: 10px;
  // margin-left: 20px;
  // font-size: 22px;
  cursor: pointer;
  transition: all 0.3s;
  font-size: 20px;
  margin-bottom: 10px;
  padding: 10px 20px;

  @media only screen and (max-width: 431px) {
    margin-left: 0;
    width: 250px;
    margin-bottom: 0;
  }
}

.availableProviders {
  background-color: #00000096;
  border-radius: 5px;
  margin-top: 30px;
  padding: 20px 30px;
  @media only screen and (max-width: 431px) {
    max-width: 300px;
    width: 100%;
  }

  &__title {
    font-size: 18px;
    margin: 0;
    color: rgb(193, 191, 191);
    @media only screen and (max-width: 431px) {
      font-size: 18px;
      line-height: 1;
      text-align: center;
      padding-bottom: 10px;
    }
  }
  &__names {
    color: #fff;
    text-decoration: none;
    display: flex;
    justify-content: space-around;
    align-items: center;
    font-size: 24px;
    transition: color 0.3s;
    margin-top: 30px;
    margin-bottom: 10px;
    &:hover {
      color: rgb(193, 191, 191);
    }

    @media only screen and (max-width: 431px) {
      flex-direction: column;
      align-items: center;
    }
  }
}
</style>
