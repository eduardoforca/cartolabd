<template>
  <div class="q-pa-lg row items-center justify-center">
    <q-card class="col-12" style="max-width: 560px">
      <q-card-section class="bg-secondary card-title text-uppercase text-white">Meu Perfil</q-card-section>
      <q-card-section class="text-uppercase text-white">
        <div class="row justify-center q-pt-md">
          <div class="user-avatar">
            <img :src="picture ? picture.__img.src : ''"/>
          </div>
        </div>
        <div class="row justify-center q-pt-md">
          <q-btn color="primary" @click="uploader = true">Alterar Foto</q-btn>
        </div>
      </q-card-section>
      <q-card-section>
        <div class="q-px-md q-pt-md">
          <q-form ref="myForm">
            <q-input
            v-model="email"
            label="Email"
            lazy-rules
            :rules="[ (val) => val && val.length > 0 || 'Insira um email válido']"
            />
            <q-input
            v-model="name"
            label="Nome"
            lazy-rules
            :rules="[ (val) => val && val.length > 0 || 'Insira um nome válido']"
            />
            <q-input
            v-model="password"
            label="Senha"
            lazy-rules
            :type="!showPwd ? 'password' : 'text'"
            :rules="[ (val) => (!val) || (val && val.length > 6) || 'Insira uma senha válida']"
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
        <q-btn color="secondary" @click="saveChanges">Salvar</q-btn>
      </q-card-actions>
      <q-inner-loading :showing="loading">
        <q-spinner size="50px" color="primary" />
      </q-inner-loading>
    </q-card>
    <q-dialog v-model="uploader">
      <q-uploader
        @added="chooseFile"
        @start="uploader = false"
        style="max-width: 300px"
      />
    </q-dialog>
  </div>
</template>
<script>
import moment from 'moment'
export default {
  data: () => ({
    uploader: false,
    name: '',
    email: '',
    birthdate: '',
    password: '',
    showPwd: false,
    picture: null,
    loading: false
  }),
  mounted () {
    this.name = this.$store.state.user.user.name
    this.email = this.$store.state.user.user.email
    this.birthdate = moment(this.$store.state.user.user.birthdate, 'YYYY-MM-DD').format('DD/MM/YYYY')
    this.picture = {
      __img: {
        src: this.$store.state.user.user.foto
      }
    }
  },
  methods: {
    chooseFile (files) {
      this.picture = files[0]
      this.uploader = false
    },
    saveChanges () {
      this.$refs.myForm.validate().then(async (success) => {
        if (success) {
          this.loading = true
          let form = new FormData()
          form.append('name', this.name)
          form.append('email', this.email)
          if (this.password) {
            form.append('new_password', this.password)
          }
          if (this.birthdate) {
            form.append('birthdate', moment(this.birthdate, 'DD/MM/YYYY').format('YYYY-MM-DD'))
          }
          if (this.picture && this.picture instanceof File) {
            form.append('foto', this.picture)
          }
          try {
            let response = await this.$api.put(
              `/usuarios/${this.$store.state.user.user.id}/`,
              form,
              {
                headers: {
                  'Content-Type': 'multipart/form-data'
                }
              })
            if (response.status === 200) {
              this.$store.dispatch('user/setUser', { user: response.data })
              this.loading = false
            } else {
              throw response.statusText
            }
          } catch (e) {
            this.loading = false
            console.log(e)
          }
        }
      })
    }
  }
}
</script>
<style lang="css" scoped>
.user-avatar{
  width: 120px;
  height: 120px;
}
.user-avatar img {
  border-radius: 100%;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
