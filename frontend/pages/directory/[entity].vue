<script setup lang="ts">
const route = useRoute()
const entity = route.params.entity
const directory = ref({
  name: ""
})
if (entity == 'loaders') {
  directory.value.name = 'Погрузчиков'
}
const Loaders = ref()
const $backend = Fetch()

const refresh = async () => {
  console.log('refresh entity')
  Loaders.value = await $backend.get('loaders/')
  Loaders.value.map((item) => {
    item.datetime = new Date(item.updated_at)
    item.user = item.updated_by
    item.isActive = item.is_active
  })
  activeRow.value = {id: null, number: null}
}
refresh()
const addRow = () => {
  Loaders.value.push({creation: true})
}
const activeRow = ref({
  id: null,
  number: null
})
const activateRow = (row) => {
  activeRow.value.id = row.id
  activeRow.value.number = row.number
}

</script>

<template>
  <h1 class="font-bold text-2xl">Справочник {{ directory.name }}</h1>
  <DirectorySearch/>
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
    <DirectoryIncidentPage :loader-id="activeRow.id" :loader-number="activeRow.number"
                           class="w-2/5" @refresh="refresh"/>
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