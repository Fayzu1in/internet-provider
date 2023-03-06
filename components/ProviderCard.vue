<template lang="pug">
section.Providers.container-fluid
  .provider
    .provider__title Uzonline
    .provider__card
      .provider__card-name Yangi
      .provider__card-costFrom от 109.000
    

</template>
<script>
export default {
  data() {
    return {
      tariff: [
        {
          name: 'yangi',
          costfrom: '100.000',
        },
        {
          name: 'yangi 2',
          costfrom: '102.000',
        },
        {
          name: 'yangi 3',
          costfrom: '103.000',
        },
      ],
    }
  },
}
</script>
<style lang="scss" scoped>
.Providers {
  background-color: #00000096;
  padding: 15px 10px;
  .provider {
    &__title {
      font-size: 28px;
    }
  }
}
</style>
