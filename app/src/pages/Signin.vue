<template>
  <div class="q-pa-lg row items-center justify-center">
    <q-card class="col-12" style="max-width: 560px">
      <q-card-section class="bg-secondary card-title text-uppercase text-white">Login</q-card-section>
      <q-card-section>
        <div class="q-px-md q-pt-md">
          <q-form>
            <q-input
            v-model="email"
            label="Email"
            lazy-rules
            :rules="[ (val) => val && val.length > 0 || 'Insira um email válido']"
            />
            <q-input
            v-model="password"
            label="Senha"
            lazy-rules
            :type="!showPwd ? 'password' : 'text'"
            :rules="[ (val) => val && val.length > 6 || 'Insira uma senha válida']"
            >
            <template v-slot:append>
              <q-icon
              :name="showPwd ? 'visibility_off' : 'visibility'"
              class="cursor-pointer"
              @click="showPwd = !showPwd"
              />
            </template>
          </q-input>
          <q-checkbox v-model="saveCreds" label="Continuar conectado" />
        </q-form>
        </div>
      </q-card-section>
      <q-card-actions vertical align="center">
        <q-btn color="secondary" to="home">Entrar</q-btn>
        <q-btn outline color="primary" size="12px" to="sign">Não sou cadastrado</q-btn>
      </q-card-actions>
    </q-card>
  </div>
</template>
<script>
export default {
  data: () => ({
    email: '',
    password: '',
    showPwd: false,
    saveCreds: true
  })
}
</script>
<style lang="css" scoped>
.card-title {
  font-size: 16px;
  letter-spacing: 1.7px;
  font-weight: 300;
}
</style>
