<template lang="pug">
section.addressFormSection.container-fluid
  .modalBckg(v-if="switc" key='dynamic' class='animated' @click='switc=false')
  .modalRequest(v-if='switc')
    .modalRequest__top
      .closeModal(@click='switc = false')
        MaterialIcon(:icon='mdiCloseCircleOutline')
      p.title Поздравляем!  
      p.subtitle Доступные провайдеры по вашему адресу 
    .modalRequest__middle
      div(v-for="available in availableProviders" ) 
        NuxtLink.availableProvider(:to='(`/provider/${available.provider_id}/`)') 
          img.providerLogo(:src="`${available.provider_picture}`")
      //- .availableProvider 
      //-   img.providerLogo(src='/comnet.svg')
      //- .availableProvider 
      //-   img.providerLogo(src='/uzonline.png')
    .modalRequest__bottom
      p.subtitle Выгодные тарифы из доступных провайдеров 
      .splide
        Splide(:options='options' v-if="this.availableProviders?.length")
          splide-slide(v-for='available in availableProviders')
            BetterofferCard.card(:image='available.provider_picture', :nSpeed='available.night' :name='available.title', :speed='available.speed', :price='available.price' :message='available.id')
      //- BetterofferCard.card(image='/freelink.png' :name='tariff.title' :nSpeed='tariff.night' :tech='tariff.tech' :speed='tariff.speed' :price='tariff.price' :message='tariff.id')

      .help
        p Позвоните нам, и наш консультант бесплатно поможет выбрать подходящий вам тариф 
        a.help__phone(href="tel:+998909113086")
          p Позвонить
          MaterialIcon(:icon='mdiPhone')
    

  form.addressForm(action="" method="post", @submit.prevent="formSubmit")
    label.inputWrapper(for='city')
      select.addressForm__field(id='type' name='type' required v-model='selectedCity')
        option(value='' disable selected) Выберите город
        option(value='Tashkent') Tashkent
    label.inputWrapper(for='street')
      input.addressForm__field(type='text' placeholder='Укажите улицу' v-model="inputText" @input="showSuggestions = inputText.length > 0" required @click='suggestion' )
      ul.suggestionList(v-if="showSuggestions")
        li.suggestionItem(v-for="word in filteredWords" :key="word.id" @click="selectSuggestion(word.street)") {{ word.street }}
    label.inputWrapper(for='house')
      input.addressForm__field(type='text' placeholder="Укажите дом" v-model="inputHome")
    
    button.searchProviders Найти провайдеров
  div
    //- transition-group(name='fade')
    //-   div.availableProviders(v-if='switc'  class='animated')
    //-     p.availableProviders__title Доступные провайдеры на вашей улице
    //-     div(v-for='available in availableProviders' :key='available.id')
    //-       NuxtLink.availableProviders__names(:to='(`/provider/${available.id}`)') {{ available.name }}
        
      //- div(key='main-content')

      

</template>
<script>
import axios from 'axios'
import '@splidejs/splide/dist/css/splide.min.css'
import { mdiCloseCircleOutline, mdiPhone } from '@mdi/js'

export default {
  data() {
    return {
      mdiCloseCircleOutline,
      mdiPhone,
      selectedCity: '',
      streets: [],
      inputText: '',
      inputHome: '',
      showSuggestions: false,
      // SuggestionList: true,
      topProviders: null,
      response: null,
      switc: false,
      availableProviders: [],
      currentIndex: 0,
      hotTariff: null,
      options: {
        // type: 'loop',
        rewind: true,
        // padding: '20px',

        width: '250px',
        // padding: { left: 0, right: 0 },
        gap: '20px',
        perPage: 1,
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
        return word.street.toLowerCase().includes(this.inputText.toLowerCase())
      })
    },
  },

  methods: {
    formSubmit() {
      axios
        .get(`https://internetbor.uz/api/v1/coverage/?street=${this.inputText}`)
        .then((response) => {
          this.response = response.data[0]
          // console.log(this.response.providers)
          this.availableProviders = this.response.providers
          // console.log(this.availableProviders)

          if (this.response != null) {
            this.switc = true
          }
          // console.log(this.inputText)
          this.hotTariff = this.availableProviders.map('provider_id')
          // console.log(this.hotTariff)
        })
    },

    // `https://internetbor.uz/api/v1/providers/${this.availableProviders[i]}`

    selectSuggestion(word) {
      this.inputText = word
      this.SuggestionList = false
      this.showSuggestions = false
    },
    suggestion() {
      this.showSuggestions = !this.showSuggestions
    },
    nextSlide() {
      this.currentIndex = Math.min(
        this.currentIndex + 1,
        this.cards.length - this.itemsToShow
      )
    },
    prevSlide() {
      this.currentIndex = Math.max(this.currentIndex - 1, 0)
    },
  },
}
</script>

<style lang="scss" scoped>
.modalBckg {
  // width: 100%;
  // height: 100vh;
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
  // height: 600px;
  // background-color: #fff;
  border-radius: 5px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 999;
  background-color: #00000096;
  backdrop-filter: blur(10px);
  padding: 20px 20px;
  text-align: center;
  .closeModal {
    position: absolute;
    right: 10px;
    top: 10px;
    cursor: pointer;
  }

  .subtitle {
    margin: 0;
    padding-top: 20px;
    font-size: 18px;
    padding-bottom: 20px;
  }
  &__top {
    .title {
      font-size: 32px;
      margin: 0;
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
      // align-items: center;
      justify-content: center;
      // margin-top: 20px;
      padding: 3px;
      border: 1px solid rgba(128, 128, 128, 0.417);

      margin-left: 10px;
      margin-right: 10px;
      // transition: all 1s;
      cursor: pointer;
      // overflow: hidden;
      &:hover {
        border: 1px dashed #fff;
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
        // background: #000;
        background: linear-gradient(to right, #d1b88c 0%, #ec9f1b 100%);

        // border: 1px solid rgba(128, 128, 128, 0.417);
        // background: radial-gradient(
        //     ellipse farthest-corner at right bottom,
        //     #fedb37 0%,
        //     #fdb931 8%,
        //     #9f7928 30%,
        //     #8a6e2f 40%,
        //     transparent 80%
        //   ),
        //   radial-gradient(
        //     ellipse farthest-corner at left top,
        //     #ffffff 0%,
        //     #ffffac 8%,
        //     #d1b464 25%,
        //     #5d4a1f 62.5%,
        //     #5d4a1f 100%
        //   );
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
      margin-bottom: 20px;
    }
  }
  .help {
    display: flex;
    border-top: 1px solid grey;
    flex-direction: column;
    align-items: center;
    &__phone {
      font-size: 22px;

      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      text-decoration: none;

      p {
        margin: 0;
      }
    }
  }
}
.addressFormSection {
  display: flex;
  justify-content: space-around;
  flex-direction: column;
  align-items: center;
  padding-top: 50px;
}
.inputWrapper {
  position: relative;
}
.addressForm {
  max-width: 1000px;
  width: 100%;
  // margin-top: 60px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  @media only screen and (max-width: 420px) {
    flex-direction: column;
    align-items: center;
  }

  &__field {
    height: 50px;
    padding: 8px 16px;
    background-color: #00000081;
    border: 1px solid rgba(128, 128, 128, 0.417);
    backdrop-filter: blur(10px);
    color: #fff;
    // border: none;
    border-radius: 5px;
    // width: 250px;
    // margin-bottom: 20px;
    margin-left: 20px;
    font-size: 18px;
    // box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;

    // border-bottom: 2px solid #fdb931;
    // border-bottom: 2px solid #fff;

    // position: relative;
    width: 100%;
    @media only screen and (max-width: 420px) {
      margin-left: 0;
      margin-bottom: 10px;
      width: 250px;
    }
  }
  .suggestionList {
    position: absolute;
    font-size: 18px;
    top: 50px;
    left: 20px;
    width: 100%;
    max-height: 200px;
    overflow-y: auto;
    background-color: #00000096;
    // border: 1px solid #fdb931;
    border-top: none;
    border-radius: 5px;
    // box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    list-style: none;
    padding: 5px 10px;
    margin: 0;
    @media only screen and (max-width: 420px) {
      left: 0;
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
  width: 250px;
  margin-left: 20px;
  font-size: 18px;
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
    // line-height: 0;
    margin: 0;
    // padding-bottom: 50px
    color: grey;
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
      color: grey;
    }

    @media only screen and (max-width: 420px) {
      flex-direction: column;
      align-items: center;
      // margin-bottom: 10px;
    }
  }
}
:deep(.splide__arrow) {
  border-radius: 10px;
  width: 3rem;
  height: 3rem;
}
:deep(.splide__arrow--prev) {
  left: -4rem;
  // right: 0rem;
}
:deep(.splide__arrow--next) {
  right: -4rem;
  // right: 0rem;
}
:deep(.splide__pagination) {
  bottom: -1rem;
}
</style>
<!-- <style>
.splide__pagination {
  bottom: -1.2rem;
}
.splide__arrow--next {
  right: -2rem;
  /* left: -3rem; */
}
.splide__arrow--prev {
  left: -2rem;
}
</style> -->
