<template>
  <div class="q-pa-lg row items-center justify-center relative-position">
    <team-form-card class="col-12" style="max-width: 800px" @save="saveTeam"/>
    <q-inner-loading :showing="loading">
      <q-spinner size="50px" color="primary" />
    </q-inner-loading>
  </div>
</template>
<script>
import TeamFormCard from './TeamFormCard'
export default {
  components: {
    TeamFormCard
  },
  data () {
    return {
      loading: false
    }
  },
  methods: {
    async saveTeam (team) {
      this.loading = true
      try {
        let response = await this.$api.post(
          '/userClub/',
          { ...team, owner: this.$store.state.user.user.id })
        if (response.status === 201) {
          this.$store.commit('user/setTeam', { team: response.data })
          this.$router.push('manage')
        } else {
          throw response.statusText
        }
      } catch (e) {
        this.loading = false
        console.log(e)
      }
    }
  }
}
</script>
<style lang="css" scoped>
</style>
