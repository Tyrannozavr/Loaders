<script setup lang="ts">
const props = defineProps(['loaderId'])
const $backend = Fetch()
const Loader = ref({
  number: props.loaderId,
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
      number: props.loaderId,
      incidentList: data
    };
    // Loader.value.incidentList = Loader.value.incidentList.map((item) => {
    //   item.startDate = new Date(item.started_at)
    //   item.endDate = item.finished_at ? new Date(item.finished_at) : ''
    //   return item
    // })
    // console.log(1, typeof Loader.value.incidentList[0].endDate)
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}
if (!(props.loaderId == null)) {
  refreshLoader()
}
// const loader = ref({
//   number: 1,
//   incidentList: [
//     {
//       id: 1,
//       startDate: new Date(),
//       endDate: new Date(),
//       description: 'description'
//     },
//     {
//       id: 2,
//       startDate: new Date(2010, 0, 1, 0, 0, 0, 0),
//       endDate: new Date,
//       description: 'description'
//     },
//
//   ]
// })
const isModalActive = ref(false)
const addRow = () => {
  isModalActive.value = true
}
const incidentData = ref({
  number: Loader.number,
  dateStart: new Date(),
  dateEnd: null,
  description: '',
})
const saveData = () => {
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
<!--{{2+ ' '+ typeof Loader.incidentList[0].startDate}}-->
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