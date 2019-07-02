<template>
  <div v-if="$store.state.user.team">
    Você ainda não tem um time
    <q-btn to="new">Criar Time</q-btn>
  </div>
  <div v-else class="q-pa-lg row items-start justify-between">
    <div class="col-md-4 col-12">
      <q-card class="q-mb-md" style="max-width: 800px">
        <q-card-section class="bg-secondary card-title text-uppercase text-white">Meu Time</q-card-section>
        <q-card-section>
          <div class="row justify-around">
            <badge/>
            <div class="column q-ma-md items-start">
              <span class="card-title text-center full-width">Nome</span>
              <span class="text-bold text-center full-width">Meu Time</span>
              <span class="card-title text-center full-width">Patrimônio Líquido</span>
              <span class="text-bold text-center full-width">R$ 100</span>
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
      <q-card-section class="q-my-md">
        <q-select outlined v-model="formation" :options="formations" label="Formação" />
      </q-card-section>
      <q-card-section>
        <q-list bordered>
          <q-item-label header>Goleiro</q-item-label>
          <q-item class="q-my-sm" clickable>
            <q-item-section avatar v-if="!gks[0]" >
              <q-avatar icon="add"></q-avatar>
            </q-item-section>
            <q-item-section>
              <q-item-label v-if="gks[0]">{{gks[0].name}}</q-item-label>
              <q-item-label v-else>Comprar Goleiro</q-item-label>
            </q-item-section>
          </q-item>
          <q-separator/>
          <q-item-label header>Defensores</q-item-label>
          <q-item v-for="i in formation.value[0].amount" :key="'def' + i" class="q-my-sm" clickable>
            <q-item-section avatar v-if="!def[i]" >
              <q-avatar icon="add"></q-avatar>
            </q-item-section>
            <q-item-section>
              <q-item-label v-if="def[i]">{{def[i].name}}</q-item-label>
              <q-item-label v-else>Comprar Defensor</q-item-label>
            </q-item-section>
          </q-item>
          <q-separator/>
          <q-item-label header>Meio-campistas</q-item-label>
          <q-item v-for="i in formation.value[1].amount" :key="'mei' + i" class="q-my-sm" clickable>
            <q-item-section avatar v-if="!mei[i]" >
              <q-avatar icon="add"></q-avatar>
            </q-item-section>
            <q-item-section>
              <q-item-label v-if="mei[i]">{{mei[i].name}}</q-item-label>
              <q-item-label v-else>Comprar Meio-campista</q-item-label>
            </q-item-section>
          </q-item>
          <q-separator/>
          <q-item-label header>Atacantes</q-item-label>
          <q-item v-for="i in formation.value[2].amount" :key="'ata' + i" class="q-my-sm" clickable>
            <q-item-section avatar v-if="!ata[i]" >
              <q-avatar icon="add"></q-avatar>
            </q-item-section>
            <q-item-section>
              <q-item-label v-if="ata[i]">{{ata[i].name}}</q-item-label>
              <q-item-label v-else>Comprar Atacante</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-card-section>
    </q-card>
    <q-dialog v-model="editing">
      <team-form-card style="min-width: 60vw" @save="saveTeam"/>
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
    formations: [
      { label: '3-4-3', value: [{ cod_pos: 'DEF', amount: 3 }, { cod_pos: 'MEI', amount: 4 }, { cod_pos: 'ATA', amount: 3 }] },
      { label: '3-5-2', value: [{ cod_pos: 'DEF', amount: 3 }, { cod_pos: 'MEI', amount: 5 }, { cod_pos: 'ATA', amount: 2 }] },
      { label: '4-2-4', value: [{ cod_pos: 'DEF', amount: 4 }, { cod_pos: 'MEI', amount: 2 }, { cod_pos: 'ATA', amount: 4 }] },
      { label: '4-3-3', value: [{ cod_pos: 'DEF', amount: 4 }, { cod_pos: 'MEI', amount: 3 }, { cod_pos: 'ATA', amount: 3 }] },
      { label: '4-4-2', value: [{ cod_pos: 'DEF', amount: 4 }, { cod_pos: 'MEI', amount: 4 }, { cod_pos: 'ATA', amount: 2 }] },
      { label: '4-5-1', value: [{ cod_pos: 'DEF', amount: 4 }, { cod_pos: 'MEI', amount: 5 }, { cod_pos: 'ATA', amount: 1 }] },
      { label: '5-3-2', value: [{ cod_pos: 'DEF', amount: 5 }, { cod_pos: 'MEI', amount: 3 }, { cod_pos: 'ATA', amount: 2 }] },
      { label: '5-4-1', value: [{ cod_pos: 'DEF', amount: 5 }, { cod_pos: 'MEI', amount: 4 }, { cod_pos: 'ATA', amount: 1 }] }
    ],
    formation: { label: '3-4-3', value: [{ cod_pos: 'DEF', amount: 3 }, { cod_pos: 'MEI', amount: 4 }, { cod_pos: 'ATA', amount: 3 }] },
    squad: [],
    editing: false
  }),
  mounted () {
  },
  methods: {
    saveTeam () {
      this.editing = false
    }
  },
  computed: {
    gks () {
      return this.squad.filter((el) => {
        return el.pos === 'GOL'
      })
    },
    def () {
      return this.squad.filter((el) => {
        return el.pos === 'DEF'
      })
    },
    mei () {
      return this.squad.filter((el) => {
        return el.pos === 'MEI'
      })
    },
    ata () {
      return this.squad.filter((el) => {
        return el.pos === 'ATA'
      })
    }
  }
}
</script>
<style lang="css" scoped>
</style>
