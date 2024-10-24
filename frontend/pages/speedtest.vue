<template lang="pug">
section.speedttestContainer.container-fluid
  .speedtest 
    .speedtest__left 
      .speedtest__left-speedshow 
        p.speedText {{ text }} 
        p.bytes {{ bytes }}
      button.speedBtn(v-show="checkBtn" @click="checkSpeed") {{ $t('checkSpeed') }}
      button.speedBtnHidden(v-show="checkBtnNone"  @click="cancelCheckSpeed") {{ $t('cancel') }}
    .speedtest__right  
      .listView 
        .itemLeft {{ $t('averageSpeed') }}
        .itemRight {{ average }}
      .listView 
        .itemLeft {{ $t('browserInformation') }}
        .itemRight {{ browserVersion }}
      p.tasix {{ $t('tasIx') }}

   
</template>
<script>
import axios, { CancelToken, isCancel } from 'axios'

export default {
  data() {
    return {
      speed: 0,
      bytes: '',
      checkBtn: true,
      checkBtnNone: false,
      text: '...',
      source: CancelToken.source(),
      finished: false,
      average: '. . .',
      browserVersion: navigator.userAgent,
      ip: null,
    }
  },
  methods: {
    checkSpeed() {
      this.source = CancelToken.source()
      this.speed = 0
      this.text = '...'
      let time, loaded
      const speeds = []

      function speedToText(bytesPerMillisecond) {
        const megabitsPerSecond = bytesPerMillisecond / 125
        if (megabitsPerSecond >= 1)
          return [`${Math.round(megabitsPerSecond)}`, 'Мбит/с']
        return [`${Math.round(bytesPerMillisecond * 8)}`, 'Кбит/с']
      }

      axios
        .get('https://st17.allmovies.uz/test.bin', {
          cancelToken: this.source.token,
          responseType: 'blob',
          onDownloadProgress: (progressEvent) => {
            this.checkBtn = false
            this.checkBtnNone = true
            if (typeof time !== 'number') time = progressEvent.timeStamp
            if (typeof loaded !== 'number') loaded = progressEvent.loaded

            const timeDelta = progressEvent.timeStamp - time
            const loadedDelta = progressEvent.loaded - loaded

            if (timeDelta >= 1000) {
              const bytesPerMillisecond = loadedDelta / timeDelta
              const [text, bytes] = speedToText(bytesPerMillisecond)
              this.text = text
              this.bytes = bytes
              speeds.push(bytesPerMillisecond)

              if (speeds.length >= 10) {
                this.average = speeds.reduce((a, b) => a + b, 0) / speeds.length
                this.average = speedToText(this.average)
                this.average = this.average.join(' ')
                this.source.cancel('Test finished')
                this.checkBtn = true
                this.checkBtnNone = false
              }

              time += timeDelta
              loaded += loadedDelta
            }
          },
        })
        .catch((error) => {
          if (isCancel(error)) {
            // console.log('Request canceled')
          } else {
            // console.log(error.message)
          }
        })
    },
    cancelCheckSpeed() {
      this.source.cancel()
      this.checkBtn = true
      this.checkBtnNone = false
    },
  },
}
</script>
<style lang="scss" scoped>
* {
  width: auto;
}
.speedttestContainer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}
.speedtest {
  height: 100%;
  width: 80%;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  @media only screen and (max-width: 431px) {
    flex-direction: column;
    padding-top: 80px;
    width: 100%;
  }
  &__left {
    display: flex;
    flex-direction: column;
    align-items: center;
    &-speedshow {
      border: 4px solid #fff;
      border-radius: 50%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      width: 300px;
      height: 300px;
      @media only screen and (max-width: 431px) {
        width: 200px;
        height: 200px;
      }
      .speedText {
        font-size: 74px;
        margin: 0;

        @media only screen and (max-width: 431px) {
          font-size: 40px;
        }
      }
      .bytes {
        font-size: 22px;
        margin: 0;
      }
      animation: crescendo 1.5s alternate infinite ease-in;
      @keyframes crescendo {
        0% {
          transform: scale(1);
        }
        100% {
          transform: scale(0.9);
        }
      }
    }
    .speedBtn {
      margin-top: 40px;
      border: none;
      padding: 0 20px;
      height: 50px;

      background: #56c1ff;

      color: #fff;
      border: none;
      border-radius: 5px;
      width: 250px;
      font-size: 18px;
      cursor: pointer;

      @media only screen and (max-width: 431px) {
        margin-left: 0;
      }
    }
    .speedBtnHidden {
      margin-top: 40px;
      border: none;
      padding: 0 20px;
      height: 50px;
      background: linear-gradient(to right, #bb7979 0%, #b00e0e 100%);
      // box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;
      color: #fff;
      border: none;
      border-radius: 5px;
      width: 250px;
      font-size: 18px;
      cursor: pointer;
    }
  }
  &__right {
    max-width: 500px;
    width: 100%;
    display: flex;
    flex-direction: column;
    font-size: 18px;
    backdrop-filter: blur(10px);
    background-color: #00000096;
    padding: 20px 20px;
    border-radius: 5px;
    @media only screen and (max-width: 431px) {
      padding-top: 10px;

      font-size: 14px;
      margin-top: 30px;
    }

    .listView {
      display: flex;
      justify-content: space-between;
      border-bottom: 1px solid rgba(128, 128, 128, 0.417);
      padding: 10px 10px;
      align-items: center;
      @media only screen and (max-width: 431px) {
        flex-direction: column;
      }
      .itemLeft {
        padding-right: 50px;
        color: rgb(193, 191, 191);
        @media only screen and (max-width: 431px) {
          padding-right: 0;
        }
      }
      .itemRight {
        text-align: end;
        @media only screen and (max-width: 431px) {
          text-align: start;
          padding-top: 10px;
        }
      }
    }
    .tasix {
      text-align: center;
      padding: 0 10px;
    }
  }
}
</style>
