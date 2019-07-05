<template>
  <div class="q-pa-lg row items-start justify-center relative-position">
    <q-card class="col-12" style="max-width: 800px">
      <q-card-section class="bg-secondary">
        <div class="row justify-between items-center">
          <span class="card-title text-uppercase text-white">Partidas</span>
        </div>
      </q-card-section>
      <q-card-section class="q-my-md">
        <div class="row justify-around">
          <q-select class="col-md-6 col-12" outlined v-model="round" :options="roundOptions" label="Rodada" />
          <q-select class="col-md-6 col-12" outlined v-model="season" :options="seasonOptions" label="Temporada" />
        </div>
      </q-card-section>
      <q-card-section class="q-mt-md">
        <q-list bordered dense separator>
          <q-item v-for="i in filteredMatches" :key="i['id_match']">
            <q-item-section avatar>
              <div class="column text-center">
                <span>{{formatDate(i['datetime'])}}</span>
                <span>{{formatTime(i['datetime'])}}</span>
              </div>
            </q-item-section>
            <q-item-section>
              <div class="row justify-around items-center">
                <div class="row justify-around col-4 items-center">
                  <div class="column items-center">
                    <img class="club-crest" :src="getClub(i['home_club'])['crest']" />
                    <span class="team-score">
                      {{getClub(i['home_club'])['short_name']}}
                    </span>
                  </div>
                  <span class="score">
                    {{i['home_score'] !== null ? i['home_score'] : '-'}}
                  </span>
                </div>
                <span class="text-bold" style="font-size: 25px">
                 x
                </span>
                <div class="row justify-around col-4 items-center">
                  <span class="score">
                    {{i['away_score'] !== null ? i['away_score'] : '-'}}
                  </span>
                  <div class="column items-center">
                    <img class="club-crest" :src="getClub(i['away_club'])['crest']" />
                    <span class="team-score">
                      {{getClub(i['away_club'])['short_name']}}
                    </span>
                  </div>
                </div>
              </div>
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
import moment from 'moment'
export default {
  data: () => ({
    allMatches: [],
    realClubs: [],
    round: {},
    season: 2019,
    rounds: [],
    seasonOptions: [2019],
    loading: false
  }),
  created () {
  },
  async mounted () {
    this.loading = true
    let response = await Promise.all([
      this.$api.get('match/'),
      this.$api.get('round/'),
      this.$api.get('realClub/')
    ])
    this.allMatches = response[0].data
    this.rounds = response[1].data
    this.realClubs = response[2].data
    this.loading = false
  },
  methods: {
    formatDate (date) {
      return moment(date).format('DD/MM/YYYY')
    },
    formatTime (date) {
      return moment(date).format('HH:mm')
    },
    getClub (id) {
      return this.realClubs.find((el) => {
        return el.id === id
      })
    }
  },
  computed: {
    filteredMatches () {
      return this.allMatches.filter((el) => {
        return this.round['value'] && el._round === this.round.value['id']
      })
    },
    roundOptions () {
      return this.rounds.filter((el) => {
        return el.season === this.season
      }).map((el) => {
        return {
          label: el.round_number,
          value: el
        }
      })
    }
  }
}
</script>
<style lang="css" scoped>
.score {
  font-size: 32px;
  letter-spacing: 1.7px;
  font-weight: 300;
}
.team-score {
  font-size: 22px;
  letter-spacing: 1.7px;
  font-weight: 300;
}
.club-crest {
  width: 50px
}
</style>
