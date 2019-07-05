<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          @click="leftDrawerOpen = !leftDrawerOpen"
          aria-label="Menu"
        >
          <q-icon name="menu" />
        </q-btn>

        <q-toolbar-title>
          {{$route.name}}
        </q-toolbar-title>

        <q-btn color="accent" @click="logout">Logout</q-btn>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      bordered
      content-class="bg-grey-2"
    >
      <q-list>
        <q-item class="bg-primary  q-pb-md">
          <q-item-section avatar>
            <div class="row justify-center q-pt-md">
              <div class="sidebar-avatar">
                <img :src="$store.state.user.user.foto ? $store.state.user.user.foto : ''"/>
              </div>
            </div>
          </q-item-section>
          <q-item-section class="card-title text-uppercase text-white">
            <q-item-label>{{$store.state.user.user.name}}</q-item-label>
            <q-item-label caption class="text-white text-lowercase">{{$store.state.user.user.email}}</q-item-label>
          </q-item-section>
        </q-item>
        <q-item clickable to="/home">
          <q-item-section avatar>
            <q-icon name="home" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Home</q-item-label>
          </q-item-section>
        </q-item>
        <q-item clickable to="/myteam">
          <q-item-section avatar>
            <q-icon name="fas fa-tshirt" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Equipe</q-item-label>
          </q-item-section>
        </q-item>
        <q-item clickable to="/leagues">
          <q-item-section avatar>
            <q-icon name="fas fa-trophy" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Ligas</q-item-label>
          </q-item-section>
        </q-item>
        <q-item clickable to="/matches">
          <q-item-section avatar>
            <q-icon name="fas fa-futbol" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Partidas</q-item-label>
          </q-item-section>
        </q-item>
        <q-item clickable to="/profile">
          <q-item-section avatar>
            <q-icon name="fas fa-user" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Perfil</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  data () {
    return {
      leftDrawerOpen: this.$q.platform.is.desktop
    }
  },
  async mounted () {
    let response = await this.$api.get('userClub/')
    let allTeams = response.data
    let myTeam = allTeams.find((el) => {
      return el.owner === this.$store.state.user.user.id
    })
    if (myTeam) {
      this.$store.commit('user/setTeam', { team: myTeam })
    }
  },
  methods: {
    logout () {
      this.$store.dispatch('user/logoutUser')
      this.$router.go('/')
    },
    loadAll () {
      let scope = this
      this.$api.get('player/').then(
        (response) => {
          scope.$store.commit('user/setPlayers', response.data)
        }
      )
    }
  }
}
</script>

<style>
.card-title {
  font-size: 16px;
  letter-spacing: 1.7px;
  font-weight: 300;
}
.sidebar-avatar{
  width: 80px;
  height: 80px;
}
.sidebar-avatar img {
  border-radius: 100%;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
