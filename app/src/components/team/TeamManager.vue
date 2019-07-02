<template>
  <div>
    <div v-if="!$store.state.user.team">
      Você ainda não tem um time
      <q-btn to="new">Criar Time</q-btn>
    </div>
  </div>
</template>
<script>
export default {
  data: () => ({

  })
}
</script>
<style lang="css" scoped>
</style>
