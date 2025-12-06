<template>
  <div class="editor">
    <div class="toolbar">
      阶数：
      <select v-model="order" @change="initMatrix" class="order-select">
        <option v-for="n in 8" :key="n" :value="n">{{ n }}</option>
      </select>
      <button class="btn" @click="fillAll(0)">全 0</button>
      <button class="btn" @click="fillAll(1)">全 1</button>
    </div>

    <div class="grid" :style="{gridTemplateColumns:`repeat(${order},1fr)`}">
      <div v-for="(v,idx) in flat" :key="idx" class="cell" :class="{one:v===1}" @click="toggle(idx)">{{ v }}</div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
const props = defineProps({ modelValue: Array })
const emit  = defineEmits(['update:modelValue'])

const order = ref(4)
const matrix = ref([])

watch(order, initMatrix, { immediate: true })

function initMatrix() {
  matrix.value = Array.from({ length: order.value }, () => Array(order.value).fill(0))
  emit('update:modelValue', matrix.value)
}

function fillAll(val) {
  matrix.value.forEach(r => r.fill(val))
  emit('update:modelValue', matrix.value)
}

function toggle(idx) {
  const i = Math.floor(idx / order.value), j = idx % order.value
  matrix.value[i][j] ^= 1
  emit('update:modelValue', matrix.value)
}

const flat = computed(() => matrix.value.flat())
</script>

<style scoped>
.editor{margin-top:8px}
.toolbar{display:flex;align-items:center;gap:8px;margin-bottom:8px}
.order-select{width:60px;padding:4px;border:1px solid #ccc;border-radius:4px}
.btn{padding:6px 12px;border:1px solid #d9d9d9;border-radius:4px;background:#fff;cursor:pointer;transition:all .2s}
.btn:hover{border-color:#409eff;color:#409eff;box-shadow:0 2px 4px rgba(0,0,0,.1)}
.grid{display:grid;gap:4px;width:fit-content}
.cell{width:36px;height:36px;border:1px solid #ccc;display:flex;align-items:center;justify-content:center;cursor:pointer;background:#fff;font-weight:bold;transition:all .2s}
.cell.one{background:#409eff;color:#fff;border-color:#409eff}
.cell:hover{border-color:#409eff;box-shadow:0 2px 4px rgba(64,158,255,.2)}
</style>