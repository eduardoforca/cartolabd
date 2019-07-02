<template>
  <div class="q-pa-lg row items-center justify-center">
    <league-form-card class="col-12" style="max-width: 800px" @save="saveLeague"/>
  </div>
</template>
<script>
import LeagueFormCard from './LeagueFormCard'
export default {
  components: {
    LeagueFormCard
  },
  methods: {
    saveLeague () {
      return true
    }
  }
}
</script>
<style lang="css" scoped>
</style>
