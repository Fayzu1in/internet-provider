<template lang="pug">
component.ActionButton(
  :is='to ? "NuxtLink" : "button"',
  :to='to',
  :type='to ? null : type',
  @click='$emit("click")',
  :disabled='disabled || loading',
  :aria-label='ariaLabel',
  :form='form'
)
  ActivityIndicator(v-if='loading')
  template(v-else)
    p.ActionButton__content(:content='content') {{content}}
</template>
<script>
export default {
  props: {
    disabled: {
      type: Boolean,
      default: false,
    },
    icon: {
      type: String,
      default: null,
    },
    to: {
      type: [String, Object],
      default: null,
    },
    type: {
      type: String,
      default: 'button',
      validator(value) {
        return ['button', 'submit', 'reset'].includes(value)
      },
    },
    ariaLabel: {
      type: String,
      default: undefined,
    },
    form: {
      type: String,
      default: undefined,
    },
    loading: {
      type: Boolean,
      default: undefined,
    },
    content: {
      type: String,
      default: null,
    },
  },
}
</script>
<style lang="scss">
.ActionButton {
  color: #fff;
  padding: 10px 20px;
  background: #1bb8d1;
  border: none;
  cursor: pointer;
  font-size: 18px;
  border-radius: 10px;
  text-align: center;
  text-decoration: none;
  transition: all 0.3s;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  &__content {
    margin: 0;
  }
}
</style>
