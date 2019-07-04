<template>
  <q-card>
    <q-card-section class="bg-secondary card-title text-uppercase text-white">Modificar Time</q-card-section>
    <q-card-section>
      <div class="q-px-md q-pt-md">
        <q-form ref="myForm">
          <q-input
          v-model="nome"
          label="Nome"
          lazy-rules
          :rules="[ (val) => val && val.length > 0 || 'Insira um nome válido']"
          />
          <span class="card-title">
            Cores
          </span>
          <q-separator/>
          <div class="row justify-around">
            <div class="row items-center">
              <span class="card-title">Cor 1</span>
              <q-icon :style="`color: ${color1}; border: white solid 4px; background: black`" name="stop" size="30px" class="cursor-pointer">
                <q-popup-proxy transition-show="scale" transition-hide="scale">
                  <q-color format-model="hex" v-model="color1" />
                </q-popup-proxy>
              </q-icon>
            </div>
            <div class="row items-center">
              <span class="card-title">Cor 2</span>
              <q-icon :style="`color: ${color2}; border: white solid 4px; background: black`" name="stop" size="30px" class="cursor-pointer">
                <q-popup-proxy transition-show="scale" transition-hide="scale">
                  <q-color format-model="hex" v-model="color2" />
                </q-popup-proxy>
              </q-icon>
            </div>
            <div class="row items-center">
              <span class="card-title">Cor 3</span>
              <q-icon :style="`color: ${color3}; border: white solid 4px; background: black`" name="stop" size="30px" class="cursor-pointer">
                <q-popup-proxy transition-show="scale" transition-hide="scale">
                  <q-color format-model="hex" v-model="color3" />
                </q-popup-proxy>
              </q-icon>
            </div>
          </div>
          <q-separator/>
      </q-form>
      </div>
    </q-card-section>
    <q-card-section>
      <div class="q-px-md q-pt-md">
        <p class="card-title">
          Brasão
        </p>
        <div class="row items-center justify-around">
          <div :class="`cursor-pointer text-center ${selectedCrest === 1 ? 'selected-crest' : ''}`" style="width: 240px" @click="selectedCrest = 1">
            <svg class="icon-color" height="215px" viewBox="0 0 175 320"><use xlink:href="assets/Crest1.svg#crest1"></use></svg>
          </div>
          <div :class="`cursor-pointer text-center ${selectedCrest === 2 ? 'selected-crest' : ''}`" style="width: 240px" @click="selectedCrest = 2">
            <svg class="icon-color" height="215px" viewBox="-27 -25 275 275"><use xlink:href="assets/Crest2.svg#crest2"></use></svg>
          </div>
          <div :class="`cursor-pointer text-center ${selectedCrest === 3 ? 'selected-crest' : ''}`" style="width: 240px" @click="selectedCrest = 3">
            <svg class="icon-color" height="215px" viewBox="-20 -30 250 300"><use xlink:href="assets/Crest3.svg#crest3"></use></svg>
          </div>
        </div>
      </div>
    </q-card-section>
    <q-card-actions vertical align="center">
      <q-btn color="secondary" @click="save">Salvar</q-btn>
    </q-card-actions>
  </q-card>
</template>
<script>
export default {
  props: {
    initialValue: {
      type: Object,
      default () {
        return {
          nome: '',
          color1: '#6c00d6',
          color2: '#ffffff',
          color3: '#000000',
          crest: 1
        }
      }
    }
  },
  data: () => ({
    nome: '',
    color1: '#6c00d6',
    color2: '#ffffff',
    color3: '#000000',
    selectedCrest: 1
  }),
  mounted () {
    this.nome = this.initialValue.nome
    this.color1 = this.initialValue.color1
    this.color2 = this.initialValue.color2
    this.color3 = this.initialValue.color3
    this.selectedCrest = this.initialValue.crest
    this.$el.style.setProperty('--color-1', this.color1)
    this.$el.style.setProperty('--color-2', this.color2)
    this.$el.style.setProperty('--color-3', this.color3)
  },
  watch: {
    color1 () {
      this.$el.style.setProperty('--color-1', this.color1)
    },
    color2 () {
      this.$el.style.setProperty('--color-2', this.color2)
    },
    color3 () {
      this.$el.style.setProperty('--color-3', this.color3)
    }
  },
  computed: {
    aTeam () {
      return {
        // crest: this.selectedCrest,
        nome: this.nome,
        color1: this.color1,
        color2: this.color2,
        color3: this.color3
      }
    }
  },
  methods: {
    save () {
      this.$refs.myForm.validate().then(
        success => {
          if (success) {
            this.$emit('save', this.aTeam)
          }
        }
      )
    }
  }
}
</script>
<style lang="css" scoped>
.selected-crest {
  border-color: var(--q-color-secondary);
  border-width: 10px;
  border-style: solid;
}
.icon-color {
  --crest-color-1: var(--color-1);
  --crest-color-2: var(--color-2);
  --crest-color-3: var(--color-3);
}
</style>
