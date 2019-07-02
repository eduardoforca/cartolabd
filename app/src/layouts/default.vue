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
  methods: {
    logout () {
      this.$store.dispatch('user/logoutUser')
      this.$router.go('/')
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
</style>
