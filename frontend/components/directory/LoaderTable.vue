<script setup>
defineProps(['loaders']);
const formatDate = (datetime) => {
  const date = new Date(datetime);
  const day = String(date.getDate()).padStart(2, '0');
  const month = String(date.getMonth() + 1).padStart(2, '0'); // Months are zero-based
  const year = date.getFullYear();
  const hours = String(date.getHours()).padStart(2, '0');
  const minutes = String(date.getMinutes()).padStart(2, '0');

  return `${day}.${month}.${year} ${hours}:${minutes}`;
}
</script>
<template>
  <UButton
      class="add_button bg-red-700 w-32 rounded-xl flex items-center justify-center"
      size="md"
      color="primary"
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
      <tr style="height:10px" v-for="loader in loaders" :key="loader.id">
        <td>{{ loader.id }}</td>
        <td>{{ loader.brand }}</td>
        <td class="w-5">{{ loader.number }}</td> <!-- Изменено на w-5 -->
        <td>{{ loader.capacity }}</td>
        <td>
          <div class="is_active rounded-xl">
            <UIcon name="mi:check" v-if="loader.isActive" class=" text-green-700"/>
            <UIcon name="mi:close" class=" text-red-700" v-else/>
          </div>
        </td>
        <td>{{ formatDate(loader.datetime) }}</td>
        <td>{{ loader.user }}</td>
        <td class="edit_cell">
          <div class="edit_container">
            <button @click="$emit('edit', loader)">
              <UIcon name="rivet-icons:pencil-solid" class="text-gray-500 w-5 h-5"/>
            </button>
            <button @click="$emit('delete', loader)">
              <UIcon name="rivet-icons:close" class="text-gray-500 w-5 h-5"/>
            </button>
          </div>

        </td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
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

.is_active {
  border-width: 1px; /* Ensure border width is 1px */
  width: 80%;
  height: 100%;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
  vertical-align: middle;
}

.edit_container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  gap: 5px;
}

</style>
