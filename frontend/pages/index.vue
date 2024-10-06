<template>
  <div class="flex flex-col items-center justify-center min-h-screen">
    <h1 class="text-2xl font-bold mb-4">Welcome to My App</h1>
    <nuxt-link to="/register" class="btn mb-2">Register</nuxt-link>
    <nuxt-link to="/login" class="btn">Login</nuxt-link>
  </div>
</template>

<style>
.btn {
  @apply bg-blue-500 text-white p-2 rounded;
}
</style>
