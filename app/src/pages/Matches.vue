<template>
  <div class="q-pa-lg row items-start justify-center">
    <q-card class="col-md-7 col-12" style="max-width: 800px">
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
          <q-item v-for="i in matches" :key="i['id_match']">
            <q-item-section avatar>
              <div class="column text-center">
                <span>{{formatDate(i['datetime'])}}</span>
                <span>{{formatTime(i['datetime'])}}</span>
              </div>
            </q-item-section>
            <q-item-section>
              <div class="row justify-around items-center">
                <div class="row justify-around col-4 items-center">
                  <span class="team-score">
                    {{i['home_club']}}
                  </span>
                  <span class="score">
                    {{i['home_score']}}
                  </span>
                </div>
                <span class="text-bold" style="font-size: 25px">
                 x
                </span>
                <div class="row justify-around col-4 items-center">
                  <span class="score">
                    {{i['away_score']}}
                  </span>
                  <span class="team-score">
                    {{i['away_club']}}
                  </span>
                </div>
              </div>
            </q-item-section>
          </q-item>
        </q-list>
      </q-card-section>
    </q-card>
  </div>
</template>
<script>
import moment from 'moment'
export default {
  data: () => ({
    matches: [
      {
        id_match: 1,
        datetime: new Date(),
        home_score: 3,
        away_score: 3,
        home_club: 'VAS',
        away_club: 'FLA'
      },
      {
        id_match: 2,
        datetime: new Date(),
        home_score: 3,
        away_score: 3,
        home_club: 'VAS',
        away_club: 'FLA'
      }
    ],
    round: 1,
    season: 2019,
    roundOptions: [],
    seasonOptions: [2019]
  }),
  created () {
    for (let i = 1; i < 39; i++) {
      this.roundOptions.push(i)
    }
  },
  methods: {
    formatDate (date) {
      return moment(date).format('DD/MM/YYYY')
    },
    formatTime (date) {
      return moment(date).format('HH:mm')
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
  font-size: 26px;
  letter-spacing: 1.7px;
  font-weight: 300;
}
</style>
