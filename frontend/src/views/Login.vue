
<template>
  <div class="page">
    <!-- 左侧大图 -->
    <div class="side-img"></div>

    <!-- 右侧表单 -->
    <div class="form-box">
      <h1>{{ isReg ? '注册新账号' : '离散数学实验展示' }}</h1>

      <div class="field">
        <label>用户名</label>
        <input v-model="form.username" placeholder="请输入用户名">
      </div>

      <div class="field">
  <label>密码</label>
  <div class="pwd-box">
    <input
      :type="showPwd ? 'text' : 'password'"
      v-model="form.password"
      placeholder="请输入密码"
      @keyup.enter="submit"
    />
    <span class="eye" @click="showPwd = !showPwd">
      {{ showPwd ? '🙈' : '🙉' }}
    </span>
  </div>
</div>

      <button class="big-btn" @click="submit">{{ isReg ? '注册并登录' : '立即登录' }}</button>

      <div class="tip" @click="isReg = !isReg">
        {{ isReg ? '已有账号？去登录' : '没有账号？去注册' }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import authApi from '@/api/auth'
import { useRouter } from 'vue-router'
const showPwd = ref(false)   // 控制明文/密文

const router = useRouter()
const isReg = ref(false)
const form = reactive({ username: '', password: '' })

async function submit() {
  if (isReg.value) {
    await authApi.register(form)        // 先注册
    const { data } = await authApi.login(form) // 再登录拿 token
    localStorage.setItem('token', data.access)
  } else {
    const { data } = await authApi.login(form)
    localStorage.setItem('token', data.access)
  }
  router.push('/select')
}
</script>

<style scoped>
.page {
  display: flex;
  height: 100vh;
  font-family: Avenir, Helvetica, Arial, sans-serif;
}
.side-img {
  flex: 1;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-size: 48px;
  font-weight: bold;
  letter-spacing: 4px;
}
.form-box {
  width: 480px;
  padding: 60px 50px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.form-box h1 {
  margin: 0 0 32px;
  font-size: 28px;
  color: #333;
}
.field {
  margin-bottom: 20px;
}
.field label {
  display: block;
  margin-bottom: 6px;
  font-size: 14px;
  color: #666;
}
.field input {
  width: 100%;
  padding: 12px 16px;
  border: 1px solid #d9d9d9;
  border-radius: 6px;
  font-size: 14px;
  transition: border-color 0.2s;
}
.field input:focus {
  outline: none;
  border-color: #667eea;
}
.big-btn {
  width: 100%;
  margin-top: 8px;
  padding: 14px;
  font-size: 16px;
  font-weight: bold;
  color: #fff;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}
.big-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
}
.big-btn:active {
  transform: translateY(0);
}
.tip {
  margin-top: 16px;
  text-align: center;
  font-size: 13px;
  color: #999;
  cursor: pointer;
  transition: color 0.2s;
}
.tip:hover {
  color: #667eea;
}
.pwd-box {
  display: flex;
  align-items: center;
  position: relative;
}
.pwd-box input {
  flex: 1;
  padding-right: 40px; 
}
.eye {
  position: absolute;
  right: 12px;
  font-size: 18px;
  cursor: pointer;
  user-select: none;
}
</style>