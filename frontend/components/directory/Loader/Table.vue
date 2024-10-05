<script setup>
const props = defineProps(['loaders']);
defineEmits(['refresh'])
const addRow = () => {
  props.loaders.push({creation: true})
}
const activeRow = ref({})
const activateRow = (row) => activeRow.value = row
</script>
<template>
  <UButton
      class="add_button bg-red-700 w-32 rounded-xl flex items-center justify-center"
      size="md"
      color="primary"
      @click="addRow"
  >Добавить</UButton>
  <div class="table-container w-3/5">
    <table class="bg-white">
      <thead>
      <tr>
        <th>Код записи</th>
        <th>Марка</th>
        <th>Номер</th>
        <th>Грузоподъем
          -ность
        </th>
        <th>Активен</th>
        <th>Дата и время изменения</th>
        <th>Пользователь</th>
        <th>Действия</th>
      </tr>
      </thead>
      <tbody>
        <DirectoryLoaderTableRow
            v-for="loader in loaders"
            :loader="loader"
            @refresh="$emit('refresh')"
            class="loader_row"
            @click="activateRow(loader)"
        />
      </tbody>
    </table>
  </div>
  active row is {{activeRow}}
</template>

<style scoped>
.loader_row {
  cursor: pointer;
  &:hover {
    border: 2px solid red;
  }
}

.table-container {
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

tr {
  height: 10px;
}

.add_button {
  margin-bottom: 15px;
}
</style>
