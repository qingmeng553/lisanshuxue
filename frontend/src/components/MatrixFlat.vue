<template>
  <div class="grid" :style="{gridTemplateColumns:`repeat(${m.length},1fr)`}">
    <div v-for="v in flat" :key="idx" class="cell" :class="{one:v===1}">{{ v }}</div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
const props = defineProps({ m:Array })
const flat = computed(()=>props.m.flat())
</script>

<style scoped>
.grid{display:grid;gap:2px;width:fit-content}
.cell{width:24px;height:24px;border:1px solid #ddd;display:flex;align-items:center;justify-content:center;font-size:12px;background:#fff}
.cell.one{background:#409eff;color:#fff}
</style>