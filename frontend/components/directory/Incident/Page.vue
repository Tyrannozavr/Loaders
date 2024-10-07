<script setup lang="ts">
const props = defineProps(['loaderId', 'loaderNumber'])
const $backend = Fetch()
const Loader = ref({
  id: props.loaderId,
  incidentList: []
})
watch(
    () => props.loaderId,
    (newVal, oldVal) => {
      // console.log('loaderId changed from', oldVal, 'to', newVal)
      // You can add your logic here
      if (!(newVal == undefined)) {
        refreshLoader()
      }
    }
)

const refreshLoader = async () => {
  try {
    const response = await $backend.$get(`loaders/incidents?loaderId=${props.loaderId}`);
    let data = await response.json();
    data = data.map((item) => {
      item.startDate = new Date(item.started_at)
      item.endDate = item.finished_at ? new Date(item.finished_at) : ''
      return item
    })
    Loader.value = {
      id: props.loaderId,
      incidentList: data
    };
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}
if (!(props.loaderId == null)) {
  refreshLoader()
}
// const incidentData = ref({
//   number: props.loaderId,
//   id: '',
//   dateStart: '',
//   dateEnd: '',
//   description: '',
// })

const isModalActive = ref(false)
const addRow = () => {
  // create new instance
  isModalActive.value = true
}
const incidentData = ref({
  loaderId: Loader.value.id,
  dateStart: new Date(),
  dateEnd: null,
  description: '',
})
const saveData = () => {
  // console.log('create', incidentData.value)
// dateEnd: null
// dateStart: Date Mon Oct 07 2024 12:33:16 GMT+0300 (Москва, стандартное время)
// description: "asdf"
// loaderId: 19
//   {
//   "started_at": "2024-10-07T06:41:22Z",
//   "finished_at": null,
//   "description": "helloworld",
//   "loader": 19
// }

  $backend.$post('loaders/incidents/', {
    body: {
      "started_at": incidentData.value.dateStart,
      "finished_at": incidentData.value.dateEnd,
      "description": incidentData.value.description,
      "loader": Loader.value.id
    }
  })
  isModalActive.value = false
}
</script>

<template>
  <slot v-if="loaderId">
    <div class="incident_containe">
      <h3 class="incident_header font-bold">Простои по погрузчику {{ Loader.number }}</h3>
      <UButton
          class="add_button bg-red-700 w-32 rounded-xl flex items-center justify-center mb-4"
          size="md"
          @click="addRow"
      >Добавить
      </UButton>
      <DirectoryIncidentModal v-model="incidentData" :is-active="isModalActive"
                              @close="isModalActive = false" @save="saveData"/>
      <DirectoryIncidentTable :loader="Loader"/>
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