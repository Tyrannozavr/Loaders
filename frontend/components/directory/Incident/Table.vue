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
                                 :loader-number="loader.number"
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

<script setup>
const props = defineProps(['loader']);
const toast = useToast()
const incidentData = ref()
const isModalActive = ref(false)
const actions = ref([{
  label: 'Удалить',
  click: () => alert('Delete!' + rowToDelete.value)
}, {
  label: 'Отмена',
}])
const deleteRow = (rowId) => {
  rowToDelete.value = rowId
  toast.add({title: "Удалить информацию о простое? Вы уверены?", actions})
}
const rowToDelete = ref()
const editRow = (data) => {
  // console.log('edit row', data)
  incidentData.value = data
  isModalActive.value = true
}
const saveData = () => {
  console.log('save', incidentData.value);
};
const closeModal = () => {
  console.log('close modal')
  isModalActive.value = false
}

</script>
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