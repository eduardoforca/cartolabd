<template>
  <q-layout view="lHh Lpr lFf">
    <q-page-container>
      <div class="row" style="height: 100vh">
        <div class="bg-primary col-md-6 col-12">
          <div class="row items-center" style="width: 100%; height: 100%">
            <div class="row justify-center">
              <div class="col-md-12 col-6 row justify-center items-center">
                <div>
                  <img alt="FUT FANTASY" src="assets/logo_ff@2x.png" style="width: 20vw; max-width: 300px">
                </div>
              </div>
              <div class="col-md-12 col-6">
                <p class="q-pa-lg text-white" style="font-size: 22px">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus non mattis nunc, quis bibendum arcu. Duis sit amet sodales libero. Fusce iaculis nulla at sodales finibus. Aliquam erat volutpat. Quisque rutrum sed turpis nec tincidunt.</p>
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
</style>
