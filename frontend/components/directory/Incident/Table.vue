<template>
  <div class="table_container">
    <table class="bg-white">
      <thead>
        <tr>
          <th>Дата начала</th>
          <th>Дата окончания</th>
          <th>Время простоя</th>
          <th>Описание</th>
          <th>Действия</th>
        </tr>
      </thead>
      <tbody>
        <DirectoryIncidentTableRow v-for="incident in $props.incidents" :incident="incident"/>
      </tbody>
    </table>
  </div>

</template>

<script setup>
defineProps(['incidents']);
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