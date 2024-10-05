<script setup>
defineProps(['loaders']);
const emits = defineEmits(['refresh', 'activateRow'])

const activateRow = (loader) => emits('activateRow', loader.id)
</script>
<template>
  <div class="table-container ">
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
</style>
