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
                            @close="isModalActive = false" @save="saveData"/>
<!--    <UButton label="Show toast" @click="toast.add({ title: 'With actions', actions })"/>-->
  </div>
</template>

<script setup>
const props = defineProps(['loader']);
const toast = useToast()
const incidentData = ref()
const isModalActive = ref(false)
const actions = ref([{
  label: 'Удалить',
  click: () => alert('Delete!'+rowToDelete.value)
}, {
  label: 'Отмена',
}])

const deleteRow = (rowId) => {
  // console.log('delete row', rowId)
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
  // console.log('save', incidentData.value);

  // Find the index of the incident in the incidentList that matches incidentData.number
  const index = props.loader.incidentList.findIndex(incident => incident.id === incidentData.value.id);

  // If found, update the incident
  if (index !== -1) {
    props.loader.incidentList[index] = incidentData.value;
    // props.loader.incidentList[index] = { ...props.loader.incidentList[index], ...incidentData.value };
  } else {
    // Optionally handle case where incident is not found
    console.warn('Incident not found');
  }

  // Close the modal
  isModalActive.value = false;
};


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