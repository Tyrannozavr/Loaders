<template>
  <div class="table-container">
    <table
        class="bg-white"
    >
      <thead>
      <tr>
        <th>Код записи</th>
        <th>Марка</th>
        <th>Номер</th>
        <th>Грузоподъемность</th>
        <th>Активен</th>
        <th>Дата и время изменения</th>
        <th>Пользователь</th>
        <th>Действия</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="loader in loaders" :key="loader.id">
        <td>{{ loader.id }}</td>
        <td>{{ loader.brand }}</td>
        <td>{{ loader.number }}</td>
        <td>{{ loader.capacity }}</td>
        <td>
          <div
              class="is_active rounded-xl border-1 border-gray-200 w-12 h-6"
          >
            <UIcon
                name="mi:check"
                v-if="loader.isActive"
                class="text-green-700"
            />
            <UIcon
                name="mi:close"
                class="text-red-700"
                v-else
            />
          </div>
        </td>
        <td>{{ loader.datetime }}</td>
        <td>{{ loader.user }}</td>
        <td>
          <button @click="$emit('edit', loader)">Изменить</button>
          <button @click="$emit('delete', loader)">Удалить</button>
        </td>
      </tr>
      </tbody>
    </table>
  </div>

</template>

<script setup>
defineProps(['loaders']);
</script>
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
  padding: 8px; /* Add some padding for better spacing */
}
.is_active {
  border-width: 1px; /* Ensure border width is 1px */
  width: 90%;
  height: 100%;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
  vertical-align: middle;
  & span {
    margin: auto;
  }
}
</style>
