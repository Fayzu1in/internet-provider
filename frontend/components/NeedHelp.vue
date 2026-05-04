<template lang="pug">
ModalDialog(@close='$emit("close")')
  .NeedHelp
    .NeedHelp__logo
      MaterialIcon(:icon='mdiAccessPointNetwork', color='#1bb8d1', size='40px')
    h2.NeedHelp__title {{ $t('cantChoose') }}
    p.NeedHelp__text {{ $t('callUsForHelp') }}
    .NeedHelp__contacts
      a.Contact.Contact--phone(@click='callCatcher' )
        MaterialIcon(:icon='mdiPhone', color='#fffff')
        span 78 113 70 71
      a.Contact.Contact--telegram(@click='telegram')
        MaterialIcon(:icon='mdiChatOutline', color='#1bb8d1')
        span {{ $t('telegram') }}
    hr.NeedHelp__divider
    .NeedHelp__schedule
      .Schedule
        MaterialIcon(:icon='mdiClockOutline', color='#1bb8d1', size='30px')
        p(v-html="$t('workDaily')")
      .Schedule
        MaterialIcon(:icon='mdiCalendarMonthOutline', color='#1bb8d1', size='46px')
        p {{ $t('contactTommorow') }}
    button.closeButton(@click='$emit("close")') Закрыть
</template>
<script>
import {
  mdiAccessPointNetwork,
  mdiClockOutline,
  mdiCalendarMonthOutline,
  mdiPhone,
  mdiChatOutline,
} from '@mdi/js'
export default {
  data() {
    return {
      mdiAccessPointNetwork,
      mdiClockOutline,
      mdiCalendarMonthOutline,
      mdiPhone,
      mdiChatOutline,
    }
  },
  methods: {
    async telegram() {
      try {
        await this.$api.clickCatcher('telegram')
      } catch (error) {
        console.error('Error occured', error)
      } finally {
        window.open('https://telegram.me/InternetBor', '_blank')
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
<style lang="scss">
.NeedHelp {
  background: rgba(15, 22, 32, 0.88);
  border-radius: 28px;
  padding: 30px 25px;
  position: relative;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: unset;
  padding-bottom: 80px;

  @media only screen and (max-width: 431px) {
    width: 90%;
    padding: 25px 20px;
    padding-bottom: 80px;
  }

  // Logo icon
  &__logo {
    width: 70px;
    height: 70px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.04);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  // Title
  &__title {
    margin: 20px 0 0;
    padding: 0 55px;
    color: #ffffff;
    font-size: 1.625rem;
    font-weight: 600;
    line-height: 30px;
    text-align: center;
    white-space: nowrap;

    @media only screen and (max-width: 431px) {
      padding: 0;
      margin-top: 15px;
      white-space: normal;
    }
  }
  &__text {
    margin: 10px 0 0;

    color: rgba(255, 255, 255, 0.6);
    font-size: 1rem;
    font-weight: 400;
    line-height: 22px;
    text-align: center;
  }
  &__contacts {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 15px;
    width: 100%;
    max-width: 360px;
    margin-top: 20px;

    @media only screen and (max-width: 431px) {
      width: 100%;
    }
  }

  // Divider line
  &__divider {
    width: 100%;
    height: 1px;
    margin: 28px 0;
    border: none;
    background: rgba(255, 255, 255, 0.06);
  }

  // Schedule info container
  &__schedule {
    display: flex;
    flex-direction: column;
    gap: 20px;
    width: 100%;
    max-width: 550px;
    text-align: left;

    @media only screen and (max-width: 431px) {
      gap: 20px;
    }
  }
  .closeButton {
    border: none;
    position: absolute;
    bottom: 0;
    cursor: pointer;
    background: linear-gradient(315deg, #ff410d, #bf2f66);
    color: #fff;
    width: 100%;
    font-size: 1.325rem;
    padding: 15px 0;

    &:active {
      opacity: 0.9;
    }
  }
}

.Contact {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  gap: 12px;
  width: 100%;
  min-width: 320px;
  padding: 15px 20px;
  color: #fff;
  font-size: 1.125rem;
  font-weight: 600;
  text-decoration: none;
  white-space: nowrap;
  border-radius: 15px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  background: linear-gradient(to bottom, #9bd7e1 0%, #1bb8d1 100%) no-repeat
    fixed;
  box-shadow: 0 8px 24px rgba(212, 165, 90, 0.065);

  cursor: pointer;
  transition: all 0.3s;

  @media only screen and (max-width: 431px) {
    height: 64px;
    padding: 0 24px;
  }

  span {
    flex: 1;
    text-align: center;
  }

  // Telegram variant
  &--telegram {
    background: transparent;
    border: 1.5px solid #1bb8d1;
  }

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 32px rgba(212, 165, 90, 0.12);
  }
}

// Schedule item component
.Schedule {
  display: flex;
  align-items: center;
  gap: 10px;
  color: rgba(255, 255, 255, 0.6);

  p {
    margin: 0;
    font-size: 1rem;
    line-height: 24px;
    text-align: left;

    @media only screen and (max-width: 431px) {
      font-size: 14px;
      line-height: 18px;
    }
  }

  .time-bold {
    color: #1bb8d1;
    font-weight: 600;
  }
}
</style>
