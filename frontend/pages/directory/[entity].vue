<script setup lang="ts">
const route = useRoute()
const entity = route.params.entity
const directory = ref({
  name: ""
})
if (entity == 'loaders') {
  directory.value.name = 'Погрузчиков'
}
const Loaders = [
  {
    id: "1", brand: "Амкадор", number: "45-65 PH-1", capacity: "2.5", active: true,
  },
  {
    id: "2", brand: "Амкадор", number: "45-66 PH-1", capacity: "2.6", active: false,
  },

]
</script>

<template>
  <h1 class="font-bold text-2xl">Справочник {{directory.name}}</h1>
  <DirectorySearch />
  <DirectoryLoaderTable :loaders="Loaders" />
</template>

<style scoped>
h1 {
  margin-bottom: 10px;
}
</style>