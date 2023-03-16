<template lang="pug">
section.modalWindow
  .modal 
    .modal__title Заявка отправлена
    .modal__subtitle С вами свяжутся в течении 15-20 минут
    button.modal__closeBtn 
      MaterialIcon(:icon='mdiClose')
</template>
<script>
import { mdiClose } from '@mdi/js'
export default {
  data() {
    return {
      mdiClose,
    }
  },
}
</script>
<style lang="scss"></style>
