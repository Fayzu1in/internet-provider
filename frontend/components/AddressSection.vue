<template lang="pug">
.container-fluid
  .addressSection
    //- .currentLocation
    //-   p.currentLocation__title(@click='showCities = !showCities') {{ currentCity }}
    //-     ul.citiesList(v-if='showCities')
    //-       li.citiesList__list(v-for="city in citiesList" :key="city", @click='selectedCity(city)') {{ city }}
    //-   MaterialIcon(:icon='mdiMapMarkerOutline', size='27px')
    .addressSection__top
      .addressSection__top-left {{ $t('chooseProvider') }}
      .addressSection__top-right
        img(src='/signal.png')
    .addressSection__middle
      //- AddressForm
      NewaddressForm(:coverageCities='coverageCities', :currentCity='currentCity')
    .addressSection__bottom
      a(href='https://t.me/internet_bor_bot').addressSection__bottom-left
        img(src='/telegram.png')
        span {{ $t('quickConnectionViaBot') }}
      .addressSection__bottom-right
        a(href='tel:9989781136135') {{ $t('callBack') }}
        a(href='tel:9989781136135')
          img.phoneImage(src='/phone.png')
        .workTime
          .workTime__top +998 (78) 113-61-35
          .workTime__bottom {{ $t('everyDayFrom') }}
</template>
<script>
import { mdiMapMarkerOutline } from '@mdi/js'
export default {
  data() {
    return {
      mdiMapMarkerOutline,
      currentCity: 'Ташкент',
      showCities: false,
      coverageCities: [],
    }
  },
  async fetch() {
    await this.$api.getCoverageCities().then((res) => {
      this.coverageCities = res.data
      console.log('coverageCities', this.coverageCities)
    })
  },
  computed: {
    citiesList() {
      return [...new Set(this.coverageCities.map((cityObj) => cityObj.city))]
    },
  },
  methods: {
    selectedCity(city) {
      this.currentCity = city
    },
  },
}
</script>
<style lang="scss" scoped>
.addressSection {
  padding-top: 140px;
  @media only screen and (max-width: 576px) {
    padding-top: 80px;
  }
  .currentLocation {
    text-align: right;
    display: flex;
    align-items: center;
    padding-bottom: 90px;
    justify-content: flex-end;
    &__title {
      width: auto;
      position: relative;
      cursor: pointer;
    }
    .citiesList {
      list-style: none;
      background-color: #fff;
      position: absolute;
      width: fit-content;
      left: -10px;
      top: 30px;
      padding: 10px 20px;
      border-bottom-left-radius: 15px;
      border-bottom-right-radius: 15px;
      &__list {
        font-size: 1rem;
        color: #3f62a7;
        font-weight: 200;
        padding-bottom: 10px;
        text-wrap: nowrap;
        text-align: left;
        &:hover {
          text-decoration: underline;
        }
      }
    }
    p {
      padding-right: 12px;
      text-decoration: underline;
      margin-bottom: 0;
      color: #fff;
    }
  }
  &__top {
    display: flex;
    align-items: center;
    padding-bottom: 74px;
    justify-content: space-between;
    width: 100%;
    @media only screen and (max-width: 576px) {
      padding-bottom: 20px;
    }

    &-left {
      font-family: 'Raleway', sans-serif;
      font-size: 2.625rem;
      color: #fff;
      font-weight: bold;
      max-width: 662px;
      width: 100%;
      @media only screen and (max-width: 576px) {
        font-size: 2rem;
        line-height: 37px;
      }
    }
    &-right {
      display: flex;
      justify-content: center;
      width: auto;
      img {
        height: 180px;
        width: auto;
      }
      @media only screen and (max-width: 576px) {
        display: none;
      }
    }
  }
  &__bottom {
    font-family: 'Montserrat', sans-serif;
    display: flex;
    padding-top: 183px;
    color: #fff;
    padding-bottom: 49px;
    @media only screen and (max-width: 576px) {
      flex-direction: column;
      padding-top: 20px;
      padding-bottom: 20px;
    }
    &-left {
      display: flex;
      align-items: center;
      color: #fff;
      text-wrap: nowrap;
      width: fit-content;
      img {
        height: 43px;
        width: 43px;
      }
    }
    &-right {
      display: flex;
      align-items: center;
      justify-content: flex-end;
      @media only screen and (max-width: 576px) {
        flex-direction: column;
        align-items: flex-start;
      }
      a {
        width: auto;
        color: #fff;
      }
      .phoneImage {
        width: 43px;
        height: 39px;
        margin-left: 19px;
        margin-right: 19px;
        @media only screen and (max-width: 576px) {
          display: none;
        }
      }
      .workTime {
        width: auto;
        &__top {
          font-size: 18px;
          font-weight: bold;
        }
        &__bottom {
        }
      }
    }
  }
}
.address {
  padding-top: 150px;
  display: flex;
  flex-direction: column;
  align-items: center;

  @media only screen and (max-width: 431px) {
    padding-top: 70px;
  }

  &__top {
    font-size: 32px;
    font-weight: 600;
    text-align: center;
    @media only screen and (max-width: 431px) {
      font-size: 24px;
      // text-align: left;
    }
  }
  &__middle {
    margin: 0 auto;
    // text-align: center;
    // max-width: 750px;
    margin-top: 30px;
    width: fit-content;
    // color: #ffffff;
    padding: 20px 20px;
    // font-size: 18px;
    background-color: #ffffff93;
    border-radius: 15px;
    display: flex;
    justify-content: space-around;
    align-items: center;
    @media only screen and (max-width: 431px) {
      flex-direction: column-reverse;
      padding: 10px;
    }
    &-right {
      background-color: #0b2249;
      border-radius: 15px;
      margin-left: 20px;
      @media only screen and (max-width: 431px) {
        margin-left: 0;
      }
      .manual {
        // max-width: 400px;
        // width: 100%;
        padding: 10px 20px;
        @media only screen and (max-width: 431px) {
          padding: 10px;
        }
        p {
          font-size: 20px;
        }
        &__list {
          width: 300px;
          @media only screen and (max-width: 431px) {
            font-size: 14px;
            width: 255px;
          }
          li {
            padding-bottom: 20px;
            @media only screen and (max-width: 431px) {
              padding-bottom: 10px;
            }
          }
        }
        .title {
          @media only screen and (max-width: 431px) {
            font-size: 18px;
            text-align: center;
          }
        }
      }
    }
    @media only screen and (max-width: 431px) {
      font-size: 16px;
      // text-align: left;
      padding-top: 10px;
    }
  }
  .telegramBot {
    display: flex;
    align-items: center;
    margin-top: 30px;
    color: #fff;
    font-weight: bold;
    font-size: 1.375rem;
    @media only screen and (max-width: 431px) {
      text-align: center;
    }
    &__image {
      height: 30px;
      padding-left: 10px;
      @media only screen and (max-width: 431px) {
        display: none;
      }
    }
  }
}
</style>
