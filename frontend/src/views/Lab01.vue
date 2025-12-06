<template>
  <h2>实验 1：命题逻辑真值表</h2>

  变量：
  <input v-model="vars" placeholder="P,Q,R">

  表达式：
  <input ref="exprInput" v-model="expr" placeholder="输入逻辑式">
  <!-- 自制符号键盘 -->
  <div class="key-row">
    <button v-for="s in symbols" :key="s" @click="insertSymbol(s)">{{ s }}</button>
  </div>

  <button @click="calc">生成真值表</button>

  <!-- 结果区域 -->
  <table v-if="table.length" border="1">
    <thead>
      <tr><th v-for="k in Object.keys(table[0])" :key="k">{{ k }}</th></tr>
    </thead>
    <tbody>
      <tr v-for="(row,idx) in table" :key="idx">
        <td v-for="v in Object.values(row)" :key="v">{{ typeof v==='boolean'?(v?1:0):v }}</td>
      </tr>
    </tbody>
  </table>

  <p>主析取范式：{{ pdnf }}</p>
  <p>主合取范式：{{ pcnf }}</p>
</template>

<script setup>
import { ref } from 'vue'
import { getTruthTable } from '@/api/lab01.js'
import { ElMessage } from 'element-plus'   // 局部也可



const vars  = ref('P,Q')
const expr  = ref('')
const table = ref([])
const pdnf  = ref('')
const pcnf  = ref('')

// 逻辑符号键盘
const symbols = ['¬', '∧', '∨', '⊕', '→', '↔', '(', ')']

// 点击插入符号
function insertSymbol(s) {
  const inp = exprInput.value
  const start = inp.selectionStart
  const end   = inp.selectionEnd
  expr.value = expr.value.slice(0, start) + s + expr.value.slice(end)
  inp.focus()
  inp.setSelectionRange(start + s.length, start + s.length)
}

const exprInput = ref(null)

// 核心：符号 → Python 运算符 + 保险空格 + 强制括号
function toPy(exprStr) {
  let s = exprStr
    .replace(/¬/g, ' not ')
    .replace(/∧/g, ' and ')
    .replace(/∨/g, ' or ')
    .replace(/⊕/g, ' != ')
    .replace(/→/g, ' <= ')
    .replace(/↔/g, ' == ')

  s = s.replace(/\s+/g, ' ').trim() // 压空格

  // 给 <= 和 == 两边强制加括号，防止链式比较
  s = s.replace(/(.+?)\s*<=\s*(.+)/g, '($1) <= ($2)')
  s = s.replace(/(.+?)\s*==\s*(.+)/g, '($1) == ($2)')

  return s
}

async function calc() {
  try {
    const engExpr = toPy(expr.value)
    const res = await getTruthTable({
      vars: vars.value.split(',').map(s => s.trim()),
      expr: engExpr
    })
    table.value = res.data.table
    pdnf.value  = res.data.pdnf
    pcnf.value  = res.data.pcnf
  } catch (err) {
    // 取后端返回的 detail 或默认提示
    const msg = err.response?.data?.detail || err.message || '表达式语法错误'
    ElMessage({ message: msg, type: 'error', duration: 4000 })
  }
}
</script>

<style scoped>
.key-row{margin-top:6px}
.key-row button{font-size:18px;margin:2px;padding:4px 10px;min-width:36px;background:#f5f7fa;border:1px solid #dcdfe6;border-radius:4px;cursor:pointer}
.key-row button:hover{background:#409eff;color:#fff}
</style>