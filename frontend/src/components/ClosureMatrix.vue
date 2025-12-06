<template>
  <div class="closure">
    <div class="title">{{ title }}</div>
    <div class="grid" :style="{gridTemplateColumns:`repeat(${m.length},1fr)`}">
      <div v-for="v in flat" :key="idx" class="cell" :class="{one:v===1}">{{ v }}</div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
const props = defineProps({ title:String, m:Array })
const flat = computed(()=>props.m.flat())
</script>

<style scoped>
.closure{margin-top:12px}
.title{font-weight:bold;margin-bottom:4px}
.grid{display:grid;gap:2px;width:fit-content}
.cell{width:28px;height:28px;border:1px solid #ddd;display:flex;align-items:center;justify-content:center;font-size:14px;background:#fff}
.cell.one{background:#67c23a;color:#fff}
</style>