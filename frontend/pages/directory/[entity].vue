<script setup lang="ts">
const route = useRoute()
const entity = route.params.entity
const directory = ref({
  name: ""
})
if (entity == 'loaders') {
  directory.value.name = 'Погрузчиков'
}
const Loaders = ref([
  {
    id: "1", brand: "Амкадор", number: "45-65_PH-1", capacity: "2.5", isActive: true,
    datetime: Date.now(), user: "Иванов И.И."
  },
  {
    id: "2", brand: "Амкадор", number: "45-65 PH-1", capacity: "2.5", isActive: false,
    datetime: Date.now(), user: "Иванов И.И."
  },

])
const refresh = () => Loaders.value = [
  {
    id: "1", brand: "Амкадор", number: "45-65_PH-1", capacity: "2.5", isActive: true,
    datetime: Date.now(), user: "Иванов И.И."
  },
  {
    id: "2", brand: "Амкадор", number: "45-65 PH-1", capacity: "2.5", isActive: false,
    datetime: Date.now(), user: "Иванов И.И."
  },
]
const activeRowId = ref()
const activateRow = (rowId) => activeRowId.value = rowId
</script>

<template>
  <h1 class="font-bold text-2xl">Справочник {{directory.name}}</h1>
  <DirectorySearch />
  <DirectoryLoaderTable
      :loaders="Loaders"
      @refresh="refresh"
      @activateRow="activateRow"
  />
<!--  <DirectoryIncidentTable />-->
  incident talbe ablut {{activeRowId}}
</template>

<style scoped>
h1 {
  margin-bottom: 10px;
}
</style>