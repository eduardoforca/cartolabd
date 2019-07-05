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
            <badge class="col-12"
            :badge="this.$store.state.user.team.crest"
            :color1="this.$store.state.user.team.color1"
            :color2="this.$store.state.user.team.color2"
            :color3="this.$store.state.user.team.color3"
            />
            <div class="column q-ma-md items-start">
              <span class="card-title text-center full-width">Nome</span>
              <span class="text-bold text-center full-width">{{this.$store.state.user.team.nome}}</span>
              <span class="card-title text-center full-width">Patrimônio Líquido</span>
              <span class="text-bold text-center full-width">R$ {{this.$store.state.user.team.net_worth}}</span>
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
              <span class="text-bold text-center full-width">{{currentRound}}</span>
              <span class="card-title text-center full-width">Última Pontuação</span>
              <span class="text-bold text-center full-width">{{lastWeekScore}} pontos</span>
              <span class="card-title text-center full-width">Último Balanço</span>
              <span class="text-bold text-center full-width">R${{weekPrice - lastWeekPrice}}</span>
            </div>
          </div>
        </q-card-section>
      </q-card>
    </div>
    <q-card class="col-md-7 col-12" style="max-width: 800px">
      <q-card-section class="bg-secondary">
        <div class="row justify-between card-title text-uppercase text-white">
          <span>
            Escalação
          </span>
          <span>
            R$ {{currentPrice}}
          </span>
        </div>
      </q-card-section>
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
            <q-item v-for="i in formation.value[pos.id]" :key="pos.id + i" class="q-my-sm" clickable @click="buyingPlayers(pos.id, i)">
              <q-item-section avatar v-if="!getPos(pos.id, myPlayers)[i - 1]" >
                <q-avatar icon="add"></q-avatar>
              </q-item-section>
              <q-item-section avatar v-else>
                <img style="width: 35px" :src="getClub(getPos(pos.id, myPlayers)[i - 1].club)['crest']" />
              </q-item-section>
              <q-item-section>
                <div  v-if="getPos(pos.id, myPlayers)[i - 1]">
                  <q-item-label>
                    {{getPos(pos.id, myPlayers)[i - 1].nome}}
                  </q-item-label>
                  <q-item-label caption>Última Rodada: {{lastRoundScorePlayer(getPos(pos.id, myPlayers)[i - 1]['id'])}} pts</q-item-label>
                </div>
                <q-item-label v-else>Comprar {{pos.nome}}</q-item-label>
              </q-item-section>
              <q-item-section v-if="getPos(pos.id, myPlayers)[i - 1]" avatar>
                <q-item-label>R$ {{getPrice(getPos(pos.id, myPlayers)[i - 1]['id'])['price']}}</q-item-label>
              </q-item-section>
            </q-item>
          </div>
        </q-list>
      </q-card-section>
      <q-card-section>
        <q-btn color="primary" class="full-width" :disable="currentPrice > $store.state.user.team.net_worth || squad.length < 11"
          @click="finishTransaction"
          >Confirmar</q-btn>
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
        <q-card-section class="q-pa-none">
          <q-scroll-area style="height: 85vh">
            <q-list bordered separator>
              <q-item v-for="i in getPos(selectedPos, nonSelected)" :key="i['id']">
                <q-item-section avatar>
                  <img style="width: 35px" :src="getClub(i['club'])['crest']" />
                </q-item-section>
                <q-item-section>
                  <q-item-label>{{i['nome']}}</q-item-label>
                  <q-item-label caption>Última Rodada: {{lastRoundScorePlayer(i['id'])}} pts</q-item-label>
                </q-item-section>
                <q-item-section avatar>
                  <q-item-label>R$ {{getPrice(i['id'])['price']}}</q-item-label>
                </q-item-section>
                <q-item-section avatar>
                  <q-btn color="accent" round icon="add" @click="addPlayer(i['id'])"/>
                </q-item-section>
              </q-item>
            </q-list>
          </q-scroll-area>
        </q-card-section>
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
    buyPlayers: false,
    allPlayers: [],
    allClubs: [],
    allRounds: [],
    allPrices: [],
    allStats: [],
    allPlayerStats: [],
    allSquads: [],
    allSelected: [],
    currentRound: 3,
    selectedPos: 0
  }),
  mounted () {
    this.getAllFormations()
    let scope = this
    this.$api.get('player/').then((response) => {
      scope.allPlayers = response.data
    })
    this.$api.get('realClub/').then((response) => {
      scope.allClubs = response.data
    })
    this.$api.get('playerPrice/').then((response) => {
      scope.allPrices = response.data
    })
    this.$api.get('stat/').then((response) => {
      scope.allStats = response.data
    })
    this.$api.get('playerStats/').then((response) => {
      scope.allPlayerStats = response.data
    })
    this.$api.get('squad/').then((response) => {
      scope.allSquads = response.data
    })
    this.$api.get('selected/').then((response) => {
      scope.allSelected = response.data
    })
    this.$api.get('round/').then((response) => {
      scope.allRounds = response.data
    })
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
      let response = await this.$api.get('formation/')
      let fmts = response.data
      response = await this.$api.get('fmupos/')
      let fmupos = response.data
      response = await this.$api.get('position/')
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
          value: dict,
          id: val.id
        }
      })
      if (this.formations.length) {
        this.formation = this.formations[0]
      }
      this.loadingFormations = false
    },
    getPos (pos, array) {
      return array.filter((el) => {
        return el.position === pos
      })
    },
    lastRoundScorePlayer (playerId) {
      let pr = this.allPlayerStats.filter((pont) => {
        return pont.player === playerId && pont._round === this.lastRound.id
      })
      return pr.reduce((agg, el) => {
        let stat = this.allStats.find((st) => {
          return st.id === el.stat
        })
        if (stat) {
          return agg + el.amount * stat.points
        } else {
          return agg
        }
      }, 0)
    },
    selectionToPlayers (selection) {
      let players = []
      for (let player of selection) {
        let plr = this.allPlayers.find((el) => {
          return el.id === player.player
        })
        if (plr) {
          players.push(plr)
        }
      }
      return players
    },
    addPlayer (player) {
      this.squad.push({
        _round: this.round.id,
        club: this.$store.state.user.team.id,
        player: player
      })
      this.buyPlayers = false
    },
    buyingPlayers (pos, index) {
      this.selectedPos = pos
      let pl = this.getPos(pos, this.myPlayers)[index - 1]
      if (pl) {
        this.squad.splice(this.squad.findIndex((el) => {
          return el.player === pl.player
        }))
      }
      this.buyPlayers = true
    },
    getClub (clubId) {
      return this.allClubs.find((el) => {
        return el.id === clubId
      })
    },
    getPrice (player) {
      return this.allPrices.find((el) => {
        return el.player === player && el._round === this.round.id
      })
    },
    finishTransaction () {
      let previousSelection = this.allSelected.filter((el) => {
        return el._round === this.round.id && el.club === this.$store.state.user.team.id
      })
      for (let sel of previousSelection) {
        this.$api.delete(
          `/selected/${sel['id']}/`)
      }
      let previousSquad = this.allSquads.find((el) => {
        return el._round === this.round.id && el.club === this.$store.state.user.team.id
      })
      if (previousSquad) {
        this.$api.patch(
          `/squad/${previousSquad['id']}/`, { fmt: this.formation.id })
      } else {
        this.$api.post(
          `/squad/`, { fmt: this.formation.id, club: this.$store.state.user.team.id, _round: this.round.id })
      }
      for (let sel of this.squad) {
        this.$api.post(
          `/selected/`, sel)
      }
    }
  },
  computed: {
    lastWeekSelection () {
      if (!this.lastRound) {
        return []
      }
      return this.allSelected.filter((el) => {
        return el.club === this.$store.state.user.team.id && el._round === this.lastRound.id
      })
    },
    round () {
      return this.allRounds.find((el) => {
        return el.season === 2019 && el.round_number === this.currentRound
      })
    },
    lastRound () {
      return this.allRounds.find((el) => {
        return el.season === 2019 && el.round_number === (this.currentRound - 1)
      })
    },
    lastWeekPrice () {
      return this.lastWeekSelection.reduce((agg, el) => {
        let pr = this.allPrices.find((price) => {
          return price.player === el.player && price._round === el._round
        })
        if (pr) {
          return agg + pr.price
        } else {
          return agg
        }
      }, 0)
    },
    currentPrice () {
      return this.squad.reduce((agg, el) => {
        let pr = this.allPrices.find((price) => {
          return price.player === el.player && price._round === el._round
        })
        if (pr) {
          return agg + pr.price
        } else {
          return agg
        }
      }, 0)
    },
    lastWeekScore () {
      return this.lastWeekSelection.reduce((agg, el) => {
        let points = this.lastRoundScorePlayer(el.player)
        return agg + points
      }, 0)
    },
    weekPrice () {
      return this.lastWeekSelection.reduce((agg, el) => {
        let pr = this.allPrices.find((price) => {
          return price.player === el.player && price._round === this.round.id
        })
        if (pr) {
          return agg + pr.price
        } else {
          return agg
        }
      }, 0)
    },
    nonSelected () {
      return this.allPlayers.filter((el) => {
        let rel = this.squad.find((rl) => {
          return rl.player === el.id
        })
        return !rel
      })
    },
    myPlayers () {
      return this.selectionToPlayers(this.squad)
    }
  },
  watch: {
    round: {
      deep: true,
      handler () {
        this.squad = this.allSelected.filter((el) => {
          return el.club === this.$store.state.user.team.id && el._round === this.round.id
        })
      }
    },
    formation () {
      for (let pos of this.positions) {
        let amount = this.formation.value[pos.id]
        let posPlayers = this.getPos(pos.id, this.myPlayers)
        let currentAmount = posPlayers.length
        if (currentAmount > amount) {
          for (let player of posPlayers.slice(amount, currentAmount)) {
            this.squad.splice(this.squad.findIndex((el) => {
              return el.player === player.player
            }))
          }
        }
      }
    }
  }
}
</script>
<style lang="css" scoped>
</style>
