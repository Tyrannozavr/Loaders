<template>
  <div class="modal">
    <h2>{{ incident.id ? 'Редактировать' : 'Добавить' }} Инцидент</h2>
    <input type="datetime-local" v-model="incident.startDate" required />
    <input type="datetime-local" v-model="incident.endDate" />
    <textarea v-model="incident.description" placeholder="Описание проблемы"></textarea>

    <button @click="save">Сохранить</button>
    <button @click="$emit('close')">Отмена</button>
  </div>
</template>

<script setup>
defineProps(['incident']);
const emit = defineEmits(['close', 'save']);

const save = () => {
  emit('save', incident);
};
</script>
