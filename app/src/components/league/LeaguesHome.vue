<template>
  <div class="q-pa-lg row items-start justify-center">
    <q-card class="col-12" style="max-width: 800px">
      <q-card-section class="bg-secondary">
        <div class="row justify-between items-center">
          <span class="card-title text-uppercase text-white">Minhas Ligas</span>
          <q-btn to="leagues/new" color="primary" dense>Criar Liga</q-btn>
        </div>
      </q-card-section>
      <q-card-section>
        <q-list bordered class="q-my-md">
          <q-item v-for="i in myleagues" :key="i[id_league]" class="q-my-sm" clickable :to="`/leagues/manage/${i['id_league']}`">
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
    <q-card class="col-12 q-mt-md" style="max-width: 800px">
      <q-card-section class="bg-secondary card-title text-uppercase text-white">Todas as Ligas</q-card-section>
      <q-card-section>
        <q-list bordered class="q-my-md">
          <q-item v-for="i in allLeagues" :key="i[id_league]" class="q-my-sm" clickable :to="`/leagues/manage/${i['id_league']}`">
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
  </div>
</template>
<script>
import Badge from '../team/Badge'
export default {
  components: {
    Badge
  },
  data: () => ({
    myleagues: [{ 'id_league': 1, 'name': 'Liga da BOA' }],
    allLeagues: [{ 'id_league': 1, 'name': 'Liga da BOA' }]
  }),
  mounted () {
  },
  methods: {
  },
  computed: {
  }
}
</script>
<style lang="css" scoped>
</style>
