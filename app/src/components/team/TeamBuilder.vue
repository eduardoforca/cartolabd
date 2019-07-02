<template>
  <div class="q-pa-lg row items-center justify-center">
    <team-form-card class="col-12" style="max-width: 800px" @save="saveTeam"/>
  </div>
</template>
<script>
import TeamFormCard from './TeamFormCard'
export default {
  components: {
    TeamFormCard
  },
  methods: {
    saveTeam () {
      return true
    }
  }
}
</script>
<style lang="css" scoped>
</style>
