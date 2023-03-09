export { default as AddressForm } from '../../components/AddressForm.vue'
export { default as AddressSection } from '../../components/AddressSection.vue'
export { default as BetterOffers } from '../../components/BetterOffers.vue'
export { default as BetterofferCard } from '../../components/BetterofferCard.vue'
export { default as HeroBackground } from '../../components/HeroBackground.vue'
export { default as MaterialIcon } from '../../components/MaterialIcon.vue'
export { default as ProviderCard } from '../../components/ProviderCard.vue'
export { default as TariffCard } from '../../components/TariffCard.vue'
export { default as TheFooter } from '../../components/TheFooter.vue'
export { default as TheNavbar } from '../../components/TheNavbar.vue'
export { default as TopProviders } from '../../components/TopProviders.vue'

// nuxt/nuxt.js#8607
function wrapFunctional(options) {
  if (!options || !options.functional) {
    return options
  }

  const propKeys = Array.isArray(options.props) ? options.props : Object.keys(options.props || {})

  return {
    render(h) {
      const attrs = {}
      const props = {}

      for (const key in this.$attrs) {
        if (propKeys.includes(key)) {
          props[key] = this.$attrs[key]
        } else {
          attrs[key] = this.$attrs[key]
        }
      }

      return h(options, {
        on: this.$listeners,
        attrs,
        props,
        scopedSlots: this.$scopedSlots,
      }, this.$slots.default)
    }
  }
}
