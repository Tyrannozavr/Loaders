<script setup lang="ts">
const props = defineProps(['loaderId'])
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
const isModalActive = ref(false)
const addRow = () => {
  isModalActive.value = true
}
const incidentData = ref({
  number: loader.number,
  dateStart: new Date(),
  dateEnd: null,
  description: '',
})
const saveData = () => {
  console.log('process', incidentData.value)
  isModalActive.value = false
}
</script>

<template>
  <slot v-if="loaderId">
    <div class="incident_containe">
      <h3 class="incident_header font-bold">Простои по погрузчику {{ loader.number }}</h3>
      <UButton
          class="add_button bg-red-700 w-32 rounded-xl flex items-center justify-center mb-4"
          size="md"
          @click="addRow"
      >Добавить
      </UButton>
      <DirectoryIncidentModal v-model="incidentData" :is-active="isModalActive"
                              @close="isModalActive = false" @save="saveData" />
      <DirectoryIncidentTable :incidents="loader.incidentList"/>

    </div>
  </slot>
  <slot v-else></slot>
</template>

<style scoped>
.incident_header {
  margin-bottom: 5px;
}

textarea {
  overflow: auto;
  resize: none;
}
</style>