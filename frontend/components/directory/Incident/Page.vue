<script setup lang="ts">
defineProps(['loaderId'])
const loader = ref({
  number: 1,
  incidentList: [
    {
      id: 1,
      startDate: new Date(),
      endDate: new Date(),
      description: 'description'
    },
    {
      id: 2,
      startDate: new Date(2010, 0, 1, 0, 0, 0, 0),
      endDate: new Date,
      description: 'description'
    },

  ]
})
const addRow = () => {
  console.log('add')
}
</script>

<template>
  <slot v-if="loaderId">
    <div class="incident_container w-2/5">
      <h3 class="incident_header font-bold">Простои по погрузчику {{ loader.number }}</h3>
      <UButton
          class="add_button bg-red-700 w-32 rounded-xl flex items-center justify-center"
          size="md"
          color="primary"
          @click="addRow"
      >Добавить
      </UButton>
      <DirectoryIncidentTable :incidents="loader.incidentList"/>
    </div>
  </slot>
  <slot v-else></slot>
</template>

<style scoped>
.incident_header {
  margin-bottom: 5px;
}
</style>