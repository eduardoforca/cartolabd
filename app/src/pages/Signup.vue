<template>
  <div class="q-pa-lg row items-center justify-center">
    <q-card class="col-12" style="max-width: 560px">
      <q-card-section class="bg-secondary card-title text-uppercase text-white">Cadastro</q-card-section>
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
          <q-input v-model="birthdate" mask="##/##/####" label="Data de Nascimento">
            <template v-slot:append>
              <q-icon name="event" class="cursor-pointer">
                <q-popup-proxy ref="qDateProxy" transition-show="scale" transition-hide="scale">
                  <q-date mask="DD/MM/YYYY" minimal v-model="birthdate" @input="() => $refs.qDateProxy.hide()" />
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>
        </q-form>
        </div>
      </q-card-section>
      <q-card-actions vertical align="center">
        <q-btn color="secondary">Cadastrar</q-btn>
        <q-btn outline color="primary" size="12px" to="login">Já sou cadastrado</q-btn>
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
    birthdate: ''
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
