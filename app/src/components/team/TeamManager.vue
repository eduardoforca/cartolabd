<template>
  <div v-if="!$store.state.user.team" class="q-pa-lg row items-start justify-between">
    <div class="column items-center full-width">
      <h6>
        Você ainda não tem um time
      </h6>
      <q-btn to="new" color="primary">Criar Time</q-btn>
    </div>
  </div>
  <div v-else class="q-pa-lg row items-start justify-between">
    <div class="col-md-4 col-12">
      <q-card class="q-mb-md" style="max-width: 800px">
        <q-card-section class="bg-secondary card-title text-uppercase text-white">Meu Time</q-card-section>
        <q-card-section>
          <div class="row justify-around">
            <badge
            :color1="this.$store.state.user.team.color1"
            :color2="this.$store.state.user.team.color2"
            :color3="this.$store.state.user.team.color3"
            />
            <div class="column q-ma-md items-start">
              <span class="card-title text-center full-width">Nome</span>
              <span class="text-bold text-center full-width">{{this.$store.state.user.team.nome}}</span>
              <span class="card-title text-center full-width">Patrimônio Líquido</span>
              <span class="text-bold text-center full-width">{{this.$store.state.user.team.networth}}</span>
            </div>
          </div>
          <div class="row justify-center">
            <q-btn color="primary" @click="editing = true">Editar Time</q-btn>
          </div>
        </q-card-section>
      </q-card>
      <q-card class="q-mb-md" style="max-width: 800px">
        <q-card-section class="bg-secondary card-title text-uppercase text-white">Resumo da Rodada</q-card-section>
        <q-card-section>
          <div class="row justify-around">
            <div class="column q-ma-md items-start">
              <span class="card-title text-center full-width">Rodada Atual</span>
              <span class="text-bold text-center full-width">25</span>
              <span class="card-title text-center full-width">Última Pontuação</span>
              <span class="text-bold text-center full-width">74 pontos</span>
              <span class="card-title text-center full-width">Último Balanço</span>
              <span class="text-bold text-center full-width">+ R$12</span>
            </div>
          </div>
        </q-card-section>
      </q-card>
    </div>
    <q-card class="col-md-7 col-12" style="max-width: 800px">
      <q-card-section class="bg-secondary card-title text-uppercase text-white">Escalação</q-card-section>
      <q-card-section class="q-my-md relative-position">
        <q-select outlined v-model="formation" :options="formations" label="Formação" />
        <q-inner-loading :showing="loadingFormations">
          <q-spinner size="50px" color="primary" />
        </q-inner-loading>
      </q-card-section>
      <q-card-section>
        <q-list bordered v-if="formation">
          <div v-for="pos in positions" :key="pos.id">
            <q-separator/>
            <q-item-label header>{{pos.nome}}</q-item-label>
            <q-item v-for="i in formation.value[pos.id]" :key="pos.id + i" class="q-my-sm" clickable @click="buyPlayers = true">
              <q-item-section avatar v-if="!getPos(pos.id)[i]" >
                <q-avatar icon="add"></q-avatar>
              </q-item-section>
              <q-item-section>
                <q-item-label v-if="getPos(pos.id)[i]">{{getPos(pos.id)[i].name}}</q-item-label>
                <q-item-label v-else>Comprar {{pos.nome}}</q-item-label>
              </q-item-section>
            </q-item>
          </div>
        </q-list>
      </q-card-section>
    </q-card>
    <q-dialog v-model="editing">
      <div class="relative-position" style="min-width: 60vw">
        <team-form-card :initial-value="this.$store.state.user.team" @save="saveTeam"/>
        <q-inner-loading :showing="loading" class="full-width">
          <q-spinner size="50px" color="primary" />
        </q-inner-loading>
      </div>
    </q-dialog>
    <q-dialog v-model="buyPlayers">
      <q-card style="min-width: 40vw" class="relative-position">
        <q-card-section class="bg-secondary card-title text-uppercase text-white">Comprar Jogadores</q-card-section>
        <q-list bordered separator>
          <q-item v-for="i in 0" :key="i['id']">
            <q-item-section avatar>
              <!-- <badge height="50px"
              :color1="i.color1"
              :color2="i.color2"
              :color3="i.color3"
              /> -->
            </q-item-section>
            <q-item-section>
              <q-item-label>{{i['nome']}}</q-item-label>
            </q-item-section>
            <q-item-section avatar>
              <q-btn color="accent" round icon="add"/>
            </q-item-section>
          </q-item>
        </q-list>
        <q-inner-loading :showing="loading">
          <q-spinner size="50px" color="primary" />
        </q-inner-loading>
      </q-card>
    </q-dialog>
  </div>
</template>
<script>
import Badge from './Badge'
import TeamFormCard from './TeamFormCard'
export default {
  components: {
    Badge,
    TeamFormCard
  },
  data: () => ({
    formations: [],
    formation: '',
    squad: [],
    editing: false,
    loading: false,
    positions: [],
    loadingFormations: false,
    buyPlayers: false
  }),
  mounted () {
    this.getAllFormations()
  },
  methods: {
    async saveTeam (team) {
      this.loading = true
      try {
        let response = await this.$api.put(
          `/userClub/${this.$store.state.user.team.id}/`,
          { ...team, owner: this.$store.state.user.user.id })
        if (response.status === 200) {
          this.$store.commit('user/setTeam', { team: response.data })
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
    async getAllFormations () {
      this.loadingFormations = true
      let response = await this.$api.get('formation')
      let fmts = response.data
      response = await this.$api.get('fmupos')
      let fmupos = response.data
      response = await this.$api.get('position')
      this.positions = response.data
      this.formations = fmts.map((val) => {
        let dict = (fmupos.filter((el) => {
          return el.formation === val.id
        })).reduce(
          (agg, el) => {
            agg[el.position] = el.amount
            return agg
          }, {}
        )
        return {
          label: val.nome,
          value: dict
        }
      })
      if (this.formations.length) {
        this.formation = this.formations[0]
      }
      this.loadingFormations = false
    },
    getPos (pos) {
      return []
    }
  }
}
</script>
<style lang="css" scoped>
</style>
