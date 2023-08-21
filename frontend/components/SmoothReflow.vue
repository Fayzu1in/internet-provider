<template lang="pug">
component(:is='tag')
  slot
</template>

<script>
import smoothReflow from 'vue-smooth-reflow'

export default {
  mixins: [smoothReflow],
  props: {
    tag: {
      type: String,
      default: 'div',
    },
    options: { type: Object, default: undefined },
  },
  mounted() {
    this.$smoothReflow(this.options)
  },
}
</script>
