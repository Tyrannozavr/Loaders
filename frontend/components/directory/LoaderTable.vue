<template>
  <table>
    <thead>
      <tr>
        <th>Марка</th>
        <th>Номер</th>
        <th>Грузоподъемность</th>
        <th>Активен</th>
        <th>Действия</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="loader in loaders" :key="loader.id">
        <td>{{ loader.brand }}</td>
        <td>{{ loader.number }}</td>
        <td>{{ loader.capacity }}</td>
        <td>
          <UIcon
              name="mi:check"
              v-if="loader.active"
              class="text-green-700"
            />
          <UIcon
            name="mi:close"
            class="text-red-700"
            v-else
            />
        </td>
        <td>
          <button @click="$emit('edit', loader)">Изменить</button>
          <button @click="$emit('delete', loader)">Удалить</button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup>
defineProps(['loaders']);
</script>
