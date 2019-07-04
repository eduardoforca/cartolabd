<template>
  <div v-if="$store.state.user.team">
    Você ainda não tem um time
    <q-btn to="new">Criar Time</q-btn>
  </div>
  <div v-else class="q-pa-lg row items-start justify-between relative-position">
    <div class="col-md-4 col-12">
      <q-card class="q-mb-md" style="max-width: 800px">
        <q-card-section class="bg-secondary card-title text-uppercase text-white">Liga</q-card-section>
        <q-card-section>
          <div class="row justify-around">
            <badge
              :color1="league.color1"
              :color2="league.color2"
              :color3="league.color3"
            />
            <div class="column q-ma-md items-start">
              <span class="card-title text-center full-width">Nome</span>
              <span class="text-bold text-center full-width">{{league.name}}</span>
            </div>
          </div>
          <div class="row justify-center" v-if="league.creator === $store.state.user.user.id">
            <q-btn color="primary" @click="editing = true">Editar Liga</q-btn>
          </div>
        </q-card-section>
      </q-card>
    </div>
    <q-card class="col-md-7 col-12" style="max-width: 800px">
      <q-card-section class="bg-secondary">
        <div class="row justify-between items-center">
          <span class="card-title text-uppercase text-white">Membros</span>
          <q-btn @click="addTeams = true" color="primary" v-if="league.creator === $store.state.user.user.id" dense>Adicionar Times</q-btn>
        </div>
      </q-card-section>
      <q-card-section class="q-mt-md">
        <q-list bordered separator>
          <q-item v-for="i in members" :key="i['id']">
            <q-item-section avatar>
              <badge height="50px"/>
            </q-item-section>
            <q-item-section>
              <q-item-label>{{i['name']}}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-card-section>
    </q-card>
    <q-dialog v-model="editing">
      <league-form-card :initial-value="league" style="min-width: 60vw" @save="saveLeague"/>
    </q-dialog>
    <q-dialog v-model="addTeams">
      <q-card style="min-width: 40vw" class="relative-position">
        <q-card-section class="bg-secondary card-title text-uppercase text-white">Adicionar Membros</q-card-section>
        <q-list bordered separator>
          <q-item v-for="i in users" :key="i['id']">
            <q-item-section avatar>
              <badge height="50px"
              :color1="i.color1"
              :color2="i.color2"
              :color3="i.color3"
              />
            </q-item-section>
            <q-item-section>
              <q-item-label>{{i['nome']}}</q-item-label>
            </q-item-section>
            <q-item-section avatar>
              <q-btn color="accent" round icon="add" @click="addMember(i.id)"/>
            </q-item-section>
          </q-item>
        </q-list>
        <q-inner-loading :showing="loading">
          <q-spinner size="50px" color="primary" />
        </q-inner-loading>
      </q-card>
    </q-dialog>
    <q-inner-loading :showing="loading">
      <q-spinner size="50px" color="primary" />
    </q-inner-loading>
  </div>
</template>
<script>
import Badge from '../team/Badge'
import LeagueFormCard from './LeagueFormCard'
export default {
  components: {
    Badge,
    LeagueFormCard
  },
  data: () => ({
    members: [],
    users: [],
    league: undefined,
    editing: false,
    addTeams: false,
    loadingTeams: false
  }),
  async mounted () {
    this.loading = true
    let response = await this.$api.get(`league/${this.$route.params.league_id}`)
    this.league = response.data
    this.loading = false
    this.getAllTeams()
  },
  methods: {
    async saveLeague (league) {
      this.loading = true
      try {
        let response = await this.$api.put(
          `/league/${this.league.id}/`,
          { ...league, creator: this.$store.state.user.user.id })
        if (response.status === 200) {
          this.league = response.data
          this.editing = false
          this.loading = false
        } else {
          throw response.statusText
        }
      } catch (e) {
        this.loading = false
        console.log(e)
      }
    },
    async getAllTeams () {
      this.loadingTeams = true
      let response = await this.$api.get('userClub')
      this.users = response.data
      this.loadingTeams = false
    },
    async addMember (idMember) {
      try {
        let response = await this.$api.post(
          '/clubLeague/',
          { club: idMember, league: this.league.id })
        if (response.status !== 201) {
          throw response.statusText
        }
      } catch (e) {
        console.log(e)
      }
    }
  },
  computed: {
  }
}
</script>
<style lang="css" scoped>
</style>
