<template>
  <q-layout view="lHh Lpr lFf">
    <q-page-container>
      <div class="row" style="height: 100vh">
        <div class="bg-primary col-md-6 col-12">
          <div class="row items-center" style="width: 100%; height: 100%">
            <div class="row justify-center full-width">
              <div class="col-md-12 col-6 row justify-center items-center">
                <div>
                  <img alt="FUT FANTASY" src="assets/logo_ff@2x.png" style="width: 20vw; max-width: 300px">
                </div>
              </div>
              <div class="col-12" v-if="$q.screen.gt.sm">
                <p class="q-pa-lg text-white text-justify" style="font-size: 22px">
                  Monte seu time, comprando e vendendo os jogadores do Brasileirão. Entre em ligas personalizadas e se consagre campeão. A vitória te aguarda!
                </p>
              </div>
            </div>
          </div>
        </div>
        <router-view class="col-md-6 col-12"/>
      </div>
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  data () {
    return {
    }
  },
  methods: {
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
