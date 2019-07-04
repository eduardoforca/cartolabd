<template>
  <div class="q-pa-lg row items-center justify-center relative-position">
    <league-form-card class="col-12" style="max-width: 800px" @save="saveLeague"/>
    <q-inner-loading :showing="loading">
      <q-spinner size="50px" color="primary" />
    </q-inner-loading>
  </div>
</template>
<script>
import LeagueFormCard from './LeagueFormCard'
export default {
  components: {
    LeagueFormCard
  },
  data () {
    return {
      loading: false
    }
  },
  methods: {
    async saveLeague (league) {
      this.loading = true
      try {
        let response = await this.$api.post(
          '/league/',
          { ...league, creator: this.$store.state.user.user.id })
        if (response.status === 201) {
          this.$router.push(`manage/${response.data.id}`)
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
