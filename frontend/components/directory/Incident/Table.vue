<script setup>
defineProps(['loader']);
const emits = defineEmits(['refresh'])
const toast = useToast()
const incidentData = ref()
const isModalActive = ref(false)
const $backend = Fetch()
const actions = ref([{
  label: 'Удалить',
  click: async () => {
    const response = await $backend.$delete(`loaders/incidents/${rowToDelete.value}/`)
    if (response.status === 204) {
      toast.add({title: 'Успешно удалено!'})
      emits('refresh')
    }
  }
}, {
  label: 'Отмена',
}])
const deleteRow = (rowId) => {
  rowToDelete.value = rowId
  toast.add({title: "Удалить информацию о простое? Вы уверены?", actions})
}
const rowToDelete = ref()
const editRow = (data) => {
  incidentData.value = data
  isModalActive.value = true
}
const saveData = async () => {
  // edit row
  const response = await $backend.$put(`loaders/incidents/${incidentData.value.id}/`, {
    body: {
      "started_at": incidentData.value.dateStart,
      "finished_at": incidentData.value.dateEnd !== '' ? incidentData.value.dateEnd : null,
      "description": incidentData.value.description
    }
  })
  let data = await response.json()
  if (data) {
    emits('refresh')
  }
  isModalActive.value = false
};
const closeModal = () => {
  isModalActive.value = false
}

</script>
<template>
  <div class="table_container">
    <table class="bg-white">
      <thead>
      <tr>
        <th>Код записи</th>
        <th>Дата начала</th>
        <th>Дата окончания</th>
        <th>Время простоя</th>
        <th>Описание</th>
        <th>Действия</th>
      </tr>
      </thead>
      <tbody>
      <DirectoryIncidentTableRow v-for="incident in $props.loader.incidentList"
                                 :incident="incident"
                                 :loader-id="loader.id"
                                 @edit="editRow"
                                 @delete="deleteRow"
      />
      </tbody>
    </table>
    <DirectoryIncidentModal v-model="incidentData" :is-active="isModalActive"
                            @close="closeModal"
                            @save="saveData"
    />
  </div>
</template>

<style scoped>
.table_container {
  max-height: 600px; /* Set a maximum height for the container */
  overflow-y: auto; /* Enable vertical scrolling */
}

table {
  border-collapse: collapse; /* Prevent double borders */
}

th, td {
  border-right: 1px solid #ccc; /* Right border for each cell */
  border-bottom: 1px solid #ccc;
  padding: 0 4px; /* Add some padding for better spacing */
  text-align: center;
}
</style>