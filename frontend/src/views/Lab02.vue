<template>
  <h2>实验 4：关系矩阵性质与闭包</h2>
  <MatrixEditor v-model="matrix"/>

  <button class="calc-btn" :disabled="loading" @click="calc">
    {{ loading ? '计算中...' : '计算性质与闭包' }}
  </button>

  <!-- 结果区域 -->
  <div v-if="result" class="result-box">
    <h3>性质判定</h3>
    <ul>
      <li>自反：{{ result.props.reflexive ? '✅' : '❌' }}</li>
      <li>反自反：{{ result.props.irreflexive ? '✅' : '❌' }}</li>
      <li>对称：{{ result.props.symmetric ? '✅' : '❌' }}</li>
      <li>反对称：{{ result.props.antiSymmetric ? '✅' : '❌' }}</li>
      <li>传递：{{ result.props.transitive ? '✅' : '❌' }}</li>
    </ul>

    <h3>闭包矩阵</h3>
    <ClosureMatrix title="自反闭包 r(R)" :m="result.closures.reflexive"/>
    <ClosureMatrix title="对称闭包 s(R)" :m="result.closures.symmetric"/>
    <ClosureMatrix title="传递闭包 t(R)" :m="result.closures.transitive"/>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import MatrixEditor from '@/components/MatrixEditor.vue'
import ClosureMatrix from '@/components/ClosureMatrix.vue'
import lab02Api from '@/api/lab02.js'

const matrix = ref([])
const loading = ref(false)
const result = ref(null)

async function calc() {
  loading.value = true
  try {
    const res = await lab02Api.calculate(matrix.value)
    result.value = res.data
    // 简单成功提示
    alert('计算完成！')
  } catch (e) {
    alert('计算失败：' + (e.response?.data?.detail || e.message))
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.calc-btn{margin-top:12px;padding:8px 16px;border:1px solid #d9d9d9;border-radius:4px;background:#fff;cursor:pointer;transition:all .2s}
.calc-btn:hover{border-color:#409eff;color:#409eff;box-shadow:0 2px 4px rgba(0,0,0,.1)}
.calc-btn:disabled{opacity:.6;cursor:not-allowed}
.result-box{margin-top:12px;padding:12px;border:1px solid #dcdfe6;border-radius:4px;background:#fafafa}
.result-box h3{margin:8px 0}
.result-box ul{margin:0;padding-left:20px}
</style>