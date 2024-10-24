<template lang="pug">
main
  AddressSection
  ChooseCard(@showCallBackModal='showCallBackModal')
  TopprovidersSection
  BetteroffersSection
  AboutSection
  QuestionsSection
  .container-fluid
    .overFooter
      .overFooter__card
        .overFooter__title 15000
        .overFooter__subtitle человек выбирают нас
      .overFooter__card
        .overFooter__title 94%
        .overFooter__subtitle положительных отзывов
      .overFooter__card
        .overFooter__title 24/7
        .overFooter__subtitle поддержка
  transition(name='fade')
    CallBack(v-if='callBack' @close='showCallBack')
  transition(name='fade')
    NeedHelp(v-if='NeedHelpModal' @close='showNeedHelpModal')
  </template>

<script>
export default {
  data() {
    return {
      callBack: false,
      NeedHelpModal: false,
    }
  },
  mounted() {
    let clicked = false
    const timer = setInterval(() => {
      if (!clicked) {
        this.NeedHelpModal = true
      }
    }, 15000)
    window.addEventListener('click', () => {
      clicked = true
      clearInterval(timer)
    })
  },
  methods: {
    showCallBackModal() {
      this.callBack = true
    },
    showCallBack() {
      this.callBack = false
    },
    showNeedHelpModal() {
      this.NeedHelpModal = false
    },

    async redirectToAllplay() {
      try {
        await this.$api.clickCatcher('allplay')
      } catch (error) {
        console.error('Error occured', error)
      } finally {
        window.open('https://allplay.uz/profile/subscription', '_blank')
      }
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
.overFooter {
  display: flex;
  justify-content: space-between;
  text-align: center;
  color: #fff;
  padding-bottom: 65px;
  padding-top: 30px;
  @media only screen and (max-width: 576px) {
    flex-direction: column;
  }
  &__title {
    font-size: 3.75rem;
    font-weight: 600;
  }
  &__subtitle {
    font-size: 1.375rem;
    font-weight: 200;
  }
}
.download {
  margin: 0;
}
.loader {
  background: orange;
}
.callBackSection {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: rgba(255, 255, 255, 0.5764705882);
  margin-top: 30px;
  padding: 15px 15px;
  border-radius: 15px;
  max-width: 400px;
  width: 100%;
  .phoneCall {
    font-family: LilitaOne-Regular;
    color: #fff;
    font-size: 24px;
    padding: 5px 10px;
    border-radius: 15px;
    text-decoration: none;
    transition: all, 0.3s;
    background-color: #001b48;
    cursor: pointer;

    &:hover {
      background-color: #fff;
      color: #001b48;
    }
  }
  .callBack {
    margin-top: 10px;
    color: #001b48;
    background: none;
    border: none;
    border-radius: 10px;
    // width: 300px;
    cursor: pointer;
    transition: all 0.3s;
    font-size: 16px;
    border-bottom: 3px inset transparent;
    transition: border-bottom, 0.3s;
    border-bottom: 3px inset #001b48;
    padding-bottom: 5px;

    &:hover {
      border-bottom: 3px inset #fff;
    }

    @media only screen and (max-width: 431px) {
      margin-left: 0;
      width: 250px;
      margin-bottom: 0;
    }
  }
}
.allplaySection {
  padding-top: 30px;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  @media only screen and (max-width: 431px) {
    // display: none;
    padding-top: 15px;
  }
  .allplay {
    border-radius: 15px;
    background-color: rgba(255, 255, 255, 0.5764705882);
    padding: 20px;
    max-width: 860px;
    width: 100%;
    height: 300px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #fff;
    text-decoration: none;
    cursor: pointer;
    @media only screen and (max-width: 431px) {
      flex-direction: column;
      height: 100%;
    }
    .allplayLeft {
      img {
        height: 100px;
        // @media only screen and (max-width: 431px) {
        //   height: 0px;
        // }
      }
    }
    .allplayRight {
      width: 65%;
      height: 100%;
      border-radius: 15px;
      background-color: #0b2249;
      position: relative;
      @media only screen and (max-width: 431px) {
        width: 100%;
      }
      .moana {
        .moanaImage {
          position: absolute;
          height: 330px;
          top: -19px;
          left: -125px;
          @media only screen and (max-width: 431px) {
            height: 250px;
            top: 0;
            left: -70px;
            overflow: hidden;
          }
        }
      }
      .allplayInfo {
        display: flex;
        flex-direction: column;
        // align-items: end;
        justify-content: flex-end;
        font-size: 14px;
        padding-left: 160px;
        padding-top: 20px;
        .discount {
          font-size: 26px;
          padding-bottom: 10px;
          @media only screen and (max-width: 431px) {
            font-size: 20px;
            width: 100px;
          }
          p {
            margin: 0;
          }
        }
        .detailing {
          display: flex;
          align-items: center;
          padding-right: 10px;
          @media only screen and (max-width: 431px) {
            flex-direction: column;
          }
          .left,
          .right {
            text-align: left;
            width: 180px;
            margin-right: 5px;
            @media only screen and (max-width: 431px) {
              width: 100%;
              margin-right: 0;
              p {
                margin: 10px 0;
              }
            }
          }
        }
        .studios {
          display: flex;
          @media only screen and (max-width: 431px) {
            justify-content: center;
            align-items: center;
          }
          .studiosImage {
            height: 110px;
            // margin-left: -55px;
            position: absolute;
            bottom: -10px;
            right: -75px;
            @media only screen and (max-width: 431px) {
              height: 70px;
              position: unset;
              margin-left: -150px;
            }
          }
        }
      }
    }
  }
  .subscribeButton {
    text-decoration: none;
    color: #fff;
    background-color: #008de5;
    padding: 10px 20px;
    margin-top: 15px;
    border-radius: 10px;
    font-size: 20px;
    cursor: pointer;
  }
}
.topProvider,
.betterOffer {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  padding-top: 30px;
  @media only screen and (max-width: 431px) {
    padding-top: 0px;
  }

  .Title {
    text-align: center;
    &__top {
      padding-top: 30px;
      font-size: 32px;
      margin: 0;
      font-weight: bold;
      text-transform: uppercase;
      @media only screen and (max-width: 431px) {
        padding-bottom: 15px;
        font-size: 24px;
      }
    }
    &__bottom {
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      margin: 0;
      @media only screen and (max-width: 431px) {
        margin-top: -30px;
        margin-bottom: -60px;
      }

      img {
        height: 75px;
      }
    }

    .fireImg {
      height: 35px;
      padding-left: 10px;
      @media only screen and (max-width: 431px) {
        height: 25px;
      }
    }
    @media only screen and (max-width: 431px) {
      text-align: center;
      font-size: 22px;
    }
  }
}
.topProvider {
  padding-top: 0;
}
.tariffCards {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  @media only screen and (max-width: 431px) {
    margin-top: 20px;
  }
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
