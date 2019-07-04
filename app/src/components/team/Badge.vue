<template>
  <div v-if="badge === 1" class="text-center">
    <svg class="icon-color" :height="height" viewBox="0 0 175 320"><use xlink:href="assets/Crest1.svg#crest1"></use></svg>
  </div>
  <div v-else-if="badge === 2" class="text-center">
    <svg class="icon-color" :height="height" viewBox="-27 -25 275 275"><use xlink:href="assets/Crest2.svg#crest2"></use></svg>
  </div>
  <div v-else class="text-center">
    <svg class="icon-color" :height="height" viewBox="-20 -30 250 300"><use xlink:href="assets/Crest3.svg#crest3"></use></svg>
  </div>
</template>
<script>
export default {
  props: {
    color1: String,
    color2: String,
    color3: String,
    badge: Number,
    height: {
      default: '125px'
    }
  },
  mounted () {
    this.$el.style.setProperty('--color-1', this.color1)
    this.$el.style.setProperty('--color-2', this.color2)
    this.$el.style.setProperty('--color-3', this.color3)
  },
  watch: {
    color1 () {
      this.$el.style.setProperty('--color-1', this.color1)
    },
    color2 () {
      this.$el.style.setProperty('--color-2', this.color2)
    },
    color3 () {
      this.$el.style.setProperty('--color-3', this.color3)
    }
  }
}
</script>
<style lang="css" scoped>
.icon-color {
  --crest-color-1: var(--color-1);
  --crest-color-2: var(--color-2);
  --crest-color-3: var(--color-3);
}
</style>
