<script setup lang="ts">
const route = useRoute()
const entity = route.params.entity
const directory = ref({
  name: ""
})
if (entity == 'loaders') {
  directory.value.name = 'Погрузчиков'
}
const $backend = Fetch()
const Loaders = await $backend.get('loaders/')
Loaders.map((item) => {
  item.datetime = new Date(item.updated_at)
  item.user = item.updated_by
  item.isActive = item.is_active
})
// Loaders.forEach((item) => console.log('a', item))
    // .then((res) => res)
// console.log('new is', newLoaders)
// const Loaders = ref([
//   {
//     id: "1", brand: "Амкадор", number: "45-65_PH-1", capacity: "2.5", isActive: true,
//     datetime: Date.now(), user: "Иванов И.И."
//   },
// ])
console.log('loaders', Loaders)
const refresh = () => Loaders.value = [
  {
    id: "1", brand: "Амкадор", number: "45-65_PH-1", capacity: "2.5", isActive: true,
    datetime: Date.now(), user: "Иванов И.И."
  },
  {
    id: "2", brand: "Амкадор", number: "45-65 PH-1", capacity: "2.5", isActive: false,
    datetime: Date.now(), user: "Иванов И.И."
  },
  //     {
  //   "id": 6,
  //   "number": "аккп",
  //   "capacity": "1.000",
  //   "is_active": true,
  //   "updated_at": "2024-10-06T20:18:22.049121Z",
  //   "brand": 6,
  //   "updated_by": 1
  // }
]
const addRow = () => {
  Loaders.value.push({creation: true})
}
const activeRowId = ref()
const activateRow = (rowId) => activeRowId.value = rowId

</script>

<template>
  <h1 class="font-bold text-2xl">Справочник {{directory.name}}</h1>
  <DirectorySearch />
  <UButton
      class="add_button bg-red-700 w-32 rounded-xl flex items-center justify-center"
      size="md"
      color="primary"
      @click="addRow"
  >Добавить
  </UButton>
  <div class="table_container">
    <DirectoryLoaderTable
        :loaders="Loaders"
        @refresh="refresh"
        @activateRow="activateRow"
        class="w-3/5"
    />
    <DirectoryIncidentPage :loader-id="activeRowId" class="w-2/5"/>
  </div>

</template>

<style scoped>
h1 {
  margin-bottom: 10px;
}
.table_container {
  display: flex;
  flex-direction: row;
  gap: 10px;
}
.add_button {
  margin-bottom: 15px;
}
</style>