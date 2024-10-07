<script setup lang="ts">
defineProps({
  isUnderEdition: {
    default: false
  }
})
defineEmits(['edit', 'save', 'cancel'])
</script>

<template>
  <div class="edit_container">
          <button>
            <UIcon name="rivet-icons:pencil-solid" class="text-gray-500 w-5 h-5"
                   v-if="(!$props.isUnderEdition)" @click="$emit('edit')" />
            <UIcon name="rivet-icons:check" class="text-gray-500 w-5 h-5"
                   v-else @click="$emit('save')"/>
          </button>
          <button @click="$emit('cancel')">
            <UIcon name="rivet-icons:close" class="text-gray-500 w-5 h-5"/>
          </button>
        </div>
</template>

<style scoped>
.edit_container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  gap: 5px;
}

</style>