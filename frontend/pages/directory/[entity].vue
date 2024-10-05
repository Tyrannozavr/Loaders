<script setup lang="ts">
const route = useRoute()
const entity = route.params.entity
const directory = ref({
  name: ""
})
if (entity == 'loaders') {
  directory.value.name = 'Погрузчиков'
}

</script>

<template>
  <h1 class="font-bold text-2xl">Справочник {{directory.name}}</h1>
  <DirectorySearch />
</template>

<style scoped>
.h1 {
  margin-bottom: 15px;
}
</style>