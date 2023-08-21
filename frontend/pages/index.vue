<template lang="pug">
main
  AddressSection
  .aboutInternetbor 
    p {{ $t('internetborIs') }}
  AboutCompany
  AnswersandQuestions
  section.topProvider
    .Title 
      p.Title__top {{ $t('topProviders') }}
    .topProviders__card

  section.betterOffer
    TopProviders
    section.allplaySection
      .allplay
        .allplayLeft
          img(src='/allplay-awful-logo.png')
        .allplayRight 
          .moana 
            img.moanaImage(src='/moana.png')
          .allplayInfo 
            .discount
              p
                span(style="font-family: 'LilitaOne-Regular';") 299 
                span {{ $t('sum') }} /
                span(style="font-family: 'LilitaOne-Regular';")  30
                span.bold  {{ $t('days') }}
            .detailing
              .left
                p {{ $t('withoutAds') }}
                p {{ $t('viewOn3Devices') }}
              .right
                p {{ $t('tvArchive') }}
                p {{ $t('moreThan') }}
            .studios
              img.studiosImage(src='/studios.png')
      a.subscribeButton(href='https://allplay.uz/profile/subscription' target='_blank') {{ $t('watchMovie') }}
    .Title 
      p.Title__top  {{ $t('bestTariffOfMonth') }}
      .Title__bottom
        p {{ $t('accordingTo') }}
        img(src='/new-logo.png')
      .tariffCards.container-fluid
        BetterOffers

</template>

<script>
export default {}
</script>
<style lang="scss" scoped>
.aboutInternetbor {
  display: flex;
  justify-content: center;
  padding-top: 30px;
  p {
    max-width: 800px;
    width: 100%;
    text-align: center;
    font-size: 24px;
    margin: 0;
    line-height: 30px;
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
</style>
