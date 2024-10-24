<template lang="pug">
section.container-fluid
  .aboutCompany 
    .aboutInternetbor 
      p {{ $t('internetborIs') }}
    .header {{$t('aboutCompany')}}
    .content 
      .title {{ $t('howServiceWorks') }}
      .subtitle {{ $t('howServiceWorksPrompt') }}
      .title {{ $t('searchByAddress') }}
      .subtitle {{ $t('searchByAddressPrompt') }}
      .title {{ $t('applicationForm') }}
      .subtitle {{ $t('applicationFormPrompt') }}
      .title {{ $t('whyDoWeNeedThisService') }}
      .subtitle.nested {{ $t('whyDoWeNeedThisServicePrompr1') }}
      .subtitle.nestedSub {{ $t('whyDoWeNeedThisServicePrompr11') }}
      .subtitle.nested {{ $t('whyDoWeNeedThisServicePrompr2') }}
      .subtitle.nestedSub {{ $t('whyDoWeNeedThisServicePrompr22') }}
      .subtitle.nested {{ $t('whyDoWeNeedThisServicePrompr3') }}
      .subtitle.nestedSub {{ $t('whyDoWeNeedThisServicePrompr33') }}
      .title {{ $t('whyWeAreTrusted') }}
      .subtitle {{ $t('whyWeAreTrustedPrompt') }}
</template>
<script>
export default {}
</script>
<style lang="scss" scoped>
.aboutInternetbor {
  display: flex;
  justify-content: center;
  p {
    width: 100%;
    text-align: center;
    font-size: 24px;
    margin: 0;
    line-height: 30px;
    padding-bottom: 30px;
  }
}
.aboutCompany {
  margin-top: 30px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-color: rgba(255, 255, 255, 0.5764705882);
  padding: 15px 20px;
  border-radius: 15px;
  backdrop-filter: blur(5px);
  color: #001b48;
  text-align: left;
  @media only screen and (max-width: 576px) {
    margin-top: 0;
  }
  .header {
    font-size: 32px;
    padding-bottom: 15px;
  }
  .content {
    .title {
      font-size: 24px;
      padding-bottom: 15px;
    }
    .subtitle {
      font-size: 20px;
    }
    .subtitle:not(:last-child) {
      padding-bottom: 30px;
    }
    .nested {
      padding-bottom: 10px !important;
    }
    .nestedSub {
      padding-left: 20px;
      padding-bottom: 5px;
    }
  }
}
</style>
