<script setup>
const items = [
  {
    link: '/users', name: 'Пользователи',
  },
  {
    link: '/notifications', name: 'Уведомления и напоминания',
  },
  {
    link: '/settings', name: 'Настройки АИС ОГПА',
  },
  {
    link: '/directory/loaders', name: 'Справочник погрузчиков',
  },
  {
    link: '/recovery', name: 'Резервное копирование и восстановление',
  },
  {
    link: '/directory', name: 'Справочники',
  },

]
</script>
<template>
  <aside class="sidebar">
    <ul>
      <li v-for="item in items">
      <NuxtLink  :to="item.link">{{item.name}}</NuxtLink>
      </li>
    </ul>
  </aside>
</template>

<style scoped>
.sidebar {
  border-radius: 10px; /* Закругленные края */
  padding: 20px;
  width: 200px; /* Ширина сайдбара */
  margin-right: 10px;
}

.sidebar ul {
  list-style-type: none; /* Убираем маркеры */
  padding: 0;
}

.sidebar li {
  margin-bottom: 15px; /* Отступы между элементами */
  color: black;
}
.item_active {
  color: red;
}
</style>
