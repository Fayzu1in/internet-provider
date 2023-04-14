<template lang="pug">
section.addressFormSection.container-fluid
  .modalBckg(v-if="modalHelp || switc" @click='modalHelp = false, switc = false')
  .modalRequest(v-if="modalHelp")
    .modalRequest__top 
      .closeModal(@click="modalHelp = false")
        MaterialIcon(:icon='mdiCloseCircleOutline')
      p.title Не можете выбрать тариф ?
      p.subtitle Свяжитесь с нашим оператором и вам помогут
      .modalRequest__help 
        a.helpLink(href="tel:+998909113086") 
          span Позвонить
          MaterialIcon(:icon='mdiPhone')
        a.helpLink(href='https://telegram.me/InternetBor')
          span Телеграм
          img(src='/telegram.svg')
      .modalRequest__bottomLogo 
        img(src="/logo-full.svg")
  .modalRequest(v-if='switc')
    .modalRequest__top
      .closeModal(@click='switc = false')
        MaterialIcon(:icon='mdiCloseCircleOutline')
      p.title Поздравляем!  
      p.subtitle Доступные провайдеры по вашему адресу 
    .modalRequest__middle
      div(v-for="available in availableProviders") 
        NuxtLink.availableProvider(:to='(`/provider/${available.provider_id}/`)') 
          img.providerLogo(:src="`${available.provider_picture}`")
    .modalRequest__bottom
      p.subtitle Выгодные тарифы из доступных провайдеров 
      VueGlide(:options='options')
        VueGlideSlide(v-for="best in bestOfAvailable" :key="best.plan_id")
          BetterofferCard(:name='best.plan_name')
        template(slot='control' )
          button.glide__arrow.glide__arrow--left(data-glide-dir='<') 
            MaterialIcon(:icon='mdiChevronLeft' )
          button.glide__arrow.glide__arrow--right(data-glide-dir='>') 
            MaterialIcon(:icon='mdiChevronRight')

        
   



      .help
        p Позвоните нам, и наш консультант бесплатно поможет выбрать подходящий вам тариф 
        a.help__phone(href="tel:+998909113086")
          p Позвонить
          MaterialIcon(:icon='mdiPhone')
  form.addressForm(action="" method="post", @submit.prevent="formSubmit")
    label.inputWrapper(for='city')
      input.addressForm__field(type='text' placeholder='Город' required v-model="inputCity" @input="showCities = inputCity.length > 0" @click="showCities = !showCities, showDistrict = false, showStreets = false" )
      ul.suggestionList(v-if='showCities')
        li.suggestionItem(v-for="city in city" @click="selectCity(city.city)") {{ city.city }}

    label.inputWrapper(for='street')
      input.addressForm__field(type='text' placeholder='Район' required v-model="inputDistrict" @input="showDistrict = inputDistrict.length > 0" @click='suggestion' :disabled="isSecondDisabled" )
      ul.suggestionList(v-if="showDistrict" )
        li.suggestionItem(v-for="district in this.districtByCities"  @click="selectDistrict(district.district)") {{ district.district }}

    label.inputWrapper(for='street')
      input.addressForm__field(type='text' placeholder='Улица' required v-model="inputStreets" @input="showStreets = inputStreets.length > 0" @click="showStreets = !showStreets, showCities = false" :disabled="isThirdDisabled" )
      ul.suggestionList(v-if="showStreets")
        li.suggestionItem(v-for="street in this.streetsByDistrict"  @click="selectStreet(street.street)") {{ street.street }}

    label.inputWrapper(for='house')
      input.addressForm__field(type='text' placeholder="Дом" required v-model="inputHouse" @click='showHouses = !showHouses, showStreets = false, showDistrict=false, showCities= false' :disabled="isForthDisabled")
      ul.suggestionList(v-if="showHouses")
        li.suggestionItem(v-for="house in this.housesByStreets[0].houses" @click="selectHouse(house)" ) {{ house }}
    button.searchProviders Найти провайдеров
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
      districtByCities: [],
      streetsByDistrict: [],
      housesByStreets: [],
      topProviders: null,
      response: null,
      switc: false,
      modalHelp: false,
      availableProviders: [],
      bestOfAvailable: [],
      currentIndex: 0,

      modalBckg: false,
      options: {
        perView: 1,
        keyboard: false,
        bound: true,
        breakpoints: {
          // 800: {
          //   perView: 2,
          // },
          // 550: {
          //   perView: 1,
          // },
        },
      },
    }
  },
  async fetch() {
    this.streets = await this.$axios.$get(
      'https://internetbor.uz/api/v1/coverage/'
    )
  },

  computed: {
    filteredWords() {
      const uniqueWords = this.streets.reduce((acc, word) => {
        if (!acc[word.street]) {
          acc[word.street] = word
        }
        return acc
      }, {})
      return Object.values(uniqueWords).filter((word) => {
        return word.street
          .toLowerCase()
          .includes(this.inputDistrict.toLowerCase())
      })
    },
    city() {
      const uniqueWords = this.streets.reduce((acc, cur) => {
        if (!acc[cur.city]) {
          acc[cur.city] = cur
        }
        return acc
      }, {})
      return Object.values(uniqueWords).filter((cur) => {
        return cur.city.toLowerCase().includes(this.inputCity.toLowerCase())
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

  mounted() {
    let clicked = false
    const timer = setInterval(() => {
      if (!clicked) {
        this.modalHelp = true
        this.modalBckg = true
      }
    }, 10000)
    window.addEventListener('click', () => {
      clicked = true
      clearInterval(timer)
    })
  },

  methods: {
    selectCity(word) {
      // axios
      //   .get(`https://internetbor.uz/api/v1/coverage/?city=${word}`)
      //   .then((response) => {
      //     this.districtByCities = response.data
      //   })
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
      this.streetsByDistrict = this.streets.filter(
        (obj) => obj.district === word
      )
      // this.streetsByDistrict = this.streetsByDistrict.reduce((acc, obj) => {
      //   const foundIndex = acc.findIndex((item) => item.street === obj.street)
      //   if (foundIndex === -1) {
      //     acc.push(obj)
      //   } else {
      //     acc[foundIndex] = obj
      //   }
      //   return acc
      // }, [])
      // console.log(this.streetsByDistrict)
      this.inputDistrict = word
      this.SuggestionList = false
      this.showDistrict = false
    },
    selectStreet(word) {
      this.housesByStreets = this.streetsByDistrict.filter(
        (obj) => obj.street === word
      )
      // console.log(this.housesByStreets[0].houses)
      this.inputStreets = word
      this.showStreets = false
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
      // console.log(this.inputStreets)
      axios
        .get(
          `https://internetbor.uz/api/v1/coverage/?street=${this.inputStreets}`
        )
        .then((response) => {
          this.response = response.data[0]
          this.availableProviders = this.response.providers
          if (this.response != null) {
            this.switc = true
          }
          let result = []
          for (const obj of this.availableProviders) {
            result = result.concat(obj.provider_best)
            this.bestOfAvailable = result
          }
          console.log(this.bestOfAvailable)
        })
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
  background: linear-gradient(to right, #d1b88c 0%, #ec9f1b 100%);
  opacity: 0.7;
  color: #fff;
  cursor: pointer;
  transition: opacity, 0.3s;
}
.glide__arrow--left {
  /* // :deep(button[data-glide-dir='<']) {
  // } */

  left: 5px;

  &:hover {
    opacity: 1;
  }
}
.glide__arrow--right {
  /* // :deep(button[data-glide-dir='>']) {
  // } */

  right: 5px;

  &:hover {
    opacity: 1;
  }
}
:deep(.glide__slides) {
  display: flex !important;
  justify-content: space-around !important;
}
.glide__slide {
  width: 250px !important;
}
.modalBckg {
  position: fixed;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  background: #0000005f;
}
.modalRequest {
  border: 1px solid rgba(128, 128, 128, 0.417);
  position: fixed;
  max-width: 600px;
  width: 100%;
  border-radius: 5px;
  top: 50%;
  z-index: 999;
  background-color: #00000096;
  backdrop-filter: blur(10px);
  padding: 20px 20px;
  text-align: center;
  max-height: 100%;
  transform: translateY(-50%);
  @media only screen and (max-width: 420px) {
    overflow: scroll;
    overscroll-behavior: contain;
    top: 50%;
    max-height: 60vh;
    width: 90%;
  }

  .closeModal {
    position: absolute;
    right: 10px;
    top: 10px;
    cursor: pointer;
  }

  .subtitle {
    margin: 0;
    padding-top: 10px;
    font-size: 18px;
    padding-bottom: 15px;
    @media only screen and (max-width: 420px) {
      font-size: 16px;
      padding-top: 10px;
      padding-bottom: 10px;
    }
  }
  &__top {
    @media only screen and (max-width: 420px) {
      padding-top: 30px;
    }
    .title {
      font-size: 32px;
      margin: 0;
      @media only screen and (max-width: 420px) {
        font-size: 24px;
      }
    }
  }
  &__middle {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
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
      @media only screen and (max-width: 420px) {
        margin-left: 0;
        margin-right: 0;
        margin-bottom: 10px;
      }
      .providerLogo {
        height: 140px;
        background: #fff;
        width: 140px;
        border-radius: 5px;
      }
      .selectBtn {
        border: none;
        font-size: 18px;
        padding: 5px 0;
        color: #fff;
        background: linear-gradient(to right, #d1b88c 0%, #ec9f1b 100%);
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
      text-decoration: none;
      color: #fff;
      max-width: 180px;
      width: 100%;
      justify-content: space-around;
      margin-top: 10px;
      margin-bottom: 10px;
      transition: color 0.3s;
      &:hover {
        color: rgb(193, 191, 191);
      }
      @media only screen and (max-width: 420px) {
        justify-content: center;
        margin-bottom: 5px;
        margin-top: 5px;
      }

      span {
        font-size: 26px;
        @media only screen and (max-width: 420px) {
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
    }
    &__phone {
      font-size: 22px;

      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      text-decoration: none;
    }
  }
  &__bottomLogo {
    border-top: 1px solid grey;
    /* stylelint-disable-next-line no-descending-specificity */
    img {
      margin-top: 20px;
      height: 40px;
    }
  }
}
.addressFormSection {
  display: flex;
  justify-content: space-around;
  flex-direction: column;
  align-items: center;
  padding-top: 50px;
  @media only screen and (max-width: 420px) {
    padding-top: 30px;
  }
}
.inputWrapper {
  position: relative;
}

.addressForm {
  max-width: 1140px;
  width: 100%;
  // margin-top: 60px;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: space-around;
  @media only screen and (max-width: 420px) {
    flex-direction: column;
    align-items: center;
  }

  &__field {
    height: 50px;
    padding: 8px 20px;
    background-color: #00000081;
    border: 1px solid rgba(128, 128, 128, 0.417);
    backdrop-filter: blur(10px);
    color: #fff;
    border-radius: 5px;
    font-size: 22px;
    width: 300px;
    text-align: center;

    margin-top: 10px;
    &:disabled {
      cursor: not-allowed;
    }
    @media only screen and (max-width: 420px) {
      margin-left: 0;
      margin-bottom: 10px;
      width: 250px;
    }
  }

  .suggestionList {
    z-index: 999;
    position: absolute;
    font-size: 18px;
    top: 60px;
    left: 0px;
    width: 100%;
    max-height: 200px;
    overflow-y: auto;
    background-color: #00000096;
    // border: 1px solid #fdb931;
    border-top: none;
    border-radius: 5px;
    backdrop-filter: blur(10px);
    // box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    list-style: none;
    padding: 5px 10px;
    margin: 0;
    @media only screen and (max-width: 420px) {
      left: 0;
    }
    .suggestionItem {
      cursor: pointer;
      padding-top: 5px;
      padding-bottom: 5px;
      &:hover {
        color: rgb(193, 191, 191);
      }
    }
    .suggestionItem:not(:last-child) {
      border-bottom: 1px solid rgb(193, 191, 191);
    }
  }
}
.searchProviders {
  padding: 0 20px;
  height: 50px;
  background: linear-gradient(to right, #d1b88c 0%, #ec9f1b 100%);
  color: #fff;
  border: none;
  border-radius: 5px;
  width: 300px;
  margin-top: 10px;
  // margin-left: 20px;
  font-size: 22px;
  cursor: pointer;
  transition: all 0.3s;

  @media only screen and (max-width: 420px) {
    margin-left: 0;
  }
}

.availableProviders {
  background-color: #00000096;
  border-radius: 5px;
  margin-top: 30px;
  padding: 20px 30px;
  @media only screen and (max-width: 420px) {
    max-width: 300px;
    width: 100%;
  }

  &__title {
    font-size: 18px;
    margin: 0;
    color: rgb(193, 191, 191);
    @media only screen and (max-width: 420px) {
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

    @media only screen and (max-width: 420px) {
      flex-direction: column;
      align-items: center;
    }
  }
}
</style>
