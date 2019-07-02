<template>
  <div v-if="$store.state.user.team">
    Você ainda não tem um time
    <q-btn to="new">Criar Time</q-btn>
  </div>
  <div v-else class="q-pa-lg row items-start justify-between">
    <div class="col-md-4 col-12">
      <q-card class="q-mb-md" style="max-width: 800px">
        <q-card-section class="bg-secondary card-title text-uppercase text-white">Liga</q-card-section>
        <q-card-section>
          <div class="row justify-around">
            <badge/>
            <div class="column q-ma-md items-start">
              <span class="card-title text-center full-width">Nome</span>
              <span class="text-bold text-center full-width">Minha Liga</span>
            </div>
          </div>
          <div class="row justify-center">
            <q-btn color="primary" @click="editing = true">Editar Liga</q-btn>
          </div>
        </q-card-section>
      </q-card>
    </div>
    <q-card class="col-md-7 col-12" style="max-width: 800px">
      <q-card-section class="bg-secondary">
        <div class="row justify-between items-center">
          <span class="card-title text-uppercase text-white">Membros</span>
          <q-btn @click="addTeams = true" color="primary" dense>Adicionar Times</q-btn>
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
      <league-form-card style="min-width: 60vw" @save="saveTeam"/>
    </q-dialog>
    <q-dialog v-model="addTeams">
      <q-card style="min-width: 40vw">
        <q-card-section class="bg-secondary card-title text-uppercase text-white">Adicionar Membros</q-card-section>
        <q-list bordered separator>
          <q-item v-for="i in users" :key="i['id']">
            <q-item-section avatar>
              <badge height="50px"/>
            </q-item-section>
            <q-item-section>
              <q-item-label>{{i['name']}}</q-item-label>
            </q-item-section>
            <q-item-section avatar>
              <q-btn color="accent" round icon="add"/>
            </q-item-section>
          </q-item>
        </q-list>
      </q-card>
    </q-dialog>
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
    members: [
      { id: 1, name: 'Peladeiros' },
      { id: 2, name: 'Peladeiros' }
    ],
    users: [
      { id: 1, name: 'Peladeiros' },
      { id: 2, name: 'Peladeiros' }
    ],
    editing: false,
    addTeams: false
  }),
  mounted () {
  },
  methods: {
    saveTeam () {
      this.editing = false
    }
  },
  computed: {
  }
}
</script>
<style lang="css" scoped>
</style>
