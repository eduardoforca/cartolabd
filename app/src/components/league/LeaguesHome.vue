<template>
  <div class="q-pa-lg row items-start justify-center relative-position">
    <q-card class="col-12" style="max-width: 800px">
      <q-card-section class="bg-secondary">
        <div class="row justify-between items-center">
          <span class="card-title text-uppercase text-white">Minhas Ligas</span>
          <q-btn to="leagues/new" color="primary" dense>Criar Liga</q-btn>
        </div>
      </q-card-section>
      <q-card-section>
        <q-list bordered class="q-my-md" separator>
          <q-item v-for="i in myLeagues" :key="i['id']" clickable :to="`/leagues/manage/${i['id']}`">
            <q-item-section avatar>
              <badge height="50px"
              :badge="i.crest"
              :color1="i.color1"
              :color2="i.color2"
              :color3="i.color3"/>
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
        <q-list bordered class="q-my-md" separator>
          <q-item v-for="i in allLeagues" :key="i['id']" clickable :to="`/leagues/manage/${i['id']}`">
            <q-item-section avatar>
              <badge height="50px"
              :badge="i.crest"
              :color1="i.color1"
              :color2="i.color2"
              :color3="i.color3"/>
            </q-item-section>
            <q-item-section>
              <q-item-label>{{i['name']}}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-card-section>
    </q-card>
    <q-inner-loading :showing="loading">
      <q-spinner size="50px" color="primary" />
    </q-inner-loading>
  </div>
</template>
<script>
import Badge from '../team/Badge'
export default {
  components: {
    Badge
  },
  data: () => ({
    leaguesRelationships: [],
    allLeagues: [],
    loading: false
  }),
  async mounted () {
    this.loading = true
    let responses = await Promise.all([
      this.$api.get('league/'),
      this.$api.get('clubLeague/')
    ])
    this.allLeagues = responses[0].data
    this.leaguesRelationships = responses[1].data
    this.loading = false
  },
  methods: {
  },
  computed: {
    myLeagues () {
      let rels = this.leaguesRelationships.filter((el) => {
        return el.club === this.$store.state.user.team['id']
      })
      return this.allLeagues.filter((el) => {
        let rel = rels.find((rl) => {
          return rl.league === el.id
        })
        return !!rel
      })
    }
  }
}
</script>
<style lang="css" scoped>
</style>
