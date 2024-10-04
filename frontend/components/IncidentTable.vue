<template>
  <div>
    <h3>Простои по погрузчику</h3>
    <table>
      <thead>
        <tr>
          <th>Дата начала</th>
          <th>Дата окончания</th>
          <th>Описание</th>
          <th>Действия</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="incident in incidents" :key="incident.id">
          <td>{{ incident.startDate }}</td>
          <td>{{ incident.endDate }}</td>
          <td>{{ incident.description }}</td>
          <td>
            <button @click="$emit('edit', incident)">Изменить</button>
            <button @click="$emit('delete', incident)">Удалить</button>
          </td>
        </tr>
      </tbody>
    </table>
    <button @click="$emit('add')">Добавить инцидент</button>
  </div>
</template>

<script setup>
defineProps(['incidents']);
</script>
